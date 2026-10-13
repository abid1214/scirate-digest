from scirate_digest.gemini_tts import (
    chunk_turns,
    load_voices,
    parse_turns,
    render_chunk,
)

SPEAKERS = {"Maya", "Sam"}

SCRIPT = """Maya: Welcome to the SciRate Weekly Digest for today.
Sam: Great to be here. We have five papers.
Maya: Let's start with the top one on photon detectors.
It's about spatial light modulation.
Sam: Right — the key result is a twelve nanosecond rise time.
Narrator ignore: this line has an unknown speaker and should attach above.
"""


def test_parse_turns_basic():
    turns = parse_turns(SCRIPT, SPEAKERS)
    assert turns[0] == ("Maya", "Welcome to the SciRate Weekly Digest for today.")
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


def test_engine_defaults_to_edge(monkeypatch):
    """Deterministic voices are the default; Gemini is explicit opt-in."""
    import argparse
    from scirate_digest.cli import _resolve_engine

    args = argparse.Namespace(voice_engine="auto")
    monkeypatch.setenv("GEMINI_API_KEY", "present-but-not-selected")
    monkeypatch.delenv("VOICE_ENGINE", raising=False)
    assert _resolve_engine(args) == "edge"

    monkeypatch.setenv("VOICE_ENGINE", "gemini")
    assert _resolve_engine(args) == "gemini"

    monkeypatch.setenv("VOICE_ENGINE", "")          # unset repo var in CI
    assert _resolve_engine(args) == "edge"

    assert _resolve_engine(argparse.Namespace(voice_engine="gemini")) == "gemini"


def test_merge_consecutive_turns():
    from scirate_digest.gemini_tts import merge_consecutive_turns
    turns = [("Maya", "one."), ("Maya", "two."), ("Sam", "three."),
             ("Maya", "four.")]
    assert merge_consecutive_turns(turns) == [
        ("Maya", "one. two."), ("Sam", "three."), ("Maya", "four.")]


def test_merge_consecutive_turns_respects_cap():
    from scirate_digest.gemini_tts import merge_consecutive_turns
    turns = [("Sam", "x" * 90), ("Sam", "y" * 90)]
    merged = merge_consecutive_turns(turns, max_chars=100)
    assert merged == turns  # too long to join


def test_build_request_body_single_speaker():
    # Per the Interactions API docs, single-speaker requests carry only a
    # voice (no "speaker" field) and plain unlabeled text.
    from scirate_digest.gemini_tts import build_request_body
    body = build_request_body("hi there", {"Maya": "Kore"}, "m")
    assert "conversation between" not in body["input"]
    assert body["input"].rstrip().endswith("hi there")
    assert body["generation_config"]["speech_config"] == [{"voice": "Kore"}]


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


def test_audition_labels_are_speakable():
    """Voice ids are announced as readable names, not raw identifiers."""
    from scirate_digest.audition import _short_name

    assert _short_name("en-US-AvaMultilingualNeural") == "Ava Multilingual"
    assert _short_name("en-US-JennyNeural") == "Jenny"
    assert _short_name("en-GB-SoniaNeural") == "Sonia"


