# MEMORIA PERSISTENTE DEL PROYECTO (MEMORY.md)
> **INSTRUCCION PARA EL AGENTE DE IA:** Lee este archivo al inicio de CADA sesion antes de tocar cualquier archivo. Al finalizar cualquier cambio arquitectonico o resolver un bug no trivial, actualiza las secciones correspondientes manteniendo este archivo por debajo de 150 lineas.

## 1. Identidad y Objetivo del Proyecto
- **Nombre del Proyecto:** `NEXUS // NODE SHADER & DSP STUDIO` (`05-motor-nodos-ia`)
- **Descripcion en 1 linea:** Estudio visual interactivo de programacion por nodos (DAG) en tiempo real acoplado a un Viewport WebGL de Raymarching 3D y Sintetizador/Analizador de Audio DSP en un unico archivo autocontenido.
- **URL de Produccion / Puerto Local:** `http://127.0.0.1:8815/index.html`

## 2. Stack Tecnologico y Comandos Verificados
- **Lenguaje / Runtime:** HTML5 + CSS3 + ES2024 Vanilla JS + Canvas 2D + WebGL 1.0 (GLSL ES 1.00) + Web Audio API
- **Framework Principal:** Vanilla WebGL + Motor DAG Custom Zero-Dependencies
- **Comando para levantar entorno local:** `python3 -m http.server 8815 --bind 127.0.0.1`
- **Comando de pruebas / verificacion:** Headless Chrome CDP en puerto aislado `8815` (`0` errores de consola y compilacion GLSL verificada).

## 3. Reglas Inquebrantables de Arquitectura y Diseño
1. **Cero Codigo Incompleto:** Prohibido dejar comentarios como `// TODO`, `// implementar despues` o funciones vacias.
2. **Verificacion Real Antes de Entregar:** Ninguna tarea se reporta como terminada hasta que el codigo compile sin errores y se haya verificado con cero errores en consola del navegador.
3. **Rendimiento y Limpieza (60-120 FPS):** Buffers tipados pre-asignados (`Uint8Array` para FFT/Waveform), paso de tiempo acotado (`Math.min(rawDt, 0.033)`), ordenamiento topologico de Kahn y deteccion de ciclos DFS en $O(V + E)$.
4. **Cero Emojis Unicode:** Todos los iconos del estudio estan trazados con geometria SVG vectorial limpia.

## 4. Mapa de Archivos Clave
- `index.html` — Aplicacion completa autocontenida (UI Cyber-Industrial, Motor de Grafo DAG, Cables Bezier con pulsos de señal, Mini-Canvas por nodo, Sintetizador Web Audio FFT y Viewport 3D Raymarching GLSL).
- `GEMINI.md` / `CLAUDE.md` — Protocolo Maestro Mixiuh Labs Superpowers.
- `MEMORY.md` — Este archivo de memoria persistente entre sesiones.

## 5. Bitacora de Decisiones Tecnicas (ADR Corto)
- **[2026-10-22]:** Se implemento el motor DAG desde cero con ordenamiento topologico de Kahn en vivo, deteccion preventiva de ciclos mediante DFS (`wouldCreateCycle`), auto-layout por capas topologicas (estilo Sugiyama) y acoplamiento directo de uniformes y ecuaciones al Fragment Shader de Raymarching 3D.
- **[2026-10-22]:** Se integro un motor hibrido de Audio DSP (`Web Audio API` con osciladores + filtro resonante + `AnalyserNode` y modo armonico procedural automatico) para garantizar reactividad espectral desde el primer frame sin bloquear por politicas de autoplay.

## 6. Errores Conocidos y Soluciones Aprendidas (No Repetir)
- `[index.html / GLSL ES 1.00]`: `tanh()` y uniformes enteros dinamicos pueden fallar en ciertos drivers WebGL 1.0 -> Se uso mapeo tonal filmico ACES racional y selectores `float` en el shader GLSL.
- `[index.html / Preset 2]`: Un espacio accidental en el identificador de puerto (`' warp'`) impedia conectar el nodo Simplex 4D a la paleta en el Preset 2 -> Corregido a `'warp'` y verificado con `10` cables activos en CDP.
