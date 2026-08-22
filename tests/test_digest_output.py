from scirate_digest.cli import write_digest_markdown
from scirate_digest.models import Paper


def test_write_digest_markdown(tmp_path):
    papers = [
        Paper(
            uid="2508.11111",
            title="Quantum Advantage in Widget Sorting",
            authors=["Alice Ansatz", "Bob Bloch"],
            abstract="We sort widgets.",
            scites=42,
            summary="**TL;DR** — widgets sorted faster.",
        ),
        Paper(uid="2508.22222"),  # metadata fetch failed for this one
    ]
    out = tmp_path / "digest.md"
    write_digest_markdown(papers, "2026-08-19", out)
    text = out.read_text()
    assert "# SciRate Daily Digest — 2026-08-19" in text
    assert "## 1. Quantum Advantage in Widget Sorting" in text
    assert "42 scites" in text
    assert "widgets sorted faster" in text
    assert "## 2. 2508.22222" in text  # falls back to the uid as a title


def test_paper_to_dict_roundtrip():
    p = Paper(uid="2508.11111", title="T", scites=3)
    d = p.to_dict()
    assert d["uid"] == "2508.11111"
    assert d["abs_url"] == "https://arxiv.org/abs/2508.11111"
    assert d["scirate_url"] == "https://scirate.com/arxiv/2508.11111"


def test_load_discussed_uids(tmp_path):
    import json
    from scirate_digest.cli import load_discussed_uids
    d1 = tmp_path / "2026-08-19"; d1.mkdir()
    d2 = tmp_path / "2026-08-20"; d2.mkdir()
    (d1 / "papers.json").write_text(json.dumps([{"uid": "2608.1"}, {"uid": "2608.2"}]))
    (d2 / "papers.json").write_text(json.dumps([{"uid": "2608.2"}, {"uid": "2608.3"}]))
    assert load_discussed_uids(tmp_path) == {"2608.1", "2608.2", "2608.3"}
    # excluding today's own directory (same-day re-render)
    assert load_discussed_uids(tmp_path, exclude_date="2026-08-20") == {"2608.1", "2608.2"}


def test_load_discussed_uids_missing_dir(tmp_path):
    from scirate_digest.cli import load_discussed_uids
    assert load_discussed_uids(tmp_path / "nope") == set()


def test_load_discussed_uids_tolerates_bad_json(tmp_path):
    from scirate_digest.cli import load_discussed_uids
    d = tmp_path / "2026-08-18"; d.mkdir()
    (d / "papers.json").write_text("not json{")
    assert load_discussed_uids(tmp_path) == set()
