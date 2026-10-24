#!/usr/bin/env python3
"""
Automated Zero-Shot Benchmark Runner for Mixiuh Labs Episode 04:
La Escalera Completa de Claude 5.5:
  - Claude Haiku 5.5 (`claude-haiku-5-5`)
  - Claude Sonnet 5.5 (`claude-sonnet-5-5`)
  - Claude Opus 5.5 (`claude-opus-5-5`)

Runs all 6 challenges across all 3 Claude tiers (18 isolated runs total),
recording exact wall-clock seconds/minutes, token telemetry, and real API cost in USD.
"""

import argparse
import concurrent.futures
import json
import os
import shutil
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep04-escalera-claude")
BENCH_DIR = BASE_DIR / "benchmark"
LOGS_DIR = BENCH_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_JSON = BENCH_DIR / "benchmark_results_ep04.json"

LOCK = threading.Lock()

MODELS = {
    "haiku": {
        "cli_alias": "haiku",
        "folder": "claude-haiku-5.5",
        "display": "Claude Haiku 5.5",
    },
    "sonnet": {
        "cli_alias": "sonnet",
        "folder": "claude-sonnet-5.5",
        "display": "Claude Sonnet 5.5",
    },
    "opus": {
        "cli_alias": "opus",
        "folder": "claude-opus-5.5",
        "display": "Claude Opus 5.5",
    },
}

