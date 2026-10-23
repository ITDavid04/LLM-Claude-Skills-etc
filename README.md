
# 🧠 LLM-Claude-Skills-etc

Eine kuratierte Sammlung eigener **Claude Skills** und **Gemini Gems** rund um die FIAE/FISI-Umschulung, IT-Prüfungsvorbereitung, Bewerbung und praktische LLM-Workflows, dazu Recherche-Prompts und Kurzanleitungen zur Einrichtung.

---

## 📁 Repo-Struktur

```
LLM-Claude-Skills-etc/
├── Claude_Skills/
│   ├── Firmen-briefing-fiae.md
│   ├── IT_Bewerbungscoach_2026.md
│   ├── Lockeres_Lernmaterial/
│   │   ├── Locker.md
│   │   └── Referenzen/
│   ├── Natuerliche_Konversation/
│   │   ├── natürlich.md
│   │   └── Referenzen/
│   ├── praktikanten_search_v5.md
│   ├── Token_Sparmodus/
│   │   ├── token-sparmodus.md
│   │   ├── installieren.sh
│   │   ├── Referenzen/
│   │   └── Werkzeuge/projekt-karte.py
│   ├── Wiki_FIAE.md
│   ├── Workflow-Wiki-FIAE.md
│   └── workshop-planer-2026.md
├── Gemini_Gems/
│   ├── EduScrum_Transformer.md
│   ├── IT_Sicherheitsarchitekt_Markus_Weber.md
│   ├── Persönlicher_Python_Lehrer_Ruffy.md
│   ├── Research_Agent_für_AE-_und_FISI_Umschüler_innen.md
│   ├── Visual_Mastermind.md
│   └── akademischer_Recherche_Assistent_für_mathematische_Konzepte.md
├── Kurzanleitung_Claude_Skills.md
├── Kurzanleitung_Gemini_Gems.md
├── Recherche_Prompt_Beispiel.md
├── Recherche_Promt_Leer.md
├── LICENSE
└── README.md
```

---

## 🚀 Schnellstart

| Ich möchte... | Anleitung |
|---|---|
| Einen Claude Skill einrichten/nutzen | [`Kurzanleitung_Claude_Skills.md`](./Kurzanleitung_Claude_Skills.md) |
| Ein Gemini Gem einrichten/nutzen | [`Kurzanleitung_Gemini_Gems.md`](./Kurzanleitung_Gemini_Gems.md) |
| Eine Recherche mit einer KI sauber aufsetzen | [`Recherche_Promt_Leer.md`](./Recherche_Promt_Leer.md) |

---

## 🤖 Claude Skills

Skills liegen im `.md`-Format mit YAML-Frontmatter (`name` + `description`) vor und können direkt in Claude importiert werden (siehe Kurzanleitung oben). Liegt ein Skill in einem eigenen Ordner, gehören die Unterordner `Referenzen/` und `Werkzeuge/` mit dazu: Die Hauptdatei verweist auf sie und lädt sie nur bei Bedarf nach.

### 📚 Lernen und Wiki