def test_audition_assembles_label_and_sample_per_voice(tmp_path, monkeypatch):
    """Each candidate gets an announced label and the same sample, in order."""
    import subprocess
    from pathlib import Path

    from scirate_digest import audition

    rendered = []

    def fake_synth(text, out_path, voice=None):
        rendered.append((voice, text[:12]))
        subprocess.run(
            ["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
             "-t", "0.3", "-b:a", "48k", str(out_path)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return Path(out_path)

    monkeypatch.setattr(audition.tts, "synthesize", fake_synth)
    out = audition.render(["en-US-JennyNeural", "en-US-AriaNeural"],
                          tmp_path / "a.mp3", sample="Sample line.")
    assert out.exists() and out.stat().st_size > 0
    # announcer label then the candidate reading the sample, for each voice
    assert [v for v, _ in rendered] == [
        audition.ANNOUNCER, "en-US-JennyNeural",
        audition.ANNOUNCER, "en-US-AriaNeural",
    ]


def test_turn_retry_survives_a_flaky_request(tmp_path, monkeypatch):
    """One bad response must not cost the whole two-voice episode."""
    import asyncio

    from scirate_digest import tts

    calls = {"n": 0}

    class FakeCommunicate:
        def __init__(self, text, voice=None):
            self.text, self.voice = text, voice

        async def save(self, path):
            calls["n"] += 1
            # first attempt at the second turn returns no audio
            if self.text == "second" and calls["n"] <= 2:
                raise RuntimeError("No audio was received.")
            Path = type(tmp_path)
            Path(path).write_bytes(b"\x00" * 8)

    monkeypatch.setattr(tts, "TURN_ATTEMPTS", 3)
    monkeypatch.setitem(
        __import__("sys").modules, "edge_tts",
        type("m", (), {"Communicate": FakeCommunicate}),
    )
    real_sleep = asyncio.sleep
    monkeypatch.setattr(asyncio, "sleep", lambda *_a, **_k: real_sleep(0))

    turns = [("Maya", "first"), ("Sam", "second")]
    voices = {"Maya": "v1", "Sam": "v2"}
    paths = asyncio.run(tts._synthesize_turns(turns, voices, tmp_path))
    assert all(p.exists() and p.stat().st_size > 0 for p in paths)


def test_turn_retry_gives_up_eventually(tmp_path, monkeypatch):
    import asyncio

    from scirate_digest import tts

    class AlwaysFails:
        def __init__(self, text, voice=None):
            pass

        async def save(self, path):
            raise RuntimeError("No audio was received.")

    monkeypatch.setattr(tts, "TURN_ATTEMPTS", 2)
    monkeypatch.setitem(
        __import__("sys").modules, "edge_tts",
        type("m", (), {"Communicate": AlwaysFails}),
    )
    real_sleep = asyncio.sleep
    monkeypatch.setattr(asyncio, "sleep", lambda *_a, **_k: real_sleep(0))

    with __import__("pytest").raises(RuntimeError, match="failed after 2 attempts"):
        asyncio.run(tts._synthesize_turns([("Maya", "x")], {"Maya": "v"}, tmp_path))


def test_endpoint_failover_is_rebound_where_edge_tts_reads_it(monkeypatch):
    """A 403 must move the URL on the module edge-tts actually reads."""
    from edge_tts import communicate as ec

    from scirate_digest import tts

    monkeypatch.delenv("EDGE_WSS_URL", raising=False)
    monkeypatch.setattr(ec, "WSS_URL", "wss://original/edge/v1", raising=False)

    # anything that is not a 403 is this turn's problem, not the endpoint's
    assert tts._failover_endpoint(RuntimeError("No audio was received.")) is False
    assert ec.WSS_URL == "wss://original/edge/v1"

    assert tts._failover_endpoint(RuntimeError("403, message='Invalid response'"))
    assert ec.WSS_URL == tts._alt_wss_url()
    assert ec.WSS_URL.startswith(tts.ALT_WSS_HOST + "?Ocp-Apim-Subscription-Key=")
    # concurrent turns all see the same 403; only the first move counts
    assert tts._failover_endpoint(RuntimeError("403")) is False


def test_pinned_endpoint_is_respected(monkeypatch):
    from edge_tts import communicate as ec

    from scirate_digest import tts

    monkeypatch.setattr(ec, "WSS_URL", "wss://original/edge/v1", raising=False)
    monkeypatch.setenv("EDGE_WSS_URL", "wss://pinned/by/hand")
    tts._apply_endpoint_override()
    assert ec.WSS_URL == "wss://pinned/by/hand"
    # a pinned URL is a deliberate choice; a 403 must not wander off it
    assert tts._failover_endpoint(RuntimeError("403")) is False
    assert ec.WSS_URL == "wss://pinned/by/hand"


def test_turns_survive_an_endpoint_wide_403(tmp_path, monkeypatch):
    """The outage that cost two episodes: every turn 403s on the old host."""
    import asyncio

    from edge_tts import communicate as ec

    from scirate_digest import tts

    monkeypatch.delenv("EDGE_WSS_URL", raising=False)
    monkeypatch.setattr(ec, "WSS_URL", "wss://original/edge/v1", raising=False)

    class HostAwareCommunicate:
        def __init__(self, text, voice=None):
            pass

        async def save(self, path):
            if ec.WSS_URL == "wss://original/edge/v1":
                raise RuntimeError("403, message='Invalid response status'")
            __import__("pathlib").Path(path).write_bytes(b"\x00" * 8)

    import edge_tts as real_edge_tts

    monkeypatch.setitem(
        __import__("sys").modules, "edge_tts",
        type("m", (), {"Communicate": HostAwareCommunicate,
                       # the failover reads the real token and rebinds the
                       # real communicate module
                       "constants": real_edge_tts.constants,
                       "communicate": ec}),
    )
    real_sleep = asyncio.sleep
    monkeypatch.setattr(asyncio, "sleep", lambda *_a, **_k: real_sleep(0))

    turns = [("Maya", "one"), ("Sam", "two"), ("Maya", "three")]
    paths = asyncio.run(tts._synthesize_turns(
        turns, {"Maya": "v1", "Sam": "v2"}, tmp_path))
    assert all(p.exists() and p.stat().st_size > 0 for p in paths)
    assert ec.WSS_URL == tts._alt_wss_url()
