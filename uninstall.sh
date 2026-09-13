#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd -P)
"$ROOT/engines/bin/zaos-install-native-shims" uninstall
echo 'PASS: ZAOS native shims removed; vendor entries restored where ZAOS owned them. Framework and projects were not touched.'
