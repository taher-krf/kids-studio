# Pilot 1 · State-chaining experiment + Production Sequence 05 — "The Chair Adapts" · v0.1

**Status: PRODUCTION-TEST DOCUMENT. DEVELOPMENT MATERIAL. NOT CANON. NO RENDERER LOCK. ZERO ADDITIONAL SPEND (`DEC-0021`).** Executed 2026-09-26/27 in Kimi Cowork under the owner task brief ("Continue directly from the current canonical Kids Studio state… END-STATE → NEXT-SHOT START-STATE CONTINUITY"). Shot authority: [silent animatic shot plan v0.1](../04_episodes/development_pilots/P1_A_CHAIR_FOR_MULU_SHOT_PLAN_V0.1.md) sequence S05 (plan shots SH15–SH17, beat P1-05). Prior evidence: [P01_S01 test](PILOT01_S01_CHAIR_ATTEMPT_TEST_V0.1.md) (`RES-0013`) and the V-01–V-05 smoke test (`RES-0012`).

## 1. Phase A — State-chaining experiment (ONE take)

- **Source shot:** `P01_S01_SH04_T01.mp4` (selected take; ends with Mulu seated on the chair, Tekla standing stage-right).
- **Conditioning method:** the actual **final frame** of SH04 T01 (extracted frame 121/121, `SH04_T01_final_frame.png`) uploaded and passed as the primary `reference_image`, with the Mulu and Tekla masters as identity anchors. Instruction: continue the exact scene (same camera, light, positions), minimal motion only — Mulu stays seated, settling, doubtful glance; Tekla folds arms, deadpan stare, one slow blink. No new gag, no boing.
- **Output:** `Sequence_01_Chair_Attempt/CHAINING_TEST/P01_S01_CHAIN_SH04_TO_SH05_T01.mp4` (4.04 s, 1280×720, 24 fps). The original SH05 is untouched.
- **Result:** the first frame of the chaining take is visually indistinguishable from SH04's final frame — Mulu seated (position, scale, orientation, worried face), chair identical, Tekla at her mark, same generated hilltop, same light, same screen direction. The reaction beat plays inside that state: Mulu settles with a tiny bob and turns a doubtful look; Tekla folds her arms into the deadpan stare; hold. No reset, no reconstruction.
- **Verdict: PASS.** Final-frame conditioning retains the previous shot's spatial state convincingly in this environment.
- **What changed vs the S01 failure mode:** the SH04→SH05 state break (seated → hovering) disappears when the next shot is conditioned on the actual previous final frame instead of design masters only. Remaining drift: none observed at this minimal motion level (small-motion restraint likely helps; high-action chaining is proven by S05 below, with one partial miss at SH17).

**Consequence for the production playbook:** chaining a shot from the previous selected take's final frame is now the **default method** for connected sequences in the Kimi environment, combined with the character/world masters as identity anchors. (If a future chaining take FAILs — model reconstructs the scene despite the frame — fall back to shot design/editing: end shots on simple states and cut on action.)

## 2. Phase B — S05 "The Chair Adapts" (plan SH15–SH17)

Purpose per the brief: continuation from the failed first attempt, prop-state continuity, Tekla's builder behavior, Mulu's readable reaction, comedy without dialogue dependence, stable scale, chair modification continuity.

**Prop states (tracked explicitly):**

| State | Visible difference | Established | Persisting into |
| --- | --- | --- | --- |
| CHAIR_STATE_A | baseline ladder-back chair (as in S01) | S01 | SH15 |
| CHAIR_STATE_B | one leg (front-left from camera) visibly shorter by ~10–15%; chair wobbles; sawn-off offcut + hand saw rest on the grass beside it | SH16 (on-screen) | SH17 and all later P1 shots until the drain-hole state (plan SH26) |

The chair remains **DEVELOPMENT PROP — NOT FINAL CANON** (`PRP-CHAIR-NEW`).

