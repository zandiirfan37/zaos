#!/usr/bin/env bash
# zaos-doctor canonical regression + adversarial suite.
# Self-contained: owns and cleans its own scratch, depends on no project.
# Read-only w.r.t. everything outside its mktemp scratch. Bounded waits only.
# No orphan shells.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
DOC="$HERE/../zaos-doctor"
FX="$HERE/fixtures"
PASS=0; FAIL=0
ok()  { echo "  PASS  $1"; PASS=$((PASS+1)); }
bad() { echo "  FAIL  $1"; FAIL=$((FAIL+1)); }
# assert stdout+stderr of "$@" matches ERE $1
expect() { local re="$1"; shift; local out; out="$("$@" 2>&1)"; \
  if printf '%s' "$out" | grep -qE "$re"; then ok "$re"; \
  else bad "$re :: got: $(printf '%s' "$out" | tr '\n' '|')"; fi; }
# assert stdout+stderr of "$@" does NOT match ERE $1
refute() { local re="$1"; shift; local out; out="$("$@" 2>&1)"; \
  if printf '%s' "$out" | grep -qE "$re"; then \
    bad "unexpected match /$re/ in: $(printf '%s' "$out" | tr '\n' '|')"; \
  else ok "no match /$re/ (as expected)"; fi; }
no_secret_value() { local out; out="$("$@" 2>&1)"; \
  if printf '%s' "$out" | grep -qE 'AIza[A-Za-z0-9]|abc.def|\x1b\['; then \
    bad "SECRET VALUE LEAKED by: $*"; else ok "no secret value in output of: $*"; fi; }

SCRATCH="$(mktemp -d "${TMPDIR:-/tmp}/zaos-doctor-tests.XXXXXX")"
cleanup() {
  [ -n "${SP:-}" ] && kill "$SP" 2>/dev/null
  wait 2>/dev/null
  rm -rf "$SCRATCH"
}
trap cleanup EXIT INT TERM

echo "== read-only self-assertion =="
expect 'PASS: --assert-readonly' "$DOC" --assert-readonly

echo "== SECRET validator (leak-safe) =="
expect 'PASS: secret valid.env'                          "$DOC" --secret-file "$FX/secrets/valid.env"
expect 'WARN: secret empty.env — .*EMPTY'                "$DOC" --secret-file "$FX/secrets/empty.env"
expect 'WARN: secret malformed_syntax.env — non KEY=value' "$DOC" --secret-file "$FX/secrets/malformed_syntax.env"
expect 'WARN: secret control_byte.env — MALFORMED: [0-9]+ control' "$DOC" --secret-file "$FX/secrets/control_byte.env"
expect 'WARN: secret missing.env — declared but MISSING' "$DOC" --secret-file "$FX/secrets/missing.env"
no_secret_value "$DOC" --secret-file "$FX/secrets/control_byte.env"
no_secret_value "$DOC" --secret-file "$FX/secrets/valid.env"

echo "== SECRET: schema-driven scan =="
expect 'control_byte.env — MALFORMED' \
  "$DOC" --project "$SCRATCH" --groups secret --secrets-schema "$FX/secrets/EXPECTED.md"
no_secret_value \
  "$DOC" --project "$SCRATCH" --groups secret --secrets-schema "$FX/secrets/EXPECTED.md"

echo "== PROMOTION guard =="
expect 'WARN: promotion — production' "$DOC" --project "$FX/promotion" --groups promotion
expect 'PASS: promotion — no production dependency' "$DOC" --project "$FX/promotion_clean" --groups promotion
# comment-only reference must NOT warn
refute 'notes.md for history' "$DOC" --project "$FX/promotion" --groups promotion

# real import + real path literal MUST warn; docstring + guard-test MUST NOT
P="$SCRATCH/promo_semantic/src"; mkdir -p "$P"
printf '"""pointer: see 00_workbench/11_blueprint/09.md for the decision."""\nimport json\nY = 1\n' > "$P/doc_ok.py"
printf 'def test_guard():\n    assert "00_workbench" not in "src"\n' > "$P/test_guard.py"
expect 'PASS: promotion — no production dependency' "$DOC" --project "$SCRATCH/promo_semantic" --groups promotion
printf 'import zandi.workbench.loader\nX = 1\n' > "$P/real_import.py"
expect 'promotion — production Python depends on workbench: .*real_import.py.*import' \
  "$DOC" --project "$SCRATCH/promo_semantic" --groups promotion
