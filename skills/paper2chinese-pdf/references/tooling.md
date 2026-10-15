# Companion toolkit interface (GitHub public project)

A companion local Python CLI helps render audited manuscripts. It is intentionally **not** a fully automatic translator and **not** a PDF layout auto-reconstruction engine. It needs source-grounded human/agent work to create the Chinese blocks and crop coordinates.

```
python -m toolkit.cli inspect source.pdf --out work/source_inventory.json --preview work/source_preview
python -m toolkit.cli build examples/example_manifest.json --format pdf --out work/edition_draft.pdf
python -m toolkit.cli build examples/example_manifest.json --format docx --out work/edition_draft.docx
python -m toolkit.cli build examples/example_manifest.json --format both --out work/edition_draft
python -m toolkit.cli audit examples/example_manifest.json work/edition_draft.pdf
python -m toolkit.cli audit examples/example_manifest.json work/edition_draft.docx
```

## JSON manuscript structure
- `source_pdf`: filesystem path to original PDF, absolute or relative to manifest directory.
- `metadata`: object with `title_zh`, exact `title_en`, optional `authors`, `journal`, `year`, `doi`, `paper_number`.
- `expected_counts`: optional object with `figures`, `tables`, `equations`, `references`; populated only after actual source review.
- `blocks`: ordered list of `heading`, `paragraph`, `figure`, `table`, `equation`, `references` blocks.
- `figure`/`table`/`equation`: `source_page` uses 1-based original page numbers; `bbox` in original PDF points; label/caption if applicable.
- `references`: individual source bibliography lines (not summaries).
- `quality`: manual flags `translation_reviewed` and `layout_reviewed`; an automated file check does not certify semantic fidelity.

## Output
The build command outputs draft PDF, DOCX or both from one manifest. The audit command checks structural omissions (relative to expected counts) and validates PDF appearance heuristics. Human visual inspection is still mandatory. Do not upload the draft to a user's official translation library until manually checked and corrections completed.

**Important:** `audit` checks only structural/parsing features. DOCX final QA additionally requires independent DOCX→PNG rendering of every page and visual inspection of true mathematical subscripts/superscripts. The public CLI does not call a translation model.
