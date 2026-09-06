import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "litqa.py"
SPEC = importlib.util.spec_from_file_location("litqa", SCRIPT)
litqa = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(litqa)


def test_prompt_numbers_each_excerpt():
    prompt = litqa._prompt("What happened?", [
        {"file": "one.md", "page": 1, "text": "one"},
        {"file": "two.md", "page": 2, "text": "two"},
    ])
    assert "[E1] (file: one.md, page 1)" in prompt
    assert "[E2] (file: two.md, page 2)" in prompt


def test_ground_check_rejects_missing_or_unknown_citations():
    assert litqa.ground_check("A supported sentence. [E1]", [{}, {}]) == (True, [])
    assert litqa.ground_check("A sentence.", [{}, {}])[0] is False
    assert litqa.ground_check("A sentence. [E3]", [{}, {}])[0] is False


def test_synth_dispatches_to_opt_in_codex_backend():
    original_claude, original_codex = litqa.synth_claude, litqa.synth_codex
    try:
        litqa.synth_claude = lambda *_: {"synthesizer": "claude"}
        litqa.synth_codex = lambda *_: {"synthesizer": "codex"}
        hits = [{"file": "one.md", "page": 1, "text": "evidence"}]
        assert litqa.synth("Q", hits, 1, 0.01, "claude")["synthesizer"] == "claude"
        assert litqa.synth("Q", hits, 1, 0.01, "codex")["synthesizer"] == "codex"
    finally:
        litqa.synth_claude, litqa.synth_codex = original_claude, original_codex
