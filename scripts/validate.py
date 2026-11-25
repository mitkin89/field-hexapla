#!/usr/bin/env python3
"""Validate exported Field source anchors and bilingual editorial explanations."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
def read(name): return json.loads((ROOT / name).read_text())
books = {p.stem.replace('_', ' '): json.loads(p.read_text()) for p in (ROOT / 'data').glob('*.json')}
assert len(books) == 39
verses = sum(len(d['verses']) for d in books.values())
units = sum(len(v) for d in books.values() for v in d['verses'].values())
notes = sum(len(d['notes']) for d in books.values())
assert (verses, units, notes) == (15840, 26963, 33456)
for book, data in books.items():
    for ref, rows in data['verses'].items():
        for row in rows:
            assert all(n in data['notes'] for n in row.get('fn', [])), (book, ref)
explanations = read('assessments/explanations.json')
count = 0
for key, record in explanations['records'].items():
    match = re.fullmatch(r'(.*) (\d+:\d+)#(\d+) (.+)', key)
    assert match, key
    book, ref, index, siglum = match.groups()
    unit = books[book]['verses'][ref][int(index)]
    assert unit['t'] == record['unitText'], key
    normalized = re.sub(r'\((?:juxta\s+ed\.|s\.|fort\.|potius)\s+[^()]*\)', '', unit['t'])
    normalized = re.sub(r'\s+', ' ', normalized)
    assert siglum in unit['t'] or siglum in normalized, key
    for note_id, snapshot in record.get('noteSources', {}).items():
        assert books[book]['notes'].get(note_id) == snapshot, (key, note_id)
    variants = record.get('variants', [record])
    assert variants, key
    if 'variants' in record:
        assert len({(v.get('reading'), v.get('forWord')) for v in variants}) == len(variants), key
    for variant in variants:
        assert variant.get('n') and variant.get('en'), key
        if 'variants' in record: assert variant.get('reading'), key
        count += 1
reviewed = read('assessments/vorlage-deutung.json')
for key, tag in read('assessments/traditions.json'):
    assert tag.get('author') and tag.get('source')
    if key[0] == 'Hex': assert key[1] in reviewed
    else:
        _, book, ref, position, text = key
        unit = books[book]['verses'][ref][position]
        assert unit['t'] == text
        assert tag['noteId'] in unit['fn']
    if tag.get('check') == 'source-checked': assert tag.get('de') and tag.get('en')
print(f'OK: {len(books)} books, {units} units, {notes} footnotes; {len(explanations["records"])} source-bound records, {count} bilingual explanation texts; {len(reviewed)} reviewed assessments; {len(read("assessments/traditions.json"))} tradition annotations.')
