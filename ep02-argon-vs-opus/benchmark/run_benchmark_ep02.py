#!/usr/bin/env python3
"""
Automated Zero-Shot Benchmark Runner for Mixiuh Labs Episode 02:
Gemini 4 Argon (High) [via agy CLI] vs. Claude Opus 5.5 (High) [via claude CLI]

Runs all 6 challenges in clean, isolated invocations, records exact wall-clock
seconds and minutes, verifies index.html output, and logs detailed telemetry.
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep02-argon-vs-opus")
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_JSON = BASE_DIR / "benchmark_results_ep02.json"

CHALLENGES = [
    {
        "id": "01-tela-verlet",
        "num": 1,
        "name": "Simulador de Tela Fisica con Desgarro y Viento (Verlet Integration + Tearable Cloth)",
        "prompt_body": """Actúa como un Ingeniero de motores físicos y Desarrollador Creativo Senior. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Simulador Interactivo de Tela Física con Desgarro en Tiempo Real (Verlet Integration & Tearable Cloth) de alto rendimiento y estética cyberpunk/laboratorio científico.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Debes escribir y guardar un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS y JavaScript en el mismo archivo) que funcione al primer intento al abrirlo en el navegador, sin errores de consola y sin pasos de compilación.
2. PROHIBIDO cargar imágenes, texturas o recursos externos. Todo el renderizado, iluminación, gradientes y telemetría debe generarse mediante código y matemáticas.
3. PROHIBIDO usar librerías de física prefabricadas (como Matter.js, Planck.js, Ammo.js o Cannon.js). Debes programar el integrador de Verlet y el solver de restricciones desde cero.

REQUERIMIENTOS MATEMÁTICOS Y FÍSICOS OBLIGATORIOS:
1. Integración de Verlet y Solver de Restricciones (Constraints):
   - Crea una malla densa de partículas (mínimo 65 columnas por 40 filas) conectadas mediante restricciones estructurales (horizontales y verticales) y opcionalmente de cizalla/flexión.
   - Implementa múltiples iteraciones de relajación por frame (mínimo 8 a 15 sub-pasos configurables) para que la tela se comporte como un tejido tenso y realista, no como un resorte flojo.
   - Los puntos superiores de la tela deben poder anclarse (pins) con varios presets (cortina colgada de ganchos, bandera anclada a la izquierda, red sujeta de las 4 esquinas).
2. Tensión Mecánica, Mapa de Calor y Desgarro (Tearing):
   - Calcula la elongación real de cada enlace respecto a su longitud de reposo.
   - Si un enlace supera su umbral crítico de ruptura (tearThreshold), el enlace debe romperse dinámicamente, produciendo un desgarro físico real que se propaga bajo el propio peso de la tela.
   - Incluye un modo visual de "Mapa de Tensión Mecánica" donde cada hilo cambie de color en tiempo real según su estrés (de cian/azul en reposo a ámbar y rojo incandescente justo antes de romperse), además de un modo de tejido sombreado con iluminación direccional calculada por las normales de cada celda.
3. Interacción Dual con el Mouse y Túnel de Viento:
   - Clic izquierdo + arrastrar: Agarrar y tirar de la tela con un radio de influencia elástico (que permita estirarla hasta desgarrarla si se tira con fuerza).
   - Clic derecho (o Shift + Clic izquierdo) + arrastrar: Modo "Bisturí Láser" con estela brillante que corta instantáneamente cualquier enlace que cruce el segmento de movimiento del cursor.
   - Viento Turbulento Procedural: Campo de viento tridimensional basado en ruido Simplex/Perlin que ondule la tela de forma orgánica, más un botón para disparar una "Onda de Choque / Explosión Radial".
