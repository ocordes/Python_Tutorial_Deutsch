#!/usr/bin/env python3
"""Prüft Metadatenbox und Fußnote in Lektion 00.

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/checks/check_version.py [--head]

Geprüft wird, dass die genannte Kurz-ID zu einem Commit gehört und das
angegebene Datum zu diesem Commit passt. Mit --head muss die Zeile zusätzlich
den aktuellen Commit nennen; das gilt nur unmittelbar vor einem Commit, weil
eine Datei ihren eigenen Hash nicht tragen kann (siehe AGENTS.md, 4.4).
"""
import argparse
import glob
import os
import re
import subprocess
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[2]
HASH = re.compile(r'`([0-9a-f]{7,40})`|<code>([0-9a-f]{7,40})</code>')
DATE = re.compile(r'vom (\d{2})\.(\d{2})\.(\d{4})')


def git(*args: str) -> str:
    result = subprocess.run(['git', *args], cwd=ROOT,
                            capture_output=True, text=True, check=True)
    return result.stdout.strip()


def version_hash(line: str) -> str | None:
    """Liest die Kurz-ID aus ``code`` oder aus Backticks."""
    match = HASH.search(line)
    if not match:
        return None
    return match.group(1) or match.group(2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--head', action='store_true',
                        help='verlangt zusätzlich den aktuellen Commit')
    args = parser.parse_args()
    os.chdir(ROOT)

    path = sorted(glob.glob('tutorial/Lektion 00*.ipynb'))[0]
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    cells = nb.cells
    text = [''.join(c.source) for c in cells]
    line = text[1]

    checks = {
        'Zelle 1 enthaelt Marker': '<!-- version:start -->' in line
                                   and '<!-- version:end -->' in line,
        'Autor vorhanden': '<strong>Autor:</strong> Oliver Cordes' in line,
        'Versionslabel vorhanden': '<strong>Version:</strong>' in line,
        'Verweis auf Fussnote': '<sup><a href="#fussnote-ki">1</a></sup>' in line,
        'keine Code-Zelle im Dokument': all(c.cell_type != 'code' for c in cells),
        'Trenner vor der Fussnote': text[-2].strip() == '---',
        'Fussnote ist letzte Zelle': 'fussnote-ki' in text[-1],
        'Fussnote nennt KI-Werkzeuge': 'KI-Werkzeuge' in text[-1],
        'Fussnote nennt Git-Commit': 'Git-Commit' in text[-1],
        'Fussnote mit id': '<small id="fussnote-ki">' in text[-1],
        'Fussnote klein gesetzt': '<small' in text[-1] and '</small>' in text[-1],
        'genau eine Fussnote': sum('id="fussnote-ki"' in t for t in text) == 1,
    }

    short = version_hash(line)
    date = DATE.search(line)
    checks['Version mit Kurz-ID'] = short is not None
    checks['Version mit Commit-Datum'] = date is not None

    head = git('log', '-1', '--format=%h')
    if short:
        try:
            commit_date = git('show', '-s', '--format=%cs', short)
        except subprocess.CalledProcessError:
            checks['Commit existiert'] = False
        else:
            checks['Commit existiert'] = True
            if date:
                day, month, year = date.groups()
                checks['Datum passt zum Commit'] = (
                    commit_date == f'{year}-{month}-{day}')
        if args.head:
            checks['Version nennt HEAD'] = short == head

    fails = []
    footnote = re.sub(r'<[^>]+>', '', text[-1])
    if len(footnote) < 120:
        fails.append(f'Fussnote zu knapp ({len(footnote)} Zeichen)')
    if 'Oliver Cordes' not in ''.join(text):
        fails.append('Autor fehlt')

    bad = [k for k, v in checks.items() if not v]
    fails += [f'{Path(path).name}: {b}' for b in bad]

    print(f'{Path(path).name}: Version `{short or "?"}`'
          f' vom {date.group(0)[4:] if date else "?"}, {len(cells)} Zellen -> '
          + ('OK' if not bad else f'FEHLER {bad}'))
    if short and short != head:
        print(f'  info: HEAD ist `{head}`; die Zeile nennt den Commit, auf dem'
              ' der Stand beruht.')
    print('\nFEHLER:', fails or 'keine')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
