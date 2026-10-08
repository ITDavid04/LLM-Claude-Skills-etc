# Stimme und Beispiele

Inhalt: 1. Vorher-nachher-Paare aus echtem Material, 2. Ein gelungenes Muster, 3. Satzmuster, 4. Humor, 5. Anrede und Register

Die Beispiele zeigen, was sich ändert und warum. Sie sind keine Schablonen. Die Paare 1 und 2 stammen aus dem Projektmaterial (ASCII-Guide und Pizzeria-Quest). In beiden wurden keine Fakten ergänzt.

## 1. Vorher-nachher-Paare

### Paar 1: Einstieg in einen Fachtext

Vorher:
> Stellen Sie sich vor, ASCII-Zeichen sind wie Bausteine in einem Baukasten. Jedes Zeichen hat eine bestimmte Form und eine bestimmte optische Dichte. Wenn wir diese Bausteine geschickt anordnen, entstehen Formen. ANSI-Codes wiederum sind wie die Buntstifte, mit denen wir diese Bausteine anmalen können. Zusammen ermöglichen sie es uns, Benutzeroberflächen in Umgebungen zu schaffen, in denen keine herkömmliche Grafik verfügbar ist, wie etwa bei der Fernwartung eines Servers über eine SSH-Verbindung.

Nachher:
> Du bist per SSH auf einem Server eingeloggt. Grafik gibt es dort nicht, nur Text. Trotzdem kannst du in diesem Text Bilder zeichnen: Ein Schrägstrich `/` wird zur Diagonale, ein `@` zur dunklen Fläche. Das ist ASCII Art. ANSI-Codes sind die Buntstifte dazu, sie färben die Zeichen ein. Zusammen ergeben sie eine Oberfläche, die ohne jede Grafik auskommt.

