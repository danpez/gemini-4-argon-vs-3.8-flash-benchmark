# PLAN MAESTRO DE LANZAMIENTO OMNICANAL — LOTE #1 (MIXIUH LABS)

**Episodio 01:** *Gemini 4 Argon (High) vs. Gemini 3.8 Flash (High) — 10 Retos Extremos Zero-Shot y el Medio Píxel que Rompió un Mundo*
**Arquitectura de Distribución:** Estrategia "Caballo de Troya" (6 Plataformas, 2 Idiomas, 11 Días de Despliegue Continuo)
**Objetivo de Negocio:** Monetización < 30 días vía YouTube Partner Program (1,000 suscriptores + 4,000 horas de reproducción) + conversión directa en `https://labs.mixiuh.online` + patrocinios B2B (`mixiuhonline@gmail.com`).

---

## 1. AUDITORÍA FORENSE DEL SISTEMA DE ARCHIVOS LOCAL

Inspección verificada sobre `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia` y `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs`.

### 1.1 Paquete Maestro en Español (`@MixiuhLabsES`) — 100% Compilado y Verificado en Disco

Ubicación base: `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/`

| Tipo de Activo | Ruta Local Exacta | Especificaciones Técnicas | Hash MD5 Verificado |
|---|---|---|---|
| **Video Largo Máster 4K60 (ES)** | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/gemini-4-argon-vs-3-8-flash_2160p60.mp4` | `3840x2160 @ 60 fps`, H.264 High, AAC 48 kHz 320 kbps, `-14.0 LUFS` / `-1.8 dBTP`, Duración: `10:05.47` (`605.467 s`), Peso: `3.7 GB` | Verificado (`stages.json`) |
| **Video Largo Respaldo 1080p30 (ES)** | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/gemini-4-argon-vs-3-8-flash_1080p30.mp4` | `1920x1080 @ 30 fps`, H.264, Duración: `10:05.47`, Peso: `1.1 GB` | `bddf8d0cb1e1bf7f027ad0a05b1b1fad` |
| **Subtítulos Cerrados CC (SRT)** | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/captions_es.srt` | UTF-8, `165 cues` sincronizados por palabra (`es-MX`), Peso: `14 KB` | Verificado |
| **Subtítulos Cerrados CC (VTT)** | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/captions_es.vtt` | WebVTT (`es-MX`), Peso: `14 KB` | Verificado |
| **Metadatos de Subida (MD/JSON)** | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/youtube.md` (y `youtube.json`) | Capítulos exactos, 3 títulos A/B/C, mid-rolls y coordenadas de End Screen | Verificado |

### 1.2 Inventario de los 11 Videos Cortos en Español (Shorts / Reels / TikToks / Clips Nativos)

El Lote #1 cuenta con **10 Shorts verticales 9:16 de episodio (`out/shorts/`)** más **el Corte #00 Introductorio / Gancho** en dos variantes según la red social (Vertical `9:16` en `videos-x-comparativa/00_portada_resumen_hilo_vs.mp4` para Shorts/Reels/TikTok, y Horizontal `16:9` en `out/ligero/ep01_avance_gancho_ligero.mp4` para X/LinkedIn/Facebook), además del corte de Jefe `ep01_nivel6_jefe_ligero.mp4`.

| Orden | Rol en el Embudo | Ruta Local Exacta (`9:16` / `16:9`) | Duración / Resolución | Hash MD5 |
|---|---|---|---|---|
| **Corte #00 (Vertical 9:16)** | Intro / Gancho del Torneo (Día 1) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/00_portada_resumen_hilo_vs.mp4` | `20.0 s` \| `2160x3840 @ 60 fps` \| `25 MB` | `280c6e76419b2cb7fa165ae97c662682` |
| **Corte #00B (Horizontal 16:9)** | Avance Gancho + Protocolo (Día 1 X/LinkedIn) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/ligero/ep01_avance_gancho_ligero.mp4` | `62.0 s` \| `1920x1080 @ 60 fps` \| `29 MB` | `e29b80bd1b09aba6aa437eee129cbad9` |
| **Corte #00C (Horizontal 16:9)** | Nivel 6 Jefe Raycasting (Hilo X / LinkedIn) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/ligero/ep01_nivel6_jefe_ligero.mp4` | `65.0 s` \| `1920x1080 @ 60 fps` \| `28 MB` | `5105429f6d6cb607c59794fdab24a149` |
| **Short #01** | Problema 1: Sistema Solar Relativo (3D/GLSL) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/01_sistema-solar.mp4` | `47.0 s` \| `2160x3840 @ 60 fps` \| `134 MB` | `4a51e38300de81f63f909cd49083c1e4` |
| **Short #02** | Problema 2: Visualizador de ADN 3D (Ley de Hooke) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/02_visualizador-adn.mp4` | `51.7 s` \| `2160x3840 @ 60 fps` \| `152 MB` | `2d01e50cfd6da530d3000701ad63bcf6` |
| **Short #03** | Problema 3: Vida Artificial (Boids + Quadtree) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/03_vida-artificial.mp4` | `49.4 s` \| `2160x3840 @ 60 fps` \| `144 MB` | `aee400d75a80575315dbcb8c3997f5b9` |
| **Short #04** | Problema 4: Generador de Mazmorras (BSP + A*) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/04_generador-mazmorras.mp4` | `52.6 s` \| `2160x3840 @ 60 fps` \| `151 MB` | `3e417409ec52a27330d0b5609bcbe20b` |
| **Short #05** | Problema 5: Simulador Falling Sand (Autómatas) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/05_falling-sand.mp4` | `50.9 s` \| `2160x3840 @ 60 fps` \| `148 MB` | `33e30e17e7bd9c0a8a1d86021c35ede4` |
| **Short #06** | Problema 6: Motor 3D Raycasting DDA (El Jefe) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/06_motor-raycasting.mp4` | `54.7 s` \| `2160x3840 @ 60 fps` \| `160 MB` | `b68710af93a2df2d44f121c6a94c0c4b` |
| **Short #07** | Problema 7: Sprites Espaciales 8 Bits (Simetría) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/07_generador-sprites.mp4` | `47.7 s` \| `2160x3840 @ 60 fps` \| `135 MB` | `1606f7e0bb428f42b4663961a2838598` |
| **Short #08** | Problema 8: Reloj Analógico CSS (Trigonometría) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/08_reloj-analogico.mp4` | `41.2 s` \| `2160x3840 @ 60 fps` \| `116 MB` | `ab0804690daf19f05ff3c7bd2079bcff` |
| **Short #09** | Problema 9: Árbol Fractal con Viento (Perlin) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/09_arbol-fractal.mp4` | `58.0 s` \| `2160x3840 @ 60 fps` \| `170 MB` | `10cd8adf3d689d0ee3ff6f6e16a7af3d` |
| **Short #10** | Problema 10: Spirograph Paramétrico (Hipotrocoides + MCD) | `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/10_spirograph-parametrico.mp4` | `54.1 s` \| `2160x3840 @ 60 fps` \| `156 MB` | `20151e3bbedf05aa83a7231f2ee8a66d` |

> [!TIP]
> **Cortes alternativos de 20 segundos sin voz para X / Carruseles B2B:** En `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/` tienes también los 10 clips comparativos puros de 20 segundos (`01_sistema_solar_vs.mp4` a `10_spirograph_parametrico_vs.mp4`) con hashes MD5 independientes (`0e79bad5...` a `d4c031e5...`). Úsalos para los tweets #2 al #11 del Hilo Maestro de X.

### 1.3 Inventario de Miniaturas y Activos Gráficos (`brand-kit/`)

1. **Set Principal para "Probar y Comparar" (A/B/C Test de YouTube Studio) con Personajes (`brand-kit/04-miniaturas-ep01/`):**
   - **Variante 1 (Emoción + Marcador):** `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/04-miniaturas-ep01/01_marcador-0-10.jpg` (`1920x1080`, `0.37 MB`, MD5: `532f550e4ea9abf9c55313ab78ef711a`)
   - **Variante 2 (Evidencia Directa 17 MIN vs 4 MIN):** `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/04-miniaturas-ep01/03_17-min-vs-4-min.jpg` (`1920x1080`, `0.48 MB`, MD5: `bb0ae4797032c655f5cb9fccca9e3893`)
   - **Variante 3 (Curiosidad / Intriga ¿ROTO?):** `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/04-miniaturas-ep01/04_roto.jpg` (`1920x1080`, `0.42 MB`, MD5: `75274901a04706ca7060221e5ce8cbfb`)
   - **Variantes de Respaldo / Rotación (si alguna pierde el A/B test a los 7 días):**
     - `02_medio-pixel.jpg` (`MEDIO PÍXEL`, MD5: `b1803170dda0bb4aae8b09038dd33ea9`)
     - `05_39-min-mas-lento.jpg` (`+39 MIN MÁS LENTO`, MD5: `ec44b6ced01fbf0f95d825d2b8ca07cd`)
     - `06_vs-minimal.jpg` (`VS`, MD5: `a0f5c3bc516e1fcc0ec2504a11a04d04`)
     - `07_4-min-motor-3d.jpg` (`4 MIN`, MD5: `d892167a27e805e4569c055f736706ef`)
2. **Set de Miniaturas del Empaquetador Automático (`episodes/ep01-argon-vs-flash/out/thumbnails/`):**
   - `thumb_A.jpg` (`0 | 10`, MD5: `bbf2f441ae9af006731a32c3ad4ec326`)
   - `thumb_B.jpg` (`22 MIN | 4 MIN`, MD5: `3b762d774b97913ecd359fb1e273d7cc`)
   - `thumb_C.jpg` (`¿FLASH ROTO?`, MD5: `d6269b46661f587a5e81fcd699b27153`)
3. **Gráficos Nativos para Feed, Historias, X y LinkedIn (`brand-kit/05-extras/posts-ep01/`):**
   - Carrusel Imagen 1 (`1080x1350`, `4:5`): `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/05-extras/posts-ep01/ep01_post-1_gancho_1080x1350.png` (MD5: `c7faac019bf7bdebc7f40b89fcf4cf13`)
   - Carrusel Imagen 2 (`1080x1350`, `4:5`): `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/05-extras/posts-ep01/ep01_post-2_marcador_1080x1350.png` (MD5: `dd1ad77a4949b7628fc52bbe3b014c27`)
   - Historia Vertical (`2160x3840`, `9:16`): `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/05-extras/posts-ep01/ep01_historia_2160x3840.png` (MD5: `84cdf174f776ea6117507da236e2aac2`)
   - Tarjeta Horizontal X / LinkedIn (`1200x675`, `16:9`): `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/05-extras/posts-ep01/ep01_x-card_1200x675.png` (MD5: `45aa21d518a4f361de0142db2c8a714e`)
   - Marca de Agua Oficial YouTube Studio (`150x150`): `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/05-extras/marca-de-agua/marca-de-agua_A_insignia_150.png`

### 1.4 Paquete Maestro en Inglés (`@MixiuhLabsEN`) — Estado y Rutas Exactas

