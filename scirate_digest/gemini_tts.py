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
DEFAULT_MODEL = os.environ.get("GEMINI_TTS_MODEL") or "gemini-3.1-flash-tts-preview"
API_REVISION = os.environ.get("GEMINI_API_REVISION") or "2026-05-20"

# Host name (as it appears in the script) -> Gemini prebuilt voice name.
# Override with GEMINI_VOICES="Maya=Kore,Sam=Puck".
DEFAULT_VOICES = {"Maya": "Kore", "Sam": "Puck"}

# Max characters of transcript per TTS request (split only at turn
# boundaries). Larger chunks mean fewer requests, which matters on the
# free tier's small daily TTS quota.
MAX_CHARS = 4500
DEFAULT_RATE = 24000

_TURN_RE = re.compile(r"^\s*([A-Za-z][\w .'-]*?):\s*(.*)$")


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


# Gemini TTS takes natural-language performance direction in the input.
# Override with GEMINI_TTS_STYLE.
DEFAULT_STYLE = (
    "Perform this as a lively, natural podcast conversation between two "
    "friends — never a read-aloud. Maya sounds warm, curious and quick, "
    "reacting genuinely to what she hears; Sam is relaxed, wry and "
    "thoughtful, like a scientist explaining something he loves. Vary pace "
    "and intonation naturally, let energy rise on exciting points, and "
    "leave tiny beats at speaker handoffs."
)


def build_request_body(text: str, voices: dict[str, str], model: str) -> dict:
    """Interactions-API multi-speaker TTS request body. The input wraps the
    transcript as a conversation and names the speakers, matching speech_config."""
    who = " and ".join(voices.keys())
    style = os.environ.get("GEMINI_TTS_STYLE") or DEFAULT_STYLE
    return {
        "model": model,
        "input": f"{style}\nTTS the following conversation between {who}:\n{text}",
        "response_format": {"type": "audio"},
        "generation_config": {
            "speech_config": [{"speaker": s, "voice": v} for s, v in voices.items()]
        },
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


def _synthesize_chunk(text: str, voices: dict[str, str], api_key: str, model: str) -> tuple[bytes, int]:
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
    turns = parse_turns(transcript, set(voices))
    if not turns:
        raise RuntimeError(
            "No dialogue turns parsed — the script must use 'Maya:'/'Sam:' lines"
        )

    pcm = bytearray()
    rate = DEFAULT_RATE
    chunks = chunk_turns(turns)
    for i, chunk in enumerate(chunks, 1):
        log.info("Gemini TTS chunk %d/%d", i, len(chunks))
        data, rate = _synthesize_chunk(render_chunk(chunk), voices, api_key, model)
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
