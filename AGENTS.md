# Paper2Chinese PDF/DOCX repository agent instructions

For any task that translates an English academic PDF into a Chinese PDF/DOCX, load `skills/paper2chinese-pdf/SKILL.md` before translation and follow its references as needed.

Non-negotiable quality gates: exact English original title under Chinese translated title; complete sequential translation; inline source-faithful figures/tables/equations; human-verified two-column reading order; full rendered page QA; one paper at a time; no output archives of copyrighted full papers in GitHub repo.

The companion command-line tools in `toolkit/cli.py` implement *inspection, layout rendering from a reviewed manifest, and limited audit*. They do not translate English to Chinese automatically or guarantee numerical/semantic fidelity. Do not claim they do.

Keep all tests passing (`python -m pytest -q`) when modifying scripts. Do not commit temporary PDFs, renders, API keys, user documents, or font files.

Output formats: default PDF only, optional editable DOCX, or both. Preserve identical source-to-translation block ordering. Word requires an independent render-and-review gate; PDF rendering is not equivalent.
