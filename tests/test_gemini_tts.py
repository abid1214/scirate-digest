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
    assert load_voices() == {"Maya": "Kore", "Sam": "Charon"}
    monkeypatch.setenv("GEMINI_VOICES", "Maya=Aoede, Sam=Charon")
    assert load_voices() == {"Maya": "Aoede", "Sam": "Charon"}


def test_build_request_body_multispeaker():
    from scirate_digest.gemini_tts import build_request_body
    body = build_request_body("Maya: hi\nSam: hello", {"Maya": "Kore", "Sam": "Puck"},
                              "gemini-3.1-flash-tts-preview")
    assert body["model"] == "gemini-3.1-flash-tts-preview"
    assert "Maya and Sam" in body["input"]
    assert "Maya: hi" in body["input"]
    assert body["response_format"] == {"type": "audio"}
    assert body["generation_config"]["speech_config"] == [
        {"speaker": "Maya", "voice": "Kore"},
        {"speaker": "Sam", "voice": "Puck"},
    ]


def test_find_audio_extracts_pcm():
    import base64
    from scirate_digest.gemini_tts import _find_audio
    payload = base64.b64encode(b"\x00\x01" * 500).decode()
    resp = {"interaction": {"output_audio": {"data": payload,
            "mimeType": "audio/L16;rate=24000"}}}
    raw, rate = _find_audio(resp)
    assert rate == 24000
    assert len(raw) == 1000


def test_style_direction_in_request(monkeypatch):
    from scirate_digest.gemini_tts import build_request_body
    monkeypatch.delenv("GEMINI_TTS_STYLE", raising=False)
    body = build_request_body("Maya: hi", {"Maya": "Kore", "Sam": "Puck"}, "m")
    assert "podcast conversation" in body["input"]
    assert body["input"].rstrip().endswith("Maya: hi")
    monkeypatch.setenv("GEMINI_TTS_STYLE", "Deadpan.")
    body = build_request_body("Maya: hi", {"Maya": "Kore", "Sam": "Puck"}, "m")
    assert body["input"].startswith("Deadpan.")


def test_edge_dialogue_voices_env(monkeypatch):
    from scirate_digest.tts import load_dialogue_voices
    monkeypatch.delenv("EDGE_DIALOGUE_VOICES", raising=False)
    v = load_dialogue_voices()
    assert set(v) == {"Maya", "Sam"} and v["Maya"] != v["Sam"]
    monkeypatch.setenv("EDGE_DIALOGUE_VOICES", "Maya=en-GB-SoniaNeural, Sam=en-AU-WilliamNeural")
    assert load_dialogue_voices() == {"Maya": "en-GB-SoniaNeural", "Sam": "en-AU-WilliamNeural"}


def test_split_segments_on_break_lines():
    from scirate_digest.gemini_tts import split_segments
    script = "Maya: intro\nSam: hi\n[BREAK]\nMaya: paper one\n [break] \nSam: paper two"
    segs = split_segments(script)
    assert len(segs) == 3
    assert segs[0] == "Maya: intro\nSam: hi"
    assert segs[1] == "Maya: paper one"
    assert segs[2] == "Sam: paper two"


def test_split_segments_no_breaks():
    from scirate_digest.gemini_tts import split_segments
    assert split_segments("Maya: hello\nSam: hi") == ["Maya: hello\nSam: hi"]


def test_narration_strips_breaks():
    from scirate_digest.cli import _dialogue_to_narration
    out = _dialogue_to_narration("Maya: a\n[BREAK]\nSam: b")
    assert "[BREAK]" not in out
    assert out == "a\n\nb"
