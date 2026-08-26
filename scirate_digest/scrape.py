"""Scrape the SciRate front page for the top-scited papers.

SciRate ranks papers by "scites" over a time window (``?range=N`` days). We
only need the *ranked list of arXiv IDs* from the page — titles, authors and
abstracts are re-fetched from the arXiv API afterwards, which keeps this
parser tolerant of SciRate markup changes.

SciRate sits behind Cloudflare, which challenges plain HTTP clients and —
on datacenter IPs like GitHub Actions runners — even ordinary headless
browsers. Fetching therefore walks a chain of strategies until one yields a
real page:

1. plain HTTP (fast; works from residential networks),
2. Camoufox, a fingerprint-spoofing Firefox build that passes Cloudflare
   far more reliably than stock automation browsers,
3. Playwright Chromium with mild stealth tweaks,
4. the Wayback Machine's most recent snapshot of the SciRate front page
   (archive.org's crawler is allowed through; only used when fresh).
"""

from __future__ import annotations

import datetime as dt
import logging
import os
import re
import sys
from urllib.parse import parse_qsl

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
    """Fetch the SciRate top-papers page, walking the strategy chain."""
    url = SCIRATE_URL + (f"arxiv/{category}" if category else "")
    full_url = f"{url}?range={range_days}"
    strategies = [("plain HTTP", lambda: _fetch_plain(url, range_days))]
    # A scraping-API service fetches from its own residential proxies and
    # clears Cloudflare — the primary strategy on a datacenter (CI) IP, where
    # the local browsers below cannot pass. Only used if a key is configured.
    if _scraper_api_config()[1]:
        strategies.append(("scraping API", lambda: _fetch_scraper_api(full_url)))
    strategies += [
        ("Camoufox", lambda: _fetch_camoufox(full_url)),
        ("Playwright Chromium", lambda: _fetch_playwright(full_url)),
        ("Jina Reader", lambda: _fetch_jina(full_url)),
    ]
    if range_days <= 1 and category is None:
        # Snapshots only exist for the front page, which is the daily ranking.
        strategies.append(("Wayback Machine", _fetch_wayback))

    for name, strategy in strategies:
        try:
            html = strategy()
            if html and parse_top_papers(html, count=1):
                log.info("Fetched SciRate via %s", name)
                return html
            if html:
                log.warning("SciRate fetch via %s returned a page with no papers", name)
        except Exception as exc:
            log.warning("SciRate fetch via %s failed: %s", name, exc)
    raise RuntimeError("All strategies for fetching the SciRate page failed")


def _fetch_plain(url: str, range_days: int) -> str:
    resp = requests.get(
        url,
        params={"range": range_days},
        headers={"User-Agent": USER_AGENT, "Accept": "text/html"},
        timeout=60,
    )
    resp.raise_for_status()
    if _looks_like_challenge(resp.text):
        raise RuntimeError("Cloudflare challenge")
    return resp.text


def _scraper_api_config() -> tuple[str | None, str | None]:
    """Return (provider, api_key) from the environment, or (None, None)."""
    if os.environ.get("SCRAPERAPI_KEY"):
        return "scraperapi", os.environ["SCRAPERAPI_KEY"]
    if os.environ.get("SCRAPINGBEE_KEY"):
        return "scrapingbee", os.environ["SCRAPINGBEE_KEY"]
    return None, None


def _scraper_api_request(full_url: str, tier: str = "premium") -> tuple[str, dict]:
    """Build the (endpoint, params) for the configured scraping-API provider.

    ``tier`` is "cheap" (JS render only — a few credits) or "premium"
    (stealth/residential proxies — an order of magnitude more credits, needed
    when Cloudflare challenges the cheap tier). Extra provider params can be
    supplied as a query-string in SCRAPERAPI_EXTRA / SCRAPINGBEE_EXTRA.
    """
    provider, key = _scraper_api_config()
    if not key:
        raise RuntimeError("no scraper API key configured")
    if provider == "scraperapi":
        endpoint = "https://api.scraperapi.com/"
        params = {"api_key": key, "url": full_url, "render": "true"}
        if tier == "premium":
            params["ultra_premium"] = "true"
        extra = os.environ.get("SCRAPERAPI_EXTRA", "")
    else:
        endpoint = "https://app.scrapingbee.com/api/v1/"
        params = {"api_key": key, "url": full_url, "render_js": "true"}
        if tier == "premium":
            params["stealth_proxy"] = "true"
        extra = os.environ.get("SCRAPINGBEE_EXTRA", "")
    params.update(dict(parse_qsl(extra)))
    return endpoint, params


