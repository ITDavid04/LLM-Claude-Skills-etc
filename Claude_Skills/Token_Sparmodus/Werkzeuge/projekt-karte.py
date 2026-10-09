#!/usr/bin/env python3
"""Projekt-Karte: kompakte Übersicht eines HyperFrames-Projekts.

Statt eine 30-70 KB große index.html komplett in den Kontext zu laden,
liest Claude diese Karte (~1-2 KB) und springt danach gezielt mit
`sed -n 'START,ENDp' index.html` in die Zeilen, die es wirklich braucht.

Aufruf:
    python3 projekt-karte.py <projektordner-oder-html-datei> [...]

Nur Standardbibliothek, keine Abhängigkeiten.
"""

import os
import re
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "source", "track", "wbr"}
SKIP_DIRS = {".git", "node_modules", "vendor", "fonts", "renders",
             "snapshots", ".thumbnails", "__pycache__"}


class Karte(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []      # [tag, eintrag oder None]
        self.clips = []      # Elemente mit Timing-Attributen
        self.blocks = []     # <style>/<script>-Bereiche

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        eintrag = None
        if "data-start" in a or "data-composition-id" in a or "data-composition-src" in a:
            eintrag = {
                "tag": tag, "id": a.get("id", ""), "von": line, "bis": line,
                "start": a.get("data-start", ""), "dauer": a.get("data-duration", ""),
                "track": a.get("data-track-index", ""),
                "comp": a.get("data-composition-id", ""),
                "src": a.get("data-composition-src", "") or a.get("src", ""),
                "tiefe": sum(1 for _, e in self.stack if e),
            }
            self.clips.append(eintrag)
        elif tag in ("style", "script"):
            eintrag = {"tag": tag, "von": line, "bis": line, "src": a.get("src", "")}
            self.blocks.append(eintrag)
        if tag not in VOID:
            self.stack.append([tag, eintrag])

    def handle_endtag(self, tag):
        line = self.getpos()[0]
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for _, e in self.stack[i:]:
                    if e:
                        e["bis"] = line
                del self.stack[i:]
                return


def groesse(n):
    return f"{n / 1024:.1f} KB" if n < 1024 * 1024 else f"{n / 1024 / 1024:.1f} MB"


UEBERSCHRIFT = re.compile(r"^\s*(?:/\*|<!--)\s*[-=]{3,}\s*(.+?)\s*[-=]{3,}\s*(?:\*/|-->)")


def abschnitte(zeilen, maximal=60):
    """Kommentar-Überschriften wie /* ===== 3: Titel ===== */ als Inhaltsverzeichnis."""
    treffer = [(i, m.group(1)) for i, z in enumerate(zeilen, 1)
               if (m := UEBERSCHRIFT.match(z))]
    return treffer[:maximal]


def sprungmarken(zeilen, clips):
    """Wo im Code (außerhalb der Deklaration) wird jede Clip-id erwähnt?"""
    ergebnis = []
    for c in clips:
        if not c["id"]:
            continue
        muster = re.compile(r"(?<![\w-])" + re.escape(c["id"]) + r"(?![\w-])")
        nummern = [i for i, z in enumerate(zeilen, 1)
                   if not c["von"] <= i <= c["bis"] and muster.search(z)]
        if nummern:
            ergebnis.append((c["id"], nummern[:6]))
    return ergebnis


def karte_html(pfad):
    with open(pfad, encoding="utf-8", errors="replace") as f:
        text = f.read()
    p = Karte()
    p.feed(text)
    zeilen = text.count("\n") + 1
    print(f"## {pfad}  ({zeilen} Zeilen, {groesse(len(text.encode()))})")
    if p.clips:
        print("Timeline (Zeilen | id | start+dauer | track | extra):")
        for c in p.clips:
            einzug = "  " * c["tiefe"]
            zeit = f"{c['start'] or '-'}+{c['dauer'] or '-'}s"
            extra = " ".join(x for x in (
                f"comp={c['comp']}" if c["comp"] else "",
                f"src={c['src']}" if c["src"] else "") if x)
            print(f"  {c['von']:>4}-{c['bis']:<4} {einzug}<{c['tag']}> #{c['id'] or '?'}"
                  f"  {zeit}  t{c['track'] or '-'}  {extra}".rstrip())
        anker = sprungmarken(text.splitlines(), p.clips)
        if anker:
            print("Erwähnt in Zeilen (style/script, max. 6):")
            for cid, nummern in anker:
                print(f"  #{cid}: {', '.join(map(str, nummern))}")
    for b in p.blocks:
        quelle = f" src={b['src']}" if b["src"] else f" ({b['bis'] - b['von'] + 1} Zeilen)"
        print(f"  {b['von']:>4}-{b['bis']:<4} <{b['tag']}>{quelle}")
    kapitel = abschnitte(text.splitlines())
    if kapitel:
        print("Abschnitte (Kommentar-Überschriften):")
        for nr, titel in kapitel:
            print(f"  {nr:>4}  {titel}")
    print()


def karte_ordner(ordner):
    print(f"# Projekt-Karte: {os.path.abspath(ordner)}\n")
    html, sonst = [], []
    for wurzel, dirs, dateien in os.walk(ordner):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for d in sorted(dateien):
            pfad = os.path.join(wurzel, d)
            (html if d.endswith(".html") else sonst).append(pfad)
    print("Dateien (ohne vendor/fonts/renders):")
    for pfad in html + sonst:
        print(f"  {os.path.relpath(pfad, ordner)}  {groesse(os.path.getsize(pfad))}")
    print()
    for pfad in html:
        karte_html(pfad)


def main():
    ziele = sys.argv[1:] or ["."]
    for ziel in ziele:
        if os.path.isdir(ziel):
            karte_ordner(ziel)
        elif os.path.isfile(ziel):
            karte_html(ziel)
        else:
            print(f"Nicht gefunden: {ziel}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
