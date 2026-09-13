# Zandi Big SOP

`BIG_SOP.md` is the primary human and agent doctrine for Zandi. It states the
durable rules; project rules and task facts live with their owning project.

## Roles and authority

- **Human Lead** owns goals, priorities, product/scientific decisions, and approval of material risk.
- **ChatGPT Orchestrator** turns intent into bounded work, selects the minimum needed context, coordinates handoffs, and surfaces decisions for the Human Lead. It does not silently decide product or science.
- **Codex or Claude Executor** inspects the assigned repository, implements the approved scope, verifies proportionately, and reports evidence. They are peer executors/reviewers; neither outranks the Human Lead.

Authority is ordered: Human Lead direction; project `AGENTS.md`; current project state and relevant contracts; this SOP; an on-demand skill; framework guidance. A more-local rule governs only within its legitimate scope. Never invent a second authority for the same concept.

## Normal task loop

Use the smallest loop that can safely decide the work:

`PRECHECK → UNDERSTAND → DECIDE → IMPLEMENT → TARGETED VERIFY → COMMIT → CLEAN STATUS → MOVE ON`

### Responsive preflight

Before substantive execution, take a short, internal routing pass: identify the
project and local authority; the canonical workflow or current stage; the
smallest matching skill set and useful tools; and the proportional assurance
level. Treat an orchestrator prompt as the mission, boundary, and consequential
constraints — not a mandate to bypass a better canonical method. Silently use
the better method when that preserves intent. If a material conflict remains,
make **one concise escalation** naming the applicable authority, the conflict,
and the recommended resolution; do not create approval chatter for ordinary
implementation choices. At the end of meaningful work, report one highest-value
next action when one is evident. This is routing intelligence, not a checklist,
document, or runtime service.

When no project or repository exists, treat the request as an ad-hoc task
context: route by task family (for example research, creative work, critique,
or decision support), use external evidence when its freshness or provenance
matters, and do not invent project-local authority. Project authority resumes
as soon as the user places work in a project.

For substantive interface work, infer the interface's **current intent** before
choosing UI/UX method: who uses it now, which work or decision it must make
easier, and the project's present stage. Treat an interface for building,
debugging, experimentation, evaluation, calibration, or QA as an
**engineering/evaluation surface**: favor observability, controllability,
reproducibility, explicit state, useful diagnostics, and understandable failure
paths, without exposing sensitive data unnecessarily. Treat an interface for
ordinary end-user operation as a **product/end-user surface**: favor task
completion, clarity, accessibility, trust, and low cognitive load; keep
implementation internals from dominating it. Operations/admin and
presentation/demo intent may be recognized when they materially change the
work. A surface may evolve or split as a project matures. Do not prematurely
polish a building harness as final product UI, or ship an engineering console as
the final product by accident. Apply the matching UI/UX and browser-QA checks.

For a nontrivial new project, major rebuild, or re-foundation, first ask whether
external implementations, mature libraries, datasets, models, benchmarks, or
professional workflows are likely to change the build direction. If so, route
through the smallest relevant Project Intelligence / project-refoundation
reference and data-source tracks before greenfield structure or implementation.
Skip that pass only when the work is trivial or disposable, prior art has
negligible expected value, or the Human Lead meaningfully requires a
from-scratch path. This is a prior-art-first default, not a research ceremony.

The same reflex applies operationally: before installing or building a
capability that crosses a real cost threshold — a large download, a GPU or
driver stack, an external service, a parser/OCR/embedding/vector capability,
anything already used elsewhere in the workspace, or a long build — first look
for it on `PATH`, in nearby project environments, running services, container
images, and model caches, and prefer verified read-only reuse.

1. Identify the target project/repository or ad-hoc task context, boundary, and
   relevant local rules.
2. Read only the project state, contract, and skill needed for that decision.
3. Decide the smallest safe change and obtain approval for material choices.
4. Implement only the approved scope.
5. Run validation proportional to the change and inspect the result and diff.
6. Update `PROJECT_STATE.md` when the sprint changes meaningful project state.
7. Commit a coherent, verified project change when authorized; report outcome,
   risks, and the next action when one is evident.

Do not repeat discovery, audit, or architecture work unless new evidence could change a current decision. Stop when the requested outcome and its relevant verification are complete.

## Broader project lifecycle

For a new project, major rebuild, unfamiliar integration, or consequential design decision, widen deliberately: establish evidence and constraints, compare viable options, obtain the Human Lead decision, record the project blueprint/contracts, then return to the normal task loop. Load `PROJECT_INTELLIGENCE_SOP.md` only when this deeper work is justified.

Architecture must fit the current product, domain, risk, and operating needs. Do not copy a legacy tree, template, framework, or reference repository by habit. Complexity must pay rent.

