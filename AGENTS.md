# Projektkonfiguration: Textstil „Wissenschaft und Tutorial“

Dieses Repository ist ein deutschsprachiges Python-Tutorial für Studierende der
Physik (Vorlesung *EDV für Physikerinnen und Physiker*). Die Inhalte liegen in
Jupyter-Notebooks (`tutorial/Lektion *.ipynb`), ergänzt durch Skripte in
`tutorial/code/`, `tutorial/code2/` und Beispieldaten in `tutorial/data/`.

Diese Datei gilt für **alle Textüberarbeitungen** in diesem Projekt: Markdown-Zellen,
Notebook-Titel, README, Kommentare und Docstrings. Sie beschreibt, wie überarbeitete
Texte zu formulieren sind.

## 1. Ziel

Jeder überarbeitete Text soll zwei Ansprüchen gleichzeitig genügen:

- **Wissenschaftlich:** präzise, überprüfbar, begrifflich konsistent, ohne
  Übertreibung und ohne unnötige Vereinfachung.
- **Tutorial:** führend und nachvollziehbar, mit klaren Lernzielen, motivierten
  Beispielen und reproduzierbaren Schritten.

Der Text erklärt nicht nur *was* gilt, sondern auch *warum* es gilt und *wie* man
es anwendet.

## 2. Zielgruppe und Anrede

- Zielgruppe sind Studierende der Physik im ersten bis dritten Semester mit
  Grundkenntnissen in Mathematik, aber ohne Programmiererfahrung.
- **Anrede: „Sie“** (Großschreibung), wie in den bestehenden Lektionen.
  Kein „du“, kein „wir“ als Ersatz für die Anrede.
- Fachbegriffe werden bei der ersten Verwendung **kursiv** eingeführt und
  unmittelbar danach in einem Satz erklärt, z. B.:
  „Ein *Dictionary* ist eine Zuordnung von Schlüsseln zu Werten.“
- Englische Fachbegriffe bleiben in ihrer Originalform (`Array`, `Keyword`,
  `Type-Hinting`), werden aber beim ersten Auftreten erläutert. Nicht
  eindeutschen und nicht willkürlich zwischen Schreibweisen wechseln.

## 3. Sprachregeln

| Regel | Umsetzung |
| --- | --- |
| Tempo | Kurze Sätze, im Mittel 12–20 Wörter; ein Gedanke pro Satz. |
| Aktiv | Aktiv statt Passiv: „Die Funktion gibt den Wert zurück“ statt „Der Wert wird zurückgegeben“. |
| Präsens | Präsens für allgemeine Aussagen, Futur nur für echte Ankündigungen. |
| Präzision | Konkrete Zahlen, Einheiten und Bedingungen statt vager Angaben („etwa“, „viel“, „schnell“). |
| Absätze | Höchstens vier Sätze; danach ein Absatzwechsel oder eine Liste. |
| Wiederholung | Gleicher Begriff für gleiche Sache – keine Synonymketten („Funktion“/„Routine“/„Methode“). |
| Nüchternheit | Keine Werbesprache, keine Ausrufezeichen, keine Emojis, kein „einfach mal“, „natürlich“, „offensichtlich“, „trivial“. |
| Fehlerkultur | Fehler benennen, ohne abzuwerten: „Ein häufiger Fehler ist …“, nicht „Falsch ist …“. |
| Geschlecht | Geschlechtergerecht formulieren, ohne Lesbarkeit zu opfern: „Studierende“, „Physikerinnen und Physiker“ (wie im Projekt üblich). |

Verboten sind zudem: Floskeln („In der heutigen Zeit“, „Wie wir alle wissen“),
rhetorische Fragen als Gliederungsersatz und Meta-Sätze über den Text selbst
(„In diesem Abschnitt wird gezeigt …“), sofern die Überschrift die Funktion schon
erfüllt.

## 4. Aufbau einer Lektion

Die Reihenfolge ist verbindlich, sofern der Abschnitt nicht bereits anders
strukturiert ist:

1. **Titel** als `#`-Überschrift: `# Lektion N: Thema` (ohne Punkt am Ende).
2. **Lernziele** in einer eigenen Zelle mit hellgelbem Hintergrund und gelbem Rand:
   „Nach dieser Lektion können Sie …“ – drei bis fünf überprüfbare Ziele mit Verben
   („erklären“, „anwenden“, „implementieren“). Format siehe Abschnitt 4.3.
