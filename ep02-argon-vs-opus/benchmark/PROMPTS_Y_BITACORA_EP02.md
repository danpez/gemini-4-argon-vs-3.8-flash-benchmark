# Laboratorio Mixiuh Labs — Episodio 02: Gemini 4 Argon (High) vs. Claude Opus 5.5 (High)

## 1. Presets y Configuracion Oficial de Igualdad (Fair-Play Protocol)

Para garantizar condiciones 100% simetricas y auditables entre ambos modelos:

* **Modelo A:** `Gemini 4 Argon` — Nivel de esfuerzo: **`High`**
* **Modelo B:** `Claude Opus 5.5` — Nivel de esfuerzo: **`High`** *(No usar Medium para no restarle capacidad de razonamiento extendido, ni Extra/Max/Ultracode porque disparan bucles multi-hora que consumen 3.5x+ de cuota y rompen la metrica de tiempo Zero-Shot).*
* **Contexto Limpio:** Cada uno de los 6 retos debe ejecutarse en una **conversacion/hilo completamente nuevo** (sin memoria del reto anterior).
* **Regla Zero-Shot:** Un solo envio de prompt por reto. Sin correcciones manuales ni segundo intento. El cronometro inicia al enviar el prompt y se detiene cuando el agente termina de escribir el archivo `index.html`.
* **Regla de Cero Assets Externos:** Prohibido cargar imagenes (`.png`, `.jpg`, `.svg` externos), texturas, modelos 3D o audios externos (`.mp3`, `.wav`). Todo arte, shader, textura y sonido debe generarse matematicamente por codigo.

---

## 2. Estructura de Carpetas del Episodio 02

Todo se guarda dentro de `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep02-argon-vs-opus/`:

```text
ep02-argon-vs-opus/
├── PROMPTS_Y_BITACORA_EP02.md
├── gemini-4-argon/
│   ├── 01-tela-verlet/index.html
│   ├── 02-fluidos-navier-stokes/index.html
│   ├── 03-cuerpo-blando-sdf/index.html
│   ├── 04-voxel-minecraft/index.html
│   ├── 05-sintetizador-fm/index.html
│   └── 06-pinball-ccd/index.html
├── claude-opus-5.5/
│   ├── 01-tela-verlet/index.html
│   ├── 02-fluidos-navier-stokes/index.html
│   ├── 03-cuerpo-blando-sdf/index.html
│   ├── 04-voxel-minecraft/index.html
│   ├── 05-sintetizador-fm/index.html
│   └── 06-pinball-ccd/index.html
└── grabaciones/
    ├── 01_tela_verlet_comparativa.mov
    ├── 02_fluidos_navier_stokes_comparativa.mov
    ├── 03_cuerpo_blando_sdf_comparativa.mov
    ├── 04_voxel_minecraft_comparativa.mov
    ├── 05_sintetizador_fm_comparativa.mov
    └── 06_pinball_ccd_comparativa.mov
```

*Nota al pegar cada prompt:*
- Cuando estés probando **Gemini 4 Argon (High)**, indícale al final del prompt: `Guarda el archivo en ep02-argon-vs-opus/gemini-4-argon/<nombre-carpeta>/index.html`
- Cuando estés probando **Claude Opus 5.5 (High)**, indícale al final del prompt: `Guarda el archivo en ep02-argon-vs-opus/claude-opus-5.5/<nombre-carpeta>/index.html`

---

## 3. Resumen Global (Tiempo, Lineas, FPS, Tokens y Coste en USD)