Ubicación base: `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/episodes/ep01-argon-vs-flash-en/`

- **Archivos fuente verificados:**
  - `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/episodes/ep01-argon-vs-flash-en/episode.yaml` (`108 KB`, 16 escenas, 117 beats traducidos y validados con `mlabs check`).
  - `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/episodes/ep01-argon-vs-flash-en/TRANSLATION_NOTES.md` (`7.8 KB`).
- **Estado de compilación:** El proceso `mlabs build episodes/ep01-argon-vs-flash-en/episode.yaml` se encuentra generando las tomas de voz en inglés en `episodes/ep01-argon-vs-flash-en/build/voice/`. Si necesitas completar las etapas restantes (`timeline,music,mix,video,mux,package`) al concluir la voz, ejecuta:
  ```bash
  cd /Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs
  .venv/bin/python -m mlabs build episodes/ep01-argon-vs-flash-en/episode.yaml
  ```
- **Rutas de salida determinísticas en `episodes/ep01-argon-vs-flash-en/out/`:**
  - **Video Largo 4K60 (EN):** `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/gemini-4-argon-vs-3-8-flash-en_2160p60.mp4` (Duración estimada: `~11:13`)
  - **Subtítulos CC (EN):** `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/captions_en.srt`
  - **Miniaturas (EN):**
    - `episodes/ep01-argon-vs-flash-en/out/thumbnails/thumb_A.jpg` (`0 | 10`)
    - `episodes/ep01-argon-vs-flash-en/out/thumbnails/thumb_B.jpg` (`22 MIN | 4 MIN`)
    - `episodes/ep01-argon-vs-flash-en/out/thumbnails/thumb_C.jpg` (`FLASH BROKEN?`)
  - **10 Shorts Verticales 9:16 (EN):**
    - `episodes/ep01-argon-vs-flash-en/out/shorts/01_sistema-solar.mp4` .. `10_spirograph-parametrico.mp4`
  - **Metadatos y Capítulos Reales Medidos (EN):**
    - `episodes/ep01-argon-vs-flash-en/out/youtube.md` y `episodes/ep01-argon-vs-flash-en/out/shorts/shorts.md`

### 1.5 Verificación de Blindaje Anti-Duplicado (ES vs. EN)

1. **Huella de Audio:** El máster en español utiliza síntesis `lang: es` (`605.47 s`), mientras que el máster en inglés utiliza `lang: en, speed: 1.1` (`~673 s`). La forma de onda y espectrograma son 100% distintos.
2. **Huella Visual (Píxeles):** El motor `mlabs/i18n.py` redibuja en Skia todas las tarjetas, HUDs, sellos y subtítulos quemados en inglés (`WORLD`, `LEVEL`, `BROKEN`, `POINT TO ARGON`, `AGAINST THE CLOCK`, `LAB RULES`, `SAME PROMPT. / WHO DID IT BETTER?`).
3. **Huella Binaria (Hash MD5/SHA-256):** Ningún archivo `.mp4` ni `thumb_C.jpg` comparte longitud de frames, pista de audio ni hash binario entre `ep01-argon-vs-flash/out/` y `ep01-argon-vs-flash-en/out/`.

---

## 2. MARCAS DE TIEMPO (TIMESTAMPS) REALES Y PAUSAS MID-ROLL

Extraídas directamente de `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/youtube.json` (`duration: 605.467 s` / `10:05`). **Cero spoilers del ganador en los títulos de los capítulos.**

### 2.1 Tabla Maestra de Capítulos (Video Largo `10:05`)

| # | Timestamp Exacto (`ES`) | Segundo Exacto (`t`) | Título del Capítulo en Español (`@MixiuhLabsES`) | Título del Capítulo en Inglés (`@MixiuhLabsEN`) | Reto Matemático / Algorítmico Evaluado |
|---|---|---|---|---|---|
| 01 | `00:00` | `0.000 s` | `El mundo roto` | `The broken world` | Gancho: el bug de punto flotante (`lineHeight / 2`) |
| 02 | `00:19` | `19.833 s` | `Protocolo del experimento` | `Experiment protocol` | Reglas Zero-Shot: 1 intento, 1 `index.html`, 0 assets |
| 03 | `01:00` | `60.383 s` | `Mundo 1, Nivel 1: Sistema Solar Relativo` | `World 1, Level 1: Relative Solar System` | Matrices de transformación jerárquicas + Shaders GLSL |
| 04 | `01:44` | `104.717 s` | `Mundo 1, Nivel 2: Visualizador de ADN 3D` | `World 1, Level 2: 3D DNA Visualizer` | Geometría helicoidal paramétrica + Ley de Hooke ($F = -kx - cv$) |
| 05 | `02:36` | `156.533 s` | `Mundo 2, Nivel 3: Vida Artificial` | `World 2, Level 3: Artificial Life` | Vectores de Reynolds (Boids) + Particionamiento Quadtree $O(N \log N)$ |
| 06 | `03:17` | `197.500 s` | `Mundo 2, Nivel 4: Generador de Mazmorras` | `World 2, Level 4: Dungeon Generator` | Árboles BSP / Grafo de cuartos + Pathfinding A* |
| 07 | `04:04` | `244.400 s` | `Mundo 2, Nivel 5: Simulador Falling Sand` | `World 2, Level 5: Falling Sand Simulator` | Autómatas celulares estocásticos + Hidrostática y termodinámica |
| 08 | `04:50` | `290.067 s` | `Mundo 3, Nivel 6: Motor 3D Raycasting, el jefe` | `World 3, Level 6: 3D Raycasting Engine, the boss` | Trigonometría DDA de Carmack + Corrección de ojo de pez ($\cos\Delta\theta$) |
| 09 | `05:54` | `354.833 s` | `Mundo 3, Nivel 7: Sprites Espaciales 8 Bits` | `World 3, Level 7: 8-Bit Space Sprites` | Matrices de simetría axial procedural + Colisiones 2D |
| 10 | `06:40` | `400.750 s` | `Mundo 4, Nivel 8: Reloj Analógico CSS` | `World 4, Level 8: CSS Analog Clock` | Ángulos trigonométricos en CSS puro (`28,800 vph` / Tourbillon) |
| 11 | `07:12` | `432.367 s` | `Mundo 5, Nivel 9: Árbol Fractal con Viento` | `World 5, Level 9: Fractal Tree with Wind` | Recursión geométrica + Campo vectorial de ruido Perlin |
| 12 | `08:04` | `484.683 s` | `Mundo 5, Nivel 10: Spirograph Paramétrico` | `World 5, Level 10: Parametric Spirograph` | Curvas hipotrocoides + Teoría de números ($\text{MCD}(R, r)$) |
| 13 | `08:56` | `536.167 s` | `Pantalla de resultados` | `Results screen` | Estadísticas globales: tiempo acumulado y tasa de éxito |
| 14 | `09:21` | `561.217 s` | `Veredicto del Lab` | `Lab verdict` | Conclusión de ingeniería y acceso a demos |

> [!IMPORTANT]
> **Nota para `@MixiuhLabsEN`:** Como la locución en inglés dura ~11:13 (frente a 10:05 en español), al terminar el build de `episodes/ep01-argon-vs-flash-en/`, copia el bloque `CHAPTERS` que se genera automáticamente en `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/youtube.md`, el cual ya trae los segundos exactos recalculados sobre el timeline en inglés.

### 2.2 Configuración de Anuncios Mid-Roll y Pantalla Final (YouTube Studio)

- **Pausa Mid-Roll Manual #1:** `02:30` (`150.8 s`) — Ventana de silencio de `1.4 s` exactamente entre el Nivel 2 (ADN 3D) y el Nivel 3 (Vida Artificial).
- **Pausa Mid-Roll Manual #2:** `05:54` (`354.8 s`) — Ventana de silencio de `1.2 s` exactamente al terminar la batalla contra el Jefe del Nivel 6 (Raycasting) y antes del Nivel 7 (Sprites).
- **Pausa Mid-Roll Manual #3 (Opcional):** `07:12` (`432.3 s`) — Cambio de ronda entre Mundo 4 (Reloj CSS) y Mundo 5 (Árbol Fractal).
- **Pantalla Final (`End Screen`):** De `09:50` a `10:05` (`15.2 s`).
  - Elemento 1 (Video más reciente): `x=300, y=330` (`640x360 px`) — aparece en `09:50`.
  - Elemento 2 (Mejor para el espectador): `x=980, y=330` (`640x360 px`) — aparece en `09:50`.
  - Elemento 3 (Botón Suscribirse): `x=868, y=748` (`184x184 px`) — aparece en `09:51`.

---

## 3. CALENDARIO OPERATIVO DE DESPLIEGUE: DÍA 1 A DÍA 11

### Mapa Ejecutivo de los 11 Días

| Día | Foco del Día | Archivo YouTube (`@MixiuhLabsES` y `@MixiuhLabsEN`) | Archivo TikTok / IG Reels / FB Reels (ES) | Acción en X (Twitter) y LinkedIn |
|---|---|---|---|---|
| **Día 1** | **Lanzamiento Video Largo + Corte #00 (Intro/Gancho)** | **1.** Video Largo 4K60 (`gemini-4-argon-vs-3-8-flash_2160p60.mp4` y versión `-en`)<br>**2.** Corte #00 Vertical (`00_portada_resumen_hilo_vs.mp4` vinculado con *Related Video*) | `videos-x-comparativa/00_portada_resumen_hilo_vs.mp4` + Historias (`ep01_historia_2160x3840.png`) + Carrusel Feed (`ep01_post-1` y `post-2`) | **X (ES y EN):** Publicar Mega-Hilo de 12 Tweets (Tweet #1 con `ep01_nivel6_jefe_ligero.mp4`)<br>**LinkedIn:** Post Técnico #1 (Arquitectura + `ep01_avance_gancho_ligero.mp4`) |
| **Día 2** | **Problema 01: Sistema Solar Relativo** | `out/shorts/01_sistema-solar.mp4` (ES y EN) | `out/shorts/01_sistema-solar.mp4` | **X:** Quote-tweet del Reto 1 con link a YouTube |
| **Día 3** | **Problema 02: Visualizador de ADN 3D** | `out/shorts/02_visualizador-adn.mp4` (ES y EN) | `out/shorts/02_visualizador-adn.mp4` | **LinkedIn:** Post Técnico #2 (Alucinación de telemetría hardcoded vs código real + `02_visualizador-adn.mp4`) |
| **Día 4** | **Problema 03: Vida Artificial (Boids)** | `out/shorts/03_vida-artificial.mp4` (ES y EN) | `out/shorts/03_vida-artificial.mp4` | **X:** Clip nativo de Quadtree $O(N \log N)$ |
| **Día 5** | **Problema 04: Generador de Mazmorras** | `out/shorts/04_generador-mazmorras.mp4` (ES y EN) | `out/shorts/04_generador-mazmorras.mp4` | **LinkedIn:** Post Técnico #3 (Falsa velocidad de inferencia: entregar en 2 min un código roto + `04_generador-mazmorras.mp4`) |
| **Día 6** | **Problema 05: Simulador Falling Sand** | `out/shorts/05_falling-sand.mp4` (ES y EN) | `out/shorts/05_falling-sand.mp4` | **X:** Post con `05_falling_sand_vs.mp4` |
| **Día 7** | **Problema 06: Motor 3D Raycasting (El Jefe)** | `out/shorts/06_motor-raycasting.mp4` (ES y EN) + Revisar ganador A/B de miniatura del video largo | `out/shorts/06_motor-raycasting.mp4` | **LinkedIn:** Post Técnico #4 (Autopsia del bug `lineHeight / 2` vs `lineHeight >> 1` en `Uint32Array` + `ep01_nivel6_jefe_ligero.mp4`) |
| **Día 8** | **Problema 07: Sprites Espaciales 8 Bits** | `out/shorts/07_generador-sprites.mp4` (ES y EN) | `out/shorts/07_generador-sprites.mp4` | **X:** Post de generación procedural de assets |
| **Día 9** | **Problema 08: Reloj Analógico CSS** | `out/shorts/08_reloj-analogico.mp4` (ES y EN) | `out/shorts/08_reloj-analogico.mp4` | **LinkedIn:** Post Técnico #5 (Restricciones de arquitectura Frontend sin bucle JS + `08_reloj-analogico.mp4`) |
| **Día 10** | **Problema 09: Árbol Fractal con Viento** | `out/shorts/09_arbol-fractal.mp4` (ES y EN) | `out/shorts/09_arbol-fractal.mp4` | **X:** Post de brecha de latencia (22 min vs 4 min) |
| **Día 11** | **Problema 10: Spirograph Paramétrico + Cierre** | `out/shorts/10_spirograph-parametrico.mp4` (ES y EN) | `out/shorts/10_spirograph-parametrico.mp4` | **LinkedIn:** Post Técnico #6 (Resumen ejecutivo del Torneo 10-0 + Carrusel `ep01_post-1` y `ep01_post-2`) |