Was sich geändert hat:
- Die Anrede ist durchgehend „du" statt „Sie".
- Der Text beginnt mit einer Szene, nicht mit einem Vergleich.
- Verben tragen die Sätze („loggst", „zeichnen", „färben").
- Die abstrakte „optische Dichte" ist durch zwei konkrete Zeichen ersetzt, die im Original selbst vorkommen.
- Die Buntstift-Analogie bleibt, weil sie schon im Original stand und trägt.

### Paar 2: Eröffnung eines Abenteuers

Vorher:
> Das freut mich riesig! Maestro Luigi ist bereits begeistert – die ersten Menükarten in seiner Sprache haben ihm Tränen der Rührung in die Augen getrieben. Aber jetzt wird es ernst in der Küche von „La Bella Code". Da du **Anfänger** im **Creativ-Modus** bist, bauen wir auf unserem Vokabular auf.

Nachher:
> Die ersten Menükarten in Luigis Sprache sind gedruckt, und Luigi hat Tränen in den Augen. Dafür bestellen jetzt so viele Leute, dass es in der Küche von „La Bella Code" drunter und drüber geht. Heute bringst du Ordnung hinein.

Was sich geändert hat:
- Der Chat-Opener und der Modus-Hinweis sind weg. Der Leser ist in der Geschichte, nicht im Prompt.
- Der Rückgriff auf die erste Quest bleibt, jetzt als Szene statt als Ansage.
- Die Mission steht in einem Satz am Ende des Einstiegs.

### Paar 3: Staging-Formel

Vorher:
> Für einen Umschüler in der IT ist das Verständnis dieser Konzepte nicht nur eine nostalgische Spielerei. Es ist der Schlüssel zum Verständnis davon, wie Terminals funktionieren, wie Server Statusmeldungen ausgeben und wie Daten über Netzwerke fließen.

Nachher:
> Wer wissen will, wie ein Terminal funktioniert, braucht diese Codes. Server melden ihren Status damit, und auch bei Daten im Netzwerk tauchen sie auf.

Was sich geändert hat: Die Formel „nicht nur X, sondern der Schlüssel" und die Dreierliste aus Gewohnheit sind raus. Übrig bleibt, was der Satz wirklich behauptet. Die Aussage zu Netzwerken wurde bewusst abgeschwächt, weil sie im Original unbelegt war. Wenn der Autor mehr dazu weiß, kommt sie als konkretes Beispiel zurück.

## 2. Ein gelungenes Muster: Bild, Begriff, Grenze

Aus der Pizzeria-Reihe, Quest 5, leicht gekürzt. Es zeigt die Reihenfolge, die das Material trägt:

> Eine Transaktion ist wie ein Versprechen. Wenn du im Laden ein Eis kaufst, gibst du das Geld erst her, wenn du das Eis in der Hand hältst. Würde der Verkäufer das Geld nehmen und wegrennen, wäre der Kauf ungültig. In der Software heißt das: Entweder gelingen alle Schritte eines Vorgangs, oder der Ausgangszustand wird wiederhergestellt.

Was daran funktioniert: Zuerst eine Szene, die jeder kennt. Dann der Fachbegriff. Dann die genaue Aussage über die Software. Was fehlt, ist die Grenze des Bildes. Ein Eiskauf kennt keinen Rollback, und das ist der Teil, an dem Anfänger später stolpern. Ein Satz dazu („Beim Eis gibt es kein Zurückspulen. Die Datenbank kann das") würde das Muster vervollständigen.

Gute Praxis aus dem Material, die man übernimmt: Deep Dive 5 benennt selbst, dass die try/except-Konstruktion nur eine Simulation der echten Datenbank-Transaktion ist. Solche Hinweise kosten einen Satz und schützen den Leser.

## 3. Satzmuster

| Muster | Beispiel | Besser |
|---|---|---|
| Substantivkette | „Die Durchführung der Anmeldung am System erfolgt über …" | „Du meldest dich über … am System an." |
| Gewicht ohne Inhalt | „Das ist der eigentliche Schlüssel." | Streichen, oder den Grund nennen: „Ohne das läuft nichts, weil …" |
| Nicht X, sondern Y | „Das ist keine Spielerei, sondern Grundlagenwissen." | „Das ist Grundlagenwissen, weil …" |
| Dreierliste aus Gewohnheit | „schnell, sicher und zuverlässig" | Das eine nennen, das stimmt, und belegen |
| Pseudo-Tiefsinn | „Im Kern geht es um Vertrauen." | Sagen, welches Vertrauen worin |
| Abstrakte Anrede | „Man sollte beachten, dass …" | „Achte darauf, dass …" |
| Rhetorische Schlussfrage | „Wie fühlst du dich nach dieser Reise?" | Streichen. Im Text kann niemand antworten. Oder in eine Aufgabe verwandeln |
| Chat-Angebot | „Wenn du magst, erkläre ich es noch einfacher." | Streichen |

## 4. Humor

Die Beispiele sind Illustrationen zum Muster, keine Sätze zum Wiederverwenden.

Funktioniert:
- Eine Absurdität des Themas benennen. „Der Server hat Millionen Zeilen Log geschrieben und genau eine davon ist wichtig." Das ist wahr, kurz und der Leser kennt es.
- Trocken untertreiben. „Der Cronjob lief nicht. Das fällt meistens erst auf, wenn man ihn braucht."
- Auf die eigene Figur beziehen, wenn es eine Welt gibt. „Luigi schlägt den Gong. Antonio hört ihn nicht, er hat die Kopfhörer auf."

Funktioniert nicht:
- Ein Witz pro Abschnitt, weil „locker" verlangt wurde. Der Leser merkt die Quote.
- Wortspiele in Serie.
- Humor in Definitionen, Warnungen und Fehlermeldungen.
- Humor auf Kosten des Lesers („Wer das nicht versteht, …").
- Emojis als Pointe oder als Stimmungsmarker.

## 5. Anrede und Register

- „Du" im ganzen Text. Die Zielgruppe sind erwachsene Quereinsteiger, kein Kinderton.
- Kein Zuspruch auf Vorrat („Du schaffst das!"). Wenn etwas schwer ist, sage das und gib den nächsten kleinen Schritt.
- Fehler des Lesers werden freundlich und konkret benannt. „Das passiert fast jedem beim ersten Mal" ist nur dann ein Satz wert, wenn es stimmt.
- Fachwörter bleiben Fachwörter. Locker heißt nicht, sie zu verniedlichen. „Aggregate" bleibt „Aggregate", das Bild („Bestell-Klammer") kommt dazu.
