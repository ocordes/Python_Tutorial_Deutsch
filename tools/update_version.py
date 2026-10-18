#!/usr/bin/env python3
"""Schreibt die Versionszeile in Lektion 00 aus dem letzten Git-Commit.

Die Zelle mit Autorenzeile und Version steht zwischen den Markern
``<!-- version:start -->`` und ``<!-- version:end -->``. Das Skript ersetzt
genau diesen Bereich durch die aktuelle Kurz-ID und das Commit-Datum.

Aufruf:
    python3 tools/update_version.py            # Zelle aktualisieren
    python3 tools/update_version.py --check    # nur prüfen (Exit 1 bei Abweichung)

Die Notebooks enthalten das Ergebnis bereits als Text. Beim Lesen muss also
keine Zelle ausgeführt werden.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NOTEBOOK = REPO / 'tutorial' / 'Lektion 00: Wie benutze ich das Tutorial.ipynb'
START = '<!-- version:start -->'
END = '<!-- version:end -->'
AUTHOR = 'Oliver Cordes'
FOOTNOTE_LINK = '<sup><a href="#fussnote-ki">1</a></sup>'


def git(*args: str) -> str:
    """Ruft git im Repository auf und gibt die Ausgabe ohne Zeilenende zurück."""
    result = subprocess.run(
        ['git', *args], cwd=REPO, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def commit_version() -> tuple[str, str]:
    """Liefert Kurz-ID und Datum (TT.MM.JJJJ) des letzten Commits."""
    short_hash, date = git('log', '-1', '--format=%h%n%cs').splitlines()
    year, month, day = date.split('-')
    return short_hash, f'{day}.{month}.{year}'


def version_block(short_hash: str, date: str) -> str:
    """Baut den Inhalt der Zelle inklusive der beiden Marker."""
    line = (f'*Autor: {AUTHOR}* · '
            f'*Version: `{short_hash}` vom {date}*{FOOTNOTE_LINK}')
    return f'{START}\n{line}\n{END}'


def find_cell(notebook: dict) -> dict:
    """Sucht die Markdown-Zelle mit dem Versionsblock."""
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown' and START in ''.join(cell['source']):
            return cell
    raise SystemExit(f'Keine Zelle mit {START} in {NOTEBOOK.name} gefunden.')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true',
                        help='nur prüfen, nichts schreiben')
    args = parser.parse_args()

    notebook = json.loads(NOTEBOOK.read_text(encoding='utf-8'))
    cell = find_cell(notebook)
    current = ''.join(cell['source'])
    short_hash, date = commit_version()
    expected = version_block(short_hash, date)

    if current == expected:
        print(f'{NOTEBOOK.name}: Version `{short_hash}` vom {date} ist aktuell.')
        return 0
    if args.check:
        print(f'{NOTEBOOK.name}: Versionszeile veraltet.')
        print('  vorhanden: ' + current.replace('\n', ' | '))
        print('  erwartet:  ' + expected.replace('\n', ' | '))
        print('  aktualisieren mit: python3 tools/update_version.py')
        return 1

    cell['source'] = expected.splitlines(keepends=True)
    NOTEBOOK.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{NOTEBOOK.name}: Versionszeile auf `{short_hash}` vom {date} aktualisiert.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
