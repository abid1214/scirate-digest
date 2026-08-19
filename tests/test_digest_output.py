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
