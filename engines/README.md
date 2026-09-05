# Engine adapters

Codex and Claude execution state lives in `.runtime/engines/`.

`.agents/engines/` is reserved for future human-authored adapters or
instructions. Do not copy configuration, runtime, session, or cache state
here. Do not create Codex or Claude subfolders until an authored adapter is
needed.
