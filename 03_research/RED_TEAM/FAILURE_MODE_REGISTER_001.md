# Failure-Mode Register 001 — Pip + Nimbus independent red-team review

Status: **DIAGNOSTIC REGISTER — AWAITING OWNER REVIEW.** Companion to [INDEPENDENT_RED_TEAM_001.md](INDEPENDENT_RED_TEAM_001.md) (section references "RT §n" point there). Not canon; not an owner decision. Date: 2026-09-25 (Europe/Istanbul). Recorded in the ledger via `RSK-0003`, `PROP-0005`, `SES-20260925-006`.

**Scale (qualitative judgments, not probabilities):**
- **Likelihood:** LOW / MEDIUM / HIGH — chance the failure materializes if unmitigated, judged from current evidence.
- **Severity:** LOW / MEDIUM / HIGH / CRITICAL — impact on IP durability, safety, feasibility or economics if it occurs.
- **Detectability:** LOW / MEDIUM / HIGH — how early and reliably the failure can be detected *before* public release. HIGH = detectable early with planned tests.
- **Status:** OPEN (unmitigated), PARTIAL (some approved mitigation exists), MONITOR (external, watch only).

## Summary table

| ID | Failure mode | Likelihood | Severity | Detectability | Status |
| --- | --- | --- | --- | --- | --- |
| FM-01 | Series formula becomes visible ("help goes wrong" template) | HIGH | HIGH | HIGH | PARTIAL |
| FM-02 | Character attachment failure (indistinguishable / unloved) | MEDIUM | CRITICAL | HIGH | OPEN |
| FM-03 | Definitional asymmetry → designated-adult/toddler split | HIGH | HIGH | HIGH | PARTIAL |
| FM-04 | Powers become decorative (irrelevant to best stories) | MEDIUM | HIGH | MEDIUM | OPEN |
| FM-05 | Power inflation → arbitrary magic → stakes collapse | MEDIUM | HIGH | HIGH | PARTIAL |
| FM-06 | Cloud-body silhouette/volume drift in production | HIGH (generative-only) | HIGH | MEDIUM | OPEN |
| FM-07 | Wet/dry and weather-state continuity failures | HIGH (generative-only) | HIGH | MEDIUM | OPEN |
| FM-08 | Acting/timing quality insufficient for the comedy format | MEDIUM | CRITICAL | MEDIUM | OPEN |
| FM-09 | Similarity / brand confusion in occupied cloud-character space | MEDIUM | HIGH | MEDIUM | OPEN |
| FM-10 | Name distinctiveness failure ("Nimbus" crowded/descriptive; "Pip" generic) | HIGH | MEDIUM | HIGH | OPEN |
| FM-11 | Younger-edge (age 3) causal comprehension failure | MEDIUM | MEDIUM | HIGH | OPEN |
| FM-12 | Older-edge (6–7) boredom / rejection | MEDIUM | MEDIUM | MEDIUM | OPEN |
| FM-13 | MFK economics fail (cost exceeds plausible paths) | MEDIUM | CRITICAL | LOW–MEDIUM | OPEN |
| FM-14 | YPP inauthentic/repetitive-content classification | MEDIUM | HIGH | MEDIUM | OPEN |
| FM-15 | Uniform niceness suppresses conflict → inert or accident-only stories | MEDIUM | HIGH | MEDIUM | OPEN |
| FM-16 | Rewatch value = repetition tolerance only | MEDIUM | MEDIUM | MEDIUM | OPEN |
| FM-17 | Fear/discomfort at younger edge | LOW–MEDIUM | HIGH | HIGH | PARTIAL |
| FM-18 | Fantasy/science confusion about weather causes | LOW–MEDIUM | MEDIUM | HIGH | PARTIAL |
| FM-19 | Opportunity cost: Fix-It/Lumina never head-to-head tested | MEDIUM | MEDIUM | HIGH | OPEN |
| FM-20 | Advocacy/policy climate on AI children's content → brand/policy risk | MEDIUM | HIGH | MEDIUM | MONITOR |

## Detailed entries

