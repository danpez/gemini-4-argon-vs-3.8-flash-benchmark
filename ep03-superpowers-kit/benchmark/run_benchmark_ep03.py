#!/usr/bin/env python3
"""
Automated Zero-Shot Benchmark Runner for Mixiuh Labs Episode 03:
Gemini 4 Argon (High) [via agy CLI] — SIN SUPERPOWERS vs. CON SUPERPOWERS KIT

Runs all 6 challenges in isolated directories for both modes ("raw" vs "superkit"),
records exact wall-clock seconds/minutes, extracts exact token telemetry from
antigravity-cli transcripts, and verifies the generated index.html applications.
"""

import glob
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep03-superpowers-kit")
KIT_SRC_DIR = BASE_DIR / "regalo-superpowers-kit"
BENCH_DIR = BASE_DIR / "benchmark"
LOGS_DIR = BENCH_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_JSON = BENCH_DIR / "benchmark_results_ep03.json"

CHALLENGES = [
    {
        "id": "01-galaxia-nbody",
        "num": 1,
        "name": "Colision de Galaxias N-Body 3D y Agujero Negro Relativista (Three.js + Shaders GLSL)",
        "prompt_body": """Actúa como un Astrofísico Computacional y Programador Gráfico Senior de WebGL/Three.js. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Simulador Interactivo 3D de Colisión de Galaxias N-Body y Agujero Negro Supermasivo con Lente Gravitacional en Tiempo Real, con estética de observatorio espacial cyberpunk/científico.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS, JavaScript y Shaders GLSL en el mismo archivo) que funcione al primer intento al abrirlo en el navegador, sin errores de consola. Puedes importar únicamente `three` y `OrbitControls` mediante `<script type="importmap">` desde un CDN estándar (unpkg o cdnjs).
2. PROHIBIDO cargar imágenes, texturas o modelos externos. Todo el renderizado de estrellas, nebulosas volumétricas, disco de acreción relativista, distorsión gravitacional y telemetría debe generarse mediante código y matemáticas.
3. PROHIBIDO usar emojis Unicode en la interfaz o en el código; usa iconos vectoriales SVG o símbolos geométricos limpios.

REQUERIMIENTOS MATEMÁTICOS, FÍSICOS Y VISUALES OBLIGATORIOS:
1. Simulación Gravitacional N-Body 3D de Alto Rendimiento (Mínimo 35,000 a 60,000 Estrellas Activas):
   - Simula la interacción gravitacional tridimensional entre dos galaxias espirales en colisión (Vía Láctea vs. Andrómeda) orbitando núcleos supermasivos en 3D.
   - Colorea cada estrella dinámicamente según su velocidad radial/orbital y temperatura (desplazamiento Doppler relativista: azul/cian intenso al acercarse o en el núcleo caliente, ámbar/rojo al alejarse en las colas de marea gravitacional).
2. Agujero Negro Supermasivo y Shaders GLSL de Disco de Acreción + Lente Gravitacional:
   - En el centro del núcleo principal, renderiza el Horizonte de Sucesos rodeado por un Disco de Acreción Relativista animado con shaders GLSL (turbulencia de plasma, brillo asimétrico por beaming relativista y jets polares de energía).
   - Incluye un efecto de Lente Gravitacional (Anillo de Einstein) y visualización opcional de la malla de partición espacial 3D / pozos de potencial gravitatorio.
3. Interacción 3D en Vivo y Presets Astrofísicos:
   - Cámara orbital suave (`OrbitControls`) + clic/botón para inyectar un "Agujero Negro Errante", disparar una "Onda de Choque de Supernova" o fusionar los núcleos.
   - Selector de Presets en vivo: 1) Colisión Andrómeda-Vía Láctea, 2) Cuásar Binario Relativista, 3) Anillo de Einstein & Lente Puro, 4) Colapso de Cúmulo Globular.
   - Selector de Modos Visuales: 1) Espectro Doppler + Bloom Relativista, 2) Mapa Térmico de Velocidad Orbital, 3) Visualización de Partición Espacial Octree 3D, 4) Campo de Vectores Gravitacionales.
4. HUD de Observatorio y Telemetría en Tiempo Real:
   - Paneles flotantes translúcidos (glassmorphism oscuro) con sliders interactivos para Masa del Agujero Negro, Constante Gravitacional (G), Paso de Tiempo (dt / Cámara Lenta) e Intensidad de Lente Gravitacional.
   - Telemetría en vivo: FPS, tiempo de frame (ms), estrellas activas, nodos espaciales, energía del sistema y radio de Schwarzschild.""",
    },
    {
        "id": "02-terminal-trading",
        "num": 2,
        "name": "Terminal Cuantitativa HFT 3D: Superficie de Liquidez WebGL, Heatmap DOM y Motor de Flash-Crash",
        "prompt_body": """Actúa como un Arquitecto de Sistemas Financieros de Alta Frecuencia (HFT) e Ingeniero de Visualización WebGL/Canvas. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo una Terminal Institucional Interactiva de Trading Cuantitativo y Microestructura de Mercado en Tiempo Real (con Superficie 3D de Liquidez/Volatilidad, Mapa de Calor de Libro de Órdenes DOM, Gráfico de Velas Multi-Indicador y Simulador de Flash-Crash) en un único archivo HTML.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS y JavaScript en el mismo archivo) que funcione al abrirlo directamente en el navegador a 60–120 FPS sin errores de consola. Puedes usar Three.js vía `<script type="importmap">` o WebGL/Canvas 2D de alta densidad.
2. PROHIBIDO cargar imágenes o datos externos. Todo el motor de emparejamiento de órdenes (Order Matching Engine Limit/Market), los bots algorítmicos creadores de mercado (Market Makers) y las visualizaciones 3D/2D deben generarse en vivo con matemáticas estocásticas (movimiento browniano geométrico con saltos de Poisson y volatilidad estocástica Heston).
3. PROHIBIDO usar emojis Unicode; diseña toda la iconografía con SVG vectorial y tipografía monoespaciada financiera.

REQUERIMIENTOS TÉCNICOS Y VISUALES OBLIGATORIOS:
1. Motor de Emparejamiento de Órdenes en Tiempo Real (Matching Engine + HFT Bots):
   - Simula un flujo continuo de miles de órdenes límite, órdenes de mercado y cancelaciones por segundo con libros de órdenes reales (Bids en verde esmeralda/cian y Asks en carmesí/ámbar).
   - Permite alternar entre activos (`BTC-PERP`, `NVDA-AI`, `ETH-PERP`, `SOL-HFT`) y ejecutar órdenes manuales (Long / Short Market & Limit con apalancamiento configurable) viendo el impacto inmediato en el precio y en el PnL de la cartera.
2. Cuatro Visualizaciones Sincronizadas de Alto Impacto a 60–120 FPS:
   - a) **Gráfico Principal de Velas Japonesas + Liquidez Heatmap**: Velas en tiempo real con Bandas de Bollinger, VWAP, EMAs, perfil de volumen lateral (Volume Profile) y ráfagas de partículas brillantes en cada liquidación masiva.
   - b) **Superficie 3D Interactiva de Volatilidad Implícita y Profundidad de Mercado (3D Orderbook / Volatility Surface)**: Malla tridimensional rotatoria e interactiva que muestre en vivo la tensión del libro de órdenes y la curvatura de volatilidad.
   - c) **Escalera DOM (Depth of Market) y Cinta de Transacciones (Time & Sales)**: Barras horizontales de alta velocidad y cinta de ejecuciones institucionales (Whale Alerts).
   - d) **Osciloscopio de Microestructura / Latencia y Flujo de Toxicidad (VPIN / Order Flow Imbalance)**.
3. Simuladores de Eventos Extremos de Mercado (Botones de Estrés en Vivo):
   - Botones interactivos para detonar en vivo: `Disparar Flash Crash (-25%)`, `Inyectar Ballena ($50M Buy Wall)`, `Short Squeeze Algorítmico`, `Cascada de Liquidaciones` y `Calmar Mercado`.
4. HUD de Telemetría Cuantitativa:
   - Indicadores en tiempo real de FPS, órdenes procesadas/seg, latencia del motor en microsegundos, Spread Bid-Ask, Delta de Volumen Acumulado (CVD) y estado de posición abierta (PnL no realizado, margen y precio de liquidación).""",
    },
    {
        "id": "03-arcade-boss-rush",
        "num": 3,
        "name": "Cyberpunk Bullet-Hell Boss Rush con Shaders Neon, Fisica de Particulas y Audio Sintetizado WebAudio",
        "prompt_body": """Actúa como un Director Técnico de Videojuegos Arcade Bullet-Hell y Programador de DSP WebAudio. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Videojuego Completo "Cyberpunk Boss Rush" (`CYBER//CORE: OVERLORD`) con Cortinas de Proyectiles Matemáticas, Múltiples Fases de Jefe Biomecánico, Cámara Lenta (Bullet-Time), Partículas con Colisión Espacial y Banda Sonora/SFX Sintetizados en Tiempo Real con WebAudio en un único archivo HTML.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS y JavaScript puro con Canvas 2D / WebGL y WebAudio API nativa) que funcione al primer intento sin errores de consola.
2. PROHIBIDO cargar imágenes, sprites o archivos de audio externos. Toda la geometría cibernética del jefe, los escudos hexagonales, los láseres de plasma, las explosiones de partículas y la música synthwave/industrial deben generarse por código en tiempo real.
3. PROHIBIDO usar emojis Unicode; usa geometría vectorial y HUD estilo cabina de combate.

REQUERIMIENTOS DE JUGABILIDAD, FÍSICA Y AUDIO OBLIGATORIOS:
1. Jefe Biomecánico Multi-Fase con Geometría Articulada y Patrones Bullet-Hell:
   - Diseña un Jefe colosal en el centro/parte superior de la arena con núcleo giratorio, anillos de blindaje destructibles, torretas satelitales y 3 fases de combate distintas (con cambio visual dramático y onda expansiva al pasar de fase):
     - **Fase 1 (Protocolo Espiral Cuántica)**: Cortinas hipnóticas de proyectiles en rosas polares, espirales de Fermat y ondas senoidales dobles.
     - **Fase 2 (Cañones de Plasma y Barrido Láser)**: Rayos láser gigantes con pre-aviso holográfico (telegraphing), drones buscadores y anillos de pulso electromagnético.
     - **Fase 3 (Singularidad Overdrive)**: El núcleo se abre liberando patrones combinados de alta densidad (1,500+ proyectiles activos simultáneos a 60–120 FPS).
2. Nave del Jugador, Modo Piloto Automático IA y Mecánicas "Witch-Time":
   - La nave puede controlarse con Mouse o Teclado (WASD / Flechas) + Disparo concentrado/disperso, Dash con invulnerabilidad (deja estela de post-imagen neón) y Bomba EMP que limpia proyectiles convirtiéndolos en cristales de puntaje.
   - OBLIGATORIO: Incluye un conmutador activo por defecto de **"Piloto Automático IA (Modo Demo / Espectáculo)"** que esquive proyectiles calculando vectores de peligro, use el Dash y dispare al jefe automáticamente, permitiendo tomar control manual en cualquier momento.
   - Botón/tecla para activar **"Bullet-Time (Dilatación Temporal)"** con distorsión cromática y rastro de velocidad.
3. Motor de Audio Sintetizado en Vivo (WebAudio API):
   - Secuenciador synthwave/darksynth procedural (bajo ácido, batería electrónica y arpegios en tensión que aceleran según la fase del jefe) + efectos de sonido sintetizados para disparos, impactos, láseres, alertas de fase y explosiones (con botón de Mute).
4. HUD Táctico y Modo Debug de Colisiones:
   - Barra de vida segmentada del Jefe por fases, multiplicador de combo, escudo de la nave, botones directos para saltar a `Fase 1`, `Fase 2`, `Fase 3`, `Detonar EMP`, `Activar Bullet-Time` y `Modo Debug Físico` (que muestre en pantalla la rejilla espacial, hitboxes exactos y vectores de velocidad de las balas).""",
    },
    {
        "id": "04-red-zero-trust",
        "num": 4,
        "name": "Centro de Comando Ciberdefensa 3D: Globo Terrestre WebGL de Ataques DDoS y Firewall Zero-Trust (Three.js)",
        "prompt_body": """Actúa como un Arquitecto Principal de Ciberseguridad Zero-Trust y Desarrollador de Visualización 3D en Three.js/WebGL. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Centro de Comando Global 3D de Ciberdefensa e Inspección de Amenazas en Tiempo Real (`AEGIS // ZERO-TRUST SOC 3D`) en un único archivo HTML.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido. Usa `<script type="importmap">` apuntando a un CDN confiable (unpkg o cdnjs) para importar `three` y `OrbitControls`.
2. PROHIBIDO cargar imágenes o mapas externos. El globo terráqueo cibernético, la grilla geodésica continental, los centros de datos, los arcos balísticos 3D de paquetes de red y las ondas de choque deben generarse 100% mediante geometría procedural y shaders en Three.js.
3. PROHIBIDO usar emojis Unicode; usa iconografía vectorial técnica de centro de operaciones de seguridad (SOC).

REQUERIMIENTOS VISUALES, 3D Y DE INGENIERÍA OBLIGATORIOS:
1. Globo Terrestre 3D Interactivo + Vista de Topología de Malla Zero-Trust:
   - Renderiza en Three.js un Globo Planetario Holográfico de alta precisión (con atmósfera Fresnel luminosa, retícula latitud/longitud, masas continentales procedurales y anillos orbitales de satélites/nodos).
   - Sitúa al menos 18 nodos globales estratégicos (`US-EAST Virginia`, `EU-CENTRAL Frankfurt`, `AP-TOKYO`, `MX-QUERETARO`, `SG-SINGAPORE`, `BR-SAO PAULO`, `CH-ZURICH`, `UK-LONDON`, `AU-SYDNEY`, etc.) con torres de estado luminosas.
   - Permite alternar con transición suave entre **1) Vista Globo Planetario 3D** y **2) Vista Topología de Clúster Zero-Trust 3D (Grafo Espacial de Microsegmentación)**.
2. Simulación Masiva de Tráfico y Ciberataques en Tiempo Real (Arcos Bézier 3D + Partículas):
   - Cientos de pulsos de datos viajando en tiempo real por curvas Bézier elevadas sobre el globo:
     - Tráfico legítimo cifrado mTLS (cian / verde esmeralda).
     - Ataques de Botnet DDoS Volumétricos (arcos carmesí/naranja de alta densidad que generan ondas de choque sísmicas al impactar el nodo destino).
     - Intentos de intrusión L7 (`SQL Injection`, `XSS Payload`, `JWT Forgery`, `RCE Exploit`) en color ámbar/magenta.
3. Motor de Defensa Activa Zero-Trust y Controles de Respuesta a Incidentes:
   - Al hacer clic sobre cualquier nodo 3D en el globo (Raycasting), abre su telemetría detallada (carga de CPU, ancho de banda en Gbps, certificados mTLS, reglas WAF activas) y permite **"Aislar Nodo (Quarantine)"** o **"Re-enrutar Tráfico (Anycast Scrubbing)"**.
   - Panel de mando con botones de acción inmediata: `Simular Ataque DDoS Masivo (850 Gbps)`, `Inyectar Exploit SQLi / Zero-Day`, `Activar Escudo IA Zero-Trust (Auto-Mitigación)`, `Rotar Llaves mTLS Globales` y `Cambiar Vista (Globo 3D / Grafo 3D)`.
4. HUD de Telemetría SOC e Inspector de Paquetes en Vivo:
   - Gráficos en tiempo real de Tráfico Limpio vs. Tráfico Mitigado (Gbps), matriz de amenazas bloqueadas por vector (DDoS, SQLi, XSS, Brute Force), registro de auditoría de paquetes inspeccionados con firma criptográfica y contador de FPS/Draw Calls.""",
    },
    {
        "id": "05-motor-nodos-ia",
        "num": 5,
        "name": "Estudio Visual de Nodos Reactivos para Shaders GLSL 3D y Sintesis Audio-Reactiva (Node Graph Studio)",
        "prompt_body": """Actúa como un Ingeniero Principal de Herramientas Creativas (estilo TouchDesigner / Blender Shader Nodes / Unreal Blueprints) y Programador de Shaders GLSL. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Estudio Visual Interactivo de Programación por Nodos en Tiempo Real (`NEXUS // NODE SHADER & DSP STUDIO`) donde conectar y ajustar nodos modulares modifica en vivo un Viewport WebGL de Raymarching 3D y un Sintetizador/Analizador de Audio en un único archivo HTML.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS, JavaScript, Canvas 2D y WebGL Shaders GLSL en el mismo archivo) que funcione al primer intento a 60–120 FPS sin errores de consola.
2. PROHIBIDO cargar librerías externas de grafos o imágenes externas. Todo el motor de grafo dirigido acíclico (DAG), el lienzo infinito con zoom/paneo, los cables Bézier animados con pulsos de señal y el compilador/evaluador hacia el shader WebGL deben estar programados desde cero.
3. PROHIBIDO usar emojis Unicode; usa iconos vectoriales limpios.

REQUERIMIENTOS ARQUITECTÓNICOS Y VISUALES OBLIGATORIOS:
1. Lienzo Interactivo de Nodos con Cables Bézier Animados y Previsualización en Cada Nodo:
   - Nodos arrastrables con encabezados codificados por categoría, puertos de entrada/salida tipados (`Float`, `Vec3/Color`, `SDF Geometry`, `Audio FFT`), sliders/knobs interactivos dentro de cada nodo y un **mini-canvas en vivo dentro de cada nodo** que muestre la onda, textura o señal que ese nodo está generando en tiempo real.
   - Cables curvos cúbicos (Bézier) con brillo neón por los que viajan partículas/pulsos luminosos a la velocidad del flujo de datos; permite arrastrar desde un puerto para crear nuevas conexiones, desconectar cables y detectar ciclos inválidos en el DAG sin colgar la aplicación.
2. Viewport Principal WebGL Raymarching 3D en Tiempo Real (Acoplado al Grafo):
   - Un panel destacado (o vista dividida/flotante ampliable) que renderice a 60–120 FPS un Shader GLSL de Raymarching 3D (fractales Mandelbulb/SDF, túneles cuánticos, metamateriales iridiscentes con iluminación especular, plegamiento espacial y aberración cromática) cuyos uniformes y ecuaciones responden instantáneamente a los nodos conectados en el grafo.
3. Categorías de Nodos y Presets Espectaculares de 1 Clic:
   - Incluye nodos de: `Generador LFO / Tiempo`, `Analizador Audio FFT / Sintetizador`, `Ruido Fractal Simplex 4D`, `Geometría SDF (Toroide / Octaedro / Fractal)`, `Operador Booleano / Twist / Repetición Infinita`, `Paleta Espectral Coseno` y `Master Output WebGL + Post-Bloom`.
   - Botones de Presets que reconstruyen y animan el grafo al instante: `1. Agujero de Gusano Raymarching`, `2. Fractal Ciber-Cristal 4D`, `3. Pulso Audio-Reactivo Synth`, `Auto-Ordenar Grafo (Layout)` y `Inyectar Mutación Procedural`.
4. Telemetría del Motor DAG y GPU:
   - Barra superior e inspector con orden de evaluación topológica en vivo, tiempo de evaluación del grafo (ms), FPS del shader WebGL, número de nodos/cables activos y consola de estado del compilador GLSL.""",
    },
    {
        "id": "06-mixiuh-os-desktop",
        "num": 6,
        "name": "Sistema Operativo Web Completo 'Mixiuh OS' con Gestor de Ventanas, Apps 3D/Audio en Vivo y Dock Fisico",
        "prompt_body": """Actúa como un Arquitecto Principal de Sistemas Operativos Web y Diseñador de Interfaces Futuristas. Tu objetivo es superar un benchmark de código "Zero-Shot" construyendo un Entorno de Escritorio y Sistema Operativo Web Completo e Interactivo (`MIXIUH OS v4.0 // CYBER-KERNEL DESKTOP`) que ejecute simultáneamente múltiples aplicaciones reales (Laboratorio 3D WebGL, Terminal de Comandos Interactiva, Estudio Sintetizador Polifónico WebAudio y Monitor de Kernel/Procesos) dentro de un Gestor de Ventanas Flotantes con Física en un único archivo HTML.

REGLAS ESTRICTAS DEL BENCHMARK:
1. Escribe y guarda un ÚNICO archivo `index.html` 100% autocontenido (HTML, CSS y JavaScript en el mismo archivo) que funcione al primer intento a 60–120 FPS sin errores de consola.
2. PROHIBIDO cargar imágenes o recursos externos. El fondo de pantalla animado (shader/canvas procedural), los iconos vectoriales del Dock, las ventanas glassmorphic y las aplicaciones internas deben generarse 100% por código.
3. PROHIBIDO usar emojis Unicode; diseña todos los iconos del sistema, botones de ventana y barra de estado con SVG vectorial de alta precisión.

REQUERIMIENTOS DEL SISTEMA OPERATIVO Y APLICACIONES EN VIVO:
1. Gestor de Ventanas Avanzado (Window Manager) + Barra Superior + Dock con Magnificación Física:
   - Múltiples ventanas flotantes con estética glassmorphism oscuro (`backdrop-filter: blur`), sombras profundas, bordes reactivos, gestión real de foco (`z-index`), arrastrar desde la barra de título, redimensionar desde bordes/esquinas, minimizar al Dock, maximizar/restaurar y modo **"Mosaico Automático (Tile All Windows)"** o **"Exposé / Vista General"**.
   - Fondo de escritorio dinámico con shader/malla procedural interactiva al cursor y selector de temas en vivo (`Cyberpunk Cyan`, `Quantum Violet`, `Emerald Matrix`, `Solar Amber`).
   - Dock inferior con iconos vectoriales que se magnifican suavemente con física de resortes al pasar el cursor e indicadores luminosos de aplicaciones abiertas.
2. Cuatro Aplicaciones Reales Ejecutándose en Paralelo desde el Arranque (Todas Visibles y Activas):
   - **App 1 — HoloCore 3D Shader Studio**: Ventana con un lienzo WebGL / 3D interactivo que renderiza un núcleo hiper-geométrico 3D rotatorio con controles propios en la ventana (cambiar geometría: Toroide Cuántico / Esfera Geodésica / Hipercubo, velocidad, modo wireframe/plasma y explosión de partículas).
   - **App 2 — Mixiuh Kernel Terminal (`zsh // mixiuh-os`)**: Terminal interactiva real con historial y botones de comandos rápidos de 1 clic (`neofetch`, `benchmark`, `top`, `matrix`, `netstat`, `clear`) que imprimen arte ASCII vectorial, métricas del sistema y diagnósticos animados en tiempo real.
   - **App 3 — PulseWave FM Synth & Spectrum Analyzer**: Estación musical compacta con teclado tocable, secuenciador automático con botón Play/Stop, perillas de filtro/resonancia y analizador de espectro FFT + osciloscopio animado a 60 FPS usando WebAudio API.
   - **App 4 — Kernel Telemetry & Task Manager**: Monitor de recursos del sistema en tiempo real con gráficos circulares y sparklines de CPU, GPU Frame Time, Memoria Heap, FPS globales y tabla de procesos activos con botón para impulsar prioridad o reiniciar procesos.
3. Controles Rápidos de Demostración en la Barra Superior:
   - Botones de acceso directo en la barra superior del escritorio: `Organizar en Mosaico (4 Apps)`, `Cascada Dinámica`, `Cambiar Tema Visual`, `Ejecutar Stress Test Global` y reloj/telemetría de FPS en vivo.""",
    },
]


