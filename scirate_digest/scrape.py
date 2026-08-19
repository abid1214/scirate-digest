"""Scrape the SciRate front page for the top-scited papers.

SciRate ranks papers by "scites" over a time window (``?range=N`` days). We
only need the *ranked list of arXiv IDs* from the page — titles, authors and
abstracts are re-fetched from the arXiv API afterwards, which keeps this
parser tolerant of SciRate markup changes.

SciRate sits behind Cloudflare, which sometimes challenges plain HTTP
clients. When that happens we fall back to driving a headless Chromium via
Playwright (installed with the ``browser`` extra) and waiting for the
challenge to clear.
"""

from __future__ import annotations

import logging
import re

import requests
from bs4 import BeautifulSoup

from .models import Paper

log = logging.getLogger(__name__)

SCIRATE_URL = "https://scirate.com/"

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)

# New-style (2408.12345) and old-style (quant-ph/0301040) arXiv identifiers.
ARXIV_ID_RE = re.compile(r"/arxiv/(\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})")


def _looks_like_challenge(html: str) -> bool:
    return "Just a moment" in html or "_cf_chl_opt" in html


def fetch_html(range_days: int = 1, category: str | None = None) -> str:
    """Fetch the SciRate top-papers page, falling back to a headless browser."""
    url = SCIRATE_URL + (f"arxiv/{category}" if category else "")
    try:
        resp = requests.get(
            url,
            params={"range": range_days},
            headers={"User-Agent": USER_AGENT, "Accept": "text/html"},
            timeout=60,
        )
        if resp.ok and not _looks_like_challenge(resp.text):
            return resp.text
        log.info("SciRate returned a Cloudflare challenge; retrying with a browser")
    except requests.RequestException as exc:
        log.info("Plain HTTP fetch of SciRate failed (%s); retrying with a browser", exc)
    return _fetch_html_browser(f"{url}?range={range_days}")


def _fetch_html_browser(url: str, timeout_s: int = 120) -> str:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError(
            "SciRate is challenging plain HTTP requests and Playwright is not "
            "installed. Install it with: pip install 'scirate-digest[browser]' "
            "&& playwright install chromium"
        ) from exc

    with sync_playwright() as p:
        browser = p.chromium.launch(
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        )
        try:
            ctx = browser.new_context(
                user_agent=USER_AGENT,
                viewport={"width": 1920, "height": 1080},
                locale="en-US",
            )
            # Hide the webdriver flag that Cloudflare uses to detect headless browsers.
            ctx.add_init_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            )
            page = ctx.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=timeout_s * 1000)
            # Give the Cloudflare managed challenge time to clear.
            for _ in range(timeout_s // 3):
                html = page.content()
                if not _looks_like_challenge(html):
                    return html
                page.wait_for_timeout(3000)
            raise RuntimeError("Cloudflare challenge on SciRate did not clear in time")
        finally:
            browser.close()


def parse_top_papers(html: str, count: int = 10) -> list[Paper]:
    """Extract the ranked papers from a SciRate listing page.

    Prefers the structured markup (elements carrying a ``data-uid``), which
    also yields scite counts; falls back to ``/arxiv/<id>`` links in document
    order, which preserves the ranking even if the markup changes.
    """
    soup = BeautifulSoup(html, "html.parser")
    papers: list[Paper] = []
    seen: set[str] = set()

    for node in soup.select("[data-uid]"):
        uid = node.get("data-uid", "").strip()
        if not uid or uid in seen:
            continue
        seen.add(uid)
        papers.append(Paper(uid=uid, scites=_find_scites(node)))

    if not papers:
        for match in ARXIV_ID_RE.finditer(html):
            uid = match.group(1)
            if uid not in seen:
                seen.add(uid)
                papers.append(Paper(uid=uid))

    return papers[:count]


def _find_scites(node) -> int | None:
    for el in node.select('[class*="scite"]'):
        text = el.get_text(strip=True)
        if text.isdigit():
            return int(text)
    return None


def fetch_top_papers(
    count: int = 10, range_days: int = 1, category: str | None = None
) -> list[Paper]:
    html = fetch_html(range_days=range_days, category=category)
    papers = parse_top_papers(html, count=count)
    if not papers:
        raise RuntimeError(
            "No papers found on the SciRate page — the markup may have changed"
        )
    return papers