CHALLENGES = [
    {
        "id": "01-rover-suspension",
        "num": 1,
        "name": "Simulador de Monster Truck / Rover Planetario con Suspension de Resortes Amortiguados y Terreno Destructible",
        "prompt_body": """Actúa como un Ingeniero Senior de Simulación Vehicular y Física de Videojuegos. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Simulador Interactivo de Monster Truck / Rover Planetario con Suspensión de Resortes Amortiguados (Hooke's Law + Amortiguación Viscosa) y Terreno Procedural Destructible en un solo archivo.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML5, CSS y JavaScript puro en el mismo archivo) que funcione al primer intento al abrirlo en el navegador a 60 FPS, sin errores de consola y sin librerías de física externas (prohibido Matter.js, Box2D, Planck, Cannon, etc.).
2. PROHIBIDO cargar imágenes o recursos externos. Todo debe dibujarse proceduralmente en Canvas 2D / WebGL con estética cyberpunk de laboratorio de ingeniería.

REQUERIMIENTOS MATEMÁTICOS Y FUNCIONALES OBLIGATORIOS:
1. Chasis Rígido/Verlet y Suspensión Independiente con Ley de Hooke:
   - Modela un vehículo todoterreno (Monster Truck / Rover espacial de 4 o 6 ruedas) con cuerpo principal, jaula antivuelco y ruedas conectadas mediante puntales de suspensión elástica con amortiguadores reales (F = -k * x - c * v_rel).
   - Dibuja visualmente los resortes en zig-zag y los pistones hidráulicos comprimiéndose y estirándose en tiempo real, coloreados según el nivel de compresión mecánica, además de vectores de fuerza opcionales sobre cada rueda.
   - Implementa tracción rotacional en los neumáticos con fricción contra el suelo, derrape con partículas de polvo/chispas, propulsor de cohete trasero (Nitro Boost con llamas procedurales) y propulsores de giro en el aire para hacer acrobacias.
2. Terreno Procedural Infinito y Destructible:
   - Genera un terreno continuo de colinas, cráteres, rampas de salto, puentes colgantes de tablones físicos y obstáculos rocosos usando ruido fractal / splines.
   - Al hacer clic izquierdo en el terreno (o disparar el cañón de plasma del rover), provoca una explosión con onda de choque que excave un cráter real deformando la malla del suelo en vivo y lanzando escombros físicos.
3. Modo Piloto Automático Activo desde el Segundo 0.0 + Control Manual:
   - Al abrir el archivo debe iniciar con el "Modo Prueba de Laboratorio / Piloto Automático" ACTIVO por defecto para que el rover acelere, salte rampas y amortigüe impactos automáticamente de inmediato, cambiando a control manual en cuanto el usuario presione `WASD` / Flechas / Espacio.
4. HUD de Telemetría e Ingeniería en Caliente:
   - Sliders en vivo para ajustar rigidez del resorte (k), amortiguación (damping c), gravedad (Tierra, Luna, Marte, Júpiter), torque del motor, tamaño de rueda y botón de "Desplegar Obstáculos / Explosión".
   - Telemetría en tiempo real con FPS, velocidad en km/h, RPM, ángulo de inclinación del chasis, fuerza G máxima y gráfico en vivo de compresión de los amortiguadores.""",
    },
    {
        "id": "02-slime-feromonas",
        "num": 2,
        "name": "Laboratorio Biologico de Slime Mold (Physarum) y Colonia de 50,000 Agentes con Difusion de Feromonas",
        "prompt_body": """Actúa como un Investigador en Vida Artificial, Sistemas Complejos y Computación Gráfica de Alto Rendimiento. Tu objetivo es superar un benchmark de código "Zero-Shot" creando un Laboratorio Interactivo de Inteligencia de Enjambre y Slime Mold Biológico (Physarum Polycephalum) con 50,000 agentes autónomos y difusión química de feromonas a 60 FPS.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML5, CSS y JavaScript / WebGL / TypedArrays) que funcione al abrirlo directamente en el navegador sin errores de consola y sin dependencias externas.
2. Utiliza buffers tipados (`Float32Array` / `Uint32Array` sobre `ImageData` o Shaders WebGL ping-pong) para garantizar 60 FPS reales con decenas de miles de agentes simultáneos.

REQUERIMIENTOS MATEMÁTICOS Y BIOLÓGICOS OBLIGATORIOS:
1. Modelo Matemático de Physarum (Sensores Químicos + Actuadores):
   - Simula un mínimo de 35,000 a 60,000 agentes microbianos. Cada agente posee posición (x, y), ángulo de dirección (theta) y especie.
   - En cada paso de simulación, cada agente muestrea el mapa de feromonas con 3 sensores frontales (izquierdo a theta - sensorAngle, central a theta, derecho a theta + sensorAngle a una distancia sensorDist), gira hacia la mayor concentración química con ruido estocástico, avanza y deposita un rastro brillante de feromona.
2. Difusión Laplaciana y Evaporación en el Mapa Químico:
   - Aplica en cada frame un kernel de difusión 3x3 y un factor de decaimiento/evaporación (`decayRate`) sobre el campo de feromonas para que emerjan autopistas orgánicas, venas bioluminiscentes y redes de transporte idénticas a un organismo vivo.
3. Ecosistema Multiespecie, Nodos de Nutrientes y Barreras Interactivas:
   - Incluye al menos 3 especies bioluminiscentes (Cian, Magenta y Ámbar/Verde Neón) con matriz de atracción/repulsión cruzada para observar simbiosis o guerra territorial celular.
   - Coloca nodos de nutrientes pulsantes (que el moho conectará formando la red de camino mínimo estilo el experimento del metro de Tokio) y permite al usuario con el mouse:
     a) Sembrar ráfagas de nuevos agentes o fuentes de comida.
     b) Dibujar muros/barreras sólidas de placa de Petri.
     c) Lanzar pulsos de antibiótico/repelente químico.
4. HUD Científico y Presets Instantáneos:
   - Selector de 5 presets genéticos en un clic: "Red Ferroviaria de Tokio", "Guerra de 3 Colonias", "Mitosis Celular", "Red Neuronal Sináptica" y "Tormenta Quiral".
   - Sliders en vivo para `sensorAngle`, `sensorDistance`, `turnSpeed`, `moveSpeed`, `evaporationRate`, `diffusion` y contador real de FPS, agentes activos y entropía química.""",
    },
    {
        "id": "03-puente-estructural",
        "num": 3,
        "name": "Simulador de Ingenieria Civil y Colapso de Puentes con Analisis de Tension Finita y Paso de Trenes",
        "prompt_body": """Actúa como un Ingeniero Estructural Senior y Programador de Motores Físicos. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Simulador Interactivo de Ingeniería Civil y Colapso de Puentes (Structural Bridge Builder & Stress Analyzer) con cálculo de tensión axial, paso de trenes/convoyes pesados y fractura en cadena en tiempo real.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML5, CSS y JavaScript puro) que funcione al primer intento en el navegador a 60 FPS, sin librerías externas.
2. Todo el solver físico (integración de Verlet/RK4 con sub-stepping, rigidez por material, rotura de enlaces e hidrodinámica visual del río inferior) debe estar programado desde cero.

REQUERIMIENTOS DE INGENIERÍA Y FÍSICA OBLIGATORIOS:
1. Solver Estructural de Nodos, Vigas y Cables con Mapa de Calor de Estrés:
   - Implementa nodos de anclaje fijos en los acantilados y nodos libres conectados por distintos materiales de construcción: Plataforma de Carretera/Vía, Vigas de Acero (alta resistencia a compresión y tracción), Cables Tensores (solo tracción, alta flexibilidad) y Pilares de Concreto.
   - En cada sub-paso físico (mínimo 12 sub-iteraciones por frame), calcula la deformación porcentual (elongación y compresión) de cada elemento respecto a su límite elástico (`yieldLimit`).
   - Colorea cada viga en tiempo real con un Mapa de Calor de Ingeniería: Azul/Cian (compresión segura), Verde Esmeralda (reposo), Ámbar (70% de carga) y Rojo Incandescente vibrante (90-100% justo antes de la fractura), mostrando además el porcentaje numérico de estrés máximo.
2. Fractura Estructural en Cadena y Colapso al Cañón:
   - Si cualquier viga o cable supera el 100% de su capacidad máxima de carga, debe romperse instantáneamente emitiendo chispas y ondas de choque, redistribuyendo el peso a las vigas vecinas y desencadenando un colapso estructural progresivo realista donde la estructura y los vehículos caen al río inferior produciendo salpicaduras de agua.
3. Convoy de Prueba de Carga Activo desde el Inicio + Editor de Construcción:
   - El simulador debe abrirse con un puente colgante/truss de ingeniería preconstruido y lanzar automáticamente un Tren/Convoy Pesado de Prueba cruzando el puente desde el segundo 0.0 para que la física y el mapa de tensión se vean en acción de inmediato.
   - Incluye 4 Presets de Puentes ("Puente Truss Warren Estable", "Puente Colgante Al Límite — Colapso Dramático", "Arco de Acero Industrial", "Puente Sobrecargado — Prueba de Fallo") más un Modo Constructor completo (añadir/eliminar nodos y vigas con el mouse y control de presupuesto en USD).
4. HUD de Telemetría Civil:
   - Controles para peso y velocidad del tren/camión, gravedad, factor de resistencia de materiales, terremoto/viento lateral, botón de "Lanzar Convoy Pesado", "Cámara Lenta (Bullet Time 0.25x)" y telemetría de FPS, tensión pico (%), vigas intactas vs. fracturadas y costo estructural en dólares.""",
    },
    {
        "id": "04-sintetizador-acido-3d",
        "num": 4,
        "name": "Estudio Acustico Acido TB-303 + Caja de Ritmos TR-909 + Cupula Holografica Espectral 3D",
        "prompt_body": """Actúa como un Ingeniero de Procesamiento Digital de Señales de Audio (DSP) y Artista de Shaders 3D. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Estudio Musical Interactivo con Sintetizador de Bajo Ácido (estilo Roland TB-303), Caja de Ritmos (estilo TR-909) y una Cúpula/Túnel Holográfico Espectral 3D en tiempo real.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML5, CSS, WebAudio API y WebGL/Canvas 3D) sin cargar archivos de audio (.mp3/.wav) ni texturas externas. Todo sonido debe sintetizarse matemáticamente en tiempo real con WebAudio API.

REQUERIMIENTOS DE SÍNTESIS DSP Y VISUALIZACIÓN 3D OBLIGATORIOS:
1. Motor de Síntesis Ácida TB-303 + Batería Sintética TR-909:
   - Línea de Bajo Ácido (TB-303): Oscilador conmutable (Sawtooth / Square), filtro resonante pasa-bajos en cascada con envolvente dedicada (`Cutoff`, `Resonance`, `EnvMod`, `Decay`), soporte real para `Accent` (énfasis en volumen y barrido de filtro), `Slide/Glide` (portamento exponencial entre pasos consecutivos) y etapa de distorsión `Overdrive` mediante `WaveShaperNode` con curva tanh.
   - Caja de Ritmos (TR-909): 4 voces sintetizadas desde cero: Kick (senoidal con barrido rápido de frecuencia y punch), Snare (cuerpo tonal + ruido blanco filtrado), Closed/Open Hi-Hat (red de osciladores cuadrados metálicos pasa-altos) y Clap/Rimshot, más unidad de Delay Estéreo sincronizado al tempo (BPM).
2. Secuenciador por Pasos de 16 Pasos con 4 Patrones Preprogramados y Modo Visual Activo:
   - Matriz interactiva de 16 pasos donde cada paso de la línea ácida permita elegir Nota, Octava (`-1`, `0`, `+1`), `Accent`, `Slide` y `Gate`, junto con las 4 pistas de percusión.
   - Incluye 4 presets musicales listos ("Acid Warehouse 138 BPM", "Cyberpunk Phonk 125 BPM", "Hypnotic Modular 132 BPM", "Detroit Electro 140 BPM").
   - IMPORTANTE: Desde el segundo 0.0 (incluso antes de que el navegador desbloquee el contexto de audio con un clic), el secuenciador y el analizador espectral deben correr en modo visual activo (generando envolventes espectrales reales sincronizadas al patrón actual y activando el audio WebAudio instantáneamente al primer clic en cualquier parte o en el botón grande de PLAY/AUDIO).
3. Cúpula / Túnel Holográfico Espectral 3D + Osciloscopio:
   - En la mitad superior/central de la interfaz, renderiza a 60 FPS una escena 3D interactiva (geometría de terreno/cúpula geodésica/túnel de ondas FFT en perspectiva 3D con iluminación neón y partículas reactivas) cuyas alturas, colores y pulsos respondan en vivo a las bandas de frecuencia (`Sub-Bass`, `Acid Mid`, `Highs`) y a la forma de onda del sintetizador.
   - Incluye perillas rotatorias (knobs) arrastrables con el mouse para `Cutoff`, `Resonance`, `EnvMod`, `Decay`, `Distortion`, `Delay Mix` y `BPM`, más osciloscopio en vivo y medidor de FPS.""",
    },
    {
        "id": "05-pathtracer-bvh",
        "num": 5,
        "name": "Path Tracer Estocastico en Tiempo Real en WebGL2 con BVH, Refraccion Caustica y Denoiser Temporal",
        "prompt_body": """Actúa como un Investigador Principal en Gráficos por Computadora y Arquitecto de Motores de Ray Tracing en GPU. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Path Tracer Estocástico Monte Carlo en Tiempo Real ejecutándose íntegramente en WebGL2 (Fragment Shaders GLSL ES 3.0) con Refracción Cáustica, Lentes de Vidrio, Acumulación Temporal Progresiva y Denoiser en un solo archivo.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML5, CSS, JavaScript y Shaders GLSL ES 3.0 embebidos) que funcione a 60 FPS al abrirlo en el navegador sin errores de consola y sin librerías externas.
2. Todo el trazado de rayos, intersecciones geométricas, rebote estocástico de fotones y acumulación ping-pong en texturas flotantes (`RGBA32F` / `RGBA16F` con `EXT_color_buffer_float`) debe ejecutarse en la GPU.

REQUERIMIENTOS MATEMÁTICOS Y DE GPU OBLIGATORIOS:
1. Trazado de Caminos Monte Carlo (Multi-Bounce Path Tracing) y BVH/Primitivas Analíticas:
   - Implementa en GLSL ES 3.0 un integrador de transporte de luz con soporte de 2 a 10 rebotes por muestra, generador pseudoaleatorio de alta calidad por píxel/frame (PCG / Wang Hash) y muestreo por importancia del coseno (Cosine-Weighted Hemisphere Sampling) más Next-Event Estimation (Direct Light Sampling hacia las fuentes de área para converger rápido y generar cáusticas y sombras suaves).
   - Soporta intersección rápida contra múltiples primitivas organizadas en volúmenes delimitadores (AABB / BVH): Esferas de cristal y espejo, Cajas rotadas, Planos de Cornell Box y Anillos/Cilindros emisivos.
2. Materiales Físicamente Basados (PBR) y Dispersión Cromática:
   - Material Dieléctrico / Vidrio Realista: Ecuaciones de Fresnel (aproximación de Schlick), ley de Snell, reflexión interna total y dispersión cromática opcional (índice de refracción IOR dependiente del canal R/G/B para separar la luz en arcoíris sobre el suelo).
   - Material Metálico Microfacet con rugosidad (`roughness`) ajustable en vivo.
   - Material Difuso Lambertiano y Luces de Área Emisivas de alta intensidad.
3. Acumulación Temporal Ping-Pong + Filtro Denoiser Espacial:
   - Utiliza dos Framebuffers (Ping-Pong FBOs) para acumular muestras por píxel (`SPP`) progresivamente, eliminando el ruido Monte Carlo en pocos segundos y reiniciando el acumulador limpiamente cuando el usuario orbita la cámara o modifica un parámetro.
   - Añade un pase de post-procesado con Tone Mapping ACES Filmic, corrección Gamma y un filtro Denoiser bilateral/Á-Trous conmutable en vivo para comparar la imagen cruda vs. filtrada.
4. Escenas Interactivas, Cámara Orbital y HUD de GPU:
   - Incluye 3 escenas conmutables ("Cornell Box Cyberpunk con Esfera de Cristal y Espejo", "Laboratorio de Lentes Ópticos y Dispersión", "Anillo de Metales y Luces Volumétricas").
   - Controles en vivo para rebotes máximos (`Max Bounces`), rugosidad metálica, índice de refracción (`IOR`), apertura de lente (`Depth of Field / Bokeh`), distancia focal, rotación automática suave y telemetría con FPS, SPP acumulados, rayos por segundo (MRays/s) y resolución.""",
    },
    {
        "id": "06-consola-retro-cpu",
        "num": 6,
        "name": "Consola Retro Virtual + Ensamblador en Vivo + Debugger Hexadecimal de CPU y 3 Juegos ROM en 1 Archivo",
        "prompt_body": """Actúa como un Ingeniero de Arquitectura de Computadoras, Creador de Emuladores y Desarrollador de Sistemas Embebidos. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo una Consola Retro Virtual Completa (Arquitectura CPU de 8-Bits / CHIP-8 Extendida) con Ciclo Fetch-Decode-Execute, Inspector Hexadecimal de Memoria RAM, Desensamblador Paso a Paso, Ensamblador Integrado y 3 Juegos/Demos ROM Jugables compilados en memoria dentro de un único archivo `index.html`.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML5, CSS y JavaScript puro) que funcione al primer intento en el navegador sin errores de consola y sin archivos externos.
2. PROHIBIDO hacer un juego en JS normal disfrazado de emulador: debes programar una Máquina Virtual real con un arreglo de memoria RAM (`Uint8Array(4096)`), registros de CPU (`Uint8Array(16)`), contador de programa `PC`, puntero de pila `SP`, pila de llamadas, decodificador de opcodes binarios de 16 bits y compilador de código ensamblador a bytecode en memoria.

REQUERIMIENTOS DE ARQUITECTURA DE SISTEMAS OBLIGATORIOS:
1. Máquina Virtual y Ciclo Fetch-Decode-Execute Real:
   - Implementa una CPU completa compatible con el set de instrucciones CHIP-8 (los 35 opcodes estándar: `00E0` CLS, `00EE` RET, `1nnn` JP, `2nnn` CALL, `3xkk`/`4xkk` SE/SNE, `6xkk` LD, `7xkk` ADD, `8xy0..8xyE` ALU bit a bit y aritmética con bandera de acarreo `VF`, `Annn` LD I, `Cxkk` RND, `Dxyn` DRW de sprites con detección de colisión en `VF`, `Ex9E`/`ExA1` teclado, `Fx07..Fx65` temporizadores, BCD y memoria).
   - Pantalla CRT virtual con post-procesado de fósforo brillante, curvatura opcional, scanlines y beeper de audio WebAudio activado por el Sound Timer (`ST`) a 60Hz.
2. Debugger de Ingeniería e Inspector de Hardware en Tiempo Real:
   - Panel de Registros de CPU en vivo (`PC`, `I`, `SP`, `DT`, `ST` y los 16 registros `V0`..`VF` con barras visuales e indicadores en hexadecimal y decimal).
   - Desensamblador en Tiempo Real: Muestra una ventana deslizante con las instrucciones alrededor del `PC` actual traducidas de su opcode hexadecimal (ej. `0x0204: D125 -> DRW V1, V2, 5`), iluminando la línea exacta que está ejecutando la CPU.
   - Visor Hexadecimal de Memoria RAM (Hex Dump de los 4 KB de RAM coloreando la zona de fuentes `0x000-0x1FF`, el programa ROM `0x200+` y la dirección apuntada por `PC` e `I`).
   - Controles de Depuración: `Run / Pause`, `Step Into (1 Instrucción)`, `Step Frame (1/60s)`, `Reset ROM` y slider de frecuencia de reloj (`Clock Speed`: de 10 Hz para ver la CPU pensar instrucción por instrucción hasta 1,200 Hz).
3. Ensamblador en Vivo + 3 ROMs Precompiladas que Arranquen desde el Segundo 0.0:
   - Incluye un Compilador Ensamblador (Assembler) en JavaScript que tome código fuente ASM con etiquetas (labels) y mnemónicos, lo ensamble a bytecode y lo cargue en la RAM a partir de `0x200`.
   - Incluye al menos 3 ROMs completas escritas en ASM/bytecode listas para cargar con un clic (y que la ROM #1 arranque corriendo automáticamente al abrir el HTML con modo demo/attract o jugable de inmediato):
     1) "CYBER PONG / BREAKOUT" (con rebote de pelota, paletas y marcador en sprites BCD).
     2) "STAR INVADERS / LASER DEFENSE" (nave espacial disparando a oleadas alienígenas).
     3) "MATRIX PLASMA / MAZE GENERATOR" (demoscene gráfica y generador de laberintos de alta velocidad).
   - Incluye un editor de código ASM en la interfaz donde el usuario pueda modificar las instrucciones de cualquiera de las ROMs y pulsar "ASSEMBLE & FLASH TO RAM" para ver sus cambios correr en la CPU.""",
    },
]