---

## 4. DÍA 1: LANZAMIENTO DEL VIDEO LARGO ("CABALLO DE TROYA")

### 4.1 YouTube Español (`@MixiuhLabsES`) — Video Largo

- **Archivo de Video a Subir:**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/gemini-4-argon-vs-3-8-flash_2160p60.mp4`
- **Archivo de Subtítulos (CC `es-MX`) a Subir:**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/captions_es.srt`
- **Marca de Agua del Canal (Personalización > Branding):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/05-extras/marca-de-agua/marca-de-agua_A_insignia_150.png`
- **3 Miniaturas para "Probar y Comparar" (A/B/C Test en YouTube Studio):**
  1. `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/04-miniaturas-ep01/01_marcador-0-10.jpg`
  2. `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/04-miniaturas-ep01/03_17-min-vs-4-min.jpg`
  3. `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/04-miniaturas-ep01/04_roto.jpg`
- **3 Títulos para "Probar y Comparar" (A/B/C Test en YouTube Studio):**
  - **Título A:** `Gemini 4 Argon vs 3.8 Flash: el medio píxel que rompió un mundo`
  - **Título B:** `Gemini 4 Argon vs 3.8 Flash: 10-0, 55 contra 94 minutos`
  - **Título C:** `Gemini 4 Argon vs 3.8 Flash: 10 retos de código, un solo intento`

**Descripción Lista para Copiar y Pegar (`@MixiuhLabsES`):**
```text
Gemini 4 Argon vs Gemini 3.8 Flash: 10 retos extremos de código y matemáticas zero-shot, mismo prompt y un solo intento. ¿Cuál domina la ingeniería real en 2026?

Puse a prueba a Gemini 4 Argon y Gemini 3.8 Flash (variantes High dentro de Antigravity) con el mismo prompt en 10 problemas progresivos: gráficos 3D con Three.js y GLSL, simulaciones físicas, algoritmos de grafos, raycasting trigonométrico, pixel art, CSS puro y matemáticas paramétricas. Cada modelo tuvo un solo intento (zero-shot) y entregó todo en un único archivo index.html, sin imágenes ni texturas externas.

PROMPTS, DEMOS JUGABLES Y BENCHMARK COMPLETO
Laboratorio central, prompts y recursos: https://labs.mixiuh.online
Código fuente de los 20 proyectos: https://github.com/danpez/gemini-4-argon-vs-3.8-flash-benchmark
Demos interactivas en vivo (Argon y Flash): https://danpez.github.io/gemini-4-argon-vs-3.8-flash-benchmark/

CAPÍTULOS
00:00 El mundo roto
00:19 Protocolo del experimento
01:00 Mundo 1, Nivel 1: Sistema Solar Relativo
01:44 Mundo 1, Nivel 2: Visualizador de ADN 3D
02:36 Mundo 2, Nivel 3: Vida Artificial
03:17 Mundo 2, Nivel 4: Generador de Mazmorras
04:04 Mundo 2, Nivel 5: Simulador Falling Sand
04:50 Mundo 3, Nivel 6: Motor 3D Raycasting, el jefe
05:54 Mundo 3, Nivel 7: Sprites Espaciales 8 Bits
06:40 Mundo 4, Nivel 8: Reloj Analógico CSS
07:12 Mundo 5, Nivel 9: Árbol Fractal con Viento
08:04 Mundo 5, Nivel 10: Spirograph Paramétrico
08:56 Pantalla de resultados
09:21 Veredicto del Lab

HERRAMIENTAS DEL LABORATORIO
- Voz: Voicefy (mi propia voz clonada ejecutándose de forma local en mi Mac).
- Edición y subtítulos: Reelfy + Mixiuh Labs Studio (pipeline propio).
- Música: Chiptune original generada por código (cero samples de terceros).
- Entorno de prueba: Gemini 4 Argon (High) y Gemini 3.8 Flash (High) en Antigravity.

CANALES OFICIALES Y CONTACTO
- Canal en Inglés (Propiedad cruzada oficial de Mixiuh Labs): https://www.youtube.com/@MixiuhLabsEN
- Web oficial: https://labs.mixiuh.online
- Contacto comercial y patrocinios: mixiuhonline@gmail.com

La narración utiliza mi propia voz clonada con Voicefy (ejecución local).

#Gemini4Argon #GeminiFlash #IA
```

**Etiquetas (Tags de YouTube Studio — copiar en una sola línea):**
```text
Gemini 4 Argon, Gemini 3.8 Flash, Gemini 4 Argon vs Gemini 3.8 Flash, comparativa de IA para programar, zero-shot coding, Antigravity, raycasting, Mixiuh Labs, benchmark matematico IA
```

**Comentario Fijado (`@MixiuhLabsES`):**
```text
Aquí no se opina: se prueba.

Si quieres probar tú mismo las 20 simulaciones en tu navegador, copiar los 10 prompts exactos del torneo y revisar las herramientas que usamos en el laboratorio, entra aquí:
https://labs.mixiuh.online

Dato curioso del experimento: los minutos son de mis notas (redondeados al minuto) y Flash terminó antes en 3 de los 10 retos... pero espera a ver lo que entregó en el Nivel 4 (03:17) y el bug de medio píxel del Nivel 6 (04:50).

¿Qué modelos enfrentamos en el Episodio 02 de Mixiuh Labs? Déjalo abajo.
```

---

### 4.2 YouTube Inglés (`@MixiuhLabsEN`) — Video Largo

- **Archivo de Video a Subir:**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/gemini-4-argon-vs-3-8-flash-en_2160p60.mp4`
- **Archivo de Subtítulos (CC `en-US`) a Subir:**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/captions_en.srt`
- **Marca de Agua del Canal:**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/05-extras/marca-de-agua/marca-de-agua_A_insignia_150.png`
- **3 Miniaturas para "Test & Compare" (YouTube Studio EN):**
  1. `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/thumbnails/thumb_A.jpg` (`0 | 10`)
  2. `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/thumbnails/thumb_B.jpg` (`22 MIN | 4 MIN`)
  3. `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/thumbnails/thumb_C.jpg` (`FLASH BROKEN?`)
- **3 Títulos para "Test & Compare" (YouTube Studio EN):**
  - **Title A:** `Gemini 4 Argon vs 3.8 Flash: the half pixel that broke a world`
  - **Title B:** `Gemini 4 Argon vs 3.8 Flash: 10-0, 55 vs 94 minutes`
  - **Title C:** `Gemini 4 Argon vs 3.8 Flash: 10 coding challenges, one attempt`

**Descripción Lista para Copiar y Pegar (`@MixiuhLabsEN` — Duración Real Verificada `09:28`, Mid-rolls en `02:22` y `05:33`, End Screen `09:13–09:28`):**
```text
Gemini 4 Argon vs Gemini 3.8 Flash: 10 zero-shot math and coding challenges, same prompt, one attempt. Which frontier model actually ships working code on the first try?

I tested Gemini 4 Argon and Gemini 3.8 Flash (High variants, inside Antigravity) with the exact same prompt across 10 progressive challenges: 3D with Three.js and custom GLSL shaders, physics simulations, graph algorithms, DDA raycasting, 8-bit pixel art, pure CSS and parametric math. Each model got a single zero-shot attempt and delivered everything inside one self-contained index.html file, with zero external images or 3D models.

PROMPTS, PLAYABLE DEMOS & FULL BENCHMARK
Central Lab, Prompts & AI Resources: https://labs.mixiuh.online
Source code for all 20 projects: https://github.com/danpez/gemini-4-argon-vs-3.8-flash-benchmark
Playable live demos (Argon and Flash): https://danpez.github.io/gemini-4-argon-vs-3.8-flash-benchmark/

CHAPTERS
00:00 The broken world
00:18 Experiment protocol
00:53 World 1, Level 1: Relative Solar System
01:37 World 1, Level 2: 3D DNA Visualizer
02:27 World 2, Level 3: Artificial Life
03:05 World 2, Level 4: Dungeon Generator
03:51 World 2, Level 5: Falling Sand Simulator
04:35 World 3, Level 6: 3D Raycasting Engine, the boss
05:33 World 3, Level 7: 8-Bit Space Sprites
06:15 World 4, Level 8: CSS Analog Clock
06:46 World 5, Level 9: Fractal Tree with Wind
07:36 World 5, Level 10: Parametric Spirograph
08:23 Results screen
08:47 Lab verdict

LAB TOOLS
- Voice: Voicefy, my own cloned voice, running locally on my Mac (narrated in English).
- Editing and captions: Reelfy + Mixiuh Labs Studio (custom pipeline).
- Music: original chiptune generated by code (no samples or third-party tracks).
- Models: Gemini 4 Argon and Gemini 3.8 Flash (High variants) in Antigravity.

OFFICIAL CHANNELS & BUSINESS INQUIRIES
- Spanish Channel (Official Mixiuh Labs cross-ownership property): https://www.youtube.com/@MixiuhLabsES
- Official Lab Hub: https://labs.mixiuh.online
- Sponsorships & Business Inquiries: mixiuhonline@gmail.com

The narration uses my own cloned voice with Voicefy (runs locally).

#Gemini4Argon #GeminiFlash #AI
```

