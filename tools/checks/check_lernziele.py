#!/usr/bin/env python3
"""Prüft die gelb gestaltete Lernzielzelle und die Legende in Lektion 00.

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/checks/check_lernziele.py [--base=HEAD]

Mit --base wird zusätzlich geprüft, dass gegenüber der Basisversion keine
Markdown-Links verloren gehen.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[2]

YELLOW_BG = 'background-color: #fffde7'
YELLOW_BORDER = 'border: 2px solid #f9a825'
GREEN_BG = 'background-color: #e8f5e9'
SUMMARY = '<div style="background-color: #e8f5e9'


def src(cell):
    return ''.join(cell['source'])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Vergleichscommit für die Linkprüfung')
    args = parser.parse_args()
    os.chdir(ROOT)

    fails = []
    for path in sorted(glob.glob('tutorial/Lektion *.ipynb')):
        name = path.split('/')[-1]
        nb = json.load(open(path, encoding='utf-8'))
        try:
            nbformat.validate(nbformat.read(path, as_version=4))
        except Exception as exc:  # noqa: BLE001
            fails.append(f'{name}: nbformat {exc}')
        cells = nb['cells']

        if args.base:
            old = subprocess.run(['git', 'show', f'{args.base}:{path}'],
                                 capture_output=True, text=True)
            if old.returncode == 0:
                old_links = set(re.findall(r'\]\(([^)]+)\)', ''.join(
                    src(c) for c in json.loads(old.stdout)['cells']
                    if c['cell_type'] == 'markdown')))
                new_links = set(re.findall(r'\]\(([^)]+)\)', ''.join(
                    src(c) for c in cells if c['cell_type'] == 'markdown')))
                lost = old_links - new_links
                if lost:
                    fails.append(f'{name}: Links entfernt: {sorted(lost)}')

        if name.startswith('Lektion 00'):
            legend = [i for i, c in enumerate(cells)
                      if c['cell_type'] == 'markdown' and '### 2.1 Legende der Zellfarben' in src(c)]
            checks = {
                'keine Lernzielzelle': not any(
                    '<h2 style="margin-top: 0;">Lernziele</h2>' in src(c) for c in cells),
                'genau eine Legende': len(legend) == 1,
            }
            if legend:
                text = src(cells[legend[0]])
                checks['gelbe Box in Legende'] = YELLOW_BG in text and YELLOW_BORDER in text
                checks['gruene Box in Legende'] = (
                    GREEN_BG in text and 'border: 2px solid #1b5e20' in text)
                checks['beide Beschriftungen'] = (
                    'Lernziele' in text and 'Zusammenfassung' in text)
                # Legende muss in Abschnitt 2 liegen
                sec2 = [i for i, c in enumerate(cells)
                        if c['cell_type'] == 'markdown' and src(c).startswith('## 2.')]
                sec3 = [i for i, c in enumerate(cells)
                        if c['cell_type'] == 'markdown' and src(c).startswith('## 3.')]
                checks['Legende in Abschnitt 2'] = bool(
                    sec2 and sec3 and sec2[0] < legend[0] < sec3[0])
            bad = [k for k, v in checks.items() if not v]
            print(f'{name}: ' + ('OK' if not bad else f'FEHLER {bad}'))
            fails += [f'{name}: {b}' for b in bad]
            continue

        boxes = [i for i, c in enumerate(cells) if YELLOW_BG in src(c)]
        if len(boxes) != 1:
            fails.append(f'{name}: {len(boxes)} Lernzielzellen')
            continue
        i = boxes[0]
        cell = cells[i]
        text = src(cell)
        checks = {
            'Zelle ist Markdown': cell['cell_type'] == 'markdown',
            'hellgelber Hintergrund': YELLOW_BG in text,
            'gelber Rand': YELLOW_BORDER in text,
            'h2 Lernziele': '<h2 style="margin-top: 0;">Lernziele</h2>' in text,
            'Leitsatz vorhanden': '<p>Nach dieser Lektion können Sie:</p>' in text,
            'drei bis fünf Ziele': 3 <= text.count('<li>') <= 5,
            'keine Leerzeilen im Block': '\n\n' not in text,
            'keine Markdown-Ueberschrift': not re.search(r'^#+ ', text, re.M),
            'Position nach Titel und Trenner': (
                i == 2 and cells[0]['cell_type'] == 'markdown'
                and src(cells[0]).startswith('# ')
                and src(cells[1]).strip() == '---'),
            'Inhaltsverzeichnis folgt': (
                i + 1 < len(cells) and '**Inhalt**' in src(cells[i + 1])),
            'Zusammenfassung zuletzt': SUMMARY in src(cells[-1]),
        }
        bad = [k for k, v in checks.items() if not v]
        print(f'{name}: Zelle {i}, {text.count("<li>")} Ziele -> '
              + ('OK' if not bad else f'FEHLER {bad}'))
        fails += [f'{name}: {b}' for b in bad]

    print('\nFEHLER:', fails or 'keine')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
