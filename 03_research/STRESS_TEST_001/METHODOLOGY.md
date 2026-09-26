# Stress Test 001 — Methodology

Status: **DEVELOPMENT / STRESS-TEST MATERIAL — NOT CANON.** Authorized by the human owner task "CONCEPT DURABILITY & SERIES CAPACITY STRESS TEST" (2026-09-25, Europe/Istanbul). This document defines the method; nothing here approves canon, episodes, designs, names, or production. Companion artifacts in this directory are listed in [README.md](README.md).

## 1. Question under test

Can the approved Pip + Nimbus development direction (`DEC-0013`–`DEC-0017`) sustain a distinctive, rewatchable, non-formulaic children's series over a large episode catalog? The stance is **falsification**: the test is designed to break the concept, not to confirm it. A strong result is evidence; a weak result is also a deliverable.

Kill/revise criteria are inherited from `03_research/RED_TEAM/INDEPENDENT_RED_TEAM_001.md` §19, in particular: **the test failing to yield ~50 mechanism-distinct premises after duplicate rejection is a "revise substantially" trigger.**

## 2. Inputs

- Approved direction: `DEC-0013`–`DEC-0017` (ages 4–6 core, ~3–7 envelope as test claim; visual-first sparse speech; ~5–7 min pilot target; cause/effect + anticipation + escalation + adaptation/repair grammar; implicit educational value; mild rain/mild wind only; powers never auto-solve; balanced agency).
- Red-team diagnostic: `03_research/RED_TEAM/INDEPENDENT_RED_TEAM_001.md` and `FAILURE_MODE_REGISTER_001.md` (used as stress hypotheses, not verdicts).
- Research Sprint 001 corpus and `03_research/PIP_NIMBUS_FEASIBILITY.md`.
- Show Bible v0.1 proposal's eight historical premise examples (re-coded as part of the audit trail; they remain proposals).

## 3. Pre-generation development hypotheses

Before any large-scale generation, minimum development hypotheses were established in [DEVELOPMENT_HYPOTHESES.md](DEVELOPMENT_HYPOTHESES.md): candidate ownable hooks (name-removal tested), character contradiction/want/fear structures, a character comedy engine distinct from the plot engine, an expressive (not expanded) power philosophy, and third-force mechanisms. All remain **development hypotheses** — proposals for owner review, not canon. Generation uses them so the test measures the concept at its strongest plausible specification, per red-team outcome B (testing the unmodified shell would measure a generic frame). Where a hypothesis materially changes the concept, the analysis notes which results depend on it.

## 4. Pipeline

1. **Generation.** Five independent generator passes, each assigned a distinct story-family cluster with mechanism quotas and agency/power-role spread requirements (§6). Generators work from the shared coding taxonomy (§5) so that output is clusterable. Target ~145 raw candidates; volume is an instrument for rejection, not a goal.
2. **Schema validation.** `scripts/stress_test_analysis.py --validate` parses every JSONL record and rejects malformed or out-of-vocabulary rows.
3. **Review and rejection.** Independent reviewer passes (no reviewer reviews a batch from its own generator cluster) apply the acceptance rubric (§7) and rejection criteria (§8). Every candidate receives `status: accepted|rejected` with a coded reason.
4. **Clustering and near-duplicate detection.** Mechanism signatures (§5.4) are computed by script; clusters of size ≥2 receive qualitative review; near-duplicates are rejected or merged with reasons recorded. Automated similarity is an aid only; final distinctness calls are qualitative.
5. **Analysis.** Distributions and correlations computed by script from the final pool and reported in [ANALYSIS_REPORT.md](ANALYSIS_REPORT.md): story-family coverage, mechanism diversity, formula concentration, agency balance, power necessity, character-comedy share, production-burden coding, age-risk flags, rewatch support.
6. **Control sample.** Bounded samples for paused alternatives Fix-It and Lumina ([CONTROL_SAMPLE.md](CONTROL_SAMPLE.md)) answer only the comparative questions the owner asked; alternatives are not reopened for development.
7. **Synthesis.** [FINDINGS_AND_RECOMMENDATION.md](FINDINGS_AND_RECOMMENDATION.md) classifies the concept (PROCEED / PROCEED WITH REPAIRS / REWORK CONCEPT / REOPEN ALTERNATIVES / STOP) as a recommendation to the owner.

## 5. Coding taxonomy

All coded fields use closed vocabularies so clustering is meaningful. Free-text fields carry the creative content.

### 5.1 Story family (`family`)

One primary family per premise (secondary allowed in `family_secondary`):