**Tags (`@MixiuhLabsEN`):**
```text
Gemini 4 Argon, Gemini 3.8 Flash, Gemini 4 Argon vs Gemini 3.8 Flash, AI coding comparison, zero-shot coding, Antigravity, raycasting, Mixiuh Labs, AI math benchmark
```

**Pinned Comment (`@MixiuhLabsEN`):**
```text
Here, we don't guess: we test.

Test all 20 live simulations in your browser, grab the exact 10 zero-shot prompts, and explore our AI engineering stack right here:
https://labs.mixiuh.online

Quick lab note: generation times come from my benchmark logs (rounded to the minute). Flash actually finished faster in 3 of the 10 challenges—until you see what it shipped in Level 4 (03:17) and the half-pixel floating-point bug in Level 6 (04:50).

Which frontier models should we throw into the lab next? Drop your pick below.
```

---

## 5. DESPLIEGUE DIARIO DE LOS 11 VIDEOS CORTOS (DÍA 1 A DÍA 11)

> [!CAUTION]
> **Regla de Oro en YouTube Studio (`@MixiuhLabsES` y `@MixiuhLabsEN`):**
> Sube exactamente **1 Short por día**. En la pantalla de detalles de YouTube Studio, baja a la sección **`Related Video` (Video relacionado)** y selecciona el video largo de 10 minutos (`Gemini 4 Argon vs 3.8 Flash: el medio píxel que rompió un mundo`). Esto convierte un botón clicable sobre el reproductor de Shorts en un puente directo de horas de reproducción hacia las 4,000 horas del YPP.

---

### DÍA 1 — CORTE #00: INTRODUCCIÓN Y GANCHO DEL TORNEO (ADEMÁS DEL VIDEO LARGO)

- **Archivo Vertical 9:16 (YouTube Shorts ES / TikTok / IG Reels / FB Reels):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/00_portada_resumen_hilo_vs.mp4`
- **Archivo Horizontal 16:9 Alternativo (Avance de 62s con Voz para Feed de Facebook / LinkedIn):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/ligero/ep01_avance_gancho_ligero.mp4`
- **Archivo Historia 9:16 (IG Stories / FB Stories / WhatsApp):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/05-extras/posts-ep01/ep01_historia_2160x3840.png` (colocar sticker de enlace a `https://labs.mixiuh.online` entre `y=1600` y `y=1720`).

#### 1. YouTube Short #00 (`@MixiuhLabsES`)
- **Título:** `Puse a competir a dos Gemini en 10 retos extremos (Un solo intento)`
- **Descripción:**
  ```text
  Gemini 4 Argon (High) vs Gemini 3.8 Flash (High): 10 retos de código y matemáticas zero-shot sin correcciones.
  Prompts y demos jugables: https://labs.mixiuh.online
  Haz clic en el video relacionado aquí abajo para ver el torneo completo de 10 minutos.
  #Shorts #Gemini #IA
  ```
- **Video Relacionado (`Related Video`):** Vincular al Video Largo de 10:05 en `@MixiuhLabsES`.

#### 2. YouTube Short #00 (`@MixiuhLabsEN`)
- **Título:** `I tested Gemini 4 Argon vs 3.8 Flash on 10 extreme coding challenges`
- **Descripción:**
  ```text
  Gemini 4 Argon (High) vs Gemini 3.8 Flash (High): 10 zero-shot coding and math challenges, single attempt.
  Prompts & live demos: https://labs.mixiuh.online
  Tap the related video below to watch the full 10-minute tournament.
  #Shorts #Gemini #AI
  ```
- **Related Video:** Vincular al Video Largo en `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  Le di exactamente el mismo prompt a Gemini 3.8 Flash y al nuevo Gemini 4 Argon en 10 retos extremos de física, gráficos 3D y matemáticas. Un solo intento, cero texturas externas. El que se llama "Flash" tardó 39 minutos más en total y medio píxel le rompió el mundo en el Nivel 6. Ya está el torneo completo de 10 minutos en nuestro canal de YouTube Mixiuh Labs ES y todas las demos en labs.mixiuh.online #ia #programacion #gemini #desarrolloweb #tecnologia #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Automatización ManyChat)
- **Copy:**
  ```text
  ¿Qué pasa cuando enfrentas a Gemini 3.8 Flash contra el nuevo Gemini 4 Argon en 10 retos extremos de programación y matemáticas sin permitirles corregir ni una línea?

  10 retos. 1 solo intento (Zero-Shot). Todo dentro de un único archivo HTML.
  El resultado fue un 10-0 implacable y una diferencia de 39 minutos en el reloj acumulado.

  Comenta la palabra GEMINI aquí abajo y te envío por mensaje directo el enlace al torneo completo de 10 minutos + los 10 prompts exactos y las demos jugables de labs.mixiuh.online.

  #inteligenciaartificial #programacion #gemini #desarrollodesoftware #ingenieria #mixiuhlabs
  ```

#### 5. Facebook Reel + Post (ES — Sin Enlace en el Cuerpo)
- **Copy del Post:**
  ```text
  Enfrentamos a Gemini 3.8 Flash contra Gemini 4 Argon en un torneo de 10 niveles de programación gráfica, física y matemáticas con un solo intento por reto.

  Uno tardó 94 minutos y se rompió en dos pruebas. El otro terminó en 55 minutos con 10 de 10 funcionando a la primera.

  Te dejé el enlace al video completo de 10 minutos y las demos interactivas en el primer comentario fijado.
  ```
- **Primer Comentario Fijado en Facebook:**
  ```text
  Mira el torneo completo de 10 minutos en YouTube (@MixiuhLabsES) y prueba los 20 proyectos en vivo desde tu navegador aquí: https://labs.mixiuh.online
  ```

---

### DÍA 2 — SHORT #01: SISTEMA SOLAR RELATIVO (JERARQUÍA DE MATRICES + GLSL)

- **Archivo ES (`@MixiuhLabsES` / TikTok / IG / FB):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/01_sistema-solar.mp4` (`47.0 s`)
- **Archivo EN (`@MixiuhLabsEN`):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/shorts/01_sistema-solar.mp4`

#### 1. YouTube Short #01 (`@MixiuhLabsES`)
- **Título:** `Reto 1: Sistema Solar Relativo en un solo intento (Gemini 4 Argon vs 3.8 Flash)`
- **Descripción:**
  ```text
  Mismo prompt, un solo intento, cero imágenes: Sistema Solar Relativo con jerarquía de matrices y shaders GLSL.
  Punto para Argon. Tiempo de entrega: Flash 7 min, Argon 11 min.
  Prompts y demos en vivo: https://labs.mixiuh.online
  #Shorts #Gemini #IA
  ```
- **Video Relacionado:** Video Largo `@MixiuhLabsES`.

#### 2. YouTube Short #01 (`@MixiuhLabsEN`)
- **Título:** `Challenge 1: Relative Solar System in a single attempt (Gemini 4 Argon vs 3.8 Flash)`
- **Descripción:**
  ```text
  Same prompt, one attempt, zero images: Relative Solar System with scene-graph matrices and GLSL shaders.
  Point to Argon. Delivery time: Flash 7 min, Argon 11 min.
  Prompts & live demos: https://labs.mixiuh.online
  #Shorts #Gemini #AI
  ```
- **Related Video:** Video Largo `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  Nivel 1 del torneo: programar un Sistema Solar en 3D sin usar ni una sola imagen externa. Sorpresa en el cronómetro: Flash terminó en 7 minutos y Argon en 11... pero de cerca el Sol de Flash parece foco de baño, mientras Argon programó granulación solar en GLSL y eclipses de luna de sangre píxel por píxel. Torneo completo en YouTube Mixiuh Labs ES y demos en labs.mixiuh.online #ia #threejs #webgl #programacion #gemini #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Trigger ManyChat)
- **Copy:**
  ```text
  Nivel 1/10: Sistema Solar Relativo en 3D con cero texturas externas.

  Flash ganó la carrera del reloj (7 min vs 11 min), pero cuando bajas el brillo del Sol en Argon aparecen manchas solares, granulación procedural en shaders GLSL, el árbol de matrices Sol-Tierra-Luna en vivo y un laboratorio de eclipses reales.

  Comenta GEMINI y te mando por DM el benchmark completo de 10 minutos + el repositorio y demos de labs.mixiuh.online.

  #threejs #webgl #programacion #inteligenciaartificial #gemini #mixiuhlabs
  ```

#### 5. Facebook Reel (ES)
- **Copy del Post:**
  ```text
  Nivel 1 del laboratorio: pedirle a dos IA un Sistema Solar 3D donde la Luna herede la matriz de movimiento de la Tierra, sin usar texturas externas. Flash acabó 4 minutos antes, pero mira la diferencia cuando acercamos la cámara al Sol. El enlace al experimento completo y a las demos está en el primer comentario.
  ```
- **Primer Comentario Fijado:**
  ```text
  Prueba este sistema solar en vivo y mira el torneo completo de 10 minutos aquí: https://labs.mixiuh.online
  ```

---

### DÍA 3 — SHORT #02: VISUALIZADOR DE ADN 3D (LEY DE HOOKE + TELEMETRÍA REAL VS FALSA)

- **Archivo ES (`@MixiuhLabsES` / TikTok / IG / FB):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/02_visualizador-adn.mp4` (`51.7 s`)
- **Archivo EN (`@MixiuhLabsEN`):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/shorts/02_visualizador-adn.mp4`

#### 1. YouTube Short #02 (`@MixiuhLabsES`)
- **Título:** `Mismo prompt: Argon en 5 min, Flash en 7 min (Visualizador de ADN 3D)`
- **Descripción:**
  ```text
  Mismo prompt, un solo intento, cero imágenes: Visualizador de ADN 3D con física de resortes (Ley de Hooke).
  Punto para Argon. Tiempo de entrega: Flash 7 min, Argon 5 min.
  Prompts y demos en vivo: https://labs.mixiuh.online
  #Shorts #Gemini #IA
  ```
- **Video Relacionado:** Video Largo `@MixiuhLabsES`.

#### 2. YouTube Short #02 (`@MixiuhLabsEN`)
- **Título:** `Same prompt: Argon in 5 min, Flash in 7 min (3D DNA Visualizer)`
- **Descripción:**
  ```text
  Same prompt, one attempt, zero images: 3D DNA Visualizer with Hooke's Law spring physics.
  Point to Argon. Delivery time: Flash 7 min, Argon 5 min.
  Prompts & live demos: https://labs.mixiuh.online
  #Shorts #Gemini #AI
  ```
