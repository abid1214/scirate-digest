"""Two-host podcast audio via Gemini multi-speaker text-to-speech.

Uses the Gemini REST API directly (no SDK, to avoid version drift). The
model returns raw little-endian 16-bit PCM, which we assemble into a WAV and
transcode to MP3 with ffmpeg. Long scripts are split on speaker-turn
boundaries and the PCM is concatenated, because a single TTS request is
length-limited.

Requires GEMINI_API_KEY and ffmpeg on PATH.
"""

from __future__ import annotations

import base64
import logging
import os
import re
import subprocess
import tempfile
import time
import wave
from pathlib import Path

import requests

log = logging.getLogger(__name__)

# Google's TTS lives on the Interactions API (the generateContent path 404s
# for TTS models). Model/revision are overridable via env for future updates.
API_URL = "https://generativelanguage.googleapis.com/v1beta/interactions"
# Use `or` (not a default arg): CI passes these as empty strings when the
# optional repo variables are unset, and get(key, default) returns "" then.
# Per-turn synthesis makes ~100 requests per episode, which exhausts the
# pro TTS preview's small daily request quota mid-episode (observed: hard
# 429 "check your plan and billing" at turn 41). The 2.5 flash TTS preview
# has a much higher daily quota; the distortion previously heard on flash
# was the separate 3.1 preview in multi-speaker mode. Override with
# GEMINI_TTS_MODEL.
DEFAULT_MODEL = os.environ.get("GEMINI_TTS_MODEL") or "gemini-2.5-flash-preview-tts"
API_REVISION = os.environ.get("GEMINI_API_REVISION") or "2026-05-20"

# Host name (as it appears in the script) -> Gemini prebuilt voice name.
# Override with GEMINI_VOICES="Maya=Kore,Sam=Puck".
DEFAULT_VOICES = {"Maya": "Kore", "Sam": "Charon"}

# Max characters of transcript per TTS request (split only at turn
# boundaries). Google documents that multi-speaker consistency drifts on
# outputs "longer than a few minutes" and recommends smaller chunks, so
# this targets roughly 1.5-2 minutes of audio per request.
MAX_CHARS = 2200
DEFAULT_RATE = 24000

_TURN_RE = re.compile(r"^\s*([A-Za-z][\w .'-]*?):\s*(.*)$")
_BREAK_RE = re.compile(r"^\s*\[BREAK\]\s*$", re.IGNORECASE)

# Musical bumper played at [BREAK] markers. Path is repo-relative in CI.
STINGER_PATH = os.environ.get("STINGER_PATH") or "assets/stinger.mp3"
BREAK_SILENCE_S = 0.6  # breathing room on each side of the stinger
TURN_GAP_S = 0.35  # beat between speaker turns when synthesizing per-turn


def split_segments(transcript: str) -> list[str]:
    """Split the script at [BREAK] lines into segments (empty ones dropped)."""
    segments: list[list[str]] = [[]]
    for line in transcript.splitlines():
        if _BREAK_RE.match(line):
            segments.append([])
        else:
            segments[-1].append(line)
    return ["\n".join(s).strip() for s in segments if "\n".join(s).strip()]


def _stinger_pcm(rate: int) -> bytes:
    """The break audio as raw PCM at the target rate: silence + stinger +
    silence. Falls back to plain silence if the asset or ffmpeg is missing."""
    silence = b"\x00\x00" * int(BREAK_SILENCE_S * rate)
    music = b""
    if os.path.exists(STINGER_PATH):
        try:
            r = subprocess.run(
                ["ffmpeg", "-i", STINGER_PATH, "-f", "s16le", "-acodec",
                 "pcm_s16le", "-ac", "1", "-ar", str(rate), "-"],
                capture_output=True,
            )
            if r.returncode == 0:
                music = r.stdout
        except OSError:
            pass
    if not music:
        music = b"\x00\x00" * int(1.0 * rate)  # silent break if no stinger
    return silence + music + silence


def load_voices() -> dict[str, str]:
    env = os.environ.get("GEMINI_VOICES", "").strip()
    if not env:
        return dict(DEFAULT_VOICES)
    voices = {}
    for pair in env.split(","):
        if "=" in pair:
            name, voice = pair.split("=", 1)
            voices[name.strip()] = voice.strip()
    return voices or dict(DEFAULT_VOICES)