| Reto | `Argon` Tiempo | `Argon` Tokens (`In` / `Cache` / `Out`) | `Argon` Coste USD | `Opus` Tiempo | `Opus` Tokens Est. (`In+CW` / `Cache` / `Out`) | `Opus` Coste Est. USD | Veredicto del Arbitro |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **01. Tela Fisica Verlet** | **6.68 min** | `92.7K` / `0` / `38.5K` (`2 pasos`) | **`\$0.65`** | 30.87 min | `~145K` / `~2.40M` / `~92K` (`~28 pasos`) | `~\$3.05` | **Gana Argon** (`4.62x` mas rapido, `4.7x` mas barato y `120 FPS` vs `28 FPS`) |
| **02. Fluidos Navier-Stokes** | **10.00 min** | `290.2K` / `610.9K` / `58.4K` (`9 pasos`) | **`\$1.40`** | 18.47 min | `~95K` / `~1.45M` / `~64K` (`~18 pasos`) | `~\$2.05` | **Gana Argon** (`1.85x` mas rapido, `1.46x` mas barato y GPU Bloom multicapa) |
| **03. Cuerpo Blando 3D SDF** | 34.74 min | `332.3K` / `1.27M` / `88.1K` (`19 pasos`) | **`\$1.98`** | **30.87 min** | `~140K` / `~2.30M` / `~96K` (`~26 pasos`) | `~\$3.08` | **Gana Opus en Tiempo (`1.13x`) y 6 Formas / Argon en Coste y `120 FPS`** |
| **04. Motor Voxel 3D** | **6.99 min** | `94.5K` / `0` / `40.4K` (`2 pasos`) | **`\$0.67`** | 23.65 min | `~115K` / `~1.85M` / `~78K` (`~22 pasos`) | `~\$2.51` | **Empate Tecnico** (Argon `3.38x` mas rapido y `\$0.67`; Opus escala a `2.58M voxels`) |
| **05. Sintetizador FM + FFT** | **24.07 min** | `153.6K` / `317.9K` / `40.3K` (`10 pasos`) | **`\$0.85`** | 30.23 min | `~142K` / `~2.35M` / `~95K` (`~27 pasos`) | `~\$3.08` | **Gana Opus en Estudio (8 pistas + Acid 303) / Argon `3.6x` mas barato** |
| **06. Pinball CCD Arcade** | **7.65 min** | `97.2K` / `65.2K` / `41.2K` (`3 pasos`) | **`\$0.70`** | 24.57 min | `~118K` / `~1.90M` / `~76K` (`~22 pasos`) | `~\$2.49` | **Gana Argon** (`3.21x` mas rapido, `3.55x` mas barato, 3 flippers y Multiball 3x) |
| **TOTAL ACUMULADO** | **90.13 min** | **`1.06M` / `2.26M` / `306.9K`** (`45 pasos`) | **`\$6.26 USD`** | **158.66 min** | **`~755K` / `~12.25M` / `~501K`** (`~143 pasos`) | **`~\$16.26 USD`** | **Argon es `1.76x` mas rapido, `~2.60x` mas economico y genera `+63.7%` mas codigo** |

*Tarifas oficiales aplicadas:*
- **`Gemini 4 Argon (High)` (`agy` CLI — telemetria exacta extraida de `transcript_full.jsonl`):** `\$2.00 / 1M` Input, `\$0.20 / 1M` Cache Read, `\$12.00 / 1M` Output.
- **`Claude Opus 5.5 (High)` (`claude` CLI — tarifa oficial `tier_4_20_cache_read_0_20` extraida del binario de `claude`):** `\$4.00 / 1M` Input, `\$5.00–\$8.00 / 1M` Cache Write, `\$0.20 / 1M` Cache Read, `\$20.00 / 1M` Output.

---

### RETO 01: Simulador de Tela Fisica con Desgarro y Viento (Verlet Integration + Tearable Cloth)
* **Tiempo Gemini 4 Argon (High):** `6.68 minutos (400.74 s) | 2,766 lineas (88.0 KB) | 120 FPS`
* **Tiempo Claude Opus 5.5 (High):** `30.87 minutos (1,852.14 s) | 1,352 lineas (65.9 KB) | 28 FPS`
* **Ganador y Notas del Arbitro:** `Gana Gemini 4 Argon (High). Fue 4.62x mas rapido (6.68 min vs 30.87 min) y corre a 120 FPS clavados con osciloscopio de tension y chispas termicas. Opus activo cizalla + flexion (18,430 enlaces) con 30 iteraciones de relajacion por defecto, hundiendo el framerate en CPU a 28 FPS (6.28 ms/frame).`

#### Prompt Reto 01 (Copiar y pegar):

