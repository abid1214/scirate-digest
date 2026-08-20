"""Build a podcast RSS feed from the published episodes.

Each daily run appends an entry to ``digests/episodes.json`` (the durable
manifest) and regenerates ``docs/feed.xml`` + ``docs/index.html``, which
GitHub Pages serves. Subscribe to the feed URL in any podcast app and new
episodes download automatically.

The episode audio itself is not committed to git — the enclosure points at
the MP3 attached to that day's GitHub Release, whose URL is deterministic
from the date.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from email.utils import format_datetime
from html import escape as html_escape
from pathlib import Path
from xml.sax.saxutils import escape

REPO = "abid1214/scirate-digest"
# Where GitHub Pages serves docs/ from. Override with SCIRATE_DIGEST_SITE_URL.
SITE_URL = os.environ.get("SCIRATE_DIGEST_SITE_URL", "https://abid1214.github.io/scirate-digest")
RELEASE_MP3 = "https://github.com/" + REPO + "/releases/download/digest-{date}/digest.mp3"

PODCAST_TITLE = "The SciRate Daily Digest"
PODCAST_DESCRIPTION = (
    "A daily audio digest of the most-scited new papers on SciRate. Each "
    "episode reads the papers' full arXiv source and delivers an executive "
    "summary and analysis, generated automatically with Claude."
)
PODCAST_AUTHOR = "SciRate Daily Digest"

MANIFEST = Path("digests/episodes.json")
DOCS = Path("docs")


@dataclass
class Episode:
    date: str  # YYYY-MM-DD
    title: str
    summary: str
    mp3_url: str
    mp3_bytes: int
    # [{"rank", "uid", "title", "abs_url", "scirate_url", "scites"}], newest schema.
    papers: list = field(default_factory=list)

    def pub_datetime(self) -> datetime:
        # Publish at the workflow's usual time so ordering is stable.
        return datetime.strptime(self.date, "%Y-%m-%d").replace(
            hour=13, minute=30, tzinfo=timezone.utc
        )


def load_manifest() -> list[Episode]:
    if not MANIFEST.exists():
        return []
    return [Episode(**e) for e in json.loads(MANIFEST.read_text())]


def save_manifest(episodes: list[Episode]) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(episodes, key=lambda e: e.date, reverse=True)
    MANIFEST.write_text(json.dumps([asdict(e) for e in ordered], indent=2))


def upsert_episode(episodes: list[Episode], new: Episode) -> list[Episode]:
    kept = [e for e in episodes if e.date != new.date]
    kept.append(new)
    return sorted(kept, key=lambda e: e.date, reverse=True)


def episode_from_run(date: str, mp3_path: Path, papers_path: Path) -> Episode:
    raw = json.loads(papers_path.read_text()) if papers_path.exists() else []
    papers = []
    for rank, p in enumerate(raw, 1):
        uid = p.get("uid", "")
        papers.append({
            "rank": rank,
            "uid": uid,
            "title": p.get("title") or uid,
            "abs_url": p.get("abs_url") or f"https://arxiv.org/abs/{uid}",
            "scirate_url": p.get("scirate_url") or f"https://scirate.com/arxiv/{uid}",
            "scites": p.get("scites"),
        })
    titles = [p["title"] for p in papers]
    summary = (
        f"Today's {len(titles)} papers: " + "; ".join(titles) + "."
        if titles else PODCAST_DESCRIPTION
    )
    mp3_bytes = mp3_path.stat().st_size if mp3_path.exists() else 0
    return Episode(
        date=date,
        title=f"SciRate Digest — {date}",
        summary=summary,
        mp3_url=RELEASE_MP3.format(date=date),
        mp3_bytes=mp3_bytes,
        papers=papers,
    )


def _show_notes_html(ep: Episode) -> str:
    """HTML show notes: an ordered list of papers, each linked to arXiv."""
    if not ep.papers:
        return f"<p>{html_escape(ep.summary)}</p>"
    lines = ["<p>The most-scited new papers on SciRate today:</p>", "<ol>"]
    for p in ep.papers:
        scites = ""
        if p.get("scites") is not None:
            scites = f" — {p['scites']} scites"
        lines.append(
            f'<li><a href="{html_escape(p["abs_url"])}">{html_escape(p["title"])}</a> '
            f'(<a href="{html_escape(p["abs_url"])}">arXiv:{html_escape(p["uid"])}</a>'
            f' · <a href="{html_escape(p["scirate_url"])}">SciRate</a>){scites}</li>'
        )
    lines.append("</ol>")
    return "".join(lines)


def build_feed(episodes: list[Episode]) -> str:
    now = format_datetime(datetime.now(timezone.utc))
    feed_url = f"{SITE_URL}/feed.xml"
    image_tags = ""
    if (DOCS / "cover.jpg").exists() or (DOCS / "cover.png").exists():
        cover = "cover.jpg" if (DOCS / "cover.jpg").exists() else "cover.png"
        img = f"{SITE_URL}/{cover}"
        image_tags = (
            f'<itunes:image href="{escape(img)}"/>'
            f"<image><url>{escape(img)}</url><title>{escape(PODCAST_TITLE)}</title>"
            f"<link>{escape(SITE_URL)}</link></image>"
        )

    items = []
    for e in episodes:
        # Cache-busting version tag: podcast apps key audio by enclosure URL
        # and the GUID. When a day's episode is re-rendered (e.g. the audio
        # changes) the byte count changes, so the URL/GUID change and apps
        # re-download instead of serving a stale cached file. GitHub ignores
        # the extra query param and serves the same asset.
        versioned_url = f"{e.mp3_url}?v={e.mp3_bytes}"
        guid = versioned_url
        notes = _show_notes_html(e)
        items.append(
            "<item>"
            f"<title>{escape(e.title)}</title>"
            f"<description><![CDATA[{notes}]]></description>"
            f"<content:encoded><![CDATA[{notes}]]></content:encoded>"
            f'<itunes:summary>{escape(e.summary)}</itunes:summary>'
            f'<enclosure url="{escape(versioned_url)}" length="{e.mp3_bytes}" type="audio/mpeg"/>'
            f'<guid isPermaLink="false">{escape(guid)}</guid>'
            f"<pubDate>{format_datetime(e.pub_datetime())}</pubDate>"
            f'<link>{escape("https://github.com/" + REPO + "/releases/tag/digest-" + e.date)}</link>'
            "</item>"
        )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" '
        'xmlns:content="http://purl.org/rss/1.0/modules/content/" '
        'xmlns:atom="http://www.w3.org/2005/Atom">\n'
        "<channel>"
        f"<title>{escape(PODCAST_TITLE)}</title>"
        f"<link>{escape(SITE_URL)}</link>"
        f'<atom:link href="{escape(feed_url)}" rel="self" type="application/rss+xml"/>'
        "<language>en-us</language>"
        f"<description>{escape(PODCAST_DESCRIPTION)}</description>"
        f"<itunes:author>{escape(PODCAST_AUTHOR)}</itunes:author>"
        f"<itunes:summary>{escape(PODCAST_DESCRIPTION)}</itunes:summary>"
        '<itunes:explicit>false</itunes:explicit>'
        '<itunes:category text="Science"><itunes:category text="Physics"/></itunes:category>'
        f"<lastBuildDate>{now}</lastBuildDate>"
        f"{image_tags}"
        f"{''.join(items)}"
        "</channel></rss>\n"
    )


def build_index(episodes: list[Episode]) -> str:
    rows = "\n".join(
        f'<li><a href="https://github.com/{REPO}/releases/tag/digest-{e.date}">'
        f"{escape(e.title)}</a> — {escape(e.summary)}</li>"
        for e in episodes
    )
    feed_url = f"{SITE_URL}/feed.xml"
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(PODCAST_TITLE)}</title>
<style>
 body {{ font-family: system-ui, sans-serif; max-width: 44rem; margin: 3rem auto;
        padding: 0 1rem; line-height: 1.5; }}
 code {{ background:#f0f0f0; padding:.1em .3em; border-radius:3px; }}
 a {{ color:#0a58ca; }}
</style></head><body>
<h1>🎙️ {escape(PODCAST_TITLE)}</h1>
<p>{escape(PODCAST_DESCRIPTION)}</p>
<h2>Subscribe</h2>
<p>Add this feed URL in your podcast app (Apple Podcasts, Overcast, Pocket
Casts, Spotify → "Add by URL"):</p>
<p><code>{escape(feed_url)}</code></p>
<p><a href="feed.xml">Raw RSS feed</a></p>
<h2>Episodes</h2>
<ul>
{rows}
</ul>
</body></html>
"""


