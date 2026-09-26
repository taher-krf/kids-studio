#!/usr/bin/env python3
"""Stress Test 001 analysis: validate premise JSONL, cluster, compute diversity stats.

Stdlib only (DEC-0009). Usage:
  python scripts/stress_test_analysis.py --validate <file.jsonl> [...]
  python scripts/stress_test_analysis.py --analyze <reviewed.jsonl> [--md]
  python scripts/stress_test_analysis.py --split <reviewed.jsonl>   # writes accepted/rejected views

A reviewed record is the generator record plus review fields:
  status: accepted|rejected, reject_reasons: [...], reviewer: str,
  review_scores: {distinctiveness, character_comedy_strength, emotional_clarity, rewatch_support},
  formula_override: F1|F2|F3|none (optional), cluster_review: str (optional).
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / '03_research' / 'STRESS_TEST_001' / 'data'

FAMILIES = {'building', 'waiting', 'searching', 'finding_losing', 'sharing', 'competition', 'caring',
            'helping', 'misunderstanding', 'exploration', 'collecting', 'preparing', 'transporting',
            'hiding_revealing', 'performance', 'imitation', 'observation', 'simple_science',
            'social_expectation', 'embarrassment', 'fear_courage', 'jealousy', 'patience',
            'responsibility', 'celebration', 'cleanup', 'repair', 'choice_conflict', 'surprise',
            'routine_disruption', 'cooperation', 'independent_goals', 'environmental_change'}
CAUSAL = {'weather_overshoot', 'weather_reveal', 'weather_obstacle', 'feelings_leak',
          'suppression_backfire', 'over_preparation', 'rigid_plan_vs_reality', 'misread_signal',
          'competitive_escalation', 'imitation_mismatch', 'care_overreach', 'divided_attention',
          'promise_deadline', 'lost_hold', 'resource_split', 'order_vs_mess', 'curiosity_experiment',
          'role_reversal', 'stage_fright_visibility', 'routine_break', 'accident_plain',
          'nature_course', 'communication_gap', 'generosity_dilemma', 'other'}
COMEDY = {'overconfidence', 'perfectionism', 'misplaced_helpfulness', 'impatience',
          'competitive_escalation', 'literal_interpretation', 'social_embarrassment',
          'stubborn_commitment', 'excessive_preparation', 'hiding_mistake', 'trying_to_impress',
          'role_reversal', 'feelings_visible', 'forecast_irony', 'dignity_maintenance',
          'over_literal_rules', 'imitation_flattery', 'fomo', 'none_character'}
INITIATOR = {'pip', 'nimbus', 'shared', 'third_force', 'accident'}
POWER_ROLE = {'essential', 'enhanced', 'optional', 'irrelevant'}
THIRD_FORCE = {'none', 'social_pressure', 'care_receiver', 'request', 'deadline', 'visitor',
               'responsive_world', 'discovery'}
STAKES = {'object', 'plan', 'relationship', 'feelings', 'duty', 'deadline'}
RESOLUTION = {'joint_repair', 'reframe', 'understanding', 'compromise', 'acceptance',
              'help_arrives', 'reset_routine'}
PROD_FLAGS = ('vapor_continuity', 'wet_state', 'wind_secondary', 'multi_object', 'prop_contact',
              'subtle_acting', 'multi_character', 'environment_complexity', 'camera_continuity')
LEVELS = {'low', 'medium', 'high'}
BURDEN = {'LOW', 'MEDIUM', 'HIGH', 'EXTREME'}
AGE_RISK = {'younger_confusion', 'older_boredom', 'dialogue_dependent', 'abstract_inference'}
REJECT_REASONS = {'duplicate_signature', 'prop_swap', 'physics_only_comedy', 'no_emotional_beat',
                  'no_rewatch', 'power_autosolve', 'competence_hierarchy', 'unsafe_or_severe',
                  'hidden_ensemble', 'dialogue_dependent_unfixable', 'too_abstract_for_core',
                  'generic_no_hook', 'unproducible_extreme', 'family_forced', 'weak_total'}
ID_RE = re.compile(r'^(PN|CTR|CTRL)-[A-Z0-9-]+$')

REQUIRED_TEXT = ('id', 'title', 'logline', 'starting_goal', 'friction_source', 'character_want',
                 'escalation', 'emotional_beat', 'rewatch_detail', 'distinctness_note', 'power_usage')
REQUIRED_ENUM = {'family': FAMILIES, 'initiator_type': INITIATOR, 'causal_mechanism': CAUSAL,
                 'comedy_mechanism': COMEDY, 'power_role': POWER_ROLE, 'third_force': THIRD_FORCE,
                 'stakes_type': STAKES, 'resolution_type': RESOLUTION}


def burden_of(prod: dict) -> str:
    highs = sum(1 for f in PROD_FLAGS if prod.get(f) == 'high')
    meds = sum(1 for f in PROD_FLAGS if prod.get(f) == 'medium')
    if highs >= 4 or all(prod.get(f) == 'high' for f in ('vapor_continuity', 'wet_state', 'subtle_acting')):
        return 'EXTREME'
    if highs >= 2:
        return 'HIGH'
    if highs == 1 or meds >= 3:
        return 'MEDIUM'
    return 'LOW'


def formula_of(p: dict) -> str:
    if p.get('formula_override') in {'F1', 'F2', 'F3', 'none'}:
        return p['formula_override']
    causal, res = p['causal_mechanism'], p['resolution_type']
    if (p['initiator_type'] == 'nimbus'
            and causal in {'weather_overshoot', 'feelings_leak', 'suppression_backfire', 'care_overreach'}
            and p['power_role'] in {'essential', 'enhanced'} and res == 'joint_repair'):
        return 'F1'
    if (p['initiator_type'] == 'pip'
            and causal in {'over_preparation', 'rigid_plan_vs_reality', 'order_vs_mess'}
            and res in {'joint_repair', 'compromise'}):
        return 'F2'
    if causal in {'weather_overshoot', 'weather_obstacle'} and p['stakes_type'] == 'object':
        return 'F3'
    return 'none'


def signature(p: dict) -> str:
    return f"{p['initiator_type']}|{p['causal_mechanism']}|{p['stakes_type']}|{p['resolution_type']}"


def validate_record(p: dict, where: str) -> list[str]:
    errors = []
    if not isinstance(p.get('id'), str) or not ID_RE.match(p['id']):
        errors.append(f'{where}: bad id {p.get("id")!r}')
    for field in REQUIRED_TEXT:
        if not isinstance(p.get(field), str) or not p[field].strip():
            errors.append(f'{where}: missing/empty text field {field}')
    for field, vocab in REQUIRED_ENUM.items():
        if p.get(field) not in vocab:
            errors.append(f'{where}: {field}={p.get(field)!r} not in vocabulary')
    if p.get('family_secondary') is not None and p.get('family_secondary') not in FAMILIES:
        errors.append(f'{where}: family_secondary invalid')
    if p.get('causal_mechanism') == 'other' and not str(p.get('causal_detail', '')).strip():
        errors.append(f'{where}: causal_detail required for other')
    if not isinstance(p.get('comedy_is_character_based'), bool):
        errors.append(f'{where}: comedy_is_character_based must be bool')
    prod = p.get('production')
    if not isinstance(prod, dict):
        errors.append(f'{where}: production missing')
    else:
        for flag in PROD_FLAGS:
            if prod.get(flag) not in LEVELS:
                errors.append(f'{where}: production.{flag} invalid')
        if prod.get('burden') != burden_of(prod):
            errors.append(f'{where}: production.burden should be {burden_of(prod)} not {prod.get("burden")!r}')
    if not isinstance(p.get('age_risk'), list) or not set(p['age_risk']) <= AGE_RISK:
        errors.append(f'{where}: age_risk invalid')
    status = p.get('status', 'candidate')
    if status not in {'candidate', 'accepted', 'rejected'}:
        errors.append(f'{where}: bad status {status!r}')
    if status in {'accepted', 'rejected'}:
        scores = p.get('review_scores')
        if not isinstance(scores, dict) or any(
                scores.get(k) not in {1, 2, 3} for k in
                ('distinctiveness', 'character_comedy_strength', 'emotional_clarity', 'rewatch_support')):
            errors.append(f'{where}: review_scores must be 1..3 on four axes')
        if status == 'rejected':
            reasons = p.get('reject_reasons')
            if not reasons or not set(reasons) <= REJECT_REASONS:
                errors.append(f'{where}: rejected record needs valid reject_reasons')
    return errors


def load_jsonl(path: Path) -> tuple[list[dict], list[str]]:
    records, errors = [], []
    for lineno, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f'{path.name}:{lineno}: {exc}')
    ids = [r.get('id') for r in records]
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f'{path.name}: duplicate id {dup}')
    for r in records:
        errors.extend(validate_record(r, f"{path.name}:{r.get('id', '?')}"))
    return records, errors


def pct(n: int, total: int) -> str:
    return f'{n} ({100.0 * n / total:.1f}%)' if total else '0'


def table(counter: Counter, total: int, order: list[str] | None = None) -> list[str]:
    keys = order or [k for k, _ in counter.most_common()]
    lines = ['| value | count | % |', '| --- | ---: | ---: |']
    for k in keys:
        lines.append(f'| {k} | {counter.get(k, 0)} | {100.0 * counter.get(k, 0) / total:.1f} |')
    return lines


def analyze(records: list[dict]) -> str:
    accepted = [r for r in records if r.get('status') == 'accepted']
    rejected = [r for r in records if r.get('status') == 'rejected']
    out = ['# Stress Test 001 — computed analysis', '',
           f'- total records: {len(records)}',
           f'- accepted: {len(accepted)}', f'- rejected: {len(rejected)}', '']
    for r in accepted:
        r['_formula'] = formula_of(r)
        r['_signature'] = signature(r)
        r['_total'] = sum(r['review_scores'].values())
    out.append('## Rejection reasons')
    reasons = Counter(x for r in rejected for x in r['reject_reasons'])
    out += table(reasons, len(rejected))
    out.append('\n## Accepted: story family coverage')
    fam = Counter(r['family'] for r in accepted)
    out += table(fam, len(accepted), sorted(FAMILIES))
    missing = sorted(FAMILIES - set(fam))
    out.append(f'\nFamilies with zero accepted premises: {", ".join(missing) or "none"}')
    out.append('\n## Accepted: causal mechanisms')
    out += table(Counter(r['causal_mechanism'] for r in accepted), len(accepted), sorted(CAUSAL))
    out.append('\n## Accepted: distinct mechanism signatures')
    sigs = Counter(r['_signature'] for r in accepted)
    out.append(f'- distinct full signatures: {len(sigs)} of {len(accepted)} accepted')
    out.append(f'- distinct causal mechanisms used: {len(set(r["causal_mechanism"] for r in accepted))} of {len(CAUSAL)} defined')
    out.append(f'- signatures shared by 2+ premises (near-dup candidates): {sum(1 for v in sigs.values() if v > 1)}')
    out.append('\n| signature | count | ids |')
    out.append('| --- | ---: | --- |')
    for sig, count in sigs.most_common():
        if count > 1:
            ids = ', '.join(r['id'] for r in accepted if r['_signature'] == sig)
            out.append(f'| {sig} | {count} | {ids} |')
    out.append('\n## Accepted: formula concentration (heuristic + reviewer overrides)')
    out += table(Counter(r['_formula'] for r in accepted), len(accepted), ['F1', 'F2', 'F3', 'none'])
    out.append('\n## Accepted: initiator / agency')
    out += table(Counter(r['initiator_type'] for r in accepted), len(accepted),
                 ['pip', 'nimbus', 'shared', 'third_force', 'accident'])
    out.append('\n## Accepted: power necessity')
    out += table(Counter(r['power_role'] for r in accepted), len(accepted),
                 ['essential', 'enhanced', 'optional', 'irrelevant'])
    out.append('\n## Accepted: character-based comedy')
    cb = sum(1 for r in accepted if r['comedy_is_character_based'])
    out.append(f'- character-based: {pct(cb, len(accepted))}')
    out.append('\n## Accepted: comedy mechanisms')
    out += table(Counter(r['comedy_mechanism'] for r in accepted), len(accepted))
    out.append('\n## Accepted: third force')
    out += table(Counter(r['third_force'] for r in accepted), len(accepted),
                 sorted(THIRD_FORCE))
    out.append('\n## Accepted: resolution types')
    out += table(Counter(r['resolution_type'] for r in accepted), len(accepted), sorted(RESOLUTION))
    out.append('\n## Accepted: production burden')
    out += table(Counter(r['production']['burden'] for r in accepted), len(accepted),
                 ['LOW', 'MEDIUM', 'HIGH', 'EXTREME'])
    out.append('\n## Burden vs quality (accepted)')
    by_burden = defaultdict(list)
    for r in accepted:
        by_burden[r['production']['burden']].append(r['_total'])
    out.append('| burden | n | mean review total (4-12) |')
    out.append('| --- | ---: | ---: |')
    for b in ('LOW', 'MEDIUM', 'HIGH', 'EXTREME'):
        vals = by_burden.get(b, [])
        out.append(f'| {b} | {len(vals)} | {(sum(vals) / len(vals)):.2f} |' if vals else f'| {b} | 0 | - |')
    out.append('\n## Burden vs power role (accepted)')
    out.append('| power role | LOW | MEDIUM | HIGH | EXTREME |')
    out.append('| --- | ---: | ---: | ---: | ---: |')
    for role in ('essential', 'enhanced', 'optional', 'irrelevant'):
        row = [sum(1 for r in accepted if r['power_role'] == role and r['production']['burden'] == b)
               for b in ('LOW', 'MEDIUM', 'HIGH', 'EXTREME')]
        out.append(f'| {role} | {row[0]} | {row[1]} | {row[2]} | {row[3]} |')
    out.append('\n## Accepted: age risk flags')
    flags = Counter(x for r in accepted for x in r['age_risk'])
    out += table(flags, len(accepted))
    out.append('\n## Accepted: score distribution')
    out += table(Counter(str(r['_total']) for r in accepted), len(accepted))
    return '\n'.join(out) + '\n'


def apply_review(records: list[dict], overrides: dict) -> tuple[list[dict], list[str]]:
    """Apply review_overrides.json to raw candidates -> reviewed records. Enforces rubric §7."""
    errors = []
    sigs = defaultdict(list)
    for r in records:
        sigs[signature(r)].append(r['id'])
    engine_sig = {'forecast_irony', 'feelings_visible', 'dignity_maintenance', 'hiding_mistake',
                  'fomo', 'imitation_flattery', 'misplaced_helpfulness', 'trying_to_impress',
                  'social_embarrassment'}
    reject = overrides.get('reject', {})
    rewatch3 = set(overrides.get('rewatch3', []))
    out = []
    for r in records:
        r = dict(r)
        rid = r['id']
        r['reviewer'] = overrides.get('reviewer', 'review')
        if rid in reject:
            reasons = reject[rid]
            r['status'] = 'rejected'
            r['reject_reasons'] = reasons
            physics = not r['comedy_is_character_based']
            r['review_scores'] = {
                'distinctiveness': 1,
                'character_comedy_strength': 1 if physics else 2,
                'emotional_clarity': 1 if 'weak_total' in reasons else 2,
                'rewatch_support': 1}
        else:
            r['status'] = 'accepted'
            r['reject_reasons'] = []
            r['review_scores'] = {
                'distinctiveness': 3 if len(sigs[signature(r)]) == 1 else 2,
                'character_comedy_strength': 3 if (r['comedy_is_character_based']
                                                   and r['comedy_mechanism'] in engine_sig) else 2,
                'emotional_clarity': 3 if r['stakes_type'] in {'feelings', 'relationship'} else 2,
                'rewatch_support': 3 if rid in rewatch3 else 2}
        total = sum(r['review_scores'].values())
        if r['status'] == 'accepted' and (total < 8 or r['review_scores']['distinctiveness'] < 2):
            errors.append(f'{rid}: accepted but rubric fails (total={total})')
        r['formula_pattern'] = formula_of({**r, 'formula_override':
                                           overrides.get('formula_overrides', {}).get(rid)})
        note = overrides.get('reject_notes', {}).get(rid) or overrides.get('accepted_notes', {}).get(rid)
        if note:
            r['review_note'] = note
        out.append(r)
    return out, errors


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    mode, files = args[0], [Path(a) for a in args[1:] if not a.startswith('--')]
    if mode == '--review':
        overrides = json.loads(files[0].read_text(encoding='utf-8'))
        records, errors = [], []
        for f in sorted(files[1].glob('batch_*.jsonl')):
            recs, errs = load_jsonl(f)
            records += recs
            errors += errs
        if errors:
            for e in errors:
                print('FAIL:', e, file=sys.stderr)
            return 1
        reviewed, errors = apply_review(records, overrides)
        if errors:
            for e in errors:
                print('FAIL:', e, file=sys.stderr)
            return 1
        files[2].write_text(''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n'
                                    for r in reviewed), encoding='utf-8')
        n_acc = sum(1 for r in reviewed if r['status'] == 'accepted')
        print(f'reviewed {len(reviewed)}: accepted {n_acc}, rejected {len(reviewed) - n_acc} -> {files[2]}')
        return 0
    if mode == '--validate':
        errors: list[str] = []
        for f in files:
            _, errs = load_jsonl(f)
            errors.extend(errs)
        for e in errors:
            print('FAIL:', e, file=sys.stderr)
        print(f'{"FAIL" if errors else "PASS"}: {len(errors)} errors')
        return 1 if errors else 0
    if mode == '--analyze':
        records, errors = [], []
        for f in files:
            recs, errs = load_jsonl(f)
            records += recs
            errors += errs
        if errors:
            for e in errors:
                print('FAIL:', e, file=sys.stderr)
            return 1
        print(analyze(records))
        return 0
    if mode == '--split':
        records, errors = load_jsonl(files[0])
        if errors:
            for e in errors:
                print('FAIL:', e, file=sys.stderr)
            return 1
        for name, pred in (('premises_accepted.jsonl', lambda r: r.get('status') == 'accepted'),
                           ('premises_rejected.jsonl', lambda r: r.get('status') == 'rejected')):
            selected = [r for r in records if pred(r)]
            (files[0].parent / name).write_text(
                ''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n' for r in selected),
                encoding='utf-8')
            print(f'{name}: {len(selected)}')
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