```markdown
Actúa como un Ingeniero de motores físicos y Desarrollador Creativo Senior. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un **Simulador Interactivo de Tela Física con Desgarro en Tiempo Real (Verlet Integration & Tearable Cloth)** de alto rendimiento y estética cyberpunk/laboratorio científico.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Debes entregar un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS y JavaScript en el mismo archivo) que funcione al primer intento al abrirlo en el navegador, sin errores de consola y sin pasos de compilación.
2. PROHIBIDO cargar imágenes, texturas o recursos externos. Todo el renderizado, iluminación, gradientes y telemetría debe generarse mediante código y matemáticas.
3. PROHIBIDO usar librerías de física prefabricadas (como Matter.js, Planck.js, Ammo.js o Cannon.js). Debes programar el integrador de Verlet y el solver de restricciones desde cero.

REQUERIMIENTOS MATEMÁTICOS Y FÍSICOS OBLIGATORIOS:
1. **Integración de Verlet y Solver de Restricciones (Constraints):**
   - Crea una malla densa de partículas (mínimo 65 columnas por 40 filas) conectadas mediante restricciones estructurales (horizontales y verticales) y opcionalmente de cizalla/flexión.
   - Implementa múltiples iteraciones de relajación por frame (mínimo 8 a 15 sub-pasos configurables) para que la tela se comporte como un tejido tenso y realista, no como un resorte flojo.
   - Los puntos superiores de la tela deben poder anclarse (pins) con varios presets (cortina colgada de ganchos, bandera anclada a la izquierda, red sujeta de las 4 esquinas).
2. **Tensión Mecánica, Mapa de Calor y Desgarro (Tearing):**
   - Calcula la elongación real de cada enlace respecto a su longitud de reposo.
   - Si un enlace supera su umbral crítico de ruptura (`tearThreshold`), el enlace debe romperse dinámicamente, produciendo un desgarro físico real que se propaga bajo el propio peso de la tela.
   - Incluye un modo visual de "Mapa de Tensión Mecánica" donde cada hilo cambie de color en tiempo real según su estrés (de cian/azul en reposo a ámbar y rojo incandescente justo antes de romperse), además de un modo de tejido sombreado con iluminación direccional calculada por las normales de cada celda.
3. **Interacción Dual con el Mouse y Túnel de Viento:**
   - **Clic izquierdo + arrastrar:** Agarrar y tirar de la tela con un radio de influencia elástico (que permita estirarla hasta desgarrarla si se tira con fuerza).
   - **Clic derecho (o Shift + Clic izquierdo) + arrastrar:** Modo "Bisturí Láser" con estela brillante que corta instantáneamente cualquier enlace que cruce el segmento de movimiento del cursor.
   - **Viento Turbulento Procedural:** Campo de viento tridimensional basado en ruido Simplex/Perlin que ondule la tela de forma orgánica, más un botón para disparar una "Onda de Choque / Explosión Radial".
4. **HUD de Laboratorio y Telemetría en Tiempo Real:**
   - Panel de control interactivo para ajustar en vivo: gravedad, fuerza de viento, iteraciones del solver, umbral de ruptura (`tearThreshold`), rigidez, modo de renderizado (Malla de Tensión, Sombreado Volumétrico, Neón Cyberpunk) y botones de reinicio / presets de anclaje.
   - Indicadores en tiempo real de FPS, número de partículas activas, enlaces íntegros vs. enlaces rotos y tensión máxima actual.

Escribe el archivo completo y funcional en la carpeta `01-tela-verlet/index.html` dentro del directorio asignado a tu modelo.
```

---

### RETO 02: Simulador de Fluidos Navier-Stokes en WebGL (Shaders GLSL + Vorticity Confinement)
* **Tiempo Gemini 4 Argon (High):** `10.00 minutos (600.02 s) | 2,506 lineas (83.6 KB) | 120 FPS`
* **Tiempo Claude Opus 5.5 (High):** `18.47 minutos (1,108.01 s) | 1,444 lineas (62.7 KB) | 120 FPS`
* **Ganador y Notas del Arbitro:** `Gana Gemini 4 Argon (High) en velocidad (1.85x mas rapido) e impacto visual con post-procesado GPU Bloom multicapa y dibujo de paredes libres. Opus logra una calle de vortices de Karman clasica y relieve volumetrico de tinta impecable a 120 FPS.`

#### Prompt Reto 02 (Copiar y pegar):

