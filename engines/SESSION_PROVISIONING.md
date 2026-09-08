# Session provisioning

`bin/zaos-session` is the canonical local launcher for bounded ZAOS sessions.
It resolves both the Git worktree and its actual metadata directory with Git;
it never assumes `.git` is a directory.

| Capability | Command shape | Writable scope |
| --- | --- | --- |
| `READ_ONLY` | `zaos-session READ_ONLY <engine> <repo>` | No project mutation. |
| `NORMAL_MUTATIVE_PROJECT` | `zaos-session NORMAL_MUTATIVE_PROJECT <engine> <project-repo>` | Project worktree and its resolved Git metadata only. `.agents` is rejected. |
| `ZAOS_MAINTENANCE` | `zaos-session ZAOS_MAINTENANCE <engine> <.agents-repo>` | The explicitly selected `.agents` repository and its resolved Git metadata only. |

For a commit-capable Codex project session, the critical provision is the
CLI-supported `--add-dir "$(git rev-parse --absolute-git-dir)"` paired with
`--sandbox workspace-write`. Codex otherwise mounts the worktree writable but
its Git metadata read-only, so `git add` cannot create `index.lock`.

Claude uses its supported working-directory plus `--add-dir <resolved-git-dir>`
route with `--permission-mode auto`; it does not use `bypassPermissions`.
Its `--restricted` mode is deliberately not used for mutations because that
mode removes command/code execution and cannot perform Git transactions.

The modes are selected before mutation. If the engine or a managed host denies
the required capability, preflight fails before project changes. The launcher
does not chmod, remount, or widen the Zandi root.

## Evidence, 2026-09-08

The Codex runtime fragment at
`.runtime/engines/codex/config.toml` supplied only the UV cache as an additional
`sandbox_workspace_write.writable_roots` entry; it had no Git-directory
resolution or launch routing. A fresh Codex `workspace-write` fixture session
therefore wrote `prepatch.txt` but failed `git add` with a read-only
`.git/index.lock`. The Codex CLI help documents `--add-dir` as an additional
writable directory. Runtime session evidence for successful ZAOS commits shows
the Codex session was started at `/home/pc_pusaka/zandi` and committed with
`git -C projects/04_zaos`; the failing fresh session was started directly at
`projects/04_zaos` and reported its Git directory non-writable. The meaningful
provisioning difference is therefore the workspace root / explicit writable
Git-directory scope, not Unix ownership or mount flags. The active maintenance
session separately demonstrates that an externally selected
`danger-full-access` profile can write the maintenance repository; it is not
the normal-project route.
