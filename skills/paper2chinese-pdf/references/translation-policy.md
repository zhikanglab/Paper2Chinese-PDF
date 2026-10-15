# Translation policy — completeness, fidelity, and reproducibility

## What counts as full translation
- Include title, author and affiliation where legible, abstract, keywords, introductory background, materials, apparatus, experimental design, calculations and formulas, all sections/subsections in the original order, conclusions, acknowledgments, data availability, declarations, appendices, and references.
- Do not collapse 12 pages into 4 pages of conclusions. A polished condensation is **not** a full-paper translation.
- Preserve inline citation numbers and their targets, e.g. [17] stays [17]. Translate in-text commentary but normally retain reference-list bibliographic metadata in the original language.
- An internal English acronym may remain on first usage with its expanded English name and Chinese technical equivalent.
- No automatic conversion of USD/kJ/MPa/ms/% that changes numerical meaning. All numerical values, sig figs, ranges and signs are source-controlled.

## Mandatory opening structure
```
4. 偏高岭土基泡沫地聚物（MKFG）的动态力学行为研究
Mechanical behaviors of metakaolin-based foamed geopolymer (MKFG) under dynamics loading
作者：…… | 期刊：…… | 年份：…… | DOI：…… (only verified)

摘要
[Full Chinese translation of the abstract]
关键词：[Translated, retaining acronyms]
```
Use the first full page to establish heading hierarchy; don't use decorative oversized cover pages that delay the first section.

## Scientific fidelity red flags
- ``loading pressure (MPa)`` often refers to gas gun operating pressure, not specimen compressive stress.
- ``strain rate (s⁻¹)`` is measured/reconstructed for each impact; launching speeds or pressures are loading controls, not strain-rate values.
- Target/design density, dry density, apparent density, and age-conditioned wet/experimental-state density are not interchangeable.
- ``DIF`` requires a static comparator under matched conditions; do not invent it if absent.
- Bar material and apparatus are physical specifications: distinguish steel, aluminum-based, hollow aluminum, viscoelastic PMMA.
- ``W_abs = W_i - W_r - W_t`` is a measured residual energy balance, not automatically pure microscopic fracture dissipation.
- Strength dynamic enhancement, modulus enhancement, energy absorption ratio, specific energy absorption, and energy absorption density have distinct denominators.
- If original table contradicts prose, keep both source forms and include a clearly marked translator verification note.
- Source errors, flawed units, implausible values must be *reported*, not silently modified.

## Structure and evidence map
For each source paragraph, keep an internal mapping:
`source page -> original section -> translated section -> related figure/table/equation IDs -> QA status`.
If an entire paragraph or figure is left undecoded, label the deliverable **incomplete**, do not archive as accepted.

## Figure translation
A source figure containing English legends can remain as the original raster or vector crop to protect curve/data fidelity. Add a faithful Chinese caption and optional concise bilingual key for important labels. If the user explicitly wants all in-figure labels Chinese, redraw carefully with data-level access; replacing text inside images blindly is error-prone.

## Restricted/ownership notes
Translate user-supplied or authorized research PDFs for personal study; do not publish copyrighted full paper images or translated full texts in a public GitHub repository without necessary rights. Release the **tool, prompts, code and synthetic examples** publicly, not copied articles.