```markdown
Actúa como un Programador Gráfico de GPU y Especialista en Dinámica de Fluidos Computacional (CFD). Tu objetivo es superar un benchmark de código "Zero-Shot" creando un **Simulador de Fluidos Eulerianos Navier-Stokes en Tiempo Real acelerado por GPU (WebGL / Shaders GLSL)** en un solo archivo.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Entrega un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS, JavaScript y Shaders GLSL embebidos) que funcione al abrirlo directamente en el navegador a 60–120 FPS sin errores de consola.
2. PROHIBIDO cargar imágenes o texturas externas. Todo debe calcularse en la GPU mediante Framebuffer Objects (FBOs) en ping-pong y Fragment Shaders.

REQUERIMIENTOS MATEMÁTICOS Y DE GPU OBLIGATORIOS:
1. **Pipeline Completo de Navier-Stokes en Shaders GLSL (Ping-Pong FBOs):**
   - Implementa en WebGL (WebGL2 o WebGL1 con extensiones de textura flotante `EXT_color_buffer_float` / `OES_texture_half_float`) las etapas clásicas de Jos Stam (*Stable Fluids*):
     a) **Inyección de fuerzas y tinta (Splats):** Al mover o arrastrar el mouse, inyecta cantidad de movimiento en el campo de velocidad y color bioluminiscente en el campo de densidad.
     b) **Confinamiento de Vorticidad (Vorticity Confinement):** Calcula el rotacional ($\nabla \times \vec{u}$) y reinyecta fuerza rotacional para preservar los remolinos turbulentos finos característicos del humo y plasma.
     c) **Divergencia y Proyección de Presión (Solver de Jacobi):** Calcula la divergencia del campo de velocidad, resuelve la ecuación de Poisson para la presión con múltiples iteraciones de Jacobi en GPU y resta el gradiente de presión ($\nabla p$) para garantizar un fluido incompresible ($\nabla \cdot \vec{u} = 0$).
     d) **Advección Semi-Lagrangiana:** Transporta tanto el campo de velocidad como el campo de color/densidad hacia atrás en el tiempo con interpolación bilineal.
2. **Obstáculos Sólidos Interactivos en el Flujo:**
   - Permite colocar o mover al menos un obstáculo circular/cilíndrico dentro del túnel (o dibujar barreras) con condiciones de frontera sin deslizamiento/reflexión para observar el desprendimiento de vórtices (Calle de Vórtices de Karman) cuando se activa un chorro continuo de fluido.
3. **Modos de Visualización Científica y Estética:**
   - Selector en vivo para alternar entre:
     1) **Tinta Bioluminiscente + Bloom/Glow** (humo neón multicapa sobre fondo oscuro).
     2) **Mapa de Velocidad Vectorial** (color codificado por dirección y magnitud de velocidad).
     3) **Mapa de Vorticidad / Rotacional** (visualización científica de giros horarios vs. antihorarios).
     4) **Mapa de Presión Interna.**
4. **HUD y Controles en Caliente:**
   - Sliders para viscosidad/disipación de velocidad, disipación de tinta, intensidad de vorticidad (`curl`), iteraciones de presión de Jacobi, radio de inyección, modo "Chorro de Túnel de Viento Automático", explosión multicolor y botón de limpieza.
   - Telemetría en pantalla con FPS, resolución de la rejilla de simulación y estado de FBOs.

Escribe el archivo completo y funcional en la carpeta `02-fluidos-navier-stokes/index.html` dentro del directorio asignado a tu modelo.
```

---

### RETO 03: Fisica de Cuerpos Blandos 3D y Gelatina Volumetrica (3D Soft-Body Physics & SDF / Marching Cubes)
* **Tiempo Gemini 4 Argon (High):** `34.74 minutos (2,084.59 s) | 2,543 lineas (93.7 KB) | 120 FPS`
* **Tiempo Claude Opus 5.5 (High):** `30.87 minutos (1,852.28 s) | 1,701 lineas (101.7 KB) | 82 FPS`
* **Ganador y Notas del Arbitro:** `Gana Claude Opus 5.5 (High) por ligero margen en tiempo (30.87 min vs 34.74 min) y acabado estetico con 6 morfologias XPBD (Osito, Cubo, Toroide, Capsula, Flan, Esfera) y piso reflectante a 82 FPS. Argon gana en fluidez pura (120 FPS), vista simultanea Esqueleto + Piel y osciloscopio de energia.`

