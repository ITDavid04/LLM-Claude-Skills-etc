---
name: token-sparmodus
description: Workflow, der Tokenkosten senkt und Sitzungen effizienter macht, auf Deutsch. Nutze diese Skill, wenn es um Kosten, Tokenverbrauch, Kontextgröße, lange oder teure Sitzungen, Sitzungswechsel oder Übergaben geht, bei „/token-sparmodus", „spar Tokens", „das wird teuer", „neue Sitzung", „Übergabe schreiben" oder „Sitzung abschließen". Nutze sie auch von dir aus, wenn in einer bestehenden Sitzung ein neues Video oder eine neue, unabhängige Aufgabe beginnt, wenn ein Ergebnis fertig und committet ist, oder bevor du eine große Datei komplett lesen, einen Voll-Render starten oder einen Subagenten losschicken willst. Enthält einen Hyperframes-Videoworkflow und ein Werkzeug (projekt-karte.py), das eine Komposition auf eine kurze Karte mit Zeilennummern reduziert.
---

# Token-Sparmodus

**Kernidee:** Bei jeder Antwort liest das Modell den kompletten bisherigen Verlauf noch einmal mit. Die Kosten einer Antwort wachsen also mit der Länge der Sitzung, nicht mit der Länge der Frage. Eine kurze Frage am Ende einer langen Video-Sitzung kostet ein Vielfaches derselben Frage in einer frischen Sitzung.

Daraus folgen drei Hebel, nach Wirkung sortiert:

1. **Kurze Sitzungen:** eine Sitzung pro Video oder Aufgabe, danach Übergabe und Schluss.
2. **Gezielt lesen:** erst die Karte, dann nur die Zeilen, die gebraucht werden. Nie „zur Sicherheit" ganze Dateien.
3. **Knapp ausgeben:** Ergebnisse landen in Dateien und Commits, nicht als Code-Dump im Chat.

Wo die Person ausdrücklich etwas anderes will (alles lesen, ausführlich erklären), gilt ihr Wunsch. Qualität geht vor Sparen: lieber einmal richtig lesen als dreimal falsch editieren.

Pfade wie `Werkzeuge/…` und `Referenzen/…` beziehen sich auf den Ordner dieser Skill (in Claude Code: `.claude/skills/token-sparmodus/`).

## Der Workflow in fünf Phasen

### 1. Starten: frische Sitzung, klarer Auftrag
- **Eine Sitzung = ein Video / eine Aufgabe.** Ein neues Video in einer alten Sitzung schleppt den ganzen Verlauf des letzten Videos mit.
- Der erste Prompt enthält Ziel, Ordner, Vorlage/Stil, Format, Länge und wann es fertig ist. Vorlagen: `Referenzen/startprompts.md`.
- Gibt es eine Übergabe-Notiz (`NOTIZ.md` im Projektordner), wird nur sie gelesen, nicht der alte Verlauf rekonstruiert.

### 2. Orientieren: billig und gezielt
- **Erst die Karte:** `python3 Werkzeuge/projekt-karte.py <ordner>` liefert Dateien, Timeline mit Zeilennummern, Style-/Script-Bereiche und Abschnitts-Überschriften. Bei den bisherigen Videos sind das 1–2 KB statt 25–67 KB `index.html`.
- **Dann gezielt:** `sed -n '211,247p' index.html` für genau eine Szene, `grep -n` für einzelne Stellen.
- **Nie lesen:** `vendor/`, `fonts/`, `renders/`, `node_modules/`, minifizierte Dateien, Lockfiles, Binärdateien.
- **Skills dosiert:** Den Einstiegs-Skill laden, wenn er Pflicht ist, aber Referenzdateien eines Skills nur öffnen, wenn der aktuelle Schritt sie braucht. Bei Änderungen an einem bestehenden Projekt nennt `hyperframes.json` → `authoringSkill` den zuständigen Workflow.
- Eine Datei, die in dieser Sitzung schon gelesen wurde und sich nicht geändert hat, wird nicht erneut gelesen.

### 3. Bauen: kleine Diffs statt Neuschreiben
- **Edit statt Rewrite.** Eine 50-KB-Datei neu zu schreiben kostet die vollen 50 KB als Ausgabe, und Ausgabe-Tokens sind die teuersten. Ein gezielter Edit kostet ein paar Zeilen.
- **Varianten kopieren:** Eine neue Version eines bestehenden Videos (z. B. Steampunk-Fassung) entsteht per `cp -r` und gezielten Edits, nicht durch Neubau.
- **Änderungswünsche bündeln:** Fünf Korrekturen in einer Nachricht sind ein Durchlauf, fünf Nachrichten sind fünf Durchläufe mit wachsendem Verlauf.
- Unabhängige Tool-Aufrufe parallel in einem Schritt.

