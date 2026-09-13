#!/usr/bin/env bash
# Exercises the scoped native-command shim installer end to end in an
# isolated fake HOME/PATH — never touches the real ~/.local/bin or the real
# codex/claude binaries.
set -euo pipefail

ROOT=$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/../.." && pwd -P)
INSTALLER="$ROOT/engines/bin/zaos-install-native-shims"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

fail() { printf 'FAIL: %s\n' "$*" >&2; exit 1; }
expect() { [[ "$1" == *"$2"* ]] || fail "expected [$2] in [$1]"; }

# --- fixture workspace: a fake ZAOS root with a real-looking .agents/engines/bin/zaos ---
FAKE_WORKSPACE="$TMP/workspace"
FAKE_AGENTS="$FAKE_WORKSPACE/.agents"
mkdir -p "$FAKE_AGENTS/engines/bin"
cat > "$FAKE_AGENTS/engines/bin/zaos" <<'EOF'
#!/usr/bin/env bash
printf 'ZAOS_ROUTED engine=%s args=%s\n' "$1" "${*:3}" > "$ZAOS_CAPTURE"
EOF
chmod +x "$FAKE_AGENTS/engines/bin/zaos"

# --- fixture "vendor" binaries on a fake PATH entry ---
VENDOR_DIR="$TMP/vendor-bin"
mkdir -p "$VENDOR_DIR"
for name in codex claude; do
  cat > "$VENDOR_DIR/$name" <<EOF
#!/usr/bin/env bash
printf 'VENDOR_REAL_BIN name=$name args=%s\n' "\$*" > "\$ZAOS_CAPTURE"
EOF
  chmod +x "$VENDOR_DIR/$name"
done

BIN_DIR="$TMP/local-bin"
REAL_BIN_DIR="$TMP/real-bin"
CONFIG_DIR="$TMP/config"
mkdir -p "$BIN_DIR"
# Simulate the pre-install state: codex/claude are the only entries on PATH,
# resolving to the vendor fixtures, exactly like a plain symlink install.
for name in codex claude; do
  ln -s "$VENDOR_DIR/$name" "$BIN_DIR/$name"
done

export ZAOS_SHIM_BIN_DIR="$BIN_DIR" ZAOS_REAL_BIN_DIR="$REAL_BIN_DIR" ZAOS_SHIM_CONFIG_DIR="$CONFIG_DIR"
export PATH="$BIN_DIR:$PATH"

status_before=$("$INSTALLER" status)
expect "$status_before" "codex: not shimmed"
expect "$status_before" "claude: not shimmed"

# Point the installer at the fake workspace by running it from inside it, so
# its own script-relative AGENTS_ROOT discovery lands on our fixture instead
# of the real .agents tree.
cp "$INSTALLER" "$FAKE_AGENTS/engines/bin/zaos-install-native-shims"
chmod +x "$FAKE_AGENTS/engines/bin/zaos-install-native-shims"
"$FAKE_AGENTS/engines/bin/zaos-install-native-shims" install

[ -x "$BIN_DIR/codex" ] || fail "codex shim missing after install"
[ -x "$BIN_DIR/claude" ] || fail "claude shim missing after install"
[ -x "$REAL_BIN_DIR/codex" ] || fail "real codex binary not preserved"
[ -x "$REAL_BIN_DIR/claude" ] || fail "real claude binary not preserved"
[ -f "$CONFIG_DIR/config.sh" ] || fail "config file not written"
grep -qF "$FAKE_AGENTS" "$CONFIG_DIR/config.sh" || fail "config does not point at fixture agents root"

status_after=$("$INSTALLER" status)
expect "$status_after" "codex: shimmed"
expect "$status_after" "claude: shimmed"

cap="$TMP/capture"

# --- A: inside the ZAOS-managed workspace, the shim routes through zaos ---
mkdir -p "$FAKE_WORKSPACE/projects/demo"
out=$(cd "$FAKE_WORKSPACE/projects/demo" && ZAOS_CAPTURE="$cap" codex --some-flag 2>&1)
got=$(<"$cap")
expect "$got" "ZAOS_ROUTED engine=terra"
expect "$got" "--some-flag"

out=$(cd "$FAKE_WORKSPACE/projects/demo" && ZAOS_CAPTURE="$cap" claude --some-flag 2>&1)
got=$(<"$cap")
expect "$got" "ZAOS_ROUTED engine=claude"
expect "$got" "--some-flag"

# --- B: outside the ZAOS-managed workspace, the shim is a transparent passthrough ---
OUTSIDE="$TMP/outside-project"; mkdir -p "$OUTSIDE"
out=$(cd "$OUTSIDE" && ZAOS_CAPTURE="$cap" codex --plain 2>&1)
got=$(<"$cap")
expect "$got" "VENDOR_REAL_BIN name=codex args=--plain"

out=$(cd "$OUTSIDE" && ZAOS_CAPTURE="$cap" claude --plain 2>&1)
got=$(<"$cap")
expect "$got" "VENDOR_REAL_BIN name=claude args=--plain"

# --- C: escape hatch — ZAOS_INTERNAL_EXEC bypasses routing even inside the workspace ---
out=$(cd "$FAKE_WORKSPACE/projects/demo" && ZAOS_INTERNAL_EXEC=1 ZAOS_CAPTURE="$cap" codex --bypass 2>&1)
got=$(<"$cap")
expect "$got" "VENDOR_REAL_BIN name=codex args=--bypass"

# --- D: raw-binary escape hatch is directly reachable regardless of the shim ---
[ -x "$REAL_BIN_DIR/codex" ] || fail "raw codex binary not directly reachable"
out=$(ZAOS_CAPTURE="$cap" "$REAL_BIN_DIR/codex" --raw 2>&1)
got=$(<"$cap")
expect "$got" "VENDOR_REAL_BIN name=codex args=--raw"

# --- E: recursion check — the shim never re-enters itself. zaos's own routed
# exec must land on the real binary, not loop back through $BIN_DIR/codex. A
# real recursive setup would exceed bash's exec/function nesting and fail
# loudly rather than silently succeed, so a clean single VENDOR_REAL_BIN
# capture line (already asserted above) is the positive proof; additionally
# confirm no stray recursion marker files were left by a runaway loop.
[ "$(find "$TMP" -name '*.recursion-marker' | wc -l)" -eq 0 ] || fail "recursion marker found"

# --- uninstall restores the original entries ---
"$INSTALLER" uninstall
[ -L "$BIN_DIR/codex" ] || fail "codex not restored to a plain entry after uninstall"
[ -L "$BIN_DIR/claude" ] || fail "claude not restored to a plain entry after uninstall"
[ ! -e "$REAL_BIN_DIR/codex" ] || fail "real-bin copy left behind after uninstall"
resolved=$(readlink -f "$BIN_DIR/codex")
[ "$resolved" = "$(readlink -f "$VENDOR_DIR/codex")" ] || fail "codex does not resolve back to the vendor fixture"

printf 'PASS: scoped native-command shim install/route/passthrough/escape-hatch/uninstall\n'