3. **Motivation:** ein konkretes Problem, das ohne das neue Konzept nicht lösbar ist.
4. **Definition oder Prinzip:** die Regel, das Konzept oder die Syntax.
5. **Beispiel:** lauffähiger, minimaler Code mit erwarteter Ausgabe.
6. **Übung:** eine Aufgabe mit steigendem Schwierigkeitsgrad und, falls sinnvoll,
   einer Lösung in einer separaten Zelle.
7. **Zusammenfassung:** eine Zelle mit hellgrünem Hintergrund und dunkelgrünem Rand,
   ohne Nummer, mit maximal fünf Bulletpoints, die die Kernaussagen wiederholen
   (Format siehe Abschnitt 4.2).

Abschnitte werden fortlaufend nummeriert (`## 1. Funktionen`, `### 1.1 Definition`).
Einzige Ausnahme ist die Zusammenfassung: Sie steht am Ende, trägt keine Nummer und
zählt nicht zur Abschnittsnummerierung.
Jeder Abschnitt beginnt mit einem Satz, der sein Ziel nennt, und endet mit einem
Ergebnis, das man prüfen kann.

### 4.1 Sonderfall Lektion 00

`Lektion 00: Wie benutze ich das Tutorial?` ist ein Orientierungsnotebook, keine
Lehrlektion. Für diese Datei gelten folgende Abweichungen:

- **Keine Lernziele** und **keine Zusammenfassung**.
- Direkt unter dem Titel steht eine Autorenzeile im Format
  `*Autor: Vorname Nachname*`, im Projekt also `*Autor: Oliver Cordes*`. In
  derselben Zelle folgen die Versionsangabe und der Fußnotenverweis
  (Format siehe Abschnitt 4.4).
- Aufbau: Titel → Autorenzeile → Lesehinweis mit Link zum Inhaltsverzeichnis →
  die Abschnitte 1 bis 3 → Inhaltsverzeichnis.
- Das Inhaltsverzeichnis ist der letzte Abschnitt und wird passend nummeriert
  (derzeit `## 4. Inhaltsverzeichnis`). Danach folgt als letzte Zelle die
  Fußnote zum Einsatz von KI-Werkzeugen (Abschnitt 4.4).
- Abschnitt 2 enthält die Legende der Zellfarben (`### 2.1 Legende der Zellfarben`):
  Gelb steht für die Lernziele, Grün für die Zusammenfassung.
- Die Abschnitte beschreiben die Bedienung des Tutorials; Motivation, Definition,
  Beispiel und Übung entfallen.

### 4.2 Format der Zusammenfassung

Die Zusammenfassung ist genau eine Markdown-Zelle und besteht aus einem HTML-Block:
hellgrüner Hintergrund (`#e8f5e9`), dunkelgrüner Rand (`2px solid #1b5e20`),
abgerundete Ecken und Innenabstand. Die Überschrift ist ein `<h2>` ohne Nummer, die
Punkte stehen in einer `<ul>`-Liste.

```html
<div style="background-color: #e8f5e9; border: 2px solid #1b5e20; border-radius: 6px; padding: 12px 18px;">
<h2 style="margin-top: 0;">Zusammenfassung</h2>
<ul>
 <li>Erster Merksatz mit <code>Code</code>.</li>
 <li>Zweiter Merksatz.</li>
</ul>
</div>
```

- Der Block enthält **keine Leerzeilen**: Markdown beendet einen HTML-Block an der
  ersten Leerzeile, danach stünde der Inhalt außerhalb des Rahmens.
- Inline-Code wird als `<code>…</code>` geschrieben, Sonderzeichen als `&amp;`,
  `&lt;` und `&gt;`. Markdown-Syntax wie `` `…` `` oder `*…*` wirkt im Block nicht.
- Auf Formeln wird verzichtet; Fachbegriffe werden ausgeschrieben.
- Vor dem Block steht eine Trennlinie, danach folgt nichts mehr: keine Trennzelle,
  keine leere Zelle. Der Block ist die letzte Zelle der Lektion.

### 4.3 Format der Lernziele

Die Lernziele stehen in einer eigenen Markdown-Zelle: ein HTML-Block mit hellgelbem
Hintergrund (`#fffde7`) und gelbem Rand (`2px solid #f9a825`), mit denselben Ecken
und demselben Innenabstand wie die Zusammenfassung. Die Überschrift ist ein `<h2>`
ohne Nummer; darunter stehen der Satz „Nach dieser Lektion können Sie:“ und drei bis
fünf Punkte.

