# Multi-Agent Routing

Zandi now has **two peer implementation/review agents**: Codex CLI and Claude
Code CLI. This file is the canonical reference for roles, model routing,
handoff, concurrency, and Claude operating budget. It supplements
`CHATGPT_CODEX_COLLABORATION.md` and `ZANDI_MASTER_WORKFLOW.md`; it does not
replace the architecture-authority doctrine, the Project Intelligence workflow,
the complexity-must-pay-rent principle, or the approval and
clean-slate/repo-study policies.

## 1. Roles

Roles are durable. Model and agent assignments are adaptive.

- **Human Lead** — goals, priorities, scientific/product decisions, final
  approval and final authority.
- **Zandi Orchestrator / ChatGPT** — decides the next sprint; synthesizes
  project evidence and references; routes work between implementation
  agents/models; reviews approval boundaries; coordinates handoffs; challenges
  architecture and scientific decisions.
- **Codex CLI** — peer implementation/review agent; filesystem, code, tests,
  and Git execution; primary implementation agent when available.
- **Claude Code CLI** — peer implementation/review agent; filesystem, code,
  tests, and Git execution; backup/takeover implementer; independent reviewer
  when useful.
- **ECC-Zandi** — engineering doctrine, patterns, checklists, and review
  guidance. It does not dictate universal project structure.

Neither Codex nor Claude Code holds architecture or scientific authority over
the Human Lead or the Orchestrator.

## 2. Model routing

Specific model names are **not** permanent architectural requirements. The
following is adaptive operational guidance for current defaults:

| Situation | Codex | Claude |
| --- | --- | --- |
| Normal implementation | Terra Medium | Sonnet Medium |
| Hard implementation / review | Terra High | Sonnet High, or a stronger reasoning model where justified |
| Exceptional synthesis / debugging | strongest available tier, only when complexity/risk justifies the cost | strongest available tier, only when complexity/risk justifies the cost |

Assignments adapt to capability, cost, latency, quota, task complexity, and
scientific/security risk.

## 3. Agent handoff policy

Do not switch implementation agents arbitrarily in the middle of an unbounded
edit. Preferred handoff boundary:

1. inspect current Git status;
2. inspect the diff;
3. run relevant tests if feasible;
4. identify DONE / IN_PROGRESS / REMAINING;
5. preserve all valid existing work;
6. the new agent reads the repository, contracts, and diff rather than
   restarting the task.

The repository, contracts, tests, and evidence are the shared source of truth.
Do not depend on transferring long chat transcripts. The receiving agent first
inspects, in order:

1. `AGENTS.md` / project agent instructions;
2. `PROJECT_STATE.md`;
3. `git status` and current HEAD;
4. the active contract(s) relevant to the assigned task.

Do not rediscover the whole project from scratch.

If one agent hits a usage limit mid-sprint and there is no urgency, waiting for
reset is the safest default. If takeover is necessary, the receiving agent must
first inspect current work and continue only the remaining scope.

## Project state responsibility

Codex and Claude Code are both responsible for maintaining the project's
canonical `PROJECT_STATE.md` when they are the active writer completing a
state-changing sprint. Updating it is part of the Definition of Done (see
`ZANDI_MASTER_WORKFLOW.md`), normally in the same commit that establishes the
new state — the Human Lead does not have to ask for it each sprint.

## 4. Concurrent work policy

By default, only **one** agent is the active writer in a given working tree.
Safe default: one agent writes (e.g. Codex), the other reviews/stands by (e.g.
Claude Code), or vice versa.

Do not let Codex and Claude Code modify the same working tree simultaneously.
Parallel implementation may later use isolated Git worktrees or branches, but
only when the complexity pays rent and data/runtime implications have been
addressed.

## 5. Claude operating budget

Human Lead operational preference for Claude weekly usage:

| Weekly usage | Policy |
| --- | --- |
| 0–40% | normal use |
| 40–50% | be selective |
| 50–60% | high-value work or Codex backup only |
| >= 60% | stop Claude work until weekly reset unless the Human Lead explicitly overrides |

Default Claude effort for routine work is **Medium**; use higher effort only
when reasoning complexity justifies it. Do not sacrifice scientific or
engineering quality to save quota — instead reduce redundant context, repeated
audits, and duplicated agent work.

## 6. Context and token efficiency

- Do not ask each new agent to rediscover the entire project.
- Read active contracts, current Git state, relevant evidence, and only the
  files needed for the task.
- Use the project's `PROJECT_STATE.md` and any existing handoff artifact.
- Avoid repeating broad Project Intelligence once the gate is complete.
- Do not have Claude duplicate Codex work merely for redundancy; use
  independent review only when it adds decision value.

For Claude Code specifically: use `/clear` between unrelated tasks; keep one
session while the same bounded task continues; use Medium effort by default.

## 7. Agent configuration (no credentials)

- `/home/pc_pusaka/zandi/.codex` — Codex state/config.
- `/home/pc_pusaka/zandi/.claude` — Claude Code state/config.
- `~/.claude` — currently a compatibility symlink to
  `/home/pc_pusaka/zandi/.claude`.

Do not migrate `.codex` / `.claude` into a common folder now. A possible future
housekeeping target is `/home/pc_pusaka/zandi/.ai/{codex,claude}/`; this is
**not approved** for implementation. Global configuration mutation, including
`~/.codex` and `~/.claude` contents, remains an explicit approval boundary.

## 8. Project-level Claude adapter

A project may carry a thin `CLAUDE.md` that imports or references the canonical
project instructions (such as `AGENTS.md`). `CLAUDE.md` must not become a
competing governance source. The canonical project contracts, policies, tests,
evidence, and `AGENTS.md` remain authoritative.

## 9. New-chat bootstrap

For a new Zandi Orchestrator chat, provide/read:

1. the Zandi instructions package/repository;
2. the active project's `PROJECT_STATE.md`.

Optionally add a special compact handoff only when the project is mid-sprint or
extra context is genuinely required.

Global instructions = **how we work**. `PROJECT_STATE.md` = **where the project
is now**. The project repository = the detailed source of truth. Global
instructions do not contain the complete live state of every project.
