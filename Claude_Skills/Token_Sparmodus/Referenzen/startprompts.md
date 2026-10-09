# Startprompts

Ein guter Startprompt spart mehrere Rückfrage-Runden. Jede Runde liest den Verlauf neu, also ist die vollständige erste Nachricht der billigste Weg. Platzhalter in `<…>` ersetzen, nicht zutreffende Zeilen weglassen.

## Neues Video

```text
Neues Video im Token-Sparmodus.
Ordner: videos/<name>
Inhalt: <Thema / Botschaft in 1–2 Sätzen>
Format: <16:9 | 9:16 | 1:1>, <Sekunden> s, <Anzahl> Szenen
Stil: <z. B. wie videos/claude-anleitung-witzig, aber Farben X>
Musik: <eigene generieren | aus videos/<x>/assets übernehmen | keine>
Fertig, wenn: check grün, Kontaktbogen freigegeben, ein Render, Commit + Push.
```

## Variante eines bestehenden Videos

```text
Token-Sparmodus. Kopiere videos/<vorlage> nach videos/<neu>.
Ändere nur: <Stil / Format / Texte / Musik>.
Struktur und Timing bleiben gleich. Nicht neu bauen, gezielt editieren.
Fertig, wenn: check grün, Kontaktbogen, ein Render, Commit + Push.
```

## Korrektur an einem bestehenden Video

```text
Token-Sparmodus. videos/<name>: Erst Projekt-Karte, dann nur betroffene Szenen lesen.
Änderungen (alle in einem Durchlauf):
1. Szene <n>: <was>
2. Szene <m>: <was>
3. <…>
Danach check, Kontaktbogen, Render nur wenn ich es freigebe.
```

## Weiterarbeiten nach Übergabe

```text
Lies videos/<name>/NOTIZ.md und arbeite im Token-Sparmodus.
Aufgabe: <nächster Schritt>. Fertig, wenn: <Kriterium>.
```

## Allgemeine Aufgabe (kein Video)

```text
Token-Sparmodus. Repo: <repo>, Branch: <branch>.
Ziel: <was am Ende existieren soll>.
Relevante Dateien: <pfade, falls bekannt>.
Nicht anfassen: <…>.
Fertig, wenn: <Kriterium>.
```

## Formulierungen, die Runden sparen

- „Alle Änderungen in einem Durchlauf" verhindert Ping-Pong.
- „Render erst nach Freigabe" verhindert teure Zwischenrenders.
- „Nenn Annahmen kurz und mach weiter" verhindert Rückfragen bei Kleinigkeiten.
- „Antworte knapp: was geändert, wo, geprüft?" hält die Ausgaben klein.
