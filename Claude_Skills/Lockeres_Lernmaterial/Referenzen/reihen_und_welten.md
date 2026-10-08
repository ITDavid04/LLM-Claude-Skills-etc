# Reihen und Welten

Inhalt: 1. Wann eine Welt sich lohnt, 2. Weltbibel, 3. Begriff-Bild-Tabelle, 4. Rückgriffe, 5. Aufbau einer Reihe, 6. Aufgaben und Nachweis, 7. Teaser und Abschluss, 8. Erzählrichtungen

## 1. Wann eine Welt sich lohnt

Eine gemeinsame Welt (eine Pizzeria, eine Detektei, ein Handwerksbetrieb) lohnt sich bei Reihen von drei oder mehr Texten, die aufeinander aufbauen. Der Leser kennt dann Küche und Figuren schon, und neue Begriffe landen in vertrautem Gelände. Bei einem Einzeltext reicht ein einziges tragendes Bild, eine ganze Welt wäre Aufwand ohne Ertrag.

Wähle die Welt nach dem Thema, nicht nach Geschmack. Sie muss genug Dinge enthalten, die den Fachbegriffen entsprechen. Eine Pizzeria hat Bestellungen, Stationen, Übergaben und ein Archiv, und deshalb trägt sie ein Thema wie Domain-Driven Design. Eine Welt, in der die Hälfte der Bilder hinkt, erzeugt mehr Erklärarbeit als sie spart.

## 2. Weltbibel

Lege vor dem ersten Text eine kurze Weltbibel an und halte sie im ganzen Projekt ein. Der Aufwand ist klein, der Nutzen ist groß: Im vorhandenen Pizzeria-Material wechselt die „goldene Pizzaschaufel" im letzten Text zur „goldenen Schürze", weil niemand festgelegt hatte, was am Ende überreicht wird.

Vorlage:

```text
Welt:            [Ort und Situation in zwei Sätzen]
Figuren:         [Name, Rolle, eine Eigenheit, die wiederkehrt]
Orte:            [Küche, Lager, ...]
Running Gags:    [maximal zwei bis drei, mit dem Text, in dem sie zuerst vorkommen]
Abschlussmotiv:  [was am Ende der Reihe überreicht oder erreicht wird]
Ton:             [trocken / warm / spöttisch, ein Wort genügt]
Tabu:            [was nicht vorkommt, zum Beispiel Gewalt oder reale Firmen]
```

Running Gags brauchen Planung. Ein Gag, der in Text 2 auftaucht, kommt in Text 4 oder 5 zurück und löst sich im Abschluss auf. Ein Gag, der nur einmal vorkommt, ist ein Witz, kein Running Gag.

## 3. Begriff-Bild-Tabelle

Lege sie vor dem Schreiben an. Sie hat drei Spalten. Die dritte ist die wichtigste.

| Fachbegriff | Bild | Wo das Bild hinkt |
|---|---|---|
| Aggregate | Bestell-Klammer: Alles, was zusammengehört, kommt in eine Klammer | Eine Klammer hat keinen Chef, ein Aggregate hat einen Einstiegspunkt (Aggregate Root) |
| Repository | Bücherei: Man leiht das Buch, liest und stellt es zurück | In der Bücherei ändert man das Buch nicht, im Repository wird gespeichert, was sich geändert hat |
| Domain Event | Post-it an der Pinnwand: Information über etwas, das schon passiert ist | Ein Post-it kann man abnehmen, ein Event ist eine Tatsache und bleibt |

Die Tabelle stammt in Teilen aus der Pizzeria-Reihe. Die dritte Spalte ist ein Vorschlag und im Original nicht enthalten. Die Spalte „Wo das Bild hinkt" kommt in den Text, nicht nur in die Notizen. Ein Satz reicht.

## 4. Rückgriffe

Ab dem zweiten Text kommt mindestens ein benannter Rückgriff auf einen früheren. „Erinnerst du dich an die Bestell-Klammer aus Teil 2?" Das stärkt das Gefühl, dass die Reihe zusammenhängt, und wiederholt den Stoff ohne Pauschal-Rückblick.