def _fetch_scraper_api(full_url: str, timeout_s: int = 150) -> str:
    # Cheap tier first: it costs ~15x fewer credits and sometimes clears
    # Cloudflare on its own. Escalate to stealth/residential only on a
    # challenge or block.
    last_exc: Exception | None = None
    for tier in ("cheap", "premium"):
        endpoint, params = _scraper_api_request(full_url, tier=tier)
        try:
            resp = requests.get(endpoint, params=params, timeout=timeout_s)
            resp.raise_for_status()
            if _looks_like_challenge(resp.text):
                raise RuntimeError(f"Cloudflare challenge (via scraping API, {tier} tier)")
            return resp.text
        except Exception as exc:
            log.info("scraping API %s tier failed: %s", tier, exc)
            last_exc = exc
    raise last_exc if last_exc else RuntimeError("scraping API failed")


def _wait_out_challenge(page, timeout_s: int) -> str:
    """Poll an open browser page until the Cloudflare challenge clears."""
    for _ in range(max(timeout_s // 3, 1)):
        html = page.content()
        if not _looks_like_challenge(html):
            return html
        page.wait_for_timeout(3000)
    raise RuntimeError(f"Cloudflare challenge did not clear in {timeout_s}s")


def _fetch_camoufox(url: str, timeout_s: int = 150) -> str:
    from camoufox.sync_api import Camoufox

    # geoip=True aligns the spoofed timezone/locale with the egress IP —
    # a mismatch there is an instant Cloudflare flag. Headed clears
    # challenges best; pick how to be headed by platform:
    #   * a real desktop session (Windows/macOS, or Linux with $DISPLAY) -> headed
    #   * headless Linux with SCIRATE_DIGEST_HEADED=1 -> Camoufox's xvfb ("virtual")
    #   * otherwise -> headless (fine from a residential IP)
    kwargs: dict = {"geoip": True, "humanize": True}
    want_headed = (
        os.environ.get("SCIRATE_DIGEST_HEADED") == "1" or bool(os.environ.get("DISPLAY"))
    )
    if not want_headed:
        kwargs["headless"] = True
    elif sys.platform.startswith("linux") and not os.environ.get("DISPLAY"):
        kwargs["headless"] = "virtual"  # spin up xvfb (Linux only)
    else:
        kwargs["headless"] = False  # real desktop, incl. Windows/macOS
    with Camoufox(**kwargs) as browser:
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=timeout_s * 1000)
        return _wait_out_challenge(page, timeout_s)


def _fetch_playwright(url: str, timeout_s: int = 60) -> str:
    from playwright.sync_api import sync_playwright

    # Cloudflare fingerprints headless Chromium aggressively; a headed browser
    # under a virtual display (xvfb) clears managed challenges far more
    # reliably. Set SCIRATE_DIGEST_HEADED=1 and run under `xvfb-run` to use it.
    headed = os.environ.get("SCIRATE_DIGEST_HEADED") == "1"
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=not headed,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"],
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
            return _wait_out_challenge(page, timeout_s)
        finally:
            browser.close()


def _fetch_jina(full_url: str) -> str:
    """Fetch through the Jina Reader proxy, which browses from its own
    infrastructure and returns the page as markdown (the link-regex parser
    handles that fine)."""
    resp = requests.get(
        "https://r.jina.ai/" + full_url,
        headers={"User-Agent": USER_AGENT},
        timeout=120,
    )
    resp.raise_for_status()
    if _looks_like_challenge(resp.text):
        raise RuntimeError("Cloudflare challenge (via reader proxy)")
    return resp.text


def _fetch_wayback(max_age_days: int = 5) -> str:
    """Fetch archive.org's most recent snapshot of the SciRate front page.

    The front page is the ranking for the last day, so a fresh snapshot is a
    faithful (if slightly stale) source when Cloudflare blocks live access.
    A Save Page Now capture is requested first so the snapshot is from today
    whenever archive.org's crawler can reach SciRate.
    """
    try:
        requests.get(
            "https://web.archive.org/save/https://scirate.com/",
            headers={"User-Agent": USER_AGENT},
            timeout=180,
        )
    except requests.RequestException as exc:
        log.info("Save Page Now request failed (%s); trying existing snapshots", exc)

    resp = requests.get(
        "https://archive.org/wayback/available",
        params={"url": "scirate.com"},
        headers={"User-Agent": USER_AGENT},
        timeout=60,
    )
    resp.raise_for_status()
    snap = resp.json().get("archived_snapshots", {}).get("closest")
    if not snap or not snap.get("available"):
        raise RuntimeError("no Wayback snapshot available")
    taken = dt.datetime.strptime(snap["timestamp"], "%Y%m%d%H%M%S")
    age = dt.datetime.utcnow() - taken
    if age > dt.timedelta(days=max_age_days):
        raise RuntimeError(f"latest Wayback snapshot is {age.days} days old")
    log.info("Using Wayback snapshot from %s", taken.isoformat())
    snap_resp = requests.get(
        snap["url"].replace("http://", "https://", 1),
        headers={"User-Agent": USER_AGENT},
        timeout=120,
    )
    snap_resp.raise_for_status()
    return snap_resp.text


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
