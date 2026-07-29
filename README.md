
# 🧠 LLM-Claude-Skills-etc

Eine kuratierte Sammlung eigener **Claude Skills** und **Gemini Gems** rund um die FIAE/FISI-Umschulung, IT-Prüfungsvorbereitung und praktische LLM-Workflows – inklusive Kurzanleitungen zur Einrichtung.

---

## 📁 Repo-Struktur

```
LLM-Claude-Skills-etc/
├── Claude_Skills/
│   ├── IT_Bewerbungscoach_2026.md
│   └── Wiki_FIAE.md
├── Gemini_Gems/
│   ├── EduScrum_Transformer.md
│   ├── IT_Sicherheitsarchitekt_Markus_Weber.md
│   ├── Persönlicher_Python_Lehrer_Ruffy.md
│   ├── Research_Agent_für_AE-_und_FISI_Umschüler_innen.md
│   ├── Visual_Mastermind.md
│   └── akademischer_Recherche_Assistent_für_mathematische_Konzepte.md
├── Kurzanleitung_Claude_Skills.md
├── Kurzanleitung_Gemini_Gems.md
├── LICENSE
└── README.md
```

---

## 🚀 Schnellstart

| Ich möchte... | Anleitung |
|---|---|
| Einen Claude Skill einrichten/nutzen | [`Kurzanleitung_Claude_Skills.md`](./Kurzanleitung_Claude_Skills.md) |
| Ein Gemini Gem einrichten/nutzen | [`Kurzanleitung_Gemini_Gems.md`](./Kurzanleitung_Gemini_Gems.md) |

---

## 🤖 Claude Skills

Skills liegen im `.md`-Format mit YAML-Frontmatter (`name` + `description`) vor und können direkt in Claude importiert werden (siehe Kurzanleitung oben).

| Skill | Zweck | Trigger-Beispiele |
|---|---|---|
| **[`it-bewerbungscoach-2026`](./Claude_Skills/IT_Bewerbungscoach_2026.md)** | Bewerbungscoach für IT-Umschüler (FIAE/FISI) mit ATS-Optimierung, Recruiter-Logik und Positionierung als automatisierungs-/DevOps-affiner Anwendungsentwickler | Lebenslauf erstellen/überarbeiten, Anschreiben, GitHub/LinkedIn-Profiltexte |
| **[`wiki-fiae`](./Claude_Skills/Wiki_FIAE.md)** | Erstellt und prüft Wiki-Artikel im FIAE/FISI-Prüfungsformat (Typ A: kompakter Prüfungs-Wiki / Typ B: mathematischer Deep Dive) inkl. ROT/GELB/GRÜN-IHK-Relevanz-Markierung | "Wiki-Artikel zu [Thema]", "Deep Dive mit ROT/GELB/GRÜN", "Prüf diesen Wiki-Eintrag" |

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

Entstanden im Rahmen der FIAE-Umschulung am Dualis-Institut Hamburg – als praktische Werkzeugsammlung für IHK-Prüfungsvorbereitung, Bewerbungsprozess und LLM-gestützte Lernbegleitung.

## 📄 Lizenz

[MIT](./LICENSE)
