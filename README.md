# ZAOS

ZAOS is a portable, model-neutral agent operating framework for Codex and Claude. It keeps the native commands people already use while applying project-aware, proportional capability routing inside one managed workspace. It never installs vendor software or secrets.

## Supported engines

- Codex
- Claude

## First install

```bash
git clone https://github.com/zandiirfan37/zaos.git
cd zaos
./install.sh --workspace ~/my-workspace
```

The installer is idempotent. It preserves the real vendor binaries, installs scoped native shims, and makes the `zaos` admin command available in `~/.local/bin` (ensure that directory is on your `PATH`). One installed engine is sufficient.

## Normal daily use

```bash
cd ~/my-workspace/my-project
codex
```

or:

```bash
claude
```

Inside the managed workspace, ZAOS discovers the Git project and applies the appropriate capability. Outside it, `codex` and `claude` retain their normal vendor behavior.

## Administration, updates, and recovery

```bash
zaos doctor
zaos engines status
zaos update
```

`zaos update` requires a clean framework checkout, fetches its configured canonical origin, fast-forwards only when safe, runs any migrations, refreshes shims, checks engine status, and runs doctor. It stops rather than guessing. Vendor CLI upgrades remain your choice; after one, use `zaos engines refresh` with an explicit vendor-path hint if a preserved raw-engine pointer needs repair.

If routing is unhealthy, the preserved raw binary path is shown by `zaos engines status`; run it directly, or use `ZAOS_INTERNAL_EXEC=1 codex` / `claude` to bypass routing. Run `./uninstall.sh` from the framework checkout to restore the native entries installed by ZAOS.

## Remote Git and publication

Normal sessions remain proportionally sandboxed. For remote Git or GitHub work, explicitly launch the needed project:

```bash
zaos codex <project> --remote-git
# or
zaos claude <project> --remote-git
```

For explicit releases or other public/external publication, use `--external-publish`. These modes are distinct from ordinary work and from each other.

## Operating model and agent workflow

The Human Lead owns architecture, product decisions, and `HUMAN_PASS`. The Orchestrator owns constraints, acceptance, and problem definition. An agent investigates, implements, and verifies; it may report `ENGINEERING_PASS`, but never replaces Human Audit. Perform Human Audit early in product development.

To install with another coding agent, give it: “Clone ZAOS from https://github.com/zandiirfan37/zaos and install it into my workspace. Follow the canonical repository instructions. Do not replace my vendor Codex or Claude installations. Run `zaos doctor` afterward and report PASS/BLOCKED.”

For later maintenance: “Update ZAOS to the newest compatible canonical version. Run required migrations and `zaos doctor`. Do not modify my projects. Stop and report if verification fails.”

Read [ZAOS_HUMAN.md](ZAOS_HUMAN.md) for the operator guide and [ZAOS_ORCHESTRATOR.md](ZAOS_ORCHESTRATOR.md) for the agent/orchestrator contract. Technical detail is under [engines/](engines/README.md) and [instructions/](instructions/README.md).

## Repository shape

This is the single canonical framework repository. `instructions/` is tracked here, not a submodule. Projects, private runtime, secrets, caches, and private project material are excluded.
