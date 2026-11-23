# Scripts

These scripts produced the data; they live in the Safran repository (`tools/hexapla/`) and expect its layout
(OSHB text in `bundled/`, page transcriptions in `tools/hexapla/field/<book>/ocr`).

- `split.py` – cuts the scans into tiles for transcription.
- `build.py` – page transcriptions → structured data; locates each Hebrew lemma in the MT by its consonants.
- `morph.py`, `lsj_glosses.py` – Greek morphology and short meanings (run morph.py, lsj_glosses.py, morph.py).
- `vorlage_candidates.py` – candidates for a different Vorlage (confusable letters) for review.
