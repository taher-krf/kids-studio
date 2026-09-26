# Changelog

## 2026-09-25 — Foundation bootstrap

Created source-of-truth documents, childhood-first editorial gate, agent and production specifications, machine-readable templates, validation scripts, CI workflows, and context export. Historical context is imported as `RES-0001`; no finished content or creative canon was approved.

## Episode scaffold correction

`create_episode.py` now appends the episode proposal ID to the master ledger and keeps its source brief reference repository-relative (`ERR-0001`, `FIX-0001`).

## 2026-09-25 — Mandatory session finalization rule

Added the mandatory end-of-session GitHub synchronization rule to `AGENTS.md` as the single canonical location; `CLAUDE.md` explicitly inherits it and `08_operations/SESSION_PROTOCOL.md` references it. Recorded as `DEC-0012` and `AGT-0001` (`SES-20260925-003`).

## 2026-09-25 — Research Sprint 001 and Show Bible v0.1 proposal

Added cited child-development, comedy, pacing, repeat-viewing, format-reference, market, competitor, platform and AI-production research; a source register and audit/red-team log; a decision synthesis with owner matrix; and a separate, explicitly non-canon Show Bible v0.1 proposal. Updated project state for owner review. Recorded `RES-0004`–`RES-0006`, `PROP-0004`, `RSK-0002`, and `SES-20260925-004`. No audience, concept, power, runtime, episode or production stack was approved.

## 2026-09-25 — Owner-approved development direction

Recorded the owner's development decisions for the 4–6 core audience, approximately 3–7 accessibility, Pip + Nimbus with two primary characters, visual-first sparse speech, approximately 5–7-minute pilot target, cause-and-effect comedy, implicit educational/social value, variable readable pacing, mild rain/wind initial tests, and balanced character agency (`DEC-0013`–`DEC-0016`). Final Canon v1.0 remains blocked pending independent red-team review and concept stress testing (`DEC-0017`). Corrected Research Sprint 001 agent and timezone provenance through new ledger entries (`FIX-0002`, `FIX-0003`), and clarified future CONTEXT_PACK `Source commit` metadata (`FIX-0004`). Historical ledger entries, proposal, and exports were not rewritten (`SES-20260925-005`).

## 2026-09-25 — Independent red-team review 001

Completed the independent red-team review of the approved development direction required by `DEC-0017`: created `03_research/RED_TEAM/INDEPENDENT_RED_TEAM_001.md` and `03_research/RED_TEAM/FAILURE_MODE_REGISTER_001.md`; recorded new open risks (`RSK-0003`) and the recommended diagnostic outcome B with required modifications (`PROP-0005`); updated project state, roadmap, risk register, and open questions (`SES-20260925-006`). No canon, creative asset, decision, or production work was approved; `DEC-0013`–`DEC-0017` unchanged; concept stress testing awaits owner review.

## 2026-09-26 — Concept durability and series-capacity stress test 001

Executed the owner-authorized concept stress test: created `03_research/STRESS_TEST_001/` (methodology, development hypotheses, analysis report, Fix-It/Lumina control sample, originality/name screen, economics note, findings and recommendation) and `scripts/stress_test_analysis.py` (stdlib validation/clustering/review/analysis). Generated 168 premise skeletons (148 hypothesis-guarded + 20 unguarded naive baseline + 20 controls), rejected 26 with coded reasons, and computed mechanism, family, formula, agency, power-necessity, comedy, and production-burden analyses. Result: 125 distinct mechanism signatures, all 33 story families, 0% F1/F3 formula concentration in the accepted pool; durability shown to be conditional on the proposed development hypotheses. Recorded `RES-0007`, `RSK-0004` (new risks incl. resolution monoculture, quality-cost coupling, name-pair collision), and `PROP-0006` (recommendation: PROCEED WITH REPAIRS); updated project state, roadmap, risk register, and open questions (`SES-20260926-001`). No canon, episode, design, or production work was approved; `DEC-0013`–`DEC-0017` unchanged; the recommendation awaits owner review.

## 2026-09-26 — Creative development: Show Bible v0.2 draft and pilot shortlist

The owner shifted priority from research to making the show (`DEC-0018`). Added the [Show Bible v0.2 development draft](01_show_bible/SHOW_BIBLE_V0.2_DEVELOPMENT.md) with its premise, "One friend can't hide a single feeling. The other won't show one." It uses the working names Mulu (cloud) and Tekla (armored builder) and covers expressive-weather rules, comedy and story engines, world, rituals, dialogue, pacing, production-aware rules and open owner decisions. Also added [pilot candidates](04_episodes/PILOT_CANDIDATES_V0.2.md) (ten concepts, three proposed development pilots), a [Visual Bible brief](05_visual_system/VISUAL_BIBLE_BRIEF_V0.2.md), a [production benchmark brief](06_production/PRODUCTION_BENCHMARK_BRIEF_V0.2.md), and a desk-level [name screen](03_research/NAME_SCREEN_002.md). Development-draft pointers were added to the provisional stubs. Recorded `DEC-0018`, `RES-0008`, `PROP-0007`, `RSK-0005`, `SES-20260926-002`. Nothing is canon. No scripts, artwork, tools, purchases or publishing. `DEC-0013`–`DEC-0017` unchanged.
