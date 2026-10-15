# Paper2Chinese — High-Fidelity Academic Translation Agent Skill
## 🚀 Quick Start

**Paper2Chinese is an open-source Agent Skill for high-fidelity academic paper translation.**

Translate English research papers into Chinese while preserving the original structure, figures, tables, equations, and scientific notation.

**Supported outputs:** PDF, editable Word (DOCX), or both.

### Step 1: Install the Skill

Open Codex and enter:

```text
Install the paper2chinese-pdf Agent Skill from:

https://github.com/zhikanglab/Paper2Chinese-PDF

Skill directory: skills/paper2chinese-pdf

Install the Skill for reuse across future sessions.

Check whether the PDF/DOCX toolkit and its Python
dependencies also need to be installed.

Verify the installation and report the results.
```

### Step 2: Upload Your Paper

Start a new Codex session and upload an English research paper in PDF format.

### Step 3: Translate

```text
Use the paper2chinese-pdf Skill to translate
the uploaded academic paper into Chinese.

Requirements:
- Preserve the original English title below the Chinese title.
- Translate the full text without summarizing.
- Preserve the original section and paragraph order.
- Place figures, tables, and equations near their corresponding text.
- Preserve scientific notation, subscripts, and superscripts.
- Maintain natural Chinese character spacing.
- Preserve all original experimental data and conclusions.
- Inspect the final document page by page.

Output format: PDF.
```

### Important Notes

Paper2Chinese is an AI-assisted translation workflow,
not a fully automatic one-click translation service.

Translation accuracy, figure placement, mathematical notation,
and final document quality still require verification.

Additional Python dependencies may be needed for PDF/DOCX generation.

---
**English:** A reproducible agent skill and layout helper for translating academic English PDFs into readable **PDF and editable Word (DOCX)** Chinese editions with inline original figures, tables and equations.

> **Status: early open-source starter / public beta.** This repository contains a complete bilingual layout/QA **skill**, a copy-paste ChatGPT prompt, a reviewable JSON manuscript format, and functioning PDF inspect/build/audit, DOCX build/audit, and source-alignment helper commands. **It is NOT an automatic one-click paper translator**: an AI agent or researcher must supply and review accurate Chinese translations and source-page figure/table/equation coordinates. No OpenAI API call is required by the companion CLI; it does not expose or secretly upload your PDFs.

## Why this project exists
Readers of technical manuscripts should **not** read translated paragraphs on page 3, then have to jump to page 25 for the original figure or equation. The Chinese title should be immediately followed by the English title. Scientific values, captions, equations, references and appendices must remain traceable to their original locations. A draft PDF must pass a render → inspect → repair loop before publication.

## Three ways to use it

### A. ChatGPT without native Skills installation
Open `PROMPT_另一个聊天框直接使用.md`; paste it into a new ChatGPT chat or a ChatGPT **Project instructions** field. Attach the English PDF plus (optionally) a trusted sample Chinese PDF for style reference. Ask to translate **one paper at a time**. Whether the app can generate downloadable PDF files depends on the currently available tools.

### B. Codex / other Agent Skills implementations
- Install the Skill from `skills/paper2chinese-pdf/` into your Codex user-level Skills directory, or copy it into `.agents/skills/paper2chinese-pdf/` in your own repository.
- Or use the separately distributed `paper2chinese-pdf-skill.zip` with its `SKILL.md`, references and standalone PDF tooling.
- For compatible hosts supporting portable Agent Plugins, the repository root includes `plugin.json` and the `skills/` directory. This is a **skill-only starter**, without an MCP server.
- Ask: `Use the paper2chinese-pdf skill to translate this source paper into a Chinese PDF, Word document, or both, with inline figures/tables/equations and QA.`
- A skill is a set of procedural instructions; it is **not** by itself a PDF rendering engine. The agent still needs local utilities.

### C. Python companion CLI — inspect, render from reviewed manuscript, audit
Python >= 3.10. Install dependencies (`python-docx` is included for Word output):

```bash
python -m pip install -e .
paper2zh inspect path/to/source.pdf --out work/source_inventory.json --preview work/preview
python examples/make_synthetic_source.py
paper2zh build examples/example_manifest.json --format pdf --out work/demo.pdf
paper2zh build examples/example_manifest.json --format docx --out work/demo.docx
paper2zh build examples/example_manifest.json --format both --out work/demo_both
paper2zh audit examples/example_manifest.json work/demo_both.pdf
paper2zh audit examples/example_manifest.json work/demo_both.docx
```

