# Zandi skills

Skills are concise, reusable guidance that loads **on demand**. Physical skill
directories are flat: `.agents/skills/<skill-name>/`. Categories are metadata,
not folders.

| Skill | Category | Status | Purpose |
| --- | --- | --- | --- |
| UI/UX Pro Max | DOMAIN | TESTED | Local UI/UX design intelligence from official upstream. |
| Ask the Council | REASONING | TESTED | Bounded multi-perspective deliberation for consequential decisions. |
| ML Research | DOMAIN | TESTED | Scientifically rigorous tabular predictive modelling guidance. |
| Browser QA | WORKFLOW | TESTED | Verify an already-running local web UI: screenshots, responsive/visual checks, console errors, route/form smoke. Canonical owner of browser automation. |
| Project Re-foundation | WORKFLOW | DRAFT | Branchable, evidence-led recovery or re-foundation workflow. |
| Project Architecture | WORKFLOW | DRAFT | Narrow, reusable derivation of minimum project architecture, early-clean-home timing, and numbering convention. |
| Medical Imaging Research | DOMAIN | DRAFT | Reusable medical-imaging research decisions: data semantics, preprocessing, evaluation, validation, reconstruction/segmentation fairness. |

- **DOMAIN** — expert knowledge to apply.
- **REASONING** — how to deliberate.
- **WORKFLOW** — how to execute a repeatable task.
- **ASSURANCE** — how to challenge or verify a result.
- **META** — how skills or context are created or evaluated.

A skill must solve a repeated real problem. Keep it small: no giant `SKILL.md`;
load deep references only when needed. Do not blindly install community skills:
inspect source and scripts first. Skills are **TESTED before TRUSTED** and
should reduce future context or work, not add bureaucracy.

Lifecycle: `DRAFT → TESTED → TRUSTED → STABLE`.

- `DRAFT → TESTED`:
  - **Reasoning/domain skills** (guidance the agent applies) need an evidence-backed
    eval pass: a `<skill>/eval/cases.toml` with ≥3 behavioural cases (≥1 regression
    tripwire) and a green
    `uv run --no-project python .agents/eval/zaos_eval.py run <skill>` recorded in
    `ZANDI_SKILL.md` (evidence path + pass count + cost). See `.agents/eval/README.md`.
  - **Tool-wrapper skills** (a script + a checklist; e.g. `browser-qa`) instead need
    reproducible script tests — pass path, assertion-failure path, negative/error
    path — plus one real-target demo, all recorded in `ZANDI_SKILL.md` with the
    evidence dir. Do not force behavioural eval cases onto a tool wrapper.
- `TESTED → TRUSTED` still requires real-project use — the eval does not replace it.
- Any skill revision re-runs its cases; a drop in pass count or `--ab` skill lift
  blocks the change until explained.
- Eval evidence lives in `.runtime/eval/` (disposable); it is never canonical
  project truth.

## Proactive routing

Reach for a skill without being explicitly asked when the task itself is
domain/substantive work, not merely because this list was read. For each
skill below, two distinct questions matter and must not be conflated:

- **Owns** — the specific material decision(s) the skill actually answers.
- **Reach for it when** — the situation that should make you open it.

Match a task to a skill by its **owned decision**, not by topic keyword.
Two skills can share a domain word ("medical," "model") while owning
completely different decisions — route by which decision the task actually
needs resolved, not by which skills mention the same word.

- **Project Re-foundation**
  Owns: how to triage and sequence a legacy recovery, rebuild, or
  external-base acquisition.
  Reach for it when: material legacy recovery, rebuild, or re-foundation is
  in play.

- **Project Architecture**
  Owns: how to derive the minimum project structure, when to stand up an
  early clean project home, and the numbering/ordering convention.
  Reach for it when: a project's structure/boundaries need to be derived or
  materially reconsidered, or a clean project needs to be stood up early
  during recovery/rebuild.

- **ML Research**
  Owns: tabular prediction-contract framing, leakage/split discipline, and
  the experiment→evidence→decision→promotion boundary for tabular
  classification/regression work.
  Reach for it when: a substantive tabular ML/scientific modelling or
  evaluation decision is being made.
  Also owns (domain-neutral, reachable independent of the above): how to
  select a winner among many candidates using validation data and trust
  that winner appropriately — see the dedicated cue below.