| Skill | Zweck | Trigger-Beispiele |
|---|---|---|
| **[`wiki-fiae`](./Claude_Skills/Wiki_FIAE.md)** | Erstellt und prüft Wiki-Artikel im FIAE/FISI-Format mit ROT/GELB/GRÜN-IHK-Relevanz-Markierung. Drei Typen: kompakter Prüfungs-Wiki (A), mathematisch-technischer Deep Dive (B) und Infomaterial ohne Prüfungsbezug (C, nur auf ausdrücklichen Wunsch) | „Wiki-Artikel zu [Thema]", „Deep Dive mit ROT/GELB/GRÜN", „Prüf diesen Wiki-Eintrag" |
| **[Workflow Wiki-FIAE](./Claude_Skills/Workflow-Wiki-FIAE.md)** | Kein eigener Skill, sondern die Arbeitsanweisung dazu: der Ablauf für neue Artikel, vom Entwurf über Web-Verifikation und eigene Reviews bis zu gewichteten externen Reviews | ergänzt `wiki-fiae` |
| **[`lockeres-lernmaterial`](./Claude_Skills/Lockeres_Lernmaterial/Locker.md)** | Schreibt Lernmaterial, das sich gern liest, ohne an fachlicher Genauigkeit zu verlieren: Erklärtexte, Übungen, Aufgabenreihen mit gemeinsamer Welt. Der Spaß kommt aus Text und Aufbau, nicht aus Emojis. Mit Prüfliste, Stimme und Beispielen sowie Regeln für Reihen und Welten | „mach das lockerer", „klingt zu trocken", „bau daraus eine Aufgabenreihe" |
| **[`workshop-planer-2026`](./Claude_Skills/workshop-planer-2026.md)** | Copilot für Dozent:innen in der IT-Umschulung: erarbeitet im Dialog Workshop-Pläne mit Zeitraster, Agenda und Übungen, bei denen Blöcke und Pausen genau die verfügbare Zeit ergeben | „Workshop-Plan für [Thema], 4 Stunden", „Zeitraster für EduScrum" |

### 💼 Bewerbung und Praktikum

| Skill | Zweck | Trigger-Beispiele |
|---|---|---|
| **[`praktikanten-search`](./Claude_Skills/praktikanten_search_v5.md)** | Recherche-Assistent für Praktikums- und Umschulungsbewerbungen. Trennt belegte Fakten von Einschätzungen und übergibt die Ergebnisse strukturiert an den Bewerbungscoach | „Recherchier die Firma für meine Bewerbung", „passende Praktikumsbetriebe" |
| **[`it-bewerbungscoach-2026`](./Claude_Skills/IT_Bewerbungscoach_2026.md)** | Bewerbungscoach für IT-Umschüler (FIAE/FISI) mit ATS-Optimierung, Recruiter-Logik und Positionierung als automatisierungs-/DevOps-affiner Anwendungsentwickler | Lebenslauf erstellen/überarbeiten, Anschreiben, GitHub/LinkedIn-Profiltexte |
| **[`firmen-briefing-fiae`](./Claude_Skills/Firmen-briefing-fiae.md)** | Briefing vor dem Vorstellungsgespräch oder Praktikumseinsatz: Betriebs-Steckbrief, Arbeitgeberbewertungen (klar als subjektiv gekennzeichnet), Talking-Points, FIAE-Tätigkeitsfelder und erste Projektideen für die IHK-Prüfung. Schreibt bewusst kein Anschreiben | „Durchleuchte die Firma X", „Gesprächsvorbereitung Praktikumsbetrieb", „Projektideen für den Projektantrag" |

### ⚙️ Arbeiten mit Claude

| Skill | Zweck | Trigger-Beispiele |
|---|---|---|
| **[`natuerliche-konversation`](./Claude_Skills/Natuerliche_Konversation/natürlich.md)** | Macht Claudes Gesprächsführung im Chat natürlicher, anschlussfähiger und ehrlicher: Rückfragen, Frust, Widerspruch, gute Nachrichten, Abschlüsse. Mit Modi, Formulierungsbausteinen und einer Übersicht, was wie gut belegt ist | „Du klingst steif", „zu schmeichelnd", Gesprächsverhalten für einen Bot entwerfen |
| **[`token-sparmodus`](./Claude_Skills/Token_Sparmodus/token-sparmodus.md)** | Workflow gegen hohe Tokenkosten: eine Sitzung pro Video/Aufgabe, gezieltes Lesen per Projekt-Karte, Kontaktbogen statt vieler Screenshots, Render-Disziplin und Übergabe-Notiz für die nächste Sitzung. Mit Hyperframes-Videoworkflow, `projekt-karte.py` und `installieren.sh` für Claude Code | „spar Tokens", „neue Sitzung", „Übergabe schreiben", neues Video in alter Sitzung |

