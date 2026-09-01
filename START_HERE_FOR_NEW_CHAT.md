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

When continuing an existing project, also read that project's compact
current-state/handoff artifact. Global instructions define how to work, not the
full live state of every project.

ECC-Zandi Standard-Advanced is the current validated project-workflow harness.
ZAINE is frozen for now. Treat all frameworks and projects as independent Git
repositories; the Zandi root is behaviorally non-Git. Keep work local and do
not mutate global configuration or activate integrations without approval.

For every completed project, request a concise **Framework lessons learned**
section and classify any reusable finding through the improvement loop.
