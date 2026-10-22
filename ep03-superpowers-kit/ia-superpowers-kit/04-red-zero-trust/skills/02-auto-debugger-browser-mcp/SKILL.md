---
name: 02-auto-debugger-browser-mcp
description: Protocolo de auto-verificacion y reparacion autonoma en navegador usando Chrome DevTools MCP o Playwright antes de entregar cualquier interfaz web, juego o visualizacion.
---

# Skill 02: Auto-Debugger Visual con Browser MCP

## Cuando activar esta habilidad
Activa esta habilidad siempre que crees o modifiques un archivo HTML, CSS, JavaScript, TypeScript, React, Next.js, Canvas 2D o WebGL/Three.js.

## El Ciclo de Auto-Reparacion en 4 Pasos
Prohibido decirle al usuario "Listo" sin haber ejecutado este ciclo:

1. **Levantar Entorno Local:**
   - Si no hay un servidor activo, levanta uno en segundo plano (por ejemplo, `python3 -m http.server 8765` o `npm run dev`).
2. **Inspeccion de Consola y Red (Zero-Error Gate):**
   - Abre la URL en el navegador mediante **Browser MCP** (`chrome-devtools` o `playwright`).
   - Lee todos los mensajes de `console.error`, excepciones no capturadas (`pageerror`) y recursos fallidos (`status >= 400`).
   - Si existe **cualquier error en consola** (por ejemplo, error de compilacion de Shader GLSL, variable `undefined`, o fallo de importacion), analiza la linea exacta, parcha el codigo y recarga la pagina hasta obtener **0 errores**.
3. **Prueba de Interaccion Real:**
   - Haz clic en los botones principales, cambia de pestaña o simula entrada de mouse/teclado para comprobar que el estado de la aplicacion responde.
4. **Auditoria Visual y de Framerate:**
   - Toma una captura o snapshot de la vista renderizada para confirmar que no hay pantallas en blanco, canvas de tamaño `0x0` ni textos superpuestos.
