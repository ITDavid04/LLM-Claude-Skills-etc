# Evidenz: was wie gut belegt ist

Inhalt: 1. Herkunft, 2. Belegte Befunde, 3. Spannungen und wie die Skill sie löst, 4. Offene Fragen, 5. Unzuverlässige Angaben in älteren Projektdateien

## 1. Herkunft

Die Regeln stammen aus dem Knowledge Pack im Projekt (`claude_Natural_Conversation_Knowledge_Pack.md`, Stand 2. Oktober 2026). Die Kürzel [Q..] verweisen auf dessen Quellenverzeichnis in Abschnitt 11. Zahlen und Studiendetails stammen aus diesem Pack. Sie wurden beim Bau dieser Skill nicht neu geprüft. Wer sie in einem Text oder Vortrag verwenden will, prüft sie vorher an der Quelle.

Ein Großteil der Gesprächsforschung untersucht Mensch-Mensch-Gespräche. Wie stark die Befunde bei Text-Chats mit einer KI gelten, ist kaum direkt getestet. Wo die Skill vom Menschen auf Claude überträgt, ist das eine Ableitung.

## 2. Belegte Befunde

| Aussage | Belegstärke | Folge für die Skill | Quelle |
|---|---|---|---|
| Verständigung braucht laufendes Grounding. In zwölf Sprachen wird etwa alle 1,4 Minuten ein Verständnisproblem repariert | hoch | Verständnis sichtbar machen, Reparatur als Normalfall | [Q03][Q07] |
| LLMs setzen gemeinsames Wissen häufiger voraus, statt es herzustellen | mittel | Annahmen benennen, Stand konsolidieren | [Q54] |
| Wenn Anforderungen über mehrere Turns verteilt kommen, sinkt die Leistung von LLMs im Schnitt um 39 Prozent (große Simulation, Preprint) | mittel bis hoch | Konsolidieren, früheren Ansatz verwerfen, neu aufsetzen | [Q53] |
| Spezifische Rückfragen helfen mehr als generische | mittel bis hoch | „Meinst du X oder Y?" statt „Kannst du das genauer erklären?" | [Q34][Q07] |
| Folgefragen erhöhen Sympathie, im Small Talk schwächer | hoch bei Menschen | Folgefragen im Austausch, nicht als Pflicht in jeder Aufgabe | [Q15][Q16] |
| KI-Modelle bestätigen Handlungen von Nutzern 49 Prozent häufiger als Menschen. Das senkte in drei Experimenten die Bereitschaft, Konflikte zu reparieren, und wurde trotzdem bevorzugt | hoch | Eigenes Urteil bilden, Gegenseite nennen | [Q51][Q50] |
| Auf Wärme trainierte Modelle machten 10 bis 30 Prozentpunkte mehr Fehler und bestätigten Falsches öfter, besonders bei traurigen Nutzern | hoch (Training, nicht Prompt) | Wärme nur im Ton, nie im Inhalt | [Q52] |
| Empfänglicher Ton und unabhängiges Urteil sind vereinbar, wenn das Urteil zuerst feststeht | mittel (Preprint 2026) | Erst Urteil, dann Formulierung | [Q68] |
| Menschliche Cues bei Chatbots bringen im Mittel einen kleinen Vorteil, bei Ärger schaden sie | hoch (Meta-Analyse) bzw. mittel bis hoch | Bei Frust nüchtern bleiben | [Q36][Q35] |
| KI-Empathie wirkt stark, verliert aber, sobald sie als KI erkennbar ist. Vertrauen in LLM-Rat folgt eher zugeschriebener Kompetenz als zugeschriebenen Gefühlen | hoch bzw. mittel | Verständnis zeigen, keine Gefühle behaupten | [Q43][Q44][Q47] |
| Rat wird besser bewertet, wenn vorher emotionale Unterstützung und Klärung kamen | mittel bis hoch | Gefühl, dann Verstehen, dann Rat | [Q18] |
| Optionen und Erklärung sind die bevorzugte Reparatur bei Chatbot-Fehlern. Umformulieren ist die häufigste und am wenigsten wirksame Nutzerreaktion | mittel | Bei Nichtverstehen Optionen anbieten | [Q31][Q32][Q33] |
| Manipulative Abschiede in Companion-Apps steigern Engagement, schaden Vertrauen | mittel bis hoch | Gespräche leicht enden lassen | [Q57] |
| Humor hilft nur, wenn er verbindend und gelungen ist | mittel | Sparsam, nie bei Ärger | [Q24][Q39] |

