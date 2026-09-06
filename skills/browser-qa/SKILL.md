---
name: browser-qa
description: Verify a web UI that is already running — screenshots, visual/responsive checks, console-error detection, route and form smoke. Use for dashboard/app/presentation QA and visual verification. Not for scraping, not for load testing, not for driving third-party sites.
---

# Browser QA

Local browser verification for ZAOS web surfaces (project dashboards, the MiniLab
app, the taskboard, the VIS-TP presentation, gradtime apps). The engineering
doctrine asks for browser-smoke evidence on web work; this skill provides it.

## Safety — read first

- **Never start, stop, restart, rebind, or kill a server.** This skill only
  connects to a URL that is *already serving*. The project (or the operator, via
  `! <cmd>`) owns the server lifecycle.
- **Port 8765 is a protected live presentation.** A read-only screenshot (GET) is
  fine; never send it interactions that mutate state.
- Bind test servers to `127.0.0.1` only. Do not QA a remote/public site with this.
- Screenshots and the JSON report are **evidence**, not project truth — they go
  under the project's `evidence/` or a scratch dir, never into a contract.

## Helper

`scripts/shot.py` — a thin Playwright wrapper. Uses the pre-installed browser
payload at `.runtime/browsers/playwright` (nothing is downloaded). `uv run`
resolves the pinned `playwright` package.

```bash
uv run .agents/skills/browser-qa/scripts/shot.py http://127.0.0.1:PORT \
  --out evidence/home.png \
  --wait "#main" \
  --expect-text "Dashboard" --expect-selector "#chart" --expect-absent ".error" \
  --widths 375,768,1280
```

Exit `0` = every `--expect-*` passed and (unless `--allow-console-errors`) no
console errors. Exit `1` = a check failed. The JSON report lists every check,
console message, HTTP status, page title, and screenshot paths.

For anything `shot.py` cannot express (multi-step flows, auth, form submission,
clicking through a wizard), write a short throwaway Playwright script with the
same PEP-723 header — do not extend `shot.py` into a framework.

## QA checklist (apply what the surface warrants)

- **Renders**: HTTP < 400, expected heading/landmark present, no console errors.
- **Responsive**: check the real breakpoints the design targets (`--widths`);
  look for overflow, clipped content, broken layout in each screenshot.
- **Routes**: hit each significant route; a detail route with a bad id should 404
  or redirect, not 500.
- **Forms** (if present): submit valid input → expected redirect *status* (do not
  silently follow it); submit invalid/oversized input → visible error, not a
  crash; confirm nothing was written that needed approval.
- **Presentation decks**: title slide renders, navigation works, no missing
  assets (console 404s), key numbers visible.
- **Evidence**: keep the screenshot(s) + JSON report; name what you verified and
  what you did not.

## When NOT to use this

Static HTML with no JS and no server — just read the file. API-only services —
use `curl`/`httpx`. Scraping external sites, SEO audits, load/perf testing,
pixel-diffing across commits — out of scope; propose a dedicated tool if a real
recurring need appears.