def load_results():
    if RESULTS_JSON.exists():
        try:
            return json.loads(RESULTS_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"started_at": datetime.now().isoformat(), "runs": {}}


def save_results(data):
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


def prepare_workspace(mode: str, cid: str) -> Path:
    if mode == "raw":
        target_dir = BASE_DIR / "ia-sin-kit" / cid
        target_dir.mkdir(parents=True, exist_ok=True)
        for fname in ["CLAUDE.md", "GEMINI.md", "MEMORY.md", ".cursorrules"]:
            p = target_dir / fname
            if p.exists():
                p.unlink()
        for sdir in ["skills", ".gemini", ".claude"]:
            sp = target_dir / sdir
            if sp.exists():
                shutil.rmtree(sp, ignore_errors=True)
        return target_dir
    elif mode == "superkit":
        target_dir = BASE_DIR / "ia-superpowers-kit" / cid
        target_dir.mkdir(parents=True, exist_ok=True)
        for fname in ["CLAUDE.md", "GEMINI.md", "MEMORY.md", ".cursorrules"]:
            src = KIT_SRC_DIR / fname
            if src.exists():
                shutil.copy2(src, target_dir / fname)
        skills_dst = target_dir / "skills"
        if skills_dst.exists():
            shutil.rmtree(skills_dst, ignore_errors=True)
        shutil.copytree(KIT_SRC_DIR / "skills", skills_dst)
        return target_dir
    else:
        raise ValueError(f"Unknown mode: {mode}")


