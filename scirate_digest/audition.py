"""Render a side-by-side sample of candidate host voices.

Picking podcast voices from name and reputation has been unreliable — the
only real test is listening. This renders one MP3 in which each candidate
reads the same few lines, announced by index, so a pair can be chosen by ear
and then set via the EDGE_DIALOGUE_VOICES repo variable.

    python -m scirate_digest.audition \
        --voices en-US-AvaMultilingualNeural,en-US-JennyNeural \
        --out audition.mp3
"""

from __future__ import annotations

import argparse
import logging
import tempfile
from pathlib import Path

from . import tts

log = logging.getLogger(__name__)

# Long enough to hear prosody and warmth, short enough to compare quickly.
SAMPLE = (
    "Here's the part I keep coming back to. They didn't make the decoder "
    "faster — they changed what the decoder has to do. Once you only need "
    "the syndrome differences, the whole latency budget looks different. "
    "That's the kind of result that quietly moves a roadmap."
)
ANNOUNCER = "en-US-AndrewMultilingualNeural"


def _short_name(voice: str) -> str:
    """en-US-AvaMultilingualNeural -> 'Ava Multilingual'."""
    core = voice.split("-", 2)[-1].removesuffix("Neural")
    out = []
    for ch in core:
        if ch.isupper() and out and not out[-1].endswith(" "):
            out.append(" ")
        out.append(ch)
    return "".join(out).strip()


def render(voices: list[str], out_path: Path, sample: str = SAMPLE,
           announcer: str = ANNOUNCER) -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        parts: list[Path] = []
        for i, voice in enumerate(voices, 1):
            label = tmp / f"{i:02d}-label.mp3"
            body = tmp / f"{i:02d}-body.mp3"
            tts.synthesize(f"Option {i}. {_short_name(voice)}.", label,
                           voice=announcer)
            log.info("Rendering option %d: %s", i, voice)
            tts.synthesize(sample, body, voice=voice)
            parts += [label, tts._break_audio_file(tmp / f"gap{i}"), body,
                      tts._break_audio_file(tmp / f"gap{i}b")]
        tts._concat_mp3(parts, out_path, reencode=True)
    return out_path


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    ap = argparse.ArgumentParser(description="Audition candidate host voices.")
    ap.add_argument("--voices", required=True,
                    help="comma-separated edge-tts voice names")
    ap.add_argument("--out", type=Path, default=Path("audition.mp3"))
    ap.add_argument("--text", default=SAMPLE, help="sample line to read")
    args = ap.parse_args(argv)
    voices = [v.strip() for v in args.voices.split(",") if v.strip()]
    if not voices:
        raise SystemExit("no voices given")
    path = render(voices, args.out, sample=args.text)
    print(f"wrote {path} ({path.stat().st_size / 1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