#### Prompt Reto 03 (Copiar y pegar):

```markdown
Actúa como un Ingeniero de Simulación Física 3D y Artista Técnico en WebGL/Three.js. Tu objetivo es superar un benchmark de código "Zero-Shot" creando un **Laboratorio Interactivo de Física de Cuerpos Blandos 3D (Soft-Body Jelly / Gummy Physics)** donde figuras tridimensionales gelatinosas y translúcidas caigan, rebotan, se deformen elásticamente conservando su volumen y colisionen entre sí y con el cursor.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Entrega un ÚNICO archivo `index.html` 100% autocontenido. Puedes importar únicamente `three` y `OrbitControls` mediante `<script type="importmap">` desde un CDN estándar (unpkg o cdnjs).
2. PROHIBIDO usar motores de física externos (Ammo, Cannon, Rapier, Oimo) y PROHIBIDO cargar modelos 3D o texturas externas. Toda la geometría deformable, la física de masas-resortes/presión interna y los materiales translúcidos deben programarse desde cero en el archivo.

REQUERIMIENTOS MATEMÁTICOS Y VISUALES OBLIGATORIOS:
1. **Motor de Cuerpos Blandos 3D con Conservación de Volumen:**
   - Cada cuerpo blando debe estar modelado por una red tridimensional de nodos de masa conectados por resortes estructurales, de cizalla y de presión interna (o un esqueleto volumétrico de partículas acoplado a una superficie suave mediante *skinning* ponderado o *Marching Cubes / SDF*).
   - Si un cuerpo se aplasta verticalmente al chocar contra el suelo, debe expandirse horizontalmente (*efecto Poisson / conservación de volumen*) y jamás colapsar en un plano invertido (debe contar con fuerzas de restauración de forma o presión de gas ideal $P \propto 1/V$).
2. **Materiales Translúcidos Tipo Goma / Gelatina (Subsurface & Fresnel):**
   - Renderiza los cuerpos con un aspecto visual espectacular de gelatina/gomita translúcida: brillo especular húmedo, borde Fresnel luminoso, refracción/transmisión simulada o shaders personalizados, sombras suaves proyectadas sobre una plataforma de laboratorio reflectante y partículas de impacto.
   - Incluye al menos 3 morfologías generadas por código (por ejemplo: Osito de Goma procedural / Cápsula Orgánica, Cubo biselado gelatinoso y Esfera/Toroide elástico) en distintos colores neón translúcidos.
3. **Interacción Directa en 3D (Raycasting):**
   - **Arrastrar y Lanzar (Grab & Slingshot):** Hacer clic sobre cualquier cuerpo blando para sujetarlo en el aire, estirarlo como goma elástica y lanzarlo contra otros cuerpos o contra las paredes de contención.
   - **Golpe / Impulso Radial y Gravedad Cero:** Botón para invocar nuevos cuerpos blandos desde arriba, botón de "Pisotón / Aplastamiento Masivo" y conmutador de gravedad o cámara lenta (*Bullet Time*).
4. **HUD de Telemetría y Control Físico:**
   - Controles en tiempo real para rigidez de resortes (`stiffness`), presión interna de volumen, amortiguamiento (`damping`), elasticidad de rebote contra el suelo, visualización del esqueleto interno de resortes/nodos en paralelo con la piel translúcida, y contador de FPS y energía cinética/elástica del sistema.

Escribe el archivo completo y funcional en la carpeta `03-cuerpo-blando-sdf/index.html` dentro del directorio asignado a tu modelo.
```

---

### RETO 04: Motor Voxel 3D Procedural con Biomas, Agua, Iluminacion y Edicion de Bloques (Three.js)
* **Tiempo Gemini 4 Argon (High):** `6.99 minutos (419.28 s) | 2,569 lineas (89.7 KB) | 120 FPS`
* **Tiempo Claude Opus 5.5 (High):** `23.65 minutos (1,419.27 s) | 1,665 lineas (91.6 KB) | 120 FPS`
* **Ganador y Notas del Arbitro:** `Empate Tecnico de Alto Contraste: Argon arrasa en velocidad (3.38x mas rapido: 6.99 min vs 23.65 min) con 66,684 voxels a 120 FPS e iconos 3D isometricos en el hotbar. Opus invirtio 23.65 min para construir un motor masivo de 2,586,165 voxels en 213 chunks con Ambient Occlusion por vertice, iluminacion BFS y picos nevados a 120 FPS.`

