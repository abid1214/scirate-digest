"""Turn the podcast script into an MP3 using Microsoft Edge neural TTS.

edge-tts is free and needs no API key, which keeps the only paid dependency
of this project the Claude API. The script is synthesized in one pass;
edge-tts splits long text into requests internally.
"""

from __future__ import annotations

import asyncio
from pathlib import Path

DEFAULT_VOICE = "en-US-AndrewMultilingualNeural"


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
