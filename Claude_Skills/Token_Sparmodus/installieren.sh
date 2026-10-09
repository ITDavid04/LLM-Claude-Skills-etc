#!/usr/bin/env bash
# Installiert den Token-Sparmodus als Claude-Code-Skill in ein Projekt.
#
#   bash installieren.sh <ziel-repo>          z. B. bash installieren.sh ~/Hyperframes
#   bash installieren.sh --global             nach ~/.claude/skills (für alle Projekte)
#
# Claude Code erwartet den Skill als <repo>/.claude/skills/<name>/SKILL.md.
set -euo pipefail

quelle="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ziel_arg="${1:-}"

if [[ -z "$ziel_arg" ]]; then
  echo "Aufruf: bash installieren.sh <ziel-repo> | --global" >&2
  exit 1
elif [[ "$ziel_arg" == "--global" ]]; then
  basis="$HOME/.claude/skills"
else
  [[ -d "$ziel_arg" ]] || { echo "Ordner nicht gefunden: $ziel_arg" >&2; exit 1; }
  basis="$(cd "$ziel_arg" && pwd)/.claude/skills"
fi

ziel="$basis/token-sparmodus"
mkdir -p "$ziel"
cp "$quelle/token-sparmodus.md" "$ziel/SKILL.md"
cp -r "$quelle/Referenzen" "$quelle/Werkzeuge" "$ziel/"
chmod +x "$ziel/Werkzeuge/projekt-karte.py"

echo "Installiert: $ziel"
echo "Projekt-Karte testen: python3 $ziel/Werkzeuge/projekt-karte.py <projektordner>"
