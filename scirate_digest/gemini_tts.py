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
import wave
from pathlib import Path

import requests

log = logging.getLogger(__name__)

API_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
DEFAULT_MODEL = os.environ.get("GEMINI_TTS_MODEL", "gemini-2.5-flash-preview-tts")

# Host name (as it appears in the script) -> Gemini prebuilt voice name.
# Override with GEMINI_VOICES="Maya=Kore,Sam=Puck".
DEFAULT_VOICES = {"Maya": "Kore", "Sam": "Puck"}

# Max characters of transcript per TTS request (split only at turn boundaries).
MAX_CHARS = 2400
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


def _synthesize_chunk(text: str, voices: dict[str, str], api_key: str, model: str) -> tuple[bytes, int]:
    body = {
        "contents": [{"parts": [{"text": text}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {
                "multiSpeakerVoiceConfig": {
                    "speakerVoiceConfigs": [
                        {"speaker": s, "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": v}}}
                        for s, v in voices.items()
                    ]
                }
            },
        },
    }
    resp = requests.post(
        API_URL.format(model=model), params={"key": api_key}, json=body, timeout=240
    )
    if resp.status_code >= 400:
        raise RuntimeError(f"Gemini TTS HTTP {resp.status_code}: {resp.text[:300]}")
    data = resp.json()
    parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
    for p in parts:
        inline = p.get("inlineData") or p.get("inline_data")
        if inline and inline.get("data"):
            rate = DEFAULT_RATE
            mime = inline.get("mimeType") or inline.get("mime_type") or ""
            m = re.search(r"rate=(\d+)", mime)
            if m:
                rate = int(m.group(1))
            return base64.b64decode(inline["data"]), rate
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
