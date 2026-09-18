---
name: wiki-fiae
description: >
  Erstellt und prüft Wiki-Artikel im FIAE/FISI-Umschulungs-Format für das
  Dualis-Institut Hamburg. Verwende diese Skill immer wenn der User einen
  neuen Wiki-Artikel erstellen will, einen bestehenden Artikel prüfen/reviewen
  lassen will, oder Inhalte "im Wiki-Format" oder "als Wiki-Eintrag" haben
  möchte. Auch triggern bei Begriffen wie "Lernwiki", "IHK-Wiki",
  "Prüfungswiki", "Deep Dive" oder wenn explizit nach ROT/GELB/GRÜN-Markierung
  gefragt wird. Die Skill gilt für drei Dokumenttypen: kompakte Prüfungswikis
  (wie LF7.x-Artikel), mathematisch/technische Deep-Dive-Artikel (wie
  L'Hospital oder algorithmische Komplexität) sowie reines Infomaterial ohne
  Prüfungsbezug (Typ C) – Typ C aber NUR, wenn der User wörtlich "Nutze Typ C"
  oder "Typ C Infomaterial" schreibt, niemals durch Schlagwort-Interpretation.
---

# Wiki FIAE/FISI – Skill

## Zielgruppe & Kontext

- **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr, Dualis-Institut Hamburg
- **Zweck:** IHK-Prüfungsvorbereitung (AP1 schriftlich + Fachgespräch)
- **Ton:** Direkt, zugänglich, analogiebasiert – keine unnötige Fachsprache

---

## Drei Dokumenttypen

### Typ A – Kompakter Prüfungs-Wiki (thematisch, z.B. LF7.x)

Für systemische IT-Themen mit Praxisbezug (IoT, Netzwerk, Cloud, Security etc.).

**Pflicht-Elemente:**

1. **Kopfzeile / Frontmatter-Block**
   ```
   > **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
   > **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
   > **Lernzeit:** Ca. XX–XX Minuten
   > **Status:** Draft / Final
   > **Stand:** Jahr
   ```

2. **IHK-Kernfragen-Tabelle** (5 Fragen mit Sprungmarken zu Abschnitten)

3. **Nummerierte Hauptabschnitte** mit:
   - Einleitendes Grundprinzip als Blockquote (prägnanter Merksatz)
   - Unterabschnitte (1.1, 1.2 …)
   - Tabellen mit Spalten: Aspekt / Beschreibung / IHK-Relevanz
   - IHK-Relevanz-Emoji in Tabellen: 🔴 Prüfungsstoff / 🟡 Kontextwissen / 🟢 Nice to know
   - IHK-Typfragen als Blockquote mit direkter Musterantwort

4. **Zyklus-/Vergleichsdiagramme** (ASCII oder Mermaid) wo sinnvoll

5. **Selbsttest-Tabelle** (5 Fragen + Kurzantworten)

6. **IHK-Cheatsheet** (10 Begriffe + Kurzdefinitionen)

7. **Prüfungstaktik-Tabelle** (Aufgabentyp / Formulierung / Was IHK hören will)

8. **Merk-Sätze** (3–5 Blockquotes für mündliche Prüfung)

9. **Metadaten-Block** (YAML-Codeblock am Ende)

---

### Typ B – Deep Dive / Mathematisch-technischer Artikel (z.B. L'Hospital, O-Notation)

Für Themen mit mathematischem oder algorithmischem Schwerpunkt.

**Pflicht-Elemente:**

1. **Kurze Einleitung** – Was ist das Thema, wann braucht man es?

2. **Einfache Erklärung** – Analogie aus IT-Kontext (bevorzugt: O-Notation, Laufzeiten, Algorithmen)

3. **Voraussetzungen / Wann anwenden?** – klare Bedingungen, keine Unschärfen

4. **Schritt-für-Schritt-Rezept** – nummerierte Schritte, reproduzierbar

5. **Praktische Aufgaben** (mind. 4–5) mit:
   - Hinweis: erst selbst rechnen
   - Wo sinnvoll: mehrere Lösungswege anbieten

6. **Sidefacts mit IHK-Relevanz** (ROT / GELB / GRÜN als Fetttext-Label, nicht Emoji)
   - ROT = hochrelevant für IHK
   - GELB = mittelwichtig
   - GRÜN = nice to know

7. **Typische Fehler / Prüfungsfallen** (mit Relevanz-Label)

8. **Lösungen** (vollständig, alle Schritte ausgeschrieben)

---

### Typ C – Infomaterial (kein Lernmaterial, kein Prüfungsbezug)

**Trigger-Regel (verbindlich, kein Ermessensspielraum):**
Typ C wird ausschließlich verwendet, wenn der User es explizit und wörtlich anfordert
(z.B. "Nutze Typ C", "Typ C Infomaterial"). Formulierungen wie "ohne IHK-Fokus",
"nur Info" oder "kein Prüfungsbezug" lösen Typ C NICHT automatisch aus – das sind
keine Trigger, sondern höchstens ein Hinweis, dass beim User nachgefragt werden
sollte, ob Typ C gemeint ist. Ohne den expliziten Typ-C-Befehl gilt der Default:
Typ A oder Typ B je nach Thema, inklusive IHK-Relevanz-Markierung.

Für reine Wissens-/Übersichtsartikel ohne IHK-Prüfungsbezug – z.B. Konzepte,
Methoden oder Themen, die zum Verständnis beitragen, aber nicht klassifiziert
oder prüfungsrelevant markiert werden sollen.

**Zwei Ausprägungen (User gibt vor, welche gewünscht ist; im Zweifel nachfragen):**
- **Einfach** – kompakte Übersicht: Kernidee, zentrale Begriffe/Rollen/Bausteine,
  kurzes Fazit
- **Ausführlich** – mehr Tiefe und Abschnitte (z.B. Vor-/Nachteile, Praxisbezug,
  typische Herausforderungen), aber weiterhin ohne die Typ-A/B-Prüfungselemente

**Pflicht-Elemente:**

1. **Titel + kurze Einleitung** – was ist das Thema, worum geht es
2. **Klar gegliederte Hauptabschnitte** (Überschriften, ggf. Tabellen), sachlich
   und verständlich, Fachbegriffe kurz erklärt
3. **Kurzes Fazit / Zusammenfassung** am Ende

**Ausdrücklich NICHT enthalten in Typ C:**
- Keine IHK-Relevanz-Markierung (🔴🟡🟢 oder ROT/GELB/GRÜN)
- Keine Kopfzeile mit Prüfungsrelevanz/Lernzeit
- Keine IHK-Kernfragen-Tabelle, kein Selbsttest, kein Cheatsheet, keine
  Prüfungstaktik-Tabelle, keine Merk-Sätze
- Keine Studien-/Quellenzitate im Fließtext (z.B. "[4][14]") und keine Linkliste
- Kein KI-typischer Ausklang ("Wenn du magst, kann ich noch…")

---

## Universelle Qualitätsregeln (alle Typen, IHK-Relevanz nur A/B)

### Inhalt
- Bei Typ A/B: jede Behauptung mit IHK-Relevanz kennzeichnen. Bei Typ C: keine
  IHK-Relevanz-Markierung, siehe Typ-C-Abschnitt oben
- Keine unbegründeten Aussagen – immer "warum" mitliefern
- Fachbegriffe beim ersten Auftreten kurz erklären
- Analogien bevorzugen aus: Kochen, Handwerk, Logistik, Gärtnerei – was zur Zielgruppe passt (Quereinsteiger!)

### Mathematik / LaTeX (Typ B)
- Kurze Terme inline: `\(x^2\)`
- Längere Ausdrücke / Gleichungen als Block: `\[ ... \]`
- Kein gemischtes System innerhalb eines Abschnitts

### Tabellen
- Immer Header-Zeile mit **Fettschrift**
- Spalten konsequent durchhalten
- IHK-Relevanz als eigene Spalte oder Zeile

### Was NICHT ins Wiki gehört
- KI-Generierungsartefakte ("Wenn du magst, kann ich noch…")
- Redundante Infos (Legende nicht im Text wiederholen)
- Abschnitte ohne inhaltlichen Mehrwert

---

## Review-Modus (Prüfen eines bestehenden Artikels)

Wenn ein fertiger Artikel zur Prüfung vorgelegt wird:

1. **Fachliche Richtigkeit** – Sind alle Aussagen korrekt? Gibt es Unschärfen oder Fehler?
2. **Vollständigkeit** – Fehlen Pflicht-Elemente des jeweiligen Typs?
3. **Didaktik** – Ist die Erklärung für Quereinsteiger verständlich? Analogien vorhanden?
4. **IHK-Relevanz** (nur Typ A/B) – Ist die ROT/GELB/GRÜN-/🔴🟡🟢-Einstufung korrekt?
   Bei Typ C entfällt dieser Punkt vollständig.
5. **Format-Konsistenz** – LaTeX, Tabellen, Blockquotes konsistent?
6. **Artefakte** – KI-Formulierungen, Redundanzen, doppelte Inhalte?

Feedback strukturieren als:
- **Fachlich / Inhaltlich** (kritisch)
- **Didaktisch / Struktur** (empfohlen)
- **Kleinigkeiten** (optional)
- **Fazit** mit klarer Empfehlung

---

## Beispiele für Trigger-Prompts

- "Erstell mir einen Wiki-Artikel zu [Thema] im FIAE-Format"
- "Prüf mal diesen Wiki-Eintrag"
- "Ich brauche einen Deep Dive zu [Thema] mit Aufgaben und ROT/GELB/GRÜN"
- "Mach das im Wiki-Format für unsere Umschüler"
- "Kannst du das als IHK-Wiki aufbereiten?"
- "Nutze Typ C Infomaterial, einfache Ausarbeitung zu [Thema]" (einziger gültiger
  Typ-C-Trigger; "ohne IHK-Fokus" o.ä. allein reicht nicht aus)
