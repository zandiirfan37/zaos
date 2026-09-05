# Ask the Council / Council Skill

- **Remote:** https://github.com/tsenart/council-skill
- **Pinned commit:** `2040ee1bfb1c7b4c4d42f0924265c36b443681f9`
- **Purpose:** Portable, bounded multi-agent deliberation for consequential decisions and genuine trade-offs.
- **License:** MIT (locally detected).
- **Stars:** not recorded locally.
- **Architecture/features:** a skill entry point plus local panel profiles, persona briefs, three-round protocol (blind-first analysis, cross-examination, final positions), and a compact verdict template. It supports Codex, Claude Code, Amp, and graceful single-agent fallback.
- **Why adopted:** it is the smallest inspected implementation that directly supports Codex and enforces independent first-round analysis without APIs, installer infrastructure, or executable runtime code.
- **Dataset availability:** none.
- **Adoption mode:** COMPONENT / REASONING_SKILL.
- **Canonical local skill location:** `.agents/skills/ask-the-council/`.
- **Local clone status:** runtime payload installed; upstream inspection clone is temporary.
- **Catalogued:** 2026-09-05.