### FM-01 — Series formula becomes visible ("help goes wrong" template)
- **Cause:** Atmospheric-only powers + single approved engine + escalation as default beat (RT §6–8).
- **Impact:** Caregiver fatigue; formula named within ~3–5 episodes (inference); 6–7-edge rejection; S24 template-content exposure.
- **Current evidence:** Proposal's 8 stress-test examples concentrate in one mechanism family; `RSK-0002` pre-identified interchangeability; `DEC-0016` balanced-agency rule mitigates authorship, not mechanism.
- **Likelihood:** HIGH. **Severity:** HIGH. **Detectability:** HIGH (premise mechanism coding; caregiver T6).
- **Status:** PARTIAL. **Mitigation candidate:** Mechanism-diversity scoring in premise stress test; character comedy engine (RT §24.5); vary cause-kind and resolution-kind, not props.
- **Test required:** Coded premise census; T6 caregiver formula-naming. **Decision owner:** Human owner (on stress-test evidence).

### FM-02 — Character attachment failure
- **Cause:** Trait-label definitions without contradiction, want, or fear; no behavioral signatures; characterization channel narrowed by sparse dialogue (RT §4–5, §10).
- **Impact:** No preference, no merch pull, no durability — the primary IP failure.
- **Current evidence:** Zero preference/appeal evidence in repository; definitions contain no wants/fears; T3 untested.
- **Likelihood:** MEDIUM. **Severity:** CRITICAL. **Detectability:** HIGH (T3 preference/description test).
- **Status:** OPEN. **Mitigation candidate:** Required modifications RT §24.1–24.2, §24.5 (contradictions, wants, comedy engine, behavioral signatures).
- **Test required:** T3, T5, T6. **Decision owner:** Human owner.

### FM-03 — Definitional asymmetry → designated-adult / designated-toddler split
- **Cause:** Nimbus defined by deficit + learning objective ("acts before fully understanding," "learns to listen"); Pip defined with no deficit (proposal §6–7; RT §5).
- **Impact:** Drift into the fixed competence hierarchy `DEC-0016` forbids; Pip becomes straight-man, Nimbus chaos-agent; comedy range narrows to one axis.
- **Current evidence:** Observed in the current approved-direction-adjacent proposal text (RT §5). **This failure mode is currently visible in seed form.**
- **Likelihood:** HIGH if definitions unchanged. **Severity:** HIGH. **Detectability:** HIGH (definition audit; premise authorship coding).
- **Status:** PARTIAL (DEC-0016 rule restrains, definitions pull). **Mitigation candidate:** Rebalanced definitions (RT §24.2).
- **Test required:** Premise authorship/mechanism coding in stress test; T3 distinct-words check. **Decision owner:** Human owner.

### FM-04 — Powers become decorative
- **Cause:** Instrumental (tool) power framing; atmospheric effects that modify rather than restructure problems (RT §6).
- **Impact:** Nimbus's defining trait unjustified in the strongest stories → "gimmick" verdict; identity depends on a feature the stories don't need.
- **Current evidence:** 3 of 8 proposal examples barely use powers, including the strongest ("a quiet hello").
- **Likelihood:** MEDIUM. **Severity:** HIGH. **Detectability:** MEDIUM (premise census counting power-necessary stories).
- **Status:** OPEN. **Mitigation candidate:** Expressive power philosophy (RT §24.3).
- **Test required:** Premise census ("is the power necessary here?"); T2 attribution. **Decision owner:** Human owner.

### FM-05 — Power inflation → arbitrary magic
- **Cause:** Variety pressure under FM-01/FM-04 tempts new powers; each addition dilutes stakes if not philosophy-gated.
- **Impact:** Stakes death; illegibility for 4–6s; production-continuity load multiplies.
- **Current evidence:** `RSK-0002` (weather power inflation); `POWER_RULES.md` lists unapproved candidates; `DEC-0016` bounds initial tests only.
- **Likelihood:** MEDIUM. **Severity:** HIGH. **Detectability:** HIGH (ledger/coding catches additions).
- **Status:** PARTIAL. **Mitigation candidate:** Five-property gate for any power change (RT §6); owner-only approval (existing).
- **Test required:** Script rule-audit ("could another power solve this instantly?"); T1/T2. **Decision owner:** Human owner.