**Continuity chain used:** SH05 T01 final frame → SH15 reference; SH15 T01 final frame → SH16 reference; SH16 T01 final frame → SH17 reference; Mulu/Tekla masters as identity anchors in all three. Cameras locked medium throughout (HT-02 axis; Mulu left, chair centre, Tekla right).

### SH15 — The measuring (6 s, plan 7 s — tool-duration judgement per intent)

- **Continuity-in:** S01 end state (Mulu hovering stage-left of the chair with doubt; Tekla stage-right, arms folded); chair STATE_A.
- **Action:** Tekla takes the yellow folding ruler from her apron pocket, extends it toward Mulu to measure him; the ruler comes back bent/wiggly; she stares at it, one firm nod; ruler back in pocket.
- **Continuity-out:** ruler in pocket (D15); both at their marks; chair unchanged.
- **Result T01:** start frame identical to SH05's end (chaining holds). The ruler reads as a yellow tape-style ruler; the **bent-ruler gag is clearly visible** (the ruler drapes in a curve, f072–f096). The "sinks into his fluff" contact was softened into a drape toward the chair side. Tekla's eyes go wide-round for a moment at f096 (a surprise break from her half-lidded neutral — expressive and charming, but an eye-style watch item, consistent with the known light-sclera/generic-eye drift risk). Mulu holds position, scale and worried-doubt read throughout.
- **Verdict: PASS.** Notes: fluff-sink contact not literal (class 3, soft-contact easing); Tekla wide-eye moment logged as watch item.

### SH16 — The saw (6 s)

- **Continuity-in:** SH15 end state; chair STATE_A.
- **Action:** Tekla kneels beside the chair with a small wooden-handled hand saw, saws a few centimetres off the nearest chair leg with calm strokes; the offcut drops to the grass; she sets the saw down and stands, deadpan; the chair stands with one shorter leg and wobbles gently.
- **Continuity-out:** chair **STATE_B** (short leg, wobble ON), offcut + saw on the grass, Tekla standing arms folded, Mulu hovering watching.
- **Result T01:** the full beat plays as directed — kneel, visible sawing strokes, offcut drop, saw set down, stand. Final frame shows the shortened leg, offcut with sawdust, and the saw on the grass; the chair reads wobbly. Tekla's shell, bands, apron and ruler hold through the kneel (no shell deformation, D12 clean); Mulu hovers on-model stage-left the whole shot.
- **Verdict: PASS.** Prop-state transition A→B happens on-screen and is unambiguous.

### SH17 — Sitting…? over the wobble (6 s)

- **Continuity-in:** SH16 end state — chair STATE_B (short leg, wobble), offcut + saw on grass, Tekla stage-right arms folded, Mulu hovering stage-left.
- **Action:** Mulu floats over the wobbling chair and hovers just above the seat; the chair wobbles beneath him; his doubt reads (worried face, slight puff droop); he does not sit; Tekla watches, one slow blink; hold.
- **Continuity-out:** chair STATE_B persists; Mulu hovering; leads into S06 (the strap).
- **Result T01:** chair STATE_B preserved in **every** frame (short leg + wobble + offcut + saw all persist); Tekla's position/pose exact. **Start-state miss:** Mulu is absent at frame 0 (he was hovering stage-left in SH16's final frame) and flies in within ~0.5 s — since the plan's action is an entrance-and-hover, the cut still reads cleanly, but the inherited state was not fully respected. He hovers **beside** the seat rather than directly over it; the doubt face and puff droop read clearly; the wobble-under-a-floating-friend gag is readable.
- **Verdict: MIXED.** Failure class: 3 (imperfect start-frame adherence: one character dropped at frame 0), partial 2 (prompt implied an entrance, which the tool used). No retry — the take is materially usable and the limitation is recorded (generation-limit rule).

## 3. Sequence review (S05 as a whole)

