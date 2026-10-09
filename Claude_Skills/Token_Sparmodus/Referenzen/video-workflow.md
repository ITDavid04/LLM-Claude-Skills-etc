# Video-Workflow (Hyperframes), token-sparend

Befehle laufen aus dem Repo-Wurzelverzeichnis, mit dem Skill unter `.claude/skills/token-sparmodus/` (siehe `installieren.sh`). Gilt für Projekte wie `Hyperframes/videos/<name>/` mit `index.html`, `hyperframes.json`, `assets/`, `fonts/`, `vendor/`, `renders/`.

## Größenordnungen (Stand der bisherigen Videos)

| Was | Größe | Grob in Tokens |
|---|---|---|
| `index.html` komplett | 25–67 KB | 7.000–20.000 |
| Projekt-Karte | 1–2 KB | 300–600 |
| Eine Szene per `sed -n` | 20–40 Zeilen | 300–800 |
| Ein Screenshot / Frame | – | 1.000–1.600 |
| Kontaktbogen mit 15 Frames | ein Bild | ca. 1.600 |
| Alle Hyperframes-Skills zusammen | ca. 480 KB | weit über 100.000, nie alle laden |

Alles, was einmal gelesen wurde, wird bei jeder weiteren Antwort der Sitzung erneut mitgelesen.

## Neues Video

1. **Frische Sitzung.** Startprompt aus `startprompts.md`.
2. **Vorlage wählen statt bei null anfangen:** Gibt es ein ähnliches Video (Format, Länge, Aufbau), dann Karte davon ansehen und als Vorlage nennen.
3. **Plan einmal, kurz:** Szenenliste mit Zeiten als Tabelle, eine Freigabe-Runde. Keine drei Plan-Varianten ausformulieren, wenn nicht danach gefragt wurde.
4. **Bauen in einem Rutsch**, dann `lint`.
5. **Prüfen:** `npx hyperframes check` (bei Iteration `--no-contrast` zum Beschleunigen), Ausgabe gekürzt lesen.
6. **Visuell prüfen per Kontaktbogen** (siehe unten), nicht Frame für Frame.
7. **Ein Voll-Render** nach Freigabe. `test -s` und `ffprobe` statt Video erneut ansehen.
8. Commit, `NOTIZ.md`, Sitzung beenden.

## Variante eines bestehenden Videos (z. B. Steampunk-, Hochformat-, Witzig-Fassung)

```bash
cp -r videos/claude-anleitung-witzig videos/claude-anleitung-neu
rm -rf videos/claude-anleitung-neu/renders
python3 .claude/skills/token-sparmodus/Werkzeuge/projekt-karte.py videos/claude-anleitung-neu
```

Dann gezielt ändern: `meta.json` (id/name), Farben und Schriften im `<style>`-Block, Texte pro Szene. Die Karte zeigt, in welchen Zeilen was steht. Die Komposition nicht neu schreiben, nur austauschen.

## Änderung an einer Szene

```bash
python3 .claude/skills/token-sparmodus/Werkzeuge/projekt-karte.py videos/<name>          # Abschnitte + Zeilen
sed -n '211,247p' videos/<name>/index.html               # nur diese Szene lesen
```

Danach mit einem gezielten Edit ändern. Wenn sich Zeilennummern durch den Edit verschieben, die Karte neu erzeugen, statt die Datei neu zu lesen.

Tipp für neue Kompositionen: Jede Szene im Script mit einer Kommentar-Überschrift beginnen, z. B. `/* ===== 3: Titel (9-12) ===== */`. Die Karte listet diese Überschriften als Inhaltsverzeichnis.

## Kontaktbogen statt vieler Screenshots

Aus einem fertigen Render, ein Bild pro 3 Sekunden, 5 × 3 Kacheln:

```bash
ffmpeg -v error -y -i renders/<name>.mp4 \
  -vf "fps=1/3,scale=216:-1,tile=5x3" -frames:v 1 kontakt.png
```

- `fps=1/3` an die Szenenlänge anpassen (Szenen à 3 s → ein Frame pro Szene).
- Für Querformat `scale=320:-1,tile=4x4` o. ä.
- Erst bei einem konkreten Verdacht eine einzelne Szene groß ansehen (`snapshot --at <t>`).
- `kontakt.png` nicht committen.

## Render-Disziplin

- Voll-Render nur nach Freigabe oder wenn ausdrücklich gewünscht. Ein Render liefert kaum neue Information, die `check` plus Kontaktbogen nicht schon gezeigt hätten.
- Nach dem Render: `test -s out.mp4 && ffprobe -v error -show_entries format=duration -of csv=p=0 out.mp4`, nicht das ganze `ffprobe`-JSON.
- Render-Logs nur mit `| tail -20` lesen.

## Nie in den Kontext laden

`vendor/gsap.min.js`, `fonts/*.woff2`, `renders/*.mp4`, `assets/*.mp3`, `node_modules/`, `package-lock.json`, generierte Musik-Skripte nur dann, wenn genau daran gearbeitet wird (`tools/make-music.py` ist ca. 22 KB).

## Musik und Assets wiederverwenden

Bestehende Scores und Generator-Skripte aus anderen Videoordnern kopieren und Parameter ändern, statt neu zu komponieren. Die passende Datei per `ls videos/*/assets/` finden, nicht per Lesen.
