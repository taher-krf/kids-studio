#!/usr/bin/env python3
"""Append a structured session entry after human/agent review of the fields."""
import argparse
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / 'PROJECT_LEDGER.md'


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--action', required=True)
    p.add_argument('--evidence', required=True)
    p.add_argument('--author', required=True)
    p.add_argument('--follow-up', default='None')
    args = p.parse_args()
    now = datetime.now(ZoneInfo('Europe/Istanbul'))
    text = LEDGER.read_text(encoding='utf-8')
    day = now.strftime('%Y%m%d')
    numbers = [int(n) for n in re.findall(rf'^ID: SES-{day}-(\d{{3}})', text, re.M)]
    ident = f'SES-{day}-{max(numbers, default=0)+1:03d}'
    block = f'''\n## {ident}\n\nID: {ident}
Timestamp: {now.isoformat(timespec='seconds')}
Timezone: Europe/Istanbul (UTC+03:00)
Entry Type: SESSION
Status: RECORDED
Author/Agent: {args.author}
Triggered By: Session execution
Context: See PROJECT_STATE.md
Previous Related Entries: None
Decision / Finding / Action: {args.action}
Reasoning: Session work recorded for durable history.
Alternatives Considered: None recorded.
Evidence: {args.evidence}
Risks: See project risk register.
Impact: See changed files.
Files Affected: See Git diff.
Dependencies: None recorded.
Supersedes: None
Superseded By: None
Follow-up Required: {args.follow_up}
Notes: Historical entry; append corrections, never edit.\n'''
    with LEDGER.open('a', encoding='utf-8', newline='\n') as handle:
        handle.write(block)
    print(ident)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