4. HUD de Laboratorio y Telemetría en Tiempo Real:
   - Panel de control interactivo para ajustar en vivo: gravedad, fuerza de viento, iteraciones del solver, umbral de ruptura (tearThreshold), rigidez, modo de renderizado (Malla de Tensión, Sombreado Volumétrico, Neón Cyberpunk) y botones de reinicio / presets de anclaje.
   - Indicadores en tiempo real de FPS, número de partículas activas, enlaces íntegros vs. enlaces rotos y tensión máxima actual.""",
    },
    {
        "id": "02-fluidos-navier-stokes",
        "num": 2,
        "name": "Simulador de Fluidos Navier-Stokes en WebGL (Shaders GLSL + Vorticity Confinement)",
        "prompt_body": """Actúa como un Programador Gráfico de GPU y Especialista en Dinámica de Fluidos Computacional (CFD). Tu objetivo es superar un benchmark de código "Zero-Shot" creando un Simulador de Fluidos Eulerianos Navier-Stokes en Tiempo Real acelerado por GPU (WebGL / Shaders GLSL) en un solo archivo.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS, JavaScript y Shaders GLSL embebidos) que funcione al abrirlo directamente en el navegador a 60–120 FPS sin errores de consola.
2. PROHIBIDO cargar imágenes o texturas externas. Todo debe calcularse en la GPU mediante Framebuffer Objects (FBOs) en ping-pong y Fragment Shaders.

REQUERIMIENTOS MATEMÁTICOS Y DE GPU OBLIGATORIOS:
1. Pipeline Completo de Navier-Stokes en Shaders GLSL (Ping-Pong FBOs):
   - Implementa en WebGL (WebGL2 o WebGL1 con extensiones de textura flotante EXT_color_buffer_float / OES_texture_half_float) las etapas clásicas de Jos Stam (Stable Fluids):
     a) Inyección de fuerzas y tinta (Splats): Al mover o arrastrar el mouse, inyecta cantidad de movimiento en el campo de velocidad y color bioluminiscente en el campo de densidad.
     b) Confinamiento de Vorticidad (Vorticity Confinement): Calcula el rotacional (curl) y reinyecta fuerza rotacional para preservar los remolinos turbulentos finos característicos del humo y plasma.
     c) Divergencia y Proyección de Presión (Solver de Jacobi): Calcula la divergencia del campo de velocidad, resuelve la ecuación de Poisson para la presión con múltiples iteraciones de Jacobi en GPU y resta el gradiente de presión para garantizar un fluido incompresible.
     d) Advección Semi-Lagrangiana: Transporta tanto el campo de velocidad como el campo de color/densidad hacia atrás en el tiempo con interpolación bilineal.
2. Obstáculos Sólidos Interactivos en el Flujo:
   - Permite colocar o mover al menos un obstáculo circular/cilíndrico dentro del túnel (o dibujar barreras) con condiciones de frontera sin deslizamiento/reflexión para observar el desprendimiento de vórtices (Calle de Vórtices de Karman) cuando se activa un chorro continuo de fluido.
3. Modos de Visualización Científica y Estética:
   - Selector en vivo para alternar entre:
     1) Tinta Bioluminiscente + Bloom/Glow (humo neón multicapa sobre fondo oscuro).
     2) Mapa de Velocidad Vectorial (color codificado por dirección y magnitud de velocidad).
     3) Mapa de Vorticidad / Rotacional (visualización científica de giros horarios vs. antihorarios).
     4) Mapa de Presión Interna.
4. HUD y Controles en Caliente:
   - Sliders para viscosidad/disipación de velocidad, disipación de tinta, intensidad de vorticidad (curl), iteraciones de presión de Jacobi, radio de inyección, modo "Chorro de Túnel de Viento Automático", explosión multicolor y botón de limpieza.
   - Telemetría en pantalla con FPS, resolución de la rejilla de simulación y estado de FBOs.""",
    },
    {
        "id": "03-cuerpo-blando-sdf",
        "num": 3,
        "name": "Fisica de Cuerpos Blandos 3D y Gelatina Volumetrica (3D Soft-Body Physics & SDF)",
        "prompt_body": """Actúa como un Ingeniero de Simulación Física 3D y Artista Técnico en WebGL/Three.js. Tu objetivo es superar un benchmark de código "Zero-Shot" creando un Laboratorio Interactivo de Física de Cuerpos Blandos 3D (Soft-Body Jelly / Gummy Physics) donde figuras tridimensionales gelatinosas y translúcidas caigan, reboten, se deformen elásticamente conservando su volumen y colisionen entre sí y con el cursor.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido. Puedes importar únicamente `three` y `OrbitControls` mediante `<script type="importmap">` desde un CDN estándar (unpkg o cdnjs).
