# Kids Studio

Foundation for an original, AI-assisted children's animated media/IP project. The authoritative project is the private GitHub repository `taher-krf/kids-studio`. No episodes, characters, visual designs, or production tools are approved by this bootstrap.

Start with [PROJECT_STATE.md](PROJECT_STATE.md), then [AGENTS.md](AGENTS.md). Historical reasoning is preserved in [PROJECT_LEDGER.md](PROJECT_LEDGER.md). The next phase is a human-reviewed Show Bible v0.1.

## Source hierarchy

1. `PROJECT_LEDGER.md`: immutable historical record; corrections are new entries.
2. `PROJECT_STATE.md`: operational current state, with every meaningful change tied to a ledger entry.
3. Show Bible and canon documents: detailed current creative rules.
4. Episode and production artifacts: execution records.
5. Research: supporting evidence, with provenance and uncertainty.

If documents conflict, the current approved decision in `PROJECT_STATE.md` governs operations; preserve old ledger text and append a conflict entry.

## Local checks

Requires Python 3.10+ and Git. Run `python scripts/validate_repository.py` and `python -m unittest discover -s tests -v`. To enable the optional local safeguard: `git config core.hooksPath .githooks`. CI independently enforces ledger prefix integrity against the prior commit/PR base. Create a context export with `python scripts/export_context_pack.py`.
