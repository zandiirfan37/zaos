# Efficient Agentic Engineering

Engineering doctrine for agent-run work: how to spend context, tokens, time,
quota, latency, and human attention as finite resources without lowering
reasoning, scientific rigor, testing, or safety. This is review and practice
guidance, not project structure authority. Operational routing lives in the
Zandi instructions; model-specific quotas and product names do not belong here.

## Progressive context loading

Load the minimum authoritative context needed to act correctly, then stop.

Default order for a project:

1. project agent instructions (`AGENTS.md` / adapter);
2. the canonical current-state artifact (`PROJECT_STATE.md` or equivalent);
3. where the project follows a staged plan, the **active stage** of that plan
   (in Zandi, the current `PROJECT_BLUEPRINT.md` stage);
4. current Git HEAD and status;
5. the active contract(s) for the assigned sprint;
6. the current diff and the relevant tests.

Expand into research/intelligence, historical decisions, Git history,
references, and broader repository exploration only when a concrete uncertainty
requires it. Stop loading once the uncertainty is resolved. Minimum sufficient
context first; expand on evidence, not habit.

## Current-state compression

One compact canonical current-state artifact per complex project. It carries
compressed current truth and points to deeper evidence by path; it does not
copy history. Detailed history stays in Git, contracts, and evidence artifacts.
Do not maintain multiple overlapping permanent state, handoff, session, or TODO
documents. Durable evidence is detailed; handoff context is compressed.

## Diff-first review

Independent review normally starts from current state + active contract +
relevant Git diff + relevant test/verification evidence — not broad repository
rediscovery. Widen scope only when the diff crosses architectural boundaries,
evidence is inconsistent, contract compliance is unclear, or scientific/security
risk demands it. Reviewer effort must pay for decision value.

## Technical quality is not semantic validity

Passing engineering checks does not make a modelling-critical field valid.
No target, label, event time, status, eligibility, censoring, risk-set,
cohort, or split field may be promoted for modelling use solely because its
dtype is correct, its range is plausible, its missingness is acceptable, its
linkage succeeds, or its technical tests pass. Promotion additionally
requires explicit semantic evidence: what the field means at source, what
real-world event or state it records, its point-in-time availability, its
temporal semantics, and the modelling uses it is permitted and prohibited
for. Absent that evidence, the field's state is "technically ready, semantic
readiness unproven" and it must not enter modelling. (Zandi observed this
failure directly: a technically clean modelling-critical field cleared
engineering checks without semantic validation before modelling.)

## Feature-universe completeness is not a feature tournament

A rigorous feature-family tournament run inside an already-narrowed candidate
set does not establish that the feature universe was complete. Before a
feature contract is declared final, every materially available predictor
resource family — including structural or context fields used only for
slicing or calibration — must carry an explicit disposition: `ADMITTED`,
`CANDIDATE_FOR_EXPERIMENT`, `DEFERRED`, `REJECTED`, `DIAGNOSTIC_ONLY`, or
`NOT_APPLICABLE`. Nothing may be silently absent. A field is never forced
into a model merely for ablation when a semantic, leakage, or
point-in-time gate excludes it — record `REJECTED` with the reason. When a
predecessor project exists, its design intelligence — features, targets,
labels, experiments, failures, technical debt, untested ideas — is recovered
read-only before the new experimental scope is called complete. The Zandi
instructions own the gate mechanics (`PROJECT_INTELLIGENCE_SOP.md`, the
Resource / Feature Universe Gate, the Legacy Design-Intelligence Recovery
Gate, and the Study-Design Freeze Gate); this section is the doctrine.
(Zandi observed this failure directly: a feature study was frozen within an
IPS/SKS-only set and an omitted original field later produced a large
improvement.)

This completeness principle is archetype-general. Whatever the resource kind —
a predictor column, a corpus source, an image source and its annotation set, a
tool or environment — every materially available resource family carries an
explicit disposition before the resource or feature contract is frozen, and a
contract built from a convenient subset (one domain, one source, one index,
one tool set) is not evidence that the universe was complete. The resource-
intelligence *depth* is parameterised by archetype in the Zandi instructions
(`PROJECT_INTELLIGENCE_SOP.md`, Resource-Intelligence Profiles); the tabular
missingness/preprocessing checklist below is one profile, not a universal
requirement.

## Data intelligence depth and preprocessing discipline

For a modelling or data project, data intelligence inspects each material
dataset and each materially relevant variable deeply enough to support the
downstream preprocessing, missing-data, feature-engineering, and
experimental-design decisions — not only a surface profile. It may propose a
processing strategy but must not silently execute scientific feature-selection.
Three rules bound it:

- Do not infer a statistical missingness mechanism (MCAR / MAR / MNAR) without
  evidence; an observed missingness pattern is not a mechanism.