### 4. Prüfen: günstig zuerst, teuer einmal
- Reihenfolge: `lint` → `check` → Einzelbilder (`snapshot --at …`) → **ein** Voll-Render am Ende.
- **Bilder sind teuer.** Ein Screenshot kostet grob 1.000–1.600 Tokens. Statt zehn Einzelbildern einen Kontaktbogen anschauen (mehrere Frames in einem kleinen Bild, Befehl in `Referenzen/video-workflow.md`).
- **Ausgaben kürzen:** `| tail -20`, `--json` mit gezieltem Feld, `--quiet`. Lange Logs nie komplett in den Kontext holen.
- Ein fertiges MP4 nicht „zur Kontrolle" in Frames zerlegen und alle ansehen. Stichproben an den Szenenwechseln reichen.

### 5. Abschließen: übergeben und Schluss
- Committen und pushen.
- `NOTIZ.md` im Projektordner schreiben oder aktualisieren (Vorlage: `Referenzen/sitzungs-uebergabe.md`, höchstens 30 Zeilen).
- Der Person einen fertigen Startprompt für die nächste Sitzung geben.
- Dann: **neue Sitzung für das nächste Video.**

## Wann Claude von sich aus eine neue Sitzung vorschlägt

Kurz und einmalig, mit fertiger Übergabe, sobald einer dieser Fälle eintritt:

- Ein neues Video oder ein unabhängiges Thema beginnt in einer Sitzung, in der schon etwas fertig gebaut wurde.
- Das aktuelle Ergebnis ist committet und gepusht.
- Die Sitzung ist lang geworden (mehrere Renders, viele Screenshots, große Dateien gelesen).
- Dieselbe Korrektur dreht sich zum dritten Mal im Kreis. Ein frischer Start mit sauberer Notiz löst das oft schneller.

Formulierung, etwa: „Das Video ist fertig und gepusht. Für das nächste lohnt sich eine frische Sitzung, hier ist der Startprompt dafür: …"

Nicht vorschlagen mitten in einer laufenden Änderung oder wenn die Person gerade Rückfragen zum aktuellen Ergebnis hat.

## Verhalten bei Antworten

- **Knapp antworten.** Was geändert wurde, wo, ob es geprüft ist. Kein Wiederholen des Auftrags, keine Zusammenfassung von Code, der im Diff steht.
- **Keine großen Codeblöcke im Chat**, wenn der Code ohnehin in eine Datei geschrieben wird.
- **Subagenten nur bei echtem Fan-out** (viele Dateien parallel durchsuchen). Jeder Subagent startet kalt und baut seinen Kontext neu auf.
- **Rückfragen nur, wenn eine falsche Annahme teurer ist als die Frage.** Sonst Annahme in einem Halbsatz nennen und liefern.
- **Fehlschläge nicht blind wiederholen.** Erst die Ursache in der Fehlermeldung lesen, dann einmal gezielt korrigieren.

## Hebel außerhalb des Chats

| Hebel | Wann | Wirkung |
|---|---|---|
| Neue Sitzung | neues Video, neue Aufgabe | größter Hebel, Verlauf beginnt bei null |
| `/clear` (Claude Code) | gleiche Umgebung, neues Thema | wie neue Sitzung, Repo bleibt |
| `/compact <Fokus>` | Aufgabe läuft noch, Verlauf ist lang | ersetzt den Verlauf durch eine Zusammenfassung |
| `/context`, `/cost` | zwischendurch | zeigt Kontextbelegung bzw. Kosten, sofern verfügbar |
| `CLAUDE.md` schlank halten | dauerhaft | wird automatisch mitgeladen, jede Zeile kostet in jeder Sitzung. Boilerplate aus `hyperframes init` (8 KB, doppelt als `AGENTS.md`) pro Videoordner löschen oder kürzen |
| Kleineres Modell | Texte tauschen, Timing schieben, Tippfehler | günstiger pro Token, reicht für mechanische Edits |
| Großes Modell | Konzept, Storyboard, kniffliges Debugging | spart Runden, weil es seltener danebenliegt |

Prompt-Caching hilft automatisch: ein unveränderter Verlauf wird beim nächsten Turn günstiger gelesen. Es macht lange Sitzungen billiger, aber nie billiger als kurze.

## Referenzen

- `Referenzen/video-workflow.md`: Hyperframes-spezifisch (Projekt-Karte, Szenen gezielt bearbeiten, Varianten, Kontaktbogen, Render-Disziplin)
- `Referenzen/sitzungs-uebergabe.md`: Vorlage für `NOTIZ.md` und den Startprompt der nächsten Sitzung
- `Referenzen/startprompts.md`: kurze, vollständige Startprompts für typische Aufgaben
- `Werkzeuge/projekt-karte.py`: kompakte Karte einer Komposition (nur Python-Standardbibliothek)
