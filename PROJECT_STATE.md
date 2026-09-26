# Project state

Last meaningful update: owner-authorized creative development phase (`DEC-0018`) produced the Show Bible v0.2 development draft, a ten-concept pilot shortlist with three selected development pilots, a Visual Bible brief, a production benchmark brief, and a desk-level name screen (`PROP-0007`, `RES-0008`, `RSK-0005`, `SES-20260926-002`); all await owner review. Earlier: concept durability stress test (`RES-0007`, `RSK-0004`, `PROP-0006`), independent red-team review (`RSK-0003`, `PROP-0005`), human-approved development direction (`DEC-0013`–`DEC-0017`), and Research Sprint 001. Historical research and proposals remain preserved as originally recorded.

## Objective and phase

Build original, highly rewatchable children's entertainment with durable character/IP value and AI-assisted internal production. AI is not the public brand. Phase: **FOUNDATION / PRE-PRODUCTION creative development** (`DEC-0018`: priority is now making a fun children's show, not further research). Milestone: Show Bible v0.2 development draft complete and awaiting owner review (`PROP-0007`). **Final Canon v1.0 is blocked.** Production is not authorized.

## Approved operational decisions

- GitHub `https://github.com/taher-krf/kids-studio.git` is the canonical repository (`DEC-0001`).
- `PROJECT_LEDGER.md` is append-only history; corrections and supersessions are new entries (`DEC-0002`, `DEC-0003`).
- This file describes current state; changes require ledger entries (`DEC-0004`).
- Human approval governs canon changes; agents may propose only (`DEC-0005`).
- Foundation phase and no premature production lock (`DEC-0006`).
- Childhood-first editorial and sensitive-content escalation policy (`DEC-0008`).
- Python standard-library validation and export scripts; no paid or external production service added (`DEC-0009`).
- Local workspaces are temporary execution copies; no session is complete until changes are validated, committed, pushed to `origin/main`, and remotely verified (`DEC-0012`, `AGT-0001`).
- Canonical human project timezone: `Europe/Istanbul (UTC+03:00)` (`FIX-0003`).

## Approved development direction

These are **HUMAN-APPROVED DEVELOPMENT DECISIONS**, not final Canon v1.0 (`DEC-0013`–`DEC-0017`).

- Core target audience: ages 4–6; accessibility envelope: approximately ages 3–7 (`DEC-0013`).
- Primary concept for continued development: Pip + Nimbus. Initial core cast: two primary characters. Fix-It and Lumina remain in project history but are paused (`DEC-0014`).
- Format: visual-first storytelling with sparse speech where needed for comprehension; silence is not mandatory. Pilot runtime target: approximately 5–7 minutes (`DEC-0013`).
- Primary comedy/story approach: clear cause and effect, anticipation, escalation, adaptation/repair, and satisfying resolution (`DEC-0015`).
- Educational and social value stays implicit within entertainment, without preachy instruction. Pacing varies while remaining readable; it is neither permanently slow nor intentionally hyperstimulating (`DEC-0015`).
- Nimbus's **INITIAL development-test abilities** are limited to mild rain and mild wind. Powers never automatically solve the story (`DEC-0016`).
- Either Pip or Nimbus may initiate the problem. Pip is not always the intelligent correct character; Nimbus is not always the foolish troublemaker (`DEC-0016`).
- Creative development phase authorized: Show Bible v0.2 drafting, pilot concept shortlist (no scripts), Visual Bible brief (no artwork), production benchmark brief (no tool selection or execution), and name development with targeted checks. "Pip" and "Nimbus" are historical working names that should probably be replaced. Stress-test lessons are to be applied at the agent's creative judgment; `PROP-0006` repair items were neither formally adopted nor rejected (`DEC-0018`).

## Final canon status

**NOT APPROVED / BLOCKED.** The approved development direction authorizes continued development only (`DEC-0017`, `DEC-0018`). Final character design, finished episodes, and production have no approval. The current creative working draft is the **Show Bible v0.2 development draft** (`01_show_bible/SHOW_BIBLE_V0.2_DEVELOPMENT.md`, `PROP-0007`) — a **proposal**, not canon. The Show Bible v0.1 file, the red-team recommendations (`PROP-0005`), and the stress-test development hypotheses and repairs (`PROP-0006`, `03_research/STRESS_TEST_001/`) remain historical **proposals**.

## Provisional creative direction

The following remain **PROVISIONAL** or open for later owner decisions: final character identities, names and visual designs, world and premise specifics, final power and expressive-weather rules, episode canon, pilot selection, and production approach.

