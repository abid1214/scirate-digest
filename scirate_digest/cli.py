"""Command-line entry point: scrape → fetch sources → summarize → podcast."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import os
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
    p.add_argument("--top", type=int, default=5, help="number of papers (default 5)")
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
    p.add_argument(
        "--voice-engine", choices=["auto", "edge", "gemini"], default="auto",
        help="TTS backend: 'gemini' = two-host dialogue, 'edge' = single "
             "narrator, 'auto' = gemini if GEMINI_API_KEY is set else edge",
    )
    p.add_argument("--voice", default=None, help="edge-tts voice name (edge engine)")
    p.add_argument(
        "--gemini-model", default=None,
        help="Gemini TTS model ID (default gemini-2.5-flash-preview-tts)",
    )
    p.add_argument(
        "--max-source-chars", type=int, default=60_000,
        help="per-paper cap on extracted LaTeX characters (default 60000)",
    )
    p.add_argument(
        "--output-dir", type=Path, default=Path("output"),
        help="base output directory (default ./output)",
    )
    p.add_argument("--date", default=None, help="episode date, YYYY-MM-DD (default today)")
    p.add_argument(
        "--allow-repeats", action="store_true",
        help="do not filter out papers already discussed in past episodes",
    )
    p.add_argument("--skip-audio", action="store_true", help="stop after the script; no TTS")
    p.add_argument(
        "--skip-summaries", action="store_true",
        help="scrape and fetch sources only; no Claude API calls (for testing)",
    )
    return p


def run(args: argparse.Namespace) -> Path:
    if not args.skip_summaries and not (
        os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")
    ):
        raise RuntimeError(
            "ANTHROPIC_API_KEY is not set. Add it as a repository secret "
            "(Settings → Secrets and variables → Actions) or export it locally, "
            "or run with --skip-summaries."
        )

    date_str = args.date or dt.date.today().isoformat()
    out_dir = args.output_dir / date_str
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.ids:
        papers = [Paper(uid=uid) for uid in args.ids[: args.top]]
        log.info("Using %d manually supplied arXiv IDs", len(papers))
    else:
        # Scrape a larger ranked pool so that papers already covered in past
        # episodes can be skipped while still filling the top-N with fresh
        # ones (hot papers stay in SciRate's ranking for several days).
        pool_size = max(args.top * 6, 30)
        log.info("Scraping SciRate for the top %d papers…", pool_size)
        papers = scrape.fetch_top_papers(
            count=pool_size, range_days=args.range_days, category=args.category
        )
        if not args.allow_repeats:
            seen = load_discussed_uids(exclude_date=date_str)
            fresh = [p for p in papers if p.uid not in seen]
            skipped = [p.uid for p in papers if p.uid in seen]
            if skipped:
                log.info(
                    "Skipping %d already-discussed paper(s): %s",
                    len(skipped), ", ".join(skipped[:10]),
                )
            papers = fresh
        papers = papers[: args.top]
        if not papers:
            raise RuntimeError(
                "No papers left after filtering out previously discussed ones "
                "— rerun with --allow-repeats or a wider --range"
            )
        if len(papers) < args.top:
            log.warning(
                "Only %d fresh paper(s) available today (wanted %d)",
                len(papers), args.top,
            )
    log.info("Papers: %s", ", ".join(p.uid for p in papers))

    log.info("Fetching metadata from the arXiv API…")
    try:
        arxiv_source.fetch_metadata(papers)
    except Exception as exc:
        log.warning("arXiv metadata fetch failed (%s); continuing without it", exc)

    log.info("Downloading and extracting arXiv source tarballs…")
    arxiv_source.fetch_sources(papers, max_chars=args.max_source_chars)

    engine = _resolve_engine(args)

    if not args.skip_summaries:
        client = summarize.make_client()
        for i, paper in enumerate(papers, 1):
            log.info("[%d/%d] Summarizing %s — %s", i, len(papers), paper.uid, paper.title)
            try:
                paper.summary = summarize.summarize_paper(client, paper, model=args.model)
            except Exception as exc:
                log.error("%s: summarization failed: %s", paper.uid, exc)
                paper.summary = f"*Summary unavailable ({exc}).*\n\n{paper.abstract}"

        questions: list[dict] = []
        try:
            from . import questions as questions_mod

            questions = questions_mod.fetch_open_questions()
            if questions:
                log.info("Answering %d listener question(s) in the mailbag", len(questions))
        except Exception as exc:
            log.warning("Could not fetch listener questions (%s); skipping mailbag", exc)
        (out_dir / "questions.json").write_text(json.dumps(questions, indent=2))

        log.info("Writing podcast script (%s)…", "two-host dialogue" if engine == "gemini" else "narration")
        if engine == "gemini":
            script = summarize.write_dialogue_script(
                client, papers, date_str, model=args.model, questions=questions
            )
        else:
            script = summarize.write_podcast_script(client, papers, date_str, model=args.model)
        (out_dir / "podcast_script.txt").write_text(script)

    (out_dir / "papers.json").write_text(
        json.dumps([p.to_dict() for p in papers], indent=2)
    )
    write_digest_markdown(papers, date_str, out_dir / "digest.md")
    log.info("Wrote %s", out_dir / "digest.md")

    if not args.skip_summaries and not args.skip_audio:
        _render_audio(
            script_text=(out_dir / "podcast_script.txt").read_text(),
            mp3_path=out_dir / "digest.mp3",
            out_dir=out_dir,
            date_str=date_str,
            engine=engine,
            gemini_model=args.gemini_model,
            edge_voice=args.voice,
        )

    return out_dir



def _render_audio(
    script_text: str,
    mp3_path: Path,
    out_dir: Path,
    date_str: str,
    engine: str,
    gemini_model: str | None = None,
    edge_voice: str | None = None,
) -> dict:
    """Synthesize the episode, falling back if Gemini fails, and record which
    path actually produced the audio.

    The returned metadata is also written to ``audio_meta.json`` beside the
    episode and committed with it, so a finished run can be audited without
    reading CI logs (a late/duplicate run once silently replaced good Gemini
    audio with fallback voices and nothing in the repo showed it)."""
    log.info("Synthesizing podcast audio via %s…", engine)
    mp3 = None
    rendered_with = None
    model_used = gemini_model or None
    if engine == "gemini":
        from . import gemini_tts

        model_used = gemini_model or gemini_tts.DEFAULT_MODEL
        try:
            mp3 = gemini_tts.synthesize_dialogue(script_text, mp3_path, model=model_used)
            rendered_with = "gemini-per-turn"
        except Exception as exc:
            # Never lose the episode to a Gemini hiccup. First fallback keeps
            # two hosts by voicing each turn with its own edge voice; last
            # resort is a single narrator.
            log.error("Gemini TTS failed (%s); trying two-voice edge fallback", exc)
            from . import tts

            try:
                mp3 = tts.synthesize_dialogue(script_text, mp3_path)
                rendered_with = "edge-two-voice"
            except Exception as exc2:
                log.error("Two-voice fallback failed (%s); single narrator", exc2)
                script_text = _dialogue_to_narration(script_text)
    if mp3 is None:
        from . import tts  # imported lazily so --skip-audio needs no edge-tts

        mp3 = tts.synthesize(script_text, mp3_path, voice=edge_voice or tts.DEFAULT_VOICE)
        rendered_with = rendered_with or ("edge-narrator" if engine == "gemini" else "edge")

    meta = {
        "date": date_str,
        "rendered_with": rendered_with,
        "model": model_used,
        "turns": sum(
            1 for line in script_text.splitlines()
            if line.split(":", 1)[0].strip() in ("Maya", "Sam")
        ),
        "mp3_bytes": mp3.stat().st_size,
    }
    log.info("Wrote %s (%.1f MB) via %s", mp3, meta["mp3_bytes"] / 1e6, rendered_with)
    (out_dir / "audio_meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    return meta


def load_discussed_uids(
    digests_dir: Path = Path("digests"), exclude_date: str | None = None
) -> set[str]:
    """arXiv IDs covered by past episodes, from the committed digest history.

    ``exclude_date`` keeps a same-day re-render from treating its own earlier
    output as history (which would swap in five different papers)."""
    seen: set[str] = set()
    if not digests_dir.is_dir():
        return seen
    for pj in sorted(digests_dir.glob("*/papers.json")):
        if exclude_date and pj.parent.name == exclude_date:
            continue
        try:
            for p in json.loads(pj.read_text()):
                uid = p.get("uid")
                if uid:
                    seen.add(uid)
        except (json.JSONDecodeError, OSError) as exc:
            log.warning("Could not read %s (%s); ignoring it", pj, exc)
    return seen


def _resolve_engine(args: argparse.Namespace) -> str:
    """Pick the TTS engine.

    Default is edge: its neural voices are deterministic, so Maya and Sam
    sound identical in every turn of every episode. Gemini's TTS re-generates
    the voice on each request, and in practice it never held a stable pair —
    whole-conversation chunks drifted across an episode, and per-turn requests
    varied turn to turn (measured: the female host smearing 130-180 Hz into
    the male range). Set VOICE_ENGINE=gemini (or --voice-engine gemini) to
    opt back in."""
    if args.voice_engine != "auto":
        return args.voice_engine
    env = (os.environ.get("VOICE_ENGINE") or "").strip().lower()
    if env in ("edge", "gemini"):
        return env
    return "edge"


def _dialogue_to_narration(script: str) -> str:
    """Strip 'Maya:'/'Sam:' speaker labels (and [BREAK] audio cues) so a
    single narrator can read it; breaks become paragraph pauses."""
    import re

    out = []
    for line in script.splitlines():
        if re.match(r"^\s*\[BREAK\]\s*$", line, re.IGNORECASE):
            out.append("")
            continue
        out.append(re.sub(r"^\s*[A-Za-z][\w .'-]*?:\s*", "", line))
    return "\n".join(out)


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