### FM-06 — Cloud-body silhouette/volume drift
- **Cause:** Vapor body has no stable silhouette; generative drift hides in fluid form (RT §15).
- **Impact:** Identity inconsistency across shots/episodes; QC load; potential YPP "mass-produced generic" appearance; child recognition (T10) undermined.
- **Current evidence:** Vendor docs prove reference conditioning, not continuity (S38–S40); repo lists silhouette drift as likely failure mode.
- **Likelihood:** HIGH under generative-only; lower under hybrid. **Severity:** HIGH. **Detectability:** MEDIUM (needs benchmark; drift is gradual).
- **Status:** OPEN. **Mitigation candidate:** Fixed volume grammar in Visual Bible (RT §14.2); deterministic character layer; benchmark stressor #1.
- **Test required:** Weighted production benchmark (RT §24.6); T10. **Decision owner:** Human owner.

### FM-07 — Wet/dry and weather-state continuity failures
- **Cause:** States (wet, wind-blown, raining) must persist across shots; generative video is state-blind (RT §15).
- **Impact:** Story information corrupted (states are plot here); reshoot cost; credibility of cause/effect.
- **Current evidence:** First/last-frame controls do not guarantee in-between or cross-shot state (S38/S40).
- **Likelihood:** HIGH under generative-only. **Severity:** HIGH. **Detectability:** MEDIUM.
- **Status:** OPEN. **Mitigation candidate:** State as first-class manifest metadata; deterministic effects for state-critical shots; benchmark stressor #2.
- **Test required:** Benchmark; multi-shot continuity review. **Decision owner:** Human owner.

### FM-08 — Acting/timing quality insufficient for the comedy format
- **Cause:** Sparse-dialogue format makes subtle nonverbal acting load-bearing; generative video approximates timing and flattens reaction nuance (RT §10, §15).
- **Impact:** Comedy reads flat; emotional beats unreadable; the core promise fails even if plots are sound.
- **Current evidence:** Verified low-dialogue precedents rely on elite hand-crafted performance (S30/S31, Aardman); vendor multi-character workflows unproven for this (S43).
- **Likelihood:** MEDIUM. **Severity:** CRITICAL (format-level). **Detectability:** MEDIUM (animatic benchmark reveals it).
- **Status:** OPEN. **Mitigation candidate:** Deterministic/hybrid acting layer; acting-hold stressor in benchmark; behavioral-signature design.
- **Test required:** Benchmark (expressive silent emotion); T4/T9. **Decision owner:** Human owner.

