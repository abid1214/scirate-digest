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
# Microsoft's newest conversational neural voices. These are deterministic:
# the same voice name always renders the same speaker, so the hosts never
# drift or swap. Override with EDGE_DIALOGUE_VOICES="Maya=...,Sam=...".
DEFAULT_DIALOGUE_VOICES = {
    "Maya": "en-US-EmmaMultilingualNeural",
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


def _concat_mp3(paths: list[Path], out_path: Path, reencode: bool = False) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        for p in paths:
            f.write(f"file '{p}'\n")
        list_file = f.name
    try:
        # Stream copy first (when all segments share edge's codec params);
        # re-encode when inputs are mixed (e.g. a music stinger) or copy fails.
        attempts = [["-b:a", "128k"]] if reencode else [["-c", "copy"], ["-b:a", "128k"]]
        for extra in attempts:
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


def _break_audio_file(tmp_dir: Path) -> Path:
    """The [BREAK] bumper: the stinger asset padded with silence, or plain
    silence if the asset is missing. Rendered once per run into tmp_dir."""
    from .gemini_tts import STINGER_PATH, BREAK_SILENCE_S

    out = tmp_dir / "break.mp3"
    if os.path.exists(STINGER_PATH):
        r = subprocess.run(
            ["ffmpeg", "-y", "-i", str(STINGER_PATH),
             "-af", f"adelay={int(BREAK_SILENCE_S*1000)}|{int(BREAK_SILENCE_S*1000)},"
                    f"apad=pad_dur={BREAK_SILENCE_S}",
             "-ac", "1", "-ar", "24000", "-b:a", "96k", str(out)],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        if r.returncode == 0 and out.exists() and out.stat().st_size > 0:
            return out
    subprocess.run(
        ["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
         "-t", "1.6", "-b:a", "48k", str(out)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True,
    )
    return out


def synthesize_dialogue(transcript: str, out_path: Path) -> Path:
    """Two-voice fallback: render each speaker turn with its host's edge
    voice and stitch, inserting the break bumper at [BREAK] markers. Raises
    if the transcript has no Maya:/Sam: turns."""
    from .gemini_tts import parse_turns, split_segments

    voices = load_dialogue_voices()
    segments = [parse_turns(seg, set(voices)) for seg in split_segments(transcript)]
    segments = [s for s in segments if s]
    if not segments:
        raise RuntimeError("no dialogue turns to synthesize")
    turns = [t for seg in segments for t in seg]

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        seg_dir = Path(td)
        log.info(
            "edge-tts dialogue fallback: %d turns, 2 voices, %d segments",
            len(turns), len(segments),
        )
        paths = asyncio.run(_synthesize_turns(turns, voices, seg_dir))
        missing = [p for p in paths if not p.exists() or p.stat().st_size == 0]
        if missing:
            raise RuntimeError(f"{len(missing)} audio segments failed to render")

        # Interleave the break bumper between segments.
        has_breaks = len(segments) > 1
        ordered: list[Path] = []
        i = 0
        break_file = _break_audio_file(seg_dir) if has_breaks else None
        for si, seg in enumerate(segments):
            if si and break_file is not None:
                ordered.append(break_file)
            ordered.extend(paths[i:i + len(seg)])
            i += len(seg)
        _concat_mp3(ordered, out_path, reencode=has_breaks)
    if not out_path.exists() or out_path.stat().st_size == 0:
        raise RuntimeError("TTS produced no audio")
    return out_path
