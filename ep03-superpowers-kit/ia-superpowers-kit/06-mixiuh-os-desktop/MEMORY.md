# MEMORIA PERSISTENTE DEL PROYECTO (MEMORY.md)
> **INSTRUCCION PARA EL AGENTE DE IA:** Lee este archivo al inicio de CADA sesion antes de tocar cualquier archivo. Al finalizar cualquier cambio arquitectonico o resolver un bug no trivial, actualiza las secciones correspondientes manteniendo este archivo por debajo de 150 lineas.

## 1. Identidad y Objetivo del Proyecto
- **Nombre del Proyecto:** `MIXIUH OS v4.0 // CYBER-KERNEL DESKTOP`
- **Descripcion en 1 linea:** Entorno de escritorio y sistema operativo web interactivo en un unico archivo HTML autocontenido con gestor de ventanas flotantes, Dock con fisica de resortes y 4 aplicaciones en tiempo real (HoloCore 3D Shader Studio, Mixiuh Kernel Terminal, PulseWave FM Synth & Spectrum Analyzer y Kernel Telemetry & Task Manager).
- **URL de Produccion / Puerto Local:** `http://127.0.0.1:8816/index.html`

## 2. Stack Tecnologico y Comandos Verificados
- **Lenguaje / Runtime:** HTML5 + CSS3 Glassmorphism + ES2024 Vanilla JS (100% autocontenido)
- **Framework Principal:** Motor nativo sin dependencias externas (WebGL Shader Wallpaper, Proyeccion 3D/4D, WebAudio API FM Synth + FFT, Canvas 2D)
- **Comando para levantar entorno local:** `python3 -m http.server 8816 --bind 127.0.0.1`
- **Comando de pruebas / verificacion:** Verificacion de sintaxis JS con Node (`new Function`), auditoria de IDs DOM, cero emojis Unicode y cero recursos externos.

## 3. Reglas Inquebrantables de Arquitectura y Diseño
1. **Cero Codigo Incompleto:** Prohibido dejar comentarios como `// TODO`, `// implementar despues` o funciones vacias.
2. **Verificacion Real Antes de Entregar:** Ninguna tarea se reporta como terminada hasta que el codigo compile sin errores y se haya verificado con cero errores en consola.
3. **Rendimiento y Limpieza:** Bucle maestro unificado (`masterLoop`) con `dt` clamping (`Math.min(rawDt, 0.033)`) y buffers pre-asignados (`Float32Array`, `Uint8Array`) sin recoleccion de basura en tiempo real.
4. **Cero Emojis y Cero Recursos Externos:** Todos los iconos del sistema, controles de ventana y el Dock estan construidos con SVG vectorial inline.

## 4. Mapa de Archivos Clave
- `index.html` — Sistema operativo web completo `MIXIUH OS v4.0` (Window Manager, Top Bar, Physics Dock y 4 aplicaciones en vivo).
- `MEMORY.md` — Este archivo de memoria persistente entre sesiones.
- `GEMINI.md` / `CLAUDE.md` — Protocolo Maestro Mixiuh Labs Superpowers.

## 5. Bitacora de Decisiones Tecnicas (ADR Corto)
- **[2026-10-21]:** Se instalo el **Mixiuh Labs AI Superpowers Kit v1.0** para eliminar la amnesia entre sesiones y exigir auto-verificacion de codigo.
- **[2026-10-22]:** Se implemento `index.html` con arquitectura de bucle unico `requestAnimationFrame`, shader WebGL para el fondo interactivo al cursor, proyeccion 4D de hipercubo/toroide/geodesica con fisica de explosion, terminal `zsh` con lluvia Matrix y sintetizador FM polifonico WebAudio con analizador FFT de 48 bandas.

## 6. Errores Conocidos y Soluciones Aprendidas (No Repetir)
- `[index.html / WebGL Shader]`: `fwidth` requiere `OES_standard_derivatives` en WebGL 1.0 -> Se reemplazo la rejilla derivada por `smoothstep(cos(...))` analitico para garantizar compilacion limpia en cualquier GPU sin depender de extensiones.
- `[index.html / WebAudio API]`: `AudioContext` inicia suspendido hasta el primer gesto del usuario -> Se implemento un sintetizador visual de respaldo sincronizado con el secuenciador hasta que el primer `pointerdown` desbloquea el DSP real a 48kHz.
