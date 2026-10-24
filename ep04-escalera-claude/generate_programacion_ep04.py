#!/usr/bin/env python3
"""Genera la carpeta programacion/ completa para el Episodio 04 (Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5)
del Miercoles 28 al Viernes 30 de Octubre de 2026 y la sincroniza en iCloud Drive."""
from __future__ import annotations

import shutil
from pathlib import Path

EP04_DIR = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep04-escalera-claude")
PROG_DIR = EP04_DIR / "programacion"
PROG_DIR.mkdir(parents=True, exist_ok=True)

ICLOUD_ROOT = Path("/Users/kevingonzalezlopez/Library/Mobile Documents/com~apple~CloudDocs/Mixiuh/Mixiuh Labs")

FILES: dict[str, str] = {}

FILES["00_INDICE_PROGRAMACION.md"] = """# INDICE DE PROGRAMACION OMNICANAL — EPISODIO 04 (`Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5 — La Escalera Completa de Claude`)

**Cadencia Oficial:** Arranca el **Miercoles 28 de Octubre de 2026** (justo al dia siguiente de concluir el **Episodio 03 — Mixiuh Superpowers Kit** el Martes 27 de Octubre). Se publica el **Video Largo en `4K @ 60fps`** (Espanol e Ingles) el Miercoles 28 por la manana (`11:00 CST`) y **2 Shorts/Reels/TikToks/Tweets por dia** durante 3 dias (**Miercoles 28, Jueves 29 y Viernes 30 de Octubre de 2026**).

## Resumen Ejecutivo del Benchmark Real (`18 Corridas Aisladas en Claude Code CLI`)
- **Marcador Global Triple (`3 - 2 - 1`):** **Claude Opus 5.5 (`3 pts`) — Claude Sonnet 5.5 (`2 pts`) — Claude Haiku 5.5 (`1 pt`)**
- **Tiempo Total Real (`6 Retos`):**
  - **Claude Haiku 5.5 (`claude-haiku-5-5`):** `87.40 min` (`5,243.8s`) | `5,998 lineas`
  - **Claude Sonnet 5.5 (`claude-sonnet-5-5`):** `105.04 min` (`6,302.0s`) | `8,005 lineas`
  - **Claude Opus 5.5 (`claude-opus-5-5`):** `179.20 min` (`10,751.7s`) | `8,900 lineas`
- **Costo Total API Real (`6 Retos`):**
  - **Claude Haiku 5.5:** `$1.54 USD` (`4.87M tokens` · **19.4x mas barato que Opus**)
  - **Claude Sonnet 5.5:** `$12.22 USD` (`4.00M tokens` · **2.45x mas barato que Opus**)
  - **Claude Opus 5.5:** `$29.94 USD` (`4.46M tokens` · `1.19M tokens de salida`)
- **Desglose por Reto:**
  - **Reto 01 (`Rover Planetario 2D Verlet`):** **Gana Opus 5.5 (`1-0-0`)** — Opus (`42.1m | $6.81`) construyo puente colgante de tablones, crateres lunares y faro volumetrico a `61 FPS`; Haiku (`19.2m | $0.35`) funciono a `60 FPS`; Sonnet (`20.1m | $2.51`) trunco el JS (`SyntaxError`).
  - **Reto 02 (`Slime Mold Physarum GPU`):** **Gana Opus 5.5 (`2-0-0`)** — Opus (`13.4m | $2.55`) mapeo 28 estaciones reales de la bahia de Tokio con 60,000 agentes GPU a `60 FPS`; Sonnet (`6.6m | $0.79`) quemo el centro en blanco; Haiku (`5.7m | $0.06`) fallo el shader GLSL (`vec3 to vec4`).
  - **Reto 03 (`Puente Estructural XPBD`):** **Gana Opus 5.5 (`3-0-0`)** — Los 3 funcionaron a `60 FPS` (Haiku `17.9m | $0.30`, Sonnet `17.0m | $1.98`), pero Opus (`19.7m | $3.58`) implemento un solver XPBD de 20 sub-pasos con etiquetas de % de estres en cada viga y pilares submarinos.
  - **Reto 04 (`Sintetizador Acido 3D TB-303 + TR-909`):** **Gana Haiku 5.5 por ROI (`3-0-1`)** — Haiku (`8.7m | $0.21`) entrego terreno espectral 3D de particulas, osciloscopio, 7 perillas giratorias y secuenciador TB-303 + 909 a `61 FPS`, costando **24 veces menos** que Opus (`31.0m | $5.00`).
  - **Reto 05 (`Path Tracer WebGL2 BVH`):** **Gana Sonnet 5.5 (`3-1-1`)** — Sonnet (`13.9m | $1.67`) rindio `29 FPS` con dispersion cromatica arcoiris en cristal y Denoiser A-Trous x4, duplicando los `15 FPS` de Opus (`31.4m | $5.05`) en menos de la mitad de tiempo y a un tercio del costo.
  - **Reto 06 (`Consola Retro CHIP-8 CPU`):** **Gana Sonnet 5.5 (`3-2-1` Final)** — Tanto Haiku (`21.3m | $0.48`) como Sonnet (`35.2m | $3.75`) arrancaron jugando Pong en automatico a `60 FPS` (Sonnet con CRT curvo, barras de registros y editor ASM), mientras que Opus (`41.6m | $6.93`) olvido auto-ensamblar la ROM al inicio (`ROM: 0 B`).

## Rutas de Entregables en iCloud Drive
- **Espanol (`EP04 Escalera Claude`):** `/Users/kevingonzalezlopez/Library/Mobile Documents/com~apple~CloudDocs/Mixiuh/Mixiuh Labs/EP04 Escalera Claude/`
- **Ingles (`EP04 Escalera Claude - English`):** `/Users/kevingonzalezlopez/Library/Mobile Documents/com~apple~CloudDocs/Mixiuh/Mixiuh Labs/EP04 Escalera Claude - English/`

## Archivos de Programacion por Red Social en esta Carpeta

1. [01_YOUTUBE_ESPANOL.md](./01_YOUTUBE_ESPANOL.md) — Canal `@MixiuhLabs` (Video Largo `4K60` + 6 Shorts `4K60` + 6 Portadas `4K PNG`, del 28 al 30 de Octubre).
2. [02_YOUTUBE_INGLES.md](./02_YOUTUBE_INGLES.md) — Canal Ingles (Video Largo `4K60` + 6 Shorts `4K60` + 6 Portadas `4K PNG`, del 28 al 30 de Octubre).
3. [03_INSTAGRAM.md](./03_INSTAGRAM.md) — Cuenta `@mixiuhlabs` (Post Carrusel de lanzamiento + 6 Reels en `4K` vertical `2160x3840 @ 60fps` con portadas `4K PNG`, del 28 al 30 de Octubre).
4. [04_TIKTOK.md](./04_TIKTOK.md) — Cuenta `@mixiuhlabs` (6 TikToks en `4K60` con portadas `4K PNG`, fechas, horas, titulos SEO y descripciones).
5. [05_TWITTER_X.md](./05_TWITTER_X.md) — Cuenta `@mixiuh` (Hilo Maestro de lanzamiento + 2 videos nativos por dia con las 6 comparativas triples `ep04_vs_01..06.png`, del 28 al 30 de Octubre).
"""