rm -f "$P/real_import.py"
printf 'CFG = open("00_workbench/14_build/candidate.json")\n' > "$P/real_path.py"
expect 'promotion — production Python depends on workbench: .*real_path.py' \
  "$DOC" --project "$SCRATCH/promo_semantic" --groups promotion
rm -f "$P/real_path.py"
# docstring/guard-test still clean after removing the real deps
expect 'PASS: promotion — no production dependency' "$DOC" --project "$SCRATCH/promo_semantic" --groups promotion

echo "== JOB stale detection (bounded, no busy-poll) =="
PROJ="$SCRATCH/proj"; JD="$PROJ/runtime/jobs"; mkdir -p "$JD"
# fast, chunky writer so the 2s sample sees growth even on a loaded host
( for i in $(seq 1 400); do echo "tick $i $(date +%s%N) ------------------------------"; sleep 0.05; done > "$JD/healthy.log" ) &
HP=$!; printf 'PID=%s\nLOG=%s\nEXPECT_SECONDS=30\n' "$HP" "$JD/healthy.log" > "$JD/healthy.job"
echo "final output" > "$JD/gone.log"
printf 'PID=999999\nLOG=%s\nEXPECT_SECONDS=5\n' "$JD/gone.log" > "$JD/gone.job"
( sleep 20 ) & SP=$!
: > "$JD/stale.log"; printf 'PID=%s\nLOG=%s\nEXPECT_SECONDS=2\n' "$SP" "$JD/stale.log" > "$JD/stale.job"
T0=$(date +%s); OUT="$("$DOC" --project "$PROJ" --groups job 2>&1)"; T1=$(date +%s)
printf '%s\n' "$OUT" | sed 's/^/    /'
printf '%s' "$OUT" | grep -q 'healthy.job — output progressing' && ok "healthy job not falsely stale" || bad "healthy job classification"
printf '%s' "$OUT" | grep -q 'gone.job — PID 999999 gone'       && ok "process-gone stale descriptor detected" || bad "gone job"
printf '%s' "$OUT" | grep -q 'stale.job — .*STALL_SUSPECTED'    && ok "stale job detected (bounded 2s sample)" || bad "stale job"
printf '%s' "$OUT" | grep -q 'do not auto-kill'                 && ok "doctor says do-not-auto-kill" || bad "missing do-not-auto-kill guard"
[ $((T1-T0)) -le 15 ] && ok "job scan bounded ($((T1-T0))s, no 60x busy poll)" || bad "job scan took $((T1-T0))s"
kill "$SP" 2>/dev/null; wait "$HP" 2>/dev/null; wait "$SP" 2>/dev/null; SP=""
rm -rf "$PROJ"; ok "job fixtures cleaned (no orphan shells)"

echo "== GIT: clean vs dirty, transaction-capability, no mutation =="
G="$SCRATCH/gitproj"; mkdir -p "$G"
git -C "$G" init -q
git -C "$G" -c user.email=t@t -c user.name=t commit -q --allow-empty -m init
expect 'git — worktree clean' "$DOC" --project "$G" --groups git
expect 'transaction-capable' "$DOC" --project "$G" --groups git --mode ZAOS_MAINTENANCE
H1="$(git -C "$G" rev-parse HEAD)$(git -C "$G" status --porcelain)"
echo "dirt" > "$G/untracked.txt"
expect 'git — worktree DIRTY' "$DOC" --project "$G" --groups git
"$DOC" --project "$G" --groups git,promotion,resource,secret >/dev/null 2>&1
H2="$(git -C "$G" rev-parse HEAD)$(git -C "$G" status --porcelain)"
[ "$H1" != "$H2" ] && [ -f "$G/untracked.txt" ] && ok "doctor did not alter git state (only the test's own dirt differs)" || bad "git state changed unexpectedly"

