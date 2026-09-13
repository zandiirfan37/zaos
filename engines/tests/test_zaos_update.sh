#!/usr/bin/env bash
# Guarded fast-forward update against a disposable local canonical remote.
set -euo pipefail
ROOT=$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/../.." && pwd -P)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
git clone -q --bare "$ROOT" "$TMP/origin.git"
git clone -q "$TMP/origin.git" "$TMP/installed"
git clone -q "$TMP/origin.git" "$TMP/publisher"
git -C "$TMP/publisher" config user.email test@zaos.invalid
git -C "$TMP/publisher" config user.name 'ZAOS test'
printf '2.0.1\n' > "$TMP/publisher/VERSION"
git -C "$TMP/publisher" add VERSION
git -C "$TMP/publisher" commit -qm 'test: simulated framework release'
git -C "$TMP/publisher" push -q origin main
HOME="$TMP/home"
export HOME
mkdir -p "$HOME/.local/bin"
"$TMP/installed/engines/bin/zaos-update"
[ "$(tr -d '[:space:]' < "$TMP/installed/VERSION")" = 2.0.1 ] || { echo 'FAIL: updater did not fast-forward'; exit 1; }
printf 'dirty\n' > "$TMP/installed/.update-test-dirty"
if "$TMP/installed/engines/bin/zaos-update" >/dev/null 2>&1; then
  echo 'FAIL: updater accepted a dirty framework'
  exit 1
fi
echo 'PASS: guarded canonical fast-forward update and dirty-state refusal'