## Project design, workbench, and truth

`00_workbench/` is the canonical pre-production laboratory and the default home
for evolvable work: exploratory design and planning, comparative architecture or
outline work, research and prior-art review, experiments, benchmarks,
simulations, parser/model tournaments, synthetic or provisional datasets,
prototypes and UI explorations, usability and red-team testing, migration
rehearsal and shadow runs, audits and decision evidence, debugging done to
understand a problem, scratch, temporary roadmaps, unresolved specifications,
and implementation alternatives. Importance alone is not a reason to promote an
artifact.

The `00_` prefix is deliberate and permanent: it keeps the laboratory visually
first as other top-level files and directories accumulate. Simulation, research,
experimentation, and testing are functions of `00_workbench/`, not separate
top-level zones — do not add a parallel `simulation/`, `research/`, or
`experiments/` root. **Workbench owns uncertainty; production owns decisions:**
workbench stores the journey toward the answer, production stores only the
answer that has earned promotion.

When a decision converges, promotion is: **explore/design/test in
`00_workbench/` → understand the winner → rewrite or refactor it cleanly in its
canonical project location → verify proportionally → update
`PROJECT_STATE.md` and contracts as needed**. Production must never depend on
`00_workbench/`; the original workbench item may remain as provenance.

Promotion is not a folder move and never a verbatim copy of an experimental tree
into production. A dataset created or generated in `00_workbench/` stays a
workbench artifact while it is experimental, synthetic, provisional, under
comparison, or built only for evaluation; if it becomes production truth,
fixture, or serving input, promote it explicitly into a production-owned
location with preserved provenance and validation, and with no serving-time
dependency on its workbench origin. Reproducible generated experiment output
normally stays uncommitted unless it is needed as evidence, fixture, or decision
record. Rejected UI prototypes and superseded designs are not kept in production
for history — Git and `00_workbench/` own that.

Production stays minimal and intentional: every committed production file has a
clear role — runtime code, tests, config, schema/contracts, migration,
operational script, required documentation, canonical fixture or data, or
packaging metadata. Scratch and aborted-iteration names (`coba.py`,
`test_fix.py`, `final2.py`, `backup_old.json`, `temp/`, `old_version/`,
`fix_baru/`) and unused prototype trees do not belong in production; Git holds
prior versions.

After `00_workbench/`, human-facing top-level project zones default to ordered,
semantic paths such as `01_research/`, `02_data_pipeline/`, and
`03_evaluation/`. Adapt those zones to the actual project; do not create empty
folders or documents because a template shows them. Inside `00_workbench/`,
subprojects may themselves carry sequential human-facing numbers
(`00_workbench/01_<topic>/`, `02_<topic>/`, …) where research chronology and
reasoning history matter; create one only when real work exists, never as an
empty placeholder, and do not impose a fixed internal scaffold. Preserve machine
and tool semantics instead: `src/`, `tests/`, `config/`, `contracts/`,
`runtime/`, `migrations/`, scripts, framework paths, and manifests normally stay
unnumbered. **Number human sequence; preserve machine semantics.**

Do not confuse the workspace project catalog with internal zone order. Paths
such as `projects/01_<project>/` are append-only project identities; a retired
number is never reused. Paths such as `00_workbench/`, `01_research/`, and
`02_deliverables/` organize one project's human-facing work and are not its
identity. Machine-semantic production paths (`src/`, `tests/`, `config/`,
`contracts/`, `runtime/`, `migrations/`, `scripts/`, `.github/`) are a fourth,
separate category and are never numbered.

Git is durable project history; `PROJECT_STATE.md` is compact current project
truth; contracts and evidence hold durable technical or scientific truth where
applicable. Session/model memory is not canonical truth. Neither workbench nor
archive/history is active production authority. A clean working tree does not
imply a reconciled runtime: where a project has deliberately modified external
runtime state — a derived image, an edited external config, an inserted database
row, a configured service or index — that reconstruction knowledge is durable
project truth and belongs in a committed, one-screen runtime contract (expected
persistent topology; what is reproducible and how; what is disposable;
intentional external modifications, without secrets; recovery steps).
Fast-changing observed state stays in a gitignored snapshot, never hand-edited.

Add project-local `AGENTS.md`
only when meaningful local rules or routing diverge from these defaults.

In brief: preserve **hard contracts** (including machine/tool contracts,
scientific or product locks, append-only project IDs, production independence
from workbench, and one active writer per working tree); apply **defaults** of
workbench-first evolvable work, numbered human zones, Git + project-state
discipline, prior-art before unnecessary greenfield work, and adaptive
templates unless the project needs otherwise; add **optional** directories,
external frameworks/tools, and local instructions only when earned; and record
domain pipelines, locks, required machine paths, and naming rules as
**project-specific**.