### FM-09 — Similarity / brand confusion in occupied cloud space
- **Cause:** Anthropomorphic cloud + weather help is occupied territory; no qualitative screen yet performed.
- **Impact:** Brand confusion; originality claims indefensible; potential legal exposure if expression converges.
- **Current evidence:** [Cloudbabies](https://www.bbc.co.uk/mediacentre/mediapacks/childrens2012/cbeebies/cloudbabies/) (52×10' preschool, cloud/sky cast, [international distribution](https://www.animationmagazine.net/2013/10/cloudbabies-soar-germany/)); nimbus-cloud lead in [Middlemost Post](https://www.commonsensemedia.org/tv-reviews/middlemost-post); repo competitor matrix: "none of those components is unique." External spot-check only — not a clearance.
- **Likelihood:** MEDIUM. **Severity:** HIGH. **Detectability:** MEDIUM (screen + T10 confusion test).
- **Status:** OPEN. **Mitigation candidate:** Qualitative originality/name screen before design lock (RT §24.7); documented nearest-neighbor divergence.
- **Test required:** Screen; T10. **Decision owner:** Human owner (+ IP counsel if screen escalates).

### FM-10 — Name distinctiveness failure
- **Cause:** "Nimbus" is descriptive of the character's nature and crowded in children's media; "Pip" is a common character name.
- **Impact:** Weak brand ownership; search/SEO dilution; rename cost later > rename cost now.
- **Current evidence:** Multiple children's "Nimbus the cloud" properties (e.g. [1](https://www.youtube.com/watch?v=SeV_LOqThgg), [2](https://www.youtube.com/watch?v=6EbPoXOcowM)); Middlemost Post usage (FM-09). Names remain provisional — correct.
- **Likelihood:** HIGH (that the names stay weak). **Severity:** MEDIUM. **Detectability:** HIGH (search/screen).
- **Status:** OPEN. **Mitigation candidate:** Include names in the screen (RT §24.7); keep renaming a live owner option.
- **Test required:** Name screen; child/caregiver name-association check inside T3/T6. **Decision owner:** Human owner.

### FM-11 — Younger-edge (age 3) causal comprehension failure
- **Cause:** Multi-step causal chains exceed one-concrete-action processing (repo age table, RT §9).
- **Impact:** "3–7 accessibility" claim fails at the bottom; packaging risk if claimed early.
- **Current evidence:** [AGE_4_6_EVIDENCE.md](../CHILD_DEVELOPMENT/AGE_4_6_EVIDENCE.md) band table; S04 video-only warning.
- **Likelihood:** MEDIUM. **Severity:** MEDIUM. **Detectability:** HIGH (T1 age-stratified).
- **Status:** OPEN. **Mitigation candidate:** Treat envelope as test claim (RT §24.9); anchors at the younger edge (T7).
- **Test required:** T1, T7. **Decision owner:** Human owner.

### FM-12 — Older-edge (6–7) boredom / rejection
- **Cause:** Gentle stakes + no humor-layering mechanisms; competing attention context (gaming/short-form, S19).
- **Impact:** Envelope fails at the top; co-viewing older siblings disengage; catalog longevity narrows to the core band.
- **Current evidence:** S19; absence of layering mechanisms (RT §9, §12).
- **Likelihood:** MEDIUM. **Severity:** MEDIUM. **Detectability:** MEDIUM (T4 flat-affect; T5 at 6–7).
- **Status:** OPEN. **Mitigation candidate:** Callback/acting-detail layering (RT §12); do not chase the edge by raising peril.
- **Test required:** T4, T5, T8 at 6–7. **Decision owner:** Human owner.

### FM-13 — MFK economics fail
- **Cause:** MFK ad limits (S23), disabled funnel features (S22), high continuity-driven production cost (FM-06/07/08), no validated non-ad path.
- **Impact:** Concept cannot pay for itself at realistic yields; project ends at pilot regardless of creative quality.
- **Current evidence:** Policy research (HIGH/PRIMARY on constraints); cost side unmeasured (benchmark pending); dependency coupling (RT §16).
- **Likelihood:** MEDIUM. **Severity:** CRITICAL. **Detectability:** LOW–MEDIUM (only proxies before launch: benchmark cost + comparables).
- **Status:** OPEN. **Mitigation candidate:** Economics one-pager pre-canon (RT §24.10); hybrid-cost realism; non-ad path evidence (books/licensing research) sequenced after identity proof.
- **Test required:** Benchmark cost model; 30–50-channel comparable sample (per market doc). **Decision owner:** Human owner.

### FM-14 — YPP inauthentic / repetitive-content classification
- **Cause:** Formula-tight episodes + AI production at volume = the exact profile S24 names (mass-produced, interchangeable, template).
- **Impact:** Monetization ineligibility; YouTube Kids exclusion risk (S20 quality gates).
- **Current evidence:** S24 (HIGH/PRIMARY); repo market doc flags weak/common formats.
- **Likelihood:** MEDIUM. **Severity:** HIGH. **Detectability:** MEDIUM (policy review per batch + variation evidence trail).
- **Status:** OPEN. **Mitigation candidate:** Premise-coding variation records and human editorial authorship trail as compliance assets; compilation policy (RT §16.5).
- **Test required:** Pre-publication policy refresh + per-batch quality review (proposed launch control, policy doc). **Decision owner:** Human owner.

### FM-15 — Uniform niceness suppresses conflict
- **Cause:** "Neither is punished for being themselves" + cooperative frame + no flaws = no legitimate source of desire-based conflict (RT §5, §8, MO2).
- **Impact:** Stories inert or accident-only; emotional-conflict family forced into misunderstanding-only; instructional drift.
- **Current evidence:** Frame language in CHARACTER_RULES.md / RELATIONSHIP.md / proposal §8, §18.
- **Likelihood:** MEDIUM. **Severity:** HIGH. **Detectability:** MEDIUM (premise census: count accident-caused vs. desire-caused).
- **Status:** OPEN. **Mitigation candidate:** Contradictions/wants (RT §24.2); bounded selfishness allowed and repaired (owner-level creative decision).
- **Test required:** Premise census; T9. **Decision owner:** Human owner.

### FM-16 — Rewatch value = repetition tolerance only
- **Cause:** Second-view mechanisms (callbacks, motifs, acting detail, ritual) asserted, not built (RT §12).
- **Impact:** Rewatch becomes property-independent; no durability advantage over any competitor; S14 caveat caps comprehension gains.
- **Current evidence:** No design/audio/acting grammar exists; repo repeat-viewing doc rates voluntary-replay drivers LOW/INFERENCE.
- **Likelihood:** MEDIUM. **Severity:** MEDIUM. **Detectability:** MEDIUM (T5 unprompted replay).
- **Status:** OPEN. **Mitigation candidate:** Rewatch requirements in stress-test brief (fair callback per episode; one discoverable detail per scene; motif deliverable).
- **Test required:** T5, plus recall on viewing 1 vs 2 (repo design). **Decision owner:** Human owner.

### FM-17 — Fear / discomfort at younger edge
- **Cause:** Individual sensitivity varies (S01/S07); even mild weather can read as threat at 3; sound design can accidentally intensify.
- **Impact:** Safety failure at the exact trust boundary; caregiver rejection; policy exposure (S26) if severe.
- **Current evidence:** Mild-only bound approved (DEC-0016; proposal §11 excludes severe weather) — good mitigation in place; untested with children.
- **Likelihood:** LOW–MEDIUM. **Severity:** HIGH (safety class). **Detectability:** HIGH (T4 in every session).
- **Status:** PARTIAL. **Mitigation candidate:** Existing mild bound + fear monitoring as stop-rule (RT §18).
- **Test required:** T4 (never waived). **Decision owner:** Human owner.

### FM-18 — Fantasy/science confusion about weather
- **Cause:** Character-caused weather could be read as meteorology; fantasy/reality judgments are context-sensitive (S07).
- **Impact:** Misconception risk; undermines the implicit-education stance and caregiver trust.
- **Current evidence:** Proposal §5/§8 already separates fantasy powers from real observation — aligned; systematic rule not yet written.
- **Likelihood:** LOW–MEDIUM. **Severity:** MEDIUM. **Detectability:** HIGH (ask "how did it happen" in T2).
- **Status:** PARTIAL. **Mitigation candidate:** Systematic science-boundary rule (RT MO6); never explain powers as weather science.
- **Test required:** T2 follow-up ("does rain really work that way?"). **Decision owner:** Human owner.

### FM-19 — Opportunity cost: alternatives never head-to-head tested
- **Cause:** Fix-It (production control) and Lumina (calm parent positioning) are paused with identical LOW/INFERENCE grades; stress-test resources commit to Pip + Nimbus alone.
- **Impact:** Project may spend its test budget on the wrong horse and discover it late.
- **Current evidence:** Feasibility control table (all calls LOW/INFERENCE); `DEC-0014` pauses, not rejects, alternatives.
- **Likelihood:** MEDIUM. **Severity:** MEDIUM. **Detectability:** HIGH (build one control into the test design).
- **Status:** OPEN. **Mitigation candidate:** At least one side-by-side animatic control in the stress-test design (RT §27.6).
- **Test required:** Control animatic through T1/T5/T6. **Decision owner:** Human owner.

### FM-20 — Advocacy/policy climate on AI children's content
- **Cause:** 2026 advocacy campaigns against AI children's video (S28; AP reporting S29); policy drift possible despite current compliance.
- **Impact:** Reputational "AI slop" association regardless of quality; potential future policy tightening; platform trust friction.
- **Current evidence:** S24/S27 (current rules: no blanket AI ban; disclosure scoped to photorealistic content); S28/S29 (advocacy/reporting, not policy).
- **Likelihood:** MEDIUM (climate effects; timing unknowable). **Severity:** HIGH. **Detectability:** MEDIUM (pre-publication policy refresh; monitoring).
- **Status:** MONITOR. **Mitigation candidate:** Quality-first evidence trail; voluntary transparency consideration; policy refresh gate before any upload (already proposed).
- **Test required:** None internal; standing pre-launch policy review. **Decision owner:** Human owner.

---

*End of Failure-Mode Register 001. All ratings are qualitative reviewer judgments on desk evidence; none is a measured probability. No failure mode is currently observed as having occurred; FM-03 is observed in seed form at the definition level. Historical ledger bytes untouched; register recorded via RSK-0003 / PROP-0005 / SES-20260925-006.*