def extract_agy_tokens_for_tag(run_tag: str):
    """Reads antigravity-cli brain transcripts to extract exact input/cache/output tokens for a specific run_tag."""
    best = None
    for p in sorted(
        glob.glob("/Users/kevingonzalezlopez/.gemini/antigravity-cli/brain/*/.system_generated/logs/transcript_full.jsonl"),
        key=os.path.getmtime,
    ):
        try:
            with open(p, encoding="utf-8") as f:
                raw_lines = f.readlines()
            if not raw_lines:
                continue
            first_obj = json.loads(raw_lines[0])
            u_in = str(first_obj.get("content", ""))
            if run_tag in u_in:
                lines = [json.loads(l) for l in raw_lines]
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


def run_single(mode: str, challenge: dict):
    cid = challenge["id"]
    target_dir = prepare_workspace(mode, cid)
    target_file = target_dir / "index.html"
    run_tag = f"EP03_BENCHMARK_TAG::{cid}::{mode}"

    if mode == "raw":
        full_prompt = (
            f"[{run_tag}]\n"
            f"{challenge['prompt_body']}\n\n"
            f"INSTRUCCIÓN DE ARCHIVO OBLIGATORIA: Escribe el código HTML completo directamente en el archivo `{target_file}` usando tu herramienta de escritura de archivos. No pidas confirmación."
        )
        cmd = [
            "agy",
            "--dangerously-skip-permissions",
            "--disable-slash-commands",
            "--model",
            "gemini-4-argon-high",
            "--effort",
            "high",
            "-p",
            full_prompt,
        ]
    elif mode == "superkit":
        port_num = 8810 + challenge["num"]
        full_prompt = (
            f"[{run_tag}]\n"
            f"ESTÁS OPERANDO CON EL PROTOCOLO MIXIUH LABS SUPERPOWERS KIT EN `{target_dir}`.\n"
            f"Sigue el protocolo de `{target_dir}/GEMINI.md`, `{target_dir}/MEMORY.md` y las 5 skills en `{target_dir}/skills/`.\n"
            f"(Nota de aislamiento de entorno: si levantas un servidor HTTP o verificación headless para este reto, usa el puerto exclusivo `{port_num}` o un puerto efímero libre y ciérralo al terminar).\n\n"
            f"{challenge['prompt_body']}\n\n"
            f"INSTRUCCIÓN DE ARCHIVO OBLIGATORIA: Escribe el código HTML completo directamente en `{target_file}` y actualiza `{target_dir}/MEMORY.md` al finalizar. No pidas confirmación."
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
    else:
        raise ValueError(f"Unknown mode: {mode}")

    log_path = LOGS_DIR / f"{cid}_{mode}.log"
    print(f"[{datetime.now().strftime('%H:%M:%S')}] >>> STARTING {mode.upper()} on {cid} ...", flush=True)
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

    extracted_from_stdout = False
    if not target_file.exists() or target_file.stat().st_size < 500:
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

    token_telemetry = extract_agy_tokens_for_tag(run_tag)

    res = {
        "challenge_id": cid,
        "mode": mode,
        "run_tag": run_tag,
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
    cost_str = f"${token_telemetry['cost_usd']:.4f}" if token_telemetry else "N/A"
    tok_str = f"{token_telemetry['total_tokens']:,} tok" if token_telemetry else "N/A"
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] <<< FINISHED {mode.upper()} on {cid}: "
        f"{elapsed_sec}s ({elapsed_min}m) | {lines_count} lines ({res['size_kb']} KB) | {tok_str} ({cost_str})",
        flush=True,
    )
    return res


