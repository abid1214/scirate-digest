"""Shared data structures."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict


@dataclass
class Paper:
    """A paper ranked on SciRate, enriched with arXiv metadata and source text."""

    uid: str  # arXiv identifier, e.g. "2408.12345" or "quant-ph/0301040"
    title: str = ""
    authors: list[str] = field(default_factory=list)
    abstract: str = ""
    scites: int | None = None
    source_text: str | None = None  # extracted LaTeX body, None if unavailable
    summary: str | None = None  # generated executive summary + analysis

    @property
    def abs_url(self) -> str:
        return f"https://arxiv.org/abs/{self.uid}"

    @property
    def scirate_url(self) -> str:
        return f"https://scirate.com/arxiv/{self.uid}"

    def to_dict(self) -> dict:
        d = asdict(self)
        d["abs_url"] = self.abs_url
        d["scirate_url"] = self.scirate_url
        return d
