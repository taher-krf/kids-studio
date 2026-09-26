# Stress Test 001 — Development Hypotheses

Status: **DEVELOPMENT HYPOTHESES — NOT CANON, NOT OWNER-APPROVED.** Created under the owner-authorized stress test. Every hypothesis here is a proposal for later owner review; none modifies `DEC-0013`–`DEC-0017`. Mild rain / mild wind remain the only test powers (`DEC-0016`); nothing below adds powers. Character names remain provisional working names.

Purpose: red-team outcome B (`PROP-0005`) requires the stress test to run against the concept's strongest plausible specification rather than its current generic shell. These hypotheses are that specification. Where they are weak, the stress test should expose it.

---

## 1. Ownable-hook hypotheses

A hook must survive the **name-removal test**: state it without "Pip", "Nimbus", "cloud", or "weather" words and check whether it still describes a specific show rather than a genre. Three candidates were developed and probed.

### H1 — "The forecast friend"
> One friend cannot hide a feeling: every feeling shows up around him as a small physical event before he says a word — and his best friend has become an expert at reading him.

Name-removed: *"One character's feelings physically manifest around him before he can speak them; his friend reads those signs better than he does."*
Probe: structurally specific — it names a **visibility rule** and a **relationship skill**. It is not "organized + silly solve problems." Nearest neighbors: feelings-as-weather is a known *poetic device* in children's books, but as a *series engine* (dramatic irony for 4-year-olds: the audience can always see the feeling coming) it is not occupied by any competitor in `03_research/COMPETITORS/COMPETITOR_MATRIX.md`. Residual risk: a screen may find closer neighbors (recorded in the originality screen).

### H2 — "Help that has to be read, not asked for"
> A friend who shows what he needs instead of saying it, and a planner who keeps misreading the signs.

Weaker: reduces to a misunderstanding engine; collapses toward a single mechanism over a catalog. Recorded, not pursued as primary.

### H3 — "The little sky that lives with us"
> A household-scale piece of sky participates in everyday life.

Weakest: a setting gimmick, no relationship rule; fails to differentiate from any cloud character. Rejected as a hook candidate.

**Hypothesis adopted for generation:** H1 as primary; H2 retained as a subplot mechanism family. **Not approved as the show's hook** — the property-level ownability verdict is a stress-test output (see ANALYSIS_REPORT), and the final hook remains an owner decision.

---

## 2. Character contradiction / want / fear hypotheses

Goal: each lead is pulled in **two directions by their own nature** (red-team §5: trait corridors → contradictions), with **no definitional asymmetry** — neither is defined by a deficit relative to the other. Three structures were compared.

### Structure A — "Two bids for belonging" (adopted for generation)

- **Pip.** *Want:* for things to go well — and to be **wanted**, not just useful. *Fear:* being the boring one; that if the plan is not needed, he is not needed. *Contradiction:* he plans to secure shared joy, but over-planning **squeezes out the very spontaneity he envies** in Nimbus. He organizes fun like a duty and then watches Nimbus get the laughs. *Behavioral signatures:* contingency lists for feelings; rehearses hellos; tidies things that were fine; says "as planned" when nothing is.
- **Nimbus.** *Want:* to be **needed** — helping is his bid for belonging. *Fear:* that his feelings (which physically leak out of him) make him a burden — "my rain ruins things." *Contradiction:* the more he tries to **hide** a feeling, the more it shows (suppression backfire); he would rather cause a small disaster than admit he is sad. *Behavioral signatures:* hovers too close when worried; produces apologetic drizzle when embarrassed; skittery gusts when excited; goes unnaturally still when hiding something (the tell).

**Why this structure:** (1) Symmetric — both leads share one fear (being unwanted) expressed through opposite strategies (competence vs. helpfulness), which generates social comedy from *comparison*, not hierarchy. (2) Neither is "smart vs. silly": Pip's failures come from feeling, Nimbus's competence is real (he genuinely can water a garden). (3) It powers jealousy, embarrassment, competition, and performance families — the exact families the red team found weak — without adding cast. (4) It gives the audience the H1 dramatic-irony position: Nimbus's state is visible; Pip's is hidden under competence — two different reading games.

### Structure B — "Order-lover vs. sensation-seeker"

Pip wants predictability and fears chaos; Nimbus wants novelty and fears boredom. Rejected: this is the generic odd-couple corridor the red team already flagged; it generates plan-vs-impulse only, one tension axis.

### Structure C — "Both compete for the world's approval"

Both want to impress the implied community. Rejected as primary: makes third parties load-bearing in every story and pushes toward vanity themes ill-suited to 4–6. Retained as an occasional episode spice (social_expectation family).

**Adopted: Structure A**, with C as a rare variant. Twelve-state re-test under A: Pip can now be selfish (hoards the plan), afraid (of being left out), uncertain (plan fails), generous (cedes the plan), brave (improvises publicly). Nimbus can be selfish (helping to be praised), afraid (of his own rain), uncertain (am I welcome?), confident (real skill), brave (admits a feeling). Both pass without hierarchy.

