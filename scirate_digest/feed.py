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
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from email.utils import format_datetime
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
    papers = json.loads(papers_path.read_text()) if papers_path.exists() else []
    titles = [p.get("title") or p.get("uid", "") for p in papers]
    if titles:
        summary = f"Today's {len(titles)} papers: " + "; ".join(titles) + "."
    else:
        summary = PODCAST_DESCRIPTION
    mp3_bytes = mp3_path.stat().st_size if mp3_path.exists() else 0
    return Episode(
        date=date,
        title=f"SciRate Digest — {date}",
        summary=summary,
        mp3_url=RELEASE_MP3.format(date=date),
        mp3_bytes=mp3_bytes,
    )


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
        guid = e.mp3_url
        items.append(
            "<item>"
            f"<title>{escape(e.title)}</title>"
            f"<description>{escape(e.summary)}</description>"
            f'<itunes:summary>{escape(e.summary)}</itunes:summary>'
            f'<enclosure url="{escape(e.mp3_url)}" length="{e.mp3_bytes}" type="audio/mpeg"/>'
            f'<guid isPermaLink="false">{escape(guid)}</guid>'
            f"<pubDate>{format_datetime(e.pub_datetime())}</pubDate>"
            f'<link>{escape("https://github.com/" + REPO + "/releases/tag/digest-" + e.date)}</link>'
            "</item>"
        )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" '
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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build the podcast RSS feed.")
    ap.add_argument("--add", metavar="DATE", help="upsert an episode for YYYY-MM-DD")
    ap.add_argument("--mp3", type=Path, help="path to the episode MP3 (for --add)")
    ap.add_argument("--papers", type=Path, help="path to papers.json (for --add)")
    args = ap.parse_args(argv)

    episodes = load_manifest()
    if args.add:
        ep = episode_from_run(args.add, args.mp3 or Path(), args.papers or Path())
        episodes = upsert_episode(episodes, ep)
        save_manifest(episodes)
    write_docs(episodes)
    print(f"Wrote feed with {len(episodes)} episode(s) to {DOCS}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
