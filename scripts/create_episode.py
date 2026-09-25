#!/usr/bin/env python3
"""Create an authorized proposal record from templates, never finished content."""
import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
EPISODES = ROOT / '04_episodes'


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--approved-brief', required=True, help='Path to the human-authorized brief')
    p.add_argument('--title', required=True)
    args = p.parse_args()
    brief = Path(args.approved_brief).resolve()
    try:
        brief_name = brief.relative_to(ROOT)
    except ValueError:
        p.error('Approved brief must be inside this repository')
    if not brief.is_file() or not brief.read_text(encoding='utf-8').strip():
        p.error('An existing nonempty approved brief is required')
    if 'OWNER_APPROVED_EPISODE_PROPOSAL' not in brief.read_text(encoding='utf-8'):
        p.error('Brief must contain OWNER_APPROVED_EPISODE_PROPOSAL marker')
    existing = [int(n) for n in re.findall(r'EP-(\d{4})', '\n'.join(x.name for x in EPISODES.iterdir()))]
    ident = f'EP-{max(existing, default=0)+1:04d}'
    folder = EPISODES / ident
    folder.mkdir(exist_ok=False)
    manifest = json.loads((EPISODES / 'templates/PRODUCTION_MANIFEST_TEMPLATE.json').read_text(encoding='utf-8'))
    manifest.update(episode_id=ident, title=args.title)
    (folder / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    (folder / 'README.md').write_text(f'# {ident}: {args.title}\n\nStatus: PROPOSAL. Source brief: {brief_name.as_posix()}. No episode canon or production approval.\n', encoding='utf-8')
    now = datetime.now(ZoneInfo('Europe/Istanbul')).isoformat(timespec='seconds')
    record = f'''\n## {ident}

ID: {ident}
Timestamp: {now}
Timezone: Europe/Istanbul (UTC+03:00)
Entry Type: EPISODE PROPOSAL RECORD
Status: PROVISIONAL
Author/Agent: Episode scaffold script; operator TO_VERIFY
Triggered By: Approved proposal brief {brief_name.as_posix()}
Context: Episode proposal scaffold
Previous Related Entries: None
Decision / Finding / Action: Created {ident} proposal manifest and record. No story, episode canon, production, or publishing approval.
Reasoning: Keep episode identity and creation in immutable master history.
Alternatives Considered: None.
Evidence: {brief_name.as_posix()} and 04_episodes/{ident}/manifest.json
Risks: Editorial, originality, safety, and continuity reviews remain required.
Impact: New proposal identity only.
Files Affected: 04_episodes/{ident}/, PROJECT_LEDGER.md
Dependencies: Owner review gates.
Supersedes: None
Superseded By: None
Follow-up Required: Run reviewers and record owner decision before canon change.
Notes: Historical entry; append corrections, never edit.
'''
    with (ROOT / 'PROJECT_LEDGER.md').open('a', encoding='utf-8', newline='\n') as handle:
        handle.write(record)
    print(ident)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
