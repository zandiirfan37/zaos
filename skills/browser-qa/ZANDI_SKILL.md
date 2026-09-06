# Zandi skill metadata — Browser QA

- **Name:** browser-qa
- **Category:** WORKFLOW
- **Owner:** Zandi (native)
- **Status:** TESTED
- **Created:** 2026-09-06 (capability-expansion wave 1)
- **Scope:** verification of an already-running local web UI — screenshots,
  responsive/visual checks, console-error detection, route/form smoke,
  presentation validation. Not scraping, not load testing, not external sites,
  not server lifecycle management.
- **Canonical owner of:** browser automation in ZAOS. The pre-installed Playwright
  browser payload at `.runtime/browsers/playwright` (chromium build 1234, ~656 MB)
  is owned by this skill; it was previously orphaned (downloaded by the
  taskboard pilot, its `.links` back-reference left pointing at a pre-migration
  path — harmless, GC metadata only).
- **Dependency:** `playwright==1.62.0` (Python), resolved on demand by `uv run`
  via the script's PEP-723 header. No `node`/`npm`. Browsers are not downloaded.
- **Integration:** CLI + thin skill. **No MCP, no hook, no always-on service.**
- **Tested (2026-09-06):**
  - `scripts/shot.py` against a throwaway `127.0.0.1:8791` server: multi-width
    screenshots, `--expect-text` / `--expect-selector` / `--expect-absent`,
    console warning capture, HTTP status, exit-0 on pass.
  - Read-only GET screenshot of the live VIS-TP presentation on the protected
    port 8765: HTTP 200, title captured, screenshot verified, **port 8765 pid
    unchanged before/after** — confirmed non-disruptive.
  - Negative path: `shot.py` against a dead port exits 1 with a navigate check
    failure (see `.runtime/eval/browser-qa/`).
- **Known limitations:** headless chromium only (no firefox/webkit payload);
  `shot.py` does single-page checks — multi-step flows need a throwaway script;
  no visual-diff/pixel-regression; WSL2 headless only (no headed mode).
- **Disable/remove:** delete `.agents/skills/browser-qa/`. Optionally delete
  `.runtime/browsers/playwright` (regenerable). Nothing else depends on it.