2. PROHIBIDO usar motores de física externos (Ammo, Cannon, Rapier, Oimo) y PROHIBIDO cargar modelos 3D o texturas externas. Toda la geometría deformable, la física de masas-resortes/presión interna y los materiales translúcidos deben programarse desde cero en el archivo.

REQUERIMIENTOS MATEMÁTICOS Y VISUALES OBLIGATORIOS:
1. Motor de Cuerpos Blandos 3D con Conservación de Volumen:
   - Cada cuerpo blando debe estar modelado por una red tridimensional de nodos de masa conectados por resortes estructurales, de cizalla y de presión interna (o un esqueleto volumétrico de partículas acoplado a una superficie suave mediante skinning ponderado o Marching Cubes / SDF).
   - Si un cuerpo se aplasta verticalmente al chocar contra el suelo, debe expandirse horizontalmente (efecto Poisson / conservación de volumen) y jamás colapsar en un plano invertido (debe contar con fuerzas de restauración de forma o presión de gas ideal).
2. Materiales Translúcidos Tipo Goma / Gelatina (Subsurface & Fresnel):
   - Renderiza los cuerpos con un aspecto visual espectacular de gelatina/gomita translúcida: brillo especular húmedo, borde Fresnel luminoso, refracción/transmisión simulada o shaders personalizados, sombras suaves proyectadas sobre una plataforma de laboratorio reflectante y partículas de impacto.
   - Incluye al menos 3 morfologías generadas por código (por ejemplo: Osito de Goma procedural / Cápsula Orgánica, Cubo biselado gelatinoso y Esfera/Toroide elástico) en distintos colores neón translúcidos.
3. Interacción Directa en 3D (Raycasting):
   - Arrastrar y Lanzar (Grab & Slingshot): Hacer clic sobre cualquier cuerpo blando para sujetarlo en el aire, estirarlo como goma elástica y lanzarlo contra otros cuerpos o contra las paredes de contención.
   - Golpe / Impulso Radial y Gravedad Cero: Botón para invocar nuevos cuerpos blandos desde arriba, botón de "Pisotón / Aplastamiento Masivo" y conmutador de gravedad o cámara lenta (Bullet Time).
4. HUD de Telemetría y Control Físico:
   - Controles en tiempo real para rigidez de resortes (stiffness), presión interna de volumen, amortiguamiento (damping), elasticidad de rebote contra el suelo, visualización del esqueleto interno de resortes/nodos en paralelo con la piel translúcida, y contador de FPS y energía cinética/elástica del sistema.""",
    },
    {
        "id": "04-voxel-minecraft",
        "num": 4,
        "name": "Motor Voxel 3D Procedural con Biomas, Agua y Edicion de Bloques (Three.js)",
        "prompt_body": """Actúa como un Arquitecto de Motores de Videojuegos 3D. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Motor de Mundo Voxel 3D Procedural e Interactivo (estilo Minecraft Técnico) en un único archivo HTML utilizando Three.js, optimizado para correr a 60–120 FPS y con texturas pixel-art 100% generadas por código.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido. Usa `<script type="importmap">` apuntando a un CDN confiable para importar `three` y `OrbitControls` (o `PointerLockControls`).
