#!/usr/bin/env python3
"""Prüft Jupyter-Notebooks gegen die Regeln aus AGENTS.md.

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/checks/check_style.py [--allow-no-goals] [--base=COMMIT] [NOTEBOOK ...]

Ohne Notebook-Angaben werden alle Lektionen geprüft. Mit --base wird
zusätzlich geprüft, dass keine Anker oder Links verloren gehen.
"""
import glob
import json
import os
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILLER = r'\b(einfach|natürlich|offensichtlich|trivial|eigentlich|quasi|halt|irgendwie|rumprobieren)\b'
DU = r'\b(du|dein|deine|deinem|deiner|dir|dich|euch|euer)\b'


def read(path):
    return json.load(open(path, encoding='utf-8'))


def markdown(nb):
    md = '\n\n'.join(''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'markdown')
    # HTML-Kommentare (z. B. die Versionsmarker) sind unsichtbar und keine Prosa
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    # Zusammenfassung liegt als HTML-Block vor: fuer die Pruefungen zurueck nach Markdown
    md = re.sub(r'<h2[^>]*>\s*(.*?)\s*</h2>', r'## \1', md)
    md = re.sub(r'<li>\s*(.*?)\s*</li>', r' * \1', md)
    md = re.sub(r'<code>(.*?)</code>', r'`\1`', md)
    md = re.sub(r'</?(?:div|ul)[^>]*>', '', md)
    return md


def prose(md):
    """Entfernt Codeblöcke, Formeln, Tabellen und Überschriften für die Absatzprüfung."""
    md = re.sub(r'```.*?```', '', md, flags=re.S)
    md = re.sub(r'\$\$.*?\$\$', '', md, flags=re.S)
    md = re.sub(r'^\s*\|.*$', '', md, flags=re.M)
    return md


def paragraphs(md):
    out = []
    for block in prose(md).split('\n\n'):
        b = block.strip()
        if not b or b[0] in '#*-[<|>`$':
            continue
        out.append(b)
    return out


def heading_anchors(md):
    return set(re.findall(r"<a id=['\"]([^'\"]+)['\"]>", md))


def links(md):
    return re.findall(r'\]\(([^)]+)\)', md)


def check(path, base_ref=None, allow_no_goals=False):
    errors, notes = [], []
    try:
        nb = read(path)
    except Exception as exc:  # noqa: BLE001
        return [f'kein gültiges JSON: {exc}'], notes

    try:
        import nbformat
        nbformat.validate(nbformat.read(path, as_version=4))
    except ImportError:
        notes.append('nbformat nicht installiert – Schema nicht geprüft')
    except Exception as exc:  # noqa: BLE001
        errors.append(f'nbformat.validate: {exc}')

    md = markdown(nb)
    # Code-Spans und Formeln sind Code, keine Prosa
    text = re.sub(r'`[^`]*`', '', prose(md))

    if re.search(DU, text, re.I):
        errors.append('du-Form: ' + ', '.join(sorted(set(re.findall(DU, text, re.I)))))
    if '!' in text:
        errors.append(f'Ausrufezeichen: {text.count("!")}')
    sog = len(re.findall(r'\bsog\.', text))
    if sog:
        errors.append('sog.: %d' % sog)
    filler = re.findall(FILLER, text, re.I)
    if filler:
        errors.append('Füllwörter: ' + ', '.join(sorted(set(filler))))
    if re.search(r'^----+$', md, re.M):
        errors.append('Trenner mit mehr als drei Bindestrichen')
    if 'Lernziele' not in md and not allow_no_goals:
        errors.append('Lernziele fehlen')

    for para in paragraphs(text):
        protected = re.sub(
            r'(?:z\.\s?B|d\.\s?h|u\.\s?a|bzw|ca|vgl|Dr|Prof|Nr)\.',
            lambda m: m.group(0).replace('.', '\u2024'), para)
        sents = [s for s in re.split(r'(?<=[.!?])\s+', protected) if s.strip()]
        if len(sents) > 4:
            errors.append(f'Absatz mit {len(sents)} Sätzen: {para[:60]}…')

    for target in links(md):
        if target.startswith(('http://', 'https://', '#', 'mailto:')):
            continue
        local = urllib.parse.unquote(target.split('#')[0])
        if local and not os.path.exists(os.path.join(os.path.dirname(path), local)):
            errors.append(f'toter relativer Link: {target}')

    if base_ref:
        try:
            old = subprocess.run(
                ['git', 'show', f'{base_ref}:{path}'],
                capture_output=True, text=True, check=True,
            ).stdout
            old_md = markdown(json.loads(old))
            lost = heading_anchors(old_md) - heading_anchors(md)
            if lost:
                errors.append('entfernte Anker: ' + ', '.join(sorted(lost)))
            old_links = set(links(old_md))
            if old_links - set(links(md)):
                errors.append('entfernte Links: ' + ', '.join(sorted(old_links - set(links(md)))))
        except subprocess.CalledProcessError:
            notes.append('kein Vergleich mit HEAD möglich (Datei dort unbekannt)')

    return errors, notes


def main():
    args = sys.argv[1:]
    base = None
    allow_no_goals = False
    while args and args[0].startswith('--'):
        flag = args.pop(0)
        if flag.startswith('--base='):
            base = flag.split('=', 1)[1]
        elif flag == '--allow-no-goals':
            allow_no_goals = True
        else:
            sys.exit(f'Unbekannte Option: {flag}')
    os.chdir(ROOT)
    if not args:
        args = sorted(glob.glob('tutorial/Lektion *.ipynb'))
    failed = False
    for path in args:
        errors, notes = check(path, base, allow_no_goals)
        print(f'\n== {os.path.basename(path)} ==')
        for note in notes:
            print('  info:', note)
        if errors:
            failed = True
            for err in errors:
                print('  FEHLER:', err)
        else:
            print('  OK')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
