# Session provisioning

`bin/zaos-session` is the canonical local launcher for bounded ZAOS sessions.
It resolves both the Git worktree and its actual metadata directory with Git;
it never assumes `.git` is a directory.

| Capability | Command shape | Writable scope |
| --- | --- | --- |
| `READ_ONLY` | `zaos-session READ_ONLY <engine> <repo>` | No project mutation. |
| `NORMAL_MUTATIVE_PROJECT` | `zaos-session NORMAL_MUTATIVE_PROJECT <engine> <project-repo>` | Project worktree and its resolved Git metadata only. `.agents` is rejected. No loopback network. |
| `FULL_LOCAL_DEV` | `zaos-session FULL_LOCAL_DEV <engine> <project-repo>` | Same scope as `NORMAL_MUTATIVE_PROJECT`, plus loopback network access, for the task class that needs live local-service verification (DB/RAGFlow/UAT). Runs a capability preflight before launch and fails fast with `CAPABILITY_BLOCKED` rather than letting an agent discover a missing capability after minutes of work. `.agents` is rejected. |
| `ZAOS_MAINTENANCE` | `zaos-session ZAOS_MAINTENANCE <engine> <.agents-repo>` | The explicitly selected `.agents` repository and its resolved Git metadata only. |

## FULL_LOCAL_DEV: the network-parity gap

Filesystem/Git parity between engines was already solved (see the 2026-09-08
evidence below). A separate gap surfaced during a Stage 08T attempt in
`projects/05_chatbot_rag`: a Codex session reported `.git/index` read-only
*and* PostgreSQL/RAGFlow/UAT loopback EPERM. Root-caused 2026-09-12:

- Codex's `--sandbox workspace-write` (and `read-only`) denies **all**
  network syscalls, including loopback, as an inherent part of the sandbox
  profile — confirmed with a live probe: `curl 127.0.0.1:19381` returns
  `Failed to connect ... Couldn't connect to server` under `workspace-write`,
  but `HTTP 404` (reachable) from an unsandboxed shell on the same host.
- Claude's `--permission-mode auto` does not restrict network syscalls in
  any mode — this is why Claude sessions never saw this failure. The two
  engines were never on an equivalent capability profile for network; this
  was not a Claude-only allowance someone had to notice, it's a difference
  in what each CLI's sandbox primitive controls.
- The only documented way to unblock network in Codex CLI 0.150.1 without
  widening filesystem access is the config key
  `sandbox_workspace_write.network_access=true` under `--sandbox
  workspace-write`. Verified: with this key set, loopback HTTP succeeds
  *and* a write outside the granted roots still fails
  `Read-only file system` — filesystem containment is unaffected.
  `--sandbox danger-full-access` also unblocks network but removes
  filesystem containment too, so it is not used for this task class.
- `zaos-session FULL_LOCAL_DEV codex ...` therefore adds exactly
  `-c 'sandbox_workspace_write.network_access=true'` on top of the normal
  `workspace-write --add-dir <git-dir>` route. Claude's `FULL_LOCAL_DEV`
  route is identical to `NORMAL_MUTATIVE_PROJECT` — no extra grant needed.
- The Stage 08T session itself was not re-launched or altered by this fix;
  its uncommitted work in `projects/05_chatbot_rag` is untouched. The
  most parsimonious explanation for its failure is that it was not started
  through `zaos-session`, matching the same anti-pattern already documented
  below for Git-metadata resolution.
- Terra (Codex, `gpt-5.6-terra`) proved the corrected route itself on
  2026-09-12 in the disposable fixture
  `.runtime/session-fixtures/full-local-dev-smoke/`: filesystem write,
  a real Git commit, a TCP-level Postgres connection on `:5442`, an HTTP
  reach to RAGFlow on `:19381`, an HTTP 200 `/ready` from the UAT gateway
  on `:8090`, and `ss -tln` listing all three listeners — non-destructively,
  outside any product repository.

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