The JSON example is a **synthetic demonstration**, not a full translated research paper. For your own work, create a reviewed manifest with ordered Chinese text blocks and `source_page`/`bbox` crops (original PDF coordinates in points). This tool is deliberately honest about what it cannot infer automatically.

## Manifest example
```
{
  "source_pdf": "../source.pdf",
  "metadata": {
    "title_zh": "某多孔材料的动态力学行为研究",
    "title_en": "Dynamic mechanical behavior of a porous material",
    "paper_number": "4",
    "authors": "A. Researcher et al.",
    "journal": "Journal of Example",
    "year": "2026"
  },
  "blocks": [
    {"type": "heading", "text": "摘要"},
    {"type": "paragraph", "text": "这是完整翻译后的中文段落。"},
    {"type": "figure", "source_page": 2, "bbox": [60,120,500,380], "label": "图1", "caption": "不同载荷下的响应曲线"},
    {"type": "equation", "source_page": 3, "bbox": [130,420,490,465], "label": "（1）"}
  ],
  "expected_counts": {"figures": 1, "tables": 0, "equations": 1, "references": 0},
  "quality": {"translation_reviewed": false, "layout_reviewed": false}
}
```

### QA logic and limitations
- `inspect`: extracts page text blocks with coordinates, counts and optional preview PNGs. Two-column reading order is **not guaranteed**; visually validate it.
- `build`: creates a **draft** Chinese PDF / editable DOCX / both from correctly ordered reviewed JSON blocks and cropped source figures/tables/equations (inline). Never treat the draft as a full translation without checking its Chinese text.
- `audit`: checks metadata, structural expected-count coverage, crop bounds and output-specific PDF/DOCX structure; Word alignment and actual image counts are checked. This is **not** a language semantic verifier and cannot certify accurate translation.
- At release, do a visual inspection of every rendered page, and check Chinese-language terminology and numerical fidelity manually.
- Font file paths must be supplied or use system fonts. **No font files are bundled in the repo.**

## Publication, licensing, and privacy
Source code and the synthetic demo are MIT-licensed. **Do not commit other authors' copyrighted PDFs, full translated papers, personal records, API keys, or proprietary fonts.** Review article copyrights and publisher permissions before publicly distributing full translations and figures.

## GitHub repository vs Agent Plugin vs cloud software
This repository includes a minimal **portable Agent Plugin manifest** (`plugin.json`) and a matching **skill-only plugin** at `skills/paper2chinese-pdf/SKILL.md`. Packaging does **not** mean this has been reviewed or published in the ChatGPT Plugin Directory; user eligibility and host support still apply.

The plugin is primarily a **workflow skill**. Its PDF helper scripts run locally when the execution environment supports Python. A hosted ChatGPT app providing one-click translation to all consumers would require a network-accessible MCP server, hosted file processing, authentication/security/privacy design, and plugin submission. We do not claim those have been built. See [official Agent Plugins packaging guidance](https://developers.openai.com/plugins/build/plugins).

## Roadmap
- [ ] Assisted figure/table anchor detection with manual verification UI
- [ ] Optional translation-provider integrations with request budget and provenance
- [ ] Interactive bilingual alignment QA and diff reports
- [ ] Robust math/table re-typesetting and scanned-paper support
- [ ] Optional hosted MCP/plugin deployment with privacy controls

Contributions and issue reports welcome. Please attach only **synthetic or rights-cleared** repro inputs.


## Choosing output formats (new)

| User preference | Command | Deliverable |
|---|---|---|
| Default / archive only PDF | `paper2zh build manuscript.json --format pdf --out translation.pdf` | PDF only |
| Editable Word | `paper2zh build manuscript.json --format docx --out translation.docx` | Real `.docx` with editable text; original diagrams embedded |
| Both PDF and Word | `paper2zh build manuscript.json --format both --out translation` | `translation.pdf` + `translation.docx` |

The **same reviewed translation blocks** drive both layouts. Word is **not** a renamed PDF. Text and scientific subscripts/superscripts are native document runs; original graphs and complex original equations may still be embedded as images for source fidelity. The PDF and Word layouts may have different page breaks.

**Additional Word quality requirement:** render final `.docx` into PNGs using Word or LibreOffice (or the appropriate host DOCX renderer); inspect every single page for CJK glyphs, character gaps, image placement, math indices and split tables. `paper2zh audit ... translation.docx` is only a structural helper, **not a visual or semantic validation**.

The original user's SHPB library remains **PDF-only**. Merely supporting Word in this repository does not create Word files for that archive unless explicitly requested.
