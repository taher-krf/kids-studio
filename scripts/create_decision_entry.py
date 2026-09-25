#!/usr/bin/env python3
"""Append a structured decision or proposal, with permanent next ID."""
import argparse
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / 'PROJECT_LEDGER.md'


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--type', choices=['DEC', 'PROP'], required=True)
    p.add_argument('--status', choices=['APPROVED', 'PROVISIONAL', 'REJECTED'], required=True)
    p.add_argument('--action', required=True)
    p.add_argument('--reason', required=True)
    p.add_argument('--evidence', required=True)
    p.add_argument('--author', required=True)
    p.add_argument('--related', default='None')
    p.add_argument('--follow-up', default='None')
    args = p.parse_args()
    if args.type == 'PROP' and args.status == 'APPROVED':
        p.error('An approved proposal needs an explicit DEC entry')
    now = datetime.now(ZoneInfo('Europe/Istanbul'))
    previous = LEDGER.read_text(encoding='utf-8')
    numbers = [int(n) for n in re.findall(rf'^ID: {args.type}-(\d{{4}})', previous, re.M)]
    ident = f'{args.type}-{max(numbers, default=0)+1:04d}'
    block = f'''\n## {ident}\n\nID: {ident}
Timestamp: {now.isoformat(timespec='seconds')}
Timezone: Europe/Istanbul (UTC+03:00)
Entry Type: {'DECISION' if args.type == 'DEC' else 'PROPOSAL'}
Status: {args.status}
Author/Agent: {args.author}
Triggered By: Project decision process
Context: See PROJECT_STATE.md
Previous Related Entries: {args.related}
Decision / Finding / Action: {args.action}
Reasoning: {args.reason}
Alternatives Considered: None recorded.
Evidence: {args.evidence}
Risks: See risk register.
Impact: See affected state/canon files.
Files Affected: See Git diff.
Dependencies: Human approval for canon.
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
