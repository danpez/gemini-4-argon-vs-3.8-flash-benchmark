#!/usr/bin/env python3
"""Genera episode.yaml para EP03 en Espanol (ep03-superpowers-kit) e Ingles (ep03-superpowers-kit-en)
con los datos reales del benchmark agy (Gemini 4 Argon High: Sin Kit vs Mixiuh Superpowers Kit, marcador 2-4)."""
from pathlib import Path

ROOT = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs")
EP_ES_DIR = ROOT / "episodes" / "ep03-superpowers-kit"
EP_EN_DIR = ROOT / "episodes" / "ep03-superpowers-kit-en"
EP_ES_DIR.mkdir(parents=True, exist_ok=True)
EP_EN_DIR.mkdir(parents=True, exist_ok=True)

YAML_ES = """# EP03 - IA Sin Kit vs IA + Mixiuh Superpowers Kit (Mixiuh Labs, episodio 03)
# Benchmark real ejecutado con agy --model gemini-4-argon-high --effort high
# IA SIN KIT (clave interna 'flash') a la izquierda en ambar (#FBBF24, sprite 'warning')
# SUPERKIT (clave interna 'argon') a la derecha en violeta (#B794F6, sprite 'rocket')
episode:
  id: ep03
  slug: ia-sin-kit-vs-mixiuh-superpowers-kit
  title: "Gemini 4 Argon High Sin Kit vs Mixiuh Superpowers Kit: ¿Realmente Necesitas Skills y Memoria Hoy?"
  voice: {voice_id: a580803d-fac8-4eb5-8453-709a13418052, stability: 0.5, speed: 1.05, seed: 7}
  render: {res: 2160, fps: 60}
  models:
    flash: {name: "IA Sin Kit (Argon Raw)", tag: "IA SIN KIT", color: "#FBBF24", side: left, sprite: "warning"}
    argon: {name: "IA + Superpowers Kit", tag: "SUPERKIT", color: "#B794F6", side: right, sprite: "rocket"}
  sources:
    galaxia_nbody: {file: "../../../ep03-superpowers-kit/grabaciones/01_galaxia_nbody_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    terminal_trading: {file: "../../../ep03-superpowers-kit/grabaciones/02_terminal_trading_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    arcade_boss_rush: {file: "../../../ep03-superpowers-kit/grabaciones/03_arcade_boss_rush_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    red_zero_trust: {file: "../../../ep03-superpowers-kit/grabaciones/04_red_zero_trust_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    motor_nodos_ia: {file: "../../../ep03-superpowers-kit/grabaciones/05_motor_nodos_ia_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    mixiuh_os_desktop: {file: "../../../ep03-superpowers-kit/grabaciones/06_mixiuh_os_desktop_comparativa.mov", content_box: [0, 0, 1920, 1080]}
  defaults: {pre: 0.0, post: 0.18, scene_tail: 0.35, transition: cut}
  captions: {plate: 0.88}
  pronunciations:
    "N-Body": "ene body"
    "Barnes-Hut": "Barns Jat"
    "HFT": "ache efe te"
    "VWAP": "ve uoble a pe"
    "Zero-Trust": "Zero Trust"
    "WAF": "uaf"
    "DAG": "dag"
    "MCP": "eme ce pe"
    "MixiuhOS": "Mixiuh O S"
    "Superkit": "Súper Kit"
    "Argon": "Árgon"
  thumbnails:
    - id: A
      text: "RAW | SUPERKIT"
      layout: split
      left: {clip: galaxia_nbody, t: 6.0, roi: [240, 60, 880, 960]}
      right: {clip: galaxia_nbody, t: 24.0, roi: [240, 60, 880, 960]}
    - id: B
      text: "$7.69 | $10.85"
      layout: split
      left: {clip: red_zero_trust, t: 6.5, roi: [240, 60, 880, 960]}
      right: {clip: red_zero_trust, t: 24.5, roi: [240, 60, 880, 960]}
    - id: C
      text: "2 | 4"
      layout: split
      left: {clip: mixiuh_os_desktop, t: 6.5, roi: [240, 60, 880, 960]}
      right: {clip: mixiuh_os_desktop, t: 24.5, roi: [240, 60, 880, 960]}
  youtube:
    titles:
      - "¿Siguen Sirviendo los Kits de Skills y Memoria? Gemini 4 Argon High Sin Kit vs Superpowers Kit"
      - "Probé Gemini 4 Argon High A Pelo vs Con 5 Skills y Auto-Debugger en 6 Sistemas Extremos"
      - "IA Sin Kit vs Mixiuh Superpowers Kit: El Veredicto Real en Tiempo, Costo y Calidad (4K60)"
    tags:
      - "Gemini 4 Argon High"
      - "Mixiuh Superpowers Kit"
      - "Antigravity Skills"
      - "Claude Code Skills"
      - "MCP Auto-Debugger"
      - "programar con IA"
      - "Mixiuh Labs"
    links:
      - {label: "Descargar Mixiuh AI Superpowers Kit (Gratis)", url: "https://labs.mixiuh.online"}
      - {label: "Probar las 12 demos interactivas reales del Episodio 03", url: "https://labs.mixiuh.online"}

scenes:

  # ===============================================================================================
  # ESCENA 01: HOOK
  # ===============================================================================================
  - id: hook
    chapter: "¿Siguen siendo necesarios los Kits de Skills hoy?"
    music: {cue: hook, gain_db: 0}
    hud: false
    beats:
      - id: hook-01
        say: "Con un modelo tan bestial como Gemini 4 Argon High, ¿realmente sigue valiendo la pena instalar kits de Skills, memoria persistente y depuradores de navegador?"
        voice: {speed: 1.10}
        transition: cut
        show:
          - clip: galaxia_nbody
            model: flash
            t: 2.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
          - clip: red_zero_trust
            model: flash
            t: 5.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "realmente"
            transition: glitch
        gfx:
          - {kind: big_text, at: "Argon", p: {text: "GEMINI 4 ARGON HIGH · SIN FILTROS", color: FLASH, accent: FLASH, y: 780, size: 88}}
        sfx:
          - {name: select, at: "Argon", gain_db: -4}

      - id: hook-02
        say: "Corrimos doce ejecuciones reales en Antigravity y el resultado nos sorprendió: el modelo en crudo ganó dos retos ahorrando 64 por ciento en tokens, pero el Superkit ganó 4 a 2 en sistemas complejos."
        voice: {speed: 1.10}
        transition: flash
        show:
          - clip: terminal_trading
            model: argon
            t: 20.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: big_text, at: "sorprendió", p: {text: "SUPERKIT 4 - 2 SIN KIT", color: WIN, accent: ARGON, y: 780, size: 104}}
        sfx:
          - {name: coin, at: "sorprendió", gain_db: -3}

      - id: hook-03
        say: "Hoy enfrentamos a la IA sin configuración contra el Mixiuh Superpowers Kit en seis sistemas extremos, y te regalo el repositorio completo para que lo instales en un minuto."
        voice: {speed: 1.10}
        show:
          - {clip: terminal_trading, model: argon, t: 21.0, roi: [0, 0, 1920, 1080]}
          - {clip: arcade_boss_rush, model: flash, t: 6.0, roi: [0, 0, 1920, 1080]}
          - {clip: mixiuh_os_desktop, model: argon, t: 22.0, roi: [0, 0, 1920, 1080]}
          - card: timer_race
            cut_at: "seis"
            p: {title: "TIEMPO TOTAL · 6 SISTEMAS REALES", flash: 276, argon: 302, ratio_text: "MARCADOR REAL: SUPERKIT 4 - 2 SIN KIT ($10.85 VS $7.69)"}
        gfx:
          - {kind: vs_badge, at: "seis", dur: 0.9, p: {x: 960, y: 598, beam: false}}
        sfx:
          - {name: powerup, at: "regalo", gain_db: -5}

  # ===============================================================================================
  # ESCENA 02: LOGO STING
  # ===============================================================================================
  - id: sting
    music: {cue: sting, gain_db: 0}
    hud: false
    beats:
      - id: sting-01
        dur: 2.9
        transition: cut
        show:
          - card: logo_sting
            p: {}

  # ===============================================================================================
  # ESCENA 03: ARQUITECTURA DEL SUPERPOWERS KIT
  # ===============================================================================================
  - id: protocolo
    chapter: "Qué incluye el Mixiuh Superpowers Kit"
    music: {cue: bed, gain_db: 0}
    hud: false
    beats:
      - id: protocolo-01
        say: "Soy Kevin, esto es Mixiuh Labs, y durante semanas vi cómo miles de desarrolladores culpan al modelo cuando su código sale lento, roto o carísimo."
        transition: pixel_wipe
        show:
          - card: title_card
            p: {kicker: "BENCHMARK REAL AGY CLI", title: "EXPERIMENTO 03", subtitle: "Gemini 4 Argon High: Sin Kit vs Superpowers Kit"}
        gfx:
          - {kind: lower_third, at: 0.35, p: {title: "Kevin González", subtitle: "Arquitecto del torneo · Mixiuh Labs"}}
        sfx:
          - {name: blip, at: "Mixiuh", gain_db: -6}

      - id: protocolo-02
        say: "El problema real es mandar a la IA a programar a ciegas: sin reglas de arquitectura, sin memoria persistente entre sesiones y sin un depurador que verifique el navegador."
        show:
          - split:
              flash: {clip: terminal_trading, t: 6.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: terminal_trading, t: 24.0, rate: 1.0, roi: [240, 60, 1440, 960]}
        sfx:
          - {name: select, at: "ciegas", gain_db: -6}
          - {name: select, at: "depurador", gain_db: -6}

      - id: protocolo-03
        say: "Por eso empaquetamos el Mixiuh Superpowers Kit: cinco habilidades modulares de alto rendimiento, un banco de memoria infinita y un guardia de calidad por MCP."
        show:
          - card: rules_card
            p:
              title: "MIXIUH SUPERPOWERS KIT V1.0"
              items: ["5 SKILLS + MEMORIA INFINITA", "AUTO-DEBUGGER DE NAVEGADOR"]
              reveal_at: [0.4, 2.3]

      - id: protocolo-04
        say: "En cada reto medimos el tiempo de entrega, el consumo real de tokens en dólares y si la aplicación sostiene 120 cuadros por segundo sin un solo error de consola."
        show:
          - card: stats_card
            p:
              title: "TELEMETRÍA REAL DE LAS 12 CORRIDAS"
              rows:
                - {label: "VICTORIAS EN TORNEO", flash: "2 RETOS", argon: "4 RETOS", better: argon}
                - {label: "COSTO API TOTAL", flash: "$7.69 USD", argon: "$10.85 USD", better: flash}

      - id: protocolo-05
        say: "Veamos la diferencia brutal en código real a través de seis niveles extremos."
        transition: pixel_wipe
        show:
          - card: scoreboard_card
            p:
              title: "LOS 6 DESAFÍOS REALES EN AGY"
              total: false
              rows:
                - {n: 1, title: "Nivel 1 · Simulador Galáctico N-Body 3D"}
                - {n: 2, title: "Nivel 2 · Terminal de Trading HFT Zero-GC"}
                - {n: 3, title: "Nivel 3 · Arcade Bullet-Hell Boss Rush"}
                - {n: 4, title: "Nivel 4 · Ciber-Defensa Zero-Trust 3D"}
                - {n: 5, title: "Nivel 5 · Motor de Nodos y Shaders GLSL"}
                - {n: 6, title: "Nivel 6 · Sistema Operativo Web MixiuhOS"}
        sfx:
          - {name: levelup, at: "seis", gain_db: -3}

  # ===============================================================================================
  # ESCENA 04: NIVEL 1 — SIMULADOR GALÁCTICO N-BODY 3D (GANA SUPERKIT: 0 - 1)
  # ===============================================================================================
  - id: reto01
    chapter: "Nivel 1: Simulador Galáctico N-Body 3D"
    music: {cue: battle, gain_db: 0}
    hud: {reto: 1, total: 6, title: "GALAXIA N-BODY 3D"}
    beats:
      - id: reto01-01
        say: "Nivel 1: simular la colisión gravitatoria de dos galaxias espirales con agujeros negros supermasivos y lente relativista en tiempo real."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 1, total: 6, world: "1-1", world_name: "SKILL 01 · SHADERS Y OCTREE", title: "GALAXIA N-BODY 3D", subtitle: "48,000 estrellas, Barnes-Hut Octree y pozo gravitacional 3D", times: {flash: 45, argon: 44}}
          - clip: galaxia_nbody
            model: argon
            t: 18.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "con"

      - id: reto01-02
        say: "Sin el kit, Gemini 4 Argon High tardó 45 minutos y logró animar 48 mil estrellas a 60 cuadros con un millón de tokens, pero dejó un error 404 en consola y una malla espacial casi plana."
        show:
          - clip: galaxia_nbody
            model: flash
            t: 1.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "45", dur: 1.8, p: {from: 0, to: 45, suffix: "MIN", label: "IA SIN KIT · $1.26 USD · 1 ERROR 404", color: FLASH, accent: FLASH}}

      - id: reto01-03
        say: "Con el Superpowers Kit terminó en 44 minutos: gastó 2 dólares con 25 centavos al auditar el navegador, pero entregó cero errores, una deformación gravitatoria 3D brutal y memoria documentada."
        transition: flash
        show:
          - clip: galaxia_nbody
            model: argon
            t: 19.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [100, 56, 1720, 968]
        gfx:
          - {kind: counter, at: "44", dur: 1.8, p: {from: 0, to: 44, suffix: "MIN", label: "SUPERKIT · $2.25 USD · 0 ERRORES + POZO 3D", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "44", gain_db: -3}

      - id: reto01-04
        say: "Un minuto más rápido, cero errores en consola y mejor geometría relativista: el primer punto es para el Superpowers Kit."
        show:
          - split:
              flash: {clip: galaxia_nbody, t: 6.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: galaxia_nbody, t: 24.0, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "primer"
            transition: flash
            p:
              winner: argon
              headline: "POZO GRAVITACIONAL 3D Y 0 ERRORES"
              reason: "44 min ($2.25) vs 45 min ($1.26) · 0 errores de consola y malla de curvatura 3D superior"
              score: {flash: 0, argon: 1}
        score: {flash: 0, argon: 1}
        score_at: "primer"

  # ===============================================================================================
  # ESCENA 05: NIVEL 2 — TERMINAL DE TRADING HFT ZERO-GC (GANA SUPERKIT: 0 - 2)
  # ===============================================================================================
  - id: reto02
    chapter: "Nivel 2: Terminal de Trading HFT Zero-GC"
    music: {cue: bed, gain_db: 0}
    hud: {reto: 2, total: 6, title: "TERMINAL TRADING HFT"}
    beats:
      - id: reto02-01
        say: "Nivel 2: una terminal institucional de trading de alta frecuencia capaz de procesar miles de órdenes por segundo con libro de profundidad y mapa de calor de liquidez."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 2, total: 6, world: "1-2", world_name: "SKILL 02 · MEMORIA ZERO-GC", title: "TERMINAL TRADING HFT", subtitle: "70,406 órdenes/s, Float32Array RingBuffer y mapa de liquidez", times: {flash: 73, argon: 57}}
          - clip: terminal_trading
            model: argon
            t: 18.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "con"

      - id: reto02-02
        say: "Aquí la IA sin kit sufrió su corrida más larga: tardó 73 minutos, escribió casi 3 mil 900 líneas por un dólar setenta y cinco y su motor se quedó en 11 mil órdenes por segundo."
        show:
          - clip: terminal_trading
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "73", dur: 1.8, p: {from: 0, to: 73, suffix: "MIN", label: "IA SIN KIT · $1.75 USD · 11,073 ORD/S", color: FLASH, accent: FLASH}}

      - id: reto02-03
        say: "En cambio, las Skills de arquitectura Zero-GC guiaron al Superkit directo al grano en 57 minutos y por un dólar cincuenta y seis, alcanzando 70 mil 406 órdenes por segundo."
        transition: flash
        show:
          - clip: terminal_trading
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "57", dur: 1.8, p: {from: 0, to: 57, suffix: "MIN", label: "SUPERKIT · $1.56 USD · 70,406 ORD/S (6.3X)", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "57", gain_db: -4}

      - id: reto02-04
        say: "Dieciséis minutos más rápido, más barato en tokens y seis veces más caudal de órdenes: el Superpowers Kit se pone dos a cero."
        show:
          - split:
              flash: {clip: terminal_trading, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: terminal_trading, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "dos"
            transition: flash
            p:
              winner: argon
              headline: "6.3X MÁS RENDIMIENTO Y MÁS BARATO"
              reason: "57 min ($1.56) vs 73 min ($1.75) · 70,406 vs 11,073 ord/s con buffers Zero-GC"
              score: {flash: 0, argon: 2}
        score: {flash: 0, argon: 2}
        score_at: "dos"

  # ===============================================================================================
  # ESCENA 06: NIVEL 3 — ARCADE BULLET-HELL BOSS RUSH (GANA IA SIN KIT: 1 - 2)
  # ===============================================================================================
  - id: reto03
    chapter: "Nivel 3: Arcade Bullet-Hell Boss Rush"
    music: {cue: tension, gain_db: 0}
    hud: {reto: 3, total: 6, title: "ARCADE BOSS RUSH"}
    beats:
      - id: reto03-01
        say: "Nivel 3: un juego Arcade Bullet-Hell con jefe biomecánico de tres fases, miles de proyectiles simultáneos, colisión continua y sintetizador musical."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 3, total: 6, world: "2-1", world_name: "RONDA 03 · DANMAKU Y WEB AUDIO", title: "ARCADE BOSS RUSH", subtitle: "Pool de proyectiles TypedArray, Spatial Hash y sintetizador FM", times: {flash: 51, argon: 69}}
          - clip: arcade_boss_rush
            model: flash
            t: 4.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "miles"

      - id: reto03-02
        say: "Y aquí llegó la primera sorpresa: Gemini 4 Argon High sin kit ya domina TypedArrays de fábrica, terminó en 51 minutos por un dólar sesenta y cuatro y desató espirales de 379 balas a 61 cuadros."
        show:
          - clip: arcade_boss_rush
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "51", dur: 1.8, p: {from: 0, to: 51, suffix: "MIN", label: "IA SIN KIT · $1.64 USD · 379 BALAS ACTIVAS", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "51", gain_db: -4}

      - id: reto03-03
        say: "Con el Superpowers Kit, la sobrecarga de leer las cinco Skills e iterar sobre la memoria alargó la entrega hasta los 69 minutos con un patrón más conservador de 96 proyectiles."
        transition: flash
        show:
          - clip: arcade_boss_rush
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "69", dur: 1.8, p: {from: 0, to: 69, suffix: "MIN", label: "SUPERKIT · $1.68 USD · 96 BALAS ACTIVAS", color: ARGON, accent: ARGON}}

      - id: reto03-04
        say: "Dieciocho minutos más veloz y con patrones de ataque cuatro veces más intensos: primer punto legítimo para la IA sin kit, que acorta el marcador uno a dos."
        show:
          - split:
              flash: {clip: arcade_boss_rush, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: arcade_boss_rush, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "primer"
            transition: flash
            p:
              winner: flash
              headline: "IA SIN KIT GANA EN VELOCIDAD Y DANMAKU"
              reason: "51 min ($1.64) vs 69 min ($1.68) · 379 balas en espiral a 61 FPS y 18 min más rápido"
              score: {flash: 1, argon: 2}
        score: {flash: 1, argon: 2}
        score_at: "primer"

  # ===============================================================================================
  # ESCENA 07: NIVEL 4 — CIBER-DEFENSA ZERO-TRUST 3D (GANA IA SIN KIT: 2 - 2 EMPATE)
  # ===============================================================================================
  - id: reto04
    chapter: "Nivel 4: Ciber-Defensa Zero-Trust 3D"
    music: {cue: battle, gain_db: 0}
    hud: {reto: 4, total: 6, title: "RED ZERO-TRUST 3D"}
    beats:
      - id: reto04-01
        say: "Nivel 4: un centro de mando de ciberseguridad Zero-Trust capaz de inspeccionar paquetes criptográficos y neutralizar ataques DDoS e inyecciones SQL en vivo."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 4, total: 6, world: "2-2", world_name: "RONDA 04 · EFICIENCIA ONE-SHOT", title: "RED ZERO-TRUST 3D", subtitle: "Globo holográfico 3D, inspección mTLS y mitigación DDoS", times: {flash: 24, argon: 43}}
          - clip: red_zero_trust
            model: flash
            t: 4.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "neutralizar"

      - id: reto04-02
        say: "En este reto, la IA sin kit dio una cátedra de eficiencia: en solo 5 pasos de agente y 23 minutos y medio construyó el globo 3D con etiquetas flotantes por apenas 74 centavos."
        show:
          - clip: red_zero_trust
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "23", dur: 1.8, p: {from: 0, to: 24, suffix: "MIN", label: "IA SIN KIT · $0.74 USD · SOLO 5 PASOS", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "74", gain_db: -3}

      - id: reto04-03
        say: "Mientras tanto, el protocolo obligatorio del Superkit le hizo ejecutar 32 pasos de lectura y auditoría, tardando 43 minutos y consumiendo 2 dólares con 4 centavos para llegar al mismo resultado."
        transition: flash
        show:
          - clip: red_zero_trust
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "43", dur: 1.8, p: {from: 0, to: 43, suffix: "MIN", label: "SUPERKIT · $2.04 USD · 32 PASOS AGÉNTICOS", color: ARGON, accent: ARGON}}

      - id: reto04-04
        say: "Casi el doble de rápido y 64 por ciento más barato en tokens: la IA sin kit gana el cuarto reto y empata el partido dos a dos."
        show:
          - split:
              flash: {clip: red_zero_trust, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: red_zero_trust, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "empata"
            transition: flash
            p:
              winner: flash
              headline: "EMPATE 2 - 2 · ONE-SHOT EN 5 PASOS"
              reason: "23.5 min ($0.74, 190K tok) vs 42.8 min ($2.04, 2.59M tok) · Etiquetas 3D en cada nodo"
              score: {flash: 2, argon: 2}
        score: {flash: 2, argon: 2}
        score_at: "empata"

  # ===============================================================================================
  # ESCENA 08: NIVEL 5 — MOTOR DE NODOS Y AGENTES IA (GANA SUPERKIT: 2 - 3)
  # ===============================================================================================
  - id: reto05
    chapter: "Nivel 5: Motor de Nodos y Shaders GLSL (DAG)"
    music: {cue: bed, gain_db: 0}
    hud: {reto: 5, total: 6, title: "MOTOR NODOS IA DAG"}
    beats:
      - id: reto05-01
        say: "Nivel 5: un editor visual de flujos multi-agente con cables Bézier, ejecución topológica en paralelo y detección de ciclos infinitos."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 5, total: 6, world: "3-1", world_name: "SKILL 05 · GRAFOS DAG Y GLSL", title: "MOTOR DE NODOS IA", subtitle: "Compilador topológico de Kahn, cables Bézier y Raymarching 3D", times: {flash: 55, argon: 47}}
          - clip: motor_nodos_ia
            model: argon
            t: 18.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "ejecución"

      - id: reto05-02
        say: "Con el marcador empatado, subimos la complejidad arquitectónica: sin el kit, la IA tardó 55 minutos coordinando el compilador del grafo con el visor WebGL y conectó 8 cables."
        show:
          - clip: motor_nodos_ia
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "55", dur: 1.8, p: {from: 0, to: 55, suffix: "MIN", label: "IA SIN KIT · $1.58 USD · 8 CABLES DAG", color: FLASH, accent: FLASH}}

      - id: reto05-03
        say: "Aquí las plantillas del Superpowers Kit brillaron de nuevo: resolvió el compilador topológico en 47 minutos con 10 cables perfectamente distribuidos y un shader 4D con iluminación Fresnel."
        transition: flash
        show:
          - clip: motor_nodos_ia
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [100, 56, 1720, 968]
        gfx:
          - {kind: counter, at: "47", dur: 1.8, p: {from: 0, to: 47, suffix: "MIN", label: "SUPERKIT · $1.72 USD · 10 CABLES + FRESNEL 4D", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "47", gain_db: -3}

      - id: reto05-04
        say: "Ocho minutos más rápido y con un grafo visual impecable: el Superpowers Kit rompe el empate y toma ventaja tres a dos."
        show:
          - split:
              flash: {clip: motor_nodos_ia, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: motor_nodos_ia, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "rompe"
            transition: flash
            p:
              winner: argon
              headline: "GRAFO DAG DE 10 CABLES Y RAYMARCHING 4D"
              reason: "47 min ($1.72) vs 55 min ($1.58) · 8 min más rápido y mejor distribución topológica"
              score: {flash: 2, argon: 3}
        score: {flash: 2, argon: 3}
        score_at: "rompe"

  # ===============================================================================================
  # ESCENA 09: NIVEL 6 — SISTEMA OPERATIVO WEB MIXIUHOS (GANA SUPERKIT: 2 - 4 FINAL)
  # ===============================================================================================
  - id: reto06
    chapter: "Nivel 6: Sistema Operativo Web MixiuhOS"
    music: {cue: battle, gain_db: 0}
    hud: {reto: 6, total: 6, title: "MIXIUH OS DESKTOP"}
    beats:
      - id: reto06-01
        say: "Nivel final: construir un sistema operativo web completo con gestor de ventanas, sistema de archivos virtual, terminal interactiva, editor de código y monitor de recursos."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 6, total: 6, world: "3-2", world_name: "MEMORIA INFINITA + AUTO-DEBUGGER", title: "MIXIUH OS DESKTOP", subtitle: "Gestor de ventanas y 4 apps en vivo: WebGL, Synth, Terminal y Kernel", times: {flash: 29, argon: 42}}
          - clip: mixiuh_os_desktop
            model: argon
            t: 18.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "terminal"

      - id: reto06-02
        say: "Sin el kit, la IA terminó rápido en 29 minutos por 72 centavos, pero al no verificar el navegador dejó el arte ASCII de la terminal aplastado en una línea y sin controles en la ventana 3D."
        show:
          - clip: mixiuh_os_desktop
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "29", dur: 1.8, p: {from: 0, to: 29, suffix: "MIN", label: "IA SIN KIT · $0.72 USD · ASCII APLASTADO", color: FLASH, accent: FLASH}}

      - id: reto06-03
        say: "El Superpowers Kit invirtió 42 minutos y un dólar sesenta usando su Auto-Debugger para inspeccionar el DOM, puliendo el banner de neofetch, los presets 3D y las perillas del sintetizador."
        transition: flash
        show:
          - clip: mixiuh_os_desktop
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "42", dur: 1.8, p: {from: 0, to: 42, suffix: "MIN", label: "SUPERKIT · $1.60 USD · 4 APPS VERIFICADAS", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "42", gain_db: -3}

      - id: reto06-04
        say: "Cuando integras cuatro subsistemas en una misma pantalla, el Auto-Debugger marca la diferencia: victoria final cuatro a dos para el Mixiuh Superpowers Kit."
        show:
          - split:
              flash: {clip: mixiuh_os_desktop, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: mixiuh_os_desktop, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "cuatro"
            transition: flash
            p:
              winner: argon
              headline: "VICTORIA 4 - 2 DEL SUPERPOWERS KIT"
              reason: "42 min ($1.60) vs 29 min ($0.72) · Auto-Debugger pulió las 4 sub-aplicaciones y MEMORY.md"
              score: {flash: 2, argon: 4}
        score: {flash: 2, argon: 4}
        score_at: "cuatro"

  # ===============================================================================================
  # ESCENA 10: PANTALLA DE RESULTADOS Y VEREDICTO HONESTO
  # ===============================================================================================
  - id: resultados
    chapter: "Veredicto real: cuándo usar el Kit y cuándo no"
    music: {cue: results, gain_db: 0}
    hud: false
    beats:
      - id: resultados-01
        say: "Cuatro a dos en el marcador final: un experimento cien por ciento real que demuestra tanto el poder nativo de Gemini 4 Argon High como el valor del Superpowers Kit."
        post: 2.8
        transition: flash
        show:
          - {clip: galaxia_nbody, model: argon, t: 24.0, rate: 1.0, roi: [0, 0, 1920, 1080]}
          - {clip: mixiuh_os_desktop, model: argon, t: 24.0, rate: 1.0, roi: [0, 0, 1920, 1080]}
          - card: scoreboard_card
            cut_at: "experimento"
            p:
              title: "MARCADOR REAL · EPISODIO 03 (4 - 2)"
              rows:
                - {n: 1, title: "Simulador Galáctico N-Body 3D", winner: argon, flash_min: 45, argon_min: 44}
                - {n: 2, title: "Terminal de Trading HFT Zero-GC", winner: argon, flash_min: 73, argon_min: 57}
                - {n: 3, title: "Arcade Bullet-Hell Boss Rush", winner: flash, flash_min: 51, argon_min: 69}
                - {n: 4, title: "Ciber-Defensa Zero-Trust 3D", winner: flash, flash_min: 24, argon_min: 43}
                - {n: 5, title: "Motor de Nodos y Shaders GLSL", winner: argon, flash_min: 55, argon_min: 47}
                - {n: 6, title: "Sistema Operativo Web MixiuhOS", winner: argon, flash_min: 29, argon_min: 42}
        sfx:
          - {name: powerup, at: 0.05, gain_db: -4}

      - id: resultados-02
        say: "En tiempo acumulado, la IA sin kit sumó 276 minutos frente a 302 minutos del Superkit, que fue más rápido en los retos de mayor complejidad pero invirtió tiempo auditando el navegador."
        show:
          - card: timer_race
            p: {flash: 276, argon: 302, title: "TIEMPO TOTAL · 6 SISTEMAS REALES", ratio_text: "SIN KIT: 276 MIN · SUPERKIT: 302 MIN (MÁS VELOZ EN HFT Y DAG)"}

      - id: resultados-03
        say: "En calidad técnica, el Superpowers Kit eliminó el único error de consola del torneo, sextuplicó el rendimiento en trading a 70 mil órdenes por segundo y dejó memoria documentada."
        post: 0.4
        show:
          - card: stats_card
            p:
              title: "AUDITORÍA TÉCNICA EN CHROME"
              rows:
                - {label: "CAUDAL HFT (RETO 02)", flash: "11,073 ORD/S", argon: "70,406 ORD/S", better: argon}
                - {label: "ERRORES DE CONSOLA", flash: "1 ERROR 404", argon: "0 ERRORES", better: lower}

      - id: resultados-04
        say: "Y en la factura de API está el dato clave: 7 dólares con 69 centavos y 6.1 millones de tokens sin kit, contra 10 dólares con 85 centavos y 13.2 millones de tokens al cargar las Skills y el Auto-Debugger."
        post: 0.8
        show:
          - card: stats_card
            p:
              title: "FACTURA REAL DE TOKENS (USD)"
              rows:
                - {label: "TOKENS CONSUMIDOS", flash: "6.12M TOK", argon: "13.20M TOK", better: flash}
                - {label: "COSTO API TOTAL", flash: "$7.69 USD", argon: "$10.85 USD", better: flash}
        sfx:
          - {name: coin, at: "7", gain_db: -3}

  # ===============================================================================================
  # ESCENA 11: VEREDICTO FINAL Y DESCARGA DEL KIT
  # ===============================================================================================
  - id: cierre
    chapter: "Conclusión: ¿Son necesarios los Kits hoy?"
    music: {cue: outro, gain_db: 0}
    hud: false
    beats:
      - id: cierre-01
        say: "La lección es contundente: antes de pagar por un modelo más caro, dale a tu agente reglas claras de arquitectura, habilidades especializadas y verificación automática."
        transition: pixel_wipe
        show:
          - split:
              flash: {clip: galaxia_nbody, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: galaxia_nbody, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}

      - id: cierre-02
        say: "Para prototipos de un solo archivo, Gemini 4 Argon High en crudo ya es tan capaz que ahorra tokens sin ayuda; pero en arquitecturas multicapa y producción, el Superpowers Kit gana 4 a 2."
        captions: false
        show:
          - card: quote_card
            p:
              text: "En retos de un tiro, Gemini 4 Argon High sin kit ahorra 29% en tokens ($7.69 vs $10.85). En sistemas complejos (HFT, DAG y Web OS), el Superpowers Kit gana 4-2 con 0 errores."
              author: "Veredicto Real · Mixiuh Labs"

      - id: cierre-03
        say: "Te dejé las doce demos interactivas y la descarga gratuita del Mixiuh Superpowers Kit en labs punto mixiuh punto online, listo para Claude Code, Antigravity y Cursor."
        show:
          - split:
              flash: {clip: arcade_boss_rush, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: arcade_boss_rush, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}
          - split:
              flash: {clip: mixiuh_os_desktop, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: mixiuh_os_desktop, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}
            cut_at: "descarga"

      - id: cierre-04
        say: "Suscríbete a Mixiuh Labs, descarga el kit hoy mismo y déjame en los comentarios qué habilidad o torneo multinivel quieres que construyamos en el Episodio 04."
        transition: pixel_wipe
        show:
          - card: end_screen
            p: {headline: "Descarga gratis el Superpowers Kit", sub: "labs.mixiuh.online · suscríbete a Mixiuh Labs"}
        sfx:
          - {name: coin, at: 0.3, gain_db: -3}

  # ===============================================================================================
  # ESCENA 12: ENDSCREEN
  # ===============================================================================================
  - id: endscreen
    music: {cue: outro, gain_db: 0}
    hud: false
    beats:
      - id: endscreen-01
        say: "Experimento 03 terminado: nos vemos en el siguiente nivel, aquí en Mixiuh Labs."
        dur: 11.0
        show:
          - continue: true
"""

