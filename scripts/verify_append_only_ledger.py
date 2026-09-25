#!/usr/bin/env python3
"""Check exact byte-prefix preservation of committed PROJECT_LEDGER.md."""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / 'PROJECT_LEDGER.md'


def git_bytes(ref: str) -> bytes:
    result = subprocess.run(['git', 'show', f'{ref}:PROJECT_LEDGER.md'], cwd=ROOT,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValueError(f'Cannot read ledger at {ref}: {result.stderr.decode(errors="replace").strip()}')
    return result.stdout


def verify(old: bytes, new: bytes) -> None:
    if not new.startswith(old):
        mismatch = next((i for i, (a, b) in enumerate(zip(old, new)) if a != b), min(len(old), len(new)))
        raise ValueError(f'Ledger historical bytes changed or truncated at byte {mismatch}')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-ref', help='Git commit/ref whose ledger must be preserved')
    parser.add_argument('--old-file', type=Path, help='Previous ledger file for direct comparison')
    parser.add_argument('--new-file', type=Path, help='Candidate ledger file (default working tree)')
    parser.add_argument('--staged', action='store_true', help='Compare against staged index version')
    args = parser.parse_args()
    if args.base_ref and args.old_file:
        parser.error('Choose --base-ref or --old-file')
    try:
        old = args.old_file.read_bytes() if args.old_file else git_bytes(args.base_ref) if args.base_ref else b''
        if args.staged:
            result = subprocess.run(['git', 'show', ':PROJECT_LEDGER.md'], cwd=ROOT,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode:
                raise ValueError('Staged ledger is missing')
            new = result.stdout
        else:
            new = (args.new_file or LEDGER).read_bytes()
        verify(old, new)
    except (OSError, ValueError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    print(f'PASS: ledger retains {len(old)} historical bytes; candidate has {len(new)} bytes')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
