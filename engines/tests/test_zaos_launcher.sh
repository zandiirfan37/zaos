#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/../.." && pwd -P)
LAUNCHER="$ROOT/engines/bin/zaos"
SESSION="$ROOT/engines/bin/zaos-session"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# Force the session router's recursion-guard binary resolution to fall back to
# PATH (this test's harmless stand-in CLIs) instead of a real host install of
# the native-command shims under ~/.local/lib/zaos-real-bin.
export ZAOS_REAL_BIN_DIR="$TMP/no-real-bin-on-this-host"

fail() { printf 'FAIL: %s\n' "$*" >&2; exit 1; }
expect() { [[ "$1" == *"$2"* ]] || fail "expected [$2] in [$1]"; }

P="$TMP/project"; mkdir "$P"; git -C "$P" init -q

plan=$(cd "$P" && "$LAUNCHER" terra --print-plan)
expect "$plan" "ZAOS_PROJECT=$P"; expect "$plan" "ZAOS_ENGINE=terra"; expect "$plan" "ZAOS_CAPABILITY=NORMAL_MUTATIVE_PROJECT"
plan=$(cd "$P" && "$LAUNCHER" claude --print-plan)
expect "$plan" "ZAOS_ENGINE=claude"
plan=$(cd "$ROOT/.." && "$LAUNCHER" --print-plan)
expect "$plan" "ZAOS_CAPABILITY=ZAOS_MAINTENANCE"
root_out=$(cd "$ROOT/.." && "$LAUNCHER" --print-plan 2>&1)
[[ "$root_out" != *"not a git repository"* ]] || fail "workspace root leaked raw Git error"
plan=$("$LAUNCHER" terra "$P" --local-dev --print-plan)
expect "$plan" "ZAOS_CAPABILITY=FULL_LOCAL_DEV"
plan=$("$LAUNCHER" codex "$P" --external-publish --print-plan)
expect "$plan" "ZAOS_CAPABILITY=ZAOS_EXTERNAL_PUBLISH"
if "$LAUNCHER" codex "$P" --local-dev --external-publish --print-plan >/dev/null 2>&1; then
  fail "mutually exclusive elevated capabilities were accepted"
fi

# Project/task capability declaration: a project can ask for FULL_LOCAL_DEV
# itself via .zaos-capability, with no --local-dev flag and no project-name
# hardcoding in the launcher.
plan=$(cd "$P" && "$LAUNCHER" terra --print-plan)
expect "$plan" "ZAOS_CAPABILITY=NORMAL_MUTATIVE_PROJECT"
printf '# local services required\nFULL_LOCAL_DEV\n' > "$P/.zaos-capability"
plan=$(cd "$P" && "$LAUNCHER" terra --print-plan)
expect "$plan" "ZAOS_CAPABILITY=FULL_LOCAL_DEV"
rm -f "$P/.zaos-capability"

# Exercise the real public → internal router path using harmless stand-in
# CLIs.  This proves the engine mapping and session profile without starting
# an interactive provider session.
BIN="$TMP/bin"; mkdir "$BIN"
for name in codex claude; do
  cat > "$BIN/$name" <<'EOF'
#!/usr/bin/env bash
printf '%s\n' "$0 $*" > "$ZAOS_CAPTURE"
EOF
  chmod +x "$BIN/$name"
done
capture="$TMP/capture"
PATH="$BIN:$PATH" ZAOS_CAPTURE="$capture" "$LAUNCHER" terra "$P" -- smoke
got=$(<"$capture"); expect "$got" "codex --sandbox workspace-write -C $P"; expect "$got" "--add-dir $P/.git smoke"
PATH="$BIN:$PATH" ZAOS_CAPTURE="$capture" "$LAUNCHER" claude "$P" -- smoke
got=$(<"$capture"); expect "$got" "claude --permission-mode auto"; expect "$got" "--add-dir $P/.git smoke"
PATH="$BIN:$PATH" ZAOS_CAPTURE="$capture" "$LAUNCHER" codex "$P" --external-publish -- smoke
got=$(<"$capture"); expect "$got" "sandbox_workspace_write.network_access=true"

# This execution environment forbids socket syscalls, so it cannot host the
# loopback service needed to pass the real preflight. Verify public selection
# at the session boundary, then separately assert the real preflight fails
# closed below.
fake_session="$TMP/fake-session"
cat > "$fake_session" <<'EOF'
#!/usr/bin/env bash
printf '%s\n' "$*" > "$ZAOS_CAPTURE"
EOF
chmod +x "$fake_session"
ZAOS_SESSION_BIN="$fake_session" ZAOS_CAPTURE="$capture" "$LAUNCHER" terra "$P" --local-dev -- smoke
got=$(<"$capture"); expect "$got" "FULL_LOCAL_DEV codex $P -- smoke"
if PATH="$BIN:$PATH" ZAOS_CAPTURE="$capture" "$LAUNCHER" terra "$P" --local-dev -- smoke 2>"$TMP/full-local-dev.err"; then
  fail "FULL_LOCAL_DEV unexpectedly bypassed loopback preflight"
fi
expect "$(<"$TMP/full-local-dev.err")" "CAPABILITY_BLOCKED: loopback service unreachable"

# The internal command remains callable independently.
PATH="$BIN:$PATH" ZAOS_CAPTURE="$capture" "$SESSION" ZAOS_MAINTENANCE codex "$ROOT" -- smoke
got=$(<"$capture"); expect "$got" "codex --sandbox workspace-write -C $ROOT"
[[ "$got" != *"network_access=true"* ]] || fail "ordinary maintenance unexpectedly has network egress"
printf 'PASS: zaos public launcher discovery, profiles, engine routes, and internal session compatibility\n'
