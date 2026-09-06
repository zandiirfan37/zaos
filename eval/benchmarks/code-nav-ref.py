# /// script
# requires-python = ">=3.11"
# dependencies = ["jedi>=0.19"]
# ///
"""code-nav-ref — tournament arm B1 reference implementation. NOT an adopted ZAOS
capability (see code-intel.md: baseline was sufficient). Kept as the technique to
reach for during deliberate heavy impact-analysis: import-resolved Python
navigation via jedi (no server, no index).

    uv run .agents/eval/benchmarks/code-nav-ref.py <root> <op> ...

ops:
  def   <symbol> [--hint file.py]      where a symbol is defined
  refs  <file.py> <symbol>             every real reference, grouped by file (import-resolved)
  callers <file.py> <symbol>           refs, minus the definition and pure re-exports
  imports <module.py>                  what this module imports (internal first)
  usedby <module.py>                   which project files import this module
  symbols <file.py>                    top-level defs/classes with line numbers

Output is compact text + a trailing one-line summary. It reflects the code on
disk right now — there is no cache to go stale.
"""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


def _proj(root: str):
    import jedi
    r = Path(root).resolve()
    sp = [str(r / "src")] if (r / "src").is_dir() else []
    return jedi.Project(str(r), added_sys_path=sp), r


def _rel(p, root: Path) -> str:
    try:
        return str(Path(p).resolve().relative_to(root))
    except ValueError:
        return str(p)


def _find_def_line(path: Path, symbol: str) -> tuple[int, int] | None:
    for i, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
        m = re.search(rf"\b(def|class)\s+{re.escape(symbol)}\b", line)
        if m:
            return i, line.index(symbol) + 1
    return None


def op_def(root, args):
    import jedi
    proj, r = _proj(root)
    sym = args[0]
    hint = None
    if "--hint" in args:
        hint = args[args.index("--hint") + 1]
    candidates = [Path(root) / hint] if hint else list((r).rglob("*.py"))
    for f in candidates:
        if "site-packages" in str(f):
            continue
        loc = _find_def_line(f, sym)
        if loc:
            s = jedi.Script(path=str(f), project=proj)
            for d in s.infer(line=loc[0], column=loc[1]):
                print(f"{_rel(f, r)}:{loc[0]}  {d.description}")
                return 0
            print(f"{_rel(f, r)}:{loc[0]}  def/class {sym}")
            return 0
    print(f"no definition of {sym} found")
    return 1


def _refs(root, file, sym):
    import jedi
    proj, r = _proj(root)
    p = Path(root) / file if not Path(file).is_absolute() else Path(file)
    loc = _find_def_line(p, sym)
    if not loc:
        sys.exit(f"no def/class {sym} in {file}")
    refs = jedi.Script(path=str(p), project=proj).get_references(
        line=loc[0], column=loc[1], include_builtins=False)
    byfile: dict[str, list[int]] = {}
    for ref in refs:
        if not ref.module_path or "site-packages" in str(ref.module_path):
            continue
        byfile.setdefault(_rel(ref.module_path, r), []).append(ref.line)
    return byfile, _rel(p, r), loc[0], r


def op_refs(root, args):
    byfile, defrel, defline, _ = _refs(root, args[0], args[1])
    for k in sorted(byfile):
        print(f"{k}: {sorted(set(byfile[k]))}")
    print(f"\n{len(byfile)} files, {sum(len(set(v)) for v in byfile.values())} references "
          f"(def at {defrel}:{defline})")
    return 0


def op_callers(root, args):
    byfile, defrel, defline, r = _refs(root, args[0], args[1])
    sym = args[1]
    out = {}
    for k, lines in byfile.items():
        real = []
        for ln in sorted(set(lines)):
            try:
                txt = (r / k).read_text(errors="replace").splitlines()[ln - 1]
            except (IndexError, OSError):
                real.append(ln); continue
            if re.match(rf"\s*(from|import)\b", txt) or re.search(rf'["\']{sym}["\']', txt):
                continue  # import line or a re-export string (e.g. __all__)
            if k == defrel and ln == defline:
                continue
            real.append(ln)
        if real:
            out[k] = real
    for k in sorted(out):
        print(f"{k}: {out[k]}")
    print(f"\n{len(out)} files call {sym}")
    return 0


def _module_imports(path: Path) -> tuple[list[str], list[str]]:
    tree = ast.parse(path.read_text(errors="replace"))
    internal, external = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            (internal if node.module.split(".")[0] in ("gradtime", "gradtime_ops", "app")
             else external).append(node.module)
        elif isinstance(node, ast.Import):
            for n in node.names:
                (internal if n.name.split(".")[0] in ("gradtime", "gradtime_ops", "app")
                 else external).append(n.name)
    return sorted(set(internal)), sorted(set(external))


def op_imports(root, args):
    p = Path(root) / args[0] if not Path(args[0]).is_absolute() else Path(args[0])
    internal, external = _module_imports(p)
    print("internal:")
    for m in internal:
        print(f"  {m}")
    print("external:", ", ".join(external))
    print(f"\n{len(internal)} internal, {len(external)} external imports")
    return 0


def op_usedby(root, args):
    _, r = _proj(root)
    target = args[0].replace("/", ".").removesuffix(".py").removeprefix("src.")
    tail = target.split(".")[-1]
    hits = []
    for f in r.rglob("*.py"):
        if "site-packages" in str(f):
            continue
        txt = f.read_text(errors="replace")
        if re.search(rf"\b(from|import)\s+[\w.]*\b{re.escape(tail)}\b", txt):
            hits.append(_rel(f, r))
    for h in sorted(set(hits)):
        print(h)
    print(f"\n{len(set(hits))} files import {tail}")
    return 0


def op_symbols(root, args):
    p = Path(root) / args[0] if not Path(args[0]).is_absolute() else Path(args[0])
    tree = ast.parse(p.read_text(errors="replace"))
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            kind = "class" if isinstance(node, ast.ClassDef) else "def"
            print(f"{node.lineno}: {kind} {node.name}")
    return 0


OPS = {"def": op_def, "refs": op_refs, "callers": op_callers, "imports": op_imports,
       "usedby": op_usedby, "symbols": op_symbols}


def main() -> int:
    if len(sys.argv) < 3 or sys.argv[2] not in OPS:
        sys.exit(__doc__)
    root, op = sys.argv[1], sys.argv[2]
    if not Path(root).is_dir():
        sys.exit(f"not a directory: {root}")
    return OPS[op](root, sys.argv[3:])


if __name__ == "__main__":
    sys.exit(main())