def parse_turns(transcript: str, speakers: set[str]) -> list[tuple[str, str]]:
    """Parse 'Name: text' lines into (speaker, text) turns.

    Lines that don't start with a known speaker are appended to the current
    turn (so a wrapped/multi-line utterance stays intact)."""
    turns: list[list[str]] = []
    for line in transcript.splitlines():
        m = _TURN_RE.match(line)
        if m and m.group(1).strip() in speakers:
            turns.append([m.group(1).strip(), m.group(2).strip()])
        elif turns and line.strip():
            turns[-1][1] += " " + line.strip()
    return [(s, t.strip()) for s, t in turns if t.strip()]


def chunk_turns(turns: list[tuple[str, str]], max_chars: int = MAX_CHARS) -> list[list[tuple[str, str]]]:
    chunks: list[list[tuple[str, str]]] = []
    cur: list[tuple[str, str]] = []
    n = 0
    for s, t in turns:
        ln = len(s) + 2 + len(t) + 1
        if cur and n + ln > max_chars:
            chunks.append(cur)
            cur, n = [], 0
        cur.append((s, t))
        n += ln
    if cur:
        chunks.append(cur)
    return chunks


def render_chunk(chunk: list[tuple[str, str]]) -> str:
    return "\n".join(f"{s}: {t}" for s, t in chunk)


def merge_consecutive_turns(
    turns: list[tuple[str, str]], max_chars: int = MAX_CHARS
) -> list[tuple[str, str]]:
    """Join adjacent turns by the same speaker (capped at max_chars) so
    per-turn synthesis makes one request per contiguous speaker run."""
    merged: list[tuple[str, str]] = []
    for s, t in turns:
        if merged and merged[-1][0] == s and len(merged[-1][1]) + len(t) + 1 <= max_chars:
            merged[-1] = (s, merged[-1][1] + " " + t)
        else:
            merged.append((s, t))
    return merged


# Gemini TTS takes natural-language performance direction in the input.
# Override with GEMINI_TTS_STYLE.
# Deliberately minimal: heavy character/energy direction was found to
# over-steer the model — exaggerated emphasis and even timbre morphing
# (voices bending away from their configured prebuilt sound). The assigned
# voices carry the characters; the direction only asks for calm delivery.
DEFAULT_STYLE = (
    "Read this podcast conversation in a calm, natural, understated way: "
    "even pacing, plain conversational emphasis, never dramatic or "
    "exaggerated. Use each speaker's assigned voice exactly as configured, "
    "unchanged from start to finish."
)
DEFAULT_STYLE_SINGLE = (
    "Read this podcast speech in a calm, natural, understated way: even "
    "pacing, plain conversational emphasis, never dramatic or exaggerated."
)


def build_request_body(text: str, voices: dict[str, str], model: str) -> dict:
    """Interactions-API TTS request body. Multi-speaker requests name each
    speaker in speech_config and in the input; single-speaker requests take
    only a voice (no "speaker" field — the API 400s on it) and plain text
    with no speaker label."""
    style = os.environ.get("GEMINI_TTS_STYLE")
    if len(voices) > 1:
        who = " and ".join(voices.keys())
        style = style or DEFAULT_STYLE
        input_text = f"{style}\nTTS the following conversation between {who}:\n{text}"
        speech_config = [{"speaker": s, "voice": v} for s, v in voices.items()]
    else:
        style = style or DEFAULT_STYLE_SINGLE
        input_text = f"{style}\n{text}"
        speech_config = [{"voice": v} for v in voices.values()]
    return {
        "model": model,
        "input": input_text,
        "response_format": {"type": "audio"},
        "generation_config": {"speech_config": speech_config},
    }


def _find_audio(node) -> tuple[bytes, int] | None:
    """Walk the response JSON for the first base64 audio payload (a dict with a
    'data' string and an audio-ish mime), tolerant of schema variations."""
    if isinstance(node, dict):
        data = node.get("data")
        mime = node.get("mimeType") or node.get("mime_type") or node.get("mime") or ""
        if isinstance(data, str) and len(data) > 500 and (
            "audio" in mime.lower() or "output_audio" in str(node.keys()).lower() or not mime
        ):
            try:
                raw = base64.b64decode(data)
            except Exception:
                raw = None
            if raw and len(raw) > 200:
                rate = DEFAULT_RATE
                m = re.search(r"rate=(\d+)", mime) or re.search(r"(\d{4,6})", str(
                    node.get("sampleRateHertz") or node.get("sample_rate") or ""))
                if m:
                    rate = int(m.group(1))
                return raw, rate
        for v in node.values():
            found = _find_audio(v)
            if found:
                return found
    elif isinstance(node, list):
        for v in node:
            found = _find_audio(v)
            if found:
                return found
    return None


