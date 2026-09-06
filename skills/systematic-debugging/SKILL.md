---
name: systematic-debugging
description: Diagnose a bug, failing test, build failure, or unexpected behavior from evidence before proposing a fix. Use when the cause is not already demonstrated; not for a known trivial edit.
---

# Systematic debugging

Find the smallest demonstrated cause before changing code. This is a fast path out of guess-and-check, not a mandatory investigation for a known typo.

1. Reproduce or capture the failure; read the actual error and affected boundary.
2. Trace backward through relevant inputs, state, and recent changes; compare one known-working analogue when discriminating.
3. State one smallest testable hypothesis, test it, then make the narrow fix.
4. Verify the original symptom and closest regression boundary.

After two failed speculative fixes, stop patching and return to evidence. If the cause is external or timing-dependent, record the investigation and add the smallest appropriate handling/observability; do not pretend it was fixed.

Use normal project authority for tests, access, and escalation. Do not turn this into a universal TDD, subagent, or postmortem requirement.