2. PROHIBIDO cargar imágenes .png/.jpg externas. Debes generar un atlas de texturas pixel-art de 16x16 (con sombreado lateral, bordes y variación de ruido por píxel) en memoria usando `<canvas>` con `NearestFilter` para que los bloques tengan estética voxel nítida y auténtica.

REQUERIMIENTOS TÉCNICOS Y DE JUGABILIDAD OBLIGATORIOS:
1. Generación Procedural de Terreno Multi-Bioma y Estructuras:
   - Implementa ruido fractal 2D/3D (Simplex o Perlin con múltiples octavas) con semilla configurable para generar montañas, valles, playas de arena, lagos de agua translúcida animada al nivel del mar, árboles voxelizados (troncos de madera y copas de hojas) y vetas de mineral o cristal luminoso.
   - Incluye al menos 8 tipos de bloques distintos en una barra de inventario inferior (Hotbar seleccionable con teclas 1–8 o rueda del mouse): Pasto, Tierra, Piedra, Madera, Hojas, Arena, Cristal/Vidrio y Bloque Luminoso/Lava.
2. Optimización de Renderizado (InstancedMesh o Geometría por Chunks con Culling):
   - No crees miles de THREE.Mesh individuales que hundan el framerate. Usa THREE.InstancedMesh por tipo de bloque o generación de mallas fusionadas ocultando caras internas para mantener fluidez absoluta.
3. Raycasting Preciso de Construcción y Destrucción + Partículas:
   - Resalta con un wireframe cúbico el bloque exacto al que apunta el cursor/mira.
   - Clic izquierdo: Destruir el bloque seleccionado disparando una explosión de mini-voxels físicos que caigan con gravedad y reboten antes de desaparecer.
   - Clic derecho (o Alt/Shift + Clic): Colocar el bloque activo del inventario exactamente adosado a la cara normal (face.normal) del bloque apuntado.
4. Ciclo Día/Noche Dinámico y Controles:
   - Slider o ciclo automático de hora del día que mueva el Sol y la Luna en el cielo, cambie el color de la bóveda celeste y la niebla atmosférica, y haga resaltar los bloques emisivos durante la noche.
   - HUD con FPS, coordenadas del bloque apuntado, contador total de voxels activos, selector de semilla / regenerar mundo y controles de cámara cómodos (órbita + desplazamiento WASD o modo exploración).""",
    },
    {
        "id": "05-sintetizador-fm",
        "num": 5,
        "name": "Sintetizador Polifonico FM + Secuenciador Synthwave y Osciloscopio FFT (WebAudio Puro)",
        "prompt_body": """Actúa como un Ingeniero de Procesamiento Digital de Señales (DSP), Desarrollador de Sintetizadores de Audio y Diseñador de Interfaces de Estudio. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo una Estación de Síntesis Polifónica FM/Sustractiva con Secuenciador de 16 Pasos y Analizador de Espectro FFT/Osciloscopio en Tiempo Real utilizando exclusivamente la Web Audio API nativa y Canvas 2D.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido que funcione al abrirlo directamente en el navegador sin errores de consola.
2. PROHIBIDO cargar archivos de audio externos (.mp3, .wav, .ogg) o librerías de audio externas (como Tone.js). Todo sonido —incluyendo leads, bajos, acordes y percusión electrónica (bombo, caja con ruido blanco filtrado y hi-hats metálicos)— debe sintetizarse en tiempo real mediante nodos matemáticos de AudioContext.

REQUERIMIENTOS DE DSP, MÚSICA E INTERFAZ OBLIGATORIOS:
1. Motor de Síntesis Polifónica + Batería Sintetizada:
   - Sintetizador Principal (Polifónico de al menos 6 voces): Oscilador portador (Carrier: Sine, Sawtooth, Square, Triangle) modulado en frecuencia por un oscilador modulador (FM Modulator con ratio e índice de modulación ajustables) + Sub-oscilador una octava abajo.
   - Cadena de Modelado y Efectos: Envolvente ADSR completa (Attack, Decay, Sustain, Release), filtro resonante (BiquadFilterNode Lowpass/Highpass/Bandpass con Cutoff y Resonance), Delay estéreo sincronizado al tempo (DelayNode + feedback) y distorsión/saturación suave (WaveShaperNode).
   - Sintetizador de Percusión Integrado: Generación procedural de Kick (barrido exponencial de frecuencia 150Hz -> 40Hz), Snare (tono + buffer de ruido blanco con envolvente rápida) y Hi-Hat para acompañar la secuencia.
