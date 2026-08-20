"""Turn the podcast script into an MP3 using Microsoft Edge neural TTS.

edge-tts is free and needs no API key, which keeps the only paid dependency
of this project the Claude API. Two modes:

- ``synthesize``: single narrator, one pass (edge-tts splits long text
  internally).
- ``synthesize_dialogue``: two-host mode used when Gemini TTS is
  unavailable — each 'Maya:'/'Sam:' turn is rendered with that host's own
  edge voice and the segments are stitched with ffmpeg, so the fallback
  still sounds like two people.
"""

from __future__ import annotations

import asyncio
import logging
import os
import subprocess
import tempfile
from pathlib import Path

log = logging.getLogger(__name__)

DEFAULT_VOICE = "en-US-AndrewMultilingualNeural"

# Host name -> edge voice for the two-host fallback.
# Override with EDGE_DIALOGUE_VOICES="Maya=en-US-AriaNeural,Sam=...".
DEFAULT_DIALOGUE_VOICES = {
    "Maya": "en-US-AriaNeural",
    "Sam": "en-US-AndrewMultilingualNeural",
}


def load_dialogue_voices() -> dict[str, str]:
    env = os.environ.get("EDGE_DIALOGUE_VOICES", "").strip()
    if not env:
        return dict(DEFAULT_DIALOGUE_VOICES)
    voices = {}
    for pair in env.split(","):
        if "=" in pair:
            name, voice = pair.split("=", 1)
            voices[name.strip()] = voice.strip()
    return voices or dict(DEFAULT_DIALOGUE_VOICES)


async def _synthesize(text: str, out_path: Path, voice: str) -> None:
    import edge_tts

    communicate = edge_tts.Communicate(text, voice=voice)
    await communicate.save(str(out_path))


def synthesize(text: str, out_path: Path, voice: str = DEFAULT_VOICE) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    asyncio.run(_synthesize(text, out_path, voice))
    if not out_path.exists() or out_path.stat().st_size == 0:
        raise RuntimeError("TTS produced no audio")
    return out_path


async def _synthesize_turns(turns, voices, seg_dir: Path) -> list[Path]:
    import edge_tts

    sem = asyncio.Semaphore(4)  # be kind to the free endpoint
    paths = [seg_dir / f"seg{i:04d}.mp3" for i in range(len(turns))]

    async def one(i, speaker, text):
        async with sem:
            await edge_tts.Communicate(text, voice=voices[speaker]).save(str(paths[i]))

    await asyncio.gather(*(one(i, s, t) for i, (s, t) in enumerate(turns)))
    return paths


def _concat_mp3(paths: list[Path], out_path: Path) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        for p in paths:
            f.write(f"file '{p}'\n")
        list_file = f.name
    try:
        # Stream copy first (all segments share edge's codec params);
        # re-encode as a fallback if copy is rejected.
        for extra in (["-c", "copy"], ["-b:a", "128k"]):
            r = subprocess.run(
                ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file,
                 *extra, str(out_path)],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            if r.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0:
                return
        raise RuntimeError("ffmpeg failed to concatenate audio segments")
    finally:
        os.unlink(list_file)


def synthesize_dialogue(transcript: str, out_path: Path) -> Path:
    """Two-voice fallback: render each speaker turn with its host's edge
    voice and stitch. Raises if the transcript has no Maya:/Sam: turns."""
    from .gemini_tts import parse_turns  # reuse the turn parser

    voices = load_dialogue_voices()
    turns = parse_turns(transcript, set(voices))
    if not turns:
        raise RuntimeError("no dialogue turns to synthesize")

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        seg_dir = Path(td)
        log.info("edge-tts dialogue fallback: %d turns, 2 voices", len(turns))
        paths = asyncio.run(_synthesize_turns(turns, voices, seg_dir))
        missing = [p for p in paths if not p.exists() or p.stat().st_size == 0]
        if missing:
            raise RuntimeError(f"{len(missing)} audio segments failed to render")
        _concat_mp3(paths, out_path)
    if not out_path.exists() or out_path.stat().st_size == 0:
        raise RuntimeError("TTS produced no audio")
    return out_path