# Keep under the ~10 requests/minute TTS limit when per-turn requests
# return quickly; a 429 retry still handles the occasional overshoot.
MIN_REQUEST_INTERVAL_S = float(os.environ.get("GEMINI_TTS_MIN_INTERVAL_S") or 6.0)
_last_request_ts = 0.0


def _synthesize_chunk(text: str, voices: dict[str, str], api_key: str, model: str) -> tuple[bytes, int]:
    global _last_request_ts
    since = time.monotonic() - _last_request_ts
    if since < MIN_REQUEST_INTERVAL_S:
        time.sleep(MIN_REQUEST_INTERVAL_S - since)
    _last_request_ts = time.monotonic()
    for attempt in range(4):
        resp = requests.post(
            API_URL,
            headers={
                "x-goog-api-key": api_key,
                "Content-Type": "application/json",
                "Api-Revision": API_REVISION,
            },
            json=build_request_body(text, voices, model),
            timeout=240,
        )
        # Per-minute rate limits clear on their own — wait them out. (A daily
        # quota exhaustion also returns 429; after the retries it falls
        # through to the caller's edge-tts fallback.)
        if resp.status_code == 429 and attempt < 3:
            retry_after = resp.headers.get("Retry-After")
            wait = min(float(retry_after) if retry_after else 30.0 * (attempt + 1), 120)
            log.info("Gemini TTS rate-limited (429); retrying in %.0fs", wait)
            time.sleep(wait)
            continue
        break
    if resp.status_code >= 400:
        raise RuntimeError(f"Gemini TTS HTTP {resp.status_code}: {resp.text[:300]}")
    data = resp.json()
    found = _find_audio(data)
    if found:
        return found
    raise RuntimeError(f"Gemini TTS returned no audio: {str(data)[:300]}")


def synthesize_dialogue(
    transcript: str,
    out_path: Path,
    api_key: str | None = None,
    model: str = DEFAULT_MODEL,
    voices: dict[str, str] | None = None,
) -> Path:
    api_key = api_key or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set")
    voices = voices or load_voices()
    segments = split_segments(transcript)
    seg_turns = [parse_turns(seg, set(voices)) for seg in segments]
    seg_turns = [t for t in seg_turns if t]
    if not seg_turns:
        raise RuntimeError(
            "No dialogue turns parsed — the script must use 'Maya:'/'Sam:' lines"
        )

    # Default mode synthesizes each speaker's turns as separate SINGLE-voice
    # requests: with exactly one voice configured per request, the model has
    # no speaker-to-voice assignment to get wrong, so voices can never swap
    # or gender-drift mid-episode (which multi-speaker mode does, per chunk).
    # GEMINI_TTS_MODE=multi restores whole-conversation chunks.
    mode = (os.environ.get("GEMINI_TTS_MODE") or "turns").strip().lower()
    pcm = bytearray()
    rate = DEFAULT_RATE
    done = 0
    if mode == "multi":
        # Chunk within each segment so [BREAK] boundaries align with synthesis
        # boundaries and the stinger can be spliced between them.
        seg_chunks = [chunk_turns(t) for t in seg_turns]
        total = sum(len(c) for c in seg_chunks)
        for si, chunks in enumerate(seg_chunks):
            if si:
                pcm.extend(_stinger_pcm(rate))
            for chunk in chunks:
                done += 1
                log.info("Gemini TTS chunk %d/%d", done, total)
                data, rate = _synthesize_chunk(render_chunk(chunk), voices, api_key, model)
                pcm.extend(data)
    else:
        seg_groups = [merge_consecutive_turns(t) for t in seg_turns]
        total = sum(len(g) for g in seg_groups)
        gap = b"\x00\x00" * int(TURN_GAP_S * rate)
        for si, groups in enumerate(seg_groups):
            if si:
                pcm.extend(_stinger_pcm(rate))
            for gi, (speaker, text) in enumerate(groups):
                done += 1
                log.info("Gemini TTS turn %d/%d (%s)", done, total, speaker)
                data, rate = _synthesize_chunk(
                    text, {speaker: voices[speaker]}, api_key, model
                )
                if gi:
                    pcm.extend(gap)
                pcm.extend(data)

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav_path = tmp.name
    try:
        with wave.open(wav_path, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)  # 16-bit
            w.setframerate(rate)
            w.writeframes(bytes(pcm))
        subprocess.run(
            ["ffmpeg", "-y", "-i", wav_path, "-b:a", "128k", str(out_path)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    finally:
        os.path.exists(wav_path) and os.unlink(wav_path)

    if not out_path.exists() or out_path.stat().st_size == 0:
        raise RuntimeError("ffmpeg produced no audio")
    return out_path