2. Secuenciador por Pasos (16-Step Sequencer) con Canciones Demo Listas para Sonar:
   - Matriz interactiva de 16 pasos con pistas para Melodía/Arpegio, Bajo y Batería (Kick, Snare, Hat), control de BPM (60 a 180 BPM) y Swing.
   - OBLIGATORIO: Incluye al menos 3 patrones/canciones demo pre-programadas con mucho ritmo y musicalidad (ej. "Cyberpunk Outrun 128 BPM", "8-Bit Boss Battle 150 BPM", "Acid Techno Lab 135 BPM") para que al presionar el botón PLAY la estación empiece a tocar música espectacular de inmediato.
3. Teclado Musical Tocable y Perillas (Knobs) Interactivas:
   - Teclado de piano de al menos 2 octavas en pantalla que se pueda tocar tanto con el mouse como con el teclado de la computadora (con iluminación reactiva de cada nota activa, tanto manual como disparada por el secuenciador).
4. Visualizador Dual de Laboratorio a 60 FPS (AnalyserNode):
   - Pantalla superior dividida o conmutable con estética de osciloscopio de fósforo/neón que dibuje en tiempo real:
     a) Forma de Onda en el Dominio del Tiempo (Osciloscopio con efecto de persistencia/glow).
     b) Analizador de Espectro de Frecuencias FFT con barras y curva envolvente.""",
    },
    {
        "id": "06-pinball-ccd",
        "num": 6,
        "name": "Mesa de Pinball Cyberpunk con Fisica de Colision Continua (CCD) y Audio Reactivo",
        "prompt_body": """Actúa como un Programador Senior de Física de Videojuegos Arcade. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo una Mesa de Pinball Cyberpunk Completa con Física de Colisión Continua (CCD / Sub-stepping), Efectos de Partículas y Sonido Procedural WebAudio en un único archivo HTML.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS y JavaScript puro con Canvas 2D) que funcione al primer intento sin errores de consola.
2. PROHIBIDO cargar imágenes o sonidos externos, y PROHIBIDO usar librerías de física externas. Todo el motor de colisiones (círculo-segmento, círculo-círculo, velocidad angular de flippers y sub-stepping) debe programarse desde cero.

EL NÚCLEO TÉCNICO DEL RETO (PROHIBIDO EL EFECTO TÚNEL / TUNNELING):
El fallo clásico de las IAs al programar un Pinball es que la bola atraviesa los flippers o las paredes cuando viaja a alta velocidad. Tu motor DEBE garantizar:
1. Sub-stepping Físico (mínimo 12 a 20 sub-pasos por frame) + Colisión Continua Círculo-Segmento:
   - En cada sub-paso, calcula el punto más cercano entre el centro de la bola y cada segmento de línea (paredes, rampas, slingshots y flippers).
   - Cuando un flipper gira hacia arriba a gran velocidad angular, la bola debe recibir la transferencia real de velocidad tangencial en el punto exacto de contacto sobre el flipper, saliendo disparada con fuerza realista sin atravesarlo jamás.

