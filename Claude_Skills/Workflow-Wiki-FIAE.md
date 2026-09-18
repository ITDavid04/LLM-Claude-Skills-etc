# Arbeitsanweisung: Standard-Workflow für neue Wiki-Artikel

> Ersetzt/ergänzt Abschnitt 6 ("Review-Workflow, der sich bewährt hat") im `Style-Guide_Wiki-FIAE.md`. Ab sofort gilt dieser Ablauf für jeden neuen LF8.x-Artikel, sofern nicht ausdrücklich anders vereinbart.

---

## Der Loop im Überblick

```text
1. Draft erstellen
      ↓
2. Web-Suche zur Verifikation (Normen, Versionsstände, Fachbegriffe, Datums-/Zahlenangaben)
      ↓
3. Dokument anpassen (falls nötig) + Konsistenz-Sweep (Schritt 3a)
      ↓
4. Eigene Review Nr. 1 (gegen Style-Guide-Checkliste, nicht nur Sprachgefühl)
      ↓
5. Dokument anpassen + Konsistenz-Sweep
      ↓
6. Externe Prüfung anfordern (mehrere unabhängige Reviews)
      ↓
7. Reviews GEGENPRÜFEN, dann lesen und GEWICHTEN (nicht alle gleich behandeln, siehe unten)
      ↓
8. Dokument überarbeiten + Konsistenz-Sweep
      ↓
9. Finale Review erbeten (Fokus vorgeben, siehe Schritt 9)
      ↓
10. Finale Review lesen
      ↓
11. Verbesserungen vornehmen + Konsistenz-Sweep → Status auf final NACH ausdrücklichem OK vom Auftraggeber
```

---

## Schritt-für-Schritt-Details

### 1. Draft erstellen
- Alle relevanten Rohdateien vollständig lesen (nicht nur überfliegen), bevor geschrieben wird.
- Format nach `wiki-fiae`-Skill (Typ A oder B) und `Style-Guide_Wiki-FIAE.md` von Anfang an mitdenken – spart eine ganze Review-Runde.
- Pflicht-Elemente-Checkliste (Style-Guide Abschnitt 5) bereits beim Schreiben abhaken, nicht erst danach.
- **Teilungsentscheidung (A/B vs. ein kompakter Artikel) vorab treffen, nicht reaktiv während des Schreibens.** Faustregel: Ab **3 oder mehr eigenständigen Unterthemen**, die jeweils eine eigene Typfrage, Prüfungsfalle und einen eigenen Cheatsheet-Block bräuchten, tendenziell splitten. Bei 1–2 Unterthemen oder wenn ein Unterthema (z. B. Existenzgründung) mangels Rohmaterial ohnehin kompakt bleiben muss, als ein Artikel halten. Im Zweifel: kompakt beginnen, erst splitten, wenn der Umfang beim Schreiben spürbar über den Typ-A-Rahmen hinauswächst.

### 2. Web-Suche zur Verifikation
- Gezielt bei: Normen/Standards (ISO, OMG/UML, DIN, RFC), Versionsangaben, Zahlen/Statistiken, Aussagen zu "aktuell gültig".
- **Verpflichtend, nicht optional, sobald das Rohmaterial Datums-, Grenzwert- oder Prognoseangaben enthält** (Gesetzesstände, Beitragsbemessungsgrenzen, Konjunkturdaten, EU-Richtlinien-Fristen o. ä.) – auch wenn das Rohmaterial "fertig bearbeitet" wirkt. Rohmaterial war wiederholt bereits beim Erstellen ein Jahr oder mehr veraltet (Beitragswerte, Konjunkturzahlen, EU-Reformen); das fällt nur durch aktive Recherche auf, nicht durchs bloße Lesen.
- Nicht nötig bei: reinem Lehrbuchwissen ohne Versionsbezug (z. B. Grundprinzip von ETL).
- Ergebnis direkt mit Quelle im Artikel vermerken (YAML `quellen_fachlich`).

### 3. Dokument anpassen
- Nur Korrekturen aus Schritt 2 einarbeiten, keine Scope-Erweiterung.