- **Medical Imaging Research**
  Owns: medical-imaging data semantics (subjects, orientation/affine,
  modality), preprocessing/leakage boundaries specific to imaging,
  PSNR/SSIM/Dice-style metric contracts and their failure modes,
  subject-level validation/external-confirmation design, and fair
  reconstruction/segmentation comparison.
  Reach for it when: a medical-imaging modelling, preprocessing, or
  evaluation decision is being made. Does not own formula-specific
  inverse-problem mathematics (e.g. a project's own sampling-operator or
  spectral-descriptor design) — that stays project-local evidence; this
  skill only supplies the general medical-imaging evaluation/validation
  layer around it.

- **Ask the Council**
  Owns: nothing domain-specific — it is the deliberation mechanism itself.
  Reach for it when: consequential ambiguity or a genuine trade-off remains
  after evidence gathering, including when two skills disagree on a
  material, same-specificity decision (see below).

- **UI/UX Pro Max**
  Owns: UI/UX design decisions (layout, style, accessibility, motion,
  stack-specific implementation).
  Reach for it when: substantive UI/UX design work is being done.

- **Browser QA**
  Owns: how to verify a running web UI — screenshots as evidence, responsive
  breakpoints, console-error detection, route/form/presentation smoke, and the
  "never touch the server lifecycle" boundary.
  Reach for it when: a web app, dashboard, or presentation needs to be checked
  in a real browser, or the engineering doctrine's browser-smoke evidence is due.
  Not for: scraping, external sites, load testing, pixel-diffing.

### Direct routing cue: candidate/model-selection stability

`resampling-based candidate/model-selection stability` (bootstrap winner
stability, practical ties, robustness gates, freeze-before-confirmation) →
`ml-research/references/candidate-selection-and-stability.md`.

This applies whenever a task is choosing a winner among many candidates
using a validation set — models, hyperparameters, thresholds, or a
hand-crafted scoring formula — **even when the task is not tabular ML**.
Reach for this reference directly by this cue; do not first require the
task to look like tabular classification/regression before considering it,
and do not open the rest of `ml-research`'s body for it unless a tabular
decision is also in play.

## Multi-skill composition

A task may need zero, one, or multiple skills. Decide by decomposing the
task into its **material decision surfaces** (the specific consequential
questions it raises), then checking, per decision, whether a skill above
owns it:

- **Zero skills** — no registered skill's owned decision matches anything
  in the task (routine edits, single-fact lookups, non-substantive work).
- **One skill** — every consequential decision surface in the task
  collapses into a single skill's owned scope.
- **Multiple skills** — the task raises two or more decision surfaces with
  genuinely distinct owners (e.g. a medical-imaging evaluation task needs
  both "is this metric defined correctly" — Medical Imaging Research — and
  "is this candidate-selection design statistically sound" — the ML
  Research reference above; neither owner subsumes the other).

Do not load a skill merely because it shares a topic word with the task.
Loading every skill tagged with a domain the task superficially resembles
is exactly the eager-loading behavior this section exists to prevent.

### Lazy-loading rule

1. Resolve candidate skills from this README first — never open a skill's
   body to decide whether it's relevant.
2. Load only the top-level `SKILL.md` of skills that actually matched a
   decision surface in step 1.
3. Load a skill's `references/*` files only when a specific sub-question
   inside that skill's scope requires it — never preload them.
4. Do not load an adjacent or sibling skill merely because it shares a
   domain with one you've already loaded; each additional skill must match
   its own distinct decision surface.

### Precedence when skills or evidence conflict

For routine overlap, resolve in this order (cheapest and most authoritative
first):

`explicit Human/project frozen contract` > `actual project/data evidence`
> `domain-specific skill on its own domain's specifics` > `general
methodology skill on generalities`.

If two sources at the **same** specificity level disagree on a material,
consequential decision, do not silently arbitrate between them — **STOP and
escalate** (recommend Ask the Council or a Human decision), per BIG_SOP's
existing escalation clause. This is not a new mechanism; it is the ordinary
escalation rule applied to a skill-conflict trigger.
