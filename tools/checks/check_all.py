#!/usr/bin/env python3
"""Führt alle Notebook-Prüfungen aus und fasst das Ergebnis zusammen.

Alle Prüfungen liegen als ``tools/checks/check_*.py`` neben diesem Skript.
Neue Prüfungen werden dort abgelegt und ohne weitere Registrierung
mit ausgeführt. Neue Skripte müssen ohne Argumente laufen; bekannte Optionen
ergänzt dieses Skript. Das Ergebnis wird über den Exit-Code gemeldet.

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/checks/check_all.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECK_DIR = Path(__file__).resolve().parent
TITLES = {
    'check_lernziele.py': 'Lernziele und Legende',
    'check_separators.py': 'Trenner und Zusammenfassung',
    'check_numbering.py': 'Nummerierung und Anker',
    'check_style.py': 'Stil nach AGENTS.md',
    'check_version.py': 'Version und Fußnote',
    'check_outputs.py': 'Ausgaben der Lektion 12',
}
ORDER = [
    'check_lernziele.py',
    'check_separators.py',
    'check_numbering.py',
    'check_style.py',
    'check_version.py',
]
ARGS = {
    'check_style.py': ['--allow-no-goals'],
}


def discover() -> list[tuple[str, list[str]]]:
    """Sammelt alle Prüfskripte, bekannte zuerst, neue danach alphabetisch."""
    scripts = sorted(
        path for path in CHECK_DIR.glob('check_*.py')
        if path.resolve() != Path(__file__).resolve())
    ordered = [CHECK_DIR / name for name in ORDER if (CHECK_DIR / name).is_file()]
    ordered.extend(path for path in scripts if path not in ordered)
    return [(TITLES.get(path.name, path.stem), [str(path), *ARGS.get(path.name, [])])
            for path in ordered]


def main() -> int:
    checks = discover()
    failed = []
    for title, command in checks:
        print(f'\n### {title}\n', flush=True)
        result = subprocess.run([sys.executable, *command], cwd=ROOT)
        if result.returncode != 0:
            failed.append(title)
    print('\n' + '=' * 60, flush=True)
    if failed:
        print('Fehlgeschlagen:', ', '.join(failed))
        return 1
    print(f'{len(checks)} Prüfungen bestanden.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
