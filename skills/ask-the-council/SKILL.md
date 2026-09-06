---
name: ask-the-council
description: Run a bounded, read-only, multi-perspective council for a consequential decision or genuine tradeoff. Use only when independent viewpoints and cross-examination could change the decision; do not use for routine coding or simple edits.
---

# Ask the Council

## Zandi usage policy

Default to **one builder / fast path**. Convene a council only for a major
architecture decision, meaningful scientific trade-off, competing plausible
strategies, an expensive or irreversible choice, or when the Human explicitly
asks for one.

Do **not** convene one for routine coding, obvious fixes, simple factual
questions, ordinary file edits, decisions already locked, or any task where a
second opinion cannot change the outcome. State that the council is
unnecessary and proceed directly for those cases.

A task that starts routine can cross into a consequential decision boundary
mid-task (for example, a routine refactor reveals that a scientific formula's
semantics would materially change). When that happens, stop, name the
boundary crossed, and recommend Council or the relevant skill/evidence rather
than silently continuing — this is `RECOMMEND_COUNCIL_AND_STOP`, the default.
Self-convening Council automatically (`AUTO_USE_COUNCIL`) is not a global
default; it requires explicit, project-local Human authority recorded in that
project's `AGENTS.md`.

Council delegates are advisory and read-only by default: give them only the
minimum context needed, do not ask them to modify files, and keep outputs
bounded. Use the default three-member triad; enlarge the panel only when the
decision is unusually ambiguous. Record disagreement rather than forcing
consensus.

Use this skill when the user wants a multi-perspective council rather than a
single answer. Good triggers include:

- "run a council on this"
- "get multiple perspectives"
- "debate this decision"
- "stress test this plan"
- architecture, product, strategy, debugging, research, fiction, philosophy,
  editorial, risk, or founder tradeoffs

If `$ARGUMENTS` is non-empty, treat it as the problem statement. Otherwise ask
the user for the question to deliberate on.

## First Step

Read only the references you need:

- `references/profiles.yaml` for panel selection
- `references/protocol.md` for orchestration
- `references/verdict-template.md` for final output shape
- `references/personas/<member>.md` only for the members you actually select

## Defaults

- Prefer 3 members unless the user asks for a full panel or the problem is
  unusually ambiguous.
- Without an explicit panel/profile, derive three complementary **roles** from
  the decision surface rather than defaulting to an architecture panel. Include
  a domain/craft perspective, a skeptical or methodological counterweight, and
  the relevant reader/user/stakeholder perspective. Examples: methodology /
  statistics / domain skeptic for science; novelist / developmental editor /
  reader for fiction; philosopher / argument critic / editor for an essay;
  analyst / source skeptic / domain specialist for web research.
- Use a named persona/profile only when it was requested or clearly provides
  the needed role. The legacy profiles are a compact fallback for generic
  strategy/architecture questions, not a role catalog that limits domains.
- Keep the final verdict compact unless the user asks to see the rounds.

## Workflow

### 1. Resolve The Panel

Honor, in order:

1. explicit `--members`
2. explicit `--triad`
3. explicit `--profile`
4. a dynamically derived complementary role triad for the actual decision
5. keyword triad or `classic` fallback only if dynamic role selection is not
   informative

### 2. Round 1: Independent Analysis

- Run each selected member independently.
- Keep round 1 blind-first: each member sees only the problem statement and
  their own persona text.
- Ask for a compact standalone analysis that ends with a clear verdict,
  confidence, and where the member may be wrong.

Preferred orchestration:

- If the host supports explicit subagents or forked contexts, use one
  independent delegate per selected member.
- In Codex, prefer `spawn_agent`, then `send_input` and `wait_agent`.
- In Amp, prefer one `oracle` call per selected member.
- In Claude Code, use parallel or forked agent contexts when they are
  available. If they are not easy to access, keep the protocol in the main
  session and separate the member outputs clearly.

Suggested round 1 packet:

```text
You are operating as one member of a structured council.

Persona:
{persona}

Problem:
{problem}

Produce a compact standalone analysis.
End with a clear verdict, confidence, and where you may be wrong.
Do not anticipate the other members.
```

### 3. Round 2: Cross-Examination

- Share the round 1 outputs with each member.
- Ask each member to:
  - name the position they most disagree with and why
  - name one insight that strengthened their thinking
  - say whether anything changed
  - restate their position after the exchange
- Prefer sequential execution so later responses can react to earlier
  disagreements.

If another delegate pass would be disproportionate, run the cross-exam locally
and disclose that choice.

Suggested round 2 packet:

```text
Here are the other council members' round 1 analyses:

{peer_outputs}

Respond to all of the following:
1. Which member do you most disagree with, and why?
2. Which member strengthened your thinking, and how?
3. What changed, if anything?
4. Restate your position after the exchange.

Keep it compact and engage at least two members by name.
```

### 4. Round 3: Final Position

- Ask for a short final stance only.
- No new arguments unless a host limitation forces a condensed fallback.
- Socrates may ask one final question before stating a position.

### 5. Synthesis

- Use `references/verdict-template.md`.
- Default to the final verdict only.
- If the user asks to show rounds, include concise round summaries after the
  verdict.

## Fallback Mode

If the host cannot cleanly support multi-round orchestration, or the full
protocol would be disproportionate:

1. simulate round 1 as clearly separated persona sections
2. simulate round 2 as explicit cross-exam sections
3. simulate round 3 as final positions
4. disclose that you used the single-agent fallback

## Guardrails

- Do not force consensus.
- If the panel converges too quickly, run one counterfactual pass.
- Prefer substance over theater: the council should improve the answer, not
  just decorate it.