FILES["01_YOUTUBE_ESPANOL.md"] = """# PROGRAMACION YOUTUBE ESPANOL (`@MixiuhLabs`) — EPISODIO 04 (`Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5`)

**Regla de Cadencia:** Video Largo `4K @ 60fps` el **Miercoles 28 de Octubre de 2026 a las `11:00 CST`** + **2 Shorts diarios en `4K @ 60fps`** (`12:00/13:00 CST` y `19:00 CST`) los dias **Miercoles 28, Jueves 29 y Viernes 30 de Octubre de 2026**.

---

## 1. VIDEO LARGO PRINCIPAL (`4K @ 60fps`)

- **Fecha de Publicacion:** Miercoles 28 de Octubre de 2026
- **Hora de Publicacion:** `11:00 CST`
- **Archivo de Video (`4K @ 60fps` en iCloud Drive):** `/Users/kevingonzalezlopez/Library/Mobile Documents/com~apple~CloudDocs/Mixiuh/Mixiuh Labs/EP04 Escalera Claude/claude-haiku-vs-sonnet-vs-opus-escalera_2160p60.mp4`
- **Archivo de Subtitulos (`es-MX`):** `/Users/kevingonzalezlopez/Library/Mobile Documents/com~apple~CloudDocs/Mixiuh/Mixiuh Labs/EP04 Escalera Claude/captions_es.srt`
- **Miniaturas para Probar y Comparar (A/B/C Test en YouTube Studio):**
  1. `thumbnails/thumb_A.jpg` (`$1.54 | $29.94`)
  2. `thumbnails/thumb_B.jpg` (`HAIKU | OPUS`)
  3. `thumbnails/thumb_C.jpg` (`3 | 2 | 1`)
- **Titulos para Probar y Comparar (A/B/C Test en YouTube Studio):**
  1. **Titulo A:** `Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5: ¿Vale la Pena Pagar 20 Veces Mas? (4K60)`
  2. **Titulo B:** `Puse a Competir los 3 Niveles de Claude en 6 Retos Extremos ($1.54 vs $12.22 vs $29.94)`
  3. **Titulo C:** `La Escalera Completa de Claude: Cuando Usar Haiku, Sonnet u Opus para Programar`
- **Descripcion Completa (copiar y pegar):**
```text
$1.54 USD por Haiku 5.5, $12.22 USD por Sonnet 5.5 y $29.94 USD por Opus 5.5: ¿realmente vale la pena pagar 20 veces mas al programar con Claude? Corrimos 18 benchmarks aislados en un solo intento con los 3 niveles de Claude 5.5 en 6 retos extremos de fisica, shaders WebGL2, sintesis musical y emulacion de CPU.

El resultado rompio todos los pronosticos: Opus 5.5 arraso en los primeros 3 retos de fisica multicapa y shaders cientificos (3-0), pero en la segunda mitad Haiku 5.5 dio la sorpresa construyendo un estudio Acid Techno 3D a 61 FPS por solo $0.21 USD (24 veces mas barato que Opus), y Sonnet 5.5 gano los ultimos 2 retos duplicando los FPS de Opus en el Path Tracer WebGL2 (29 vs 15 FPS) y arrancando Pong en vivo en la consola CHIP-8 mientras Opus ($6.93 USD) dejo la ROM inicial en 0 bytes.

DEMOS INTERACTIVAS Y PROMPTS
Probar las 18 demos interactivas reales del Episodio 04: https://labs.mixiuh.online
Ver telemetria de costos, tiempos y prompts exactos: https://labs.mixiuh.online

HERRAMIENTAS
- Voz: Voicefy, mi propia voz clonada, corre local en mi Mac.
- Edicion y subtitulos: Reelfy + Mixiuh Labs Studio (mi pipeline propio 4K60).
- Musica: chiptune original generada por codigo (sin samples ni pistas de terceros).
- Stack: claude --model haiku/sonnet/opus --effort high (18 corridas aisladas).

#ClaudeCode #ClaudeOpus #ClaudeSonnet #ClaudeHaiku #MixiuhLabs #Programacion #IA
```
- **Comentario Fijado:**
```text
Prueba las 18 aplicaciones reales (Haiku vs Sonnet vs Opus) en tu navegador y revisa la factura exacta de tokens en https://labs.mixiuh.online — ¿Que nivel de Claude usas en tu dia a dia y para que reservas Opus?
```

---

## 2. CALENDARIO DE LOS 6 SHORTS EN `4K60` (2 POR DIA · 28 AL 30 DE OCTUBRE DE 2026)

### Short #01 — Rover Planetario 2D con Suspension Verlet
- **Fecha:** Miercoles 28 de Octubre de 2026
- **Hora:** `13:00 CST`
- **Archivo `4K60` (`2160x3840`):** `EP04 Escalera Claude/shorts/01_01_rover_suspension.mp4`
- **Portada `4K PNG` (`2160x3840`):** `EP04 Escalera Claude/miniaturas_4k/01_01_rover_suspension_portada_4k.png`
- **Titulo Oficial (Opcion A):** `Rover Planetario Verlet: Haiku ($0.35) vs Sonnet ($2.51) vs Opus ($6.81)`
- **Titulo Alternativo (Opcion B):** `Sonnet Rompio el Codigo y Haiku Funciono por $0.35: Escalera Claude #01`
- **Descripcion (copiar y pegar):**
```text
Reto 01/06 del Episodio 04 (Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5): Rover Planetario con Suspension Verlet y Ley de Hooke.
Punto para Opus 5.5 (Marcador: Opus 1 - Sonnet 0 - Haiku 0). Haiku ($0.35, 19m) entrego un rover funcional a 60 FPS, Sonnet ($2.51, 20m) trunco el script JS en negro, y Opus ($6.81, 42m) construyo un puente colgante de tablones con faro volumetrico y vectores de fuerza.
Prueba las 18 demos y ve el episodio completo en 4K60 en Mixiuh Labs: https://labs.mixiuh.online
#Shorts #ClaudeCode #ClaudeOpus #MixiuhLabs #Programacion #IA
```

### Short #02 — Bio-Red Physarum 100K Agentes GPU
- **Fecha:** Miercoles 28 de Octubre de 2026
- **Hora:** `19:00 CST`
- **Archivo `4K60` (`2160x3840`):** `EP04 Escalera Claude/shorts/02_02_slime_feromonas.mp4`
- **Portada `4K PNG` (`2160x3840`):** `EP04 Escalera Claude/miniaturas_4k/02_02_slime_feromonas_portada_4k.png`
- **Titulo Oficial (Opcion A):** `60,000 Agentes GPU Mapeando Tokio: Haiku ($0.06) vs Sonnet ($0.79) vs Opus ($2.55)`
- **Titulo Alternativo (Opcion B):** `Bio-Red Physarum en WebGL2: Por Que Opus Domina en Shaders Cientificos`
- **Descripcion (copiar y pegar):**
```text
Reto 02/06 del Episodio 04 (Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5): Bio-Red Physarum de Feromonas en GPU WebGL2.
Punto para Opus 5.5 (Marcador: Opus 2 - Sonnet 0 - Haiku 0). Haiku ($0.06, 5.7m) fallo al compilar el shader GLSL, Sonnet ($0.79, 6.6m) logro 60 FPS pero saturo el centro en blanco, y Opus ($2.55, 13.4m) mapeo 28 estaciones reales de la bahia de Tokio a 60 FPS.
Episodio completo en 4K60 en Mixiuh Labs: https://labs.mixiuh.online
#Shorts #ClaudeCode #WebGL #MixiuhLabs #Shaders #IA
```

### Short #03 — Puente Estructural XPBD con Fractura en Vivo
- **Fecha:** Jueves 29 de Octubre de 2026
- **Hora:** `12:00 CST`
- **Archivo `4K60` (`2160x3840`):** `EP04 Escalera Claude/shorts/03_03_puente_estructural.mp4`
- **Portada `4K PNG` (`2160x3840`):** `EP04 Escalera Claude/miniaturas_4k/03_03_puente_estructural_portada_4k.png`
- **Titulo Oficial (Opcion A):** `Simulador de Puentes XPBD: Haiku ($0.30) vs Sonnet ($1.98) vs Opus ($3.58)`
- **Titulo Alternativo (Opcion B):** `Los 3 Niveles de Claude Construyen un Puente con Fractura en Vivo`
- **Descripcion (copiar y pegar):**
```text
Reto 03/06 del Episodio 04 (Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5): Simulador de Puente Estructural con Fractura Progresiva.
Punto para Opus 5.5 (Marcador: Opus 3 - Sonnet 0 - Haiku 0). Los tres modelos lograron 60 FPS (Haiku por $0.30 con camion de 20t y Sonnet por $1.98 con tren pesado), pero Opus ($3.58, 19.7m) implemento un solver XPBD de 20 sub-pasos con porcentaje de esfuerzo impreso en cada viga.
Episodio completo en 4K60 en Mixiuh Labs: https://labs.mixiuh.online
#Shorts #ClaudeCode #Fisica #MixiuhLabs #JavaScript #IA
```

### Short #04 — Estudio Acido 3D TB-303 + TR-909 (Batacazo de Haiku)
- **Fecha:** Jueves 29 de Octubre de 2026
- **Hora:** `19:00 CST`
- **Archivo `4K60` (`2160x3840`):** `EP04 Escalera Claude/shorts/04_04_sintetizador_acido_3d.mp4`
- **Portada `4K PNG` (`2160x3840`):** `EP04 Escalera Claude/miniaturas_4k/04_04_sintetizador_acido_3d_portada_4k.png`
- **Titulo Oficial (Opcion A):** `Por Solo $0.21 USD: Cuando Claude Haiku 5.5 Humilla el Precio de Opus ($5.00)`
- **Titulo Alternativo (Opcion B):** `Estudio Acid Techno 3D (TB-303 + 909): Haiku $0.21 vs Sonnet $1.52 vs Opus $5.00`
- **Descripcion (copiar y pegar):**
```text
Reto 04/06 del Episodio 04 (Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5): Estudio Musical Acid Techno 3D (TB-303 + TR-909 + Tunel FFT).
Punto para Haiku 5.5 por ROI (Marcador: Opus 3 - Sonnet 0 - Haiku 1). En solo 8.7 minutos y por 21 centavos de dolar, Haiku construyo un terreno espectral 3D de particulas, osciloscopio, 7 perillas y secuenciador completo a 61 FPS, costando 24 veces menos que Opus ($5.00 USD, 31 min).
Prueba el sintetizador en vivo en Mixiuh Labs: https://labs.mixiuh.online
#Shorts #ClaudeHaiku #WebAudio #MixiuhLabs #Synth #IA
```

### Short #05 — Path Tracer WebGL2 con BVH y Denoiser
- **Fecha:** Viernes 30 de Octubre de 2026
- **Hora:** `12:00 CST`
- **Archivo `4K60` (`2160x3840`):** `EP04 Escalera Claude/shorts/05_05_pathtracer_bvh.mp4`
- **Portada `4K PNG` (`2160x3840`):** `EP04 Escalera Claude/miniaturas_4k/05_05_pathtracer_bvh_portada_4k.png`
- **Titulo Oficial (Opcion A):** `Sonnet Duplica los FPS de Opus a 1/3 del Costo: Path Tracer WebGL2 BVH`
- **Titulo Alternativo (Opcion B):** `Ray Tracing en Tiempo Real: Haiku ($0.13) vs Sonnet ($1.67) vs Opus ($5.05)`
- **Descripcion (copiar y pegar):**
```text
Reto 05/06 del Episodio 04 (Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5): Motor Path Tracer Monte Carlo en WebGL2 con BVH y Denoiser A-Trous.
Punto para Sonnet 5.5 (Marcador: Opus 3 - Sonnet 1 - Haiku 1). Sonnet ($1.67 USD, 13.9 min) renderizo una Cornell Box Cyberpunk con dispersion cromatica arcoiris en cristal a 29 FPS, casi el doble de fluido que Opus ($5.05 USD, 31.4 min, 15 FPS) y en menos de la mitad de tiempo.
Episodio completo en 4K60 en Mixiuh Labs: https://labs.mixiuh.online
#Shorts #ClaudeSonnet #RayTracing #MixiuhLabs #WebGL2 #IA
```

### Short #06 — Consola Retro CHIP-8 con CPU y Ensamblador
- **Fecha:** Viernes 30 de Octubre de 2026
- **Hora:** `19:00 CST`
- **Archivo `4K60` (`2160x3840`):** `EP04 Escalera Claude/shorts/06_06_consola_retro_cpu.mp4`
- **Portada `4K PNG` (`2160x3840`):** `EP04 Escalera Claude/miniaturas_4k/06_06_consola_retro_cpu_portada_4k.png`
- **Titulo Oficial (Opcion A):** `Opus Gasto $6.93 y Dejo la ROM en 0 Bytes: Consola Retro CHIP-8 (Veredicto 3-2-1)`
- **Titulo Alternativo (Opcion B):** `Emulador CHIP-8 Completo: Haiku ($0.48) y Sonnet ($3.75) Juegan Pong vs Opus ($6.93)`
- **Descripcion (copiar y pegar):**
```text
Reto 06/06 del Episodio 04 (Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5): Consola Retro CHIP-8 con CPU de 35 Opcodes, Desensamblador y Monitor CRT.
Punto para Sonnet 5.5 (Marcador Final: Opus 3 - Sonnet 2 - Haiku 1). Tanto Haiku ($0.48) como Sonnet ($3.75) arrancaron jugando Pong en automatico a 60 FPS con desensamblador en vivo, mientras que Opus ($6.93, 41.6 min) olvido auto-ensamblar la ROM en el arranque (ROM: 0 B).
Juega las 18 demos en vivo en: https://labs.mixiuh.online
#Shorts #ClaudeCode #RetroGaming #MixiuhLabs #Emulador #IA
```
"""