Regeln:
- Benenne, worauf du zurückgreifst. „Wie im letzten Teil" ist zu vage.
- Ein Rückblick-Kasten steht nur, wenn er etwas wiederholt, das für den neuen Stoff gebraucht wird. Im ersten Text gibt es keinen.
- Wiederhole nicht in denselben Worten. Greife das Bild auf und gib ihm eine neue Aufgabe.
- Lege nicht mehr als zwei, drei Rückgriffe pro Text an, sonst wirkt der Text wie eine Zusammenfassung.

## 5. Aufbau einer Reihe

Ein bewährtes Gerüst für fünf bis sechs Texte:

1. Der Anfang: Grundbegriffe und ihre Bilder.
2. Erste Anwendung: Das Gelernte in einer kleinen Situation einsetzen.
3. Vertiefung: Einen früheren Begriff erneut aufgreifen und einen neuen darauf bauen.
4. Kombination: Altes und Neues in einer Aufgabe verbinden.
5. Prüfung: Alles zusammen an einem größeren Fall.
6. Abschluss: Rückblick auf die Reihe und eine ehrliche Antwort auf die Frage, wann sich der Aufwand nicht lohnt.

Der letzte Punkt stammt aus der Pizzeria-Reihe und ist gute Praxis. Wer ein Verfahren beibringt, sagt auch, wann man es nicht braucht.

Prüfe vor dem Schreiben, dass die Reihe zum Plan passt. Im vorhandenen Material versprach die Übersichtsseite Themen (Entities, Value Objects, Event Sourcing), die in den Texten nie vorkamen, und die Teil-Nummern in den Teasern stimmten nicht. Gleiche Übersicht und Texte ab, bevor die Reihe erscheint.

## 6. Aufgaben und Nachweis

- Jede Aufgabe ist konkret und in einer Sitzung machbar.
- Aufgaben bauen aufeinander auf: Aufgabe 2 nutzt das Ergebnis von Aufgabe 1.
- Eine Zusatzaufgabe ist als solche markiert und darf schwerer sein.
- Der Nachweis ist ein greifbares Ergebnis: ein Glossar, eine Skizze, ein Log, ein Screenshot. Er schult nebenbei Dokumentation.
- Die Aufgabe nennt ein Erfolgskriterium, wenn Fehlinterpretationen naheliegen. Beispiel aus dem Material: „Deine Liste enthält nur ganze Pizzen oder Bestellungen und keine einzelnen Zutaten."
- Reflexionsfragen sind echte Fragen mit einer prüfbaren Antwort („Warum haben wir belegen und backen getrennt?"). Rhetorische Schlussfragen entfallen.
- Lösungen gibt es nur, wenn der Auftrag sie verlangt. Hilfen und Tipps stehen schon im Text.

## 7. Teaser und Abschluss

Ein Teaser nennt in ein bis zwei Sätzen das konkrete nächste Thema und warum es auf diesem aufbaut. „Im nächsten Teil sortieren wir die Wörter in feste Gruppen." Kein Cliffhanger, keine Frage an den Leser, keine Dopplung desselben Teasers.

Der Abschluss einer Reihe fasst die Begriffe in einer kleinen Tabelle zusammen (Begriff, Bild, Werkzeug) und sagt ehrlich, wann man das Verfahren lieber lässt. Kein Glückwunsch-Pathos, ein Satz reicht.

## 8. Erzählrichtungen

Wer verschiedene Erzählstile braucht, kann sie über den Ton der Weltbibel steuern. Mögliche Grundrichtungen:

| Richtung | Passt zu | Die Welt liefert |
|---|---|---|
| Detektei | Fehlersuche, Analyse, Debugging | Fälle, Spuren, Verdächtige |
| Handwerksbetrieb | Abläufe, Rollen, Werkzeuge | Werkstatt, Auftrag, Übergabe |
| Küche | Prozesse, Zustände, Verantwortung | Stationen, Bons, Ofen |
| Expedition | Neues Gelände erkunden | Karte, Ausrüstung, Etappen |
| Mentor-Gespräch | Konzepte erklären, Warum-Fragen | Zwei Personen, die reden |

Die Richtung ist ein Mittel, kein Selbstzweck. Wenn das Thema in keine Welt passt, bleibt der Text ohne Welt und lebt von Szene und Bild.
