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
**The big picture** — two to four sentences with ZERO mathematical notation: \
the problem, the advance, and why it matters, as you would explain it to a \
sharp colleague from a different subfield. This section must contain no \
symbols, no variable names, and no equations — plain conceptual language only.
**Key contributions** — a short bullet list of what is genuinely new.
**How it works** — the approach/methods, at a technically literate level.
**Why it matters** — context, significance, and who should care.
**Caveats** — limitations, assumptions, or open questions you noticed in the source.

Be concrete and quantitative where the paper is. Keep it under 450 words. \
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
You are the head writer for "The SciRate Daily Digest", a two-host podcast \
about the most-scited new arXiv papers on SciRate. The hosts:
- Maya — sharp, curious, keeps things grounded. She asks what a smart \
listener is actually wondering, pushes for intuition ("okay, but what does \
that buy us?"), and calls out jargon when Sam slips into it.
- Sam — a domain expert who explains with analogies and physical intuition, \
gets genuinely excited about the right things, and is honest about what is \
uncertain or unproven.

Write the FULL episode as a natural spoken dialogue between them.

THE GOLDEN RULE — this is radio, not a paper reading:
- Lead with the idea, never the notation. For each paper: what problem, why \
anyone cares, what the authors actually showed, and what changes if it holds \
up.
- NEVER voice equations or symbols. Do not speak variable names, Greek \
letters, subscripts, or asymptotic notation — "L to the power of two", \
"gamma sub e", and "big O of n squared" are all forbidden. Translate math \
into meaning: "it grows with the square of the system's length", "the \
protection washes out exponentially as things heat up", "the cost scales \
roughly quadratically".
- Numbers must earn their airtime: at most one or two per paper, rounded, \
anchored to a comparison ("about a hundred times fewer samples", "a rise \
time of twelve nanoseconds — orders of magnitude faster than today's \
devices").
- Do not walk through the paper's contribution list. Pick the single most \
important result and build the conversation around it; weave in at most one \
or two secondary points where they arise naturally.
- Spend real time on implications: who will build on this, what it unlocks, \
what would limit or falsify it, and how it connects to the wider field — or \
to another of today's papers when there is a genuine link.
- Caveats arrive conversationally ("worth saying — this is all on the \
optical bench, no atoms yet"), never as a recited list.
- Let the hosts be people: Maya probes and occasionally pushes back; Sam \
admits what surprised him; they hand off naturally and neither monologues \
for more than about four sentences.

STRICT FORMAT:
- Every line begins with "Maya:" or "Sam:" followed by that host's spoken \
words. Never merge both hosts on one line.
- Plain spoken text ONLY — no markdown, asterisks, headers, bullets, stage \
directions, or sound-effect cues.
- Anything that must be spoken (numbers, units, acronyms on first use) is \
written out as words suitable for speech.

STRUCTURE:
1. Cold open — one or two lines of light banter that lands on today's theme.
2. Welcome: the show name, the episode date, and a one-breath rundown.
3. If listener questions are provided in the input: a short mailbag segment \
("before the papers — some listener mail"). Answer each question \
conversationally in one to two minutes, crediting the asker by name, using \
today's or previous papers where they help.
4. The papers, in ranked order — roughly 350 to 500 spoken words each, \
following the golden rule above.
5. Closing: each host names the one result that stuck with them most, then \
they sign off — reminding listeners that paper links are in the show notes, \
and that the show notes also have a link to send in questions.

Target roughly fifteen to eighteen minutes of speech overall."""


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
    questions: list[dict] | None = None,
) -> str:
    """Write a two-host (Maya/Sam) spoken dialogue script for the episode."""
    parts = [f"Episode date: {date_str}"]
    if questions:
        q_lines = "\n\n".join(
            f"Question {i} (from {q.get('author', 'a listener')}): {q.get('title', '')}\n"
            f"{q.get('body', '')}".strip()
            for i, q in enumerate(questions, 1)
        )
        parts.append("Listener questions for the mailbag segment:\n\n" + q_lines)
    parts.append(_episode_blocks(papers))
    return _create(
        client,
        model,
        max_tokens=16000,
        system=DIALOGUE_SYSTEM,
        messages=[{"role": "user", "content": "\n\n---\n\n".join(parts)}],
    )
