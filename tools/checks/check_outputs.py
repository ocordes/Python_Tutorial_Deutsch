#!/usr/bin/env python3
"""Prüft die gespeicherten Ausgaben der Lektion 12.

Alle Python-Zellen werden in einem frischen Namensraum ausgeführt. Stimmen die
installierten Versionen von numpy und pandas mit den Versionen überein, mit
denen die Ausgaben erzeugt wurden, werden die Ausgaben zeichengenau
verglichen. Bei anderen Versionen prüft das Skript nur, dass die Zellen
fehlerfrei und ohne Warnungen laufen; die Darstellung kann sich zwischen
Versionen unterscheiden.

Shell-Zellen wie ``!cat`` werden nicht ausgeführt: Das Programm ``cat`` ist
nicht auf jeder Plattform verfügbar, und die Ausgabe dient nur der Anzeige.

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/checks/check_outputs.py
"""
from __future__ import annotations

import contextlib
import io
import os
import sys
import warnings
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK = ROOT / 'tutorial' / 'Lektion 12: Pandas.ipynb'
EXPECTED_VERSIONS = {'numpy': '2.5.3', 'pandas': '3.0.6'}


def main() -> int:
    try:
        import nbformat
        import numpy as np
        import pandas as pd
    except ImportError as exc:
        print(f'übersprungen: {exc}')
        return 0

    if not NOTEBOOK.is_file():
        print(f'FEHLER: {NOTEBOOK} fehlt')
        return 1

    installed = {'numpy': np.__version__, 'pandas': pd.__version__}
    exact = installed == EXPECTED_VERSIONS
    nb = nbformat.read(NOTEBOOK, as_version=4)
    nbformat.validate(nb)
    os.chdir(NOTEBOOK.parent)

    namespace = {}
    failures = []
    count = 0
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != 'code':
            continue
        count += 1
        if cell.execution_count != count:
            failures.append(
                f'Zelle {i}: execution_count {cell.execution_count}, erwartet {count}')
        source = cell.source
        if not source.strip():
            failures.append(f'Zelle {i}: leere Code-Zelle')
            continue
        if source.lstrip().startswith('!'):
            continue

        buffer = io.StringIO()
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            try:
                with contextlib.redirect_stdout(buffer):
                    exec(compile(source, f'{NOTEBOOK.name}:{i}', 'exec'), namespace)
            except Exception as exc:  # noqa: BLE001
                failures.append(f'Zelle {i}: {type(exc).__name__}: {exc}')
                continue

        for warning in caught:
            failures.append(
                f'Zelle {i}: Warnung {warning.category.__name__}: {warning.message}')

        if exact:
            stored = ''.join(
                ''.join(output.get('text', '')) for output in cell.get('outputs', []))
            actual = buffer.getvalue()
            if stored != actual:
                failures.append(
                    f'Zelle {i}: Ausgabe weicht ab\n'
                    f'-- gespeichert --\n{stored}'
                    f'-- neu --\n{actual}')

    print(f'{NOTEBOOK.name}: {count} Code-Zellen, '
          f'numpy {installed["numpy"]}, pandas {installed["pandas"]}')
    if exact:
        print('  Ausgaben werden zeichengenau verglichen.')
    else:
        print('  info: Ausgaben werden nicht verglichen; geprüft mit '
              f'numpy {EXPECTED_VERSIONS["numpy"]}, '
              f'pandas {EXPECTED_VERSIONS["pandas"]}.')
    print('FEHLER:', failures or 'keine')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
