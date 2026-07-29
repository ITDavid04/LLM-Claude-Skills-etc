---
name: wiki-fiae
description: >
  Erstellt und prüft Wiki-Artikel im FIAE/FISI-Umschulungs-Format für das
  Dualis-Institut/Syntax Hamburg. Verwende diese Skill immer wenn der User einen
  neuen Wiki-Artikel erstellen will, einen bestehenden Artikel prüfen/reviewen
  lassen will, oder Inhalte "im Wiki-Format" oder "als Wiki-Eintrag" haben
  möchte. Auch triggern bei Begriffen wie "Lernwiki", "IHK-Wiki",
  "Prüfungswiki", "Deep Dive" oder wenn explizit nach ROT/GELB/GRÜN-Markierung
  gefragt wird. Die Skill gilt für beide Dokumenttypen: kompakte Prüfungswikis
  (wie LF7.x-Artikel) UND mathematisch/technische Deep-Dive-Artikel (wie
  L'Hospital oder algorithmische Komplexität).
---
 
# Wiki FIAE/FISI – Skill
 
## Zielgruppe & Kontext
 
- **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr, Dualis-Institut Hamburg
- **Zweck:** IHK-Prüfungsvorbereitung (AP1 schriftlich + Fachgespräch)
- **Ton:** Direkt, zugänglich, analogiebasiert – keine unnötige Fachsprache
---
 
## Zwei Dokumenttypen
 
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
 
## Universelle Qualitätsregeln (beide Typen)
 
### Inhalt
- Jede Behauptung mit IHK-Relevanz kennzeichnen
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
4. **IHK-Relevanz** – Ist die ROT/GELB/GRÜN-Einstufung korrekt?
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
 