```html
<div style="background-color: #fffde7; border: 2px solid #f9a825; border-radius: 6px; padding: 12px 18px;">
<h2 style="margin-top: 0;">Lernziele</h2>
<p>Nach dieser Lektion können Sie:</p>
<ul>
 <li>Erstes Ziel mit <code>Code</code>,</li>
 <li>Zweites Ziel.</li>
</ul>
</div>
```

- Für den Block gelten dieselben Regeln wie in Abschnitt 4.2: keine Leerzeilen,
  Inline-Code als `<code>…</code>`, Sonderzeichen maskiert.
- Vor der Zelle steht eine eigene Trennzelle mit `---`; dahinter folgt direkt die
  Zelle mit dem Inhaltsverzeichnis (`**Inhalt**` und den Links), ohne Trennlinie.

### 4.4 Version und Fußnote

Unter dem Titel steht eine Markdown-Zelle mit Autorenzeile, Versionsangabe und
Fußnotenverweis. Die Version wird aus dem letzten Git-Commit erzeugt und als Text
gespeichert; beim Lesen muss keine Zelle ausgeführt werden.

```html
<!-- version:start -->
*Autor: Oliver Cordes* · *Version: `f2745f5` vom 18.10.2026*<sup><a href="#fussnote-ki">1</a></sup>
<!-- version:end -->
```

- Die Zeile wird **nicht von Hand** gepflegt, sondern mit
  `python3 tools/update_version.py` aus der Kurz-ID (`git log -1 --format=%h`)
  und dem Commit-Datum (`%cs`, ausgegeben als `TT.MM.JJJJ`) erzeugt.
- `python3 tools/update_version.py --check` prüft die Zeile ohne zu schreiben und
  endet bei einer Abweichung mit Exit-Code 1.
- Die Marker `<!-- version:start -->` und `<!-- version:end -->` begrenzen den
  Bereich, den das Skript ersetzt; sie werden nicht gerendert.
- Beim Binder-Build ruft `.binder/postBuild` das Skript vor dem Aufräumen auf.
  Die ausgelieferte Fassung trägt damit den Commit, aus dem das Image gebaut wurde.
- Die Angabe nennt den Commit, auf dem der Stand beruht. Wer die Lektion ändert,
  aktualisiert die Zeile anschließend; der eigene Commit ist darin noch nicht
  enthalten, weil eine Datei ihren eigenen Hash nicht tragen kann.

Die Fußnote steht am Dokumentende, getrennt durch eine eigene `---`-Zelle:

```html
<small id="fussnote-ki"><sup>1</sup> Bei der Erstellung dieses Tutorials haben KI-Werkzeuge Texte überarbeitet und Codebeispiele erstellt. Die fachliche Prüfung der Inhalte liegt beim Autor. Die Versionsangabe nennt den Git-Commit, auf dem der Stand dieses Notebooks beruht.</small>
```

- Der Verweis `<sup><a href="#fussnote-ki">1</a></sup>` steht in der Autorenzeile.
- Die Fußnote ist die letzte Zelle des Dokuments; das Inhaltsverzeichnis bleibt
  der letzte Abschnitt davor.
- Keine Code-Zelle und kein `!git`-Aufruf: Die Angaben stehen als fester Text im
  Notebook und sind ohne Ausführen einer Zelle sichtbar.

## 5. Formatierung (bestehende Konventionen beibehalten)

- Markdown-Zellen werden durch `---`-Zeilen voneinander getrennt.
- Nach jedem Abschnitt steht genau eine eigene Markdown-Zelle mit `---`, ebenso
  zwischen dem letzten Abschnitt und der Zusammenfassung. Nach der Zusammenfassung
  folgt keine Linie und keine leere Zelle.
- Hervorhebungen sparsam und bedeutungstragend:
  `**fett**` für Merksätze und zentrale Begriffe, *kursiv* für Fachbegriffe und
  fremdsprachige Ausdrücke, `` `Code` `` für Bezeichner, Pfade und Literale.
- Aufzählungen mit ` * ` (Leerzeichen, Stern, Leerzeichen), Verschachtelung mit
  vier Leerzeichen.
- Codeblöcke immer mit Sprachkennung (`python`).
- Verweise auf Abschnitte über die vorhandenen Anker (`<a id=...></a>`) und
  `[Text](#anker)`; Anker und Inhaltsverzeichnisse beim Überarbeiten **nicht**
  umbenennen, sonst brechen die Links.
- Formeln als LaTeX (`$...$`, `$$...$$`), Symbole nur nach Definition verwenden.

## 6. Überarbeitungs-Workflow

1. **Befund:** Ziele des Abschnitts, Zielgruppe und vorhandene Begriffe aus dem
   Umfeld lesen (vorherige und nächste Lektion).
