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
import create_episode
import build_dev_sketches
import xml.etree.ElementTree as ET
from unittest.mock import patch


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

    def test_episode_scaffold_records_master_history(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            episodes = root / '04_episodes'
            (episodes / 'templates').mkdir(parents=True)
            (episodes / 'templates/PRODUCTION_MANIFEST_TEMPLATE.json').write_text('{"status":"PROPOSAL"}', encoding='utf-8')
            brief = root / 'brief.md'
            brief.write_text('OWNER_APPROVED_EPISODE_PROPOSAL', encoding='utf-8')
            (root / 'PROJECT_LEDGER.md').write_text('# Ledger\n', encoding='utf-8')
            with patch.object(create_episode, 'ROOT', root), patch.object(create_episode, 'EPISODES', episodes), patch.object(sys, 'argv', ['create_episode.py', '--approved-brief', str(brief), '--title', 'Test']):
                self.assertEqual(create_episode.main(), 0)
            self.assertEqual(json.loads((episodes / 'EP-0001/manifest.json').read_text(encoding='utf-8'))['episode_id'], 'EP-0001')
            self.assertIn('ID: EP-0001', (root / 'PROJECT_LEDGER.md').read_text(encoding='utf-8'))
            self.assertIn('Source brief: brief.md', (episodes / 'EP-0001/README.md').read_text(encoding='utf-8'))


class SketchTests(unittest.TestCase):
    def test_committed_sketches_match_generator(self):
        with tempfile.TemporaryDirectory() as temp:
            written = build_dev_sketches.build(Path(temp))
            self.assertEqual(len(written), len(build_dev_sketches.SHEETS))
            for path in written:
                ET.parse(path)
                committed = ROOT / '05_visual_system' / 'sketches' / path.name
                self.assertEqual(path.read_bytes(), committed.read_bytes(),
                                 f'{path.name} is stale: run python scripts/build_dev_sketches.py')

    def test_development_manifests_have_unique_ids(self):
        ids = []
        for name in ('CHARACTER_MANIFEST.json', 'PROP_MANIFEST.json', 'ENVIRONMENT_MANIFEST.json'):
            data = json.loads((ROOT / '05_visual_system' / name).read_text(encoding='utf-8'))
            self.assertEqual(data['status'], 'DEVELOPMENT_PROPOSAL')
            ids.extend(item['id'] for item in data['items'])
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == '__main__':
    unittest.main()
