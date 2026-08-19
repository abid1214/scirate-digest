"""Command-line entry point: scrape → fetch sources → summarize → podcast."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import sys
from pathlib import Path

from . import arxiv_source, scrape, summarize
from .models import Paper

log = logging.getLogger("scirate_digest")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="scirate-digest",
        description="Daily audio-podcast digest of the top papers on SciRate.",
    )
    p.add_argument("--top", type=int, default=10, help="number of papers (default 10)")
    p.add_argument(
        "--range", type=int, default=1, dest="range_days",
        help="SciRate ranking window in days (default 1)",
    )
    p.add_argument(
        "--category", default=None,
        help="restrict to an arXiv category feed on SciRate, e.g. quant-ph",
    )
    p.add_argument(
        "--ids", nargs="*", default=None,
        help="skip scraping and digest these arXiv IDs instead",
    )
    p.add_argument("--model", default=summarize.DEFAULT_MODEL, help="Claude model ID")
    p.add_argument("--voice", default=None, help="edge-tts voice name")
    p.add_argument(
        "--max-source-chars", type=int, default=60_000,
        help="per-paper cap on extracted LaTeX characters (default 60000)",
    )
    p.add_argument(
        "--output-dir", type=Path, default=Path("output"),
        help="base output directory (default ./output)",
    )
    p.add_argument("--date", default=None, help="episode date, YYYY-MM-DD (default today)")
    p.add_argument("--skip-audio", action="store_true", help="stop after the script; no TTS")
    p.add_argument(
        "--skip-summaries", action="store_true",
        help="scrape and fetch sources only; no Claude API calls (for testing)",
    )
    return p


def run(args: argparse.Namespace) -> Path:
    date_str = args.date or dt.date.today().isoformat()
    out_dir = args.output_dir / date_str
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.ids:
        papers = [Paper(uid=uid) for uid in args.ids[: args.top]]
        log.info("Using %d manually supplied arXiv IDs", len(papers))
    else:
        log.info("Scraping SciRate for the top %d papers…", args.top)
        papers = scrape.fetch_top_papers(
            count=args.top, range_days=args.range_days, category=args.category
        )
    log.info("Papers: %s", ", ".join(p.uid for p in papers))

    log.info("Fetching metadata from the arXiv API…")
    try:
        arxiv_source.fetch_metadata(papers)
    except Exception as exc:
        log.warning("arXiv metadata fetch failed (%s); continuing without it", exc)

    log.info("Downloading and extracting arXiv source tarballs…")
    arxiv_source.fetch_sources(papers, max_chars=args.max_source_chars)

    if not args.skip_summaries:
        client = summarize.make_client()
        for i, paper in enumerate(papers, 1):
            log.info("[%d/%d] Summarizing %s — %s", i, len(papers), paper.uid, paper.title)
            try:
                paper.summary = summarize.summarize_paper(client, paper, model=args.model)
            except Exception as exc:
                log.error("%s: summarization failed: %s", paper.uid, exc)
                paper.summary = f"*Summary unavailable ({exc}).*\n\n{paper.abstract}"

        log.info("Writing podcast script…")
        script = summarize.write_podcast_script(client, papers, date_str, model=args.model)
        (out_dir / "podcast_script.txt").write_text(script)

    (out_dir / "papers.json").write_text(
        json.dumps([p.to_dict() for p in papers], indent=2)
    )
    write_digest_markdown(papers, date_str, out_dir / "digest.md")
    log.info("Wrote %s", out_dir / "digest.md")

    if not args.skip_summaries and not args.skip_audio:
        from . import tts  # imported lazily so --skip-audio needs no edge-tts

        log.info("Synthesizing podcast audio…")
        voice = args.voice or tts.DEFAULT_VOICE
        mp3 = tts.synthesize((out_dir / "podcast_script.txt").read_text(), out_dir / "digest.mp3", voice=voice)
        log.info("Wrote %s (%.1f MB)", mp3, mp3.stat().st_size / 1e6)

    return out_dir


def write_digest_markdown(papers: list[Paper], date_str: str, path: Path) -> None:
    lines = [
        f"# SciRate Daily Digest — {date_str}",
        "",
        f"The top {len(papers)} papers on [SciRate](https://scirate.com/) today.",
        "",
    ]
    for rank, p in enumerate(papers, 1):
        scites = f" · {p.scites} scites" if p.scites is not None else ""
        authors = ", ".join(p.authors[:8]) + (" et al." if len(p.authors) > 8 else "")
        lines += [
            f"## {rank}. {p.title or p.uid}",
            "",
            f"[arXiv:{p.uid}]({p.abs_url}) · [SciRate]({p.scirate_url}){scites}",
            "",
            f"*{authors}*" if authors else "",
            "",
            p.summary or p.abstract or "",
            "",
        ]
    path.write_text("\n".join(lines))


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    args = build_parser().parse_args(argv)
    try:
        run(args)
    except Exception as exc:
        log.error("Digest failed: %s", exc)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