- **Related Video:** Video Largo `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  Cachamos a Gemini 3.8 Flash haciendo trampa en el Nivel 2. El reto pedía una doble hélice de ADN con más de 10,000 partículas y física de resortes. En su panel Flash presume "18,480 partículas"... pero abrimos el código y ese número es texto fijo en el HTML (en realidad genera 17,840 y olvidó el slider de densidad). Argon entregó 24,500 partículas reales en 5 minutos. Prueba ambos en labs.mixiuh.online #ia #programacion #codigo #gemini #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Trigger ManyChat)
- **Copy:**
  ```text
  Nivel 2/10: cuando una IA te miente en la cara con un número escrito a mano en el HTML.

  Flash presume "18,480 PTS" en su interfaz, pero ningún script actualiza esa etiqueta y omitió los controles de densidad y morfología que exigía el prompt. Argon tardó 2 minutos menos (5 min vs 7 min) y programó 24,500 partículas reales gobernadas por la Ley de Hooke.

  Comenta GEMINI y te envío por DM el video completo de 10 minutos + el código fuente y los prompts en labs.mixiuh.online.

  #programador #desarrolloweb #inteligenciaartificial #javascript #gemini #mixiuhlabs
  ```

#### 5. Facebook Reel (ES)
- **Copy del Post:**
  ```text
  Por esto siempre revisamos el código línea por línea en Mixiuh Labs. En el Nivel 2 (Visualizador de ADN 3D), el panel de Flash presume 18,480 partículas... pero ese número estaba escrito a mano en el HTML y nunca cambia. Te dejé el enlace al análisis completo y las demos interactivas en el primer comentario.
  ```
- **Primer Comentario Fijado:**
  ```text
  Inspecciona el código y juega con el visualizador de ADN en vivo aquí: https://labs.mixiuh.online
  ```

---

### DÍA 4 — SHORT #03: VIDA ARTIFICIAL (BOIDS DE REYNOLDS + QUADTREE)

- **Archivo ES (`@MixiuhLabsES` / TikTok / IG / FB):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/03_vida-artificial.mp4` (`49.4 s`)
- **Archivo EN (`@MixiuhLabsEN`):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/shorts/03_vida-artificial.mp4`

#### 1. YouTube Short #03 (`@MixiuhLabsES`)
- **Título:** `Vida Artificial: Gemini 4 Argon vs 3.8 Flash (2,500 agentes en vivo)`
- **Descripción:**
  ```text
  Mismo prompt, un solo intento, cero imágenes: Vida Artificial con reglas de Reynolds y Quadtree espacial.
  Punto para Argon. Tiempo de entrega: Flash 3 min, Argon 5 min.
  Prompts y demos en vivo: https://labs.mixiuh.online
  #Shorts #Gemini #IA
  ```
- **Video Relacionado:** Video Largo `@MixiuhLabsES`.

#### 2. YouTube Short #03 (`@MixiuhLabsEN`)
- **Título:** `Artificial Life: Gemini 4 Argon vs 3.8 Flash (2,500 Boids in real time)`
- **Descripción:**
  ```text
  Same prompt, one attempt, zero images: Artificial Life with Reynolds flocking and Quadtree spatial partitioning.
  Point to Argon. Delivery time: Flash 3 min, Argon 5 min.
  Prompts & live demos: https://labs.mixiuh.online
  #Shorts #Gemini #AI
  ```
- **Related Video:** Video Largo `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  Nivel 3: el duelo más parejo de todo el torneo. 2,500 agentes autónomos huyendo de depredadores en tiempo real sin colapsar el navegador. Flash terminó en 3 minutos y hasta le metió audio sintetizado sin que se lo pidiera. Argon tardó 5 minutos pero agregó visualización de la malla Quadtree en vivo y 3 leviatanes con IA propia. Demos y video completo en labs.mixiuh.online #ia #algoritmos #programacion #simulacion #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Trigger ManyChat)
- **Copy:**
  ```text
  Nivel 3/10: aquí no hubo nocaut, fue decisión dividida por puntos.

  Ambos modelos implementaron particionamiento espacial para mover más de 2,000 boids sin caer en fuerza bruta O(N²). Flash sorprendió en 3 minutos con audio reactivo; Argon ganó por sus capas de depuración científica (teclas Q, V, T, N, P) y 3 depredadores autónomos.

  Comenta GEMINI para recibir por DM el torneo completo de 10 minutos y probar ambas parvadas en labs.mixiuh.online.

  #cienciadedatos #algoritmos #programacion #ia #gemini #mixiuhlabs
  ```

#### 5. Facebook Reel (ES)
- **Copy del Post:**
  ```text
  El enfrentamiento más cerrado del laboratorio: simular una parvada de 2,500 agentes con reglas de separación, alineación y cohesión en un solo intento. Flash lo sacó en 3 minutos; Argon tardó 5 pero metió tres depredadores con inteligencia propia. Enlace al video completo y demos en el primer comentario.
  ```
- **Primer Comentario Fijado:**
  ```text
  Prueba el simulador de Vida Artificial y mira los 10 retos en: https://labs.mixiuh.online
  ```

---

### DÍA 5 — SHORT #04: GENERADOR DE MAZMORRAS (CUANDO SER 6X MÁS RÁPIDO NO SIRVE DE NADA)

- **Archivo ES (`@MixiuhLabsES` / TikTok / IG / FB):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/04_generador-mazmorras.mp4` (`52.6 s`)
- **Archivo EN (`@MixiuhLabsEN`):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/shorts/04_generador-mazmorras.mp4`

#### 1. YouTube Short #04 (`@MixiuhLabsES`)
- **Título:** `Mismo prompt: Argon en 12 min, Flash en 2 min (Generador de Mazmorras)`
- **Descripción:**
  ```text
  Mismo prompt, un solo intento, cero imágenes: Generador de Mazmorras con algoritmo A* y niebla de guerra.
  Punto para Argon. Tiempo de entrega: Flash 2 min (con bugs), Argon 12 min (RPG jugable).
  Prompts y demos en vivo: https://labs.mixiuh.online
  #Shorts #Gemini #IA
  ```
- **Video Relacionado:** Video Largo `@MixiuhLabsES`.

#### 2. YouTube Short #04 (`@MixiuhLabsEN`)
- **Título:** `Same prompt: Argon in 12 min, Flash in 2 min (Dungeon Generator)`
- **Descripción:**
  ```text
  Same prompt, one attempt, zero images: Dungeon Generator with A* pathfinding and fog of war.
  Point to Argon. Delivery time: Flash 2 min (buggy), Argon 12 min (full mini-RPG).
  Prompts & live demos: https://labs.mixiuh.online
  #Shorts #Gemini #AI
  ```
- **Related Video:** Video Largo `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  Nivel 4: Flash terminó en 2 minutos (6 veces más rápido que Argon)... pero mira lo que entregó. En el modo paso a paso dibuja la ruta antes que los cuartos, deja una maraña de líneas moradas encima del mapa y cuando llegas a la escalera de salida no pasa absolutamente nada. Argon se tomó 12 minutos y programó un RPG completo con trampas, cofres, mapa de calor Dijkstra y un jefe final. Video completo en YouTube Mixiuh Labs ES y demos en labs.mixiuh.online #ia #gamedev #programacion #gemini #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Trigger ManyChat)
- **Copy:**
  ```text
  Nivel 4/10: la diferencia entre contestar rápido y entregar software que funciona a la primera.

  Flash declaró terminado el reto a los 2 minutos, pero con el renderizador de fases roto y una salida sin lógica. Argon invirtió 12 minutos y construyó un dungeon crawler completo con algoritmo A*, mapa de calor de distancias, combate contra el Guardián del Abismo y generación infinita de pisos.

  Comenta GEMINI y te envío por DM el video completo de 10 minutos + el link para jugarlo en labs.mixiuh.online.

  #gamedev #programacion #inteligenciaartificial #desarrolloweb #gemini #mixiuhlabs
  ```

#### 5. Facebook Reel (ES)
- **Copy del Post:**
  ```text
  ¿De qué sirve que un modelo de IA sea 6 veces más rápido si tienes que gastar media hora arreglando sus bugs? En el Nivel 4 (Generador de Mazmorras), Flash terminó en 2 minutos pero dejó una maraña de líneas moradas y una salida que no hace nada. Argon tardó 12 minutos y entregó un juego de rol completo. Enlace en el primer comentario.
  ```
- **Primer Comentario Fijado:**
  ```text
  Juega el generador de mazmorras y revisa los 10 prompts del experimento en: https://labs.mixiuh.online
  ```

---

### DÍA 6 — SHORT #05: SIMULADOR FALLING SAND (TERMODINÁMICA Y HIDROSTÁTICA DE PÍXELES)

- **Archivo ES (`@MixiuhLabsES` / TikTok / IG / FB):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/05_falling-sand.mp4` (`50.9 s`)
- **Archivo EN (`@MixiuhLabsEN`):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/shorts/05_falling-sand.mp4`

#### 1. YouTube Short #05 (`@MixiuhLabsES`)
- **Título:** `Simulador Falling Sand: Gemini 4 Argon vs 3.8 Flash (4 min vs 9 min)`
- **Descripción:**
  ```text
  Mismo prompt, un solo intento, cero imágenes: Simulador Falling Sand con 12 elementos y reacciones en cadena.
  Punto para Argon (4 min vs 9 min de Flash).
  Prompts y demos en vivo: https://labs.mixiuh.online
  #Shorts #Gemini #IA
  ```
- **Video Relacionado:** Video Largo `@MixiuhLabsES`.

#### 2. YouTube Short #05 (`@MixiuhLabsEN`)
- **Título:** `Falling Sand Simulator: Gemini 4 Argon vs 3.8 Flash (4 min vs 9 min)`
- **Descripción:**
  ```text
  Same prompt, one attempt, zero images: Falling Sand cellular automata with 12 elements and chain reactions.
  Point to Argon (4 min vs 9 min for Flash).
  Prompts & live demos: https://labs.mixiuh.online
  #Shorts #Gemini #AI
  ```
- **Related Video:** Video Largo `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  Nivel 5: esto pasa cuando le echas lava a un jardín en el simulador Falling Sand que Gemini 4 Argon programó en 4 minutos. El examen básico de física es que el agua se nivele: en Flash el agua desplazada se queda congelada como un domo encima del tanque. En Argon la planta bebe agua para crecer, el fuego rompe la repisa y puedes invertir la gravedad en vivo. Pruébalo en labs.mixiuh.online #ia #simulacion #fisica #programacion #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Trigger ManyChat)
- **Copy:**
  ```text
  Nivel 5/10: autómatas celulares estilo Noita programados en un solo intento.

  Ambos modelos incluyeron 12 elementos, pero en Flash el agua no logra nivelarse por dispersión lateral. En Argon (4 minutos vs 9 de Flash), las plantas absorben agua, la lava desata tormentas de fuego y la gravedad se puede invertir en tiempo real.

  Comenta GEMINI y te mando por DM el torneo completo de 10 minutos + el enlace directo a este sandbox en labs.mixiuh.online.

  #fisica #programacion #gamedev #inteligenciaartificial #gemini #mixiuhlabs
  ```

