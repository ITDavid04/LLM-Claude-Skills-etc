---
name: lockeres-lernmaterial
description: Schreibt Lernmaterial, das sich gern liest, ohne an fachlicher Genauigkeit zu verlieren, auf Deutsch mit du-Ansprache. Gedacht für Erklärtexte, Einstiege, Übungen, Aufgabenreihen und Lernabenteuer für Umschüler und Quereinsteiger, besonders im IT-Bereich. Nutze diese Skill, wenn jemand lockeres, unterhaltsames, leicht lesbares oder motivierendes Lernmaterial will, wenn ein vorhandener Text zu roh, trocken, steif oder nach KI klingt und lesbarer werden soll, oder wenn eine Story, ein Thema oder ein Rechercheergebnis zu einer Aufgabenreihe mit gemeinsamer Welt umgebaut werden soll. Der Spaß entsteht durch Text und Aufbau (Szene, Bild, Rückgriffe, trockener Humor), nie durch Emojis. Nicht gedacht für Chat-Antworten (dafür gibt es natuerliche-konversation) und nicht für Texte, bei denen eine andere Skill das Format vorgibt. Deren Struktur bleibt dann unberührt.
---

# Lockeres Lernmaterial

Menschen lesen Lernmaterial am Ende besser, wenn es freiwillig weitergelesen wird. Der Text muss also nicht nur stimmen, er muss sich lohnen. Dafür zählt vor allem der Aufbau: Wo ein Abschnitt anfängt, wie ein Fachbegriff eingeführt wird, ob der Leser etwas wiedererkennt. Humor und Bilder helfen, tragen aber allein nicht.

Zwei Leitplanken gelten immer. **Locker im Ton, streng im Inhalt:** Definitionen, Zahlen, Befehle und Prüfbegriffe sind von Ton und Witz unberührt. **Keine Emojis:** weder in Überschriften noch im Text noch in Code-Ausgaben. Ton und Struktur tragen den Text allein.

Abgrenzung: Legt eine andere Skill oder der Nutzer Struktur und Format fest (zum Beispiel `wiki-fiae` für Wiki-Artikel), bleiben diese Vorgaben unverändert und haben Vorrang. Diese Skill liefert dann nur die Stimme innerhalb des vorgegebenen Rahmens.

## Arbeitsablauf

**1. Auftrag klären, ohne zu verhören.** Setze Standardwerte: du-Ansprache, Anfänger mit Quereinstiegs-Hintergrund, kein Humor-Zusatzwunsch. Frage höchstens einmal, und nur, wenn die Antwort das Ergebnis deutlich ändert (zum Beispiel: Einzeltext oder Reihe, oder fehlendes Quellmaterial). Nenne die Annahmen in einem Halbsatz und liefere.

**2. Lernziel in einem Satz festlegen.** „Am Ende kann der Leser …" Alles, was dieses Ziel nicht stützt, fliegt raus, auch wenn es lustig ist.

**3. Bilder wählen.** Jeder Fachbegriff bekommt ein Bild aus einer Welt, die der Leser kennt. Notiere dazu in einer kurzen Tabelle, **wo das Bild hinkt**. Ein Bild, dessen Grenze du nicht kennst, führt zu falschen Vorstellungen. Vorlage in `references/reihen-und-welten.md`.

**4. Gerüst bauen.** Jeder Abschnitt folgt dem Bogen: Szene oder Problem, Bild, Fachbegriff mit exakter Definition, Auflösung (wo das Bild hinkt), Aufgabe. Bei einer Reihe kommt vorher die Weltbibel dazu.

**5. Schreiben** nach den Regeln unten.

**6. Prüfen** mit `references/pruefliste.md`. Das gilt vor allem für fachliche Fehler: Code ausführen, Beispiele gegen die eigene Lektion prüfen, Querverweise abgleichen.

**7. Ausliefern.** Längere Texte als Markdown-Datei, kurze Abschnitte direkt im Chat. Ohne Nachsatz mit Angeboten.

## Stimme