def main():
    only_mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    only_challenge = sys.argv[2] if len(sys.argv) > 2 else "all"
    max_workers = int(sys.argv[3]) if len(sys.argv) > 3 else 6

    results = load_results()
    modes_to_run = ["raw", "superkit"] if only_mode == "all" else [only_mode]

    tasks = []
    for ch in CHALLENGES:
        cid = ch["id"]
        if only_challenge != "all" and only_challenge != cid:
            continue
        if cid not in results["runs"]:
            results["runs"][cid] = {}
        for m in modes_to_run:
            prev = results["runs"][cid].get(m)
            if prev and prev.get("file_exists") and prev.get("size_bytes", 0) > 15000:
                print(f"[SKIP] {cid} ({m}) already exists ({prev['size_kb']} KB in {prev['elapsed_seconds']}s)", flush=True)
                continue
            tasks.append((m, ch))

    if not tasks:
        print("All requested benchmark runs are already complete.")
        return

    print(f"Launching {len(tasks)} benchmark runs with max_workers={max_workers} ...")
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        future_map = {pool.submit(run_single, m, ch): (m, ch["id"]) for m, ch in tasks}
        for fut in as_completed(future_map):
            m, cid = future_map[fut]
            try:
                res = fut.result()
                results = load_results()
                if cid not in results["runs"]:
                    results["runs"][cid] = {}
                results["runs"][cid][m] = res
                save_results(results)
            except Exception as e:
                print(f"[ERROR] {cid} ({m}) failed: {e}", flush=True)


if __name__ == "__main__":
    main()
