import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from verify_append_only_ledger import verify
from validate_project_state import validate as validate_state
from validate_repository import validate as validate_repo


class LedgerPrefixTests(unittest.TestCase):
    def test_append_preserves_exact_bytes(self):
        verify(b'old\r\nbytes\n', b'old\r\nbytes\nnew\n')

    def test_changed_byte_rejected(self):
        with self.assertRaisesRegex(ValueError, 'byte 3'):
            verify(b'old\n', b'oldX\n')

    def test_truncation_rejected(self):
        with self.assertRaises(ValueError):
            verify(b'old\n', b'old')

    def test_reorder_rejected(self):
        with self.assertRaises(ValueError):
            verify(b'a\nb\n', b'b\na\n')


class StateTests(unittest.TestCase):
    def test_current_repository_valid(self):
        self.assertEqual(validate_repo(), [])

    def test_unknown_state_reference_rejected(self):
        state = (ROOT / 'PROJECT_STATE.md').read_text(encoding='utf-8') + '\nDEC-9999\n'
        ledger = (ROOT / 'PROJECT_LEDGER.md').read_text(encoding='utf-8')
        self.assertIn('State cites absent ledger ID: DEC-9999', validate_state(state, ledger))

    def test_broken_link_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            (path / 'PROJECT_LEDGER.md').write_text((ROOT / 'PROJECT_LEDGER.md').read_text(encoding='utf-8'), encoding='utf-8')
            (path / 'PROJECT_STATE.md').write_text((ROOT / 'PROJECT_STATE.md').read_text(encoding='utf-8'), encoding='utf-8')
            (path / 'broken.md').write_text('[missing](missing.md)', encoding='utf-8')
            self.assertTrue(any('Broken link:' in error for error in validate_repo(path)))

    def test_manifest_fields_present(self):
        data = json.loads((ROOT / '04_episodes/templates/PRODUCTION_MANIFEST_TEMPLATE.json').read_text(encoding='utf-8'))
        self.assertEqual(data['status'], 'PROPOSAL')
        self.assertEqual(data['reuse_tags']['nimbus_powers'], [])


if __name__ == '__main__':
    unittest.main()
