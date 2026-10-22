# MEMORIA PERSISTENTE DEL PROYECTO (MEMORY.md)
> **INSTRUCCION PARA EL AGENTE DE IA:** Lee este archivo al inicio de CADA sesion antes de tocar cualquier archivo. Al finalizar cualquier cambio arquitectonico o resolver un bug no trivial, actualiza las secciones correspondientes manteniendo este archivo por debajo de 150 lineas.

## 1. Identidad y Objetivo del Proyecto
- **Nombre del Proyecto:** `CYBER//CORE: OVERLORD` (Arcade Bullet-Hell Boss Rush & WebAudio DSP)
- **Descripcion en 1 linea:** Videojuego Cyberpunk Bullet-Hell Boss Rush autocontenido a 60–120 FPS con 3 fases biomecanicas, 1,500+ proyectiles simultaneos en memoria contigua, Piloto Automatico IA por campos de peligro, Bullet-Time, Spatial Hash Grid y sintetizador Darksynth WebAudio en tiempo real.
- **URL de Produccion / Puerto Local:** `http://127.0.0.1:8813/index.html`

## 2. Stack Tecnologico y Comandos Verificados
- **Lenguaje / Runtime:** HTML5 + CSS3 + ES2024 Vanilla JavaScript (100% autocontenido en `index.html`)
- **Framework Principal:** Canvas 2D Batch Renderer + WebAudio API Procedural Synthesizer + TypedArrays (`Float32Array`, `Int32Array`, `Uint8Array`)
- **Comando para levantar entorno local:** `python3 -m http.server 8813 --bind 127.0.0.1`
- **Comando de pruebas / verificacion:** Verificacion headless via Chrome DevTools Protocol (CDP) en puerto aislado (`0` errores de consola/pagina, `0.54 ms` de tiempo de frame con `1,595` proyectiles activos).

## 3. Reglas Inquebrantables de Arquitectura y Diseño
1. **Cero Codigo Incompleto:** Prohibido dejar comentarios como `// TODO`, `// implementar despues` o funciones vacias.
2. **Verificacion Real Antes de Entregar:** Ninguna tarea se reporta como terminada hasta que el codigo compile sin errores y se haya verificado con cero errores en consola del navegador.
3. **Rendimiento y Limpieza:** Evitar algoritmos $O(N^2)$ en bucles de renderizado o procesamiento de listas grandes; usar `Spatial Hash Grid` ($O(N)$) y lotes de dibujo por color (`Canvas 2D Path Batching`).
4. **Cero Emojis / Cero Recursos Externos:** Toda la iconografia del HUD es SVG vectorial y todo el audio se sintetiza en vivo con nodos `OscillatorNode`, `BiquadFilterNode`, `DynamicsCompressorNode` y `AnalyserNode`.

## 4. Mapa de Archivos Clave
- `index.html` — Motor completo del juego, fisica con Spatial Hash Grid, IA de piloto automatico, sintetizador WebAudio DSP y HUD tactico.
- `GEMINI.md` — Protocolo Maestro Mixiuh Labs Superpowers.
- `MEMORY.md` — Este archivo de memoria persistente entre sesiones.
- `skills/` — 5 habilidades modulares del kit Superpowers (`01-memoria-infinita` a `05-automatizador-productividad`).

## 5. Bitacora de Decisiones Tecnicas (ADR Corto)
- **[2026-10-22]:** Se implemento `CYBER//CORE: OVERLORD` en `index.html` usando estructura de arreglos tipados (`SoA`) pre-asignados (`MAX_BULLETS = 4500`, `MAX_PARTICLES = 2200`, `MAX_CRYSTALS = 2500`) y una rejilla espacial `Spatial Hash Grid` de `64px` para mantener `< 1 ms` de frame time con mas de `1,595` proyectiles simultaneos en Fase 3.

## 6. Errores Conocidos y Soluciones Aprendidas (No Repetir)
- `[index.html / gameLoop & renderScene]`: En el primer cuadro de `requestAnimationFrame(now)`, el timestamp `now` puede ser menor que `performance.now()` inicial, produciendo un `rawDt` negativo y provocando `IndexSizeError: Failed to execute 'arc' on 'CanvasRenderingContext2D': The radius provided is negative` en ondas expansivas -> Se aplico clamping estricto `const dt = Math.max(0.001, Math.min(rawDt, 0.033))` y `Math.max(1, sw.radius)` en `ctx.arc`, validado con 0 errores via CDP.
