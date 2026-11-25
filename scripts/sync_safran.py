#!/usr/bin/env python3
"""Export from a trusted, committed Safran checkout (Python 3.9+, Node.js 18+)."""
import hashlib, json, pathlib, subprocess, sys
SOURCE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '../Safran').resolve()
ROOT = pathlib.Path(__file__).resolve().parents[1]
inputs = {}
def read(name):
    data = (SOURCE / name).read_bytes()
    inputs[name] = hashlib.sha256(data).hexdigest()
    return data.decode('utf-8')
def js(name, assignment):
    return json.loads(read(name).split(assignment, 1)[1].strip().removesuffix(';'))
def write(name, data, compact=False):
    target = ROOT / name
    if target.exists() and json.loads(target.read_text()) == data:
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=None if compact else 1) + '\n')
pending = []
for file in sorted((SOURCE / 'hexapla-data').glob('*.js')):
    pending.append(('data/' + file.stem + '.json', js('hexapla-data/' + file.name, ']='), True))
pending.append(('assessments/vorlage-deutung.json', js('hexapla-vorlage.js', 'window.HEXAPLA_VORLAGE=')))
pending.append(('morphology/hexapla-morph.json', js('hexapla-morph.js', 'window.HEXAPLA_MORPH='), True))
for name in ['manual-morph.json', 'lsj-glosses.json', 'open-forms.json']:
    pending.append(('morphology/' + name, json.loads(read('tools/hexapla/' + name))))
for name in ['explanations.json', 'explanations-audit.json', 'explanations-progress.json']:
    pending.append(('assessments/' + name, json.loads(read('tools/hexapla/' + name))))
# Safran's editorial data use JavaScript with comments, so evaluate only this trusted file.
read('textcrit-traditions-data.js')
code = "const fs=require('fs'),vm=require('vm'),box={window:{}};vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),box,{timeout:10000});process.stdout.write(JSON.stringify(box.window.TEXTCRIT_TRADITIONS.filter(([k])=>['Hex','HexSource'].includes(k[0]))));"
tags = json.loads(subprocess.check_output(['node', '-e', code, str(SOURCE / 'textcrit-traditions-data.js')], text=True))
pending.append(('assessments/traditions.json', tags))
commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=SOURCE, text=True).strip()
dirty = subprocess.check_output(['git', 'diff', 'HEAD', '--name-only', '--', *inputs], cwd=SOURCE, text=True).strip()
assert not dirty, 'Commit source changes before export: ' + dirty
for args in pending:
    write(*args)
for name in ['split.py', 'build.py', 'morph.py', 'lsj_glosses.py', 'vorlage_candidates.py', 'build_explanations.py', 'audit_explanations.cjs']:
    content = read('tools/hexapla/' + name)
    (ROOT / 'scripts' / name).write_text(content)
write('manifest.json', {'source': 'https://github.com/mitkin89/Safran', 'commit': commit, 'sha256': dict(sorted(inputs.items()))})
subprocess.run([sys.executable, str(ROOT / 'scripts/validate.py')], check=True)
