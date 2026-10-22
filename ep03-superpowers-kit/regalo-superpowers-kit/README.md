# MIXIUH LABS — AI SUPERPOWERS KIT (v1.0)
### Memoria Infinita + Skills de Ingenieria Senior + Auto-Debugging con Browser MCP

Descargado desde **[labs.mixiuh.online](https://labs.mixiuh.online)** (`@MixiuhLabsES` / `@MixiuhLabsEN`).

Este kit gratuito transforma cualquier agente de IA (**Claude Code**, **Google Antigravity / Gemini CLI**, **Cursor**, **Windsurf** o **VS Code Copilot**) de un chatbot con amnesia a un **Ingeniero Senior Autonomo** que:
1. **Nunca olvida tu proyecto entre sesiones** (`MEMORY.md` — Arquitectura de Memoria Persistente Local sin bases de datos pesadas).
2. **Planea antes de programar y optimiza a 60/120 FPS** (`skills/03-arquitecto-senior-120fps/SKILL.md`).
3. **Abre el navegador solo, revisa la consola de errores y repara sus propios bugs antes de entregarte el resultado** (`skills/02-auto-debugger-browser-mcp/SKILL.md`).

---

## INSTALACION EN 1 COMANDO (60 SEGUNDOS)

### Opcion A: Instalador Automatico (macOS / Linux / WSL)
Ejecuta este comando en la raiz de tu proyecto para copiar el ancla de memoria y las 5 Skills automaticamente:

```bash
bash install.sh
```

### Opcion B: Instalacion Manual (Copiar y Pegar)
1. Copia `CLAUDE.md`, `GEMINI.md`, `.cursorrules` y `MEMORY.md` a la carpeta raiz de tu proyecto.
2. Copia la carpeta `skills/` dentro de `.claude/skills/` o `.gemini/skills/` (o en tu carpeta global `~/.gemini/config/skills/`).
3. Para activar la auto-verificacion en navegador (**Browser MCP**), ejecuta:
   - **En Claude Code:**
     ```bash
     claude mcp add playwright npx @playwright/mcp@latest
     ```
   - **En Antigravity (`agy`):**
     El servidor `chrome-devtools` / `playwright` ya viene integrado o se activa desde el panel MCP.

---

## QUE INCLUYE ESTE PAQUETE

| Archivo / Modulo | Funcion Principal | Inspirado en |
| :--- | :--- | :--- |
| `MEMORY.md` | Bitacora viva de arquitectura, stack, decisiones y errores prohibidos. La IA la lee al iniciar y la actualiza al terminar. | `Agent Memory` |
| `CLAUDE.md` / `GEMINI.md` / `.cursorrules` | Reglas maestras de ejecucion para Claude Code, Antigravity/Gemini y Cursor. | Context Anchors |
| `skills/01-memoria-infinita/SKILL.md` | Protocolo para leer y actualizar `MEMORY.md` automaticamente en cada sesion sin gastar tokens innecesarios. | `akitaonrails/ai-memory` |
| `skills/02-auto-debugger-browser-mcp/SKILL.md` | Obliga a la IA a levantar servidor local, abrir navegador headless/MCP, capturar errores de consola y repararlos sola. | `Browser-Use` + `MCP` |
| `skills/03-arquitecto-senior-120fps/SKILL.md` | Metodologia de diseño modular, estructuras de datos $O(N)$ y prohibicion de codigo incompleto o `TODOs`. | `obra/superpowers` |
| `skills/04-auditor-seguridad-y-calidad/SKILL.md` | Auditoria automatica de credenciales expuestas, inyecciones, tipos estrictos y manejo de errores. | DevSecOps |
| `skills/05-automatizador-productividad/SKILL.md` | Comandos rapidos (`/brief`, `/audit`, `/ship`) para resumir repositorios, documentar y preparar despliegues en 1 paso. | Workflow Automation |

---

**Hecho con rigor cientifico en Mixiuh Labs** — *Aqui no se opina: se prueba.*
Visitanos en: https://labs.mixiuh.online
