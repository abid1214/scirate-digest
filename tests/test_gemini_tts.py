from scirate_digest.gemini_tts import (
    chunk_turns,
    load_voices,
    parse_turns,
    render_chunk,
)

SPEAKERS = {"Maya", "Sam"}

SCRIPT = """Maya: Welcome to the SciRate Daily Digest for today.
Sam: Great to be here. We have five papers.
Maya: Let's start with the top one on photon detectors.
It's about spatial light modulation.
Sam: Right — the key result is a twelve nanosecond rise time.
Narrator ignore: this line has an unknown speaker and should attach above.
"""


def test_parse_turns_basic():
    turns = parse_turns(SCRIPT, SPEAKERS)
    assert turns[0] == ("Maya", "Welcome to the SciRate Daily Digest for today.")
    assert turns[1][0] == "Sam"
    # a wrapped line with no speaker joins the previous turn
    assert "spatial light modulation" in turns[2][1]
    # an unknown-speaker line joins the last turn rather than starting a new one
    assert "unknown speaker" in turns[-1][1]
    assert all(s in SPEAKERS for s, _ in turns)


def test_chunk_turns_splits_on_size():
    turns = [("Maya", "x" * 100), ("Sam", "y" * 100), ("Maya", "z" * 100)]
    chunks = chunk_turns(turns, max_chars=250)
    assert len(chunks) == 2
    # every original turn survives exactly once
    flat = [t for c in chunks for t in c]
    assert flat == turns


def test_chunk_turns_single_when_small():
    turns = [("Maya", "hi"), ("Sam", "hello")]
    assert len(chunk_turns(turns, max_chars=1000)) == 1


def test_render_chunk_format():
    out = render_chunk([("Maya", "hi there"), ("Sam", "hello")])
    assert out == "Maya: hi there\nSam: hello"


def test_load_voices_default_and_override(monkeypatch):
    monkeypatch.delenv("GEMINI_VOICES", raising=False)
    assert load_voices() == {"Maya": "Kore", "Sam": "Puck"}
    monkeypatch.setenv("GEMINI_VOICES", "Maya=Aoede, Sam=Charon")
    assert load_voices() == {"Maya": "Aoede", "Sam": "Charon"}