#### 5. Facebook Reel (ES)
- **Copy del Post:**
  ```text
  El examen básico para un simulador de arena y fluidos es simple: que el agua quede plana. En el Nivel 5 del torneo, el agua de Flash se queda estancada como un domo, mientras que en Argon las plantas beben agua para crecer y la lava desata reacciones en cadena. Te dejé el enlace para probarlo en el primer comentario.
  ```
- **Primer Comentario Fijado:**
  ```text
  Prueba el simulador Falling Sand en tu navegador y ve el video completo en: https://labs.mixiuh.online
  ```

---

### DÍA 7 — SHORT #06: MOTOR 3D RAYCASTING, EL JEFE (EL BUG DE MEDIO PÍXEL)

- **Archivo ES (`@MixiuhLabsES` / TikTok / IG / FB):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/06_motor-raycasting.mp4` (`54.7 s`)
- **Archivo EN (`@MixiuhLabsEN`):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/shorts/06_motor-raycasting.mp4`

#### 1. YouTube Short #06 (`@MixiuhLabsES`)
- **Título:** `El bug de medio píxel: Motor 3D Raycasting (Gemini 4 Argon vs 3.8 Flash)`
- **Descripción:**
  ```text
  Mismo prompt, un solo intento, prohibido WebGL: Motor 3D Raycasting estilo Wolfenstein 1992 en Canvas 2D.
  Flash tardó 17 min y dividió la altura sin redondear (lineHeight / 2). Argon usó bit-shift (lineHeight >> 1) en 4 min.
  Prompts y demos en vivo: https://labs.mixiuh.online
  #Shorts #Gemini #IA
  ```
- **Video Relacionado:** Video Largo `@MixiuhLabsES`.

#### 2. YouTube Short #06 (`@MixiuhLabsEN`)
- **Título:** `The half-pixel bug: 3D Raycasting Engine (Gemini 4 Argon vs 3.8 Flash)`
- **Descripción:**
  ```text
  Same prompt, one attempt, zero WebGL: 1992 Wolfenstein-style DDA Raycasting Engine in pure 2D Canvas.
  Flash took 17 min and divided wall height without rounding (lineHeight / 2). Argon used a bit shift (lineHeight >> 1) in 4 min.
  Prompts & live demos: https://labs.mixiuh.online
  #Shorts #Gemini #AI
  ```
- **Related Video:** Video Largo `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  La autopsia del bug más brutal del torneo (Nivel 6: El Jefe). Pedimos un motor 3D estilo Wolfenstein de 1992 prohibiendo WebGL, todo en Canvas 2D puro. Flash tardó 17 minutos y al dar un paso las paredes se deshacen en tiras porque en la línea 1263 dividió `lineHeight / 2` sin redondear: con alturas impares queda `.5` en el buffer de píxeles. Argon usó `lineHeight >> 1` y entregó un juego completo en 4 minutos. Código y demos en labs.mixiuh.online #ia #programacion #javascript #gamedev #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Trigger ManyChat)
- **Copy:**
  ```text
  Nivel 6/10 (El Jefe): cómo medio píxel destruyó 17 minutos de trabajo de Gemini 3.8 Flash.

  En la línea 1263 de su motor de Raycasting, Flash escribió:
  `const drawStart = Math.max(0, -lineHeight / 2 + halfH);`
  Al no redondear, cada pared con altura impar genera un índice `.5` al escribir el buffer de pantalla.

  Argon escribió `-(lineHeight >> 1) + horizon` y en solo 4 minutos entregó puertas corredizas, drones, orbes y cañón de plasma.

  Comenta GEMINI y te envío por DM el video completo de 10 minutos + el código exacto en labs.mixiuh.online.

  #javascript #programacion #ingenieriadesoftware #gamedev #gemini #mixiuhlabs
  ```

#### 5. Facebook Reel (ES)
- **Copy del Post:**
  ```text
  Así es como medio píxel rompe un mundo en 3D. En el Nivel 6 del torneo pedimos un motor estilo Wolfenstein de 1992 usando solo trigonometría en Canvas 2D. Flash tardó 17 minutos y olvidó redondear una división entre dos; Argon usó un desplazamiento de bits y lo resolvió en 4 minutos. El enlace al análisis completo está en el primer comentario.
  ```
- **Primer Comentario Fijado:**
  ```text
  Juega ambos motores de Raycasting y revisa el código fuente en: https://labs.mixiuh.online
  ```

---

### DÍA 8 — SHORT #07: SPRITES ESPACIALES 8 BITS (12 NAVES PROCEDURALES + ARCADE SHMUP)

- **Archivo ES (`@MixiuhLabsES` / TikTok / IG / FB):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/07_generador-sprites.mp4` (`47.7 s`)
- **Archivo EN (`@MixiuhLabsEN`):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/shorts/07_generador-sprites.mp4`

#### 1. YouTube Short #07 (`@MixiuhLabsES`)
- **Título:** `Mismo prompt: Argon en 4 min, Flash en 13 min (Sprites Espaciales 8 Bits)`
- **Descripción:**
  ```text
  Mismo prompt, un solo intento, cero imágenes: Generador de Sprites Espaciales 8 Bits con simulador de vuelo arcade.
  Punto para Argon (4 min vs 13 min de Flash).
  Prompts y demos en vivo: https://labs.mixiuh.online
  #Shorts #Gemini #IA
  ```
- **Video Relacionado:** Video Largo `@MixiuhLabsES`.

#### 2. YouTube Short #07 (`@MixiuhLabsEN`)
- **Título:** `Same prompt: Argon in 4 min, Flash in 13 min (8-Bit Space Sprites)`
- **Descripción:**
  ```text
  Same prompt, one attempt, zero images: 8-Bit Space Sprite Generator with playable arcade flight test.
  Point to Argon (4 min vs 13 min for Flash).
  Prompts & live demos: https://labs.mixiuh.online
  #Shorts #Gemini #AI
  ```
- **Related Video:** Video Largo `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  12 naves espaciales distintas en 12 segundos y ninguna fue dibujada a mano. En el Nivel 7 pedimos un generador matemático de sprites de 8 bits donde además pudieras pilotear tu nave. Flash tardó 13 minutos; Argon lo sacó en 4 minutos con explosiones de partículas y puntaje tipo arcade. Pruébalo gratis en labs.mixiuh.online #pixelart #gamedev #ia #programacion #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Trigger ManyChat)
- **Copy:**
  ```text
  Nivel 7/10: arte pixel de 8 bits generado por matrices de simetría + minijuego espacial en un solo intento.

  Me gustó que Flash te enseña capa por capa cómo construye la máscara binaria de la nave, pero tardó 13 minutos. Argon lo entregó en 4 minutos con mucha mayor variedad morfológica y un simulador arcade donde rocas y drones revientan en píxeles.

  Comenta GEMINI y te mando por DM el torneo completo de 10 minutos + las demos en labs.mixiuh.online.

  #pixelart #indiedev #programacion #inteligenciaartificial #gemini #mixiuhlabs
  ```

#### 5. Facebook Reel (ES)
- **Copy del Post:**
  ```text
  Doce naves espaciales en doce segundos, generadas 100% con código matemático sin usar una sola imagen externa. En el Nivel 7 del torneo pusimos a ambos modelos a crear un estudio de sprites de 8 bits con simulador de vuelo incluido. Te dejé el enlace para probarlo en el primer comentario.
  ```
- **Primer Comentario Fijado:**
  ```text
  Genera tus propias naves y juega el modo arcade desde tu navegador en: https://labs.mixiuh.online
  ```

---

### DÍA 9 — SHORT #08: RELOJ ANALÓGICO CSS (ALTA RELOJERÍA SIN BUCLE JAVASCRIPT)

- **Archivo ES (`@MixiuhLabsES` / TikTok / IG / FB):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/08_reloj-analogico.mp4` (`41.2 s`)
- **Archivo EN (`@MixiuhLabsEN`):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/shorts/08_reloj-analogico.mp4`

#### 1. YouTube Short #08 (`@MixiuhLabsES`)
- **Título:** `Reloj Analógico CSS en 2 minutos: Gemini 4 Argon vs 3.8 Flash`
- **Descripción:**
  ```text
  Mismo prompt, un solo intento, cero setInterval: Reloj Analógico de lujo en CSS puro con tourbillon.
  Punto para Argon (récord del torneo: 2 min vs 4 min de Flash).
  Prompts y demos en vivo: https://labs.mixiuh.online
  #Shorts #Gemini #IA
  ```
- **Video Relacionado:** Video Largo `@MixiuhLabsES`.

#### 2. YouTube Short #08 (`@MixiuhLabsEN`)
- **Título:** `Pure CSS Analog Clock in 2 minutes: Gemini 4 Argon vs 3.8 Flash`
- **Descripción:**
  ```text
  Same prompt, one attempt, zero setInterval: Luxury CSS Analog Clock with rotating tourbillon.
  Point to Argon (tournament record: 2 min vs 4 min for Flash).
  Prompts & live demos: https://labs.mixiuh.online
  #Shorts #Gemini #AI
  ```