**Zusammenspiel:** `praktikanten-search` recherchiert, `it-bewerbungscoach-2026` schreibt daraus die Bewerbung, `firmen-briefing-fiae` bereitet aufs Gespräch vor. `lockeres-lernmaterial` ist für lange Texte da, `natuerliche-konversation` für Chat-Antworten.

**Token-Sparmodus in Claude Code installieren:**

```bash
bash Claude_Skills/Token_Sparmodus/installieren.sh ~/pfad/zum/projekt   # nur für ein Projekt
bash Claude_Skills/Token_Sparmodus/installieren.sh --global             # für alle Projekte
```

---

## 💎 Gemini Gems

Gems sind reine System-Prompts, die im Gemini Gem Manager als Instructions eingefügt werden (siehe Kurzanleitung oben).

| Gem | Zweck |
|---|---|
| **[EduScrum Transformer](./Gemini_Gems/EduScrum_Transformer.md)** | Verwandelt EduScrum-Stories in motivierende Lern-Abenteuer |
| **[IT-Sicherheitsarchitekt Markus Weber](./Gemini_Gems/IT_Sicherheitsarchitekt_Markus_Weber.md)** | Persona-basierte IT-Sicherheitsberatung zu Cloud-Migration, Supply-Chain-Security und Phishing-Risiken (DSGVO, OWASP Top 10) |
| **[Persönlicher Python-Lehrer "Ruffy"](./Gemini_Gems/Persönlicher_Python_Lehrer_Ruffy.md)** | Geduldiger Python-Tutor für Anwendungsentwickler-Umschüler mit Fokus auf Clean Code und Alltagsanalogien |
| **[Research Agent für AE-/FISI-Umschüler:innen](./Gemini_Gems/Research_Agent_für_AE-_und_FISI_Umschüler_innen%20.md)** | Lernbegleiter für Recherche, Prüfungsvorbereitung und Job-Praxis mit Alltagsanalogien |
| **[Visual Mastermind](./Gemini_Gems/Visual_Mastermind.md)** | Master Visual Strategist für die Erarbeitung von Präsentationen (Management-Beratungs-Stil) |
| **[Akademischer Recherche-Assistent für mathematische Konzepte](./Gemini_Gems/akademischer_Recherche_Assistent_für_mathematische_Konzepte%20.md)** | Fundierte, quellenbasierte Erklärungen mathematischer Konzepte mit Praxisbezug zur Softwareentwicklung |

---

## 🔎 Recherche-Prompts

Eine Vorlage für gründliche Recherchen mit einer beliebigen KI: Thema und Recherche-Punkte eintragen, die KI arbeitet sie der Reihe nach ab, belegt Aussagen mit Quellen und trennt gesichertes Wissen von Annahmen und Spekulation.

| Datei | Inhalt |
|---|---|
| **[Recherche_Promt_Leer.md](./Recherche_Promt_Leer.md)** | Leere Vorlage mit Platzhaltern für Thema und Punkte |
| **[Recherche_Prompt_Beispiel.md](./Recherche_Prompt_Beispiel.md)** | Ausgefülltes Beispiel: Vorbereitung eines EduScrum-Workshops in der IT-Umschulung |

---

## 🛠️ Formatierungsstandard für eigene Skills

Damit neue Claude Skills korrekt erkannt und per `/skill-name` aufgerufen werden, **muss** jede Datei mit YAML-Frontmatter beginnen:

```markdown
---
name: name-des-skills-in-kleinbuchstaben
description: "Kurze, präzise Beschreibung: was der Skill tut, wann er greifen soll."
---

# Titel des Skills

## Rollendefinition
## Regelwerk & Methodik
## Arbeitsmodus
```

Details dazu in [`Kurzanleitung_Claude_Skills.md`](./Kurzanleitung_Claude_Skills.md).

---

## 📌 Kontext

Entstanden im Rahmen der FIAE-Umschulung am Dualis-Institut Hamburg, als praktische Werkzeugsammlung für IHK-Prüfungsvorbereitung, Bewerbungsprozess und LLM-gestützte Lernbegleitung.

## 📄 Lizenz

[MIT](./LICENSE)
