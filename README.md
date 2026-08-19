# SciRate Daily Digest 🎙️

Every day, this repo looks at [SciRate](https://scirate.com/) for the top 10
most-scited new arXiv papers, downloads each paper's **full LaTeX source**
from arXiv, has Claude read it and write an executive summary and analysis,
and then turns the whole thing into an **audio podcast episode**.

## How it works

```
SciRate front page (?range=1)          ──►  ranked top-10 arXiv IDs (+ scite counts)
arXiv API                              ──►  titles, authors, abstracts
arXiv /e-print/<id> tarballs           ──►  extracted & cleaned LaTeX body
Claude (per paper)                     ──►  executive summary + analysis
Claude (whole episode)                 ──►  single-host podcast narration script
Microsoft Edge neural TTS (edge-tts)   ──►  digest.mp3
```

Each daily run produces, under `output/<YYYY-MM-DD>/`:

| File                 | What it is                                             |
| -------------------- | ------------------------------------------------------ |
| `digest.md`          | Written digest: per-paper summary + analysis, links    |
| `podcast_script.txt` | The full narration script                              |
| `digest.mp3`         | The podcast episode (~15 min)                          |
| `papers.json`        | Structured data for everything above                   |

The GitHub Actions workflow commits `digest.md`, the script, and
`papers.json` to `digests/<date>/` and attaches the MP3 to a GitHub release
tagged `digest-<date>` (MP3s stay out of git history).

## Setup (GitHub Actions)

1. Add a repository secret **`ANTHROPIC_API_KEY`**
   (Settings → Secrets and variables → Actions).
2. Make sure Actions are enabled. The workflow
   ([`.github/workflows/daily-digest.yml`](.github/workflows/daily-digest.yml))
   runs daily at 13:30 UTC, and can also be triggered manually from the
   Actions tab (with custom paper count / ranking window).

Text-to-speech uses [`edge-tts`](https://github.com/rany2/edge-tts), which is
free and needs no key — the Claude API key is the only credential required.

## Running locally

```bash
pip install -e ".[browser]"
playwright install chromium   # only needed if SciRate raises a Cloudflare challenge
export ANTHROPIC_API_KEY=sk-ant-...

scirate-digest                          # full run: top 10, last 1 day
scirate-digest --top 5 --range 7        # top 5 of the last week
scirate-digest --category quant-ph      # a single arXiv category feed
scirate-digest --ids 2408.12345 ...     # skip scraping, digest specific papers
scirate-digest --skip-audio             # everything except TTS
scirate-digest --skip-summaries        # scrape + source extraction only (no API calls)
```

Useful knobs: `--model` (default `claude-opus-5`), `--voice` (any
`edge-tts --list-voices` name), `--max-source-chars` (per-paper LaTeX budget,
default 60,000).

## Design notes & limitations

- **Robust scraping.** Only the *ranked list of arXiv IDs* is taken from
  SciRate; titles, authors, and abstracts come from the arXiv API, so minor
  SciRate markup changes won't corrupt the digest. If Cloudflare challenges
  the plain HTTP request, the scraper retries in headless Chromium.
- **Real source, not just abstracts.** Summaries are generated from the
  paper's extracted LaTeX body (comments, preamble, bibliography, and figure
  binaries stripped; math kept). PDF-only submissions fall back to the
  abstract, and the summary says so.
- **Refusal fallbacks.** On Opus 5 / Fable 5, server-side refusal fallbacks
  are enabled so a safety decline on one paper falls back to another model
  rather than dropping the paper.
- **Politeness.** arXiv requests are spaced 3 s apart and retried with
  backoff on 429/5xx.
- **Cost.** A daily run sends ~10 papers × up to ~60k characters of LaTeX
  plus one script-writing call — roughly 200–300k input tokens/day on Opus 5.
  Use `--model claude-sonnet-5` (or set it in the workflow) to cut costs.

## Development

```bash
pip install -e ".[dev]"
pytest
```