- Do not apply blind global imputation to structural missingness; structural
  and accidental absence are treated differently.
- Any learned preprocessing operation (imputation values, encoders, scalers,
  outlier bounds, rare-category maps) is fit only on the appropriate training
  partition and applied to validation / test / OOT — never learned from future
  or holdout data.

The Zandi instructions own the mechanics (`PROJECT_INTELLIGENCE_SOP.md`,
Section B and the Blueprint Synthesis Gate); this section is the doctrine.

## Task-triggered quality gates

The applicable gates are determined by the task type, not restated in every
prompt. The agent identifies the task type from the assigned objective and
current state, then applies the matching gates:

- **Data ingestion / cleaning** — provenance; grain and schema; structural
  quality; semantic quality; temporal meaning where relevant.
- **Modelling-critical field** (target, label, event time, status,
  eligibility, censoring, risk-set membership, cohort/split) — technical
  readiness; semantic readiness; source meaning and evidence; temporal
  semantics; explicitly allowed and prohibited modelling use.
- **Target / label** — estimand; label availability; population defined
  independently of the future outcome; event timing; status semantics;
  censoring semantics or an explicit unsupported-state declaration;
  point-in-time availability; claim boundary.
- **Feature engineering** — lineage; point-in-time validity; leakage checks;
  deterministic construction; semantic validity; and, before the feature
  contract is final, feature-universe completeness — every materially
  available predictor family explicitly dispositioned, not only those inside
  a pre-narrowed domain.
- **Modelling** — target semantic gate already passed; temporal split
  validity; sealed-test isolation; calibration and metric appropriateness;
  reproducibility.
- **Release / production** — scientific claim boundary; reproducibility;
  security and privacy; monitoring and rollback as applicable; production
  authority and data prerequisites.

This is doctrine and agent behaviour, not a workflow engine. Do not build
infrastructure to enforce it.

## Agent quality ownership

An implementation or review agent owns not only literal task execution but
also detection of violations of the applicable scientific, semantic,
temporal, provenance, privacy/security, and engineering gates within its
assigned scope. It implements, validates, updates current state, and
commits within one bounded sprint. It stops and escalates only when a
material, unresolved blocker prevents safe completion. The Human Lead and
Orchestrator do not restate standard gates in each prompt; the agent derives
them from repository governance.

## Proportional assurance

Choose the lightest assurance level that can support the actual claim; the
levels are guidance, not ceremony.

- **FAST** — routine, reversible, low-risk work: implement and inspect a smoke
  or directly relevant check, then move on. Do not manufacture state or a broad
  test run for a tiny change.
- **STANDARD** — normal serious project work (the default): recover local
  authority/current state, use the matching workflow, run targeted verification,
  inspect the meaningful result and diff, then make a clean commit/state update
  when the work changes durable project state. Safely diagnose and implement in
  one bounded sprint rather than splitting work into ceremony.
- **HARDENED** — use stronger, task-specific evidence for a scientific lock or
  confirmation, security-sensitive work, destructive migration, high-impact
  architecture, release-critical change, sealed-test boundary, or other
  consequential ambiguity. Use Council only when independent views could change
  a material decision.

Do not upgrade work merely because it is difficult, and do not downgrade a
known high-risk boundary for speed. The task-triggered gates above still define
what must be checked at each level.

## Handoff and concurrency

Before switching active implementation agents, when feasible: inspect HEAD and
status; preserve the current diff; run relevant verification; record DONE /
IN_PROGRESS / REMAINING. The receiving agent continues from repository truth
(instructions, state, Git, contracts, diff) and only the remaining scope — no
long transcript transfer, no restart. If an agent hits a usage or rate limit
and nothing is urgent, waiting for reset is the safest default.

One active writer per working tree. Multiple agents may review or reason
concurrently, but two implementation agents must not modify the same tree at
once. Parallel writers require deliberate isolation (worktrees or branches) and
are introduced only when the complexity clearly pays rent.

## Exploration stop condition

Research, architecture study, reference intelligence, and diagnosis are bounded.
Before exploring, state the decision or question it must resolve. When evidence
is sufficient: GATE COMPLETE -> decide -> implement. Reopen only on new
evidence, a failed assumption, or a new concrete question.

An audit or diagnostic must have a concrete decision it can change. If
existing evidence already establishes the relevant decision — a gate already
passed, a semantic question already answered, a repository already mapped —
consume that evidence instead of rerunning broad discovery. Avoid repeated
repo rediscovery, repeated semantic audits after a gate is established, agent
duplication, review of unchanged evidence, and audit-report-prompt loops.

## State transition as Definition of Done

For a substantive state-changing sprint: bounded implementation -> relevant
tests -> verification -> current-state update -> diff review -> commit /
checkpoint. The state update is part of the state transition, not a later
memory-maintenance task. Minor edits and test reruns must not create
state-document churn.

