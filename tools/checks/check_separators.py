#!/usr/bin/env python3
"""Prüft die Trenner-Regeln und die Stellung der Zusammenfassung.

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/checks/check_separators.py [--base=HEAD]

Mit --base wird zusätzlich geprüft, dass gegenüber der Basisversion keine
Code-Zellen, Ausgaben oder Markdown-Inhalte entfernt oder geändert wurden.
Ohne --base prüft das Skript nur die Struktur.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUMMARY = '>Zusammenfassung</h2>'


def src(cell):
    return ''.join(cell['source'])


def is_hr(cell):
    return cell['cell_type'] == 'markdown' and src(cell).strip() == '---'


def ends_hr(cell):
    if cell['cell_type'] != 'markdown':
        return False
    lines = [l for l in src(cell).split('\n') if l.strip()]
    return bool(lines) and lines[-1].strip() == '---'


def starts_hr(cell):
    if cell['cell_type'] != 'markdown':
        return False
    lines = [l for l in src(cell).split('\n') if l.strip()]
    return bool(lines) and lines[0].strip() == '---'


def is_empty(cell):
    return not src(cell).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Vergleichscommit für die Regressionsprüfung')
    args = parser.parse_args()
    os.chdir(ROOT)

    fails = []
    for path in sorted(glob.glob('tutorial/Lektion *.ipynb')):
        name = path.split('/')[-1]
        file_fails = []
        cells = json.load(open(path, encoding='utf-8'))['cells']

        old_cells = []
        if args.base:
            old = subprocess.run(['git', 'show', f'{args.base}:{path}'],
                                 capture_output=True, text=True)
            if old.returncode == 0:
                old_cells = json.loads(old.stdout)['cells']

        s_idx = [i for i, c in enumerate(cells) if SUMMARY in src(c)]
        summaries = len(s_idx)
        last = len(cells) - 1

        # 1) genau eine Zusammenfassung, und zwar als letzte Zelle;
        #    Lektion 00 ist ein Orientierungsnotebook ohne Zusammenfassung
        if summaries > 1 or (summaries == 0 and not name.startswith('Lektion 00')):
            file_fails.append(f'{summaries} Zusammenfassungen')
        if summaries:
            s = s_idx[0]
            trailing = cells[s + 1:]
            if trailing:
                file_fails.append(f'{len(trailing)} Zellen nach der Zusammenfassung')
            if s != last:
                file_fails.append('Zusammenfassung nicht letzte Zelle')

        # 2) Trenner vor jedem Abschnitt und vor der Zusammenfassung
        targets = [i for i, c in enumerate(cells)
                   if (c['cell_type'] == 'markdown' and re.match(r'^##\s', src(c)))
                   or SUMMARY in src(c)]
        for i in targets:
            if i == 0:
                continue
            prev = cells[i - 1]
            if not (is_hr(prev) or ends_hr(prev) or starts_hr(cells[i])):
                file_fails.append(
                    f'Trenner fehlt vor {src(cells[i]).splitlines()[0][:40]!r}')

        # 3) keine doppelten Trenner, keine Leerzellen an Abschnittsgrenzen
        for i, c in enumerate(cells):
            if is_hr(c) and i and is_hr(cells[i - 1]):
                file_fails.append(f'doppelter Trenner bei Zelle {i}')
            if is_empty(c) and (i + 1 < len(cells)) and (
                    is_hr(cells[i + 1]) or re.match(r'^##\s', src(cells[i + 1]))
                    or SUMMARY in src(cells[i + 1])):
                file_fails.append(
                    f'leere Zelle {i} ({c["cell_type"]}) an einer Abschnittsgrenze')

        # 4) Dokument endet nicht mit Trenner
        if cells and is_hr(cells[-1]):
            file_fails.append('Dokument endet mit Trenner')

        # 5) Code-Zellen und Ausgaben unveraendert (leere Platzhalter ausgenommen)
        def has_content(c):
            return bool(src(c).strip()) or bool(c.get('outputs'))

        def in_order_cells(old, new):
            it = iter(new)
            return all(any(x == y for y in it) for x in old)

        if old_cells:
            code_new = [c for c in cells if c['cell_type'] == 'code' and has_content(c)]
            code_old = [c for c in old_cells if c['cell_type'] == 'code' and has_content(c)]
            if not in_order_cells(code_old, code_new):
                file_fails.append('Code-Zellen oder Ausgaben geaendert oder entfernt')

        # 6) Markdown-Inhalte unveraendert (Trennzeilen zaehlen nicht zum Inhalt)
        def content(cell):
            lines = [l for l in src(cell).split('\n')
                     if l.strip() != '---' and not l.strip().startswith('<!--')]
            text = '\n'.join(lines).strip()
            # Autorenzelle traegt zusaetzlich die Version: nur den Autor vergleichen
            if text.startswith('*Autor:'):
                text = '*Autor:*'
            return text

        def in_order(old, new):
            # Ergaenzungen am Ende einer Zelle sind erlaubt (z. B. neuer Eintrag im
            # Inhaltsverzeichnis), Kuerzungen und Aenderungen nicht.
            it = iter(new)
            return all(any(y == x or y.startswith(x) for y in it) for x in old)

        if old_cells:
            md_new = [content(c) for c in cells
                      if c['cell_type'] == 'markdown' and not is_hr(c)]
            md_old = []
            for c in old_cells:
                if c['cell_type'] != 'markdown' or is_hr(c):
                    continue
                text = content(c)
                if '**Lernziele**' in text:
                    text = '**Inhalt**' + text.split('**Inhalt**', 1)[1]
                md_old.append(text)
            if not in_order(md_old, md_new):
                file_fails.append(
                    'Markdown-Inhalt geaendert oder entfernt '
                    f'({len(md_old)} -> {len(md_new)})')

        print(f'{name}: {len(cells)} Zellen, '
              f'{sum(1 for c in cells if is_hr(c))} Trennerzellen, '
              f'{len(targets)} Abschnitte -> '
              + ('OK' if not file_fails else f'FEHLER {file_fails}'))
        fails += [f'{name}: {f}' for f in file_fails]

    print('\nFEHLER:', fails or 'keine')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
