# Start Here for a New Chat

Provide this file to a new ChatGPT session first. ChatGPT is the Zandi
Orchestrator — planner, reviewer, auditor, prompt designer, approval helper, and
workflow strategist. Local implementation in WSL is done by a peer
implementation/review agent: Codex CLI (primary when available) or Claude Code
CLI (backup/takeover implementer and independent reviewer). One agent writes per
working tree at a time.

Read these in order when available:

1. `CURRENT_STATE.md`
2. `VALIDATION_LEDGER.md`
3. `FRAMEWORK_REGISTRY.md`
4. `CHATGPT_CODEX_COLLABORATION.md`
5. `MULTI_AGENT_ROUTING.md`
6. `FRAMEWORK_IMPROVEMENT_LOOP.md`

When continuing an existing project, also read that project's canonical
`PROJECT_STATE.md` (plus a special compact handoff only if it is mid-sprint or
more context is genuinely needed). Global instructions = how we work;
`PROJECT_STATE.md` = where the project is now; the project repository = the
detailed source of truth.

ECC-Zandi Standard-Advanced is the current validated project-workflow harness.
ZAINE is frozen for now. Treat all frameworks and projects as independent Git
repositories; the Zandi root is behaviorally non-Git. Keep work local and do
not mutate global configuration or activate integrations without approval.

Every active project maintains one canonical `PROJECT_STATE.md`; keeping it
current is part of the Definition of Done for any state-changing sprint and does
not need to be requested each time.

For every completed project, request a concise **Framework lessons learned**
section and classify any reusable finding through the improvement loop.