### 3a. Konsistenz-Sweep (nach JEDER inhaltlichen Korrektur, nicht nur einmal am Ende)
**Das häufigste Fehlermuster in bisherigen Artikeln:** Eine Aussage wird im Fließtext korrigiert, aber die gleiche fehlerhafte Formulierung lebt unverändert in Selbsttest, Cheatsheet, einer Musterantwort oder einer Prüfungsfalle weiter ("Haupttext korrigiert, Nebenstelle vergessen"). Das kostete in der WiSo-Serie wiederholt eine ganze zusätzliche Review-Runde.
- Nach jeder Korrektur: **gezielt nach dem alten Begriff/der alten Zahl/der alten Formulierung suchen** (grep über die gesamte Datei), nicht nur an der Korrekturstelle selbst weiterarbeiten.
- Explizit prüfen: Selbsttest, Cheatsheet, Prüfungsfallen, Merksätze, IHK-Typfragen/Musterantworten, YAML-Metadaten (`quellen_fachlich`, `review_historie`) – diese Stellen wiederholen Kernaussagen oft in eigenen Worten, daher hilft eine reine Textsuche nicht immer; bei zentralen Korrekturen alle diese Abschnitte einmal bewusst durchlesen.
- Diesen Sweep als eigenen kurzen Arbeitsschritt behandeln, nicht als gedankliches "Nebenbei" während der eigentlichen Korrektur.

### 4. Eigene Review Nr. 1
- **Nicht** nur auf Wohlklang/Verständlichkeit prüfen, sondern aktiv gegen die Style-Guide-Checkliste (Abschnitt 5) durchgehen – Punkt für Punkt, inklusive der leicht vergessbaren:
  - Fehlt "Typische Prüfungsfallen"?
  - Fehlt ein Rückverweis auf Deep-Dive-Themen aus dem Rohmaterial?
  - Ist die Lernzeit realistisch gestaffelt?
  - Sind Cheatsheet/Selbsttest/Merksätze konsistent mit evtl. bereits vorgenommenen Korrekturen?
- Auf sprachliche Absolutheiten prüfen (Style-Guide Abschnitt 1): "gilt immer", "ist dasselbe wie", unbelegte Zahlen.

### 5. Dokument anpassen
- Funde aus Schritt 4 einarbeiten.

### 6. Externe Prüfung anfordern
- Mehrere unabhängige Reviews einholen (unterschiedliche Perspektiven finden unterschiedliche Fehler).

### 7. Reviews gegenprüfen, lesen und gewichten

**Vor dem Gewichten: jede Behauptung über den Dateiinhalt selbst verifizieren.** Externe Reviews haben wiederholt Dinge behauptet, die beim Abgleich mit der tatsächlichen Datei nicht zutrafen – erfundene Markdown-Fehler, nicht existierende Links, sogar "Verifikationen" von Zahlen, die im Text gar nicht vorkamen. Bei jeder Behauptung der Form "Stelle X sagt Y" oder "Formatierungsfehler bei Z": kurz mit `grep`/direktem Blick in die Datei gegenchecken, bevor reagiert wird. Nicht bestätigte Behauptungen werden nicht umgesetzt und im `review_historie`-Eintrag kurz als "nicht bestätigt, nicht übernommen" vermerkt – das ist Teil der Transparenz, nicht optional.

**Nicht jede Review zählt gleich viel.** Kriterien zur Gewichtung:

| Signal | Einordnung |
| --- | --- |
| Review nennt konkrete, belegte Fachfehler mit Beispiel/Gegenbeispiel | Hoch gewichten, bevorzugt umsetzen |
| Review verweist auf Norm/Spezifikation/Quelle | Hoch gewichten |
| Review besteht überwiegend aus Sternebewertungen ohne neue inhaltliche Funde ("exzellent", "sehr gut" ohne Substanz) | Niedrig gewichten – liefert keine Handlungsanweisung, auch wenn wohlwollend |
| Review schlägt Scope-Erweiterung vor (neue Themen, Tools, die nicht im Rohmaterial stehen) | Kritisch prüfen, meist NICHT übernehmen – Typ-A-Rahmen nicht sprengen |
| Zwei Reviews widersprechen sich | Die mit Norm-/Fachreferenz bevorzugen, nicht die plausibler klingende; im Zweifel selbst nachrecherchieren statt zu raten |

- Explizit vermerken, welche Review-Punkte übernommen und welche bewusst verworfen wurden (Transparenz für den Auftraggeber).

### 8. Dokument überarbeiten
- Nur berechtigte Funde umsetzen (siehe Gewichtung).
- Danach: Konsistenz-Sweep wie in Schritt 3a beschrieben – nach Runde 2/3 besonders wichtig, weil hier meist mehrere Stellen gleichzeitig korrigiert werden und die Nebenstellen-Falle am größten ist.

