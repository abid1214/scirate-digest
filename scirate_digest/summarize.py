"""Generate per-paper executive summaries and the podcast script with Claude."""

from __future__ import annotations

import logging

import anthropic

from .models import Paper

log = logging.getLogger(__name__)

DEFAULT_MODEL = "claude-opus-5"

PAPER_SYSTEM = """\
You are a senior research scientist writing a daily digest of new arXiv \
papers for expert colleagues. You are given a paper's metadata and its LaTeX \
source (possibly truncated). Read the actual content — methods, results, \
proofs, experiments — not just the abstract.

Respond in markdown with exactly these sections:
**TL;DR** — two or three sentences capturing the core result.
**Key contributions** — a short bullet list of what is genuinely new.
**How it works** — the approach/methods, at a technically literate level.
**Why it matters** — context, significance, and who should care.
**Caveats** — limitations, assumptions, or open questions you noticed in the source.

Be concrete and quantitative where the paper is. Keep it under 400 words. \
Do not restate the title or authors."""

SCRIPT_SYSTEM = """\
You are the writer and host of "The SciRate Daily Digest", a podcast covering \
the most-scited new arXiv papers on SciRate. You are given today's papers \
with executive summaries. Write the complete narration script for a single \
host.

Requirements:
- Output plain narration text ONLY: no markdown, no headers, no bullet \
points, no asterisks, no stage directions, no sound-effect cues.
- Spell out symbols and math in words (say "order n squared", not "O(n^2)").
- Open with a short welcome that gives the episode date and a one-breath \
rundown of the themes in today's papers.
- Then cover each paper in ranked order: state its rank, title, and (first \
author plus "and colleagues", or all authors if three or fewer), then give an \
engaging, technically substantive treatment of what it shows, how, and why it \
matters — roughly 150 to 250 spoken words per paper.
- Use natural spoken transitions between papers.
- Close by naming the top paper once more and signing off, reminding \
listeners that links are in the show notes.
- Target roughly 15 minutes of speech overall."""


DIALOGUE_SYSTEM = """\
You are scripting a two-host podcast, "The SciRate Daily Digest", covering the \
most-scited new arXiv papers on SciRate. The hosts are Maya (a sharp, curious \
generalist who asks the questions a smart listener would) and Sam (a domain \
expert who explains clearly and precisely). You are given today's papers with \
executive summaries.

Write the FULL episode as a natural spoken dialogue between Maya and Sam.

Strict formatting:
- Every line begins with either "Maya:" or "Sam:" followed by that host's \
spoken words. Alternate naturally; never merge both hosts on one line.
- Plain spoken text ONLY — no markdown, asterisks, headers, bullet points, \
stage directions, or sound-effect cues.
- Spell out symbols and math in words (say "order n squared", not "O(n^2)").

Content:
- Open with a short back-and-forth welcome that names the episode date and \
previews the day's themes.
- Cover each paper in ranked order: name its rank and title, then have Maya \
and Sam genuinely discuss what it shows, how it works, and why it matters — \
real questions and clear explanations, roughly 180 to 260 spoken words per \
paper.
- Use natural spoken transitions between papers.
- Close by naming the top paper once more and signing off, reminding \
listeners that links are in the show notes.
Target roughly 15 minutes of speech overall."""


def make_client() -> anthropic.Anthropic:
    # Credentials resolve from the environment (ANTHROPIC_API_KEY etc.).
    return anthropic.Anthropic(max_retries=4)


def _create(client: anthropic.Anthropic, model: str, **kwargs) -> str:
    """Call the Messages API; on Opus 5 / Fable 5, enable server-side refusal
    fallbacks so a safety decline falls back to another model instead of
    dropping a paper from the digest."""
    response = None
    if model.startswith(("claude-opus-5", "claude-fable-5")):
        try:
            response = client.beta.messages.create(
                model=model,
                betas=["server-side-fallback-2026-07-01"],
                fallbacks="default",
                **kwargs,
            )
        except anthropic.BadRequestError:
            log.info("Server-side fallbacks unavailable; retrying without them")
    if response is None:
        response = client.messages.create(model=model, **kwargs)

    if response.stop_reason == "refusal":
        detail = getattr(response, "stop_details", None)
        raise RuntimeError(
            f"Model declined to respond ({getattr(detail, 'category', None)}): "
            f"{getattr(detail, 'explanation', '')}"
        )
    return "\n\n".join(b.text for b in response.content if b.type == "text").strip()


def summarize_paper(client: anthropic.Anthropic, paper: Paper, model: str = DEFAULT_MODEL) -> str:
    parts = [
        f"Title: {paper.title or '(unknown)'}",
        f"arXiv ID: {paper.uid}",
        f"Authors: {', '.join(paper.authors) or '(unknown)'}",
        f"Scites on SciRate: {paper.scites if paper.scites is not None else 'n/a'}",
        f"Abstract: {paper.abstract or '(unavailable)'}",
    ]
    if paper.source_text:
        parts.append(f"LaTeX source:\n\n{paper.source_text}")
    else:
        parts.append(
            "LaTeX source: unavailable (PDF-only submission) — analyze from "
            "the abstract and say so in the caveats."
        )
    return _create(
        client,
        model,
        max_tokens=4096,
        system=PAPER_SYSTEM,
        messages=[{"role": "user", "content": "\n\n".join(parts)}],
    )


def write_podcast_script(
    client: anthropic.Anthropic,
    papers: list[Paper],
    date_str: str,
    model: str = DEFAULT_MODEL,
) -> str:
    blocks = []
    for rank, p in enumerate(papers, 1):
        blocks.append(
            f"## Rank {rank} ({p.scites if p.scites is not None else 'n/a'} scites)\n"
            f"Title: {p.title}\n"
            f"Authors: {', '.join(p.authors)}\n"
            f"arXiv: {p.uid}\n\n"
            f"Executive summary:\n{p.summary or p.abstract}"
        )
    user = f"Episode date: {date_str}\n\n" + "\n\n---\n\n".join(blocks)
    return _create(
        client,
        model,
        max_tokens=16000,
        system=SCRIPT_SYSTEM,
        messages=[{"role": "user", "content": user}],
    )


def _episode_blocks(papers: list[Paper]) -> str:
    blocks = []
    for rank, p in enumerate(papers, 1):
        blocks.append(
            f"## Rank {rank} ({p.scites if p.scites is not None else 'n/a'} scites)\n"
            f"Title: {p.title}\n"
            f"Authors: {', '.join(p.authors)}\n"
            f"arXiv: {p.uid}\n\n"
            f"Executive summary:\n{p.summary or p.abstract}"
        )
    return "\n\n---\n\n".join(blocks)


def write_dialogue_script(
    client: anthropic.Anthropic,
    papers: list[Paper],
    date_str: str,
    model: str = DEFAULT_MODEL,
) -> str:
    """Write a two-host (Maya/Sam) spoken dialogue script for the episode."""
    user = f"Episode date: {date_str}\n\n" + _episode_blocks(papers)
    return _create(
        client,
        model,
        max_tokens=16000,
        system=DIALOGUE_SYSTEM,
        messages=[{"role": "user", "content": user}],
    )