#### Prompt Reto 04 (Copiar y pegar):

```markdown
Actúa como un Arquitecto de Motores de Videojuegos 3D. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un **Motor de Mundo Voxel 3D Procedural e Interactivo (estilo Minecraft Técnico)** en un único archivo HTML utilizando Three.js, optimizado para correr a 60–120 FPS y con texturas pixel-art 100% generadas por código.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Entrega un ÚNICO archivo `index.html` 100% autocontenido. Usa `<script type="importmap">` apuntando a un CDN confiable para importar `three` y `OrbitControls` (o `PointerLockControls`).
2. PROHIBIDO cargar imágenes `.png/.jpg` externas. Debes generar un atlas de texturas pixel-art de 16x16 (con sombreado lateral, bordes y variación de ruido por píxel) en memoria usando `<canvas>` con `NearestFilter` para que los bloques tengan estética voxel nítida y auténtica.

REQUERIMIENTOS TÉCNICOS Y DE JUGABILIDAD OBLIGATORIOS:
1. **Generación Procedural de Terreno Multi-Bioma y Estructuras:**
   - Implementa ruido fractal 2D/3D (Simplex o Perlin con múltiples octavas) con semilla configurable para generar montañas, valles, playas de arena, lagos de agua translúcida animada al nivel del mar, árboles voxelizados (troncos de madera y copas de hojas) y vetas de mineral o cristal luminoso.
   - Incluye al menos 8 tipos de bloques distintos en una barra de inventario inferior (*Hotbar* seleccionable con teclas `1`–`8` o rueda del mouse): Pasto, Tierra, Piedra, Madera, Hojas, Arena, Cristal/Vidrio y Bloque Luminoso/Lava.
2. **Optimización de Renderizado (`InstancedMesh` o Geometría por Chunks con Culling):**
   - No crees miles de `THREE.Mesh` individuales que hundan el framerate. Usa `THREE.InstancedMesh` por tipo de bloque o generación de mallas fusionadas ocultando caras internas para mantener fluidez absoluta.
3. **Raycasting Preciso de Construcción y Destrucción + Partículas:**
   - Resalta con un wireframe cúbico el bloque exacto al que apunta el cursor/mira.
   - **Clic izquierdo:** Destruir el bloque seleccionado disparando una explosión de mini-voxels físicos que caigan con gravedad y reboten antes de desaparecer.
   - **Clic derecho (o Alt/Shift + Clic):** Colocar el bloque activo del inventario exactamente adosado a la cara normal (`face.normal`) del bloque apuntado.
4. **Ciclo Día/Noche Dinámico y Controles:**
   - Slider o ciclo automático de hora del día que mueva el Sol y la Luna en el cielo, cambie el color de la bóveda celeste y la niebla atmosférica, y haga resaltar los bloques emisivos durante la noche.
   - HUD con FPS, coordenadas del bloque apuntado, contador total de voxels activos, selector de semilla / regenerar mundo y controles de cámara cómodos (órbita + desplazamiento WASD o modo exploración).

Escribe el archivo completo y funcional en la carpeta `04-voxel-minecraft/index.html` dentro del directorio asignado a tu modelo.
```

---

### RETO 05: Sintetizador Polifonico FM + Secuenciador Synthwave y Osciloscopio FFT (WebAudio Puro)
* **Tiempo Gemini 4 Argon (High):** `24.07 minutos (1,444.15 s) | 2,586 lineas (81.0 KB) | 60 FPS`
* **Tiempo Claude Opus 5.5 (High):** `30.23 minutos (1,813.59 s) | 1,933 lineas (106.3 KB) | 60 FPS`
* **Ganador y Notas del Arbitro:** `Gana Opus 5.5 en profundidad de estudio (8 pistas con linea Acid 303 + Clap, 4 compases encadenables y 4 modos de visualizador incluyendo Goniometro X-Y y Espectrograma), mientras que Argon es 1.26x mas rapido (24.07 min vs 30.23 min) con 4 demos musicales y osciloscopio + FFT simultaneos.`