YAML_EN = """# EP03 (English) - Raw AI vs Mixiuh Superpowers Kit (Mixiuh Labs, episode 03, English version)
# Real benchmark executed with agy --model gemini-4-argon-high --effort high
# RAW AI (internal key 'flash') on the left in amber (#FBBF24, sprite 'warning')
# SUPERKIT (internal key 'argon') on the right in violet (#B794F6, sprite 'rocket')
episode:
  id: ep03-en
  slug: raw-ai-vs-mixiuh-superpowers-kit-en
  title: "Gemini 4 Argon High Raw vs Mixiuh Superpowers Kit: Do You Still Need Skills & Memory Kits Today?"
  lang: en
  voice: {voice_id: a580803d-fac8-4eb5-8453-709a13418052, language: en, stability: 0.5, speed: 1.10, seed: 7}
  render: {res: 2160, fps: 60}
  models:
    flash: {name: "Raw AI (Argon Raw)", tag: "RAW AI", color: "#FBBF24", side: left, sprite: "warning"}
    argon: {name: "AI + Superpowers Kit", tag: "SUPERKIT", color: "#B794F6", side: right, sprite: "rocket"}
  sources:
    galaxia_nbody: {file: "../../../ep03-superpowers-kit/grabaciones/01_galaxia_nbody_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    terminal_trading: {file: "../../../ep03-superpowers-kit/grabaciones/02_terminal_trading_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    arcade_boss_rush: {file: "../../../ep03-superpowers-kit/grabaciones/03_arcade_boss_rush_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    red_zero_trust: {file: "../../../ep03-superpowers-kit/grabaciones/04_red_zero_trust_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    motor_nodos_ia: {file: "../../../ep03-superpowers-kit/grabaciones/05_motor_nodos_ia_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    mixiuh_os_desktop: {file: "../../../ep03-superpowers-kit/grabaciones/06_mixiuh_os_desktop_comparativa.mov", content_box: [0, 0, 1920, 1080]}
  defaults: {pre: 0.0, post: 0.18, scene_tail: 0.35, transition: cut}
  captions: {plate: 0.88}
  pronunciations:
    "N-Body": "N Body"
    "Barnes-Hut": "Barnes Hut"
    "HFT": "H F T"
    "VWAP": "V WAP"
    "WAF": "W A F"
    "DAG": "D A G"
    "MCP": "M C P"
    "GPU": "G P U"
    "API": "A P I"
    "USD": "U S D"
    "VFS": "V F S"
    "SQLi": "S Q L injection"
    "MixiuhOS": "Mixiuh O S"
  thumbnails:
    - id: A
      text: "RAW | SUPERKIT"
      layout: split
      left: {clip: galaxia_nbody, t: 6.0, roi: [240, 60, 880, 960]}
      right: {clip: galaxia_nbody, t: 24.0, roi: [240, 60, 880, 960]}
    - id: B
      text: "$7.69 | $10.85"
      layout: split
      left: {clip: red_zero_trust, t: 6.5, roi: [240, 60, 880, 960]}
      right: {clip: red_zero_trust, t: 24.5, roi: [240, 60, 880, 960]}
    - id: C
      text: "2 | 4"
      layout: split
      left: {clip: mixiuh_os_desktop, t: 6.5, roi: [240, 60, 880, 960]}
      right: {clip: mixiuh_os_desktop, t: 24.5, roi: [240, 60, 880, 960]}
  youtube:
    titles:
      - "Do You Still Need Skills & Memory Kits? Gemini 4 Argon High Raw vs Superpowers Kit"
      - "I Tested Gemini 4 Argon High Raw vs 5 Skills & Auto-Debugger Across 6 Extreme Systems"
      - "Raw AI vs Mixiuh Superpowers Kit: The Honest Verdict on Speed, Cost & Quality (4K60)"
    hook: "We ran 12 real isolated agy CLI runs with Gemini 4 Argon High (6 Raw vs 6 with the Mixiuh Superpowers Kit). Final score: 4-2 for the Superkit, but Raw AI won 2 challenges and cost $7.69 vs $10.85 USD."
    summary: "With frontier models like Gemini 4 Argon High, are Skills, Memory Banks, and Browser Auto-Debuggers still necessary, or do they just burn extra tokens? We ran 12 real isolated benchmarks in Antigravity across 6 extreme WebGL/Canvas/WebAudio systems. Raw Gemini 4 Argon High won 2 rounds (Bullet-Hell Boss Rush in 51m vs 69m with 4x denser danmaku patterns, and 3D Zero-Trust Cyber Defense in just 5 agent steps for $0.74 vs $2.04). However, the Mixiuh Superpowers Kit won 4-2 overall—delivering 6.3x higher HFT order throughput (70,406 vs 11,073 ord/s, 16 minutes faster and cheaper), faster DAG + GLSL Raymarching compilation, zero console errors, and catching multi-window UI bugs in MixiuhOS."
    keywords: ["Gemini 4 Argon High", "Mixiuh Superpowers Kit", "Antigravity Skills", "Claude Code Skills", "MCP Auto-Debugger"]
    tags:
      - "Gemini 4 Argon High"
      - "Mixiuh Superpowers Kit"
      - "Claude Code Skills"
      - "Antigravity Skills"
      - "MCP Auto-Debugger"
      - "AI coding benchmark"
      - "Mixiuh Labs"
    hashtags: ["#AICoding", "#Gemini4Argon", "#MixiuhLabs"]
    pinned_comment: "Download the complete Mixiuh AI Superpowers Kit v1.0 for free and test all 12 real interactive apps at https://labs.mixiuh.online — When do you use Skills vs Raw prompts?"
    tools:
      - "Voice: Voicefy, cloned voice running locally on Mac (narrated in English)."
      - "Editing and captions: Reelfy + Mixiuh Labs Studio (4K60 pipeline)."
      - "Music: original procedural chiptune generated by code."
      - "Stack: agy --model gemini-4-argon-high --effort high + Mixiuh Superpowers Kit v1.0."
    language: "en"
    facts: false
    links:
      - {label: "Download Mixiuh AI Superpowers Kit (Free)", url: "https://labs.mixiuh.online"}
      - {label: "Play all 12 real interactive demos from Episode 03", url: "https://labs.mixiuh.online"}

scenes:

  # ===============================================================================================
  # SCENE 01: HOOK
  # ===============================================================================================
  - id: hook
    chapter: "Are Skills & Memory Kits still necessary today?"
    music: {cue: hook, gain_db: 0}
    hud: false
    beats:
      - id: hook-01
        say: "With a frontier model as capable as Gemini 4 Argon High, do you still need Skills kits, persistent memory banks, and browser auto-debuggers?"
        voice: {speed: 1.10}
        transition: cut
        show:
          - clip: galaxia_nbody
            model: flash
            t: 2.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
          - clip: red_zero_trust
            model: flash
            t: 5.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "still"
            transition: glitch
        gfx:
          - {kind: big_text, at: "Argon", p: {text: "GEMINI 4 ARGON HIGH · REAL TEST", color: FLASH, accent: FLASH, y: 780, size: 88}}
        sfx:
          - {name: select, at: "Argon", gain_db: -4}

      - id: hook-02
        say: "We ran twelve real benchmarks in Antigravity and the truth surprised us: Raw AI won two challenges while saving 64 percent in tokens, but the Superkit won 4 to 2 on complex architectures."
        voice: {speed: 1.10}
        transition: flash
        show:
          - clip: terminal_trading
            model: argon
            t: 20.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: big_text, at: "surprised", p: {text: "SUPERKIT 4 - 2 RAW AI", color: WIN, accent: ARGON, y: 780, size: 104}}
        sfx:
          - {name: coin, at: "surprised", gain_db: -3}

      - id: hook-03
        say: "Today we pit Raw AI against the Mixiuh Superpowers Kit across six extreme systems, and I'm giving you the entire repository for free so you can install it in sixty seconds."
        voice: {speed: 1.10}
        show:
          - {clip: terminal_trading, model: argon, t: 21.0, roi: [0, 0, 1920, 1080]}
          - {clip: arcade_boss_rush, model: flash, t: 6.0, roi: [0, 0, 1920, 1080]}
          - {clip: mixiuh_os_desktop, model: argon, t: 22.0, roi: [0, 0, 1920, 1080]}
          - card: timer_race
            cut_at: "six"
            p: {title: "TOTAL TIME · 6 REAL SYSTEMS", flash: 276, argon: 302, ratio_text: "REAL SCORE: SUPERKIT 4 - 2 RAW AI ($10.85 VS $7.69)"}
        gfx:
          - {kind: vs_badge, at: "six", dur: 0.9, p: {x: 960, y: 598, beam: false}}
        sfx:
          - {name: powerup, at: "free", gain_db: -5}

  # ===============================================================================================
  # SCENE 02: LOGO STING
  # ===============================================================================================
  - id: sting
    music: {cue: sting, gain_db: 0}
    hud: false
    beats:
      - id: sting-01
        dur: 2.9
        transition: cut
        show:
          - card: logo_sting
            p: {}

  # ===============================================================================================
  # SCENE 03: SUPERPOWERS KIT ARCHITECTURE
  # ===============================================================================================
  - id: protocolo
    chapter: "Inside the Mixiuh Superpowers Kit"
    music: {cue: bed, gain_db: 0}
    hud: false
    beats:
      - id: protocolo-01
        say: "I'm Kevin, this is Mixiuh Labs, and for months I've watched developers blame the AI model whenever their code comes out slow, broken, or overpriced."
        transition: pixel_wipe
        show:
          - card: title_card
            p: {kicker: "REAL AGY CLI BENCHMARK", title: "EXPERIMENT 03", subtitle: "Gemini 4 Argon High: Raw AI vs Superpowers Kit"}
        gfx:
          - {kind: lower_third, at: 0.35, p: {title: "Kevin González", subtitle: "Tournament Referee · Mixiuh Labs"}}
        sfx:
          - {name: blip, at: "Mixiuh", gain_db: -6}

      - id: protocolo-02
        say: "The real problem is sending your AI to code blindfolded: with zero architectural guardrails, zero persistent memory across sessions, and no browser debugger to verify the output."
        show:
          - split:
              flash: {clip: terminal_trading, t: 6.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: terminal_trading, t: 24.0, rate: 1.0, roi: [240, 60, 1440, 960]}
        sfx:
          - {name: select, at: "blindfolded", gain_db: -6}
          - {name: select, at: "debugger", gain_db: -6}

      - id: protocolo-03
        say: "That's why we built the Mixiuh Superpowers Kit: five high-performance engineering skills, an infinite memory bank, and an automated MCP quality gate."
        show:
          - card: rules_card
            p:
              title: "MIXIUH SUPERPOWERS KIT V1.0"
              items: ["5 SKILLS + INFINITE MEMORY", "BROWSER AUTO-DEBUGGER GATE"]
              reveal_at: [0.4, 2.3]

      - id: protocolo-04
        say: "In every challenge we measure wall-clock time, real API token cost in dollars, and whether the app holds 120 frames per second with zero console errors."
        show:
          - card: stats_card
            p:
              title: "REAL TELEMETRY ACROSS 12 RUNS"
              rows:
                - {label: "TOURNAMENT WINS", flash: "2 ROUNDS", argon: "4 ROUNDS", better: argon}
                - {label: "REAL TOKEN BILL", flash: "$7.69 USD", argon: "$10.85 USD", better: flash}

      - id: protocolo-05
        say: "Let's see the brutal difference in real code across six extreme engineering levels."
        transition: pixel_wipe
        show:
          - card: scoreboard_card
            p:
              title: "THE 6 REAL AGY CHALLENGES"
              total: false
              rows:
                - {n: 1, title: "Level 1 · 3D N-Body Galaxy Simulator"}
                - {n: 2, title: "Level 2 · Zero-GC HFT Trading Terminal"}
                - {n: 3, title: "Level 3 · Bullet-Hell Arcade Boss Rush"}
                - {n: 4, title: "Level 4 · 3D Zero-Trust Cyber Defense"}
                - {n: 5, title: "Level 5 · AI Node & GLSL Shader Studio"}
                - {n: 6, title: "Level 6 · MixiuhOS Web Desktop"}
        sfx:
          - {name: levelup, at: "six", gain_db: -3}

  # ===============================================================================================
  # SCENE 04: LEVEL 1 — 3D N-BODY GALAXY SIMULATOR (SUPERKIT WINS: 0 - 1)
  # ===============================================================================================
  - id: reto01
    chapter: "Level 1: 3D N-Body Galaxy Simulator"
    music: {cue: battle, gain_db: 0}
    hud: {reto: 1, total: 6, title: "3D N-BODY GALAXY"}
    beats:
      - id: reto01-01
        say: "Level 1: simulate the gravitational collision of two spiral galaxies with supermassive black holes and relativistic lensing in real time."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 1, total: 6, world: "1-1", world_name: "SKILL 01 · SHADERS & OCTREE", title: "3D N-BODY GALAXY", subtitle: "48,000 stars, Barnes-Hut Octree & 3D gravity well", times: {flash: 45, argon: 44}}
          - clip: galaxia_nbody
            model: argon
            t: 18.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "with"

      - id: reto01-02
        say: "Without the kit, Gemini 4 Argon High took 45 minutes and animated 48 thousand stars at 60 frames per second for a dollar twenty-six, but left a 404 console error and a flat spacetime grid."
        show:
          - clip: galaxia_nbody
            model: flash
            t: 1.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "45", dur: 1.8, p: {from: 0, to: 45, suffix: "MIN", label: "RAW AI · $1.26 USD · 1 ERROR 404", color: FLASH, accent: FLASH}}

      - id: reto01-03
        say: "With the Superpowers Kit, it finished in 44 minutes: spending 2 dollars and 25 cents to run browser checks, delivering zero console errors, deep 3D gravity-well curvature, and full memory logs."
        transition: flash
        show:
          - clip: galaxia_nbody
            model: argon
            t: 19.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [100, 56, 1720, 968]
        gfx:
          - {kind: counter, at: "44", dur: 1.8, p: {from: 0, to: 44, suffix: "MIN", label: "SUPERKIT · $2.25 USD · 0 ERRORS + 3D WELL", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "44", gain_db: -3}

      - id: reto01-04
        say: "One minute faster, zero console errors, and deeper relativistic geometry: point one goes to the Superpowers Kit."
        show:
          - split:
              flash: {clip: galaxia_nbody, t: 6.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: galaxia_nbody, t: 24.0, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "point"
            transition: flash
            p:
              winner: argon
              headline: "3D GRAVITY WELL & ZERO ERRORS"
              reason: "44 min ($2.25) vs 45 min ($1.26) · 0 console errors & deeper 3D spacetime curvature"
              score: {flash: 0, argon: 1}
        score: {flash: 0, argon: 1}
        score_at: "point"

  # ===============================================================================================
  # SCENE 05: LEVEL 2 — ZERO-GC HFT TRADING TERMINAL (SUPERKIT WINS: 0 - 2)
  # ===============================================================================================
  - id: reto02
    chapter: "Level 2: Zero-GC HFT Trading Terminal"
    music: {cue: bed, gain_db: 0}
    hud: {reto: 2, total: 6, title: "HFT TRADING TERMINAL"}
    beats:
      - id: reto02-01
        say: "Level 2: an institutional high-frequency trading terminal processing thousands of orders per second with live depth book and liquidity heatmap."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 2, total: 6, world: "1-2", world_name: "SKILL 02 · ZERO-GC MEMORY", title: "HFT TRADING TERMINAL", subtitle: "70,406 orders/s, Float32Array RingBuffer & depth heatmap", times: {flash: 73, argon: 57}}
          - clip: terminal_trading
            model: argon
            t: 18.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "with"

      - id: reto02-02
        say: "Here Raw AI hit its longest run of the tournament: taking 73 minutes to write nearly 3,900 lines for a dollar seventy-five, while topping out at 11 thousand orders per second."
        show:
          - clip: terminal_trading
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "73", dur: 1.8, p: {from: 0, to: 73, suffix: "MIN", label: "RAW AI · $1.75 USD · 11,073 ORD/S", color: FLASH, accent: FLASH}}

      - id: reto02-03
        say: "Meanwhile, the Zero-GC architecture skills guided the Superkit to finish in 57 minutes for a dollar fifty-six, hitting a massive 70 thousand 406 orders per second."
        transition: flash
        show:
          - clip: terminal_trading
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "57", dur: 1.8, p: {from: 0, to: 57, suffix: "MIN", label: "SUPERKIT · $1.56 USD · 70,406 ORD/S (6.3X)", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "57", gain_db: -4}

      - id: reto02-04
        say: "Sixteen minutes faster, cheaper in tokens, and over six times higher order throughput: the Superpowers Kit takes a two to zero lead."
        show:
          - split:
              flash: {clip: terminal_trading, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: terminal_trading, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "two"
            transition: flash
            p:
              winner: argon
              headline: "6.3X HIGHER THROUGHPUT & CHEAPER"
              reason: "57 min ($1.56) vs 73 min ($1.75) · 70,406 vs 11,073 ord/s with Zero-GC buffers"
              score: {flash: 0, argon: 2}
        score: {flash: 0, argon: 2}
        score_at: "two"

  # ===============================================================================================
  # SCENE 06: LEVEL 3 — BULLET-HELL ARCADE BOSS RUSH (RAW AI WINS: 1 - 2)
  # ===============================================================================================
  - id: reto03
    chapter: "Level 3: Bullet-Hell Arcade Boss Rush"
    music: {cue: tension, gain_db: 0}
    hud: {reto: 3, total: 6, title: "ARCADE BOSS RUSH"}
    beats:
      - id: reto03-01
        say: "Level 3: a Bullet-Hell Arcade Boss Rush with a three-phase biomechanical boss, thousands of simultaneous projectiles, continuous collision detection, and synth audio."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 3, total: 6, world: "2-1", world_name: "ROUND 03 · DANMAKU & WEB AUDIO", title: "ARCADE BOSS RUSH", subtitle: "TypedArray bullet pool, Spatial Hash & FM synth soundtrack", times: {flash: 51, argon: 69}}
          - clip: arcade_boss_rush
            model: flash
            t: 4.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "thousands"

      - id: reto03-02
        say: "And here came the first surprise: Raw Gemini 4 Argon High already masters TypedArrays natively, finishing in 51 minutes for a dollar sixty-four and unleashing 379-bullet spirals at 61 frames per second."
        show:
          - clip: arcade_boss_rush
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "51", dur: 1.8, p: {from: 0, to: 51, suffix: "MIN", label: "RAW AI · $1.64 USD · 379 ACTIVE BULLETS", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "51", gain_db: -4}

      - id: reto03-03
        say: "With the Superpowers Kit, the overhead of reading five skills and iterating on memory stretched delivery to 69 minutes with a more conservative 96-bullet pattern."
        transition: flash
        show:
          - clip: arcade_boss_rush
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "69", dur: 1.8, p: {from: 0, to: 69, suffix: "MIN", label: "SUPERKIT · $1.68 USD · 96 ACTIVE BULLETS", color: ARGON, accent: ARGON}}

      - id: reto03-04
        say: "Eighteen minutes faster with four times denser bullet curtains: Raw AI earns its first point and cuts the lead to one to two."
        show:
          - split:
              flash: {clip: arcade_boss_rush, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: arcade_boss_rush, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "first"
            transition: flash
            p:
              winner: flash
              headline: "RAW AI WINS IN SPEED & DANMAKU DENSITY"
              reason: "51 min ($1.64) vs 69 min ($1.68) · 379 spiral bullets at 61 FPS & 18 min faster"
              score: {flash: 1, argon: 2}
        score: {flash: 1, argon: 2}
        score_at: "first"

  # ===============================================================================================
  # SCENE 07: LEVEL 4 — 3D ZERO-TRUST CYBER DEFENSE (RAW AI WINS: 2 - 2 TIE)
  # ===============================================================================================
  - id: reto04
    chapter: "Level 4: 3D Zero-Trust Cyber Defense"
    music: {cue: battle, gain_db: 0}
    hud: {reto: 4, total: 6, title: "3D ZERO-TRUST GRID"}
    beats:
      - id: reto04-01
        say: "Level 4: a Zero-Trust cybersecurity command center that inspects cryptographic packets and neutralizes live DDoS floods and SQL injections."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 4, total: 6, world: "2-2", world_name: "ROUND 04 · ONE-SHOT EFFICIENCY", title: "3D ZERO-TRUST GRID", subtitle: "3D holographic globe, mTLS inspection & DDoS quarantine", times: {flash: 24, argon: 43}}
          - clip: red_zero_trust
            model: flash
            t: 4.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "neutralizes"

      - id: reto04-02
        say: "Here Raw AI put on an efficiency clinic: in just 5 agent steps and 24 minutes, it built the 3D defense globe with floating node labels for only 74 cents."
        show:
          - clip: red_zero_trust
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "24", dur: 1.8, p: {from: 0, to: 24, suffix: "MIN", label: "RAW AI · $0.74 USD · ONLY 5 AGENT STEPS", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "74", gain_db: -3}

      - id: reto04-03
        say: "Meanwhile, the Superkit's mandatory verification protocol ran 32 agent steps, taking 43 minutes and 2 dollars and 4 cents to reach the same 60 frames per second."
        transition: flash
        show:
          - clip: red_zero_trust
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "43", dur: 1.8, p: {from: 0, to: 43, suffix: "MIN", label: "SUPERKIT · $2.04 USD · 32 AGENT STEPS", color: ARGON, accent: ARGON}}

      - id: reto04-04
        say: "Nearly twice as fast and 64 percent cheaper in tokens: Raw AI wins round four and ties the tournament at two apiece."
        show:
          - split:
              flash: {clip: red_zero_trust, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: red_zero_trust, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "ties"
            transition: flash
            p:
              winner: flash
              headline: "2 - 2 TIE · 5-STEP ONE-SHOT EFFICIENCY"
              reason: "23.5 min ($0.74, 190K tok) vs 42.8 min ($2.04, 2.59M tok) · Floating 3D node labels"
              score: {flash: 2, argon: 2}
        score: {flash: 2, argon: 2}
        score_at: "ties"

  # ===============================================================================================
  # SCENE 08: LEVEL 5 — AI AGENT NODE ENGINE (SUPERKIT WINS: 2 - 3)
  # ===============================================================================================
  - id: reto05
    chapter: "Level 5: AI Node & GLSL Shader Studio (DAG)"
    music: {cue: bed, gain_db: 0}
    hud: {reto: 5, total: 6, title: "AI NODE ENGINE DAG"}
    beats:
      - id: reto05-01
        say: "Level 5: a visual multi-agent workflow engine with Bezier cables, parallel topological execution, and infinite-cycle detection."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 5, total: 6, world: "3-1", world_name: "SKILL 05 · DAG GRAPHS & GLSL", title: "AI NODE ENGINE", subtitle: "Kahn topological compiler, Bezier wires & 3D Raymarching", times: {flash: 55, argon: 47}}
          - clip: motor_nodos_ia
            model: argon
            t: 18.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "parallel"

      - id: reto05-02
        say: "With the match tied, we raised the architectural complexity: without the kit, Raw AI took 55 minutes wiring the DAG compiler to the WebGL viewport across 8 Bezier cables."
        show:
          - clip: motor_nodos_ia
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "55", dur: 1.8, p: {from: 0, to: 55, suffix: "MIN", label: "RAW AI · $1.58 USD · 8 DAG CABLES", color: FLASH, accent: FLASH}}

      - id: reto05-03
        say: "Here the Superpowers Kit templates shone again: solving the topological compiler in 47 minutes with a cleaner 10-cable graph and a 4D Fresnel Raymarching shader."
        transition: flash
        show:
          - clip: motor_nodos_ia
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [100, 56, 1720, 968]
        gfx:
          - {kind: counter, at: "47", dur: 1.8, p: {from: 0, to: 47, suffix: "MIN", label: "SUPERKIT · $1.72 USD · 10 CABLES + 4D FRESNEL", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "47", gain_db: -3}

      - id: reto05-04
        say: "Eight minutes faster with a cleaner node layout: the Superpowers Kit breaks the tie and takes a three to two lead."
        show:
          - split:
              flash: {clip: motor_nodos_ia, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: motor_nodos_ia, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "breaks"
            transition: flash
            p:
              winner: argon
              headline: "10-CABLE DAG & 4D RAYMARCHING STUDIO"
              reason: "47 min ($1.72) vs 55 min ($1.58) · 8 min faster & cleaner topological layout"
              score: {flash: 2, argon: 3}
        score: {flash: 2, argon: 3}
        score_at: "breaks"

  # ===============================================================================================
  # SCENE 09: LEVEL 6 — MIXIUHOS WEB DESKTOP (SUPERKIT WINS: 2 - 4 FINAL)
  # ===============================================================================================
  - id: reto06
    chapter: "Level 6: MixiuhOS Web Desktop"
    music: {cue: battle, gain_db: 0}
    hud: {reto: 6, total: 6, title: "MIXIUH OS DESKTOP"}
    beats:
      - id: reto06-01
        say: "Final level: build a complete Web Operating System with a window manager, virtual filesystem, interactive bash terminal, code editor, and live process monitor."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 6, total: 6, world: "3-2", world_name: "INFINITE MEMORY + AUTO-DEBUGGER", title: "MIXIUH OS DESKTOP", subtitle: "Window manager & 4 live apps: WebGL, Synth, Terminal & Kernel", times: {flash: 29, argon: 42}}
          - clip: mixiuh_os_desktop
            model: argon
            t: 18.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "interactive"

      - id: reto06-02
        say: "Without the kit, Raw AI finished quickly in 29 minutes for 72 cents, but without browser inspection it left the terminal ASCII art squished on one line and omitted 3D geometry controls."
        show:
          - clip: mixiuh_os_desktop
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "29", dur: 1.8, p: {from: 0, to: 29, suffix: "MIN", label: "RAW AI · $0.72 USD · SQUISHED ASCII ART", color: FLASH, accent: FLASH}}

      - id: reto06-03
        say: "The Superpowers Kit spent 42 minutes and a dollar sixty using its Browser Auto-Debugger to inspect the DOM, polishing the multi-line neofetch banner, 3D presets, and synth knobs."
        transition: flash
        show:
          - clip: mixiuh_os_desktop
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "42", dur: 1.8, p: {from: 0, to: 42, suffix: "MIN", label: "SUPERKIT · $1.60 USD · 4 VERIFIED APPS", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "42", gain_db: -3}

      - id: reto06-04
        say: "When you integrate four live subsystems inside one desktop, browser verification makes all the difference: final victory four to two for the Mixiuh Superpowers Kit."
        show:
          - split:
              flash: {clip: mixiuh_os_desktop, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: mixiuh_os_desktop, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "four"
            transition: flash
            p:
              winner: argon
              headline: "4 - 2 VICTORY FOR THE SUPERPOWERS KIT"
              reason: "42 min ($1.60) vs 29 min ($0.72) · Auto-Debugger polished all 4 sub-apps & MEMORY.md"
              score: {flash: 2, argon: 4}
        score: {flash: 2, argon: 4}
        score_at: "four"

  # ===============================================================================================
  # SCENE 10: FINAL SCOREBOARD & HONEST VERDICT
  # ===============================================================================================
  - id: resultados
    chapter: "Real verdict: when to use the Kit and when not to"
    music: {cue: results, gain_db: 0}
    hud: false
    beats:
      - id: resultados-01
        say: "Four to two on the final scoreboard: a one hundred percent real benchmark that proves both the raw power of Gemini 4 Argon High and the engineering edge of the Superpowers Kit."
        post: 2.8
        transition: flash
        show:
          - {clip: galaxia_nbody, model: argon, t: 24.0, rate: 1.0, roi: [0, 0, 1920, 1080]}
          - {clip: mixiuh_os_desktop, model: argon, t: 24.0, rate: 1.0, roi: [0, 0, 1920, 1080]}
          - card: scoreboard_card
            cut_at: "real"
            p:
              title: "REAL SCORE · EPISODE 03 (4 - 2)"
              rows:
                - {n: 1, title: "3D N-Body Galaxy Simulator", winner: argon, flash_min: 45, argon_min: 44}
                - {n: 2, title: "Zero-GC HFT Trading Terminal", winner: argon, flash_min: 73, argon_min: 57}
                - {n: 3, title: "Bullet-Hell Arcade Boss Rush", winner: flash, flash_min: 51, argon_min: 69}
                - {n: 4, title: "3D Zero-Trust Cyber Defense", winner: flash, flash_min: 24, argon_min: 43}
                - {n: 5, title: "AI Node & GLSL Shader Studio", winner: argon, flash_min: 55, argon_min: 47}
                - {n: 6, title: "MixiuhOS Web Desktop", winner: argon, flash_min: 29, argon_min: 42}
        sfx:
          - {name: powerup, at: 0.05, gain_db: -4}

      - id: resultados-02
        say: "On the total stopwatch, Raw AI totaled 276 minutes versus 302 minutes for the Superkit, which finished faster on the hardest architectures while investing extra time in browser QA."
        show:
          - card: timer_race
            p: {flash: 276, argon: 302, title: "TOTAL TIME · 6 REAL SYSTEMS", ratio_text: "RAW AI: 276 MIN · SUPERKIT: 302 MIN (FASTER IN HFT & DAG)"}

      - id: resultados-03
        say: "In technical quality, the Superpowers Kit eliminated the only console error in the tournament, delivered 6.3 times higher HFT order throughput, and maintained persistent memory logs."
        post: 0.4
        show:
          - card: stats_card
            p:
              title: "HEADLESS CHROME TECHNICAL AUDIT"
              rows:
                - {label: "HFT THROUGHPUT (R2)", flash: "11,073 ORD/S", argon: "70,406 ORD/S", better: argon}
                - {label: "CONSOLE ERRORS", flash: "1 ERROR 404", argon: "0 ERRORS", better: lower}

      - id: resultados-04
        say: "And the API bill reveals the key trade-off: 7 dollars and 69 cents across 6.1 million tokens raw, versus 10 dollars and 85 cents across 13.2 million tokens with Skills and Auto-Debugging."
        post: 0.8
        show:
          - card: stats_card
            p:
              title: "REAL API TOKEN BILL (USD)"
              rows:
                - {label: "TOTAL TOKENS", flash: "6.12M TOK", argon: "13.20M TOK", better: flash}
                - {label: "TOTAL API COST", flash: "$7.69 USD", argon: "$10.85 USD", better: flash}
        sfx:
          - {name: coin, at: "7", gain_db: -3}

  # ===============================================================================================
  # SCENE 11: FINAL VERDICT & FREE SUPERKIT DOWNLOAD
  # ===============================================================================================
  - id: cierre
    chapter: "Conclusion: Do you still need Skills Kits today?"
    music: {cue: outro, gain_db: 0}
    hud: false
    beats:
      - id: cierre-01
        say: "The takeaway is crystal clear: before paying for a more expensive model, give your coding agent strict architectural rules, domain skills, and automated browser verification."
        transition: pixel_wipe
        show:
          - split:
              flash: {clip: galaxia_nbody, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: galaxia_nbody, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}

      - id: cierre-02
        say: "For single-shot prototypes, Raw Gemini 4 Argon High is already so strong that it saves tokens on its own; but for multi-layered production systems, the Superpowers Kit wins 4 to 2."
        captions: false
        show:
          - card: quote_card
            p:
              text: "On self-contained prototypes, Raw Gemini 4 Argon High saves 29% in tokens ($7.69 vs $10.85). On complex systems (HFT, DAG & Web OS), the Superpowers Kit wins 4-2 with 0 errors."
              author: "Real Benchmark Verdict · Mixiuh Labs"

      - id: cierre-03
        say: "I left all twelve interactive demos and the free Mixiuh Superpowers Kit download at labs dot mixiuh dot online, ready for Claude Code, Antigravity, and Cursor."
        show:
          - split:
              flash: {clip: arcade_boss_rush, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: arcade_boss_rush, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}
          - split:
              flash: {clip: mixiuh_os_desktop, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: mixiuh_os_desktop, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}
            cut_at: "download"

      - id: cierre-04
        say: "Subscribe to Mixiuh Labs, grab the free kit today, and tell me in the comments which multi-model tournament you want to see in Episode 04."
        transition: pixel_wipe
        show:
          - card: end_screen
            p: {headline: "Download the Free Superpowers Kit", sub: "labs.mixiuh.online · subscribe to Mixiuh Labs"}
        sfx:
          - {name: coin, at: 0.3, gain_db: -3}

  # ===============================================================================================
  # SCENE 12: ENDSCREEN
  # ===============================================================================================
  - id: endscreen
    music: {cue: outro, gain_db: 0}
    hud: false
    beats:
      - id: endscreen-01
        say: "Experiment 03 complete: see you in the next level, right here on Mixiuh Labs."
        dur: 11.0
        show:
          - continue: true
"""

(EP_ES_DIR / "episode.yaml").write_text(YAML_ES, encoding="utf-8")
(EP_EN_DIR / "episode.yaml").write_text(YAML_EN, encoding="utf-8")
print("Wrote:", EP_ES_DIR / "episode.yaml")
print("Wrote:", EP_EN_DIR / "episode.yaml")
