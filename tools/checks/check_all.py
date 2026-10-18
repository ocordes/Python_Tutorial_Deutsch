#!/usr/bin/env python3
"""Führt alle Notebook-Prüfungen aus und fasst das Ergebnis zusammen.

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/checks/check_all.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECKS = [
    ('Lernziele und Legende', ['tools/checks/check_lernziele.py']),
    ('Trenner und Zusammenfassung', ['tools/checks/check_separators.py']),
    ('Nummerierung und Anker', ['tools/checks/check_numbering.py']),
    ('Stil nach AGENTS.md', ['tools/checks/check_style.py', '--allow-no-goals']),
    ('Version und Fußnote', ['tools/checks/check_version.py']),
]


def main() -> int:
    failed = []
    for title, command in CHECKS:
        print(f'\n### {title}\n', flush=True)
        result = subprocess.run([sys.executable, *command], cwd=ROOT)
        if result.returncode != 0:
            failed.append(title)
    print('\n' + '=' * 60, flush=True)
    if failed:
        print('Fehlgeschlagen:', ', '.join(failed))
        return 1
    print(f'{len(CHECKS)} Prüfungen bestanden.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
