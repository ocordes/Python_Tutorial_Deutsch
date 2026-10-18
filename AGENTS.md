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
2. **Lernziele** als Liste: „Nach dieser Lektion können Sie …“ – drei bis
   fünf überprüfbare Ziele mit Verben („erklären“, „anwenden“, „implementieren“).
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
  `*Autor: Vorname Nachname*`, im Projekt also `*Autor: Oliver Cordes*`.
- Aufbau: Titel → Autorenzeile → Lesehinweis mit Link zum Inhaltsverzeichnis →
  die Abschnitte 1 bis 3 → Inhaltsverzeichnis.
- Das Inhaltsverzeichnis ist der letzte Abschnitt und wird passend nummeriert
  (derzeit `## 4. Inhaltsverzeichnis`).
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
- Der Block ist die letzte inhaltliche Zelle der Lektion; danach stehen höchstens
  noch eine Trennzelle mit `---` und leere Zellen.

## 5. Formatierung (bestehende Konventionen beibehalten)

- Markdown-Zellen werden durch `---`-Zeilen voneinander getrennt.
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
- [ ] Zusammenfassung in einer Zelle, hellgrün hinterlegt, dunkelgrün umrandet, ohne
      Nummer und mit höchstens fünf Punkten.
- [ ] In Lektion 00: Autorenzeile `*Autor: Oliver Cordes*` direkt unter dem Titel.
- [ ] Terminologie im Dokument einheitlich.
- [ ] Abschnitte enden mit einem prüfbaren Ergebnis.
- [ ] Keine inhaltlichen Änderungen ohne Auftrag.
