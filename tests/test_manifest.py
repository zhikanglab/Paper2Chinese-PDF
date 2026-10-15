from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]

def test_skill_and_portable_plugin_manifest():
    d = json.loads((ROOT / 'plugin.json').read_text('utf-8'))
    assert d['name'] == 'paper2chinese-pdf'
    assert d['$schema'].endswith('/plugin.schema.json')
    for path in (ROOT / 'skills/paper2chinese-pdf/SKILL.md', ROOT / '.agents/skills/paper2chinese-pdf/SKILL.md'):
        text = path.read_text('utf-8')
        parts = text.split('---', 2)
        assert len(parts) == 3
        meta = yaml.safe_load(parts[1])
        assert meta['name'] == 'paper2chinese-pdf'
        assert 0 < len(meta['description']) <= 1024
    assert (ROOT / 'skills/paper2chinese-pdf/scripts/pdf_tool.py').exists()
