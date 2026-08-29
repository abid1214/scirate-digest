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
Do not restate the title or authors.

Ignore the paper's authorship and tooling disclosures entirely — whether \
the authors used AI, a language model, or any other tool to draft, ideate, \
or check the work is not part of its scientific content. Never mention it, \
including in the caveats."""

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
- Never discuss how a paper was written or what tools its authors used. \
AI or language-model assistance disclosures are off-topic: do not mention \
them for a single paper, and never draw a trend across papers from them. \
Talk about the results, not the authorship process.
- Let the hosts be people: Maya probes and occasionally pushes back; Sam \
admits what surprised him; they hand off naturally.
- PACING (hard limits): no single speaking turn may run longer than about a \
minute of speech — roughly one hundred and twenty words. Most turns should \
run three to six sentences: substantial enough to develop one idea, never a \
monologue. Avoid rapid one-line ping-pong — keep the whole episode to at \
most about seventy speaking turns. In the mailbag, each host's total \
contribution to a given question stays under a minute, so a question is \
fully answered in under two minutes of back-and-forth.

CONTINUITY — the show has a past, and the listener remembers it:
- If the input includes a PREVIOUSLY ON THE SHOW section, those episodes \
already aired. Reach for a callback when today's paper genuinely extends, \
contradicts, or echoes one of them ("this is the other side of the decoder \
result we covered Monday") — at most one or two per episode, and only when \
the link is real.
- You know those papers only by title and a one-line gist. Never invent \
detail about them, never re-review them, and never reference an episode or \
paper that is not listed.
- Do not open or close today's episode the way the recent ones did, and do \
not reuse their framing devices. Fresh angle every day.

VARIETY AND DEPTH — five papers must never sound like one conversation \
repeated five times:
- Give each paper segment a different conversational shape. Rotate entry \
angles across the episode: open one segment from the concrete stake, one \
from a puzzle or apparent contradiction, one from the history of the \
problem, one from the single surprising result, one from a genuine link to \
another paper or a listener question. Never open two consecutive segments \
the same way.
- Ban stock phrases and repeated beats: never reuse a transition line, and \
words like "fascinating", "exciting", "the key takeaway", or "at the end \
of the day" may each appear at most once per episode. Maya's pushback must \
be a fresh, substantive objection each time — a real test, counterexample, \
or cost — never a catchphrase.
- Never have one host restate what the other just said in different words. \
Every reply must add something new: a consequence, an objection, a sharper \
example, or a correction.
- A good review, not a summary. By the end of each segment the listener \
should know: the specific claim; the evidence and how strong it is (proof, \
simulation, or experiment, and at what scale); how it sits against what \
came before; and the hosts' honest verdict — who should actually read this \
and what they would watch for next. Ground each segment in at least two \
concrete specifics unique to that paper (a named technique, a real number, \
a stated limitation). Depth beats breadth.

STRICT FORMAT:
- Every line begins with "Maya:" or "Sam:" followed by that host's spoken \
words. Never merge both hosts on one line.
- Between major segments — after the welcome, after the mailbag (if any), \
between each paper discussion, and before the closing — output a line \
containing exactly [BREAK] and nothing else. It is an audio cue for theme \
music, never spoken, and it is the ONLY permitted non-dialogue line. Wrap \
each segment up cleanly before a [BREAK] (no mid-thought cuts) and re-enter \
fresh after it, the way radio hosts return from a bumper.
- Plain spoken text ONLY — no markdown, asterisks, headers, bullets, stage \
directions, or sound-effect cues (other than the [BREAK] lines).
- Anything that must be spoken (numbers, units, acronyms on first use) is \
written out as words suitable for speech.

STRUCTURE:
1. Cold open — one or two lines of light banter that lands on today's theme.
2. Welcome: the show name, the episode date, and a one-breath rundown.
3. If listener questions are provided in the input: a short mailbag segment \
("before the papers — some listener mail"). Answer each question \
conversationally in one to two minutes, crediting the asker by name, using \
today's papers — or ones listed under PREVIOUSLY ON THE SHOW — where they \
help.
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


def _recent_block(recent: list[dict]) -> str:
    """Compact record of the last few episodes: titles and one line each."""
    lines = []
    for ep in recent:
        lines.append(f"{ep.get('date', '')}:")
        for p in ep.get("papers", []):
            takeaway = p.get("takeaway") or ""
            lines.append(
                f"  - {p.get('title', '').strip()}"
                + (f" — {takeaway}" if takeaway else "")
            )
    return "\n".join(lines)


def write_dialogue_script(
    client: anthropic.Anthropic,
    papers: list[Paper],
    date_str: str,
    model: str = DEFAULT_MODEL,
    questions: list[dict] | None = None,
    recent: list[dict] | None = None,
) -> str:
    """Write a two-host (Maya/Sam) spoken dialogue script for the episode."""
    parts = [f"Episode date: {date_str}"]
    if recent:
        parts.append(
            "PREVIOUSLY ON THE SHOW — episodes already aired, most recent "
            "first. You may refer back to any of these; do not re-review "
            "them, and never claim to have covered anything not listed "
            "here:\n\n" + _recent_block(recent)
        )
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