## One active writer and project isolation

Only one executor writes a working tree at a time. A handoff occurs at a clean boundary: inspect status and diff, run relevant checks, state DONE / IN PROGRESS / REMAINING, then let the receiving executor read repository truth. Do not rely on long chat transcripts or commit knowingly broken work merely to handoff.

Projects are independent repositories. Do not modify another project, global runtime, framework, secrets, or remote state unless the task explicitly puts it in scope. Git belongs to the target repository and is the durable history—not an activity log or a substitute for project state.

## Context and skills

Normal loading is intentionally narrow:

`BIG_SOP → relevant on-demand skill → project AGENTS.md → PROJECT_STATE + relevant contracts → current task/stage brief`

Read `CURRENT_STATE.md` only when workspace-level state matters. Do not load every global instruction, unrelated project file, or library item for routine work. Skills are on-demand reusable guidance; deeper reference material stays in `.agents/library/` and is opened only when it informs a live decision.

`ENGINEERING_DOCTRINE.md` is the on-demand deeper layer for engineering, data, and ML work: how to spend context/tokens as finite resources, progressive loading, diff-first review, task-triggered quality gates, and "technical quality is not semantic validity." Load it for a substantive engineering or scientific-modelling sprint, not for routine edits. It is subordinate to this SOP, never a second authority.

## Verification and escalation

Verification is proportional: a small text edit needs focused inspection; a behavioral change needs relevant tests; high-risk work needs stronger evidence. Never call a result successful solely because a command exited zero—inspect the meaningful result.

Escalate before destructive actions, remote writes, deployments, credentials or secrets changes, irreversible migrations, material scope expansion, or a product/scientific decision. Escalate also when required evidence is missing, constraints conflict, or progress depends on a Human Lead choice. Do not escalate merely because work is difficult when safe, bounded investigation can resolve it.

Before expensive work that depends on a declared secret, verify the secret file
exists, is readable and non-empty, is free of stray control or escape bytes, and
parses as `KEY=value` — but never print or log the value, and never
auto-normalize or auto-repair a secret; report the fault class and let the Human
Lead fix it. A live provider probe needs explicit per-sprint Human Lead
authorization and must keep the value out of logs and error text.

A task that appeared routine can cross into a material scientific,
architecture, security, or migration decision boundary mid-task—for example,
"refactor VIS" reveals that a formula's semantics would change. Stop, name the
boundary crossed, and recommend the relevant skill, evidence, or Council
instead of silently proceeding past it.

## Task framing

Before writing, establish:

- the requested outcome;
- the exact repository or owner in scope;
- constraints and explicit prohibitions;
- whether the task changes behavior, data, configuration, or only text;
- the smallest evidence needed to know it worked; and
- the condition that makes the task complete.

Make reasonable low-risk assumptions visible in the report. Do not turn an
ordinary implementation request into an architecture audit, a migration, or a
new product decision.

## Context selection

Context is a cost. Start with the narrowest useful set:

1. the assigned task;
2. `BIG_SOP.md`;
3. the target project's `AGENTS.md`;
4. its current state and task-relevant contract;
5. one relevant skill or library source, only if needed.

Add evidence only when it resolves an uncertainty that could change scope,
design, safety, or verification. Prefer repository truth, current contracts,
and directly relevant tests over old chat summaries or generic doctrine.

Never automatically load:

- another project's files;
- all global instructions;
- all skills or library cards;
- framework source merely because it exists; or
- historical material when current state is sufficient.

## Plans and changes

Plan in proportion to risk. A small correction may need only an stated intent;
a multi-step change needs a short ordered plan; a consequential decision needs
options and Human Lead approval. Keep the plan tied to observable completion
criteria.

Prefer small, reviewable changes. Preserve existing valid work. Avoid unrelated
formatting, drive-by refactors, speculative abstractions, and scope expansion.
If a dependency, data source, or requirement is ambiguous, inspect the narrow
evidence first; ask only when the remaining choice belongs to the Human Lead.

## Repository truth and Git

Before material changes, inspect the target repository's status and current
HEAD. Treat a dirty worktree as existing work to preserve, not permission to
discard. Inspect the diff before declaring completion.

Git is the rollback and provenance layer. Commit coherent verified changes in
the repository that owns them. Do not push, rewrite history, or use destructive
Git operations without explicit authorization. A commit does not prove quality;
the validation evidence does.

### Capability before mutation

For an authorized mutative canonical-project task that is expected to commit,
complete a lightweight transaction-capability preflight **before substantial
mutation**. Resolve the actual repository and Git directory (do not assume
`.git` is a directory in the worktree), confirm that the working tree, required
destinations, and Git metadata needed for normal index/commit operations are
writable; confirm repository health, status/diff, and the absence of an obvious
lock, merge, rebase, or conflicting active writer; and identify the required
verification, `PROJECT_STATE.md` update, and whether a commit is required.

