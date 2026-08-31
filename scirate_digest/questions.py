"""Listener Q&A via GitHub issues.

Open an issue whose title starts with "Q:" (or that carries a ``question``
label) and the hosts answer it in the next episode's mailbag segment. After
the episode publishes, the workflow closes each answered issue with a link
to that day's episode.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
from pathlib import Path

import requests

log = logging.getLogger(__name__)

REPO = "abid1214/scirate-digest"
API = "https://api.github.com/repos/{repo}"
MAX_QUESTIONS = 2
MAX_BODY_CHARS = 1200


def _headers(token: str | None) -> dict:
    h = {"Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def is_question(issue: dict) -> bool:
    if "pull_request" in issue:
        return False
    if issue.get("title", "").strip().lower().startswith("q:"):
        return True
    labels = {l.get("name", "").lower() for l in issue.get("labels", [])}
    return "question" in labels


def parse_issues(issues: list[dict]) -> list[dict]:
    out = []
    for issue in issues:
        if not is_question(issue):
            continue
        title = issue.get("title", "").strip()
        if title.lower().startswith("q:"):
            title = title[2:].strip()
        out.append({
            "number": issue["number"],
            "title": title,
            "body": (issue.get("body") or "")[:MAX_BODY_CHARS].strip(),
            "author": issue.get("user", {}).get("login", "a listener"),
        })
    return out[:MAX_QUESTIONS]


def fetch_open_questions(repo: str = REPO, token: str | None = None) -> list[dict]:
    token = token or os.environ.get("GITHUB_TOKEN")
    resp = requests.get(
        API.format(repo=repo) + "/issues",
        params={"state": "open", "per_page": 30, "sort": "created", "direction": "asc"},
        headers=_headers(token),
        timeout=60,
    )
    resp.raise_for_status()
    return parse_issues(resp.json())



def _distinctive(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]{5,}", text.lower())}


def answered_in_script(script: str, question: dict) -> bool:
    """Did the episode actually answer this question?

    The script is told to credit the asker by name, so their handle appearing
    is the primary signal; failing that, most of the question's distinctive
    words showing up counts. Anything else is treated as unanswered, which
    keeps the issue open for a later episode instead of silently closing a
    question the hosts never reached."""
    low = script.lower()
    author = (question.get("author") or "").strip().lower()
    if author and author != "a listener" and author in low:
        return True
    words = _distinctive(question.get("title", ""))
    if not words:
        return False
    hits = sum(1 for w in words if w in low)
    return hits >= max(2, int(0.6 * len(words)))


def filter_answered(script: str, questions: list[dict]) -> list[dict]:
    return [q for q in questions if answered_in_script(script, q)]


def close_answered(questions: list[dict], date: str, repo: str = REPO,
                   token: str | None = None) -> None:
    token = token or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN required to close answered questions")
    episode_url = f"https://github.com/{repo}/releases/tag/digest-{date}"
    for q in questions:
        base = API.format(repo=repo) + f"/issues/{q['number']}"
        body = (
            f"🎙️ Maya and Sam answered this in the mailbag segment of the "
            f"[{date} episode]({episode_url}). Thanks for the question!"
        )
        requests.post(base + "/comments", json={"body": body},
                      headers=_headers(token), timeout=60).raise_for_status()
        requests.patch(base, json={"state": "closed"},
                       headers=_headers(token), timeout=60).raise_for_status()
        log.info("Closed answered question #%d", q["number"])


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO)
    ap = argparse.ArgumentParser(description="Listener Q&A bookkeeping.")
    ap.add_argument("--close-file", type=Path,
                    help="questions.json written by the digest run")
    ap.add_argument("--script", type=Path,
                    help="podcast_script.txt; only questions the episode "
                         "actually answered are closed")
    ap.add_argument("--date", help="episode date YYYY-MM-DD (for --close-file)")
    args = ap.parse_args(argv)

    if args.close_file:
        if not args.close_file.exists():
            print("no questions file; nothing to close")
            return 0
        questions = json.loads(args.close_file.read_text())
        if not questions:
            print("no questions were queued; nothing to close")
            return 0
        if args.script and args.script.exists():
            script = args.script.read_text()
            answered = filter_answered(script, questions)
            skipped = [q for q in questions if q not in answered]
            for q in skipped:
                print(f"#{q['number']} was not answered on air; leaving it open")
        else:
            answered = questions
        if not answered:
            print("no questions were answered; nothing to close")
            return 0
        close_answered(answered, args.date)
        print(f"closed {len(answered)} answered question(s)")
    else:
        for q in fetch_open_questions():
            print(f"#{q['number']} (from {q['author']}): {q['title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
