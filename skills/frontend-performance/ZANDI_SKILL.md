# Zandi skill metadata — Frontend Performance

- **Name:** frontend-performance
- **Category / status:** WORKFLOW / TESTED (fast intake)
- **Owner:** React/Next.js rendering, async/data-flow, and bundle performance;
  UI/UX Pro Max owns visual, interaction, and accessibility decisions.
- **Sources:** `vercel-labs/agent-skills` react-best-practices at
  `063bee94c3f4df8453406c830b0a7df0f2860278` (MIT).
- **Adaptation:** retained the priority order of waterfalls, bundle cost,
  server/client data flow, rerenders, and rendering cost; removed the 70-rule
  corpus and framework-specific prescriptions until a real path needs them.
- **Fast-intake checks:** `quick_validate.py`; smoke scenarios for sequential
  fetches, a heavy optional component, and a speculative memoization request.
- **Promotion:** real-project use before TRUSTED.
