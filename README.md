# ZAOS

ZAOS is a small, model-neutral operating framework for Codex and Claude. In a managed workspace, people use native commands:

```bash
codex
claude
```

ZAOS discovers the project, selects proportional capability, then runs the real vendor engine. Outside that workspace, commands retain vendor behaviour. ZAOS never installs secrets or vendor software, and preserves raw-engine escape.

## Quick start

```bash
git clone <canonical-zaos-url> zaos
cd zaos
./install.sh --workspace ~/my-workspace
cd ~/my-workspace/my-project
codex
```

One installed engine is enough. Run `./uninstall.sh` to remove ZAOS shims. `zaos update` performs a guarded update, not a blind `git pull`.

Read [ZAOS_HUMAN.md](ZAOS_HUMAN.md) to use or recover ZAOS. Agents and orchestrators start with [ZAOS_ORCHESTRATOR.md](ZAOS_ORCHESTRATOR.md). Technical detail is under [engines/](engines/README.md) and [instructions/](instructions/README.md).

## Repository shape

This is the one canonical framework repository. `instructions/` is tracked here, not a submodule; its earlier standalone history is preserved in the consolidation merge. Projects, private runtime, secrets, caches, and the ZAOS book are outside it.
