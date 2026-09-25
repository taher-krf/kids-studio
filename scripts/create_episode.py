#!/usr/bin/env python3
"""Create an authorized proposal record from templates, never finished content."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EPISODES = ROOT / '04_episodes'


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--approved-brief', required=True, help='Path to the human-authorized brief')
    p.add_argument('--title', required=True)
    args = p.parse_args()
    brief = Path(args.approved_brief).resolve()
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
    (folder / 'README.md').write_text(f'# {ident}: {args.title}\n\nStatus: PROPOSAL. Source brief: {brief}. No episode canon or production approval.\n', encoding='utf-8')
    print(ident)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