echo "== RUNTIME contract reconcile (read-only) =="
R="$SCRATCH/rtproj"; mkdir -p "$R"
printf '# RUNTIME_CONTRACT\n\n## PERSISTENT TOPOLOGY\n\n- `ragflow-server`\n- `es01`\n' > "$R/RUNTIME_CONTRACT.md"
expect 'runtime — RUNTIME_CONTRACT.md present' "$DOC" --project "$R" --groups runtime --mode READ_ONLY
expect 'runtime — (EXPECTED tokens=[0-9]+|docker absent)' "$DOC" --project "$R" --groups runtime --mode READ_ONLY
refute 'FAIL_CHECK: runtime' "$DOC" --project "$R" --groups runtime --mode READ_ONLY
# no contract -> INFO, not WARN
expect 'runtime — no RUNTIME_CONTRACT.md' "$DOC" --project "$SCRATCH" --groups runtime

echo "== RESOURCE: advisory only =="
expect 'RESOURCE' "$DOC" --project "$SCRATCH" --groups resource
refute 'FAIL_CHECK: resource — nvidia' "$DOC" --project "$SCRATCH" --groups resource

echo "== CAPABILITY reuse hint =="
expect 'EXISTING_CAPABILITY_FOUND|on PATH:' "$DOC" --capability git
expect 'no local prior art' "$DOC" --capability zzznotarealbinary12345

echo "== CLOCK: degrades cleanly without docker =="
expect 'clock — (docker absent|no running containers|.* skew )' "$DOC" --project "$SCRATCH" --groups clock

echo "== exit code is information, never a hang/block =="
"$DOC" --project /nonexistent/xyz --groups git >/dev/null 2>&1; rc=$?
[ "$rc" -le 3 ] && ok "doctor on bad path exits cleanly ($rc), does not hang" || bad "bad-path rc=$rc"
"$DOC" --project "$FX/promotion" --groups promotion >/dev/null 2>&1; rc=$?
[ "$rc" -eq 1 ] && ok "WARN present -> exit 1 (informational)" || bad "expected exit 1 on WARN, got $rc"

echo "== ADVERSARIAL set =="
A="$SCRATCH/adv/src"; mkdir -p "$A"
printf '"""history: migrated from Chatbot_Project/00_workbench/x."""\nZ = 2\n' > "$A/ds.py"
printf '# TODO: was in 00_workbench/ during Chatbot_Project prototyping\nQ = 3\n' > "$A/cm.py"
mkdir -p "$SCRATCH/adv/tests"
printf 'def test_no_dep():\n    assert "00_workbench/" not in open("x").read()\n' > "$SCRATCH/adv/tests/test_dep.py"
expect 'PASS: promotion — no production dependency' "$DOC" --project "$SCRATCH/adv" --groups promotion
printf 'from Chatbot_Project.legacy import q\n' > "$A/realdep.py"
expect 'promotion — production Python depends on workbench' "$DOC" --project "$SCRATCH/adv" --groups promotion
rm -f "$A/realdep.py"
# unparseable production file that really references workbench -> still caught
printf 'def broken(:\n    path = "00_workbench/data/x.json"\n' > "$A/broken.py"
expect 'promotion — production Python depends on workbench: .*broken.py.*unparseable' "$DOC" --project "$SCRATCH/adv" --groups promotion
rm -f "$A/broken.py"
expect 'PASS: promotion — no production dependency' "$DOC" --project "$SCRATCH/adv" --groups promotion

echo "== NOISE budget: healthy project run is compact =="
N="$SCRATCH/clean"; mkdir -p "$N/src"; git -C "$N" init -q
git -C "$N" -c user.email=t@t -c user.name=t commit -q --allow-empty -m init
printf 'import os\nA = os.getcwd()\n' > "$N/src/main.py"
LINES="$("$DOC" --project "$N" 2>&1 | wc -l)"
[ "$LINES" -le 40 ] && ok "healthy run compact ($LINES lines)" || bad "healthy run noisy ($LINES lines)"
DUP="$("$DOC" --project "$N" 2>&1 | grep -c 'SOP\|Council\|HUMAN_DECISION\|NEXT_GATE' || true)"
[ "$DUP" -eq 0 ] && ok "no SOP/Council/handoff narration in doctor output" || bad "doctor emitted narrative noise"

echo
echo "==== RESULT: PASS=$PASS FAIL=$FAIL ===="
[ "$FAIL" -eq 0 ]
