#!/usr/bin/env bash
set -euo pipefail

echo "============================================================"
echo " MIXIUH LABS — INSTALADOR DE AI SUPERPOWERS KIT (v1.0)"
echo " https://labs.mixiuh.online"
echo "============================================================"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${1:-$(pwd)}"

echo "-> Instalando en el directorio del proyecto: $TARGET_DIR"

# 1. Copiar MEMORY.md sin sobrescribir si ya existe
if [ ! -f "$TARGET_DIR/MEMORY.md" ]; then
  cp "$SCRIPT_DIR/MEMORY.md" "$TARGET_DIR/MEMORY.md"
  echo "   [OK] Creado MEMORY.md (Memoria Persistente Anti-Amnesia)"
else
  echo "   [SKIP] MEMORY.md ya existe (se conservo tu memoria actual)"
fi

# 2. Copiar anclas de contexto para Claude Code, Antigravity/Gemini y Cursor
for anchor in CLAUDE.md GEMINI.md .cursorrules; do
  if [ ! -f "$TARGET_DIR/$anchor" ]; then
    cp "$SCRIPT_DIR/$anchor" "$TARGET_DIR/$anchor"
    echo "   [OK] Instalado $anchor"
  else
    echo "   [SKIP] $anchor ya existe"
  fi
done

# 3. Instalar las 5 Skills en .claude/skills y .gemini/skills
mkdir -p "$TARGET_DIR/.claude/skills" "$TARGET_DIR/.gemini/skills"
cp -R "$SCRIPT_DIR/skills/"* "$TARGET_DIR/.claude/skills/"
cp -R "$SCRIPT_DIR/skills/"* "$TARGET_DIR/.gemini/skills/"
echo "   [OK] 5 Skills instaladas en .claude/skills/ y .gemini/skills/"

echo ""
echo "============================================================"
echo " INSTALACION COMPLETADA CON EXITO"
echo " Para activar el control de navegador (Browser MCP) en Claude Code:"
echo "   claude mcp add playwright npx @playwright/mcp@latest"
echo "============================================================"
