import json
from pathlib import Path
from argparse import Namespace

import fitz
from toolkit.cli import audit, build, inspect_pdf


def test_inspect_build_audit(tmp_path: Path, capsys):
    source = tmp_path / 'source.pdf'
    doc = fitz.open()
    page = doc.new_page(width=595, height=842)
    page.insert_text((55, 75), 'Dynamic mechanical properties in a porous material', fontsize=12)
    page.draw_rect(fitz.Rect(90, 170, 470, 385), color=(0, 0, 0), fill=(0.92, 0.92, 0.92))
    page.insert_text((115, 205), 'Source figure F1', fontsize=16)
    page.draw_line((130, 345), (430, 240), color=(0.1, 0.2, 0.3), width=3)
    page.draw_rect(fitz.Rect(130, 480, 460, 530), color=(0, 0, 0))
    page.insert_text((150, 505), 'sigma = force/area (1)', fontsize=12)
    doc.save(source)
    doc.close()
    inventory = tmp_path / 'inventory.json'
    assert inspect_pdf(Namespace(pdf=str(source), out=str(inventory), preview=str(tmp_path / 'previews'))) == 0
    assert json.loads(inventory.read_text())['pages'] == 1
    assert (tmp_path / 'previews/page_001.png').exists()
    manifest = tmp_path / 'manifest.json'
    manifest.write_text(json.dumps({
        'source_pdf': 'source.pdf',
        'metadata': {'paper_number': '4', 'title_zh': '多孔材料的动态力学性能',
                     'title_en': 'Dynamic mechanical properties in a porous material'},
        'blocks': [
            {'type': 'heading', 'text': '摘要'},
            {'type': 'paragraph', 'text': '这是对研究内容的完整中文段落的合成测试样例。'},
            {'type': 'figure', 'source_page': 1, 'bbox': [90,170,470,385], 'label': '图1', 'caption': '响应曲线'},
            {'type': 'equation', 'source_page': 1, 'bbox': [130,480,460,530], 'label': '(1)'}
        ],
        'expected_counts': {'figures': 1, 'tables': 0, 'equations': 1, 'references': 0},
        'quality': {'translation_reviewed': False, 'layout_reviewed': False}
    }, ensure_ascii=False), encoding='utf-8')
    result = tmp_path / 'zh_draft.pdf'
    assert build(Namespace(manifest=str(manifest), out=str(result))) == 0
    assert result.is_file()
    with fitz.open(result) as d:
        assert len(d) > 0
        assert len(d[0].get_images()) >= 1
    assert audit(Namespace(manifest=str(manifest), pdf=str(result))) == 0
    manifest_data = json.loads(manifest.read_text())
    manifest_data['expected_counts']['figures'] = 2
    manifest.write_text(json.dumps(manifest_data, ensure_ascii=False))
    assert audit(Namespace(manifest=str(manifest), pdf=str(result))) == 2
