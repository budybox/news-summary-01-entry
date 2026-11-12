# news-summary-01

Entry for the make.fun competition **news-summary-01** — "Write the best summary of 11 November's world news".

## What it does

A deterministic, offline Python program that reads nothing from the network and writes a one-paragraph English digest of 12 key news stories from 11 November 2026 to `/output/entry.txt` (UTF-8, 1980 characters, within the 1–2000 character limit).

## Files

- `main.py` — the agent. Deterministic. No network calls. Writes `/output/entry.txt`.
- `README.md` — this file.
- `TRANSCRIPTS.md` — session transcript.

## How to run

    python3 main.py

Output goes to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` for local testing).

## Requirements met

- [x] Public GitHub repository under an OSI-approved license (MIT)
- [x] Program at `main.py` in root
- [x] Deterministic — same bytes every run
- [x] No network — news embedded in code
- [x] 1–2000 characters
- [x] UTF-8 output
