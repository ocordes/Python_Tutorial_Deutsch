# Prüfungen für die Notebooks

Die Skripte prüfen die Lektionen in `tutorial/` gegen die Regeln aus `AGENTS.md`.
Alle Aufrufe erfolgen aus dem Wurzelverzeichnis des Repositories:

```bash
python3 tools/checks/check_all.py
```

| Skript | Prüft |
| --- | --- |
| `check_lernziele.py` | gelbe Lernzielzelle, Leitsatz, drei bis fünf Ziele, Position, Inhaltsverzeichnis, Zusammenfassung als letzte Zelle; in Lektion 00 die Legende |
| `check_separators.py` | Trennlinie vor jedem Abschnitt, genau eine Zusammenfassung am Dokumentende, keine doppelten Trenner oder Leerzellen an Abschnittsgrenzen |
| `check_numbering.py` | fortlaufende Abschnittsnummern, passende Unterabschnitte, doppelte oder unauflösbare Anker |
| `check_style.py` | Sie-Form, Absatzlängen, Füllwörter, Ausrufezeichen, tote relative Links und das Notebook-Schema |
| `check_version.py` | Metadatenbox (Autor, Version) und Fußnote in Lektion 00; die genannte Kurz-ID muss als Commit existieren, das Datum muss dazu passen |
| `check_outputs.py` | führt die Python-Zellen der Lektion 12 aus, vergleicht die Ausgaben bei den getesteten Versionen und meldet Warnungen |

## Neue Prüfungen

Neue Prüfskripte werden als `tools/checks/check_*.py` angelegt. `check_all.py`
findet sie automatisch und führt sie ohne Argumente aus. Skripte außerhalb
dieses Verzeichnisses werden nicht als Prüfungen verwendet.

Für `check_outputs.py` werden zusätzlich `numpy`, `pandas` und `nbformat`
benötigt. Bei numpy 2.5.3 und pandas 3.0.6 werden die Ausgaben zeichengenau
verglichen; bei anderen Versionen prüft das Skript nur die Ausführbarkeit.

## Optionen

* `check_lernziele.py --base=HEAD` und `check_separators.py --base=HEAD`
  vergleichen zusätzlich mit einer Basisversion und melden entfernte Links,
  geänderte Code-Zellen oder geänderten Markdown-Inhalt. Ohne diese Option
  prüfen beide Skripte nur die Struktur; sie eignen sich damit auch nach
  beabsichtigten Textänderungen.
* `check_style.py --base=HEAD` prüft zusätzlich, dass keine Anker oder Links
  verloren gehen.
* `check_version.py --head` verlangt, dass die Versionszeile den aktuellen
  Commit nennt. Das gelingt nur unmittelbar vor einem Commit, weil eine Datei
  ihren eigenen Hash nicht tragen kann (siehe `AGENTS.md`, Abschnitt 4.4).

## Binder

`tools/` wird beim Binder-Build von `.binder/postBuild` aus dem Image entfernt.
Die Prüfungen sind deshalb im ausgelieferten Tutorial nicht sichtbar. Das gilt
auch für später ergänzte Skripte unter `tools/checks/`.