### 9. Finale Review erbeten
- Kurz benennen, was seit der letzten Runde geändert wurde, damit die Review sich auf die relevanten Stellen konzentrieren kann.
- **Ab Runde 3:** Explizit um Fokussierung auf die wichtigsten verbliebenen Punkte bitten (z. B. "nur noch die 3 wichtigsten offenen Fachfehler, keine erneute Vollprüfung"). In der Praxis lieferten spätere Runden oft nur noch 1–3 echte neue Punkte bei gleichbleibend langem Review-Text – das kostet Zeit beim Auswerten, ohne den Ertrag zu erhöhen.

### 10. Finale Review lesen
- Gleiche Gewichtungslogik wie Schritt 7 anwenden.
- Prüfen: Sind das noch neue Fachfehler, oder nur noch Geschmacksfragen/Kosmetik?

### 11. Verbesserungen vornehmen und final setzen
- Nur wenn Schritt 10 **keine harten Fachfehler** mehr zutage fördert (Kosmetik/Optionales ist okay).
- Vor dem Setzen auf `final`: letzter Konsistenz-Sweep (Schritt 3a) über die gesamte Datei – Kopf, Mitte und Ende einmal komplett gegenlesen, nicht nur die zuletzt geänderten Stellen. In der Praxis fanden sich hier noch am ehesten übersehene Nebenstellen.
- Status wird **nie eigenständig** auf `final` gesetzt – immer erst nach explizitem OK des Auftraggebers.
- YAML `review_historie` mit allen Runden (Datum, Ergebnis) fortschreiben – dokumentiert den Prozess nachvollziehbar. **Kompakt halten, nicht vollständig ausformulieren:** Ein bis drei Sätze pro Runde, nur die wichtigsten Korrekturen stichpunktartig (nicht jede Einzeländerung mit Begründung, Quelle und Fundstelle ausbreiten) – die vollständige Herleitung steht ohnehin schon im Artikeltext selbst. Faustregel: Wenn ein `ergebnis`-Feld mehr als ca. 400–500 Zeichen braucht, ist es zu ausführlich; auf die 2–4 wirklich wichtigen Punkte kürzen, Rest weglassen. Grund: Die Blöcke wurden in der Praxis (WiSo-Serie, LF5.1/5.4/5.5) mit mehreren Tausend Zeichen pro Runde unübersichtlich groß, ohne dass der Detailgrad für den eigentlichen Zweck (Nachvollziehbarkeit des Prozesses) nötig war.

---

## Abbruch-/Wiederholungskriterien

- **Weitere Loop-Runde nötig**, wenn eine Review strukturelle Lücken (fehlende Pflichtelemente) oder echte Fachfehler findet – auch wenn das Gesamturteil positiv klingt.
- **Loop kann enden**, wenn zwei aufeinanderfolgende Runden nur noch optionale/kosmetische Vorschläge liefern und keine neuen Fachfehler.
- **Loop endet immer auch dann, wenn der Auftraggeber explizit sein OK gibt** – unabhängig vom Review-Stand. Das Auftraggeber-OK ist ein eigenständiges, jederzeit gültiges Abbruchkriterium und übersteuert die anderen Kriterien; auf `final` wird ausschließlich nach diesem OK gesetzt (siehe Schritt 11).
- Bei sich wiederholenden, bereits abgelehnten Vorschlägen (z. B. Scope-Erweiterungen) nicht erneut diskutieren, sondern kurz auf die vorherige Begründung verweisen.

---

```yaml
dokument: workflow-wiki-fiae
zweck: "Standardisierter Erstellungs- und Review-Loop für LF8.x- und WiSo-Wiki-Artikel"
ersetzt: "Style-Guide_Wiki-FIAE.md Abschnitt 6"
stand: 2026-09-11
gueltig_ab: "LF8.4"
aenderung_2026-09-11: "Ergänzt auf Basis der WiSo-Serie (WiSo 1-5, 7 Artikel, je 3-4 Review-Runden): Teilungsentscheidung als Faustregel in Schritt 1; Web-Verifikation bei Datums-/Zahlenbezug als Pflicht statt optional in Schritt 2; neuer Schritt 3a 'Konsistenz-Sweep' gegen das häufigste Fehlermuster ('Haupttext korrigiert, Nebenstelle vergessen'); explizite Gegenprüfung von Review-Behauptungen gegen die tatsächliche Datei in Schritt 7; Fokussierungshinweis für Reviews ab Runde 3 in Schritt 9."
aenderung_2026-09-11_2: "Nach LF5.1/5.4/5.5 (Review-Blöcke wuchsen auf mehrere Tausend Zeichen pro Runde): review_historie-Format in Schritt 11 auf kompakte Stichpunkte (1-3 Sätze, max. ca. 400-500 Zeichen pro Runde) umgestellt statt vollständig ausformulierter Detailparagraphen."
```
