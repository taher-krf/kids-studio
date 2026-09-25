#!/usr/bin/env python3
"""Generate a new, never-overwritten timestamped context export."""
import re
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / 'exports'
MAX_LEDGER_BYTES = 200_000


def section(text: str, heading: str) -> str:
    match = re.search(rf'^## {re.escape(heading)}\n(.*?)(?=^## |\Z)', text, re.M | re.S)
    return match.group(1).strip() if match else 'Not present in current state.'


def git(*args: str) -> str:
    result = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else 'TO_VERIFY (Git metadata unavailable)'


def main() -> int:
    now = datetime.now(ZoneInfo('Europe/Istanbul'))
    day = now.strftime('%Y-%m-%d')
    serial = max([int(x.stem.rsplit('_', 1)[-1]) for x in EXPORTS.glob(f'CONTEXT_PACK_{day}_*.md') if x.stem.rsplit('_', 1)[-1].isdigit()], default=0) + 1
    path = EXPORTS / f'CONTEXT_PACK_{day}_{serial:03d}.md'
    state = (ROOT / 'PROJECT_STATE.md').read_text(encoding='utf-8')
    ledger = (ROOT / 'PROJECT_LEDGER.md').read_text(encoding='utf-8')
    entries = re.split(r'(?=^## (?:RES|DEC|PROP|EXP|ERR|FIX|RSK|AGT|TOOL|IP|VIS|STY|EP|MET|POL|SES)-)', ledger, flags=re.M)
    entries = [e for e in entries if e.startswith('## ')]
    decisions = [e for e in entries if e.startswith('## DEC-')]
    recent = entries[-10:]
    errors = [e for e in entries if e.startswith(('## ERR-', '## FIX-'))][-10:]
    index = '\n'.join('- ' + re.search(r'^## (\S+)', e).group(1) for e in entries)
    previous = sorted(EXPORTS.glob('CONTEXT_PACK_*.md'))
    previous_commit = None
    if previous:
        match = re.search(r'^Source commit: (\S+)', previous[-1].read_text(encoding='utf-8'), re.M)
        previous_commit = match.group(1) if match else None
    changed = git('diff', '--name-only', previous_commit, 'HEAD') if previous_commit and previous_commit != 'TO_VERIFY' else 'First export: no prior context pack.'
    if len(ledger.encode('utf-8')) <= MAX_LEDGER_BYTES:
        history = f'## Full ledger\n\n{ledger}'
    else:
        omitted = [re.search(r'^## (\S+)', e).group(1) for e in entries if e not in decisions and e not in recent]
        history = '## Ledger excerpt\n\nComplete ledger remains in repository. Omitted non-decision entry IDs: ' + (', '.join(omitted) or 'none') + '\n\n' + '\n'.join(decisions + [e for e in recent if e not in decisions])
    parts = [
        '# Kids Studio context pack',
        f'Canonical repository: https://github.com/taher-krf/kids-studio.git\nSource commit: {git("rev-parse", "HEAD")}\nExport timestamp: {now.isoformat(timespec="seconds")}\nTimezone: Europe/Istanbul (UTC+03:00)',
        '## Current PROJECT_STATE\n\n' + state,
        '## Approved decisions\n\n' + section(state, 'Approved operational decisions'),
        '## Provisional decisions\n\n' + section(state, 'Provisional creative direction'),
        '## Open questions\n\n' + (ROOT / '00_project/OPEN_QUESTIONS.md').read_text(encoding='utf-8'),
        '## Agent architecture\n\n' + (ROOT / '07_agents/AGENT_ARCHITECTURE.md').read_text(encoding='utf-8'),
        '## Creative canon summary\n\n' + (ROOT / '02_story_system/AGE_4_6_RULES.md').read_text(encoding='utf-8'),
        '## Technical architecture\n\n' + section(state, 'Technical architecture, agents, tools'),
        '## Risks\n\n' + section(state, 'Open questions and risks'),
        '## Recent sessions and history\n\n' + '\n'.join(recent),
        '## Recent decisions\n\n' + '\n'.join(decisions[-10:]),
        '## Recent errors and corrections\n\n' + ('\n'.join(errors) if errors else 'None recorded.'),
        '## Files changed since prior export\n\n' + changed,
        '## Next actions\n\n' + section(state, 'Next approved actions and blocks'),
        '## Ledger index\n\n' + index,
        history,
    ]
    with path.open('x', encoding='utf-8', newline='\n') as handle:
        handle.write('\n\n'.join(parts).rstrip() + '\n')
    print(path.relative_to(ROOT))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
