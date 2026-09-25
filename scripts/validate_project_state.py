#!/usr/bin/env python3
"""Validate state sections and references to durable ledger IDs."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['Objective and phase', 'Approved operational decisions', 'Provisional creative direction',
            'Technical architecture, agents, tools', 'Open questions and risks', 'Next approved actions and blocks']
ID = re.compile(r'\b(?:RES|DEC|PROP|EXP|ERR|FIX|RSK|AGT|TOOL|IP|VIS|STY|EP|MET|POL)-\d{4}\b|\bSES-\d{8}-\d{3}\b')


def validate(state: str, ledger: str) -> list[str]:
    errors = [f'Missing state section: {name}' for name in REQUIRED if f'## {name}' not in state]
    ledger_ids = set(re.findall(r'^ID: (\S+)', ledger, re.M))
    seen = set()
    for match in ID.finditer(state):
        if match.group() not in ledger_ids and match.group() not in seen:
            errors.append(f'State cites absent ledger ID: {match.group()}')
            seen.add(match.group())
    if 'PROVISIONAL' not in state or 'FOUNDATION' not in state:
        errors.append('State must preserve provisional direction and foundation phase')
    if 'SENSITIVE_CONTENT_REVIEW_REQUIRED' not in state:
        errors.append('State omits sensitive-content escalation')
    return errors


def main() -> int:
    errors = validate((ROOT / 'PROJECT_STATE.md').read_text(encoding='utf-8'),
                      (ROOT / 'PROJECT_LEDGER.md').read_text(encoding='utf-8'))
    for error in errors:
        print('FAIL:', error, file=sys.stderr)
    if errors:
        return 1
    print('PASS: project state sections and ledger references')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
