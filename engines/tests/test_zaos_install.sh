#!/usr/bin/env bash
# Portable install smoke: isolated HOME, fake vendor CLIs, no host mutation.
set -euo pipefail
unset ZAOS_INTERNAL_EXEC
ROOT=$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/../.." && pwd -P)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
HOME="$TMP/home"
export HOME
BIN="$HOME/.local/bin"
mkdir -p "$BIN" "$TMP/workspace/project"
git -C "$TMP/workspace/project" init -q
for n in codex claude; do
  printf '#!/usr/bin/env bash\nprintf "vendor-%s %%s\\n" "$*"\n' "$n" > "$BIN/$n"
  chmod +x "$BIN/$n"
done
export PATH="$BIN:$PATH"
"$ROOT/install.sh" --workspace "$TMP/workspace" >/dev/null
"$ROOT/install.sh" --workspace "$TMP/workspace" >/dev/null
[ -x "$BIN/zaos" ] || { echo 'FAIL: zaos command absent'; exit 1; }
[ -x "$HOME/.local/share/zaos/real-bin/codex" ] || { echo 'FAIL: raw codex absent'; exit 1; }
grep -qF "ZAOS_WORKSPACE_ROOT=\"$TMP/workspace\"" "$HOME/.config/zaos-native/config.sh" || { echo 'FAIL: workspace config absent'; exit 1; }
plan=$(cd "$TMP/workspace/project" && "$BIN/zaos" codex --print-plan)
printf '%s\n' "$plan" | grep -q 'ZAOS_CAPABILITY=NORMAL_MUTATIVE_PROJECT' || { echo 'FAIL: project discovery'; exit 1; }
outside="$TMP/outside"
mkdir "$outside"
out=$(cd "$outside" && codex --version)
printf '%s\n' "$out" | grep -q 'vendor-codex' || { echo 'FAIL: outside passthrough'; exit 1; }
"$ROOT/uninstall.sh" >/dev/null
[ -x "$BIN/codex" ] || { echo 'FAIL: uninstall did not restore vendor'; exit 1; }
echo 'PASS: fresh install, idempotence, discovery, passthrough, and recovery'
