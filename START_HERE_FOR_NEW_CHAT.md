# Start Here — Zandi

**What is Zandi?** A local AI Engineering Workbench: a Human Lead, a ChatGPT
Orchestrator, and two peer implementation/review agents (Codex CLI primary,
Claude Code CLI backup / takeover / independent reviewer) doing bounded,
reviewable engineering work on independent project repositories. The workspace
root is behaviorally non-Git; every framework and project owns its own Git.

## Authority — one owner per concept

| For | Read |
| --- | --- |
| How we operate (workflow, `PROJECT_STATE`, adaptive architecture, fast lane / deep gate) | `ZANDI_MASTER_WORKFLOW.md` |
| Roles, model routing, handoff, concurrency, Claude budget | `MULTI_AGENT_ROUTING.md` |
| Project intelligence + blueprint mechanics (gates A–J, archetype resource profiles) | `PROJECT_INTELLIGENCE_SOP.md` |
| Engineering doctrine (context, review, quality gates, anti-patterns) | `../frameworks/ecc/zandi-profile/EFFICIENT_AGENTIC_ENGINEERING.md` |
| Framework inventory + workspace state | `CURRENT_STATE.md` |
| Accepted evidence + failure history | `VALIDATION_LEDGER.md` |
| Turning project lessons into changes | `FRAMEWORK_IMPROVEMENT_LOOP.md` |
| Legacy data/asset migration | `LEGACY_MIGRATION_POLICY.md` |
| Prompt templates | `PROMPT_EXAMPLES.md` |

Another file may summarize or point to a concept but must not fork the rule.

## What to load

- **New session:** `CURRENT_STATE.md` and `VALIDATION_LEDGER.md`, then only the
  authority file(s) for the task.
- **Continuing a project:** that project's `AGENTS.md` and `PROJECT_STATE.md`,
  then only the active contract(s) or the current `PROJECT_BLUEPRINT.md` stage.
  Project-local contracts, `AGENTS.md`, and evidence outrank framework guidance.
- **Do not load:** the full instruction set for a routine task; a resource
  profile you are not using; completed intelligence syntheses without a new
  question; another project's files.

## Orchestrator bootstrap prompt

> You are the ChatGPT Orchestrator for Zandi, routing work to a peer
> implementation agent (Codex CLI primary, Claude Code CLI backup/reviewer —
> `MULTI_AGENT_ROUTING.md`). Have the agent read the project's `AGENTS.md` and
> `PROJECT_STATE.md`, then `CURRENT_STATE.md` and `VALIDATION_LEDGER.md`, then
> inspect workspace structure, `git status`, and the active contract(s)
> read-only. Use the smallest framework guidance that fits; keep work
> project-local; no global config mutation or framework activation. Derive
> architecture from product/domain requirements, not legacy, template, or
> previous-project folder shapes. For substantial work use
> `PROJECT_INTELLIGENCE_SOP.md` proportionately. Give me a bounded plan,
> approval points, validation gates, and a concise final report with
> **Framework lessons learned**. Ask for explicit review before destructive,
> remote, deployment, or global-configuration actions.

Every state-changing sprint updates `PROJECT_STATE.md` as part of Done — no
need to ask each time. Every completed project reports **Framework lessons
learned** through the improvement loop. Keep one implementation agent as the
active writer per working tree; hand off only at a clean Git / diff / test
boundary.