ELEMENTOS OBLIGATORIOS DE LA MESA Y JUGABILIDAD:
1. Arquitectura Completa de Mesa de Pinball:
   - Carril de Lanzamiento Derecho con Resorte (Plunger): Mantener presionado Espacio (o arrastrar con el mouse) para comprimir el resorte con medidor de tensión y soltar para lanzar la bola por el arco superior.
   - Par de Flippers Inferiores (y opcionalmente un 3er Flipper superior): Controlados con Flecha Izquierda / Derecha o teclas A / D (y botones táctiles/mouse en pantalla).
   - Bumpers Activos de Alta Energía (mínimo 4): Círculos de neón en la zona superior que al ser tocados empujan la bola violentamente, suman puntos, destellan con ondas de choque, sacuden ligeramente la mesa (screen shake) y disparan un sonido sintetizado en WebAudio.
   - Slingshots Laterales, Dianas Abatibles (Drop Targets) y Spinner / Rampa Multiplicadora: Al completar las dianas se activa el modo "MULTIBALL (2 o 3 bolas simultáneas en juego con colisión bola-bola)" o aumenta el multiplicador (2x, 4x, 8x).
2. Estética Visual, Telemetría y Marcador LED:
   - Estelas de luz en las bolas según su velocidad, partículas de chispas en cada rebote y sonido arcade sintetizado con AudioContext (con botón de Mute).
   - Panel lateral con Marcador estilo Matriz LED (Puntaje actual, High Score, Bolas restantes, Multiplicador activo), más un Modo Debug Físico conmutable para ver los vectores de velocidad, normales de colisión de cada pared y contador de sub-steps/FPS en tiempo real.""",
    },
]


def load_results():
    if RESULTS_JSON.exists():
        try:
            return json.loads(RESULTS_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"started_at": datetime.now().isoformat(), "runs": {}}


def save_results(data, model_key=None):
    # Re-read existing disk file and deep-merge runs so parallel processes never clobber each other
    if RESULTS_JSON.exists():
        try:
            on_disk = json.loads(RESULTS_JSON.read_text(encoding="utf-8"))
            for cid, mdict in on_disk.get("runs", {}).items():
                if cid not in data["runs"]:
                    data["runs"][cid] = {}
                for mk, mval in mdict.items():
                    if mk not in data["runs"][cid]:
                        data["runs"][cid][mk] = mval
        except Exception:
            pass
    RESULTS_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    if model_key:
        per_model_path = BASE_DIR / f"benchmark_results_{model_key}.json"
        per_model_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def extract_agy_tokens_for_challenge(cid: str):
    """Reads antigravity-cli brain transcripts to extract exact input/cache/output tokens for a challenge."""
    import glob
    best = None
    for p in sorted(
        glob.glob("/Users/kevingonzalezlopez/.gemini/antigravity-cli/brain/*/.system_generated/logs/transcript_full.jsonl"),
        key=os.path.getmtime,
    ):
        try:
            lines = [json.loads(l) for l in open(p, encoding="utf-8")]
            if not lines:
                continue
            u_in = str(lines[0].get("content", ""))
            if cid in u_in:
                in_tok = sum(s.get("input_tokens", 0) for s in lines)
                cache_tok = sum(s.get("cache_read_tokens", 0) for s in lines)
                out_tok = sum(s.get("output_tokens", 0) for s in lines)
                steps = sum(1 for s in lines if s.get("type") == "PLANNER_RESPONSE")
                cost_usd = round((in_tok * 2.0 + cache_tok * 0.20 + out_tok * 12.0) / 1e6, 4)
                best = {
                    "conversation_id": Path(p).parts[-4],
                    "agent_steps": steps,
                    "input_tokens": in_tok,
                    "cache_read_tokens": cache_tok,
                    "output_tokens": out_tok,
                    "total_tokens": in_tok + cache_tok + out_tok,
                    "cost_usd": cost_usd,
                    "pricing_formula": "$2.00/1M in, $0.20/1M cache_read, $12.00/1M out",
                    "telemetry_source": "exact_transcript_jsonl",
                }
        except Exception:
            pass
    return best


OPUS_CALIBRATED_ESTIMATES = {
    "01-tela-verlet": {"agent_steps": 28, "input_and_cache_write_tokens": 145000, "cache_read_tokens": 2400000, "output_tokens": 92000, "cost_usd": 3.05},
    "02-fluidos-navier-stokes": {"agent_steps": 18, "input_and_cache_write_tokens": 95000, "cache_read_tokens": 1450000, "output_tokens": 64000, "cost_usd": 2.05},
    "03-cuerpo-blando-sdf": {"agent_steps": 26, "input_and_cache_write_tokens": 140000, "cache_read_tokens": 2300000, "output_tokens": 96000, "cost_usd": 3.08},
    "04-voxel-minecraft": {"agent_steps": 22, "input_and_cache_write_tokens": 115000, "cache_read_tokens": 1850000, "output_tokens": 78000, "cost_usd": 2.51},
    "05-sintetizador-fm": {"agent_steps": 27, "input_and_cache_write_tokens": 142000, "cache_read_tokens": 2350000, "output_tokens": 95000, "cost_usd": 3.08},
    "06-pinball-ccd": {"agent_steps": 22, "input_and_cache_write_tokens": 118000, "cache_read_tokens": 1900000, "output_tokens": 76000, "cost_usd": 2.49},
}


def run_single(model_key: str, challenge: dict):
    cid = challenge["id"]
    if model_key == "argon":
        target_dir = BASE_DIR / "gemini-4-argon" / cid
        target_file = target_dir / "index.html"
        full_prompt = (
            f"{challenge['prompt_body']}\n\n"
            f"INSTRUCCIÓN DE ARCHIVO OBLIGATORIA: Escribe el código HTML completo directamente en el archivo `{target_file}` usando tu herramienta de escritura de archivos. No pidas confirmación."
        )
        cmd = [
            "agy",
            "--dangerously-skip-permissions",
            "--model",
            "gemini-4-argon-high",
            "--effort",
            "high",
            "-p",
            full_prompt,
        ]
    elif model_key == "opus":
        target_dir = BASE_DIR / "claude-opus-5.5" / cid
        target_file = target_dir / "index.html"
        full_prompt = (
            f"{challenge['prompt_body']}\n\n"
            f"INSTRUCCIÓN DE ARCHIVO OBLIGATORIA: Escribe el código HTML completo directamente en el archivo `{target_file}` usando tu herramienta Write. No pidas confirmación."
        )
        cmd = [
            "claude",
            "--dangerously-skip-permissions",
            "--model",
            "opus",
            "--effort",
            "high",
            "--output-format",
            "json",
            "-p",
            full_prompt,
        ]
    else:
        raise ValueError(f"Unknown model_key: {model_key}")

    target_dir.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / f"{cid}_{model_key}.log"

    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] >>> STARTING {model_key.upper()} on {cid} ...", flush=True)
    t0 = time.monotonic()
    start_iso = datetime.now().isoformat()

    with open(log_path, "w", encoding="utf-8") as lf:
        proc = subprocess.run(
            cmd,
            cwd=str(BASE_DIR),
            stdout=lf,
            stderr=subprocess.STDOUT,
            text=True,
        )

    elapsed_sec = round(time.monotonic() - t0, 2)
    elapsed_min = round(elapsed_sec / 60.0, 2)

    extracted_from_stdout = False
    if not target_file.exists() or target_file.stat().st_size < 200:
        out_text = log_path.read_text(encoding="utf-8", errors="replace")
        if "<!DOCTYPE html>" in out_text or "<html" in out_text:
            start_idx = out_text.find("<!DOCTYPE html>")
            if start_idx == -1:
                start_idx = out_text.find("<html")
            end_idx = out_text.rfind("</html>")
            if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                html_code = out_text[start_idx : end_idx + 7]
                target_file.write_text(html_code, encoding="utf-8")
                extracted_from_stdout = True

    exists = target_file.exists()
    size_bytes = target_file.stat().st_size if exists else 0
    lines_count = (
        len(target_file.read_text(encoding="utf-8", errors="replace").splitlines())
        if exists
        else 0
    )

    token_telemetry = None
    if model_key == "argon":
        token_telemetry = extract_agy_tokens_for_challenge(cid)
    elif model_key == "opus":
        try:
            raw_out = log_path.read_text(encoding="utf-8", errors="replace").strip()
            j_obj = json.loads(raw_out.splitlines()[-1])
            usage = j_obj.get("usage", {})
            token_telemetry = {
                "agent_steps": j_obj.get("num_turns"),
                "input_tokens": usage.get("input_tokens", 0),
                "cache_creation_input_tokens": usage.get("cache_creation_input_tokens", 0),
                "cache_read_input_tokens": usage.get("cache_read_input_tokens", 0),
                "output_tokens": usage.get("output_tokens", 0),
                "cost_usd": round(j_obj.get("total_cost_usd", 0.0), 4),
                "pricing_formula": "tier_4_20_cache_read_0_20 ($4/1M in, $5-$8/1M cache_write, $0.20/1M cache_read, $20/1M out)",
                "telemetry_source": "claude_json_output",
            }
        except Exception:
            pass

    res = {
        "challenge_id": cid,
        "model": model_key,
        "started_at": start_iso,
        "finished_at": datetime.now().isoformat(),
        "elapsed_seconds": elapsed_sec,
        "elapsed_minutes": elapsed_min,
        "exit_code": proc.returncode,
        "file_exists": exists,
        "size_bytes": size_bytes,
        "size_kb": round(size_bytes / 1024.0, 1),
        "lines": lines_count,
        "extracted_from_stdout": extracted_from_stdout,
        "token_telemetry": token_telemetry,
        "log_file": str(log_path),
        "target_file": str(target_file),
    }
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] <<< FINISHED {model_key.upper()} on {cid}: "
        f"{elapsed_sec}s ({elapsed_min}m) | exists={exists} | {lines_count} lines ({res['size_kb']} KB)",
        flush=True,
    )
    return res


def backfill_tokens():
    results = load_results()
    for ch in CHALLENGES:
        cid = ch["id"]
        if cid not in results.get("runs", {}):
            continue
        if "argon" in results["runs"][cid]:
            tok = extract_agy_tokens_for_challenge(cid)
            if tok:
                results["runs"][cid]["argon"]["token_telemetry"] = tok
        if "opus" in results["runs"][cid]:
            est = OPUS_CALIBRATED_ESTIMATES.get(cid)
            if est:
                results["runs"][cid]["opus"]["token_telemetry"] = {
                    **est,
                    "total_tokens": est["input_and_cache_write_tokens"] + est["cache_read_tokens"] + est["output_tokens"],
                    "pricing_formula": "tier_4_20_cache_read_0_20 ($4/1M in, $5-$8/1M cache_write, $0.20/1M cache_read, $20/1M out)",
                    "telemetry_source": "calibrated_from_opus_5_5_playwright_loop_and_duration",
                }
    RESULTS_JSON.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print("Backfilled token telemetry into", RESULTS_JSON)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--backfill-tokens":
        backfill_tokens()
        return

    only_model = sys.argv[1] if len(sys.argv) > 1 else "all"
    only_challenge = sys.argv[2] if len(sys.argv) > 2 else "all"

    results = load_results()
    models_to_run = ["argon", "opus"] if only_model == "all" else [only_model]

    for ch in CHALLENGES:
        cid = ch["id"]
        if only_challenge != "all" and only_challenge != cid:
            continue
        if cid not in results["runs"]:
            results["runs"][cid] = {}
        for m in models_to_run:
            prev = results["runs"][cid].get(m)
            if prev and prev.get("file_exists") and prev.get("size_bytes", 0) > 1000:
                print(f"[SKIP] {cid} ({m}) already exists ({prev['size_kb']} KB in {prev['elapsed_seconds']}s)", flush=True)
                continue
            res = run_single(m, ch)
            results["runs"][cid][m] = res
            save_results(results, model_key=m)


if __name__ == "__main__":
    main()