---

## 3. Character comedy engine (development level)

Distinct from the plot engine (`DEC-0015` grammar). The claim under test: **character behavior alone must generate comedy in scenes with no weather use.** Four engine components, all derived from §2-A:

- **E1 — Forecast irony (signature).** The audience can see Nimbus's emotional weather forming before Pip reads it. Comic anticipation for the youngest viewers: "uh-oh, the drip-drip means he's worried." This is the property's candidate **ownable comic position**: dramatic irony made visual and preschool-legible.
- **E2 — Suppression backfire.** Nimbus tries to contain a feeling; containment produces stranger small effects than honesty would have. Escalation by *kind* change (drip → hiccup-gust → fog of embarrassment), not by amount.
- **E3 — Plan theater.** Pip performs competence to secure belonging: ceremonies, schedules, labels for things that need none; comic deflation when reality declines to attend. The joke is the *performance*, never stupidity.
- **E4 — Bid collision.** Both characters make a bid for the same reassurance at the same moment (each secretly prepared the same surprise; each tries to let the other win and produces a stalemate of politeness). Comedy of mutual generosity — warmth-preserving, cruelty-free.

Supporting mechanisms (coded in `comedy_mechanism`): overconfidence, perfectionism, misplaced helpfulness, impatience, competitive escalation, literal interpretation, social embarrassment, stubborn commitment, excessive preparation, hiding a mistake, trying to impress, role reversal, feelings visible, dignity maintenance, over-literal rules, imitation/flattery, fear of missing out.

**Test embedded in the pool:** every premise must name its `comedy_mechanism`; `comedy_is_character_based=false` premises are flagged so the analysis can measure how often the show is funny *because of who they are* versus *because physics happened*.

---

## 4. Power philosophy hypothesis — "expressive, not expanded"

**Statement (proposal, bounds unchanged):** Mild rain and mild wind remain the entire power set. What changes is the *account* of them: **the effects are how Nimbus's inner state and intentions take physical form**, within strict bounds — visible trigger, visible duration, visible cost; never the primary resolver of the story; never severe; legible to a 4-year-old as "that came from him, and he didn't mean it."

Development mapping (not canon): excitement → skittery, hard-to-steer gusts; worry → intermittent drip; embarrassment → apologetic drizzle that follows him; suppressed sadness → grey sag and misty edges; calm care → soft, even, brief rain exactly where aimed. **Intent shapes character-of-effect, not power-of-effect**: intensity stays mild; duration stays short; no new effects, no transformation, no size change.

Why this is the load-bearing hypothesis:

1. It answers FM-04 (decorative powers) without power inflation (FM-05): the powers become the **character's emotional exterior** — removing them would remove the character, so `power_role=irrelevant` episodes no longer make Nimbus pointless, because *he is still the one whose feelings show* even when no rain falls.
2. It converts the small causal vocabulary from a limit into a **reading game**: few effects, many meanings — like reading a face. Variety comes from context, not from effect count.
3. It prices production honestly: emotional-weather acting is *more* demanding, not less; the burden coding in this test treats that as cost, not as a free win.

Falsifier: if the accepted pool still concentrates in `weather_overshoot`/`F1–F3` despite this hypothesis, the expressive philosophy fails at premise level and the report must say so.

---

## 5. Third-force hypotheses (no permanent third lead)

The red team identified three missing story **functions** — social pressure, a care-receiver, external friction — and warned against a hidden ensemble. Hypothesized delivery systems, all development-only:

- **T-A, The Village Layer (implied community):** the pair lives inside a small implied community that never appears on camera as a character: a note asking for a favor, muffins expected for a stall, a borrowed item to return, a friend heard but not seen. Supplies requests, deadlines, social pressure. *Guardrail: the community may ask, never solve.*
- **T-B, The Small Living Charge (recurring care-receiver):** one non-speaking, low-agency living thing in the world that needs periodic care — hypothesis: a garden bed and a visiting snail. It creates emotional stakes ("is it okay?") without dialogue or ensemble. *Guardrail: it must stay object-of-care, not a protagonist; if it starts driving plots, it has become a hidden lead.*
- **T-C, The Responsive Place (world that answers):** the compact world contains elements with simple legible behavior — a stream that carries paper boats, a kite line, a laundry line, stepping stones, a hill that echoes. Supplies friction, discovery, and callback anchors; gives wind/rain something *legible* to act on. *Guardrail: the world reacts; it never has intentions.*

Premises are coded by which function they use (`third_force`); a premise needing a speaking third character is rejected (`hidden_ensemble`). The analysis reports whether third-force use stayed a seasoning or became a crutch.

---

## 6. What these hypotheses deliberately do NOT do

- No new powers, no transformation, no size change, no severe weather.
- No third main character; no named world; no visual design; no names decision.
- No episode scripts; premises are skeletons for capacity measurement only.
- No claim that any hypothesis is correct — the stress test exists to attack them.