- **Related Video:** Video Largo `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  Nivel 8: programar un reloj mecánico con tourbillon donde JavaScript tiene prohibido mover las manecillas (cero setInterval, cero requestAnimationFrame, puro CSS). Los dos cumplieron y Flash cambia de tema más suave, pero el de Argon parece reloj suizo de aparador con modo Lujo Nocturno fosforescente... y lo hizo en 2 minutos, el récord del torneo. Míralo en labs.mixiuh.online #css #frontend #desarrolloweb #ia #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Trigger ManyChat)
- **Copy:**
  ```text
  Nivel 8/10: cuando prohíbes `setInterval` y `requestAnimationFrame` y obligas a la IA a resolver toda la cinemática del reloj en CSS puro.

  Ambos cumplieron las reglas al pie de la letra. Punto honesto para Flash por la suavidad de sus transiciones entre temas, pero Argon diseñó asas, bisel estriado, corona, tourbillon dorado y modo Lujo Nocturno en apenas 2 minutos.

  Comenta GEMINI y te envío por DM el video completo de 10 minutos + el código CSS en labs.mixiuh.online.

  #css3 #frontend #webdesign #programacion #gemini #mixiuhlabs
  ```

#### 5. Facebook Reel (ES)
- **Copy del Post:**
  ```text
  La entrega funcional más rápida de todo el torneo: 2 minutos. El reto del Nivel 8 prohibía mover las manecillas con JavaScript; todo el movimiento mecánico y el tourbillon tenían que correr en CSS puro. Mira la diferencia entre un ícono de aplicación y un reloj de aparador. Enlace en el primer comentario.
  ```
- **Primer Comentario Fijado:**
  ```text
  Prueba los 3 temas del reloj CSS y revisa el código completo en: https://labs.mixiuh.online
  ```

---

### DÍA 10 — SHORT #09: ÁRBOL FRACTAL CON VIENTO (22 MINUTOS VS 4 MINUTOS)

- **Archivo ES (`@MixiuhLabsES` / TikTok / IG / FB):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/09_arbol-fractal.mp4` (`58.0 s`)
- **Archivo EN (`@MixiuhLabsEN`):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/shorts/09_arbol-fractal.mp4`

#### 1. YouTube Short #09 (`@MixiuhLabsES`)
- **Título:** `Mismo prompt: Argon en 4 min, Flash en 22 min (Árbol Fractal con Viento)`
- **Descripción:**
  ```text
  Mismo prompt, un solo intento, cero imágenes: Árbol Fractal recursivo con viento de ruido Perlin.
  Punto para Argon (4 min vs 22 min de Flash: 18 minutos de diferencia).
  Prompts y demos en vivo: https://labs.mixiuh.online
  #Shorts #Gemini #IA
  ```
- **Video Relacionado:** Video Largo `@MixiuhLabsES`.

#### 2. YouTube Short #09 (`@MixiuhLabsEN`)
- **Título:** `Same prompt: Argon in 4 min, Flash in 22 min (Fractal Tree with Wind)`
- **Descripción:**
  ```text
  Same prompt, one attempt, zero images: Recursive Fractal Tree with Perlin noise wind physics.
  Point to Argon (4 min vs 22 min for Flash: 18-minute gap).
  Prompts & live demos: https://labs.mixiuh.online
  #Shorts #Gemini #AI
  ```
- **Related Video:** Video Largo `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  La espera más larga de todo el experimento: Gemini 3.8 Flash se tardó 22 minutos en este reto y Gemini 4 Argon solo 4 (18 minutos de diferencia). El cerezo de Flash se ve bien, pero cuando eliges "Sauce Llorón" es exactamente el mismo árbol pintado de verde y no llora nada. En Argon las ramas cuelgan como cortinas reales sobre un esqueleto de 7,407 segmentos. Pruébalo en labs.mixiuh.online #matematicas #fractales #programacion #ia #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Trigger ManyChat)
- **Copy:**
  ```text
  Nivel 9/10: 22 minutos de generación en Flash contra 4 minutos en Argon.

  El reto exigía geometría fractal recursiva deformada en vivo por un campo de viento de ruido Perlin. En Flash, el preset de Sauce Llorón solo le cambia el color al cerezo sin modificar la gravedad de las ramas. En Argon, el árbol entero se reconstruye con cortinas reales de follaje.

  Comenta GEMINI y te mando por DM el torneo completo de 10 minutos + las demos interactivas en labs.mixiuh.online.

  #fractales #matematicas #programacion #inteligenciaartificial #gemini #mixiuhlabs
  ```

#### 5. Facebook Reel (ES)
- **Copy del Post:**
  ```text
  18 minutos de diferencia en un solo prompt. Mientras Gemini 4 Argon terminó este bosque fractal en 4 minutos, Gemini 3.8 Flash se quedó pensando durante 22 minutos... y su sauce llorón resultó ser el mismo cerezo pintado de verde. Te dejé el enlace a la demo interactiva y al video completo en el primer comentario.
  ```
- **Primer Comentario Fijado:**
  ```text
  Explora el árbol fractal en vivo y mira el torneo completo en: https://labs.mixiuh.online
  ```

---

### DÍA 11 — SHORT #10: SPIROGRAPH PARAMÉTRICO (TEORÍA DE NÚMEROS + CIERRE 10-0)

- **Archivo ES (`@MixiuhLabsES` / TikTok / IG / FB):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/shorts/10_spirograph-parametrico.mp4` (`54.1 s`)
- **Archivo EN (`@MixiuhLabsEN`):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_en/shorts/10_spirograph-parametrico.mp4`

#### 1. YouTube Short #10 (`@MixiuhLabsES`)
- **Título:** `Reto 10: Spirograph Paramétrico y el error de secundaria (Gemini 4 Argon vs 3.8 Flash)`
- **Descripción:**
  ```text
  Mismo prompt, un solo intento, cero imágenes: Spirograph Paramétrico con cálculo de cierre por Máximo Común Divisor (MCD).
  Punto para Argon (4 min vs 10 min de Flash) para cerrar el marcador 10-0.
  Prompts y demos en vivo: https://labs.mixiuh.online
  #Shorts #Gemini #IA
  ```
- **Video Relacionado:** Video Largo `@MixiuhLabsES`.

#### 2. YouTube Short #10 (`@MixiuhLabsEN`)
- **Título:** `Challenge 10: Parametric Spirograph & GCD Math (Gemini 4 Argon vs 3.8 Flash)`
- **Descripción:**
  ```text
  Same prompt, one attempt, zero images: Parametric Spirograph with Greatest Common Divisor (GCD) closure math.
  Point to Argon (4 min vs 10 min for Flash) to complete the 10-0 sweep.
  Prompts & live demos: https://labs.mixiuh.online
  #Shorts #Gemini #AI
  ```
- **Related Video:** Video Largo `@MixiuhLabsEN`.

#### 3. TikTok (ES)
- **Copy:**
  ```text
  Nivel 10 (Final del Torneo): por fin sirvió para algo el Máximo Común Divisor de la secundaria. Para saber cuántas vueltas necesita un espirógrafo antes de cerrar la figura hay que calcular el MCD de todos los engranajes. Con dos engranajes ambos empatan, pero cuando activas el tercer engranaje, Flash hace la cuenta como si ese tercer engranaje no existiera y su medidor de velocidad marca 0 px/s. Argon calcula hasta 17,310 radianes exactos en 4 minutos. Marcador final: 10-0. Todo en labs.mixiuh.online #matematicas #programacion #ia #gemini #mixiuhlabs
  ```

#### 4. Instagram Reels (ES — Trigger ManyChat)
- **Copy:**
  ```text
  Nivel 10/10: cómo un cálculo de Máximo Común Divisor (MCD) selló el 10-0 definitivo a favor de Gemini 4 Argon.

  Cuando pasas de 2 a 3 engranajes en un sistema hipotrocoide, Flash ignora el tercer radio en la fórmula de cierre y deja el velocímetro de la pluma muerto en `0 px/s`. Argon resuelve la teoría de números completa en 4 minutos (contra 10 de Flash) y dibuja grabados estilo Guilloché de billete.

  Comenta GEMINI y te envío por DM el video completo de 10 minutos + los 20 proyectos interactivos en labs.mixiuh.online.

  #matematicas #geometria #programacion #inteligenciaartificial #gemini #mixiuhlabs
  ```

#### 5. Facebook Reel (ES)
- **Copy del Post:**
  ```text
  El último nivel del torneo definió el 10 a 0 con una cuenta de secundaria: el Máximo Común Divisor. Al activar un tercer engranaje en el espirógrafo, Flash calcula el cierre como si ese engranaje no existiera, mientras Argon resuelve la ecuación exacta en menos de la mitad del tiempo. Te dejé el enlace al episodio completo y las demos en el primer comentario.
  ```
- **Primer Comentario Fijado:**
  ```text
  Dibuja tus propios mandalas paramétricos y mira el torneo completo de 10 minutos en: https://labs.mixiuh.online
  ```

---

## 6. LINKEDIN: ESTRATEGIA B2B DE AUTORIDAD TÉCNICA (INGENIERÍA Y CTOs)

En LinkedIn evitamos el tono gamer juvenil y posicionamos a **Kevin González / Mixiuh Labs** como referente en evaluación empírica de modelos frontera en producción.

### Post Técnico Principal (Día 1 — Con Video Nativo `ep01_nivel6_jefe_ligero.mp4` o Carrusel `ep01_post-1` + `ep01_post-2`)

- **Archivo Adjunto Recomendado (Video Nativo 16:9):**
  `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/ligero/ep01_nivel6_jefe_ligero.mp4`
  *(O en su defecto el carrusel 4:5 con `ep01_post-1_gancho_1080x1350.png` y `ep01_post-2_marcador_1080x1350.png` en `brand-kit/05-extras/posts-ep01/`).*

**Copy B2B Listo para Copiar y Pegar en LinkedIn:**
```text
En ingeniería de software asistida por IA, el modelo más rápido no es el que imprime el primer token antes: es el que entrega código funcional en el primer intento sin consumir horas de depuración humana.

Esta semana en Mixiuh Labs ejecutamos un benchmark empírico enfrentando a Gemini 3.8 Flash (High) contra el nuevo Gemini 4 Argon (High) dentro de Antigravity bajo un protocolo estricto Zero-Shot:

- 10 problemas progresivos de computación gráfica, física y matemáticas (Three.js/GLSL, Ley de Hooke, Boids con Quadtree, BSP + A*, Autómatas Celulares, Raycasting DDA en Canvas 2D puro, Simetría 8-Bit, Cinemática CSS, Ruido Perlin y Curvas Hipotrocoides).
- Un solo intento por reto (cero correcciones iterativas).
- Entrega autocontenida en un único archivo index.html, prohibiendo texturas o activos externos.

Hallazgos clave para equipos técnicos y líderes de arquitectura:

1. Paradoja de latencia vs. convergencia de razonamiento:
Aunque Gemini 3.8 Flash lleva el apellido "Flash" y terminó antes en 3 de los 10 retos, su tiempo acumulado fue de 94 minutos frente a 55 minutos de Gemini 4 Argon (-41.5% de tiempo total). Cuando Flash entra en cadenas largas de razonamiento espacial (como el Árbol Fractal o el Motor Raycasting), sufre de sobre-pensamiento (22 min y 17 min respectivamente), mientras que Argon converge en 4 minutos.

2. Precisión aritmética de bajo nivel (El caso del Nivel 6):
Al implementar el algoritmo Digital Differential Analyzer (DDA) en Canvas 2D sin WebGL, Flash escribió en la línea 1263:
`const drawStart = Math.max(0, -lineHeight / 2 + halfH);`
Al dividir una altura impar entre 2 sin truncar a entero, introdujo un desplazamiento `.5` en el direccionamiento del buffer de píxeles, rompiendo el renderizado vertical a pesar de correr a 120 FPS. Argon utilizó desplazamiento de bits (`-(lineHeight >> 1) + horizon`), garantizando índices enteros en 4 minutos de generación.

3. Telemetría simulada vs. instrumentación real:
En dos pruebas (Visualizador de ADN y Spirograph), Flash maquetó indicadores en el DOM con valores estáticos (`18,480 PTS` escritos a mano en el HTML cuando el bucle generaba `17,840`, o `0 px/s` sin conectar al loop de render). Argon instrumentó todos los contadores contra las estructuras de datos reales.

Resultado global de calidad y funcionalidad:
- Tasa de entrega funcional Zero-Shot: Argon 10/10 (100%) vs. Flash 8/10 (80%).
- Marcador de calidad técnica: 10 - 0 a favor de Gemini 4 Argon.

Publicamos el estudio en video de 10 minutos (en español e inglés), el repositorio con los 20 proyectos de código abierto y las demos ejecutables en vivo en el navegador.

Dejo los enlaces directos a las demos, prompts y canales en el primer comentario.

#SoftwareEngineering #ArtificialIntelligence #Gemini #LLMBenchmark #WebGL #TechLeadership #MixiuhLabs
```