`building` `waiting` `searching` `finding_losing` `sharing` `competition` `caring` `helping` `misunderstanding` `exploration` `collecting` `preparing` `transporting` `hiding_revealing` `performance` `imitation` `observation` `simple_science` `social_expectation` `embarrassment` `fear_courage` `jealousy` `patience` `responsibility` `celebration` `cleanup` `repair` `choice_conflict` `surprise` `routine_disruption` `cooperation` `independent_goals` `environmental_change`

### 5.2 Causal mechanism (`causal_mechanism`)

What makes the problem happen/progress. Closed list (extendable only with justification in review notes):

`weather_overshoot` (power applies too much/wrong moment), `weather_reveal` (weather exposes/discloses something), `weather_obstacle` (weather blocks a goal without any character error), `feelings_leak` (emotional state manifests as weather and complicates things), `suppression_backfire` (hiding a feeling/mistake worsens it), `over_preparation` (planning itself creates the problem), `rigid_plan_vs_reality` (reality refuses the plan), `misread_signal` (a gesture/state is misinterpreted), `competitive_escalation` (mutual one-upping), `imitation_mismatch` (copying without the why), `care_overreach` (helping beyond what is wanted/needed), `divided_attention` (two duties collide), `promise_deadline` (a commitment/time pressure), `lost_hold` (something is lost/misplaced and must be found), `resource_split` (one thing, two needs), `order_vs_mess` (standards collide), `curiosity_experiment` (testing how something works), `role_reversal` (each tries the other's job), `stage_fright_visibility` (being seen/being ready), `routine_break` (an expected pattern changes), `accident_plain` (plain physical accident, no power), `nature_course` (environment changes on its own: seasons, tide, growth), `communication_gap` (cannot explain what is meant), `generosity_dilemma` (giving away vs keeping), `other` (must be described in `causal_detail`).

### 5.3 Character comedy mechanism (`comedy_mechanism`)

The character-based engine of the funny. Closed list:

`overconfidence` `perfectionism` `misplaced_helpfulness` `impatience` `competitive_escalation` `literal_interpretation` `social_embarrassment` `stubborn_commitment` `excessive_preparation` `hiding_mistake` `trying_to_impress` `role_reversal` `feelings_visible` (a feeling is physically visible at the wrong moment), `forecast_irony` (audience reads a character's state before the other character does), `dignity_maintenance` (pretending everything is fine), `over_literal_rules` (a rule applied where it does not belong), `imitation_flattery` `fomo` (fear of missing out / being left out), `none_character` (comedy rests on physics/situation only — **flagged**, see §8).

`comedy_is_character_based`: `true|false` — true when the scene is still comic with the weather effect removed.

### 5.4 Mechanism signature (computed)

`signature = initiator_type | causal_mechanism | stakes_type | resolution_type`

- `initiator_type`: `pip` | `nimbus` | `shared` | `third_force` | `accident`
- `stakes_type`: `object` | `plan` | `relationship` | `feelings` | `duty` | `deadline`
- `resolution_type`: `joint_repair` | `reframe` (the "problem" becomes the solution), `understanding` (someone finally gets it), `compromise` | `acceptance` (let it go / change the goal), `help_arrives` (third force resolves — capped, see §6), `reset_routine`

Distinct-mechanism counting uses both the `causal_mechanism` vocabulary count and the full signature count; both are reported.

### 5.5 Formula patterns (computed + reviewed)

The three concentration risks named in the owner brief and red-team review:

- `F1_helper_overshoot`: Nimbus helps → power overshoots → problem → joint repair.
- `F2_plan_disrupted`: Pip plans → Nimbus disrupts → chaos → cooperation.
- `F3_weather_object_chase`: weather moves/wets an object → chase → fix.

Each accepted premise is coded `formula_pattern: F1|F2|F3|none`. Concentration = share in F1–F3.

### 5.6 Power necessity (`power_role`)

Answer to: *"If Nimbus were not a cloud and had no weather ability, would the story still be essentially identical?"*

- `essential` — the story cannot exist without the cloud/weather nature.
- `enhanced` — the story works without powers but is materially better/more specific with them.
- `optional` — powers appear but could be removed with minor rewrites.
- `irrelevant` — powers do not appear; story runs on character/world alone.

### 5.7 Third force (`third_force`)

`none` | `social_pressure` (someone to impress/not disappoint) | `care_receiver` (someone/something whose wellbeing is at stake) | `request` (ask/delivery/favor from the implied community) | `deadline` (external time) | `visitor` (episodic, non-speaking or minimal) | `responsive_world` (environment/objects react) | `discovery` (the world presents something new)

### 5.8 Production burden (`production`)

Nine flags, each `low|medium|high`: `vapor_continuity`, `wet_state`, `wind_secondary`, `multi_object`, `prop_contact`, `subtle_acting`, `multi_character`, `environment_complexity`, `camera_continuity`. Overall `burden`: `LOW|MEDIUM|HIGH|EXTREME` by rule: EXTREME if ≥4 highs or any high on `vapor_continuity` + `wet_state` + `subtle_acting` together; HIGH if ≥2 highs; MEDIUM if ≥1 high or ≥3 mediums; else LOW.

### 5.9 Age risk flags (`age_risk`)

Subset of: `younger_confusion` (multi-step inference likely to lose 3–4s), `older_boredom` (nothing for 6–7s), `dialogue_dependent` (needs more than sparse anchors), `abstract_inference` (requires reading intention from subtext alone). Empty list allowed.

### 5.10 Quality scores

Reviewer-scored, 1–3 each: `distinctiveness`, `character_comedy_strength`, `emotional_clarity`, `rewatch_support`. `total` computed. Not a quality guarantee — a comparability aid.

## 6. Generation quotas (per generator, ~28–30 premises)

- Initiator: at most 40% `nimbus`, at most 40% `pip`; ≥3 `shared`, ≥2 `third_force` or `accident`.
- Power role: at most 35% `essential`; at least 15% `irrelevant` (tests whether character comedy survives without weather).
- `weather_overshoot` causal mechanism: at most 3 per batch (prop-swap guard).
- `help_arrives` resolution: at most 2 per batch (resolution must come from the pair per `DEC-0016` spirit).
- ≥60% of premises must have `comedy_is_character_based: true`.
- Every premise needs a `rewatch_detail` (fair callback, hidden detail, or motif) and an `emotional_beat`.
- Every premise states `distinctness_note`: why it differs from its nearest neighbor in the same batch.

## 7. Acceptance rubric

A candidate is accepted only if **all** hold:

1. Compressible into a clear ~5–7 min visual-first story (goal legible within seconds).
2. Contains a character-based comic mechanism (`comedy_mechanism` ≠ `none_character` or, if `none_character`, the reviewer must justify why the physics gag is exceptional).
3. Contains a real emotional beat (not decoration).
4. Contains a plausible rewatch detail.
5. No `DEC` violation: powers never auto-solve; no fixed competence hierarchy; mild, safe, non-imitable weather only; no severe peril.
6. Cast ≤ 2 leads + non-speaking third force; no hidden permanent ensemble.
7. Passes the mini ownability probe: at least one element (relationship rule, expressive-power behavior, world rule, signature gag structure) that a generic preschool show would not have.
8. Scores total ≥ 8/12, with `distinctiveness` ≥ 2.

## 8. Rejection reason codes

`duplicate_signature` | `prop_swap` (same mechanism, different object) | `physics_only_comedy` | `no_emotional_beat` | `no_rewatch` | `power_autosolve` | `competence_hierarchy` | `unsafe_or_severe` | `hidden_ensemble` | `dialogue_dependent_unfixable` | `too_abstract_for_core` | `generic_no_hook` | `unproducible_extreme` (EXTREME burden without exceptional creative score) | `family_forced` (family clearly does not fit the concept — recorded as evidence) | `weak_total`

## 9. Ownability probe (property level)

Separately from per-premise rule 7, the strongest accepted premises are re-tested with Pip/Nimbus/cloud/weather terms removed. What survives structurally (the relationship rule, the visibility-of-feelings mechanic, the forecast-irony comedy position) is reported as the ownable-layer evidence in FINDINGS.

## 10. Honesty rules

- Rejections are real: rejected candidates are preserved with reasons; re-generation to hit a number is forbidden.
- No premise is accepted to fill a family; an unsupported family is reported as a finding.
- Prop changes never count as diversity.
- The pool is generated to be inspectable: raw, rejected, and accepted files are all durable artifacts.
- The generators' own scores are advisory; reviewer scores decide acceptance.

## 11. Known method limits

- All premises are desk creations by AI agents; no child, caregiver, or market evidence is produced here. Preference remains untested (see `T1`–`T10` battery in the red-team review).
- Mechanism taxonomies are judgment tools; another coder might draw boundaries differently. The closed vocabularies, preserved pool, and recorded reasons exist so another reviewer can re-audit.
- A premise surviving this test proves *writable distinctness at skeleton level*, not episode quality, acting feasibility, or audience love.
