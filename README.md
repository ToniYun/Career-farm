# Career Farm 🐔

A gamified job-search tracker. Complete daily and weekly career tasks to hatch chickens, earn eggs, and upgrade your farm.

## Features

- **Daily tasks** — outreach, company research, practice, and more
- **Weekly tasks** — applications, mock interviews, networking
- **Farm progression** — 6 tiers from Backyard Coop to Global Egg Syndicate
- **Egg economy** — idle egg production, spendable on upgrades
- **Upgrades** — Hatch Booster, Premium Feed, Coop Expansion, Career Research Lab
- **Cross-device sync** — optional Flask server keeps state in sync between devices
- **Zero dependencies** — pure HTML/CSS/JS, no build step needed

## Quick Start

### Option A — Open directly in browser (no server needed)

Just open `index.html` in your browser. State is saved to `localStorage`.

### Option B — Run with the sync server (cross-device)

```bash
pip install -r requirements.txt
python server.py
```

Then visit [http://localhost:5050](http://localhost:5050).

State is saved to `data/rc_state.json` and synced across all open browser tabs/devices.

## Project Structure

```
career-farm/
├── index.html        # The entire app — HTML, CSS, and JS all inline
├── server.py         # Optional Flask server for cross-device sync
├── requirements.txt  # flask only
├── data/             # State storage (gitignored)
└── .gitignore
```
