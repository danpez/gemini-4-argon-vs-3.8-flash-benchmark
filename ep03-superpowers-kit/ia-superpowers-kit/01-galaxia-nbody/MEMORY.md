# MEMORIA PERSISTENTE DEL PROYECTO (MEMORY.md)
> **INSTRUCCION PARA EL AGENTE DE IA:** Lee este archivo al inicio de CADA sesion antes de tocar cualquier archivo. Al finalizar cualquier cambio arquitectonico o resolver un bug no trivial, actualiza las secciones correspondientes manteniendo este archivo por debajo de 150 lineas.

## 1. Identidad y Objetivo del Proyecto
- **Nombre del Proyecto:** MIXIUH LABS // ASTRO-OBS 01 — Simulador 3D N-Body de Colision de Galaxias y Lente Gravitacional Relativista
- **Descripcion en 1 linea:** Observatorio astrofisico interactivo 3D en tiempo real con 36,000 a 60,000 estrellas N-Body, arbol espacial Barnes-Hut Octree 3D, disco de acrecion relativista GLSL y lente gravitacional de Schwarzschild/Einstein.
- **URL de Produccion / Puerto Local:** `http://localhost:8811/index.html` (servidor efimero de verificacion cerrado tras auditoria)

## 2. Stack Tecnologico y Comandos Verificados
- **Lenguaje / Runtime:** HTML5 + CSS3 Glassmorphism + ES2024 Modules + WebGL2 Shaders GLSL
- **Framework Principal:** Three.js `v0.160.0` (`three` + `OrbitControls` via `<script type="importmap">`)
- **Comando para levantar entorno local:** `python3 -m http.server 8811`
- **Comando de pruebas / verificacion:** Verificacion Headless Chromium CDP (`gl.getError() === 0`, `CONSOLE_ERRORS: 0`, `EXCEPTIONS: 0` a 60 FPS)

## 3. Reglas Inquebrantables de Arquitectura y Diseño
1. **Cero Codigo Incompleto:** Prohibido dejar comentarios como `// TODO`, `// implementar despues` o funciones vacias.
2. **Verificacion Real Antes de Entregar:** Ninguna tarea se reporta como terminada hasta que el codigo compile sin errores y se haya verificado con cero errores en consola del navegador y WebGL (`glError === 0`).
3. **Rendimiento y Limpieza (Zero-GC):** Uso estricto de buffers tipados pre-asignados (`Float32Array`, `Int32Array`, `Uint8Array`) en el bucle `requestAnimationFrame` y particion espacial Barnes-Hut Octree 3D.
4. **Cero Recursos Externos ni Emojis:** Prohibido cargar texturas externas o usar emojis Unicode; toda la iconografia usa SVG vectorial y los materiales usan ruido FBM 3D matematico en GLSL.

## 4. Mapa de Archivos Clave
- `index.html` — Aplicacion 100% autocontenida (UI HUD Cyberpunk/Cientifico, motor fisico N-Body 3D, Octree 3D y 5 Shaders GLSL personalizados).
- `GEMINI.md` — Protocolo Maestro de Agente Mixiuh Labs Superpowers.
- `MEMORY.md` — Este archivo de memoria persistente entre sesiones.
- `skills/` — 5 habilidades modulares del kit Superpowers.

## 5. Bitacora de Decisiones Tecnicas (ADR Corto)
- **2026-10-22:** Se implemento el motor N-Body de hasta 60,000 estrellas sobre `Float32Array` contiguos con integracion simplectica, autogravedad baricentrica de halo mediante un Octree 3D de profundidad 6 y friccion dinamica de Chandrasekhar entre nucleos supermasivos.
- **2026-10-22:** Se programaron Shaders GLSL dedicados para: 1) Estrellas con desplazamiento Doppler relativista (`v_radial / c`) y perfil de difraccion Airy, 2) Disco de Acrecion con turbulencia FBM y beaming relativista asimetrico, 3) Lente Gravitacional de Anillo de Einstein (`4GM / c^2 b`), 4) Jets Polares Relativistas y 5) Nebulosa Volumetrica 3D distorsionada por el SMBH primario.

## 6. Errores Conocidos y Soluciones Aprendidas (No Repetir)
- `[index.html / einsteinLensFragmentShader]`: Declaracion GLSL pegada (`floatgravArc`) detectada en revision estatica -> Corregida a `float gravArc` e integrada con ecuacion de lente de Einstein antes de compilacion WebGL (`glError: 0`).
- `[index.html / buildSpatialOctree]`: Profundidad inicial `maxDepth = 4` generaba pocos sub-nodos visibles -> Ajustada a `maxDepth = 6` con `stride` adaptativo para visualizar cientos de celdas 3D a 60 FPS constantes.