FILES["02_YOUTUBE_INGLES.md"] = """# PROGRAMACION YOUTUBE INGLES — EPISODIO 04 (`Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5`)

**Cadencia Oficial:** Full-Length `4K @ 60fps` Video on **Wednesday, October 28, 2026 at `11:00 CST`** + **2 Daily `4K @ 60fps` Shorts** (`12:00/13:00 CST` and `19:00 CST`) on **Wednesday Oct 28, Thursday Oct 29, and Friday Oct 30, 2026**.

---

## 1. FULL-LENGTH MASTER VIDEO (`4K @ 60fps`)

- **Publish Date:** Wednesday, October 28, 2026 (`11:00 CST`)
- **Video File (`4K @ 60fps` in iCloud Drive):** `/Users/kevingonzalezlopez/Library/Mobile Documents/com~apple~CloudDocs/Mixiuh/Mixiuh Labs/EP04 Escalera Claude - English/claude-haiku-vs-sonnet-vs-opus-ladder-en_2160p60.mp4`
- **Subtitles File (`en-US`):** `/Users/kevingonzalezlopez/Library/Mobile Documents/com~apple~CloudDocs/Mixiuh/Mixiuh Labs/EP04 Escalera Claude - English/captions_en.srt`
- **A/B/C Test Titles:**
  1. `Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5: Is Opus Worth 20x the Price? (4K60)`
  2. `I Tested All 3 Claude Tiers Across 6 Extreme Coding Challenges ($1.54 vs $12.22 vs $29.94)`
  3. `The Full Claude Ladder: When to Use Haiku, Sonnet, or Opus for Coding`
- **Full Description (copy & paste):**
```text
$1.54 USD for Haiku 5.5, $12.22 USD for Sonnet 5.5, and $29.94 USD for Opus 5.5: is Claude Opus really worth paying 20x more than Haiku or 2.5x more than Sonnet? We ran 18 real isolated one-shot benchmarks in Claude Code CLI across 6 extreme physics, WebGL2, audio synthesis, and CPU emulation challenges.

Opus 5.5 swept the first three physics and multi-pass GPU simulations (3-0), but Haiku 5.5 stunned in Round 4 by building a 61 FPS 3D Acid Techno Studio for $0.21 vs Opus's $5.00, and Sonnet 5.5 won Rounds 5 and 6—doubling Opus's FPS in the WebGL2 Path Tracer (29 vs 15 FPS) and booting live Pong on a curved CRT CHIP-8 console while Opus ($6.93) left its initial ROM at 0 bytes.

LIVE DEMOS & PROMPTS
Play all 18 real interactive demos from Episode 04: https://labs.mixiuh.online
Exact prompts and API cost telemetry at Mixiuh Labs: https://labs.mixiuh.online

#ClaudeCode #ClaudeOpus #ClaudeSonnet #ClaudeHaiku #MixiuhLabs #AICoding
```

---

## 2. 6 SHORTS SCHEDULE IN `4K60` (OCT 28 TO OCT 30, 2026)

1. **Short #01 (Wed Oct 28 · `13:00 CST`):** `01_01_rover_suspension.mp4` + `thumbnails_4k/01_01_rover_suspension_portada_4k.png` — *Planetary Rover Verlet Suspension: Haiku ($0.35) vs Sonnet ($2.51) vs Opus ($6.81)*
2. **Short #02 (Wed Oct 28 · `19:00 CST`):** `02_02_slime_feromonas.mp4` + `thumbnails_4k/02_02_slime_feromonas_portada_4k.png` — *60,000 GPU Agents Mapping Tokyo: Haiku ($0.06) vs Sonnet ($0.79) vs Opus ($2.55)*
3. **Short #03 (Thu Oct 29 · `12:00 CST`):** `03_03_puente_estructural.mp4` + `thumbnails_4k/03_03_puente_estructural_portada_4k.png` — *XPBD Structural Bridge Simulator: Haiku ($0.30) vs Sonnet ($1.98) vs Opus ($3.58)*
4. **Short #04 (Thu Oct 29 · `19:00 CST`):** `04_04_sintetizador_acido_3d.mp4` + `thumbnails_4k/04_04_sintetizador_acido_3d_portada_4k.png` — *61 FPS for $0.21 USD: Haiku 5.5 Shocks Opus ($5.00) in 3D Acid Techno Studio*
5. **Short #05 (Fri Oct 30 · `12:00 CST`):** `05_05_pathtracer_bvh.mp4` + `thumbnails_4k/05_05_pathtracer_bvh_portada_4k.png` — *Sonnet Doubles Opus FPS at 1/3 the Cost: WebGL2 BVH Path Tracer*
6. **Short #06 (Fri Oct 30 · `19:00 CST`):** `06_06_consola_retro_cpu.mp4` + `thumbnails_4k/06_06_consola_retro_cpu_portada_4k.png` — *Opus Spent $6.93 and Left a 0-Byte ROM: Retro CHIP-8 Console (Final 3-2-1)*
"""

