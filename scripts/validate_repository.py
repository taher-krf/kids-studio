#!/usr/bin/env python3
"""Validate foundation structure, links, ledger IDs, schema, and state."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_project_state import validate as validate_state  # noqa: E402

REQUIRED = [
    'README.md', 'AGENTS.md', 'CLAUDE.md', 'PROJECT_STATE.md', 'PROJECT_LEDGER.md', 'CHANGELOG.md',
    '00_project/PROJECT_CHARTER.md', '00_project/BUSINESS_MODEL.md', '00_project/TARGET_AUDIENCE.md',
    '00_project/SUCCESS_METRICS.md', '00_project/ROADMAP.md', '00_project/RISK_REGISTER.md',
    '00_project/OPEN_QUESTIONS.md', '01_show_bible/SERIES_PREMISE.md', '01_show_bible/CORE_PROMISE.md',
    '01_show_bible/PIP.md', '01_show_bible/NIMBUS.md', '01_show_bible/RELATIONSHIP.md',
    '01_show_bible/WORLD_RULES.md', '01_show_bible/POWER_RULES.md', '01_show_bible/CHARACTER_RULES.md',
    '01_show_bible/VISUAL_LANGUAGE.md', '01_show_bible/DIALOGUE_RULES.md',
    '01_show_bible/FORBIDDEN_PATTERNS.md', '02_story_system/STORY_ENGINE.md',
    '02_story_system/EPISODE_STRUCTURE.md', '02_story_system/COMEDY_ENGINE.md',
    '02_story_system/COMEDY_PATTERN_LIBRARY.md', '02_story_system/REWATCH_ENGINE.md',
    '02_story_system/EDUCATIONAL_PHILOSOPHY.md', '02_story_system/AGE_4_6_RULES.md',
    '02_story_system/ORIGINALITY_RULES.md', '02_story_system/STORY_QA.md',
    '04_episodes/templates/PRODUCTION_MANIFEST_TEMPLATE.json',
    '05_visual_system/ASSET_REGISTRY.json', '07_agents/AGENT_ARCHITECTURE.md',
    '07_agents/AGENT_PERMISSION_MODEL.md', '08_operations/HUMAN_APPROVAL_GATES.md',
    '09_metrics/METRIC_DEFINITIONS.md', 'scripts/verify_append_only_ledger.py',
    'scripts/export_context_pack.py', '.github/workflows/ledger-integrity.yml',
    '.github/workflows/repository-validation.yml', '.githooks/pre-commit', '.env.example'
]
LINK = re.compile(r'(?<!!)\[[^]]*\]\(([^)]+)\)')


def validate(root: Path = ROOT) -> list[str]:
    errors = [f'Missing: {path}' for path in REQUIRED if not (root / path).is_file()]
    ledger_path = root / 'PROJECT_LEDGER.md'
    state_path = root / 'PROJECT_STATE.md'
    if not ledger_path.exists() or not state_path.exists():
        return errors
    ledger = ledger_path.read_text(encoding='utf-8')
    state = state_path.read_text(encoding='utf-8')
    ids = re.findall(r'^ID: (\S+)', ledger, re.M)
    if len(ids) != len(set(ids)):
        errors.append('Duplicate ledger IDs')
    for heading, ident in re.findall(r'^## (\S+)\n\nID: (\S+)', ledger, re.M):
        if heading != ident:
            errors.append(f'Ledger heading/ID mismatch: {heading}/{ident}')
    errors.extend(validate_state(state, ledger))
    for path in root.rglob('*.md'):
        if '.git' in path.parts:
            continue
        content = path.read_text(encoding='utf-8')
        for target in LINK.findall(content):
            if target.startswith(('http:', 'https:', 'mailto:', '#')):
                continue
            rel = unquote(target.split('#', 1)[0]).strip()
            if rel and not (path.parent / rel).exists():
                errors.append(f'Broken link: {path.relative_to(root)} -> {target}')
    try:
        manifest = json.loads((root / '04_episodes/templates/PRODUCTION_MANIFEST_TEMPLATE.json').read_text(encoding='utf-8'))
        for field in ('episode_id', 'title', 'premise', 'status', 'characters', 'locations', 'props',
                      'main_comedy_mechanism', 'secondary_comedy_mechanisms', 'powers_used',
                      'emotional_layer', 'educational_layer', 'gags_used', 'callbacks', 'ending_type',
                      'production_method', 'production_problems', 'revisions', 'reviewer_results',
                      'publication_date', 'platform', 'views', 'retention', 'rewatch_indicators',
                      'ctr', 'lessons_learned', 'reuse_tags'):
            if field not in manifest:
                errors.append(f'Episode manifest missing field: {field}')
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f'Episode manifest invalid: {exc}')
    for path in (root / '05_visual_system').glob('*.json'):
        try:
            json.loads(path.read_text(encoding='utf-8'))
        except json.JSONDecodeError as exc:
            errors.append(f'Invalid JSON {path.name}: {exc}')
    return errors


def main() -> int:
    errors = validate()
    for error in errors:
        print('FAIL:', error, file=sys.stderr)
    if errors:
        return 1
    print(f'PASS: structure, links, {len(re.findall(r"^ID: ", (ROOT / "PROJECT_LEDGER.md").read_text(encoding="utf-8"), re.M))} ledger IDs, state, and JSON')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