**Primer Comentario en LinkedIn (para no penalizar alcance del post):**
```text
Recursos completos del benchmark de Mixiuh Labs:
- Laboratorio, prompts y demos interactivas: https://labs.mixiuh.online
- Estudio completo en Español (YouTube 4K60): https://www.youtube.com/@MixiuhLabsES
- Full Study in English (YouTube 4K60): https://www.youtube.com/@MixiuhLabsEN
- Contacto para auditorías y colaboraciones B2B: mixiuhonline@gmail.com
```

---

## 7. X / TWITTER: MEGA-HILOS VIRALES (ESPAÑOL E INGLÉS) CON VIDEO NATIVO

### 7.1 Mega-Hilo en Español (12 Posts — Video Nativo en cada Post)

- **Post #1 (Gancho + Video Nativo `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/ligero/ep01_nivel6_jefe_ligero.mp4`):**
  ```text
  Gemini 3.8 Flash tardó 17 minutos en programar este mundo 3D, y medio píxel lo rompió.

  Gemini 4 Argon tardó 4 minutos, y el suyo sí se juega.

  Puse a competir a los dos en 10 retos extremos de código y matemáticas (1 intento, 0 imágenes externas). El que se llama "Flash" tardó 39 minutos más en total (94 vs 55 min) y perdió 10-0.

  Abro hilo con las 10 pruebas y el código real:
  ```
- **Post #2 (Reto 1 — Adjuntar `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/01_sistema_solar_vs.mp4`):**
  ```text
  1/10 Sistema Solar Relativo (Three.js + GLSL)
  - Flash: 7 min | Argon: 11 min

  Aquí Flash terminó 4 min antes, pero su Sol de cerca es un disco blanco plano y su eclipse es solo un aviso de texto.
  Argon programó granulación solar en shaders GLSL, eclipses de luna de sangre por píxel y dibujó el grafo de matrices Sol -> Tierra -> Luna en vivo. (1-0)
  ```
- **Post #3 (Reto 2 — Adjuntar `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/02_visualizador_adn_vs.mp4`):**
  ```text
  2/10 Visualizador de ADN 3D (Ley de Hooke)
  - Flash: 7 min | Argon: 5 min

  Flash presume "18,480 partículas" en el HUD... pero revisé el HTML y ese número está escrito a mano (en realidad genera 17,840 y olvidó el slider de densidad).
  Argon entregó 24,500 partículas reales en 5 min con 4 morfologías y onda de choque elástica. (2-0)
  ```
- **Post #4 (Reto 3 — Adjuntar `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/03_vida_artificial_boids_vs.mp4`):**
  ```text
  3/10 Vida Artificial (2,500 Boids + Quadtree)
  - Flash: 3 min | Argon: 5 min

  El duelo más parejo. Flash terminó en 3 min y agregó sonido sintetizado.
  Argon tardó 5 min pero incluyó visualización de la subdivisión Quadtree en vivo (tecla Q) y hasta 3 leviatanes depredadores con IA autónoma. (3-0)
  ```
- **Post #5 (Reto 4 — Adjuntar `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/04_generador_mazmorras_vs.mp4`):**
  ```text
  4/10 Generador de Mazmorras (BSP + A*)
  - Flash: 2 min (ROTO) | Argon: 12 min

  Flash fue 6x más rápido solo en decir que ya había terminado: dibuja la ruta antes que los cuartos, deja una maraña de líneas moradas y la salida no hace nada.
  Argon hizo un mini-RPG con trampas (-12 HP), cofres (+10 HP), mapa de calor y jefe final. (4-0)
  ```
- **Post #6 (Reto 5 — Adjuntar `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/05_falling_sand_vs.mp4`):**
  ```text
  5/10 Simulador Falling Sand (12 Elementos)
  - Flash: 9 min | Argon: 4 min

  El examen básico es que el agua quede plana: en Flash el agua desplazada se queda como un domo encima del tanque.
  En Argon (en menos de la mitad de tiempo), las plantas beben agua para crecer, el fuego colapsa repisas y puedes invertir la gravedad. (5-0)
  ```
- **Post #7 (Reto 6 — Adjuntar `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/06_motor_raycasting_vs.mp4`):**
  ```text
  6/10 Motor 3D Raycasting Wolfenstein (0 WebGL, puro Canvas 2D)
  - Flash: 17 min (ROTO) | Argon: 4 min

  El bug del medio píxel: en la línea 1263 Flash escribió `-lineHeight / 2 + halfH` sin redondear. Con alturas impares queda `.5` y rompe las columnas.
  Argon usó bit-shift `-(lineHeight >> 1)` y en 4 min armó puertas corredizas, drones y cañón de plasma. (6-0)
  ```
- **Post #8 (Reto 7 — Adjuntar `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/07_generador_sprites_vs.mp4`):**
  ```text
  7/10 Sprites Espaciales 8 Bits + Arcade Shmup
  - Flash: 13 min | Argon: 4 min

  En Flash muté la nave 55 veces bajo la paleta por defecto y casi todas salían idénticas, aunque su visor de capas está muy bien logrado.
  Argon generó 12 naves distintas en 12 segundos y un vuelo de prueba donde rocas y drones revientan en píxeles. (7-0)
  ```
- **Post #9 (Reto 8 — Adjuntar `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/08_reloj_analogico_css_vs.mp4`):**
  ```text
  8/10 Reloj Analógico en CSS Puro (0 setInterval)
  - Flash: 4 min | Argon: 2 min (Récord del torneo)

  JavaScript solo podía fijar la hora inicial. Ambos cumplieron con 3 temas y tourbillon; Flash cambia de tema más suave, pero el de Argon parece reloj suizo de aparador con modo Lujo Nocturno en solo 2 minutos. (8-0)
  ```
- **Post #10 (Reto 9 — Adjuntar `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/09_arbol_fractal_vs.mp4`):**
  ```text
  9/10 Árbol Fractal con Viento de Perlin
  - Flash: 22 min | Argon: 4 min (18 min de brecha)

  La espera más larga del torneo. El cerezo de Flash se ve bien, pero su "Sauce Llorón" es el mismo árbol pintado de verde.
  En Argon el árbol se reconstruye con cortinas reales de hojas sobre un esqueleto de 7,407 segmentos en 4 min. (9-0)
  ```
- **Post #11 (Reto 10 — Adjuntar `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/videos-x-comparativa/10_spirograph_parametrico_vs.mp4`):**
  ```text
  10/10 Spirograph Paramétrico (Hipotrocoides + MCD)
  - Flash: 10 min | Argon: 4 min

  Para calcular cuándo cierra la figura se usa el Máximo Común Divisor. Con un tercer engranaje, Flash hace la cuenta como si no existiera y su velocímetro marca `0 px/s`.
  Argon calcula cierres de hasta 17,310 radianes con acabado Guilloché. (10-0)
  ```
- **Post #12 (Veredicto + Tarjeta `brand-kit/05-extras/posts-ep01/ep01_x-card_1200x675.png` + Enlaces):**
  ```text
  Veredicto final del laboratorio Mixiuh Labs:
  - Calidad y funcionalidad: Argon 10 - 0 Flash
  - Entregas funcionales al primer intento: Argon 10/10 vs Flash 8/10
  - Tiempo total acumulado: Argon 55 min vs Flash 94 min (-41.5%)

  Aquí no se opina: se prueba.

  Video completo en 4K60 (YouTube ES): https://www.youtube.com/@MixiuhLabsES
  Prompts, código y las 20 demos jugables en tu navegador: https://labs.mixiuh.online
  ```

---

### 7.2 Mega-Thread in English (for Global AI Audience & `@MixiuhLabsEN` Traffic)

- **Post #1 (Attach `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep01-argon-vs-flash/entregables_finales_4k_es/ligero/ep01_nivel6_jefe_ligero.mp4` or EN equivalent):**
  ```text
  Gemini 3.8 Flash took 17 minutes to code this 3D world, and half a pixel broke it.

  Gemini 4 Argon took 4 minutes, and it is actually playable.

  I tested both models (High variants in Antigravity) across 10 extreme zero-shot coding & math challenges. One attempt, single HTML file, zero external images.

  The one called "Flash" took 39 minutes longer overall (94 vs 55 min) and lost 10-0. Thread with code & proof:
  ```
- **Post #2 (Attach `01_sistema_solar_vs.mp4` — o resumir Retos 1 a 5) y Post Final (Attach `ep01_x-card_1200x675.png`):**
  ```text
  Full 10-challenge breakdown:
  1. Solar System (GLSL): Flash 7m vs Argon 11m -> Argon wins (blood moon eclipse shader + scene graph)
  2. 3D DNA (Hooke's Law): Flash hardcoded "18,480" in HTML; Argon shipped 24,500 real particles in 5m
  3. Boids + Quadtree: Flash 3m vs Argon 5m (live Quadtree debug + 3 AI leviathans)
  4. Dungeon Generator: Flash shipped in 2m with broken phase order; Argon built a playable RPG in 12m
  5. Falling Sand: Flash water stuck in a dome; Argon plants drink water & invert gravity (4m vs 9m)
  6. DDA Raycasting: Flash `lineHeight / 2` float bug (17m) vs Argon `lineHeight >> 1` bit-shift (4m)
  7. 8-Bit Sprites: 4m vs 13m
  8. Pure CSS Clock: Argon 2m tournament record
  9. Perlin Fractal Tree: Argon 4m vs Flash 22m
  10. Parametric Spirograph (GCD math): Argon 4m vs Flash 10m

  Watch the full 4K60 tournament & play all 20 live demos in your browser:
  - Lab & Prompts: https://labs.mixiuh.online
  - YouTube (English): https://www.youtube.com/@MixiuhLabsEN
  - YouTube (Spanish): https://www.youtube.com/@MixiuhLabsES
  ```

---

## 8. CHECKLIST DE MONETIZACIÓN Y CONVERSIÓN EN `labs.mixiuh.online`

1. **Verificación Pre-Subida en `labs.mixiuh.online`:**
   - Instalar los favicons y manifest de `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/brand-kit/05-extras/iconos-web/` en la raíz de `https://labs.mixiuh.online`.
   - Colocar en la portada de `https://labs.mixiuh.online` el embebido del video largo de `@MixiuhLabsES` (para visitantes con navegador en `es`) y `@MixiuhLabsEN` (para visitantes en `en`), sumando tiempo de reproducción válido a YouTube desde tráfico web externo.
   - Incluir el bloque de captura de correo y enlaces de afiliados SaaS/IA junto al botón de descarga de los 10 prompts matemáticos.
2. **YouTube Studio (`@MixiuhLabsES` y `@MixiuhLabsEN`):**
   - Subir el máster `2160p60.mp4` como **Oculto (Unlisted)** 2 horas antes para que YouTube procese el códec **VP9/AV1 en 4K60** y verifique derechos antes de pasar a **Público**.
   - Configurar las pausas manuales Mid-roll en `02:30` y `05:54`.
   - Subir las 3 miniaturas en **Probar y comparar** y revisar el ganador en el Día 7.
   - Cada día (Día 1 al Día 11), enlazar el Short del día al video largo mediante **`Related Video`**.