## Context is an engineering resource

Reduce redundant context and duplicated work before reducing reasoning quality,
scientific rigor, testing, or safety. Do not reread the whole project each
session; do not repeat completed architecture or reference studies without a
new question; do not have peer agents duplicate an implementation for
reassurance. Use independent review where it changes confidence or a decision.

Once a legacy, reference, or domain synthesis is canonical, consume it first;
reopen raw legacy or external repositories only when the synthesis lacks
required detail, evidence conflicts, or a new decision genuinely requires it —
not to re-scan whole repositories. Intelligence synthesis exists to cut
repeated context consumption, not add to it.

## Command output economy

Verbose command output is context spend. Ask for the smallest output that
answers the question, using the tool's own flags — not a wrapper:

- history / status: `git log --oneline -N`, `git log --stat`, `git status --porcelain`
- diffs: `git diff --stat` first; the full diff only for the files that matter
- tests: `pytest -q`; on failure `pytest --tb=short` (or `-x` to stop at the first)
- search: `rg -n -m N` (cap matches), `rg -l` (files only) before full context
- listings: `ls -1`, `find ... | head`, name-only before full detail

Keep the full output one re-run away — never trade away a traceback, an error
chain, or a diff hunk you actually need to reason about. (RTK, a token-compressing
CLI proxy, was evaluated 2026-09-06 and rejected: net-neutral on this command
mix, lossy on debugging output, and it scatters state in `$HOME`. Evidence:
`.runtime/eval/rtk/`.)

## Code navigation

`Read` + `Grep` + `Glob` is the sufficient, canonical way to navigate a project.
A code-intelligence tournament (2026-09-07, `.agents/eval/benchmarks/code-intel.md`)
ran jedi and ast-grep against this baseline across eight navigation task classes
and found **8/8 correctness parity** — no tool improved answers, only trimmed
~17% of cost. No standing tool was adopted.

The one place a tool pulls its weight is **impact analysis on a widely-used
symbol** — "list every real caller / what breaks if I change this signature."
There, `grep` scoped to `src/` silently misses call sites in `tests/`, `app/`, and
study scripts, and unscoped `grep` buries them in import-line and comment noise.
For that specific job, reach deliberately for import-resolved references —
`jedi.Script(...).get_references(...)`; a runnable reference is at
`.agents/eval/benchmarks/code-nav-ref.py` (`refs` / `callers` / `imports` /
`usedby`). It is a technique, not an installed capability.

## Complexity must pay rent

Every additional framework, abstraction, service, agent, document, workflow,
worktree, dependency, or integration must solve a concrete problem whose benefit
exceeds its maintenance, context, coordination, and failure cost.
Professionalism is not maximum machinery.

## Adaptive agent / model routing

Use the least costly capable agent, model, and effort level that satisfies
quality, risk, and task complexity. Escalate capability for architecture,
scientific reasoning, difficult debugging, security, and consequential
independent review. Roles and engineering standards are durable; specific model
assignments and usage thresholds are operational and adaptive — keep them in the
Zandi instructions, not here.

## Optional: project-native doctor / status

Not required per project. Where a project has multiple contracts, gates,
generated artifacts, or environment assumptions, a deterministic
health/status/verify command can compress agent startup context. It reports
machine-verifiable facts only and must not become a parallel source of project
truth. Complexity-must-pay-rent governs whether it exists.

## Anti-patterns

- Repository rediscovery on every session.
- Full-context review for a tiny diff.
- Repeated audits with no decision impact.
- Two agents duplicating the same task.
- Simultaneous writers in one working tree.
- Permanent proliferation of state / handoff / session files.
- Architecture research with no stop condition.
- Adopting a tool or framework merely because it is available.
- Treating the chat transcript as the project source of truth.
- Cutting verification or scientific rigor merely to save token budget.
- Promoting a modelling-critical field on technical checks alone.
- Freezing a feature or model study before the candidate resource/feature
  universe was enumerated and each family explicitly dispositioned.
- Declaring a clean rebuild's experimental scope complete without a
  read-only legacy design-intelligence recovery pass.
- Inferring MCAR/MAR/MNAR from an observed missingness pattern without
  evidence.
- Fitting imputation, encoders, or scalers on the full dataset instead of the
  training partition only.
- Blind global imputation of structurally missing values.
- Running one overloaded discovery session instead of focused intelligence
  passes for a large new project.
- Applying the tabular resource-intelligence checklist to a corpus, media, or
  agent project instead of the matching archetype profile.
- Beginning substantial implementation before intelligence converges into an
  approved project blueprint.
- Re-scanning whole legacy or external repositories after a canonical
  synthesis already answers the question.
- Restating standard ECC gates in every prompt instead of deriving them.
- Running a deep audit for routine bounded work that the fast lane covers.
- Splitting diagnosis and implementation when one agent can safely do both.