FILES["03_INSTAGRAM.md"] = """# PROGRAMACION INSTAGRAM (`@mixiuhlabs`) — EPISODIO 04 (`Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5`)

**Regla de Cadencia:** Post Carrusel de anuncio el **Miercoles 28 de Octubre de 2026 (`11:15 CST`)** + **2 Reels diarios en `4K` (`2160x3840 @ 60fps`)** (`12:00/13:00 CST` y `19:00 CST`) los dias **Miercoles 28, Jueves 29 y Viernes 30 de Octubre de 2026**.

---

## 1. POST CARRUSEL DE LANZAMIENTO EP04 (MIERCOLES 28 DE OCTUBRE · `11:15 CST`)

- **Imagen 1 (Portada Split):** `EP04 Escalera Claude/thumbnails/thumb_A.jpg`
- **Imagenes 2 a 7 (Comparativas Triples de los 6 Retos):** `ep04-escalera-claude/benchmark/composites/ep04_vs_01_rover.png` .. `ep04_vs_06_consola.png`
- **Descripcion / Caption (copiar y pegar):**
```text
$1.54 USD en Haiku 5.5, $12.22 USD en Sonnet 5.5 y $29.94 USD en Opus 5.5: ¿en que nivel de Claude conviene gastar tu dinero hoy?

Corrimos 18 pruebas reales y aisladas en Claude Code CLI (los 3 niveles de Claude 5.5 enfrentados al mismo prompt en un solo intento):
- Claude Opus 5.5 gano 3 retos: arraso en la primera mitad con el Rover Planetario con puente colgante ($6.81), la Bio-Red de 60,000 agentes GPU mapeando 28 estaciones de Tokio ($2.55) y el Puente Estructural XPBD con porcentaje de estres por viga ($3.58).
- Claude Haiku 5.5 gano 1 reto historico por ROI: construyo el Estudio Acid Techno 3D (TB-303 + TR-909 + particulas 3D) a 61 FPS en 8.7 minutos por solo $0.21 USD (24 veces mas barato que los $5.00 de Opus).
- Claude Sonnet 5.5 gano los ultimos 2 retos: duplico los FPS de Opus en el Path Tracer WebGL2 (29 FPS vs 15 FPS por $1.67 vs $5.05) y entrego la Consola Retro CHIP-8 jugando Pong en vivo mientras Opus ($6.93) dejo la ROM inicial en 0 bytes.

Marcador Final: Opus 3 - Sonnet 2 - Haiku 1.
El Episodio 04 completo en 4K60 ya esta en el canal de YouTube de Mixiuh Labs, y puedes probar las 18 demos en vivo en labs.mixiuh.online (link en bio).

#ClaudeCode #ClaudeOpus #ClaudeSonnet #ClaudeHaiku #MixiuhLabs #Programacion #InteligenciaArtificial #DesarrolloWeb #WebGL #Coding
```

---

## 2. CALENDARIO DE LOS 6 REELS EN `4K60` (2 POR DIA · 28 AL 30 DE OCTUBRE DE 2026)

1. **Reel #01 (Miercoles 28 Oct · `13:00 CST`):** `EP04 Escalera Claude/shorts/01_01_rover_suspension.mp4` + Portada `miniaturas_4k/01_01_rover_suspension_portada_4k.png` — *EP.04 · RETO 01/06: ROVER PLANETARIO VERLET (Opus 1 - Sonnet 0 - Haiku 0)*
2. **Reel #02 (Miercoles 28 Oct · `19:00 CST`):** `EP04 Escalera Claude/shorts/02_02_slime_feromonas.mp4` + Portada `miniaturas_4k/02_02_slime_feromonas_portada_4k.png` — *EP.04 · RETO 02/06: BIO-RED PHYSARUM GPU (Opus 2 - Sonnet 0 - Haiku 0)*
3. **Reel #03 (Jueves 29 Oct · `12:00 CST`):** `EP04 Escalera Claude/shorts/03_03_puente_estructural.mp4` + Portada `miniaturas_4k/03_03_puente_estructural_portada_4k.png` — *EP.04 · RETO 03/06: PUENTE ESTRUCTURAL XPBD (Opus 3 - Sonnet 0 - Haiku 0)*
4. **Reel #04 (Jueves 29 Oct · `19:00 CST`):** `EP04 Escalera Claude/shorts/04_04_sintetizador_acido_3d.mp4` + Portada `miniaturas_4k/04_04_sintetizador_acido_3d_portada_4k.png` — *EP.04 · RETO 04/06: ESTUDIO ACIDO 3D POR $0.21 (Opus 3 - Sonnet 0 - Haiku 1)*
5. **Reel #05 (Viernes 30 Oct · `12:00 CST`):** `EP04 Escalera Claude/shorts/05_05_pathtracer_bvh.mp4` + Portada `miniaturas_4k/05_05_pathtracer_bvh_portada_4k.png` — *EP.04 · RETO 05/06: PATH TRACER WEBGL2 29 FPS (Opus 3 - Sonnet 1 - Haiku 1)*
6. **Reel #06 (Viernes 30 Oct · `19:00 CST`):** `EP04 Escalera Claude/shorts/06_06_consola_retro_cpu.mp4` + Portada `miniaturas_4k/06_06_consola_retro_cpu_portada_4k.png` — *EP.04 · RETO 06/06: CONSOLA RETRO CHIP-8 CPU (Final: Opus 3 - Sonnet 2 - Haiku 1)*
"""

