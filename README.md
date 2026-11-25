# Field's Hexapla – a digital transcription

**English** · [Deutsch](README.de.md)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24464811.svg)](https://doi.org/10.5281/zenodo.24464811)

Frederick Field, *Origenis Hexaplorum quae supersunt; sive veterum interpretum Graecorum in totum Vetus Testamentum fragmenta*, 2 vols., Oxford 1875 – transcribed page by page for all 39 books of the Hebrew Bible, with the footnotes, an English translation of the Latin footnotes, the Hebrew lemmas located in the Masoretic text, and a Greek morphology of the readings.

Field collected what survives of Origen's Hexapla: the readings of Aquila (Ἀ.), Symmachus (Σ.), Theodotion (Θ.), the Quinta and Sexta, “the Syrian”, “the Hebrew” and others, next to the Septuagint (Ο΄.) with Origen's signs ※ and ÷. To our knowledge there has been no complete digital text of Field's edition so far.

The data were prepared for the free desktop library [Safran](https://github.com/mitkin89/Safran), where they form the apparatus witness **Hex**.

## Contents

| Folder | Content | Size |
| --- | --- | --- |
| `transcription/<book>/NNNN.txt` | the printed page as transcribed: Hebrew lemma (pointed as printed), Field's Latin translation, the readings with their sigla, the footnotes | 1,838 pages |
| `footnotes-en/<book>/NNNN.txt` | English translation of the Latin footnote text; Greek, Hebrew and Syriac quotations unchanged | 1,712 pages |
| `data/<Book>.json` | structured per verse: lemma, located MT words, Latin, readings, footnotes (Latin and English), page and leaf | 15,840 verses, 26,963 units, 33,456 footnotes |
| `morphology/` | lemma, parsing and short meaning for the Greek word forms of the readings | see below |
| `assessments/vorlage-deutung.json` | 59 reviewed rows where a translator presupposes another Hebrew text (*Vorlage*) or reads the same consonants differently (*Deutung*) | 59 entries |
| `scripts/` | the scripts that produced the data (they run inside the Safran repository) | |
| `docs/` | the transcription and translation instructions (German) | |

Volume I (Genesis–Esther) and volume II (Job–Malachi) were transcribed from the scans of the University of Toronto copies on archive.org: [origenhexapla01unknuoft](https://archive.org/details/origenhexapla01unknuoft), [origenhexapla02unknuoft](https://archive.org/details/origenhexapla02unknuoft).

## Version 1.1.0 — bilingual explanations

New: **27,279 source-bound editorial records with 27,644 German/English
explanation texts** by Codex (2026), plus four supplementary source-attributed
Jewish interpretation annotations. Some records contain multiple explanations.
Field's structured text, English footnotes, morphology and the 59 existing
assessments are unchanged.

These are modern editorial explanations, not statements by Field. Their
presence does not constitute complete philological verification. Original
footnotes and reservations about attribution remain authoritative.

### New files and format

- `assessments/explanations.json`: metadata (`version`, `editor`, `date`, `basis`)
  and `records`. Keys follow `Book chapter:verse#unitIndex siglum`; unit indexes
  are zero-based in `data/<Book>.json`. Each `unitText` must exactly match the
  unit's `t`. `n` is German, `en` English. Optional `variants` items select a
  specific `reading` and optional `forWord`, with their own `n` and `en`.
  Optional `noteSources` stores exact footnote snapshots. Changed source text
  requires editorial rechecking before reusing an explanation.
- `assessments/traditions.json`: `[key, annotation]` pairs. `Hex` keys identify
  an existing `vorlage-deutung.json` assessment; `HexSource` keys identify book,
  verse, zero-based unit index and exact unit text. `noteId` identifies the
  Field footnote compared. Source, editor, category, original verification
  status and bilingual explanation (where supplied) are preserved. Only
  `check: "source-checked"` explicitly denotes a primary-text comparison.
- `assessments/explanations-audit.json` and `explanations-progress.json`:
  Safran's rendering audit. Rendered counts include app-generated explanatory
  items and differ from stored text counts. Units without a parsed synopsis
  are outside the coverage claim; coverage is not a quality assessment.
- `manifest.json`: exact Safran commit and SHA-256 hashes of export inputs.

### Reproduce and validate

Python 3.9+ and Node.js 18+, with a trusted, committed Safran checkout:

```sh
python3 scripts/sync_safran.py /path/to/Safran
python3 scripts/validate.py
```

The sync exports structured data, morphology, assessments and explanations;
page transcriptions and translated page files remain separately maintained.
Validation checks source anchors, quoted footnotes, bilingual texts, reading
selectors, tradition annotations and corpus totals. Copied Safran build/audit
scripts require Safran's layout; see [scripts/README.md](scripts/README.md).

The DOI badge above identifies archived version 1.0.0. The new version DOI
will be added once the Zenodo archive for 1.1.0 is available.

## Format

### Page transcriptions

```
=== Blatt 0120 · S. 8 · GENESIS. [Cap. I. 3–
--- Text
@ 1:3
H: יְהִי־א֑וֹר וַיְהִי־אוֹר׃
L: Fiat lux: et facta est lux.
Ο΄. Θ. γενηθήτω φῶς· καὶ ἐγένετο φῶς. Ἀ. γενέσθω φῶς· καὶ ἐγένετο φῶς. Σ. ἔστω φῶς· καὶ ἐγένετο φῶς.^9
--- Fußnoten
[9] …
```

- `=== Blatt NNNN · S. <printed page> · <running head>` – leaf number of the scan, printed page.
- `@ chapter:verse` – Field's verse number; a second numbering in brackets as printed, `(Forts.)` for a verse continued from the previous page.
- `H:` Hebrew lemma, `L:` Field's Latin translation, then the readings as running text. Footnote markers are written `^n`; footnotes follow under `--- Fußnoten` as `[n] text`.
- Italics are marked `_…_`, uncertain readings `[?]`.

The section names (`Blatt`, `Fußnoten`, `Forts.`) are German because the work was done in a German project.

### Structured data (`data/<Book>.json`)

```json
{"book": "Genesis", "vol": 1, "source": {…},
 "verses": {"1:2": [{"s": 0, "e": 3, "h": "וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ",
                     "l": "_Terra autem erat vastum et vacuum._",
                     "t": "Ο΄. ἡ δὲ γῆ ἦν ἀόρατος καὶ ἀκατασκεύαστος. ’Α. ἡ δὲ γῆ ἦν κένωμα καὶ οὐθέν.^4 …",
                     "leaf": "0119", "pg": "[7]", "fn": ["0119.0.4", …], "field": "1:2"}]},
 "notes": {"0119.0.4": {"la": "…", "en": "…"}}}
```

- Keys of `verses` are **MT** chapter:verse (Westminster Leningrad Codex). `field` keeps Field's own verse number where it differs.
- `s`, `e`: first and last MT word (0-based, words as in the WLC/OSHB text of that verse) that the lemma covers; missing when the lemma could not be located.
- `t`: the readings as printed; `fn`: footnote ids, `notes`: footnote text in Latin (`la`) and English (`en`).
- `cont: true` marks the part of a unit continued from the previous page.

### Morphology (`morphology/hexapla-morph.json`)

Word form → list of `[lemma, parsing key, short meaning]`. Parsing keys follow the LXX morphology of [lxx-morph](https://github.com/OpenScriptorium/lxx-morph). Sources, in this order: the LXX lemmas (Seth Kushniryk, CC BY 4.0), Perseus [Morpheus](https://github.com/perseids-tools/morpheus) for the other forms, a manually checked list (`manual-morph.json`), and short meanings from LSJ ([PerseusDL/lexica](https://github.com/PerseusDL/lexica)). `open-forms.json` lists the forms still without analysis.

## Method and reliability

- The pages were transcribed with Claude (Anthropic, 2026) from the page images, character by character, including all footnotes; the English footnote translation was made the same way. Each verse unit was then located in the Masoretic text by its consonants.
- This is a working transcription, **not a critical edition**. It has not been proofread completely against the print. Please check doubtful passages against the scans (leaf and page are given for every unit) and report errors as an issue.
- The classifications in `assessments/` were made with Claude and reviewed; they are an aid, not an edition.

## License

- Field's edition (1875) is in the **public domain**.
- The transcriptions, the English footnote translations, the structured data and the assessments: **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**. Please cite as below.
- `morphology/`: **[CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/)**, because it contains output of Perseus Morpheus (CC BY-SA 3.0 US) and LSJ glosses (CC BY-SA); see [morphology/LICENSE.md](morphology/LICENSE.md).
- `scripts/`: MIT.

## Citation

See [CITATION.cff](CITATION.cff). Version 1.0.0 is archived on [Zenodo](https://doi.org/10.5281/zenodo.24464811).

> Itkin, Igor Mendel (ed.). *Field's Hexapla: a digital transcription of Frederick Field, Origenis Hexaplorum quae supersunt (Oxford 1875)*. Version 1.1.0, 2026. https://github.com/mitkin89/field-hexapla/releases/tag/1.1.0
