# Codex Prompt Examples

Replace bracketed values. Each template is intentionally bounded.

## 1. Project inventory

> Inspect `[PROJECT_PATH]` read-only. Report Git status, tree, runtime,
> dependencies, tests, risks, and likely framework fit. Do not modify files,
> globals, remotes, or other repositories. Output: STATUS, INVENTORY, RISKS,
> RECOMMENDED NEXT ACTION. STOP.

## 2. New web app

> Build `[PROJECT_NAME]` only in `[PROJECT_PATH]` using `[STACK]`. Inspect
> first; use ECC-Zandi web-app guidance if suitable. Keep it local-only: no
> global config, deployment, remote, secrets, or framework activation. Add
> tests and README, validate, commit locally only if requested. Output: STATUS,
> PLAN, FILES, TESTS, RISKS, NEXT ACTION. STOP.

## 3. Existing-project audit

> Independently audit `[PROJECT_PATH]` for architecture, data safety, tests,
> dependency hygiene, security boundaries, and Git hygiene. Read-only only; do
> not start a server without asking. Output: STATUS, VERDICT, STRENGTHS,
> ISSUES, TEST ADEQUACY, PATCH PRIORITIES, NEXT ACTION. STOP.

## 4. App hardening patch

> Patch only `[PROJECT_PATH]` for these findings: `[FINDINGS]`. Preserve scope;
> do not redesign or touch frameworks/globals/remotes. Add regression tests,
> run targeted gates, inspect diff, and commit locally with `[MESSAGE]`. Output:
> STATUS, FILES CHANGED, TESTS, SECURITY RESULT, COMMIT, LIMITATIONS. STOP.

## 5. Terra High review

> Perform an independent senior review of `[PROJECT_PATH]` after `[COMMITS]`.
> Do not modify or commit. Inspect source, Git, and safe local gates only; ask
> before server/browser checks. Output: STATUS, VERDICT, REGRESSION RISKS,
> ISSUES, TEST ADEQUACY, READINESS, NEXT ACTION. STOP.

## 6. ECC-Zandi profile patch

> Update only `[PROFILE_PATH]` from this evidence: `[AUDIT_OR_PILOT]`. Keep it
> concise, on-demand, and project-local; do not change ECC upstream, globals,
> or projects. Validate Markdown/structured files, commit locally only with
> `[MESSAGE]`. Output: STATUS, FILES UPDATED, GUIDANCE ADDED, VALIDATION,
> COMMIT, NEXT ACTION. STOP.

## 7. Legacy migration inventory

> Inspect `/home/pc_pusaka/Eksperimen` read-only. Do not move, delete, rewrite,
> install, or modify anything. Inventory projects and classify each as
> KEEP_AS_ARCHIVE, PATCH_IN_PLACE, REBUILD_CLEAN, MIGRATE_DATA_ONLY, or
> DEPRECATE. Output the required legacy artifacts and approval boundaries.
> STOP.

## 8. Approval-risk checklist

> Before acting on `[TASK]`, identify all commands or changes needing approval:
> destructive data/file work, migrations, network, loopback servers/browsers,
> globals, secrets, remotes, pushes, deployment, or framework changes. Do not
> execute them. Output: SAFE NOW, APPROVAL REQUIRED, RISK, ALTERNATIVES. STOP.

## 9. Normal bounded sprint (canonical)

Default pattern for routine work. Do not restate standard ECC gates — the
agent derives them from repository governance. Add a scientific/product
constraint or an exceptional prohibition only when one actually applies.

> Execute `[BOUNDED_OBJECTIVE]` from current `PROJECT_STATE.md` and active
> contracts. Apply all relevant ECC gates automatically. Own implementation,
> validation, `PROJECT_STATE.md` update, and local commit. Escalate only
> material blockers. Output: STATUS, CHANGES, TESTS, STATE UPDATE, COMMIT.
> STOP.
