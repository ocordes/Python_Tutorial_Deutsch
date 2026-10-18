#!/usr/bin/env python3
"""Prüft Abschnittsnummerierung und interne Anker in allen Lektionen.

Zwei Konventionen:
  * explizit: Nummern stehen im Überschriftentext (## 1. Titel, ### 1.1 Titel)
              -> Nummern müssen fortlaufend und zum Elternteil passend sein.
  * hash:     Gliederung nur über die Anzahl der '#' (## Titel, ### Titel)
              -> Überschriften dürfen keine Nummer tragen, Ebenen dürfen nicht springen.

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/checks/check_numbering.py
"""
import glob
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    os.chdir(ROOT)
    ok = True
    for nb_path in sorted(glob.glob('tutorial/Lektion *.ipynb')):
        name = nb_path.split('/')[-1]
        cells = json.load(open(nb_path, encoding='utf-8'))['cells']
        heads = []          # (level, plain text)
        anchors, links = [], []
        for c in cells:
            if c['cell_type'] != 'markdown':
                continue
            text = ''.join(c['source'])
            for m in re.finditer(r"^(#{2,4})\s+(.*)$", text, re.M):
                raw = m.group(2)
                anchors += re.findall(r"id=['\"]?([A-Za-z0-9_\-]+)", raw)
                plain = re.sub(r"<a id=['\"]?[A-Za-z0-9_\-]+['\"]?></a>", '', raw).strip()
                heads.append((len(m.group(1)), plain))
            links += re.findall(r"\]\(#([A-Za-z0-9_\-]+)\)", text)

        top = [h for lvl, h in heads if lvl == 2]
        explicit = bool(top) and all(re.match(r"\d+\.\s", h) for h in top)

        if explicit:
            nums = []
            for h in top:
                m = re.match(r"(\d+)\.\s", h)
                nums.append(int(m.group(1)) if m else None)
            if nums != list(range(1, len(nums) + 1)):
                print(f'{name}: Top-Nummerierung lückenhaft {nums}')
                print(f'   {top}')
                ok = False
            current = expected = None
            for lvl, h in heads:
                if lvl == 2:
                    m = re.match(r"(\d+)\.", h)
                    current = int(m.group(1)) if m else None
                    expected = 1
                elif lvl == 3:
                    m = re.match(r"(\d+)\.(\d+)\s", h)
                    if not m:
                        print(f'{name}: Unterabschnitt ohne x.y-Nummer: {h!r}')
                        ok = False
                        continue
                    parent, sub = int(m.group(1)), int(m.group(2))
                    if parent != current or sub != expected:
                        print(f'{name}: Unterabschnitt erwartet {current}.{expected}, '
                              f'gefunden {parent}.{sub}: {h!r}')
                        ok = False
                    expected = sub + 1
            mode = 'explizit'
        else:
            mode = 'hash'
            numbered = [h for lvl, h in heads if re.match(r"\d+(\.\d+)*\.?\s", h)]
            if numbered:
                print(f'{name}: Nummer im Überschriftentext trotz Hash-Konvention: {numbered}')
                ok = False
            prev = 2
            for lvl, h in heads:
                if lvl > prev + 1:
                    print(f'{name}: Ebene springt von h{prev} auf h{lvl}: {h!r}')
                    ok = False
                prev = lvl

        dupes = {a for a in anchors if anchors.count(a) > 1}
        if dupes:
            print(f'{name}: doppelte Anker {sorted(dupes)}')
            ok = False
        broken = sorted({l for l in links if l not in anchors})
        if broken:
            print(f'{name}: unauflösbare Ankerlinks {broken}')
            ok = False
        status = 'OK' if not broken and not dupes else 'FEHLER'
        print(f'{name}: {len(top)} Abschnitte, {len(heads)} Überschriften, '
              f'{len(anchors)} Anker, {len(links)} Ankerlinks, Konvention {mode} -> {status}')

    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
