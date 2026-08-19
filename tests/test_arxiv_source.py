import gzip
import io
import tarfile
from pathlib import Path

from scirate_digest.arxiv_source import (
    extract_source_text,
    latex_to_text,
    parse_atom,
)

FIXTURES = Path(__file__).parent / "fixtures"

MAIN_TEX = r"""
\documentclass{article}
\usepackage{amsmath} % preamble comment
\begin{document}
\title{Quantum Advantage in Widget Sorting}
\section{Introduction}
Widgets are important. % trailing comment
We achieve a 50\% speedup.
\includegraphics[width=\linewidth]{fig1.pdf}
\begin{thebibliography}{9}
\bibitem{x} Someone. Something.
\end{thebibliography}
\end{document}
"""


def _tarball(files: dict[str, str]) -> bytes:
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for name, content in files.items():
            data = content.encode()
            info = tarfile.TarInfo(name=name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
    return buf.getvalue()


def test_parse_atom_fixture():
    entries = parse_atom((FIXTURES / "arxiv_atom.xml").read_text())
    assert entries[0][0] == "2508.11111"  # version suffix stripped
    assert entries[0][1] == "Quantum Advantage in Widget Sorting"  # whitespace squashed
    assert entries[0][2] == ["Alice Ansatz", "Bob Bloch"]
    assert entries[1][0] == "quant-ph/0301040"


def test_extract_from_tarball():
    blob = _tarball({"main.tex": MAIN_TEX, "appendix.tex": r"\section{Appendix} More."})
    text = extract_source_text(blob)
    assert "Widgets are important." in text
    assert "More." in text
    # main file (with \begin{document}) comes first
    assert text.index("Widgets are important.") < text.index("More.")


def test_extract_single_gzipped_tex():
    blob = gzip.compress(MAIN_TEX.encode())
    text = extract_source_text(blob)
    assert "50\\% speedup" in text


def test_extract_pdf_returns_none():
    assert extract_source_text(b"%PDF-1.5 blah blah") is None


def test_extract_truncates():
    blob = _tarball({"main.tex": "\\begin{document}" + "x" * 100_000 + "\\end{document}"})
    text = extract_source_text(blob, max_chars=1000)
    assert len(text) < 1100
    assert text.endswith("[... source truncated ...]")


def test_latex_to_text_cleans():
    out = latex_to_text(MAIN_TEX)
    assert "preamble comment" not in out
    assert "trailing comment" not in out
    assert "thebibliography" not in out
    assert "includegraphics" not in out
    assert "50\\% speedup" in out  # escaped percent is not a comment
    assert "\\usepackage" not in out  # preamble dropped
