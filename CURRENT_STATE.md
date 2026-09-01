# Current Zandi State

Zandi is rooted at `/home/pc_pusaka/zandi`. Its root remains intentionally
behaviorally non-Git; frameworks and projects are independent Git repositories
with their own history, status, and remote policy.

## Framework state

- ZAINE: `/home/pc_pusaka/zandi/frameworks/zaine` — frozen for now.
- ECC upstream: `/home/pc_pusaka/zandi/frameworks/ecc/upstream` at
  `005eff40fd4a4ac005da7a70e713459175385516` — keep clean and updateable.
- ECC-Zandi Standard-Advanced:
  `/home/pc_pusaka/zandi/frameworks/ecc/zandi-profile` — the validated,
  controlled project-workflow adapter for selected ECC reference material.

The adapter is not an ECC installation or global integration. Global
configuration mutation, including `~/.codex` and `~/.claude`, remains forbidden
unless explicitly approved.

## Agents

Zandi has two peer implementation/review agents: Codex CLI (primary) and Claude
Code CLI (backup/takeover implementer, independent reviewer). ChatGPT is the
Orchestrator; the Human Lead is final authority. State/config lives in
`/home/pc_pusaka/zandi/.codex` and `/home/pc_pusaka/zandi/.claude`; `~/.claude`
is currently a compatibility symlink to `/home/pc_pusaka/zandi/.claude`. One
agent writes per working tree at a time. See `MULTI_AGENT_ROUTING.md`.

## Project state protocol

Every active Zandi project maintains one canonical `<project-root>/PROJECT_STATE.md`
(template: `templates/PROJECT_STATE.template.md`) describing where that project
is now. Keeping it current is part of the Definition of Done for any
state-changing sprint; see `ZANDI_MASTER_WORKFLOW.md`. This file
(`CURRENT_STATE.md`) covers the workspace and frameworks, not per-project state.

## Validated project evidence

`/home/pc_pusaka/zandi/projects/ecc-minilab-pilot` is the validated ECC-Zandi
pilot. Read `VALIDATION_LEDGER.md` before treating its lessons as reusable
guidance.

## Model routing

Roles are durable; routing is adaptive. Current defaults: bounded implementation
uses Terra Medium (Codex) or Sonnet Medium (Claude Code); substantial
architecture synthesis and justified independent review use Terra High (Codex)
or Sonnet High / a stronger reasoning model (Claude Code); exceptional complex
design or debugging uses the strongest available tier only when complexity/risk
justifies the cost. Select for task complexity, risk, reasoning depth, latency,
efficiency, quota, implementation volume, independent perspective, and currently
available models; these are not permanent rules. Claude Code routing is also
bounded by the Claude weekly operating budget in `MULTI_AGENT_ROUTING.md`
(>= 60% weekly usage: stop Claude work until reset unless the Human Lead
overrides; Medium effort by default).
