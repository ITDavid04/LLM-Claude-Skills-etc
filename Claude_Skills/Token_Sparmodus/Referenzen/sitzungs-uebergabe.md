# Sitzungs-Übergabe

Ziel: Die nächste Sitzung startet mit 30 Zeilen Wissen statt mit dem ganzen alten Verlauf.

## Wann schreiben

- Am Ende jeder Sitzung, in der etwas gebaut oder entschieden wurde.
- Vor `/clear` oder `/compact`.
- Wenn Claude eine neue Sitzung vorschlägt.

## Wo

`NOTIZ.md` im Projektordner (z. B. `videos/<name>/NOTIZ.md`), mit committen. Bei Aufgaben ohne eigenen Ordner: im Repo-Wurzelverzeichnis oder direkt als Startprompt an die Person.

## Vorlage (höchstens 30 Zeilen)

```markdown
# NOTIZ: <projektname>
Stand: <Datum> · Branch: <branch> · letzter Commit: <kurz-hash>

## Ziel
<1–2 Sätze: was das Ergebnis ist, Format, Länge>

## Stand
- fertig: <was steht und geprüft ist>
- offen: <was noch fehlt>

## Entscheidungen (nicht neu diskutieren)
- <Stil, Farben, Schrift, Musik, Szenenzahl … mit kurzem Grund>

## Wichtige Stellen
- <Datei>:<Zeilen> <was dort ist>  (oder: „Karte: python3 …/projekt-karte.py videos/<name>")

## Nächster Schritt
<genau eine Sache, mit der die nächste Sitzung anfängt>

## Prüfen mit
<Befehle, z. B. npx hyperframes check, Kontaktbogen-Befehl>
```

## Regeln

- **Nur was die nächste Sitzung braucht.** Kein Protokoll, keine Fehlversuche, außer ein Irrweg wäre sonst wiederholt worden („Chiptune klang nach Mario, nicht nochmal").
- **Entscheidungen festhalten**, damit sie nicht erneut verhandelt werden.
- **Zeilennummern sind flüchtig.** Lieber Abschnittsnamen oder den Hinweis auf die Karte.
- Eine bestehende `NOTIZ.md` wird aktualisiert, nicht ergänzt. Alter Stand fliegt raus.

## Startprompt für die nächste Sitzung

Claude gibt am Ende diesen Block zum Kopieren aus:

```text
Lies videos/<name>/NOTIZ.md und arbeite im Token-Sparmodus.
Aufgabe: <nächster Schritt aus der Notiz>.
Fertig, wenn: <Kriterium>. Danach committen und pushen.
```
