"""Fetch paper metadata and full LaTeX source from arXiv.

Metadata comes from the arXiv Atom API; the paper body comes from the
``/e-print/<id>`` endpoint, which serves the submission source — usually a
gzipped tarball of ``.tex`` files, sometimes a single gzipped ``.tex`` file,
and occasionally a bare PDF (in which case no source text is available and
the digest falls back to the abstract).
"""

from __future__ import annotations

import gzip
import io
import logging
import re
import tarfile
import time
import xml.etree.ElementTree as ET

import requests

from .models import Paper

log = logging.getLogger(__name__)

API_URL = "https://export.arxiv.org/api/query"
EPRINT_URL = "https://arxiv.org/e-print/{uid}"
USER_AGENT = "scirate-digest/0.1 (github.com/abid1214/scirate-digest)"
ATOM = "{http://www.w3.org/2005/Atom}"

# Courtesy delay between arXiv requests, per their API usage guidelines.
REQUEST_DELAY_S = 3.0


def _get_with_retry(url: str, *, params: dict | None = None, attempts: int = 5) -> requests.Response:
    """GET with backoff on 429/5xx — arXiv rate-limits shared IPs readily."""
    delay = 5.0
    for attempt in range(attempts):
        try:
            resp = requests.get(
                url, params=params, headers={"User-Agent": USER_AGENT}, timeout=120
            )
            if resp.status_code in (429, 500, 502, 503, 504) and attempt < attempts - 1:
                retry_after = resp.headers.get("Retry-After")
                wait = float(retry_after) if retry_after else delay
                log.info("arXiv returned %d; retrying in %.0fs", resp.status_code, wait)
                time.sleep(wait)
                delay *= 2
                continue
            resp.raise_for_status()
            return resp
        except requests.ConnectionError:
            if attempt == attempts - 1:
                raise
            time.sleep(delay)
            delay *= 2
    raise RuntimeError("unreachable")


def fetch_metadata(papers: list[Paper]) -> None:
    """Fill in title/authors/abstract on each paper from the arXiv API."""
    if not papers:
        return
    resp = _get_with_retry(
        API_URL,
        params={"id_list": ",".join(p.uid for p in papers), "max_results": len(papers)},
    )
    by_uid = {p.uid: p for p in papers}
    for uid, title, authors, abstract in parse_atom(resp.text):
        paper = by_uid.get(uid)
        if paper is not None:
            paper.title = title
            paper.authors = authors
            paper.abstract = abstract
    missing = [p.uid for p in papers if not p.title]
    if missing:
        log.warning("arXiv API returned no metadata for: %s", ", ".join(missing))


def parse_atom(xml_text: str) -> list[tuple[str, str, list[str], str]]:
    """Parse an arXiv Atom feed into (uid, title, authors, abstract) tuples."""
    out = []
    root = ET.fromstring(xml_text)
    for entry in root.findall(f"{ATOM}entry"):
        raw_id = entry.findtext(f"{ATOM}id", "")
        # e.g. http://arxiv.org/abs/2408.12345v2 -> 2408.12345
        uid = re.sub(r"v\d+$", "", raw_id.rsplit("/abs/", 1)[-1])
        title = _squash(entry.findtext(f"{ATOM}title", ""))
        abstract = _squash(entry.findtext(f"{ATOM}summary", ""))
        authors = [
            _squash(a.findtext(f"{ATOM}name", ""))
            for a in entry.findall(f"{ATOM}author")
        ]
        if uid:
            out.append((uid, title, authors, abstract))
    return out


def _squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def download_source(uid: str) -> bytes:
    return _get_with_retry(EPRINT_URL.format(uid=uid)).content


def fetch_sources(papers: list[Paper], max_chars: int = 60_000) -> None:
    """Download and extract LaTeX source text for each paper, politely paced."""
    for i, paper in enumerate(papers):
        if i:
            time.sleep(REQUEST_DELAY_S)
        try:
            blob = download_source(paper.uid)
            paper.source_text = extract_source_text(blob, max_chars=max_chars)
            if paper.source_text is None:
                log.info("%s: source is not LaTeX (PDF-only submission?)", paper.uid)
        except Exception as exc:  # a single bad paper must not sink the digest
            log.warning("%s: failed to fetch/extract source: %s", paper.uid, exc)
            paper.source_text = None


def extract_source_text(blob: bytes, max_chars: int = 60_000) -> str | None:
    """Turn an e-print blob into readable LaTeX text, or None if not LaTeX."""
    if blob.startswith(b"%PDF"):
        return None
    if blob[:2] == b"\x1f\x8b":
        blob = gzip.decompress(blob)

    tex_files: list[tuple[str, str]] = []
    try:
        with tarfile.open(fileobj=io.BytesIO(blob)) as tar:
            for member in tar.getmembers():
                if not member.isfile() or not member.name.lower().endswith(
                    (".tex", ".ltx")
                ):
                    continue
                fh = tar.extractfile(member)
                if fh is None:
                    continue
                tex_files.append(
                    (member.name, fh.read().decode("utf-8", errors="replace"))
                )
    except tarfile.TarError:
        # Not a tarball: single-file source (a lone gzipped .tex, or raw text).
        text = blob.decode("utf-8", errors="replace")
        if "\\documentclass" in text or "\\begin{document}" in text:
            tex_files.append(("main.tex", text))

    if not tex_files:
        return None

    # Main file first (the one with \begin{document}), then the rest by size,
    # so \input'd chapters land after the introduction.
    mains = [t for t in tex_files if "\\begin{document}" in t[1]]
    rest = sorted(
        (t for t in tex_files if t not in mains), key=lambda t: -len(t[1])
    )
    ordered = mains + rest

    combined = "\n\n".join(
        f"%% ==== file: {name} ====\n{latex_to_text(body)}" for name, body in ordered
    )
    if len(combined) > max_chars:
        combined = combined[:max_chars] + "\n\n[... source truncated ...]"
    return combined


def latex_to_text(tex: str) -> str:
    """Lightly clean LaTeX for LLM consumption: drop comments, preamble noise
    and bibliography, keep the semantic body (including math) intact."""
    # Strip comments (a % not preceded by a backslash, to end of line).
    tex = re.sub(r"(?<!\\)%.*", "", tex)
    # Keep only the document body when present.
    m = re.search(r"\\begin\{document\}(.*?)(\\end\{document\}|$)", tex, re.S)
    if m:
        tex = m.group(1)
    # Drop bibliographies and figure graphics (captions survive).
    tex = re.sub(r"\\begin\{thebibliography\}.*?\\end\{thebibliography\}", "", tex, flags=re.S)
    tex = re.sub(r"\\bibliography\{[^}]*\}", "", tex)
    tex = re.sub(r"\\includegraphics(\[[^\]]*\])?\{[^}]*\}", "", tex)
    # Collapse runs of blank lines.
    tex = re.sub(r"\n{3,}", "\n\n", tex)
    return tex.strip()
