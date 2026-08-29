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


def test_audio_meta_records_engine(tmp_path, monkeypatch):
    """A finished run records which TTS path rendered the audio."""
    import json
    import types
    from pathlib import Path

    import scirate_digest
    from scirate_digest import cli

    out = tmp_path / "2026-01-01"
    out.mkdir(parents=True)
    script = "Maya: hello there.\nSam: hi back.\n"

    def fake_synth(text, path, model=None):
        Path(path).write_bytes(b"\x00" * 64)
        return Path(path)

    monkeypatch.setattr(
        scirate_digest,
        "gemini_tts",
        types.SimpleNamespace(
            DEFAULT_MODEL="gemini-2.5-flash-preview-tts",
            synthesize_dialogue=fake_synth,
        ),
        raising=False,
    )

    meta = cli._render_audio(
        script_text=script,
        mp3_path=out / "digest.mp3",
        out_dir=out,
        date_str="2026-01-01",
        engine="gemini",
    )
    assert meta["rendered_with"] == "gemini-per-turn"
    assert meta["turns"] == 2
    assert meta["model"] == "gemini-2.5-flash-preview-tts"
    assert json.loads((out / "audio_meta.json").read_text())["rendered_with"] == (
        "gemini-per-turn"
    )


def test_audio_meta_records_fallback(tmp_path, monkeypatch):
    """A Gemini failure is recorded as the fallback that actually ran."""
    import types
    from pathlib import Path

    import scirate_digest
    from scirate_digest import cli

    out = tmp_path / "2026-01-02"
    out.mkdir(parents=True)

    def boom(text, path, model=None):
        raise RuntimeError("quota exceeded")

    def _write_stub(text, path):
        Path(path).write_bytes(b"\x00" * 32)
        return Path(path)

    monkeypatch.setattr(
        scirate_digest,
        "gemini_tts",
        types.SimpleNamespace(DEFAULT_MODEL="m", synthesize_dialogue=boom),
        raising=False,
    )
    monkeypatch.setattr(
        scirate_digest,
        "tts",
        types.SimpleNamespace(
            DEFAULT_VOICE="v",
            synthesize_dialogue=_write_stub,
        ),
        raising=False,
    )

    meta = cli._render_audio(
        script_text="Maya: a\nSam: b\n",
        mp3_path=out / "digest.mp3",
        out_dir=out,
        date_str="2026-01-02",
        engine="gemini",
    )
    assert meta["rendered_with"] == "edge-two-voice"


def test_prompts_suppress_authorship_disclosures():
    """Neither stage should surface how a paper was written (AI/LLM use)."""
    from scirate_digest.summarize import DIALOGUE_SYSTEM, PAPER_SYSTEM

    assert "tooling disclosures" in PAPER_SYSTEM
    assert "Never mention it" in PAPER_SYSTEM
    assert "Never discuss how a paper was written" in DIALOGUE_SYSTEM
    assert "never draw a trend across papers from them" in DIALOGUE_SYSTEM


def test_edge_engine_renders_two_voices(tmp_path, monkeypatch):
    """The default engine must voice the dialogue, not collapse to a narrator."""
    import types
    from pathlib import Path

    import scirate_digest
    from scirate_digest import cli

    out = tmp_path / "2026-01-03"
    out.mkdir(parents=True)
    calls = []

    def two_voice(text, path):
        calls.append("dialogue")
        Path(path).write_bytes(b"\x00" * 16)
        return Path(path)

    def narrator(text, path, voice=None):
        calls.append("narrator")
        Path(path).write_bytes(b"\x00" * 16)
        return Path(path)

    monkeypatch.setattr(
        scirate_digest, "tts",
        types.SimpleNamespace(DEFAULT_VOICE="v", synthesize_dialogue=two_voice,
                              synthesize=narrator),
        raising=False,
    )
    meta = cli._render_audio(
        script_text="Maya: a\nSam: b\n", mp3_path=out / "digest.mp3",
        out_dir=out, date_str="2026-01-03", engine="edge",
    )
    assert calls == ["dialogue"]
    assert meta["rendered_with"] == "edge-two-voice"


def test_recent_episode_context_is_titles_only():
    """Callback context carries titles and one line, never whole summaries."""
    from scirate_digest.summarize import _recent_block

    block = _recent_block([
        {"date": "2026-01-02", "papers": [
            {"title": "A code paper", "takeaway": "Cheaper error correction"},
            {"title": "No takeaway paper", "takeaway": ""},
        ]},
    ])
    assert "2026-01-02:" in block
    assert "- A code paper — Cheaper error correction" in block
    assert "- No takeaway paper" in block
