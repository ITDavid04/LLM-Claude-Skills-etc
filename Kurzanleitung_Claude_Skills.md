# ⚡ Claude Skills – Kurzanleitung

Skills sind modulare Anweisungen im Markdown-Format (`.md`), die Claude beibringen, wie er bestimmte Aufgaben ausführen soll.

---

## 🚀 Methode 1: Skill als `.md`-Datei importieren (Empfohlen)

Du kannst die `.md`-Dateien aus diesem Repository direkt in Claude als persistenten Skill hochladen und chatübergreifend nutzen.

1. **Datei herunterladen**  
   Lade die gewünschte `.md`-Skill-Datei aus diesem Repository auf deinen Computer herunter.

2. **Skill in Claude hinzufügen**  
   * Öffne [claude.ai](https://claude.ai).
   * Klicke unten links auf dein **Profil / Name** und gehe in die **Einstellungen (Settings)** oder **Styles & Skills**.
   * Wähle den Bereich **Skills** aus und klicke auf **Skill hinzufügen** (*Add Skill*).
   * Lade die `.md`-Datei hoch oder füge den Code direkt ein.

3. **Skill im Chat aufrufen**  
   * Starte einen neuen Chat.
   * **Automatisch:** Claude erkennt anhand deiner Anfrage selbstständig, wann er den passenden Skill aktivieren muss.
   * **Manuell:** Du kannst den Skill jederzeit gezielt mit `/` aufrufen (z. B. `/code-reviewer`).

---

## 💬 Methode 2: Direkt als System-Prompt in den Chat kopieren

Falls du keine Dateien hochladen möchtest oder schnell etwas testen willst:

1. Kopiere den Inhalt der `.md`-Datei aus dem Repository.
2. Starte einen neuen Chat auf [claude.ai](https://claude.ai).
3. Füge den Text als erste Nachricht ein (z. B. mit dem Vorstatz: *„Agiere ab sofort nach folgendem Skill:“*).
4. Nun arbeitet Claude für den Rest des Chats nach diesen Regeln.

---

## 💡 Tipp für das Repository

Damit die Skills sauber erkannt werden, sollten die Dateinamen prägnant sein (z. B. `code-reviewer.md` statt `mein_code_prompt_v2.md`), da Claude den Dateinamen oft als Aufruf-Kommando (`/code-reviewer`) übernimmt.

---

## ⚠️ WICHTIG: Der einzig richtige Formatierungsstandard für Claude Skills

Damit ein Skill von Claude fehlerfrei erkannt, parst und per `/skill-name` aufgerufen werden kann, **muss** die Markdown-Datei zwingend mit einem **YAML-Frontmatter-Header** beginnen!

### 📋 Der Pflicht-Aufbau eines Skills

Jede Skill-Datei muss wie folgt aufgebaut sein:

```markdown
---
name: name-des-skills-in-kleinbuchstaben
description: "Kurze, präzise Beschreibung, was der Skill tut, wann er angewendet werden soll und für welche Anwendungsfälle er gedacht ist."
---

# Titel des Skills

## Rollendefinition
[Hier wird die Rolle und Perspektive von Claude beschrieben]

## Regelwerk & Methodik
[Kriterien, Schritte, Do's and Don'ts]

## Arbeitsmodus
[Verhaltensanweisungen für die Interaktion mit dem Nutzer]


🎯 Worauf du beim Selbsterstellen achten musst:

    Frontmatter ist Pflicht: Die Dreifach-Striche --- ganz oben und nach der Description dürfen niemals fehlen.

    name: Nur Kleinbuchstaben, Zahlen und Bindestriche verwenden (keine Leerzeichen oder Sonderzeichen). Dies ist auch der Befehl für /name.

    description: Sehr detailliert beschreiben! Claude liest diese Beschreibung, um zu entscheiden, wann der Skill automatisch im Chat aktiviert werden soll.