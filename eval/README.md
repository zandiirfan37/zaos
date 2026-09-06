# ZAOS evaluation harness

Answers one question with evidence instead of intuition:

> **Did this agent capability actually get better (or worse)?**

`zaos_eval.py` is a single stdlib Python file. Nothing here loads during normal
work — it runs only when you ask it to, or when a lifecycle promotion requires it.

## Run

```bash
uv run --no-project python .agents/eval/zaos_eval.py list ml-research
uv run --no-project python .agents/eval/zaos_eval.py run  ml-research
uv run --no-project python .agents/eval/zaos_eval.py run  ml-research --ab          # skill vs no-skill; reports "skill lift"
uv run --no-project python .agents/eval/zaos_eval.py run  ml-research --engine both # claude + codex
uv run --no-project python .agents/eval/zaos_eval.py run  ml-research --skill-file /tmp/candidate.md   # evaluate a revision
uv run --no-project python .agents/eval/zaos_eval.py run  ml-research --case C-unsafe-request-is-challenged
```

Exit code `0` = all cases passed, `1` = at least one failed, `2` = harness error.

## Where things live

| Thing | Path | Tracked? |
| --- | --- | --- |
| Runner | `.agents/eval/zaos_eval.py` | yes (`.agents`) |
| Cases  | `.agents/skills/<skill>/eval/cases.toml` | yes (with the skill) |
| Evidence | `.runtime/eval/<skill>/<utc>/` (`results.json`, `summary.md`, `raw/`) | **no** — disposable, never canonical |
| Response cache | `.runtime/eval/.cache/*.json` | no |

Evidence is never project truth. If a project wants to adopt an eval result as
evidence, it copies the relevant file into its own `evidence/` deliberately.

## Case kinds

- **`static`** — deterministic structural checks on `SKILL.md` (frontmatter,
  `name:`/`description:`, body line budget, required phrases). Free, <1 s. Catches
  a bloated or malformed skill.
- **`behavioural`** — feed a realistic scenario to the engine with the skill
  applied, then assert on the response:
  - `assert_all` — every regex must match (case-insensitive, multiline).
  - `assert_any` — at least one must match.
  - `assert_none` — **regression tripwires**: none may match. A case with no
    tripwire and no plausible failure mode is evaluation theatre — don't write it.
  - `[case.judge] enabled = true / rubric = "..."` — optional LLM judge (uses the
    same `claude` CLI, no API key). Use only when objective assertions genuinely
    cannot capture the property.
- **`activation`** — raw scenario, no skill pointer, real config: does routing
  reach the right skill on its own? Tests `BIG_SOP` + `skills/README.md` quality.

## A/B and skill lift

`--ab` runs each behavioural case twice: once with the skill applied, once as a
bare agent. **Skill lift** = cases that pass *with* the skill and fail *without*
it — the skill's measurable contribution.

`--skill-file PATH` evaluates an arbitrary file in place of the live `SKILL.md`,
so a proposed revision, or a deliberately-regressed variant, can be scored
without touching the real skill.

## Which model — this matters

The eval scores the **(skill + model)** system, not the skill alone. A strong
model (`sonnet`) often reaches the right answer with a broken skill or no skill,
so it is blind to skill quality. Pick the model to fit the question:

| Question | Model | Why |
| --- | --- | --- |
| Does the skill+agent produce correct guidance? (floor / promotion gate) | `--model sonnet` (default) | tests what production actually does |
| Is it the *skill* doing the work? / regression detection / skill lift | `--model haiku` | the skill's scaffolding becomes load-bearing; a weakened skill visibly degrades |

Pilot evidence: on `sonnet`, a deliberately-regressed `ml-research` (guards
removed, "use a random split" injected) still passed every case — the model
overrode the bad skill. On `haiku` the same regression failed 2/3 cases, and the
real skill showed lift on 2/3 (see `.runtime/eval/ml-research/HAIKU-*`).

## Model / auth

`claude` uses the local Claude Code subscription session (`CLAUDE_CONFIG_DIR` →
`.runtime/engines/claude`); `codex` uses `CODEX_HOME` → `.runtime/engines/codex`.
No API keys. Responses are cached by SHA-256 of (engine, model, full prompt,
skill-file bytes), so reruns are free and reproducible until an input changes;
`--no-cache` forces fresh calls.

## Lifecycle hook

`DRAFT → TESTED`: a skill needs a `cases.toml` with ≥3 behavioural cases (≥1
tripwire), a green `run --model sonnet` (floor), and — for regression cover — a
`run --model haiku --ab` where the real skill beats the weakened/absent variant
on ≥1 case. Record the evidence dir + pass count + new spend in `ZANDI_SKILL.md`.
`TESTED → TRUSTED`: still requires real-project use — eval does not replace it.
Any skill revision re-runs its cases (`--model haiku` for a real diff signal); a
drop in pass count or skill lift blocks the change until explained.

## Benchmark contracts

`benchmarks/` holds contracts for capability bake-offs that are larger than a
skill's `cases.toml` — how to compare candidate *tools* against the ZAOS baseline
(tasks, ground-truth keys, metrics, decision rule). `benchmarks/code-intel.md` is
the first: baseline vs jedi / ast-grep / Serena for code navigation.

## Removability

Delete `.agents/eval/` and every `skills/*/eval/` directory. Nothing else in ZAOS
depends on this. The lifecycle note in `skills/README.md` becomes a no-op.
