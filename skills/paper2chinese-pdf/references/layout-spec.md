# Layout specification — Chinese academic PDF & Word reading editions

## Page architecture
A4 portrait default, 18-22 mm side margins, 10.5–11.5pt Chinese body type, 1.35–1.55 line-height, non-colliding paragraph spacing. Heading hierarchy visible but restrained. Use an installed CJK font without embedding proprietary font files in the project. Keep normal academic prose left-aligned with predictable line breaks; no orphaned headings, large unneeded whitespace or excessive decoration.

## Bilingual title (mandatory)
First: Chinese title, reasonably prominent (16–18pt).
Directly below: full **original English paper title**, 10–11pt, non-italic or subtle italic. Preserve exact spelling, punctuation, case and acronym.
Follow with publication metadata verified from the source.

## Anchoring rules
- A figure should follow the nearest paragraph first discussing its scientific content, respecting source order. Include caption below image; keep panel labels (a),(b),(c) and legends fully visible. Avoid more than one page separation between discussion and figure except physically impossible cases.
- A table should appear soon after the paragraph that introduces it, with its title above or below consistently. Prefer accessible transcribed tables where parity checked. Avoid screenshots of microscopic text if a reconstruction is possible.
- An equation is always placed immediately adjacent to its introduction or derivation, retains original equation number, and is legible at normal zoom. If OCR/LaTeX is uncertain, crop the **original formula region** cleanly and align centrally.
- In appendices, include each original figure/table/equation under the corresponding appendix heading and translate its caption/neighboring explanation. No single monolithic end appendix of all source PDF pages.
- References retain original sequence and details. Avoid copying entire original article into a trailing appendix as a shortcut.

## Figure cropping guidelines
Inspect figure+caption separately where possible; crop the *plot, axes, legends, scale bars, panel letters and images* but not adjacent unrelated body paragraphs. In a two-column source a figure may span columns, so verify bounding box visually. Rasterize at 180–260 DPI, higher if fine curve labels. Any `bbox=[x0,y0,x1,y1]` should be in **original PDF points** and lie within the named original page.

## Formula cropping guidelines
Ensure whole formula baseline, subscripts and equation numbers are included. Multiple lines should be captured together unless each has its own label. Source's page image is final arbiter; never rely solely on parser text extraction for equations.

## Tables and quality
Check every row and header; no silent truncation of dense tables or black boxes. Wide tables may receive landscape page / smaller font after review or original hi-res crop with an accessible Chinese translation directly adjacent. Short captions on the same page.

## QA inspection protocol
1. Render complete output PDF to PNG at ~150 DPI and assemble contact sheets.
2. Examine every page visually, not only page one. Spot-check original figures against source page images.
3. Scan for: clipped boundaries, margin overflow, misplaced equation numbers, missing figure label, full English pages in wrong location, blank pages, Tofu `□` glyphs, rare Unicode replacement `�`, section sequence breaks.
4. Repair any failed page; re-render it and re-check local preceding/following pages for reflow regressions.
5. Only deliver and archive on passing all gates; maintain temporary files outside user Library.


## Word (DOCX) edition — same source, independent QA
- Generate **editable** paragraphs/headings in native Word structures; embed source figures as images at anchored matching passages. For exceptionally complex mathematical expressions a clean image crop is acceptable if editable OMML mathematics cannot be guaranteed; state that limitation explicitly.
- Apply **left alignment**, natural text spacing, 0 additional character spacing and normal CJK line breaking. Never distribute characters to fill a paragraph.
- Apply real Word subscript/superscript via native run formatting (`font.subscript`, `font.superscript` or correct OMML); raw `W_I` is a draft notation, NOT scientific typesetting.
- Tables should be reconstructed as editable native Word tables where fully verified; otherwise embed a legible original table image at its source location and provide Chinese title/explanatory text. Do not invent numbers.
- Render final DOCX with a Word-compatible engine to PNG, check every page and revise. Reopen exported DOCX to verify paragraphs, pictures, equations/real subscripts and filename integrity. Never assume the PDF preview also validates Word.
- For `PDF+Word`, paragraph wording, numeric values, image order and caption/figure numbers must agree despite different page counts.