FILES["04_TIKTOK.md"] = """# PROGRAMACION TIKTOK (`@mixiuhlabs`) — EPISODIO 04 (`Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5`)

**Regla de Cadencia:** **2 TikToks diarios en `4K60` (`2160x3840 @ 60fps`)** (`12:00/13:00 CST` y `19:00 CST`) los dias **Miercoles 28, Jueves 29 y Viernes 30 de Octubre de 2026**.

---

1. **TikTok #01 (Mie 28 Oct · `13:00 CST`):** `01_01_rover_suspension.mp4` + `miniaturas_4k/01_01_rover_suspension_portada_4k.png` — *Escalera de Claude #01: Rover Planetario Verlet. Haiku ($0.35) funciono a 60 FPS, Sonnet ($2.51) rompio el JS y Opus ($6.81) construyo un puente colgante con faro volumetrico. Punto para Opus (1-0-0).*
2. **TikTok #02 (Mie 28 Oct · `19:00 CST`):** `02_02_slime_feromonas.mp4` + `miniaturas_4k/02_02_slime_feromonas_portada_4k.png` — *Escalera de Claude #02: 60,000 agentes GPU mapeando 28 estaciones de Tokio. Haiku ($0.06) fallo en GLSL, Sonnet ($0.79) saturo el centro y Opus ($2.55) clavo 60 FPS. Punto para Opus (2-0-0).*
3. **TikTok #03 (Jue 29 Oct · `12:00 CST`):** `03_03_puente_estructural.mp4` + `miniaturas_4k/03_03_puente_estructural_portada_4k.png` — *Escalera de Claude #03: Puente Estructural XPBD. Los 3 lograron 60 FPS (Haiku $0.30, Sonnet $1.98), pero Opus ($3.58) imprimio el % de estres en cada viga con 20 sub-pasos. Punto para Opus (3-0-0).*
4. **TikTok #04 (Jue 29 Oct · `19:00 CST`):** `04_04_sintetizador_acido_3d.mp4` + `miniaturas_4k/04_04_sintetizador_acido_3d_portada_4k.png` — *El batacazo del torneo: Haiku 5.5 construyo este Estudio Acid Techno 3D (TB-303 + 909) a 61 FPS en 8.7 min por solo $0.21 USD vs $5.00 USD de Opus (24x mas barato). Punto para Haiku (3-0-1).*
5. **TikTok #05 (Vie 30 Oct · `12:00 CST`):** `05_05_pathtracer_bvh.mp4` + `miniaturas_4k/05_05_pathtracer_bvh_portada_4k.png` — *Escalera de Claude #05: Path Tracer WebGL2 BVH. Sonnet 5.5 ($1.67, 13.9m) rindio 29 FPS con dispersion arcoiris en cristal, duplicando los 15 FPS de Opus ($5.05, 31.4m). Punto para Sonnet (3-1-1).*
6. **TikTok #06 (Vie 30 Oct · `19:00 CST`):** `06_06_consola_retro_cpu.mp4` + `miniaturas_4k/06_06_consola_retro_cpu_portada_4k.png` — *Final de la Escalera Claude #06: Consola CHIP-8. Haiku ($0.48) y Sonnet ($3.75) arrancaron jugando Pong a 60 FPS, mientras Opus ($6.93) dejo la ROM inicial en 0 bytes. Marcador Final: Opus 3 - Sonnet 2 - Haiku 1.*
"""

