# Fields Hexapla – eine digitale Transkription

[English](README.md) · **Deutsch**

Frederick Field, *Origenis Hexaplorum quae supersunt; sive veterum interpretum Graecorum in totum Vetus Testamentum fragmenta*, 2 Bde., Oxford 1875 – Seite für Seite transkribiert für alle 39 Bücher der hebräischen Bibel, mit den Fußnoten, einer englischen Übersetzung der lateinischen Fußnoten, den im masoretischen Text verorteten hebräischen Lemmata und einer griechischen Morphologie der Lesarten.

Field hat gesammelt, was von Origenes’ Hexapla erhalten ist: die Lesarten von Aquila (Ἀ.), Symmachus (Σ.), Theodotion (Θ.), Quinta und Sexta, „dem Syrer“, „dem Hebräer“ und anderen, neben der Septuaginta (Ο΄.) mit Origenes’ Zeichen ※ und ÷. Eine vollständige digitale Fassung von Fields Ausgabe gab es unseres Wissens bisher nicht.

Die Daten entstanden für die freie Desktop-Bibliothek [Safran](https://github.com/mitkin89/Safran) und bilden dort den Apparat-Zeugen **Hex**.

## Inhalt

| Ordner | Inhalt | Umfang |
| --- | --- | --- |
| `transcription/<buch>/NNNN.txt` | die gedruckte Seite: hebräisches Lemma (punktiert wie gedruckt), Fields lateinische Übersetzung, die Lesarten mit Siglen, die Fußnoten | 1.838 Seiten |
| `footnotes-en/<buch>/NNNN.txt` | englische Übersetzung des lateinischen Fußnotentextes; griechische, hebräische und syrische Zitate unverändert | 1.712 Seiten |
| `data/<Buch>.json` | je Vers strukturiert: Lemma, zugeordnete MT-Wörter, Latein, Lesarten, Fußnoten (Latein und Englisch), Seite und Blatt | 15.840 Verse, 26.963 Einheiten, 33.456 Fußnoten |
| `morphology/` | Lemma, Bestimmung und Kurzbedeutung der griechischen Wortformen | |
| `assessments/vorlage-deutung.json` | 59 geprüfte Zeilen, in denen ein Übersetzer einen anderen hebräischen Text voraussetzt (*Vorlage*) oder dieselben Konsonanten anders liest (*Deutung*) | 59 Einträge |
| `scripts/` | die Skripte, mit denen die Daten erzeugt wurden (sie laufen im Safran-Repository) | |
| `docs/` | die Anweisungen für Transkription und Übersetzung | |

Grundlage sind die Scans der Exemplare der University of Toronto auf archive.org: Bd. I (Genesis–Ester) [origenhexapla01unknuoft](https://archive.org/details/origenhexapla01unknuoft), Bd. II (Hiob–Maleachi) [origenhexapla02unknuoft](https://archive.org/details/origenhexapla02unknuoft).

Das Format ist in der [englischen Fassung](README.md#format) beschrieben.

## Methode und Verlässlichkeit

- Die Seiten wurden mit Claude (Anthropic, 2026) nach den Seitenbildern Zeichen für Zeichen transkribiert, einschließlich aller Fußnoten; ebenso die englische Übersetzung der Fußnoten. Danach wurde jede Verseinheit über ihre Konsonanten im masoretischen Text verortet.
- Das ist eine Arbeitstranskription, **keine kritische Edition**, und sie ist nicht vollständig gegen den Druck Korrektur gelesen. Zweifelhafte Stellen bitte am Scan prüfen (Blatt und Seite stehen bei jeder Einheit) und Fehler als Issue melden.
- Die Einordnungen in `assessments/` sind mit Claude erstellt und geprüft; sie sind eine Hilfe, keine Edition.

## Lizenz

- Fields Ausgabe (1875) ist **gemeinfrei**.
- Transkription, englische Fußnoten, strukturierte Daten und Einordnungen: **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de)**.
- `morphology/`: **[CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.de)**, weil es Ergebnisse von Perseus Morpheus (CC BY-SA 3.0 US) und LSJ-Kurzbedeutungen (CC BY-SA) enthält.
- `scripts/`: MIT.

## Zitieren

Siehe [CITATION.cff](CITATION.cff). Jede Version wird auf Zenodo mit eigener DOI archiviert.
