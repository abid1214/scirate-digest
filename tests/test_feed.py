import json
import xml.dom.minidom as minidom
from pathlib import Path

import scirate_digest.feed as feed
from scirate_digest.feed import Episode, build_feed, build_index, upsert_episode


def _ep(date, title="T", mp3_bytes=100):
    return Episode(date=date, title=title, summary="s", mp3_url=f"http://x/{date}.mp3",
                   mp3_bytes=mp3_bytes)


def test_upsert_replaces_same_date_and_sorts_desc():
    eps = [_ep("2026-08-18"), _ep("2026-08-19")]
    eps = upsert_episode(eps, _ep("2026-08-19", title="new"))
    assert [e.date for e in eps] == ["2026-08-19", "2026-08-18"]
    assert eps[0].title == "new"  # replaced, not duplicated
    assert len(eps) == 2


def test_build_feed_is_valid_xml_with_enclosure():
    xml = build_feed([_ep("2026-08-19", mp3_bytes=5953248)])
    minidom.parseString(xml)  # raises if malformed
    assert 'type="audio/mpeg"' in xml
    assert 'length="5953248"' in xml
    assert "<itunes:author>" in xml


def test_feed_escapes_special_characters():
    xml = build_feed([_ep("2026-08-19", title="Bra <ket> & \"stuff\"")])
    minidom.parseString(xml)
    assert "<ket>" not in xml  # angle brackets escaped in the title text


def test_build_index_lists_episodes():
    html = build_index([_ep("2026-08-19", title="Episode One")])
    assert "Episode One" in html
    assert "feed.xml" in html


def test_episode_from_run_reads_papers(tmp_path):
    papers = tmp_path / "papers.json"
    papers.write_text(json.dumps([{"uid": "2508.1", "title": "Paper A"},
                                  {"uid": "2508.2", "title": "Paper B"}]))
    mp3 = tmp_path / "digest.mp3"
    mp3.write_bytes(b"x" * 4242)
    ep = feed.episode_from_run("2026-08-19", mp3, papers)
    assert ep.mp3_bytes == 4242
    assert "Paper A" in ep.summary and "Paper B" in ep.summary
    assert ep.mp3_url.endswith("digest-2026-08-19/digest.mp3")


def test_write_docs_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(feed, "DOCS", tmp_path / "docs")
    monkeypatch.setattr(feed, "MANIFEST", tmp_path / "digests" / "episodes.json")
    feed.save_manifest([_ep("2026-08-19")])
    feed.write_docs(feed.load_manifest())
    assert (tmp_path / "docs" / "feed.xml").exists()
    assert (tmp_path / "docs" / "index.html").exists()
    assert (tmp_path / "docs" / ".nojekyll").exists()
    minidom.parseString((tmp_path / "docs" / "feed.xml").read_text())