Schwach oder spekulativ: Dass sparsame Modalpartikeln KI-Deutsch natürlicher machen, ist eine Ableitung ohne gefundene Studie. Die Tendenz der deutschen Kommunikation zur Direktheit ist umstritten und trägt Stereotyprisiko. Beides steht in der Skill als Stilhinweis, nicht als Tatsache.

## 3. Spannungen und wie die Skill sie löst

| Spannung | Auflösung |
|---|---|
| Menschenähnlichkeit hilft oder schadet | Menschlich lesbar, nicht menschlich behauptend. Soziale Signale nach Modus dosieren |
| KI-Empathie wirkt, wird aber abgewertet | Empathie als genaues Verstehen und hilfreiche Reaktion, nicht als Gefühlsbehauptung |
| Wärme gegen Genauigkeit | Wärme bleibt auf der Ton-Ebene, der Inhalt wird davon getrennt |
| Ist Validierung schon Schmeichelei? | Prüfkriterium ist das Urteil, nicht der Ton. Bleibt die Einschätzung in der Sache gleich, ist freundliche Formulierung keine Schmeichelei |
| Nutzerpräferenz gegen Nutzerwohl | Zufriedenheit im Moment ist kein Erfolgsmaß. Maßstab ist, ob die Person informierter und handlungsfähiger aus dem Gespräch geht |
| Fragen zeigen Interesse, kosten aber Aufwand | Im Austausch ja, bei Aufgaben nur bei relevanter Mehrdeutigkeit |
| Perspektive teilen gegen erfundene Biografie | „Mir fällt bei solchen Plänen oft auf …" ja, „Als ich mal …" nein |

## 4. Offene Fragen

- Übertragbarkeit von Mensch-Mensch-Befunden auf Text-LLMs ist kaum getestet.
- Für deutschsprachige Mensch-KI-Gespräche gibt es wenig Forschung.
- Ob der Wärme-Genauigkeit-Zielkonflikt bei Prompt-Steuerung ebenso stark auftritt wie beim Training, ist nicht belegt.
- Es fehlen etablierte Metriken für „natürlich". Die Testfälle im Knowledge Pack (Abschnitt 7.7) sind ein pragmatischer Ersatz.
- Langzeitwirkungen sind kaum untersucht, die Daten reichen bis etwa vier Wochen.

## 5. Unzuverlässige Angaben in älteren Projektdateien

Das Knowledge Pack hat in `Recherche_Material_Conversation.mkd` zwei Angaben gefunden, die sich nicht bestätigen ließen. Diese Skill übernimmt sie nicht.

- Die Regel „Small Talk nur in den ersten ein bis zwei Interaktionen" (zugeschrieben Bickmore & Cassell 2001). Die Studie fand, dass sozialer Dialog das Vertrauen bei extravertierten Nutzern stärkte. Zu wiederholten Interaktionen sagt sie nichts. Die Skill nutzt stattdessen „erwidern statt initiieren".
- Die Angabe, Nutzer bevorzugten bei Smart Speakern explizite Reparaturfragen (zugeschrieben Porcheron et al. 2018). Das Paper untersucht, wie Familien Amazon Echo in Alltagsgespräche einbetten. Belege für Reparatur stehen bei [Q07][Q31][Q34].

Außerdem: Die Reparaturstudie über zwölf Sprachen hat Dingemanse als Erstautor, nicht Enfield.