- Eine Anrede im ganzen Text: du. Nicht zwischen du und Sie wechseln.
- Kurze Sätze, Verben statt Substantivketten. „Du loggst dich ein" statt „Die Durchführung der Anmeldung". Die Satzlänge wechselt, denn im Text fehlt die Stimme, und der Rhythmus muss ihre Arbeit übernehmen.
- Sage direkt, was du meinst. Ein Satz, der nur Gewicht geben soll („Das ist der Schlüssel zu allem"), kommt raus. Besonders das Muster „nicht X, sondern Y" und Dreierlisten aus Gewohnheit.
- Ein Modalpartikel pro Satz reicht („mal", „halt", „ja"). Mehr klingt gespielt.
- Fachbegriffe: erst Bild, dann Begriff, dann ein Satz Definition. Beim ersten Auftreten erklären, danach den gesetzten Begriff beibehalten und nicht durch Synonyme ersetzen.

## Abschnittsaufbau

Beginne jeden Abschnitt mit etwas, das passiert, nicht mit einer Definition. Ein Problem, eine Szene, eine Frage, die der Leser sich selbst stellen würde. Die Definition kommt, wenn der Leser sie braucht. Beispiel: „Du bist per SSH auf einem Server. Grafik gibt es dort nicht, nur Text" holt den Leser ab, bevor „ASCII" fällt.

Konkretes schlägt Allgemeines. „Ein Schrägstrich `/` wird zur Diagonale, ein `@` zur dunklen Fläche" zeigt mehr als „Zeichen haben eine optische Dichte".

## Humor

Trocken, kurz, an der Sache. Ein Halbsatz, der eine Absurdität des Themas benennt, wirkt besser als ein Witz-Slot pro Abschnitt. Humor kommt höchstens ein- bis zweimal pro Abschnitt vor. Er steht nie in Definitionen, Warnungen oder Fehlermeldungen, nie auf Kosten des Lesers und nie als Ersatz für eine Erklärung. Running Gags sind erlaubt und stark, sie brauchen aber Planung (siehe Weltbibel).

## Reihen und Rückgriffe

Bei mehreren zusammenhängenden Texten gilt: eine Welt für die ganze Reihe, Figuren und Orte vorher festlegen, Running Gags nicht wechseln. Ab dem zweiten Text mindestens ein benannter Rückgriff auf einen früheren Text („Erinnerst du dich an die Bestell-Klammer?"). Ein Rückblick-Kasten steht nur da, wo es wirklich etwas zu wiederholen gibt. Den ersten Text beginnt man nicht mit einem Pflichtrückblick. Details, Aufgabenketten und Teaser-Regeln stehen in `references/reihen-und-welten.md`.

## Aufgaben

Eine Aufgabe ist konkret und machbar: „Schreibe drei Sätze, die mit ‚Wenn … passiert ist, dann …' beginnen." Aufgaben bauen aufeinander auf und bleiben in der laufenden Geschichte. Ein Nachweis am Ende (Glossar, Skizze, Log, Screenshot) macht das Ergebnis greifbar und trainiert Dokumentation. Reflexionsfragen sind echte Aufgaben mit einer prüfbaren Antwort. Rhetorische Fragen an einen Leser, der nicht antworten kann, sind überflüssig. Anfängerhilfen (Vergleich, Tipp) stehen im Text, Lösungen nur, wenn der Auftrag sie verlangt.

## Format

- Schlichte Überschriften, kein Emoji-Satz, kein fest vorgeschriebenes Template.
- Pflicht in jedem Text: Einstieg, Kerninhalt, mindestens eine Aufgabe. Alles andere ist optional und folgt dem Inhalt. Reihenfolge und Länge der Blöcke dürfen variieren, sonst wird der Aufbau nach dem dritten Text vorhersehbar.
- Fließtext überwiegt. Tabellen nur für echte Vergleiche, Listen nur für Schritte oder Nachschlagbares.
- Code steht in Codeblöcken mit Sprachangabe, die erwartete Ausgabe darunter.

## Was nie in den fertigen Text gehört

Anreden an einen Chat-Nutzer („Das freut mich riesig!", „Da du Anfänger im Kreativ-Modus bist"), Hinweise auf Modi oder Level, Angebote am Ende („Wenn du magst, mache ich noch …"), Doppelungen aus zusammenkopierten Entwürfen und Pflichtblöcke ohne Inhalt. Der Leser ist in der Geschichte, nicht im Prompt.

## Beim Überarbeiten vorhandener Texte

Behalte den Inhalt und füge keine Fakten, Zahlen oder Quellen hinzu. Ändere Einstieg, Satzbau, Anrede und Bilder. Wenn ein Satz einen Fakt braucht, den du nicht hast, schreibe einen einfacheren Satz oder frage nach. Melde fachliche Fehler, die dir auffallen, statt sie stillschweigend zu korrigieren oder zu übernehmen. Vorher-nachher-Beispiele stehen in `references/stimme-und-beispiele.md`.

## Wann welche Datei

- `references/stimme-und-beispiele.md`: Vorher-nachher-Paare, Humor-Beispiele und Satzmuster. Lies sie vor dem Schreiben und beim Überarbeiten.
- `references/reihen-und-welten.md`: Weltbibel-Vorlage, Begriff-Bild-Tabelle, Rückgriffe, Aufgabenketten, Teaser. Lies sie bei jeder Reihe.
- `references/pruefliste.md`: Prüfliste vor der Abgabe. Lies sie immer, bevor du den Text ausgibst.
