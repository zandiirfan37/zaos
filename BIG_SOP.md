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

`UNDERSTAND → DECIDE → IMPLEMENT → TARGETED VERIFY → COMMIT → MOVE ON`

1. Identify the target repository, task boundary, and relevant local rules.
2. Read only the project state, contract, and skill needed for that decision.
3. Decide the smallest safe change and obtain approval for material choices.
4. Implement only the approved scope.
5. Run validation proportional to the change and inspect the result and diff.
6. Update `PROJECT_STATE.md` when the sprint changes meaningful project state.
7. Commit a coherent, verified project change when authorized; report outcome, risks, and the next action.

Do not repeat discovery, audit, or architecture work unless new evidence could change a current decision. Stop when the requested outcome and its relevant verification are complete.

## Broader project lifecycle

For a new project, major rebuild, unfamiliar integration, or consequential design decision, widen deliberately: establish evidence and constraints, compare viable options, obtain the Human Lead decision, record the project blueprint/contracts, then return to the normal task loop. Load `PROJECT_INTELLIGENCE_SOP.md` only when this deeper work is justified.

Architecture must fit the current product, domain, risk, and operating needs. Do not copy a legacy tree, template, framework, or reference repository by habit. Complexity must pay rent.

## One active writer and project isolation

Only one executor writes a working tree at a time. A handoff occurs at a clean boundary: inspect status and diff, run relevant checks, state DONE / IN PROGRESS / REMAINING, then let the receiving executor read repository truth. Do not rely on long chat transcripts or commit knowingly broken work merely to handoff.

Projects are independent repositories. Do not modify another project, global runtime, framework, secrets, or remote state unless the task explicitly puts it in scope. Git belongs to the target repository and is the durable history—not an activity log or a substitute for project state.

## Context and skills

Normal loading is intentionally narrow:

`BIG_SOP → relevant on-demand skill → project AGENTS.md → PROJECT_STATE + relevant contracts → current task/stage brief`

Read `CURRENT_STATE.md` only when workspace-level state matters. Do not load every global instruction, unrelated project file, or library item for routine work. Skills are on-demand reusable guidance; deeper reference material stays in `.agents/library/` and is opened only when it informs a live decision.

## Verification and escalation

Verification is proportional: a small text edit needs focused inspection; a behavioral change needs relevant tests; high-risk work needs stronger evidence. Never call a result successful solely because a command exited zero—inspect the meaningful result.

Escalate before destructive actions, remote writes, deployments, credentials or secrets changes, irreversible migrations, material scope expansion, or a product/scientific decision. Escalate also when required evidence is missing, constraints conflict, or progress depends on a Human Lead choice. Do not escalate merely because work is difficult when safe, bounded investigation can resolve it.

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

## Framework and skill discipline

Frameworks offer optional tools, not automatic process. Use only the narrow
portion that changes a real decision or reduces real risk. Keep upstream
frameworks clean; put Zandi-specific guidance in owned adapters or instructions.

Adopt or create a skill only after repeated evidence that a compact reusable
guide will save future context or work. A skill may cite library material, but
the library is reference memory—not mandatory prompt payload.

## ECC position

ECC is a framework/toolkit under `.agents/frameworks/ecc/`, not Zandi's global operating system. It is **light/off** for normal bounded work. Load it on-demand for hard debugging, complex migration, unfamiliar integrations, repeated failures, or high-risk work. Use heavier ECC assurance for release hardening, security/privacy, or major reliability verification. Do not modify ECC upstream without explicit approval.

## Stop conditions

Stop and report when the goal is met, a required approval is missing, the task would exceed its stated scope, or further investigation cannot change a decision. Preserve evidence and leave the next action clear.
