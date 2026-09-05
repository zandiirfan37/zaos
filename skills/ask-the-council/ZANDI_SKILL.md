# Zandi skill metadata — Ask the Council

- **Upstream source:** https://github.com/tsenart/council-skill
- **Pinned upstream commit:** `2040ee1bfb1c7b4c4d42f0924265c36b443681f9`
- **License:** MIT (locally verified; included as `LICENSE`)
- **Category:** REASONING
- **Status:** TESTED
- **Installed:** 2026-09-05
- **Why selected:** compact, portable protocol with blind-first independent analysis, cross-examination, disagreement-preserving synthesis, and documented Codex orchestration; it requires no external provider, API key, or runtime script.
- **Upstream files retained:** `SKILL.md`, `references/profiles.yaml`, `references/protocol.md`, `references/verdict-template.md`, and the selected-panel persona references; `LICENSE` is retained for attribution.
- **Local modifications:** renamed the skill to `ask-the-council` and added the Zandi usage policy and explicit read-only, bounded-cost defaults to `SKILL.md`. No executable code was added or altered.
- **Update procedure:** temporarily inspect a pinned upstream revision under `.runtime/tmp/`; review its license and diff only the retained files; copy reviewed runtime material into this directory; reapply and review the documented local policy; test discovery and bounded deliberation before committing.
- **External model/API requirements:** none beyond the invoking agent's normal model access. Full independent mode requires host support for isolated agent contexts; no network/API call is required by the retained files. A clearly disclosed single-agent fallback is permitted when isolation is unavailable.

Do not casually edit upstream-derived files. Keep local policy changes minimal and documented here.
