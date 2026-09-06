# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright==1.62.0"]
# ///
"""ZAOS browser-QA helper — screenshot + assert a URL that is ALREADY serving.

This script NEVER starts, stops, restarts, or binds a server. Point it at a URL
someone else is already running. It connects, checks, screenshots, disconnects.

    uv run .agents/skills/browser-qa/scripts/shot.py http://127.0.0.1:5000
    uv run .agents/skills/browser-qa/scripts/shot.py http://127.0.0.1:5000 \
        --out /tmp/home.png --expect-text "Dashboard" --expect-selector "#chart" \
        --widths 375,768,1280 --wait "#chart"

Exit 0 = all assertions passed and (unless --allow-console-errors) no console errors.
Exit 1 = an assertion failed / console error / navigation error.
Exit 2 = bad usage.

Browsers: uses the pre-installed payload at .runtime/browsers/playwright (656 MB,
chromium build 1234). Nothing is downloaded.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ZANDI = Path(__file__).resolve().parents[4]  # /home/pc_pusaka/zandi
os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", str(ZANDI / ".runtime" / "browsers" / "playwright"))

from playwright.sync_api import sync_playwright  # noqa: E402


def parse_widths(s: str | None) -> list[int]:
    if not s:
        return []
    return [int(x) for x in s.split(",") if x.strip()]


def main() -> int:
    ap = argparse.ArgumentParser(prog="shot")
    ap.add_argument("url")
    ap.add_argument("--out", help="screenshot path (single width) or prefix (multi width)")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--widths", help="comma list, e.g. 375,768,1280 — overrides --width, one shot each")
    ap.add_argument("--wait", help="CSS selector to wait for before checks/screenshot")
    ap.add_argument("--wait-ms", type=int, default=2500, help="settle time after load")
    ap.add_argument("--expect-text", action="append", default=[], help="substring that must be in the page (repeatable)")
    ap.add_argument("--expect-selector", action="append", default=[], help="selector that must exist (repeatable)")
    ap.add_argument("--expect-absent", action="append", default=[], help="selector that must NOT exist (repeatable)")
    ap.add_argument("--allow-console-errors", action="store_true")
    ap.add_argument("--full-page", action="store_true")
    ap.add_argument("--timeout", type=int, default=15000, help="navigation timeout ms")
    args = ap.parse_args()

    widths = parse_widths(args.widths) or [args.width]
    report: dict = {"url": args.url, "checks": [], "console": [], "shots": []}
    ok = True

    def check(name: str, passed: bool, detail: str = "") -> None:
        nonlocal ok
        report["checks"].append({"name": name, "passed": bool(passed), "detail": detail})
        ok = ok and bool(passed)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        try:
            for w in widths:
                page = browser.new_page(viewport={"width": w, "height": args.height})
                console: list[str] = []
                page.on("console", lambda m: console.append(f"{m.type}: {m.text}") if m.type in ("error", "warning") else None)
                page.on("pageerror", lambda e: console.append(f"pageerror: {e}"))
                try:
                    resp = page.goto(args.url, timeout=args.timeout, wait_until="domcontentloaded")
                except Exception as e:  # navigation failure
                    check(f"navigate@{w}", False, str(e)[:300])
                    page.close()
                    continue
                status = resp.status if resp else None
                check(f"http_status@{w}", status is not None and status < 400, f"status={status}")
                if args.wait:
                    try:
                        page.wait_for_selector(args.wait, timeout=args.timeout)
                    except Exception as e:
                        check(f"wait_for {args.wait}@{w}", False, str(e)[:200])
                page.wait_for_timeout(args.wait_ms)

                body = page.content()
                for t in args.expect_text:
                    check(f"text {t!r}@{w}", t in body)
                for sel in args.expect_selector:
                    check(f"selector {sel}@{w}", page.query_selector(sel) is not None)
                for sel in args.expect_absent:
                    check(f"absent {sel}@{w}", page.query_selector(sel) is None)

                if args.out or len(widths) > 1:
                    if len(widths) > 1:
                        base = args.out or "shot"
                        shot = f"{base.rsplit('.', 1)[0]}.{w}.png" if "." in os.path.basename(base) else f"{base}.{w}.png"
                    else:
                        shot = args.out
                    page.screenshot(path=shot, full_page=args.full_page)
                    report["shots"].append({"width": w, "path": shot})

                report["console"].extend(f"[{w}] {c}" for c in console)
                errs = [c for c in console if c.startswith(("error", "pageerror"))]
                if not args.allow_console_errors:
                    check(f"no_console_errors@{w}", not errs, "; ".join(errs)[:400])
                report["title"] = page.title()
                page.close()
        finally:
            browser.close()

    report["passed"] = ok
    print(json.dumps(report, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