A session that can edit project files but cannot complete the required Git
transaction is not execution-ready. Fail precheck and relaunch or enter the
proper execution mode/root; do not mutate first and discover the limitation at
commit time. This applies by session capability, not engine identity. A
read-only/analysis session does not need Git write access. A legitimate
mutative non-commit task may omit it only when its workflow explicitly does not
require a commit.

For normal substantial work, the proportional transaction is:

`PRECHECK → UNDERSTAND → MUTATE → TARGETED VERIFY → update PROJECT_STATE when materially needed → INSPECT DIFF → GIT COMMIT → VERIFY CLEAN STATUS → MOVE ON`

This is not ceremony for tiny or read-only work. If commit capability
unexpectedly disappears after mutation, stop further mutation, preserve the
diff and error evidence, do not destructively roll back automatically, and use
the correct transaction-capable session to verify and safely complete or
explicitly revert the transaction.

## ZAOS maintenance boundary

In a normal project session, read ZAOS doctrine and skills but write only the
intended project repository, including its actual Git metadata when the task
requires a commit; canonical global `.agents` authority remains read-only and
must not become writable merely to support a project commit. Canonical ZAOS
maintenance is engine-neutral: Claude or Codex may make a targeted change only
when the Human Lead explicitly requests it and the maintenance session is
write-enabled for the relevant canonical ZAOS repository **and its Git
metadata**. Then precheck, make the bounded change, verify, commit, and stop.
Session role and writable scope—not engine identity—determine authority. Keep
one active writer per working tree.

## Verification levels

Choose the lightest gate that proves the requested result:

- **Text or metadata:** inspect the exact file and relevant links.
- **Local code path:** run focused unit, lint, type, or smoke checks.
- **Behavioral change:** exercise the changed path and inspect the outcome.
- **Integration or migration:** verify the affected boundary and rollback path.
- **Release, privacy, security, reliability:** use stronger targeted assurance.

If a check cannot run, report why, what was verified instead, and the residual
risk. Do not run a full test suite merely as ceremony when a targeted check
answers the real question.

## Handoffs and concurrency

Use a handoff only when it adds value. At the boundary, record the repository,
HEAD, status, diff, checks run, and DONE / IN PROGRESS / REMAINING. The next
executor resumes from these artifacts and the local rules; it does not restart
discovery.

Parallel work is safe only when writers are isolated by worktree, branch, or
non-overlapping owner. Shared runtime, credentials, migrations, and generated
state need explicit coordination.

**Waiting on background work.** After arming a background job or monitor, stop
and yield; do not re-read an unchanged or empty output on a loop. Prefer one
background job that runs the whole wait, compute, and report chain over many
thin waiters. Confirm a spawned process is alive once after a short pause.
Suspect a stall only from two progress samples taken well apart and measured
against the job's own clock — a runtime clock can drift from the host — and then
past the expected duration with the work near-idle; use the supported restart
path and record it, rather than waiting indefinitely or killing blindly.

## Framework and skill discipline

Frameworks offer optional tools, not automatic process. Use only the narrow
portion that changes a real decision or reduces real risk. Keep upstream
frameworks clean; put Zandi-specific guidance in owned adapters or instructions.

Adopt or create a skill only after repeated evidence that a compact reusable
guide will save future context or work. A skill may cite library material, but
the library is reference memory—not mandatory prompt payload.

## Reference and retired material

`.agents/library/` holds Zandi-curated knowledge cards for pattern lookup. It is
never auto-loaded; a skill may cite one card as an idea, never as authority.

Retired frameworks and vendored external checkouts (ECC-Zandi profile, ZAINE, the
pinned ECC upstream) live inert under the workspace `.archive/`. Nothing
in the active workspace loads them. `MAINTENANCE_AND_MIGRATION.md` records the
archive taxonomy and the retrieval notes for any still-useful dormant mechanism;
`CURRENT_STATE.md` records current component status.

## Stop conditions

Stop and report when the goal is met, a required approval is missing, the task would exceed its stated scope, or further investigation cannot change a decision. Preserve evidence and leave the next action clear.

Before recommending `/clear` or handing off after mutative or boundary work,
account for durable state: working tree committed or explicitly ephemeral;
`PROJECT_STATE.md` current; no owned background job left unresolved; runtime
drift recorded in the runtime contract; open Human Lead decisions captured; next
action stated. Emit this as a short closure block at session close and whenever
a task ends with unresolved risk — not on every routine task. A read-only
session states closure is safe trivially.