#### Prompt Reto 05 (Copiar y pegar):

```markdown
Actúa como un Ingeniero de Procesamiento Digital de Señales (DSP), Desarrollador de Sintetizadores de Audio y Diseñador de Interfaces de Estudio. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo una **Estación de Síntesis Polifónica FM/Sustractiva con Secuenciador de 16 Pasos y Analizador de Espectro FFT/Osciloscopio en Tiempo Real** utilizando exclusivamente la Web Audio API nativa y Canvas 2D.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Entrega un ÚNICO archivo `index.html` 100% autocontenido que funcione al abrirlo directamente en el navegador sin errores de consola.
2. PROHIBIDO cargar archivos de audio externos (`.mp3`, `.wav`, `.ogg`) o librerías de audio externas (como Tone.js). Todo sonido —incluyendo leads, bajos, acordes y percusión electrónica (bombo, caja con ruido blanco filtrado y hi-hats metálicos)— debe sintetizarse en tiempo real mediante nodos matemáticos de `AudioContext`.

REQUERIMIENTOS DE DSP, MÚSICA E INTERFAZ OBLIGATORIOS:
1. **Motor de Síntesis Polifónica + Batería Sintetizada:**
   - **Sintetizador Principal (Polifónico de al menos 6 voces):** Oscilador portador (*Carrier*: Sine, Sawtooth, Square, Triangle) modulado en frecuencia por un oscilador modulador (*FM Modulator* con ratio e índice de modulación ajustables) + Sub-oscilador una octava abajo.
   - **Cadena de Modelado y Efectos:** Envolvente ADSR completa (Attack, Decay, Sustain, Release), filtro resonante (`BiquadFilterNode` Lowpass/Highpass/Bandpass con Cutoff y Resonance), Delay estéreo sincronizado al tempo (`DelayNode` + feedback) y distorsión/saturación suave (`WaveShaperNode`).
   - **Sintetizador de Percusión Integrado:** Generación procedural de Kick (barrido exponencial de frecuencia 150Hz -> 40Hz), Snare (tono + buffer de ruido blanco con envolvente rápida) y Hi-Hat para acompañar la secuencia.
2. **Secuenciador por Pasos (16-Step Sequencer) con Canciones Demo Listas para Sonar:**
   - Matriz interactiva de 16 pasos con pistas para Melodía/Arpegio, Bajo y Batería (Kick, Snare, Hat), control de BPM (60 a 180 BPM) y Swing.
   - **OBLIGATORIO:** Incluye al menos 3 patrones/canciones demo pre-programadas con mucho ritmo y musicalidad (ej. *"Cyberpunk Outrun 128 BPM"*, *"8-Bit Boss Battle 150 BPM"*, *"Acid Techno Lab 135 BPM"*) para que al presionar el botón **PLAY** la estación empiece a tocar música espectacular de inmediato.
3. **Teclado Musical Tocable y Perillas (Knobs) Interactivas:**
   - Teclado de piano de al menos 2 octavas en pantalla que se pueda tocar tanto con el mouse como con el teclado de la computadora (con iluminación reactiva de cada nota activa, tanto manual como disparada por el secuenciador).
4. **Visualizador Dual de Laboratorio a 60 FPS (`AnalyserNode`):**
   - Pantalla superior dividida o conmutable con estética de osciloscopio de fósforo/neón que dibuje en tiempo real:
     a) **Forma de Onda en el Dominio del Tiempo (Osciloscopio con efecto de persistencia/glow).**
     b) **Analizador de Espectro de Frecuencias FFT con barras y curva envolvente.**

Escribe el archivo completo y funcional en la carpeta `05-sintetizador-fm/index.html` dentro del directorio asignado a tu modelo.
```

---

