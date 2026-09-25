# Project state

Last meaningful update: independent red-team review of the approved development direction completed (`RSK-0003`, `PROP-0005`, `SES-20260925-006`); diagnostic outcome B (proceed to concept stress test with required modifications) recommended and now awaiting owner review. Earlier: human-approved development direction (`DEC-0013`–`DEC-0017`), Research Sprint 001 metadata corrections (`FIX-0002`, `FIX-0003`), and CONTEXT_PACK metadata clarification (`FIX-0004`, `SES-20260925-005`). Historical research and Show Bible v0.1 proposal remain preserved as originally recorded.

## Objective and phase

Build original, highly rewatchable children's entertainment with durable character/IP value and AI-assisted internal production. AI is not the public brand. Phase: **FOUNDATION / PRE-PRODUCTION development**. Milestone: owner decisions integrated; independent red-team review of Pip + Nimbus complete and awaiting owner review (`PROP-0005`); concept stress testing not yet authorized. **Final Canon v1.0 is blocked.** Production is not authorized.

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

## Final canon status

**NOT APPROVED / BLOCKED.** The approved development direction authorizes continued development and red-team testing only. Independent red-team review 001 is now complete (`03_research/RED_TEAM/INDEPENDENT_RED_TEAM_001.md`); concept stress testing must still precede any final Canon v1.0 decision (`DEC-0017`). Final character design, finished episodes, and production have no approval. The Show Bible v0.1 file remains a historical **proposal**, not a final canon document.

## Provisional creative direction

The following remain **PROVISIONAL** or open for later owner decisions: final character identities and visual designs, world and premise specifics, final power system, episode canon, pilot requirements, and production approach. The Research Sprint 001 recommendations remain evidence and test hypotheses; owner approval of a development direction does not validate audience preference, comprehension, runtime optimality, commercial demand, originality, or production feasibility (`RES-0004`–`RES-0006`, `RSK-0002`). The red-team review's recommendations (`PROP-0005`) are likewise proposals, not decisions.

## Technical architecture, agents, tools

GitHub source, Markdown source hierarchy, append-only ledger, machine-readable episode manifest template, Python validators/export, CI, and optional Git hook. Agent roles are specifications only; **active agents: none configured**. Codex, Claude Code, Kimi Code, Figma, MCP, video/audio tools, FFmpeg, Remotion, Blender, and ComfyUI are candidates or potential integrations, not installed project dependencies. Video generation: **BENCHMARK REQUIRED**. Future CONTEXT_PACK headers clarify that `Source commit` is the checkout HEAD at export time and can precede the pack's containing commit (`FIX-0004`).

## Open questions and risks

- Independent red-team review 001 is complete (`RSK-0003`, `PROP-0005`, `SES-20260925-006`); concept stress testing has not yet occurred and awaits the owner decision on `PROP-0005`. Final Canon v1.0, final character design, finished episodes, and production remain blocked (`DEC-0017`).
- Direct child/caregiver tests, global market demand, originality/legal clearance, AI production yield and economics remain `TO_VERIFY` (`RES-0004`–`RES-0006`, `RSK-0002`).
- Low-dialogue comprehension, weather power inflation, repetitive helper-error plots, safety, and balanced Pip/Nimbus agency remain live stress-test risks (`RSK-0002`, `DEC-0016`). Red-team review 001 added: missing ownable hook, Pip/Nimbus definitional asymmetry, absent character comedy engine, decorative-power and single-mechanism formula risks, near-worst-case production continuity stack, economic dependency coupling, and occupied cloud-character/name space (`RSK-0003`).
- Remote `main` push and repository-validation CI were verified (`RES-0002`). Repository-validation and ledger-integrity GitHub Actions both passed on the first ledger-changing push (`RES-0003`); each later change still requires its own checks.
- Research Sprint 001 ledger entries `RES-0004`–`RES-0006`, `PROP-0004`, `RSK-0002`, and `SES-20260925-004` retain historical metadata but are interpreted with Kimi Code execution provenance and the canonical `Europe/Istanbul` timezone (`FIX-0002`, `FIX-0003`).

## Next approved actions and blocks

**OWNER REVIEW OF INDEPENDENT RED-TEAM REVIEW 001.** The independent red-team review required by `DEC-0017` is complete (`03_research/RED_TEAM/INDEPENDENT_RED_TEAM_001.md`, `03_research/RED_TEAM/FAILURE_MODE_REGISTER_001.md`, `RSK-0003`, `PROP-0005`) and recommends diagnostic outcome B — proceed to concept stress testing with required modifications. Concept stress testing is the following action, only after the owner decides on `PROP-0005`; do not begin the 100-premise stress test, full scripts, character artwork, pilot production, renderer selection, publishing, or purchases without the applicable owner gate. Sensitive proposals require `SENSITIVE_CONTENT_REVIEW_REQUIRED` and an explicit owner decision.