def load_or_init_results():
    if RESULTS_JSON.exists():
        try:
            return json.loads(RESULTS_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {
        "episode": "EP04 — La Escalera Completa de Claude 5.5 (Haiku 5.5 vs. Sonnet 5.5 vs. Opus 5.5)",
        "started_at": datetime.now().isoformat(),
        "models": {
            "haiku": "Claude Haiku 5.5 (claude CLI --safe-mode --model haiku --effort high)",
            "sonnet": "Claude Sonnet 5.5 (claude CLI --safe-mode --model sonnet --effort high)",
            "opus": "Claude Opus 5.5 (claude CLI --safe-mode --model opus --effort high)",
        },
        "runs": {},
    }


def save_result(cid: str, model_key: str, payload: dict):
    with LOCK:
        data = load_or_init_results()
        if cid not in data["runs"]:
            data["runs"][cid] = {}
        data["runs"][cid][model_key] = payload
        RESULTS_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def prepare_workspace(model_key: str, cid: str) -> Path:
    folder_name = MODELS[model_key]["folder"]
    target_dir = BASE_DIR / folder_name / cid
    if target_dir.exists():
        shutil.rmtree(target_dir, ignore_errors=True)
    target_dir.mkdir(parents=True, exist_ok=True)
    return target_dir


def run_single(model_key: str, challenge: dict):
    cid = challenge["id"]
    m_info = MODELS[model_key]
    target_dir = prepare_workspace(model_key, cid)
    target_file = target_dir / "index.html"

    full_prompt = (
        f"{challenge['prompt_body']}\n\n"
        f"INSTRUCCIÓN DE ARCHIVO OBLIGATORIA: Escribe el código HTML completo directamente en el archivo `{target_file}` usando tu herramienta Write. No ejecutes servidores ni pidas confirmación."
    )

    cmd = [
        "claude",
        "--safe-mode",
        "--dangerously-skip-permissions",
        "--tools",
        "Write,Edit,Read",
        "--model",
        m_info["cli_alias"],
        "--effort",
        "high",
        "--output-format",
        "json",
        "-p",
        full_prompt,
    ]

    log_path = LOGS_DIR / f"{cid}_{model_key}.log"
    print(f"[{datetime.now().strftime('%H:%M:%S')}] >>> STARTING {m_info['display']} on {cid} ...", flush=True)
    t0 = time.monotonic()
    start_iso = datetime.now().isoformat()

    with open(log_path, "w", encoding="utf-8") as lf:
        proc = subprocess.run(
            cmd,
            cwd=str(target_dir),
            stdout=lf,
            stderr=subprocess.STDOUT,
            text=True,
        )

    elapsed_sec = round(time.monotonic() - t0, 2)
    elapsed_min = round(elapsed_sec / 60.0, 2)

    raw_out = log_path.read_text(encoding="utf-8", errors="replace").strip()
    j_obj = {}
    for line in reversed(raw_out.splitlines()):
        line_s = line.strip()
        if line_s.startswith("{") and line_s.endswith("}"):
            try:
                j_obj = json.loads(line_s)
                break
            except Exception:
                pass

    extracted_from_stdout = False
    if not target_file.exists() or target_file.stat().st_size < 500:
        res_text = str(j_obj.get("result", "")) + "\n" + raw_out
        if "<!DOCTYPE html>" in res_text or "<html" in res_text:
            start_idx = res_text.find("<!DOCTYPE html>")
            if start_idx == -1:
                start_idx = res_text.find("<html")
            end_idx = res_text.rfind("</html>")
            if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                html_code = res_text[start_idx : end_idx + 7]
                target_file.write_text(html_code, encoding="utf-8")
                extracted_from_stdout = True

    exists = target_file.exists()
    size_bytes = target_file.stat().st_size if exists else 0
    lines_count = (
        len(target_file.read_text(encoding="utf-8", errors="replace").splitlines())
        if exists
        else 0
    )

    usage = j_obj.get("usage", {})
    model_usage = j_obj.get("modelUsage", {})
    exact_model_ids = list(model_usage.keys())

    in_tok = usage.get("input_tokens", 0)
    cache_create_tok = usage.get("cache_creation_input_tokens", 0)
    cache_read_tok = usage.get("cache_read_input_tokens", 0)
    out_tok = usage.get("output_tokens", 0)
    thinking_tok = usage.get("output_tokens_details", {}).get("thinking_tokens", 0)
    cost_usd = round(float(j_obj.get("total_cost_usd", 0.0)), 4)

    token_telemetry = {
        "exact_model_ids": exact_model_ids,
        "agent_steps": j_obj.get("num_turns", 1),
        "duration_api_ms": j_obj.get("duration_api_ms", 0),
        "input_tokens": in_tok,
        "cache_creation_input_tokens": cache_create_tok,
        "cache_read_input_tokens": cache_read_tok,
        "output_tokens": out_tok,
        "thinking_tokens": thinking_tok,
        "total_tokens": in_tok + cache_create_tok + cache_read_tok + out_tok,
        "cost_usd": cost_usd,
        "model_usage_breakdown": model_usage,
    }

    payload = {
        "model_key": model_key,
        "model_display": m_info["display"],
        "challenge_id": cid,
        "challenge_num": challenge["num"],
        "challenge_name": challenge["name"],
        "started_at": start_iso,
        "finished_at": datetime.now().isoformat(),
        "exit_code": proc.returncode,
        "is_error": j_obj.get("is_error", False),
        "elapsed_seconds": elapsed_sec,
        "elapsed_minutes": elapsed_min,
        "file_created": exists,
        "extracted_from_stdout": extracted_from_stdout,
        "file_path": str(target_file),
        "file_size_bytes": size_bytes,
        "lines_of_code": lines_count,
        "token_telemetry": token_telemetry,
    }

    save_result(cid, model_key, payload)
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] <<< FINISHED {m_info['display']} on {cid}: "
        f"{elapsed_sec}s ({elapsed_min} min) | exists={exists} | {lines_count} lines | "
        f"cost=${cost_usd:.4f} | models={exact_model_ids}",
        flush=True,
    )
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", nargs="+", default=["haiku", "sonnet", "opus"])
    parser.add_argument("--challenges", nargs="+", default=[c["id"] for c in CHALLENGES])
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()

    tasks = []
    for ch in CHALLENGES:
        if ch["id"] not in args.challenges:
            continue
        for mk in args.models:
            if mk in MODELS:
                tasks.append((mk, ch))

    print(f"=== Launching {len(tasks)} EP04 Benchmark Runs (workers={args.workers}) ===", flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(run_single, mk, ch) for mk, ch in tasks]
        for fut in concurrent.futures.as_completed(futures):
            try:
                fut.result()
            except Exception as exc:
                print(f"[ERROR] Run raised exception: {exc}", flush=True)

    print("=== ALL REQUESTED EP04 RUNS COMPLETED ===", flush=True)


if __name__ == "__main__":
    main()