### RETO 06: Mesa de Pinball Cyberpunk con Fisica de Colision Continua (CCD) y Audio Reactivo
* **Tiempo Gemini 4 Argon (High):** `7.65 minutos (458.98 s) | 2,749 lineas (95.0 KB) | 20 Sub-pasos (1200 Hz)`
* **Tiempo Claude Opus 5.5 (High):** `24.57 minutos (1,474.07 s) | 1,508 lineas (79.4 KB) | 16 Sub-pasos (120 FPS)`
* **Ganador y Notas del Arbitro:** `Gana Gemini 4 Argon (High). Fue 3.21x mas rapido (7.65 min vs 24.57 min), incluye 3 flippers (con flipper superior derecho), 20 sub-pasos CCD a 1200 Hz (361,560 chequeos/seg), escudos kickback y boton directo TEST MULTIBALL (3X) para verificar colisiones bola-bola al instante.`

#### Prompt Reto 06 (Copiar y pegar):

```markdown
Actúa como un Programador Senior de Física de Videojuegos Arcade. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo una **Mesa de Pinball Cyberpunk Completa con Física de Colisión Continua (CCD / Sub-stepping), Efectos de Partículas y Sonido Procedural WebAudio** en un único archivo HTML.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Entrega un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS y JavaScript puro con Canvas 2D) que funcione al primer intento sin errores de consola.
2. PROHIBIDO cargar imágenes o sonidos externos, y PROHIBIDO usar librerías de física externas. Todo el motor de colisiones (círculo-segmento, círculo-círculo, velocidad angular de flippers y sub-stepping) debe programarse desde cero.

EL NÚCLEO TÉCNICO DEL RETO (PROHIBIDO EL EFECTO TÚNEL / TUNNELING):
El fallo clásico de las IAs al programar un Pinball es que la bola atraviesa los flippers o las paredes cuando viaja a alta velocidad. Tu motor DEBE garantizar:
1. **Sub-stepping Físico (mínimo 12 a 20 sub-pasos por frame) + Colisión Continua Círculo-Segmento:**
   - En cada sub-paso, calcula el punto más cercano entre el centro de la bola y cada segmento de línea (paredes, rampas, slingshots y flippers).
   - Cuando un flipper gira hacia arriba a gran velocidad angular ($\omega$), la bola debe recibir la transferencia real de velocidad tangencial ($\vec{v}_{\text{impacto}} = \vec{\omega} \times \vec{r}$) en el punto exacto de contacto sobre el flipper, saliendo disparada con fuerza realista sin atravesarlo jamás.

ELEMENTOS OBLIGATORIOS DE LA MESA Y JUGABILIDAD:
1. **Arquitectura Completa de Mesa de Pinball:**
   - **Carril de Lanzamiento Derecho con Resorte (Plunger):** Mantener presionado `Espacio` (o arrastrar con el mouse) para comprimir el resorte con medidor de tensión y soltar para lanzar la bola por el arco superior.
   - **Par de Flippers Inferiores (y opcionalmente un 3er Flipper superior):** Controlados con `Flecha Izquierda / Derecha` o teclas `A / D` (y botones táctiles/mouse en pantalla).
   - **Bumpers Activos de Alta Energía (mínimo 4):** Círculos de neón en la zona superior que al ser tocados empujan la bola violentamente, suman puntos, destellan con ondas de choque, sacuden ligeramente la mesa (*screen shake*) y disparan un sonido sintetizado en WebAudio.
   - **Slingshots Laterales, Dianas Abatibles (Drop Targets) y Spinner / Rampa Multiplicadora:** Al completar las dianas se activa el modo **"MULTIBALL (2 o 3 bolas simultáneas en juego con colisión bola-bola)"** o aumenta el multiplicador (`2x`, `4x`, `8x`).
2. **Estética Visual, Telemetría y Marcador LED:**
   - Estelas de luz en las bolas según su velocidad, partículas de chispas en cada rebote y sonido arcade sintetizado con `AudioContext` (con botón de Mute).
   - Panel lateral con Marcador estilo Matriz LED (Puntaje actual, High Score, Bolas restantes, Multiplicador activo), más un **Modo Debug Físico** conmutable para ver los vectores de velocidad, normales de colisión de cada pared y contador de sub-steps/FPS en tiempo real.

Escribe el archivo completo y funcional en la carpeta `06-pinball-ccd/index.html` dentro del directorio asignado a tu modelo.
```
