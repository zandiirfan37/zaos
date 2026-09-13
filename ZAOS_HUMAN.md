# ZAOS for Human Leads

## Start

Install once from the framework checkout:

```bash
./install.sh --workspace ~/my-workspace
```

Then enter a Git project inside that workspace and run `codex` or `claude`. ZAOS handles project discovery and engine-specific sandbox details. A normal project gets normal mutative capability; a project declares `FULL_LOCAL_DEV` in `.zaos-capability` only when its task needs local services.

## Your role

You decide correctness, usefulness, product feel, and `HUMAN_PASS`. An agent can report `ENGINEERING_PASS`, `PARTIAL`, or `BLOCKED`; it cannot replace your product audit. Audit early: report the input, what happened, what you expected, and acceptance constraints. The agent traces the first divergence and makes the smallest general repair.

## Update and recovery

`zaos update` requires a clean framework checkout, fetches its configured canonical remote, fast-forwards only, runs migrations, refreshes shims, and checks. It stops rather than guessing. `zaos doctor` diagnoses. `zaos engines status` shows preserved vendor paths; `zaos engines refresh` accepts explicit vendor-path hints after a vendor update. `./uninstall.sh` restores native entries installed by ZAOS. The raw engine remains reachable at the path reported by `zaos engines status`; `ZAOS_INTERNAL_EXEC=1 codex` or `claude` bypasses routing.

If ZAOS fails, use the raw engine and report command, directory, observed output, and expected result. Do not edit sandbox flags or Git paths as a workaround.
