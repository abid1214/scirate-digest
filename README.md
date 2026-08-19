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
2. Set up a **self-hosted runner** (see below) — required because SciRate is
   behind Cloudflare, which blocks GitHub's shared datacenter runners. A
   runner on your own machine uses a normal residential/office IP that
   Cloudflare lets through.
3. The workflow
   ([`.github/workflows/daily-digest.yml`](.github/workflows/daily-digest.yml))
   runs daily at 13:30 UTC, and can also be triggered manually from the
   Actions tab (custom paper count, ranking window, or explicit arXiv IDs).

Text-to-speech uses [`edge-tts`](https://github.com/rany2/edge-tts), which is
free and needs no key — the Claude API key is the only credential required.

### Self-hosted runner (one-time, ~10 minutes)

Pick an always-on machine on a home/office network (a Linux box is easiest;
macOS works too). It needs Python 3.12+, `git`, and the
[GitHub CLI (`gh`)](https://cli.github.com/) on its `PATH`.

1. In the repo: **Settings → Actions → Runners → New self-hosted runner**.
   Choose the OS, then run the download/configure commands GitHub shows you
   (`./config.sh --url https://github.com/abid1214/scirate-digest --token …`).
2. Start it as a service so it survives reboots and runs unattended:
   - Linux: `sudo ./svc.sh install && sudo ./svc.sh start`
   - macOS: `./svc.sh install && ./svc.sh start`
   (Or just `./run.sh` in a terminal to try it once.)
3. That's it — the workflow already targets `runs-on: self-hosted`. Trigger a
   manual run from the **Actions** tab to confirm; the daily schedule then
   fires on its own.

**On Windows:** install [Git for Windows](https://git-scm.com/download/win)
(provides Git Bash, which the workflow's steps use), Python 3.12+, and the
GitHub CLI. Register the runner from **PowerShell** with the commands GitHub
shows you, then `.\svc.ps1 install` / `.\svc.ps1 start` (older runners use
`.\svc install` / `.\svc start`) to run it as a Windows service. The browser
runs headless on Windows, which passes Cloudflare fine from a home IP. Avoid
putting the runner's working folder inside **OneDrive** — the constant churn in
`.git` and the runner's `_work` directory fights the sync client; a plain path
like `C:\actions-runner` is better. Cloning the repo into your OneDrive dev
folder for local use is fine.

Notes:
- The machine must be **awake at 13:30 UTC** for the scheduled run. Adjust the
  `cron` in the workflow to a convenient local time if needed (it's in UTC).
- The first run downloads the Camoufox and Playwright browsers (a few hundred
  MB); later runs reuse them.
- On a headless Linux runner the job installs and uses `xvfb` automatically so
  the browser can run "headed" (which clears Cloudflare most reliably). On a
  desktop session it uses your real display. If neither is available it falls
  back to a headless browser, which usually still passes from a home IP.
- If your runner can't use `sudo`, pre-install `xvfb` yourself
  (`sudo apt-get install -y xvfb`) or ignore it and rely on the headless
  fallback.

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