def write_docs(episodes: list[Episode]) -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / "feed.xml").write_text(build_feed(episodes))
    (DOCS / "index.html").write_text(build_index(episodes))
    # Tell GitHub Pages not to run the content through Jekyll.
    (DOCS / ".nojekyll").write_text("")


def refresh_from_digests(episodes: list[Episode]) -> list[Episode]:
    """Backfill each episode's paper list (and summary) from its committed
    digests/<date>/papers.json, preserving mp3 url/size. For enriching older
    episodes after a schema change."""
    for ep in episodes:
        pp = Path(f"digests/{ep.date}/papers.json")
        if pp.exists():
            fresh = episode_from_run(ep.date, Path(), pp)
            ep.papers = fresh.papers
            ep.summary = fresh.summary
    return episodes


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build the podcast RSS feed.")
    ap.add_argument("--add", metavar="DATE", help="upsert an episode for YYYY-MM-DD")
    ap.add_argument("--mp3", type=Path, help="path to the episode MP3 (for --add)")
    ap.add_argument("--papers", type=Path, help="path to papers.json (for --add)")
    ap.add_argument(
        "--refresh", action="store_true",
        help="rebuild every episode's paper list from digests/<date>/papers.json",
    )
    args = ap.parse_args(argv)

    episodes = load_manifest()
    if args.add:
        ep = episode_from_run(args.add, args.mp3 or Path(), args.papers or Path())
        episodes = upsert_episode(episodes, ep)
        save_manifest(episodes)
    if args.refresh:
        episodes = refresh_from_digests(episodes)
        save_manifest(episodes)
    write_docs(episodes)
    print(f"Wrote feed with {len(episodes)} episode(s) to {DOCS}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
