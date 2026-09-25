# Changelog

## 2026-09-25 — Foundation bootstrap

Created source-of-truth documents, childhood-first editorial gate, agent and production specifications, machine-readable templates, validation scripts, CI workflows, and context export. Historical context is imported as `RES-0001`; no finished content or creative canon was approved.

## Episode scaffold correction

`create_episode.py` now appends the episode proposal ID to the master ledger and keeps its source brief reference repository-relative (`ERR-0001`, `FIX-0001`).

## 2026-09-25 — Mandatory session finalization rule

Added the mandatory end-of-session GitHub synchronization rule to `AGENTS.md` as the single canonical location; `CLAUDE.md` explicitly inherits it and `08_operations/SESSION_PROTOCOL.md` references it. Recorded as `DEC-0012` and `AGT-0001` (`SES-20260925-003`).
