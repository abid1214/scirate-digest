from pathlib import Path

from scirate_digest.scrape import parse_top_papers

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_structured_markup():
    html = (FIXTURES / "scirate_top.html").read_text()
    papers = parse_top_papers(html, count=10)
    assert [p.uid for p in papers] == ["2508.11111", "2508.22222", "quant-ph/0301040"]
    assert [p.scites for p in papers] == [42, 17, 9]


def test_count_limits_results():
    html = (FIXTURES / "scirate_top.html").read_text()
    assert len(parse_top_papers(html, count=2)) == 2


def test_link_fallback_when_no_data_uid():
    html = """
    <html><body>
      <a href="/arxiv/2508.33333">Paper A</a>
      <a href="/arxiv/2508.44444">Paper B</a>
      <a href="/arxiv/2508.33333">Paper A again</a>
      <a href="/arxiv/hep-th/9901001">Old style</a>
    </body></html>
    """
    papers = parse_top_papers(html, count=10)
    assert [p.uid for p in papers] == ["2508.33333", "2508.44444", "hep-th/9901001"]
    assert all(p.scites is None for p in papers)


def test_empty_page_gives_no_papers():
    assert parse_top_papers("<html><body>nothing</body></html>") == []


def test_scraper_api_request_scraperapi(monkeypatch):
    from scirate_digest.scrape import _scraper_api_request, _scraper_api_config
    monkeypatch.delenv("SCRAPINGBEE_KEY", raising=False)
    monkeypatch.setenv("SCRAPERAPI_KEY", "secret123")
    monkeypatch.setenv("SCRAPERAPI_EXTRA", "ultra_premium=true&country_code=us")
    assert _scraper_api_config() == ("scraperapi", "secret123")
    endpoint, params = _scraper_api_request("https://scirate.com/?range=1", tier="premium")
    assert endpoint == "https://api.scraperapi.com/"
    assert params["api_key"] == "secret123"
    assert params["url"] == "https://scirate.com/?range=1"
    assert params["render"] == "true"
    assert params["ultra_premium"] == "true"
    assert params["country_code"] == "us"


def test_scraper_api_request_scrapingbee(monkeypatch):
    from scirate_digest.scrape import _scraper_api_request
    monkeypatch.delenv("SCRAPERAPI_KEY", raising=False)
    monkeypatch.setenv("SCRAPINGBEE_KEY", "bee456")
    endpoint, params = _scraper_api_request("https://scirate.com/?range=1", tier="premium")
    assert endpoint == "https://app.scrapingbee.com/api/v1/"
    cheap_ep, cheap = _scraper_api_request("https://scirate.com/?range=1", tier="cheap")
    assert "stealth_proxy" not in cheap and cheap["render_js"] == "true"
    assert params["render_js"] == "true"
    assert params["stealth_proxy"] == "true"


def test_no_scraper_api_config(monkeypatch):
    from scirate_digest.scrape import _scraper_api_config
    monkeypatch.delenv("SCRAPERAPI_KEY", raising=False)
    monkeypatch.delenv("SCRAPINGBEE_KEY", raising=False)
    assert _scraper_api_config() == (None, None)
