# SciRate Daily Digest 🎙️

Every day, this repo looks at [SciRate](https://scirate.com/) for the top 5
most-scited new arXiv papers, downloads each paper's **full LaTeX source**
from arXiv, has Claude read it and write an executive summary and analysis,
and then turns the whole thing into an **audio podcast episode** — a
two-host conversation (Maya & Sam) that leads with intuition and
implications rather than notation.

**Ask the hosts:** open a GitHub issue whose title starts with `Q:`
([one-tap link](https://github.com/abid1214/scirate-digest/issues/new?title=Q%3A%20))
and the next episode opens with a mailbag segment answering it; the issue is
closed automatically with a link to that episode. Every episode's show notes
also carry the ask link.

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

The daily job runs on GitHub's free hosted runners. Because SciRate is behind
Cloudflare — which blocks datacenter IPs — the scrape is routed through a
**scraping-API service** that fetches the page from residential proxies. No
server or self-hosted runner to maintain.

1. Add a repository secret **`ANTHROPIC_API_KEY`**
   (Settings → Secrets and variables → Actions).
2. Sign up for a scraping API (free tiers easily cover one page/day) and add
   its key as a secret:
   - [**ScraperAPI**](https://www.scraperapi.com/) → secret **`SCRAPERAPI_KEY`**
     (free tier ≈ 1,000 credits/month), **or**
   - [**ScrapingBee**](https://www.scrapingbee.com/) → secret **`SCRAPINGBEE_KEY`**
     (free trial ≈ 1,000 calls).

   Set whichever one you signed up for; the scraper auto-detects which key is
   present. If SciRate ever needs a stronger proxy, add
   `SCRAPERAPI_EXTRA=ultra_premium=true` (or `SCRAPINGBEE_EXTRA=...`) as a
   variable — those are merged into the request.
3. The workflow
   ([`.github/workflows/daily-digest.yml`](.github/workflows/daily-digest.yml))
   runs daily at 13:30 UTC, and can also be triggered manually from the
   Actions tab (custom paper count, ranking window, or explicit arXiv IDs).

### Voice: two-host Gemini TTS (optional) or free edge-tts

By default (no extra key) episodes are a single narrator via
[`edge-tts`](https://github.com/rany2/edge-tts) — free, no credential.

For a polished **two-host conversation** (Maya & Sam discussing the papers),
add a **`GEMINI_API_KEY`** secret from
[Google AI Studio](https://aistudio.google.com/apikey). When present, Claude
writes a two-voice dialogue script and Google's Gemini multi-speaker TTS
performs it; the runner transcodes the audio to MP3 with ffmpeg. Claude still
does all the paper-reading and analysis — Gemini only supplies the voices.

Optional repository *variables* (Settings → Secrets and variables → Actions →
Variables) tune it: `GEMINI_TTS_MODEL` (default
`gemini-3.1-flash-tts-preview`, via Google's Interactions API) and
`GEMINI_VOICES` (default
`Maya=Kore,Sam=Puck` — any two [Gemini prebuilt voices](https://ai.google.dev/gemini-api/docs/speech-generation)).

Locally, `--voice-engine gemini|edge|auto` overrides the choice.

So the only required credentials are your Claude API key and one scraping-API
key; the Gemini key is optional and only upgrades the voice.

> **No scraping key?** The scrape falls back through Camoufox, Playwright, the
> Jina Reader proxy, and a recent Wayback snapshot — but from a datacenter IP
> those are unreliable, which is why the scraping API is the recommended path.
> Alternatively, run the job on a self-hosted runner on a home/office network,
> whose residential IP passes Cloudflare directly (see git history for that
> variant of the workflow).

## Listen on your phone (podcast feed)

Each run updates a podcast **RSS feed** under `docs/`, served free by GitHub
Pages. Subscribe once and every new episode auto-downloads to your podcast app.

**Enable it once:** repo **Settings → Pages → Build and deployment → Deploy
from a branch**, choose branch **`main`** and folder **`/docs`**, Save. After
the first deploy your feed lives at:

```
https://abid1214.github.io/scirate-digest/feed.xml
```

Add that URL in Apple Podcasts, Overcast, Pocket Casts, or Spotify ("Add a
show by URL"). The landing page at
`https://abid1214.github.io/scirate-digest/` lists every episode.

Optional: drop a square **`docs/cover.jpg`** (1400×1400+; required only if you
ever submit to the Apple Podcasts directory) and it's picked up automatically.

## Running locally

```bash
pip install -e ".[browser]"
playwright install chromium   # only needed if SciRate raises a Cloudflare challenge
export ANTHROPIC_API_KEY=sk-ant-...

scirate-digest                          # full run: top 5, last 1 day
scirate-digest --top 10 --range 7       # top 10 of the last week
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
  SciRate markup changes won't corrupt the digest. Because SciRate is behind
  Cloudflare, the scraper walks a chain of strategies until one yields a page
  that actually parses into papers: plain HTTP, Camoufox (a fingerprint-
  spoofing Firefox), Playwright Chromium, the Jina Reader proxy, and finally a
  recent Wayback Machine snapshot of the front page. From a datacenter IP all
  of these are blocked — hence the self-hosted runner.
- **Real source, not just abstracts.** Summaries are generated from the
  paper's extracted LaTeX body (comments, preamble, bibliography, and figure
  binaries stripped; math kept). PDF-only submissions fall back to the
  abstract, and the summary says so.
- **Refusal fallbacks.** On Opus 5 / Fable 5, server-side refusal fallbacks
  are enabled so a safety decline on one paper falls back to another model
  rather than dropping the paper.
- **No repeats.** Papers stay hot on SciRate for days, so each episode
  filters out anything covered by a past episode (tracked via the committed
  `digests/<date>/papers.json` history) and fills the top 5 with fresh
  papers from a larger scraped pool. Override with `--allow-repeats`.
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