FILES["05_TWITTER_X.md"] = """# PROGRAMACION TWITTER / X (`@mixiuh`) — EPISODIO 04 (`Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5`)

**Regla de Cadencia:** Hilo Maestro de lanzamiento el **Miercoles 28 de Octubre de 2026 (`11:15 CST`)** + **2 videos nativos por dia** (`12:00/13:00 CST` y `19:00 CST`) los dias **Miercoles 28, Jueves 29 y Viernes 30 de Octubre de 2026**.

---

## 1. HILO DE LANZAMIENTO DEL VIDEO LARGO (MIERCOLES 28 DE OCTUBRE · `11:15 CST`)

- **Copy del Tweet Principal (Espanol):**
```text
$1.54 USD por Haiku 5.5, $12.22 USD por Sonnet 5.5 y $29.94 USD por Opus 5.5.
¿Realmente vale la pena pagar 20 veces mas al programar con Claude?

Corri 18 benchmarks aislados en Claude Code CLI (6 retos extremos x 3 niveles en un solo intento):

- Claude Opus 5.5 ($29.94 | 179 min): 3 puntos (gano Rover Verlet, Bio-Red Tokio GPU y Puente XPBD)
- Claude Sonnet 5.5 ($12.22 | 105 min): 2 puntos (gano Path Tracer WebGL2 a 29 FPS y Consola CHIP-8 con Pong en vivo)
- Claude Haiku 5.5 ($1.54 | 87 min): 1 punto (construyo el Estudio Acido 3D a 61 FPS por solo $0.21 USD vs $5.00 de Opus)

Marcador Final: Opus 3 - Sonnet 2 - Haiku 1.
Episodio 04 en 4K60 y las 18 demos en vivo: https://labs.mixiuh.online
```

---

## 2. CALENDARIO DE LOS 6 VIDEOS NATIVOS (2 POR DIA · 28 AL 30 DE OCTUBRE DE 2026)

1. **Tweet #01 (Mie 28 Oct · `13:00 CST`):** `01_01_rover_suspension.mp4` + `ep04_vs_01_rover.png` — *Reto 01/06: Rover Planetario Verlet ($0.35 vs $2.51 vs $6.81). Punto para Opus 5.5 (1-0-0).*
2. **Tweet #02 (Mie 28 Oct · `19:00 CST`):** `02_02_slime_feromonas.mp4` + `ep04_vs_02_slime.png` — *Reto 02/06: Bio-Red Physarum GPU mapeando 28 estaciones de Tokio ($0.06 vs $0.79 vs $2.55). Punto para Opus 5.5 (2-0-0).*
3. **Tweet #03 (Jue 29 Oct · `12:00 CST`):** `03_03_puente_estructural.mp4` + `ep04_vs_03_puente.png` — *Reto 03/06: Puente Estructural XPBD ($0.30 vs $1.98 vs $3.58). Punto para Opus 5.5 (3-0-0).*
4. **Tweet #04 (Jue 29 Oct · `19:00 CST`):** `04_04_sintetizador_acido_3d.mp4` + `ep04_vs_04_acido.png` — *Reto 04/06: Estudio Acido 3D TB-303 + 909. Haiku ($0.21, 8.7m) clavo 61 FPS costando 24x menos que Opus ($5.00, 31m). Punto para Haiku 5.5 (3-0-1).*
5. **Tweet #05 (Vie 30 Oct · `12:00 CST`):** `05_05_pathtracer_bvh.mp4` + `ep04_vs_05_pathtracer.png` — *Reto 05/06: Path Tracer WebGL2 BVH. Sonnet ($1.67, 29 FPS) duplico la fluidez de Opus ($5.05, 15 FPS). Punto para Sonnet 5.5 (3-1-1).*
6. **Tweet #06 (Vie 30 Oct · `19:00 CST`):** `06_06_consola_retro_cpu.mp4` + `ep04_vs_06_consola.png` — *Reto 06/06: Consola Retro CHIP-8. Haiku ($0.48) y Sonnet ($3.75) arrancaron Pong a 60 FPS; Opus ($6.93) dejo la ROM en 0 B. Final: Opus 3 - Sonnet 2 - Haiku 1.*
"""

for fname, content in FILES.items():
    (PROG_DIR / fname).write_text(content, encoding="utf-8")

for icloud_sub in ("EP04 Escalera Claude", "EP04 Escalera Claude - English"):
    dest = ICLOUD_ROOT / icloud_sub / "programacion"
    dest.mkdir(parents=True, exist_ok=True)
    for fname in FILES:
        shutil.copy2(PROG_DIR / fname, dest / fname)

print("Generated 6 scheduling files in:", PROG_DIR)