2. **Struktur vor Formulierung:** Gliederung prüfen, bevor einzelne Sätze
   umgeschrieben werden.
3. **Überarbeiten:** Regeln aus Abschnitt 3 und 4 anwenden; Inhalt verdichten statt
   aufblähen. Länge nur erhöhen, wenn eine Erklärung tatsächlich fehlt.
4. **Fachlich prüfen:** Jede Aussage muss korrekt, jede Codezeile ausführbar und
   jede Ausgabe plausibel sein. Bei Unsicherheit nachfragen statt raten.
5. **Konsistenz prüfen:** Begriffe, Anker, Querverweise, Nummerierung und
   Schreibweisen (z. B. „NumPy“) im gesamten Dokument abgleichen.
6. **Gegenlesen:** Text ohne Kontext lesen – versteht man ihn in einem Durchgang?
7. **Prüfungen:** Neue Prüfskripte liegen als `tools/checks/check_*.py` im
   Repository. `python3 tools/checks/check_all.py` findet sie automatisch und
   führt sie ohne Argumente aus; Prüfskripte außerhalb dieses Verzeichnisses
   werden nicht verwendet.

## 7. Grenzen

- **Keine inhaltlichen Änderungen ohne Auftrag.** Beim reinen Überarbeiten bleiben
  Aussagen, Beispiele, Zahlen und Code-Semantik erhalten.
- **Code nicht umformatieren**, wenn nur der Text überarbeitet werden soll.
- **Zellausgaben nicht löschen** und keine neuen Zellen einfügen, wenn das den
  Ablauf des Notebooks verändert.
- **Keine erfundenen Quellen, Messwerte oder Bibliotheksfunktionen.** Unsichere
  Angaben werden als offene Frage markiert.
- Bestehende Rechtschreibung wird korrigiert (neue deutsche Rechtschreibung),
  bestehende inhaltliche Eigenheiten des Projekts bleiben unangetastet.

## 8. Beispiele: vorher → nachher

**Vorher**
> Wie wir alle wissen, ist es total einfach, eine Funktion zu schreiben. Man kann
> den Code dann immer wieder benutzen und muss ihn nicht dauernd neu tippen.

**Nachher**
> Eine *Funktion* fasst Code zusammen, der mehrfach ausgeführt werden soll. Statt
> denselben Quelltext zu wiederholen, definieren Sie ihn einmal und rufen ihn über
> seinen Namen auf.

**Vorher**
> Hier wird jetzt gezeigt, wie man Listen benutzt. Das ist quasi ein Container, wo
> man mehrere Sachen reinpacken kann.

**Nachher**
> Eine *Liste* speichert mehrere Werte in einer festen Reihenfolge. Der Zugriff
> erfolgt über einen Index, der bei `0` beginnt:
>
> ```python
> zahlen = [3, 1, 4]
> zahlen[0]  # 3
> ```

## 9. Prüfliste vor Abgabe

- [ ] Lernziele vorhanden und überprüfbar formuliert (außer Lektion 00).
- [ ] Sie-Form durchgehend, keine Umgangssprache, keine Floskeln.
- [ ] Fachbegriffe bei der ersten Verwendung kursiv und erklärt.
- [ ] Jede Codezeile ausführbar, jede Ausgabe korrekt.
- [ ] Anker, Links und Nummerierung unverändert und funktionsfähig.
- [ ] Lernziele in eigener Zelle, hellgelb hinterlegt und gelb umrandet, mit drei bis
      fünf prüfbaren Zielen.
- [ ] Zusammenfassung in einer Zelle, hellgrün hinterlegt, dunkelgrün umrandet, ohne
      Nummer und mit höchstens fünf Punkten.
- [ ] In Lektion 00: Legende der Zellfarben in Abschnitt 2.
- [ ] Trennlinie nach jedem Abschnitt; nach der Zusammenfassung weder Linie noch
      leere Zelle.
- [ ] In Lektion 00: Autorenzeile `*Autor: Oliver Cordes*` mit Versionsangabe
      direkt unter dem Titel; `python3 tools/update_version.py --check` endet mit 0.
- [ ] In Lektion 00: Fußnote zum Einsatz von KI-Werkzeugen als letzte Zelle.
- [ ] Neue Prüfskripte liegen unter `tools/checks/check_*.py` und laufen über
      `python3 tools/checks/check_all.py`.
- [ ] Terminologie im Dokument einheitlich.
- [ ] Abschnitte enden mit einem prüfbaren Ergebnis.
- [ ] Keine inhaltlichen Änderungen ohne Auftrag.