- **Mulu continuity:** holds — silhouette, Top Puff side and curl, nubs, flat base with cool band, face construction, warm matte material; no limbs, no humanoid anatomy (D04/D06/D07 clean); scale stable across all three shots (D16 clean — chaining anchors it).
- **Tekla continuity:** holds — shell/head-shield, three-band logic, ears, apron, yellow ruler (in pocket before/after use, D15 clean), deadpan behavior; one wide-eye surprise moment in SH15 (watch item; eye-style drift risk, not a redesign signal); scale stable.
- **Chair continuity:** same development chair design in all shots; STATE_A→STATE_B transition on-screen in SH16; STATE_B persists through SH17 including the wobble, the offcut and the saw.
- **Hilltop continuity:** same generated bench-zone environment across SH15–SH17 and consistent with S01's bench zone; no geography flips (D18 clean); no text (D19 clean); no unplanned characters (D20 clean).
- **Screen direction:** held — Mulu left, chair centre, Tekla right throughout.
- **Start/end-state continuity:** SH15 and SH17…SH16 chain exactly (final frame → first frame indistinguishable); SH17 drops Mulu at frame 0 (recovers via the planned entrance). End states match the plan's continuity-out requirements in all three shots.
- **Action readability / AI morphing / camera drift:** actions read (measure → bent ruler → nod; saw → offcut → wobble; hover over wobble → doubt); no identity morphing; all cameras locked, zero drift.
- **Comedy readability:** **LANDS at development level** — the wiggly ruler and the wobbling chair under a hovering cloud both read with sound off, and neither depends on 2–4-frame timing precision (staged per the brief's timing rule).
- **Overall sequence verdict: PASS (development level)** — all brief purposes for S05 are evidenced; SH17's frame-0 character drop is the one logged limitation.

## 4. Combined findings (with RES-0013)

1. **Start-state chaining works.** Final-frame conditioning closed the exact SH04→SH05 failure mode (Phase A PASS) and carried scene, props, scale and light across SH15→SH16→SH17. This is now the default sequence-production method in the Kimi environment.
2. **Residual chaining risk:** the tool may drop a character from frame 0 when the incoming frame is crowded (SH17) — mitigate by prompting the entrance explicitly (self-correcting) or starting shots on simple states.
3. **Prop-state continuity is achievable on-screen**: a directed modification (sawn leg) executed inside one shot and persisted into the next via the chained frame.
4. **Constraint decay (RES-0013 finding) still applies** to sustained physical constraints (hover-over-a-point), but chaining contains it: each new shot re-anchors the state.
5. Class-3 tool limits unchanged for sharp timing accents and state reversals (no retest needed; RES-0012/RES-0013 stand).

## 5. Files

Clips and evidence live OUTSIDE the repository at `C:\Users\PC\Documents\GitHub\Kids Studio Assets\Production\Pilot 01\`: `Sequence_01_Chair_Attempt/CHAINING_TEST/` (Phase A take + source frame), `Sequence_02_Chair_Adapts/SH15|SH16|SH17/` (takes), `Sequence_02_Chair_Adapts/Review/` (contact strips, key frames, chained final frames). Provenance: one row per take in `PILOT01_VIDEO_LOG.csv`. Tool: Kimi Cowork video_generation plugin v0.2.8 via agent-gw (model label and seeds UNKNOWN — not exposed). 1280×720, 16:9, 24 fps. Childhood-gate clean on all takes. 4 takes total this session (1 chaining + 3 S05 shots; no retries needed).

## 6. Next recommended production action

S05 works at development level. Per the evidence, the next smallest Pilot 1 sequence is **S06 "The strap"** (plan SH18–SH19, ~16 s): it reuses this exact staging and chair STATE_B, and its dough-squeeze gag directly re-tests the known class-3 squash limit under the chaining method — the cheapest way to learn whether chaining also stabilizes transformation-adjacent action. (If the squeeze fails as a tool limit, the beat sheet's fallback staging — strap hangs empty, Mulu already popped — keeps the joke readable by editing.)
