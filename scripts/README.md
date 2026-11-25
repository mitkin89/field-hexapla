# Scripts

These scripts produced the data; they live in the Safran repository (`tools/hexapla/`) and expect its layout
(OSHB text in `bundled/`, page transcriptions in `tools/hexapla/field/<book>/ocr`).

- `split.py` – cuts the scans into tiles for transcription.
- `build.py` – page transcriptions → structured data; locates each Hebrew lemma in the MT by its consonants.
- `morph.py`, `lsj_glosses.py` – Greek morphology and short meanings (run morph.py, lsj_glosses.py, morph.py).
- `vorlage_candidates.py` – candidates for a different Vorlage (confusable letters) for review.

## Repository synchronization (1.1.0)

Run `python3 scripts/sync_safran.py /path/to/Safran` in this repository
(Python 3.9+, Node.js 18+). Use a trusted, committed checkout: the exporter
evaluates Safran's editorial JavaScript. Then run `python3 scripts/validate.py`.
Page transcriptions are separately maintained and not replaced by this export.

`build_explanations.py` and `audit_explanations.cjs` are upstream copies.
Run them from their original paths in Safran, not directly here; the audit
also needs Safran's renderer and other witnesses.