Current development proposal (`PROP-0007`, not canon): premise "One friend can't hide a single feeling. The other won't show one." Working names **Mulu** (a small soft-solid cloud whose feelings leak as mild rain and wind; replaces Nimbus) and **Tekla** (a small armored builder who hides every feeling behind "I'm fine", straightens things, builds what she can't say, and curls into a ball when overwhelmed; replaces Pip). Viewer promise: the audience reads both characters' feelings before they do. Proposed eight expressive-weather rules inside the mild rain/wind bound (`DEC-0016`), a compact reusable Hilltop world with wordless non-characters (the Snail, Somebody Downstream, the Heron), rituals (Forecast Board, Snail Check, Keep Shelf), resolution-diversity slate rules, production-aware creative rules, and three selected development pilots: "A Chair for Mulu", "Perfectly Fine", "The Secret Drip" (`04_episodes/PILOT_CANDIDATES_V0.2.md`). Name shortlist from a desk screen (`RES-0008`, `03_research/NAME_SCREEN_002.md`): recommended working pair "Mulu & Tekla"; alternates Teko, Tiko, Nubo — not legal clearance.

Research Sprint 001 recommendations remain evidence and test hypotheses; no development decision validates audience preference, comprehension, runtime optimality, commercial demand, originality, or production feasibility (`RES-0004`–`RES-0006`, `RSK-0002`).

## Technical architecture, agents, tools

GitHub source, Markdown source hierarchy, append-only ledger, machine-readable episode manifest template, Python validators/export, CI, and optional Git hook. Agent roles are specifications only; **active agents: none configured**. Codex, Claude Code, Kimi Code, Figma, MCP, video/audio tools, FFmpeg, Remotion, Blender, and ComfyUI are candidates or potential integrations, not installed project dependencies. Video generation: **BENCHMARK REQUIRED**. Future CONTEXT_PACK headers clarify that `Source commit` is the checkout HEAD at export time and can precede the pack's containing commit (`FIX-0004`).

## Open questions and risks

- Show Bible v0.2 development draft, pilot shortlist, Visual Bible brief, and production benchmark brief await owner review (`PROP-0007`, `SES-20260926-002`); the owner decisions needed are listed in the draft's section 25. Final Canon v1.0, final character design, finished episodes, and production remain blocked (`DEC-0017`).
- v0.2 risks (`RSK-0005`): whether 4-year-olds read Tekla's hidden feelings from behavior alone; weather-code/tell overload; the soft-solid cloud and discrete-rain design bet; warmth of a deadpan lead; names desk-screened only; capacity-cost and sleep-drizzle rules await ruling.
- Direct child/caregiver tests, global market demand, originality/legal clearance, AI production yield and economics remain `TO_VERIFY` (`RES-0004`–`RES-0006`, `RSK-0002`).
- Low-dialogue comprehension, weather power inflation, repetitive helper-error plots, safety, and balanced Pip/Nimbus agency remain live development risks (`RSK-0002`, `DEC-0016`). Red-team review 001 added: missing ownable hook, Pip/Nimbus definitional asymmetry, absent character comedy engine, decorative-power and single-mechanism formula risks, near-worst-case production continuity stack, economic dependency coupling, and occupied cloud-character/name space (`RSK-0003`). Stress test 001 added: durability conditional on the proposed development hypotheses (naive baseline collapses without them), resolution-monoculture risk (64% understanding+reframe endings), quality-cost coupling (the most ownable premises are HIGH/EXTREME burden), expressive-trigger scope question (unconscious/involuntary leaks vs `DEC-0016`), and a desk-level name-pair collision for "Pip and Nimbus" (`RSK-0004`).
- Remote `main` push and repository-validation CI were verified (`RES-0002`). Repository-validation and ledger-integrity GitHub Actions both passed on the first ledger-changing push (`RES-0003`); each later change still requires its own checks.
- Research Sprint 001 ledger entries `RES-0004`–`RES-0006`, `PROP-0004`, `RSK-0002`, and `SES-20260925-004` retain historical metadata but are interpreted with Kimi Code execution provenance and the canonical `Europe/Istanbul` timezone (`FIX-0002`, `FIX-0003`).

## Next approved actions and blocks

**OWNER REVIEW OF SHOW BIBLE v0.2 DEVELOPMENT DRAFT (`PROP-0007`).** Decisions needed: working names and series title; Tekla's species and both leads' sex/pronouns; the eight expressive-weather rules (including the trigger-scope ruling from `RSK-0004`); capacity cost; soft-solid cloud style; dialogue budget; supporting-character bench; selection of the three development pilots. **Recommended next action after review:** Visual Bible exploration (brief ready: `05_visual_system/VISUAL_BIBLE_BRIEF_V0.2.md`) in parallel with beat sheets for the three pilots, followed by an owner-authorized run of the weighted production benchmark (brief ready: `06_production/PRODUCTION_BENCHMARK_BRIEF_V0.2.md`) before any visual lock. Still gated: Final Canon v1.0, the T1–T10 child/caregiver battery before canon (`PROP-0006`), full scripts, final artwork, benchmark execution, renderer selection, publishing, and purchases — each requires its applicable owner decision. Sensitive proposals require `SENSITIVE_CONTENT_REVIEW_REQUIRED` and an explicit owner decision.
