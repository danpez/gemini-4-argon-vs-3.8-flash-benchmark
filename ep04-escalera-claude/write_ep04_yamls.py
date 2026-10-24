#!/usr/bin/env python3
"""Genera episode.yaml para EP04 en Espanol (ep04-escalera-claude) e Ingles (ep04-escalera-claude-en)
con los datos reales del benchmark Claude Code CLI (Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5, marcador 3-2-1)."""
from pathlib import Path

ROOT = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs")
EP_ES_DIR = ROOT / "episodes" / "ep04-escalera-claude"
EP_EN_DIR = ROOT / "episodes" / "ep04-escalera-claude-en"
EP_ES_DIR.mkdir(parents=True, exist_ok=True)
EP_EN_DIR.mkdir(parents=True, exist_ok=True)

YAML_ES = """# EP04 - Escalera Completa de Claude: Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5 (Mixiuh Labs, episodio 04)
# Benchmark real ejecutado en claude CLI con esfuerzo alto (18 corridas aisladas = 6 retos x 3 niveles)
# HAIKU | SONNET (clave interna 'flash') a la izquierda en ambar (#FBBF24, sprite 'bolt')
# OPUS 5.5 (clave interna 'argon') a la derecha en violeta (#B794F6, sprite 'argon')
episode:
  id: ep04
  slug: claude-haiku-vs-sonnet-vs-opus-escalera
  title: "Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5: ¿En Qué Nivel Conviene Gastar Tu Dinero?"
  voice: {voice_id: a580803d-fac8-4eb5-8453-709a13418052, stability: 0.5, speed: 1.05, seed: 7}
  render: {res: 2160, fps: 60}
  models:
    flash: {name: "Claude Haiku & Sonnet 5.5", tag: "HAIKU | SONNET", color: "#FBBF24", side: left, sprite: "bolt"}
    argon: {name: "Claude Opus 5.5", tag: "OPUS 5.5", color: "#B794F6", side: right, sprite: "argon"}
  sources:
    rover_suspension: {file: "../../../ep04-escalera-claude/grabaciones/01_rover_suspension_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    slime_feromonas: {file: "../../../ep04-escalera-claude/grabaciones/02_slime_feromonas_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    puente_estructural: {file: "../../../ep04-escalera-claude/grabaciones/03_puente_estructural_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    sintetizador_acido_3d: {file: "../../../ep04-escalera-claude/grabaciones/04_sintetizador_acido_3d_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    pathtracer_bvh: {file: "../../../ep04-escalera-claude/grabaciones/05_pathtracer_bvh_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    consola_retro_cpu: {file: "../../../ep04-escalera-claude/grabaciones/06_consola_retro_cpu_comparativa.mov", content_box: [0, 0, 1920, 1080]}
  defaults: {pre: 0.0, post: 0.18, scene_tail: 0.35, transition: cut}
  captions: {plate: 0.88}
  pronunciations:
    "Haiku": "Jaiku"
    "Sonnet": "Sónet"
    "Opus": "Ópus"
    "Verlet": "Verlét"
    "Hooke": "Juk"
    "Physarum": "Fisárum"
    "XPBD": "equis pe be de"
    "TB-303": "te be trescientos tres"
    "TR-909": "te ere novecientos nueve"
    "BVH": "be ve ache"
    "CHIP-8": "chip ocho"
    "WebGL2": "Web G L dos"
  thumbnails:
    - id: A
      text: "$1.54 | $29.94"
      layout: split
      left: {clip: sintetizador_acido_3d, t: 6.0, roi: [240, 60, 880, 960]}
      right: {clip: sintetizador_acido_3d, t: 24.0, roi: [240, 60, 880, 960]}
    - id: B
      text: "HAIKU | OPUS"
      layout: split
      left: {clip: puente_estructural, t: 6.5, roi: [240, 60, 880, 960]}
      right: {clip: puente_estructural, t: 24.5, roi: [240, 60, 880, 960]}
    - id: C
      text: "3 | 2 | 1"
      layout: split
      left: {clip: consola_retro_cpu, t: 6.5, roi: [240, 60, 880, 960]}
      right: {clip: consola_retro_cpu, t: 24.5, roi: [240, 60, 880, 960]}
  youtube:
    titles:
      - "Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5: ¿Vale la Pena Pagar 20 Veces Más? (4K60)"
      - "Puse a Competir los 3 Niveles de Claude en 6 Retos Extremos ($1.54 vs $12.22 vs $29.94)"
      - "La Escalera Completa de Claude: Cuándo Usar Haiku, Sonnet u Opus para Programar"
    tags:
      - "Claude Haiku 5.5"
      - "Claude Sonnet 5.5"
      - "Claude Opus 5.5"
      - "Claude Code"
      - "comparativa Claude"
      - "programar con IA"
      - "Mixiuh Labs"
    links:
      - {label: "Probar las 18 demos interactivas reales del Episodio 04", url: "https://labs.mixiuh.online"}
      - {label: "Prompts exactos y telemetría de costos en Mixiuh Labs", url: "https://labs.mixiuh.online"}

scenes:

  # ===============================================================================================
  # ESCENA 01: HOOK
  # ===============================================================================================
  - id: hook
    chapter: "¿Vale la pena pagar 20 veces más por Claude Opus?"
    music: {cue: hook, gain_db: 0}
    hud: false
    beats:
      - id: hook-01
        say: "Un dólar con cincuenta y cuatro centavos por Haiku, doce dólares con veintidós por Sonnet y casi treinta dólares por Opus: ¿realmente vale la pena pagar veinte veces más al programar con Claude?"
        voice: {speed: 1.10}
        transition: cut
        show:
          - clip: rover_suspension
            model: argon
            t: 20.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
          - clip: sintetizador_acido_3d
            model: flash
            t: 5.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "doce"
            transition: glitch
        gfx:
          - {kind: big_text, at: "treinta", p: {text: "$1.54 HAIKU · $12.22 SONNET · $29.94 OPUS", color: FLASH, accent: ARGON, y: 780, size: 78}}
        sfx:
          - {name: select, at: "treinta", gain_db: -4}

      - id: hook-02
        say: "Corrimos dieciocho pruebas aisladas con los tres niveles de Claude 5.5 y pasó lo impensable: Opus dominó la primera mitad tres a cero, pero Haiku y Sonnet le arrebataron los últimos tres retos."
        voice: {speed: 1.10}
        transition: flash
        show:
          - clip: pathtracer_bvh
            model: flash
            t: 6.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: big_text, at: "impensable", p: {text: "OPUS 3 · SONNET 2 · HAIKU 1", color: WIN, accent: ARGON, y: 780, size: 96}}
        sfx:
          - {name: coin, at: "impensable", gain_db: -3}

      - id: hook-03
        say: "Hoy subimos la escalera completa de Claude en seis desafíos extremos para descubrir exactamente en qué nivel te conviene gastar tu dinero."
        voice: {speed: 1.10}
        show:
          - {clip: slime_feromonas, model: argon, t: 21.0, roi: [0, 0, 1920, 1080]}
          - {clip: puente_estructural, model: argon, t: 22.0, roi: [0, 0, 1920, 1080]}
          - {clip: consola_retro_cpu, model: flash, t: 6.0, roi: [0, 0, 1920, 1080]}
          - card: timer_race
            cut_at: "seis"
            p: {title: "TIEMPO TOTAL · 6 RETOS REALES", flash: 105, argon: 179, ratio_text: "HAIKU 87M ($1.54) · SONNET 105M ($12.22) · OPUS 179M ($29.94)"}
        gfx:
          - {kind: vs_badge, at: "seis", dur: 0.9, p: {x: 960, y: 598, beam: false}}
        sfx:
          - {name: powerup, at: "escalera", gain_db: -5}

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
  # ESCENA 03: REGLAS DE LA ESCALERA DE CLAUDE
  # ===============================================================================================
  - id: protocolo
    chapter: "Protocolo del torneo: Haiku vs Sonnet vs Opus"
    music: {cue: bed, gain_db: 0}
    hud: false
    beats:
      - id: protocolo-01
        say: "Soy Kevin, esto es Mixiuh Labs, y cada semana me preguntan si sigue teniendo sentido pagar la tarifa completa de Opus cuando Sonnet y Haiku son tan rápidos."
        transition: pixel_wipe
        show:
          - card: title_card
            p: {kicker: "TORNEO DE 18 EJECUCIONES REALES", title: "EXPERIMENTO 04", subtitle: "Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5"}
        gfx:
          - {kind: lower_third, at: 0.35, p: {title: "Kevin González", subtitle: "Arquitecto del torneo · Mixiuh Labs"}}
        sfx:
          - {name: blip, at: "Mixiuh", gain_db: -6}

      - id: protocolo-02
        say: "Para responder con datos reales, ejecutamos el mismo prompt en un solo intento con los tres modelos: a la izquierda verás a Haiku y Sonnet lado a lado, y después a Opus a pantalla completa."
        show:
          - split:
              flash: {clip: puente_estructural, t: 6.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: puente_estructural, t: 24.0, rate: 1.0, roi: [240, 60, 1440, 960]}
        sfx:
          - {name: select, at: "mismo", gain_db: -6}
          - {name: select, at: "tres", gain_db: -6}

      - id: protocolo-03
        say: "La regla de arbitraje es estricta: evaluamos física real, ausencia de errores en consola y retorno de inversión por cada dólar consumido en la API."
        show:
          - card: rules_card
            p:
              title: "REGLAS DE LA ESCALERA CLAUDE"
              items: ["MISMO PROMPT · 1 SOLO INTENTO", "CALIDAD VISUAL VS COSTO REAL USD"]
              reveal_at: [0.4, 2.3]

      - id: protocolo-04
        say: "En total, Haiku terminó los seis retos en 87 minutos por un dólar cincuenta y cuatro, Sonnet en 105 minutos por doce dólares con veintidós, y Opus en 179 minutos por casi treinta dólares."
        show:
          - card: stats_card
            p:
              title: "FACTURA TOTAL DE LAS 18 CORRIDAS"
              rows:
                - {label: "HAIKU / SONNET", flash: "$1.54 / $12.22", argon: "$29.94 USD (OPUS)", better: flash}
                - {label: "TIEMPO TOTAL", flash: "87M / 105M", argon: "179 MIN (OPUS)", better: flash}

      - id: protocolo-05
        say: "Arranquemos con los seis retos extremos para ver dónde brilla y dónde tropieza cada nivel de Claude."
        transition: pixel_wipe
        show:
          - card: scoreboard_card
            p:
              title: "LOS 6 DESAFÍOS DE LA ESCALERA CLAUDE"
              total: false
              rows:
                - {n: 1, title: "Reto 1 · Rover Planetario con Suspensión Verlet"}
                - {n: 2, title: "Reto 2 · Bio-Red Physarum de 100K Agentes GPU"}
                - {n: 3, title: "Reto 3 · Puente Estructural con Fractura en Vivo"}
                - {n: 4, title: "Reto 4 · Estudio Ácido 3D TB-303 + TR-909"}
                - {n: 5, title: "Reto 5 · Path Tracer WebGL2 con BVH y Denoiser"}
                - {n: 6, title: "Reto 6 · Consola Retro CHIP-8 con CPU y Audio"}
        sfx:
          - {name: levelup, at: "seis", gain_db: -3}

  # ===============================================================================================
  # ESCENA 04: RETO 1 — ROVER PLANETARIO CON SUSPENSIÓN VERLET (GANA OPUS: 3-WAY 1-0-0)
  # ===============================================================================================
  - id: reto01
    chapter: "Reto 1: Rover Planetario con Suspensión Verlet"
    music: {cue: battle, gain_db: 0}
    hud: {reto: 1, total: 6, title: "ROVER SUSPENSIÓN VERLET"}
    beats:
      - id: reto01-01
        say: "Reto 1: construir un laboratorio de pruebas para un Rover marciano con chasis articulado, amortiguadores con ley de Hooke, terreno deformable y gráficas de telemetría en vivo."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 1, total: 6, world: "1-1", world_name: "RONDA 01 · FÍSICA VERLET Y HOOKE", title: "ROVER PLANETARIO 2D", subtitle: "Suspensión Rocker-Bogie, puente colgante y telemetría de resortes", times: {flash: 19, argon: 42}}
          - clip: rover_suspension
            model: argon
            t: 19.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "amortiguadores"

      - id: reto01-02
        say: "A la izquierda, Haiku sorprendió entregando un rover funcional a 60 cuadros en 19 minutos por solo 35 centavos; pero a la derecha, Sonnet gastó dos dólares y medio y truncó su código dejando la pantalla en negro."
        show:
          - clip: rover_suspension
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: stamp, at: "truncó", dur: 2.2, p: {text: "SONNET ROTO", color: FAIL, angle: -8, model: flash}}
          - {kind: counter, at: "35", dur: 1.8, p: {from: 0, to: 19, suffix: "MIN", label: "HAIKU $0.35 (60 FPS) · SONNET $2.51 ROTO", color: FLASH, accent: FLASH}}
        sfx:
          - {name: error, at: "truncó", gain_db: -3}

      - id: reto01-03
        say: "Cuando entra Opus 5.5, la diferencia de ingeniería es abismal: invirtió 42 minutos y 6 dólares con 81 centavos para construir un puente colgante de tablones, cráteres lunares, faro volumétrico y vectores de fuerza."
        transition: flash
        show:
          - clip: rover_suspension
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [100, 56, 1720, 968]
        gfx:
          - {kind: counter, at: "42", dur: 1.8, p: {from: 0, to: 42, suffix: "MIN", label: "OPUS 5.5 · $6.81 USD · PUENTE COLGANTE + FARO", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "42", gain_db: -3}

      - id: reto01-04
        say: "Aunque Haiku merece aplauso por funcionar por 35 centavos, la física de puente colgante y telemetría de Opus está en otra liga: primer punto para Opus 5.5."
        show:
          - split:
              flash: {clip: rover_suspension, t: 6.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: rover_suspension, t: 24.0, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "primer"
            transition: flash
            p:
              winner: argon
              headline: "PUNTO PARA OPUS 5.5 · PUENTE COLGANTE Y FARO"
              reason: "Opus ($6.81, 42m) entregó puente colgante y vectores · Haiku ($0.35) funcionó y Sonnet ($2.51) rompió JS"
              score: {flash: 0, argon: 1}
        score: {flash: 0, argon: 1}
        score_at: "primer"

  # ===============================================================================================
  # ESCENA 05: RETO 2 — BIO-RED PHYSARUM GPU (GANA OPUS: 3-WAY 2-0-0)
  # ===============================================================================================
  - id: reto02
    chapter: "Reto 2: Bio-Red Physarum de 100K Agentes GPU"
    music: {cue: bed, gain_db: 0}
    hud: {reto: 2, total: 6, title: "SLIME MOLD GPU"}
    beats:
      - id: reto02-01
        say: "Reto 2: simular un organismo biológico Physarum en WebGL2 donde decenas de miles de agentes en GPU trazan redes ferroviarias óptimas siguiendo rastros de feromonas."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 2, total: 6, world: "1-2", world_name: "RONDA 02 · SHADERS PING-PONG GPU", title: "SLIME MOLD PHYSARUM", subtitle: "60,000 agentes en GPU conectando la red ferroviaria de Tokio", times: {flash: 7, argon: 13}}
          - clip: slime_feromonas
            model: argon
            t: 19.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "trazan"

      - id: reto02-02
        say: "Aquí Haiku cobró apenas 6 centavos en 5 minutos, pero falló al compilar el shader GLSL asignando un vector de tres dimensiones a uno de cuatro; mientras que Sonnet logró 60 cuadros por 79 centavos pero saturó el centro en blanco."
        show:
          - clip: slime_feromonas
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: stamp, at: "falló", dur: 2.2, p: {text: "HAIKU GLSL ERROR", color: FAIL, angle: -8, model: flash}}
          - {kind: counter, at: "79", dur: 1.8, p: {from: 0, to: 7, suffix: "MIN", label: "HAIKU $0.06 ROTO · SONNET $0.79 (60 FPS)", color: FLASH, accent: FLASH}}
        sfx:
          - {name: error, at: "falló", gain_db: -3}

      - id: reto02-03
        say: "Opus 5.5 tardó 13 minutos y 2 dólares con 55 centavos para mapear 28 estaciones reales de la bahía de Tokio, desde Shinjuku hasta Yokohama, conectándolas con 60 mil agentes bioluminiscentes a 60 cuadros."
        transition: flash
        show:
          - clip: slime_feromonas
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "13", dur: 1.8, p: {from: 0, to: 13, suffix: "MIN", label: "OPUS 5.5 · $2.55 USD · 28 ESTACIONES TOKIO", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "13", gain_db: -4}

      - id: reto02-04
        say: "En shaders científicos con texturas flotantes ping-pong, Opus demuestra por qué es el modelo insignia y se pone dos a cero arriba."
        show:
          - split:
              flash: {clip: slime_feromonas, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: slime_feromonas, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "dos"
            transition: flash
            p:
              winner: argon
              headline: "PUNTO PARA OPUS 5.5 · RED DE TOKIO EN GPU"
              reason: "Opus ($2.55, 13.4m) mapeó 28 estaciones reales a 60 FPS · Haiku ($0.06) rompió el shader GLSL"
              score: {flash: 0, argon: 2}
        score: {flash: 0, argon: 2}
        score_at: "dos"

  # ===============================================================================================
  # ESCENA 06: RETO 3 — PUENTE ESTRUCTURAL CON FRACTURA (GANA OPUS: 3-WAY 3-0-0)
  # ===============================================================================================
  - id: reto03
    chapter: "Reto 3: Puente Estructural con Fractura en Vivo"
    music: {cue: tension, gain_db: 0}
    hud: {reto: 3, total: 6, title: "PUENTE ESTRUCTURAL"}
    beats:
      - id: reto03-01
        say: "Reto 3: un simulador de ingeniería civil donde los tres modelos debían construir un puente sobre un cañón, cruzar vehículos pesados y fracturar vigas cuando la tensión supera el límite elástico."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 3, total: 6, world: "2-1", world_name: "RONDA 03 · SOLVER XPBD Y TENSIÓN", title: "PUENTE ESTRUCTURAL", subtitle: "Mapa de calor de tensión, paso de tren pesado y colapso", times: {flash: 17, argon: 20}}
          - clip: puente_estructural
            model: argon
            t: 19.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "cruzar"

      - id: reto03-02
        say: "En esta ronda los tres modelos entregaron simuladores funcionales a 60 cuadros: Haiku resolvió la cercha Warren con un camión de 20 toneladas por 30 centavos, y Sonnet animó un tren de cuatro vagones por un dólar noventa y ocho."
        show:
          - clip: puente_estructural
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "30", dur: 1.8, p: {from: 0, to: 17, suffix: "MIN", label: "HAIKU $0.30 · SONNET $1.98 · AMBOS A 60 FPS", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "30", gain_db: -4}

      - id: reto03-03
        say: "Pero Opus 5.5, en 19 minutos y por 3 dólares con 58 centavos, programó un solver XPBD de 20 sub-pasos con el porcentaje exacto de esfuerzo impreso sobre cada viga, pilares submarinos y deflexión en milímetros."
        transition: flash
        show:
          - clip: puente_estructural
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "20", dur: 1.8, p: {from: 0, to: 20, suffix: "MIN", label: "OPUS 5.5 · $3.58 USD · XPBD 20 SUB-PASOS", color: ARGON, accent: ARGON}}

      - id: reto03-04
        say: "Por su precisión de grado CAD con etiquetas de estrés en cada barra, Opus gana su tercer punto consecutivo; pero cuidado, porque a partir de aquí todo cambia."
        show:
          - split:
              flash: {clip: puente_estructural, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: puente_estructural, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "tercer"
            transition: flash
            p:
              winner: argon
              headline: "PUNTO PARA OPUS 5.5 · TELEMETRÍA CAD XPBD"
              reason: "Opus ($3.58, 19.7m) mostró % de estrés por viga · Haiku ($0.30) y Sonnet ($1.98) también cumplieron"
              score: {flash: 0, argon: 3}
        score: {flash: 0, argon: 3}
        score_at: "tercer"

  # ===============================================================================================
  # ESCENA 07: RETO 4 — ESTUDIO ÁCIDO 3D TB-303 + TR-909 (GANA HAIKU: 3-WAY 3-0-1)
  # ===============================================================================================
  - id: reto04
    chapter: "Reto 4: Estudio Ácido 3D TB-303 + TR-909"
    music: {cue: battle, gain_db: -6}
    hud: {reto: 4, total: 6, title: "SINTETIZADOR ÁCIDO 3D"}
    beats:
      - id: reto04-01
        say: "Reto 4: un estudio musical Acid Techno con sintetizador TB-303, caja de ritmos TR-909 en Web Audio API, perillas de corte y distorsión, y un túnel 3D reactivo al espectro."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 4, total: 6, world: "2-2", world_name: "RONDA 04 · WEB AUDIO Y SHADERS 3D", title: "ESTUDIO ÁCIDO 3D", subtitle: "Secuenciador TB-303 + TR-909, filtro resonante y túnel FFT 3D", times: {flash: 9, argon: 31}}
          - clip: sintetizador_acido_3d
            model: flash
            t: 4.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "perillas"
        project_audio:
          wav: "../../../ep04-escalera-claude/grabaciones/04_sintetizador_acido_3d_audio.wav"
          t0: 0.0
          gain_db: -5.0

      - id: reto04-02
        say: "Y aquí llegó el batacazo del torneo: en apenas 8 minutos y medio y por solo 21 centavos de dólar, Claude Haiku 5.5 construyó un terreno espectral 3D de partículas, osciloscopio, 7 perillas giratorias y el secuenciador completo a 61 cuadros."
        show:
          - clip: sintetizador_acido_3d
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        project_audio:
          wav: "../../../ep04-escalera-claude/grabaciones/04_sintetizador_acido_3d_audio.wav"
          t0: 5.0
          gain_db: -4.5
        gfx:
          - {kind: counter, at: "21", dur: 1.8, p: {from: 0, to: 9, suffix: "MIN", label: "HAIKU 5.5 · $0.21 USD · 61 FPS + AUDIO REAL", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "21", gain_db: -3}

      - id: reto04-03
        say: "Sonnet entregó un domo wireframe por un dólar cincuenta y dos y Opus una autopista láser increíble, pero Opus tardó 31 minutos y cobró 5 dólares exactos: veinticuatro veces más caro que Haiku para la misma fluidez."
        transition: flash
        show:
          - clip: sintetizador_acido_3d
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        project_audio:
          wav: "../../../ep04-escalera-claude/grabaciones/04_sintetizador_acido_3d_audio.wav"
          t0: 19.0
          gain_db: -4.5
        gfx:
          - {kind: counter, at: "31", dur: 1.8, p: {from: 0, to: 31, suffix: "MIN", label: "OPUS 5.5 · $5.00 USD (24X MÁS CARO QUE HAIKU)", color: ARGON, accent: ARGON}}

      - id: reto04-04
        say: "Tres veces y media más rápido y veinticuatro veces más barato sin sacrificar ni un cuadro por segundo: punto histórico para Claude Haiku 5.5."
        show:
          - split:
              flash: {clip: sintetizador_acido_3d, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: sintetizador_acido_3d, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "punto"
            transition: flash
            p:
              winner: flash
              headline: "PUNTO PARA HAIKU 5.5 · 61 FPS POR $0.21"
              reason: "Haiku ($0.21, 8.7m) logró 61 FPS con 3D + TB-303 + 909 costando 24x menos que Opus ($5.00, 31m)"
              score: {flash: 1, argon: 3}
        score: {flash: 1, argon: 3}
        score_at: "punto"

  # ===============================================================================================
  # ESCENA 08: RETO 5 — PATH TRACER WEBGL2 BVH (GANA SONNET: 3-WAY 3-1-1)
  # ===============================================================================================
  - id: reto05
    chapter: "Reto 5: Path Tracer WebGL2 con BVH y Denoiser"
    music: {cue: bed, gain_db: 0}
    hud: {reto: 5, total: 6, title: "PATH TRACER WEBGL2"}
    beats:
      - id: reto05-01
        say: "Reto 5: programar desde cero un motor de Path Tracing Monte Carlo en WebGL2 con árbol BVH, refracción en cristal, cáusticas y filtro Denoiser Á-Trous en tiempo real."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 5, total: 6, world: "3-1", world_name: "RONDA 05 · RAY TRACING MONTE CARLO", title: "PATH TRACER WEBGL2", subtitle: "Acumulación temporal, dispersión cromática y Denoiser Á-Trous", times: {flash: 14, argon: 31}}
          - clip: pathtracer_bvh
            model: flash
            t: 6.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "refracción"

      - id: reto05-02
        say: "A la izquierda, Haiku armó un trazador básico por 13 centavos con bastante grano; pero a la derecha, Claude Sonnet 5.5 brilló en solo 13 minutos con 9 por un dólar sesenta y siete, renderizando dispersión arcoíris en cristal a 29 cuadros por segundo."
        show:
          - clip: pathtracer_bvh
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "29", dur: 1.8, p: {from: 0, to: 14, suffix: "MIN", label: "SONNET 5.5 · $1.67 USD · 29 FPS + ARCOÍRIS", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "29", gain_db: -3}

      - id: reto05-03
        say: "En cambio, Opus 5.5 tardó más del doble —31 minutos y 5 dólares con 5 centavos— y su shader resultó tan pesado que cayó a solo 15 cuadros por segundo."
        transition: flash
        show:
          - clip: pathtracer_bvh
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [100, 56, 1720, 968]
        gfx:
          - {kind: counter, at: "15", dur: 1.8, p: {from: 0, to: 31, suffix: "MIN", label: "OPUS 5.5 · $5.05 USD · CAE A 15 FPS", color: ARGON, accent: ARGON}}

      - id: reto05-04
        say: "Casi el doble de cuadros por segundo, en menos de la mitad de tiempo y por un tercio del costo: victoria contundente para Claude Sonnet 5.5."
        show:
          - split:
              flash: {clip: pathtracer_bvh, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: pathtracer_bvh, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "victoria"
            transition: flash
            p:
              winner: flash
              headline: "PUNTO PARA SONNET 5.5 · 29 FPS Y ARCOÍRIS"
              reason: "Sonnet ($1.67, 13.9m) duplicó los FPS de Opus ($5.05, 31.4m, 15 FPS) con dispersión cromática"
              score: {flash: 2, argon: 3}
        score: {flash: 2, argon: 3}
        score_at: "victoria"

  # ===============================================================================================
  # ESCENA 09: RETO 6 — CONSOLA RETRO CHIP-8 CPU (GANA SONNET: 3-WAY 3-2-1 FINAL)
  # ===============================================================================================
  - id: reto06
    chapter: "Reto 6: Consola Retro CHIP-8 con CPU y Audio"
    music: {cue: battle, gain_db: -5}
    hud: {reto: 6, total: 6, title: "CONSOLA RETRO CHIP-8"}
    beats:
      - id: reto06-01
        say: "Reto final: construir un emulador y estudio de desarrollo para la consola clásica CHIP-8 con CPU de 35 opcodes, monitor CRT de fósforo, desensamblador en vivo, volcado hexadecimal y compilador."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 6, total: 6, world: "3-2", world_name: "RONDA 06 · EMULADOR CPU Y COMPILADOR", title: "CONSOLA RETRO CHIP-8", subtitle: "CPU 35 opcodes, monitor CRT curvo, desensamblador y 4 ROMs", times: {flash: 35, argon: 42}}
          - clip: consola_retro_cpu
            model: flash
            t: 5.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "desensamblador"
        project_audio:
          wav: "../../../ep04-escalera-claude/grabaciones/06_consola_retro_cpu_audio.wav"
          t0: 0.0
          gain_db: -6.0

      - id: reto06-02
        say: "Miren la pantalla dividida: tanto Haiku por 48 centavos como Sonnet por 3 dólares con 75 arrancaron jugando Pong en automático a 60 cuadros, y Sonnet incluyó CRT curvo, barras de registros y editor con sintaxis coloreada."
        show:
          - clip: consola_retro_cpu
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        project_audio:
          wav: "../../../ep04-escalera-claude/grabaciones/06_consola_retro_cpu_audio.wav"
          t0: 6.0
          gain_db: -5.5
        gfx:
          - {kind: counter, at: "60", dur: 1.8, p: {from: 0, to: 35, suffix: "MIN", label: "HAIKU $0.48 Y SONNET $3.75 · PONG EN VIVO 60 FPS", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "60", gain_db: -3}

      - id: reto06-03
        say: "Y aquí vino el tropiezo más doloroso de Opus 5.5: tras 42 minutos y casi 7 dólares en tokens, olvidó invocar el ensamblador al iniciar, dejando la ROM en cero bytes y la pantalla apagada."
        transition: flash
        show:
          - clip: consola_retro_cpu
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: stamp, at: "olvidó", dur: 2.3, p: {text: "BUG ROM 0 BYTES", color: FAIL, angle: -8, model: argon}}
          - {kind: counter, at: "42", dur: 1.8, p: {from: 0, to: 42, suffix: "MIN", label: "OPUS 5.5 · $6.93 USD · ROM 0 B AL ARRANCAR", color: ARGON, accent: ARGON}}
        sfx:
          - {name: error, at: "olvidó", gain_db: -3}

      - id: reto06-04
        say: "Sonnet 5.5 se lleva el último punto con una consola impecable, dejando el marcador final de la escalera en tres puntos para Opus, dos para Sonnet y uno para Haiku."
        show:
          - split:
              flash: {clip: consola_retro_cpu, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: consola_retro_cpu, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "último"
            transition: flash
            p:
              winner: flash
              headline: "PUNTO PARA SONNET 5.5 · MARCADOR 3 - 2 - 1"
              reason: "Sonnet ($3.75) y Haiku ($0.48) arrancaron Pong a 60 FPS · Opus ($6.93) dejó la ROM en 0 bytes"
              score: {flash: 3, argon: 3}
        score: {flash: 3, argon: 3}
        score_at: "último"

  # ===============================================================================================
  # ESCENA 10: PANTALLA DE RESULTADOS Y GUÍA DE COMPRA
  # ===============================================================================================
  - id: resultados
    chapter: "Veredicto final: cuándo usar Haiku, Sonnet u Opus"
    music: {cue: results, gain_db: 0}
    hud: false
    beats:
      - id: resultados-01
        say: "Tres para Opus, dos para Sonnet y uno para Haiku: el experimento demuestra que pagar el modelo más caro no garantiza ganar todos los retos."
        post: 2.8
        transition: flash
        show:
          - {clip: rover_suspension, model: argon, t: 24.0, rate: 1.0, roi: [0, 0, 1920, 1080]}
          - {clip: consola_retro_cpu, model: flash, t: 6.0, rate: 1.0, roi: [0, 0, 1920, 1080]}
          - card: scoreboard_card
            cut_at: "experimento"
            p:
              title: "MARCADOR FINAL · OPUS 3 · SONNET 2 · HAIKU 1"
              rows:
                - {n: 1, title: "Rover Planetario Verlet (Gana Opus)", winner: argon, flash_min: 19, argon_min: 42}
                - {n: 2, title: "Bio-Red Physarum GPU (Gana Opus)", winner: argon, flash_min: 7, argon_min: 13}
                - {n: 3, title: "Puente Estructural XPBD (Gana Opus)", winner: argon, flash_min: 17, argon_min: 20}
                - {n: 4, title: "Estudio Ácido 3D $0.21 (Gana Haiku)", winner: flash, flash_min: 9, argon_min: 31}
                - {n: 5, title: "Path Tracer WebGL2 29 FPS (Gana Sonnet)", winner: flash, flash_min: 14, argon_min: 31}
                - {n: 6, title: "Consola Retro CHIP-8 (Gana Sonnet)", winner: flash, flash_min: 35, argon_min: 42}
        sfx:
          - {name: powerup, at: 0.05, gain_db: -4}

      - id: resultados-02
        say: "En el cronómetro total, Haiku completó el torneo en 87 minutos y Sonnet en 105, mientras que Opus necesitó 179 minutos, casi tres horas de cómputo."
        show:
          - card: timer_race
            p: {flash: 105, argon: 179, title: "TIEMPO TOTAL · 6 RETOS REALES", ratio_text: "HAIKU: 87 MIN · SONNET: 105 MIN · OPUS: 179 MIN"}

      - id: resultados-03
        say: "En estabilidad, ningún nivel fue infalible en un solo intento: Haiku falló un shader, Sonnet truncó un archivo y Opus olvidó auto-ensamblar la ROM del último reto tras gastar casi siete dólares."
        post: 0.4
        show:
          - card: stats_card
            p:
              title: "AUDITORÍA REAL EN CHROME (18 DEMOS)"
              rows:
                - {label: "DEMOS FUNCIONALES", flash: "5/6 HAIKU · 5/6 SONNET", argon: "5/6 OPUS 5.5", better: flash}
                - {label: "MEJOR ROI DEL TORNEO", flash: "HAIKU $0.21 (61 FPS)", argon: "OPUS $2.55 (TOKIO)", better: flash}

      - id: resultados-04
        say: "Pero la tabla de costos lo cambia todo: un dólar con cincuenta y cuatro centavos por todo el torneo en Haiku, doce dólares con veintidós en Sonnet y veintinueve dólares con noventa y cuatro en Opus."
        post: 0.8
        show:
          - card: stats_card
            p:
              title: "FACTURA REAL API (6 RETOS COMPLETOS)"
              rows:
                - {label: "CLAUDE HAIKU / SONNET", flash: "$1.54 / $12.22 USD", argon: "$29.94 USD (OPUS)", better: flash}
                - {label: "AHORRO VS OPUS 5.5", flash: "19.4X / 2.45X MENOS", argon: "PRECIO BASE 1.0X", better: flash}
        sfx:
          - {name: coin, at: "cincuenta", gain_db: -3}

  # ===============================================================================================
  # ESCENA 11: REGLA DE ORO Y CIERRE
  # ===============================================================================================
  - id: cierre
    chapter: "Regla de oro para elegir entre Haiku, Sonnet y Opus"
    music: {cue: outro, gain_db: 0}
    hud: false
    beats:
      - id: cierre-01
        say: "Aquí tienes la regla de oro para tu bolsillo: usa Haiku 5.5 para prototipos rápidos, interfaces y sintetizadores donde cuesta veinte veces menos."
        transition: pixel_wipe
        show:
          - split:
              flash: {clip: sintetizador_acido_3d, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: sintetizador_acido_3d, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}

      - id: cierre-02
        say: "Usa Sonnet 5.5 como tu caballo de batalla diario para emuladores, shaders optimizados y aplicaciones completas; y reserva Opus 5.5 únicamente para física multicapa y arquitectura pesada."
        captions: false
        show:
          - card: quote_card
            p:
              text: "Haiku ($1.54) resuelve el 80% de prototipos 20x más barato. Sonnet ($12.22) es el punto dulce diario en velocidad y FPS. Reserva Opus ($29.94) para física y arquitectura extrema."
              author: "Guía Real de Bolsillo · Mixiuh Labs"

      - id: cierre-03
        say: "Subí las dieciocho demos interactivas, los prompts exactos y la tabla de costos a labs punto mixiuh punto online para que compares los tres niveles en tu propio navegador."
        show:
          - split:
              flash: {clip: pathtracer_bvh, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: pathtracer_bvh, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}
          - split:
              flash: {clip: consola_retro_cpu, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: consola_retro_cpu, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}
            cut_at: "prompts"

      - id: cierre-04
        say: "Suscríbete a Mixiuh Labs, comparte este video con tu equipo y déjame en los comentarios qué otra familia de modelos quieres que pasemos por la escalera en el Episodio 05."
        transition: pixel_wipe
        show:
          - card: end_screen
            p: {headline: "Prueba las 18 demos en vivo", sub: "labs.mixiuh.online · suscríbete a Mixiuh Labs"}
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
        say: "Experimento 04 terminado: nos vemos en el siguiente nivel, aquí en Mixiuh Labs."
        dur: 11.0
        show:
          - continue: true
"""

YAML_EN = """# EP04 (English) - Full Claude Ladder: Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5 (Mixiuh Labs, episode 04, English version)
# Real benchmark executed in claude CLI with high effort (18 isolated runs = 6 challenges x 3 tiers)
# HAIKU | SONNET (internal key 'flash') on the left in amber (#FBBF24, sprite 'bolt')
# OPUS 5.5 (internal key 'argon') on the right in violet (#B794F6, sprite 'argon')
episode:
  id: ep04-en
  slug: claude-haiku-vs-sonnet-vs-opus-ladder-en
  title: "Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5: Which Tier Is Actually Worth Your Money?"
  lang: en
  voice: {voice_id: a580803d-fac8-4eb5-8453-709a13418052, language: en, stability: 0.5, speed: 1.10, seed: 7}
  render: {res: 2160, fps: 60}
  models:
    flash: {name: "Claude Haiku & Sonnet 5.5", tag: "HAIKU | SONNET", color: "#FBBF24", side: left, sprite: "bolt"}
    argon: {name: "Claude Opus 5.5", tag: "OPUS 5.5", color: "#B794F6", side: right, sprite: "argon"}
  sources:
    rover_suspension: {file: "../../../ep04-escalera-claude/grabaciones/01_rover_suspension_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    slime_feromonas: {file: "../../../ep04-escalera-claude/grabaciones/02_slime_feromonas_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    puente_estructural: {file: "../../../ep04-escalera-claude/grabaciones/03_puente_estructural_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    sintetizador_acido_3d: {file: "../../../ep04-escalera-claude/grabaciones/04_sintetizador_acido_3d_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    pathtracer_bvh: {file: "../../../ep04-escalera-claude/grabaciones/05_pathtracer_bvh_comparativa.mov", content_box: [0, 0, 1920, 1080]}
    consola_retro_cpu: {file: "../../../ep04-escalera-claude/grabaciones/06_consola_retro_cpu_comparativa.mov", content_box: [0, 0, 1920, 1080]}
  defaults: {pre: 0.0, post: 0.18, scene_tail: 0.35, transition: cut}
  captions: {plate: 0.88}
  pronunciations:
    "Haiku": "High koo"
    "Sonnet": "Sonnet"
    "Opus": "Oh pus"
    "Verlet": "Ver lay"
    "Hooke": "Hook"
    "Physarum": "Fy sarum"
    "XPBD": "X P B D"
    "TB-303": "T B three oh three"
    "TR-909": "T R nine oh nine"
    "BVH": "B V H"
    "CHIP-8": "Chip eight"
    "WebGL2": "Web G L two"
    "API": "A P I"
    "USD": "U S D"
  thumbnails:
    - id: A
      text: "$1.54 | $29.94"
      layout: split
      left: {clip: sintetizador_acido_3d, t: 6.0, roi: [240, 60, 880, 960]}
      right: {clip: sintetizador_acido_3d, t: 24.0, roi: [240, 60, 880, 960]}
    - id: B
      text: "HAIKU | OPUS"
      layout: split
      left: {clip: puente_estructural, t: 6.5, roi: [240, 60, 880, 960]}
      right: {clip: puente_estructural, t: 24.5, roi: [240, 60, 880, 960]}
    - id: C
      text: "3 | 2 | 1"
      layout: split
      left: {clip: consola_retro_cpu, t: 6.5, roi: [240, 60, 880, 960]}
      right: {clip: consola_retro_cpu, t: 24.5, roi: [240, 60, 880, 960]}
  youtube:
    titles:
      - "Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5: Is Opus Worth 20x the Price? (4K60)"
      - "I Tested All 3 Claude Tiers Across 6 Extreme Coding Challenges ($1.54 vs $12.22 vs $29.94)"
      - "The Full Claude Ladder: When to Use Haiku, Sonnet, or Opus for Coding"
    hook: "We ran 18 real isolated Claude Code benchmarks across all 3 tiers of Claude 5.5 (Haiku $1.54 vs Sonnet $12.22 vs Opus $29.94). Final score: Opus 3, Sonnet 2, Haiku 1."
    summary: "Is Claude Opus 5.5 really worth paying 20x more than Haiku 5.5 or 2.5x more than Sonnet 5.5? We ran 18 real isolated one-shot benchmarks in Claude Code CLI across 6 extreme physics, WebGL2, and CPU emulation challenges. Opus 5.5 swept the first three physics and multi-pass GPU simulations (3-0), but Haiku 5.5 stunned in Round 4 by building a 61 FPS 3D Acid Techno Studio for $0.21 vs Opus's $5.00, and Sonnet 5.5 won Rounds 5 and 6—doubling Opus's FPS in the WebGL2 Path Tracer (29 vs 15 FPS) and booting live Pong on a curved CRT CHIP-8 console while Opus ($6.93) left its initial ROM at 0 bytes."
    keywords: ["Claude Haiku 5.5", "Claude Sonnet 5.5", "Claude Opus 5.5", "Claude Code benchmark", "AI coding comparison"]
    tags:
      - "Claude Haiku 5.5"
      - "Claude Sonnet 5.5"
      - "Claude Opus 5.5"
      - "Claude Code"
      - "AI coding benchmark"
      - "Mixiuh Labs"
    hashtags: ["#ClaudeCode", "#ClaudeOpus", "#MixiuhLabs"]
    pinned_comment: "Test all 18 real interactive apps (Haiku vs Sonnet vs Opus) and inspect the exact prompts and token bills at https://labs.mixiuh.online — Which Claude tier is your daily driver?"
    tools:
      - "Voice: Voicefy, cloned voice running locally on Mac (narrated in English)."
      - "Editing and captions: Reelfy + Mixiuh Labs Studio (4K60 pipeline)."
      - "Music: original procedural chiptune generated by code."
      - "Stack: claude --model haiku/sonnet/opus --effort high (18 isolated runs)."
    language: "en"
    facts: false
    links:
      - {label: "Play all 18 real interactive demos from Episode 04", url: "https://labs.mixiuh.online"}
      - {label: "Exact prompts and API cost telemetry at Mixiuh Labs", url: "https://labs.mixiuh.online"}

scenes:

  # ===============================================================================================
  # SCENE 01: HOOK
  # ===============================================================================================
  - id: hook
    chapter: "Is Claude Opus really worth paying 20x more?"
    music: {cue: hook, gain_db: 0}
    hud: false
    beats:
      - id: hook-01
        say: "One dollar and fifty-four cents for Haiku, twelve dollars and twenty-two cents for Sonnet, and nearly thirty dollars for Opus: is it actually worth paying twenty times more when coding with Claude?"
        voice: {speed: 1.10}
        transition: cut
        show:
          - clip: rover_suspension
            model: argon
            t: 20.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
          - clip: sintetizador_acido_3d
            model: flash
            t: 5.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "twelve"
            transition: glitch
        gfx:
          - {kind: big_text, at: "thirty", p: {text: "$1.54 HAIKU · $12.22 SONNET · $29.94 OPUS", color: FLASH, accent: ARGON, y: 780, size: 78}}
        sfx:
          - {name: select, at: "thirty", gain_db: -4}

      - id: hook-02
        say: "We ran eighteen isolated benchmarks across all three tiers of Claude 5.5 and the unthinkable happened: Opus swept the first half three to zero, but Haiku and Sonnet stole the final three challenges."
        voice: {speed: 1.10}
        transition: flash
        show:
          - clip: pathtracer_bvh
            model: flash
            t: 6.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: big_text, at: "unthinkable", p: {text: "OPUS 3 · SONNET 2 · HAIKU 1", color: WIN, accent: ARGON, y: 780, size: 96}}
        sfx:
          - {name: coin, at: "unthinkable", gain_db: -3}

      - id: hook-03
        say: "Today we climb the entire Claude ladder across six extreme engineering challenges to find out exactly where you should spend your money."
        voice: {speed: 1.10}
        show:
          - {clip: slime_feromonas, model: argon, t: 21.0, roi: [0, 0, 1920, 1080]}
          - {clip: puente_estructural, model: argon, t: 22.0, roi: [0, 0, 1920, 1080]}
          - {clip: consola_retro_cpu, model: flash, t: 6.0, roi: [0, 0, 1920, 1080]}
          - card: timer_race
            cut_at: "six"
            p: {title: "TOTAL TIME · 6 REAL CHALLENGES", flash: 105, argon: 179, ratio_text: "HAIKU 87M ($1.54) · SONNET 105M ($12.22) · OPUS 179M ($29.94)"}
        gfx:
          - {kind: vs_badge, at: "six", dur: 0.9, p: {x: 960, y: 598, beam: false}}
        sfx:
          - {name: powerup, at: "ladder", gain_db: -5}

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
  # SCENE 03: CLAUDE LADDER PROTOCOL
  # ===============================================================================================
  - id: protocolo
    chapter: "Tournament protocol: Haiku vs Sonnet vs Opus"
    music: {cue: bed, gain_db: 0}
    hud: false
    beats:
      - id: protocolo-01
        say: "I'm Kevin, this is Mixiuh Labs, and every single week developers ask me whether it still makes sense to pay flagship Opus pricing when Sonnet and Haiku are so fast."
        transition: pixel_wipe
        show:
          - card: title_card
            p: {kicker: "18 REAL CLAUDE CLI RUNS", title: "EXPERIMENT 04", subtitle: "Claude Haiku 5.5 vs Sonnet 5.5 vs Opus 5.5"}
        gfx:
          - {kind: lower_third, at: 0.35, p: {title: "Kevin González", subtitle: "Tournament Referee · Mixiuh Labs"}}
        sfx:
          - {name: blip, at: "Mixiuh", gain_db: -6}

      - id: protocolo-02
        say: "To answer with hard data, we ran the exact same one-shot prompt across all three models: first you'll see Haiku and Sonnet side by side, followed by Opus in full screen."
        show:
          - split:
              flash: {clip: puente_estructural, t: 6.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: puente_estructural, t: 24.0, rate: 1.0, roi: [240, 60, 1440, 960]}
        sfx:
          - {name: select, at: "exact", gain_db: -6}
          - {name: select, at: "three", gain_db: -6}

      - id: protocolo-03
        say: "Our refereeing rule is strict: we score real physics accuracy, zero console errors, and return on investment per dollar spent on the API."
        show:
          - card: rules_card
            p:
              title: "CLAUDE LADDER RULES"
              items: ["SAME PROMPT · ONE SHOT ONLY", "VISUAL QUALITY VS REAL API COST"]
              reveal_at: [0.4, 2.3]

      - id: protocolo-04
        say: "In total, Haiku finished all six challenges in 87 minutes for a dollar fifty-four, Sonnet in 105 minutes for twelve dollars and twenty-two cents, and Opus in 179 minutes for nearly thirty dollars."
        show:
          - card: stats_card
            p:
              title: "TOTAL BILL ACROSS 18 RUNS"
              rows:
                - {label: "HAIKU / SONNET", flash: "$1.54 / $12.22", argon: "$29.94 USD (OPUS)", better: flash}
                - {label: "TOTAL TIME", flash: "87M / 105M", argon: "179 MIN (OPUS)", better: flash}

      - id: protocolo-05
        say: "Let's jump into all six extreme challenges to see where each tier of Claude shines and where it stumbles."
        transition: pixel_wipe
        show:
          - card: scoreboard_card
            p:
              title: "THE 6 CLAUDE LADDER CHALLENGES"
              total: false
              rows:
                - {n: 1, title: "Challenge 1 · Planetary Rover Verlet Suspension"}
                - {n: 2, title: "Challenge 2 · 100K-Agent GPU Physarum Bio-Network"}
                - {n: 3, title: "Challenge 3 · Structural Bridge Live Fracture"}
                - {n: 4, title: "Challenge 4 · 3D Acid Techno Studio TB-303 + 909"}
                - {n: 5, title: "Challenge 5 · WebGL2 BVH Path Tracer & Denoiser"}
                - {n: 6, title: "Challenge 6 · Retro CHIP-8 Console & Assembler"}
        sfx:
          - {name: levelup, at: "six", gain_db: -3}

  # ===============================================================================================
  # SCENE 04: CHALLENGE 1 — PLANETARY ROVER VERLET SUSPENSION (OPUS WINS: 3-WAY 1-0-0)
  # ===============================================================================================
  - id: reto01
    chapter: "Challenge 1: Planetary Rover Verlet Suspension"
    music: {cue: battle, gain_db: 0}
    hud: {reto: 1, total: 6, title: "ROVER VERLET SUSPENSION"}
    beats:
      - id: reto01-01
        say: "Challenge 1: build a Martian Rover suspension testbed with an articulated chassis, Hooke's law spring-dampers, deformable terrain, and live telemetry graphs."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 1, total: 6, world: "1-1", world_name: "ROUND 01 · VERLET & HOOKE PHYSICS", title: "2D PLANETARY ROVER", subtitle: "Rocker-Bogie suspension, plank bridge & spring telemetry", times: {flash: 19, argon: 42}}
          - clip: rover_suspension
            model: argon
            t: 19.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "Hooke's"

      - id: reto01-02
        say: "On the left, Haiku surprised us by delivering a working 60 FPS rover in 19 minutes for just 35 cents; but on the right, Sonnet spent two dollars and fifty-one cents and truncated its script, leaving a black screen."
        show:
          - clip: rover_suspension
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: stamp, at: "truncated", dur: 2.2, p: {text: "SONNET BROKEN", color: FAIL, angle: -8, model: flash}}
          - {kind: counter, at: "35", dur: 1.8, p: {from: 0, to: 19, suffix: "MIN", label: "HAIKU $0.35 (60 FPS) · SONNET $2.51 BROKEN", color: FLASH, accent: FLASH}}
        sfx:
          - {name: error, at: "truncated", gain_db: -3}

      - id: reto01-03
        say: "When Opus 5.5 takes over, the engineering leap is massive: it spent 42 minutes and 6 dollars and 81 cents to build a rope-plank suspension bridge, lunar craters, volumetric headlights, and live force vectors."
        transition: flash
        show:
          - clip: rover_suspension
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [100, 56, 1720, 968]
        gfx:
          - {kind: counter, at: "42", dur: 1.8, p: {from: 0, to: 42, suffix: "MIN", label: "OPUS 5.5 · $6.81 USD · PLANK BRIDGE + BEAM", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "42", gain_db: -3}

      - id: reto01-04
        say: "While Haiku deserves credit for running at 60 FPS for 35 cents, Opus's suspension bridge physics and telemetry are in another league: point one goes to Opus 5.5."
        show:
          - split:
              flash: {clip: rover_suspension, t: 6.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: rover_suspension, t: 24.0, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "point"
            transition: flash
            p:
              winner: argon
              headline: "POINT FOR OPUS 5.5 · PLANK BRIDGE & VECTORS"
              reason: "Opus ($6.81, 42m) built a plank bridge & force vectors · Haiku ($0.35) worked & Sonnet ($2.51) broke JS"
              score: {flash: 0, argon: 1}
        score: {flash: 0, argon: 1}
        score_at: "point"

  # ===============================================================================================
  # SCENE 05: CHALLENGE 2 — 100K-AGENT GPU PHYSARUM BIO-NETWORK (OPUS WINS: 3-WAY 2-0-0)
  # ===============================================================================================
  - id: reto02
    chapter: "Challenge 2: 100K-Agent GPU Physarum Bio-Network"
    music: {cue: bed, gain_db: 0}
    hud: {reto: 2, total: 6, title: "SLIME MOLD GPU"}
    beats:
      - id: reto02-01
        say: "Challenge 2: simulate a biological Physarum slime mold in WebGL2 where tens of thousands of GPU agents form optimal rail networks by following pheromone trails."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 2, total: 6, world: "1-2", world_name: "ROUND 02 · PING-PONG GPU SHADERS", title: "PHYSARUM SLIME MOLD", subtitle: "60,000 GPU agents connecting the Tokyo rail network", times: {flash: 7, argon: 13}}
          - clip: slime_feromonas
            model: argon
            t: 19.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "form"

      - id: reto02-02
        say: "Here Haiku cost just 6 cents in 5 minutes, but failed to compile its GLSL shader due to a vec3-to-vec4 dimension mismatch; while Sonnet hit 60 FPS for 79 cents but overexposed the center into a white blob."
        show:
          - clip: slime_feromonas
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: stamp, at: "failed", dur: 2.2, p: {text: "HAIKU GLSL ERROR", color: FAIL, angle: -8, model: flash}}
          - {kind: counter, at: "79", dur: 1.8, p: {from: 0, to: 7, suffix: "MIN", label: "HAIKU $0.06 BROKEN · SONNET $0.79 (60 FPS)", color: FLASH, accent: FLASH}}
        sfx:
          - {name: error, at: "failed", gain_db: -3}

      - id: reto02-03
        say: "Opus 5.5 spent 13 minutes and 2 dollars and 55 cents to map 28 real Tokyo Bay rail stations from Shinjuku to Yokohama, linking them with 60 thousand bioluminescent GPU agents at 60 FPS."
        transition: flash
        show:
          - clip: slime_feromonas
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "13", dur: 1.8, p: {from: 0, to: 13, suffix: "MIN", label: "OPUS 5.5 · $2.55 USD · 28 TOKYO STATIONS", color: ARGON, accent: ARGON}}
        sfx:
          - {name: coin, at: "13", gain_db: -4}

      - id: reto02-04
        say: "On scientific WebGL2 ping-pong float shaders, Opus proves why it's the flagship tier and takes a two to zero lead."
        show:
          - split:
              flash: {clip: slime_feromonas, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: slime_feromonas, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "two"
            transition: flash
            p:
              winner: argon
              headline: "POINT FOR OPUS 5.5 · TOKYO RAIL BIO-GRAPH"
              reason: "Opus ($2.55, 13.4m) mapped 28 real Tokyo stations at 60 FPS · Haiku ($0.06) broke GLSL"
              score: {flash: 0, argon: 2}
        score: {flash: 0, argon: 2}
        score_at: "two"

  # ===============================================================================================
  # SCENE 06: CHALLENGE 3 — STRUCTURAL BRIDGE LIVE FRACTURE (OPUS WINS: 3-WAY 3-0-0)
  # ===============================================================================================
  - id: reto03
    chapter: "Challenge 3: Structural Bridge Live Fracture"
    music: {cue: tension, gain_db: 0}
    hud: {reto: 3, total: 6, title: "STRUCTURAL BRIDGE"}
    beats:
      - id: reto03-01
        say: "Challenge 3: a civil engineering bridge simulator where all three models had to span a canyon, drive heavy vehicles across, and snap steel beams when tension exceeds the elastic limit."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 3, total: 6, world: "2-1", world_name: "ROUND 03 · XPBD SOLVER & TENSION", title: "STRUCTURAL BRIDGE", subtitle: "Live stress heatmap, heavy train crossing & progressive collapse", times: {flash: 17, argon: 20}}
          - clip: puente_estructural
            model: argon
            t: 19.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "drive"

      - id: reto03-02
        say: "In this round all three models delivered smooth 60 FPS simulators: Haiku built a Warren truss with a 20-ton truck for 30 cents, and Sonnet animated a four-car heavy freight train for a dollar ninety-eight."
        show:
          - clip: puente_estructural
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "30", dur: 1.8, p: {from: 0, to: 17, suffix: "MIN", label: "HAIKU $0.30 · SONNET $1.98 · BOTH 60 FPS", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "30", gain_db: -4}

      - id: reto03-03
        say: "However, Opus 5.5 spent 19 minutes and 3 dollars and 58 cents to code a 20-substep XPBD solver with live stress percentages printed on every single beam, underwater piers, and millimeter deflection readouts."
        transition: flash
        show:
          - clip: puente_estructural
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "19", dur: 1.8, p: {from: 0, to: 20, suffix: "MIN", label: "OPUS 5.5 · $3.58 USD · 20-SUBSTEP XPBD CAD", color: ARGON, accent: ARGON}}

      - id: reto03-04
        say: "For its CAD-grade precision with per-beam stress readouts, Opus earns its third straight point; but watch closely, because from here on everything flips."
        show:
          - split:
              flash: {clip: puente_estructural, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: puente_estructural, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "third"
            transition: flash
            p:
              winner: argon
              headline: "POINT FOR OPUS 5.5 · XPBD CAD TELEMETRY"
              reason: "Opus ($3.58, 19.7m) rendered per-beam stress % · Haiku ($0.30) & Sonnet ($1.98) also passed at 60 FPS"
              score: {flash: 0, argon: 3}
        score: {flash: 0, argon: 3}
        score_at: "third"

  # ===============================================================================================
  # SCENE 07: CHALLENGE 4 — 3D ACID TECHNO STUDIO TB-303 + 909 (HAIKU WINS: 3-WAY 3-0-1)
  # ===============================================================================================
  - id: reto04
    chapter: "Challenge 4: 3D Acid Techno Studio TB-303 + TR-909"
    music: {cue: battle, gain_db: -6}
    hud: {reto: 4, total: 6, title: "3D ACID SYNTH STUDIO"}
    beats:
      - id: reto04-01
        say: "Challenge 4: an Acid Techno music studio with a TB-303 bassline synth, TR-909 drum machine in Web Audio API, cutoff and distortion rotary knobs, and an audio-reactive 3D tunnel."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 4, total: 6, world: "2-2", world_name: "ROUND 04 · WEB AUDIO & 3D SHADERS", title: "3D ACID SYNTH STUDIO", subtitle: "TB-303 + TR-909 step sequencer, resonant filter & 3D FFT visualizer", times: {flash: 9, argon: 31}}
          - clip: sintetizador_acido_3d
            model: flash
            t: 4.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "cutoff"
        project_audio:
          wav: "../../../ep04-escalera-claude/grabaciones/04_sintetizador_acido_3d_audio.wav"
          t0: 0.0
          gain_db: -5.0

      - id: reto04-02
        say: "And here came the biggest upset of the tournament: in just 8 and a half minutes and for only 21 cents, Claude Haiku 5.5 built a 3D spectral particle terrain, oscilloscope, 7 rotary knobs, and the full sequencer at 61 FPS."
        show:
          - clip: sintetizador_acido_3d
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        project_audio:
          wav: "../../../ep04-escalera-claude/grabaciones/04_sintetizador_acido_3d_audio.wav"
          t0: 5.0
          gain_db: -4.5
        gfx:
          - {kind: counter, at: "21", dur: 1.8, p: {from: 0, to: 9, suffix: "MIN", label: "HAIKU 5.5 · $0.21 USD · 61 FPS + LIVE AUDIO", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "21", gain_db: -3}

      - id: reto04-03
        say: "Sonnet delivered a wireframe holodome for a dollar fifty-two and Opus built a slick laser highway, but Opus took 31 minutes and charged 5 full dollars: twenty-four times more expensive than Haiku for the exact same frame rate."
        transition: flash
        show:
          - clip: sintetizador_acido_3d
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        project_audio:
          wav: "../../../ep04-escalera-claude/grabaciones/04_sintetizador_acido_3d_audio.wav"
          t0: 19.0
          gain_db: -4.5
        gfx:
          - {kind: counter, at: "31", dur: 1.8, p: {from: 0, to: 31, suffix: "MIN", label: "OPUS 5.5 · $5.00 USD (24X MORE THAN HAIKU)", color: ARGON, accent: ARGON}}

      - id: reto04-04
        say: "Three and a half times faster and twenty-four times cheaper without dropping a single frame: a historic ROI point for Claude Haiku 5.5."
        show:
          - split:
              flash: {clip: sintetizador_acido_3d, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: sintetizador_acido_3d, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "historic"
            transition: flash
            p:
              winner: flash
              headline: "POINT FOR HAIKU 5.5 · 61 FPS FOR $0.21"
              reason: "Haiku ($0.21, 8.7m) hit 61 FPS with 3D + TB-303 + 909 costing 24x less than Opus ($5.00, 31m)"
              score: {flash: 1, argon: 3}
        score: {flash: 1, argon: 3}
        score_at: "historic"

  # ===============================================================================================
  # SCENE 08: CHALLENGE 5 — WEBGL2 BVH PATH TRACER (SONNET WINS: 3-WAY 3-1-1)
  # ===============================================================================================
  - id: reto05
    chapter: "Challenge 5: WebGL2 BVH Path Tracer & Denoiser"
    music: {cue: bed, gain_db: 0}
    hud: {reto: 5, total: 6, title: "WEBGL2 PATH TRACER"}
    beats:
      - id: reto05-01
        say: "Challenge 5: code a Monte Carlo Path Tracer from scratch in WebGL2 with BVH acceleration, glass refraction, caustics, and a real-time A-Trous wavelet denoiser."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 5, total: 6, world: "3-1", world_name: "ROUND 05 · MONTE CARLO RAY TRACING", title: "WEBGL2 PATH TRACER", subtitle: "Temporal accumulation, chromatic dispersion & A-Trous denoiser", times: {flash: 14, argon: 31}}
          - clip: pathtracer_bvh
            model: flash
            t: 6.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "glass"

      - id: reto05-02
        say: "On the left, Haiku built a basic noisy tracer for 13 cents; but on the right, Claude Sonnet 5.5 shone in just 13.9 minutes for a dollar sixty-seven, rendering rainbow chromatic dispersion through glass at 29 FPS."
        show:
          - clip: pathtracer_bvh
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: counter, at: "29", dur: 1.8, p: {from: 0, to: 14, suffix: "MIN", label: "SONNET 5.5 · $1.67 USD · 29 FPS + RAINBOW GLASS", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "29", gain_db: -3}

      - id: reto05-03
        say: "Meanwhile, Opus 5.5 took more than twice as long—31 minutes and 5 dollars and 5 cents—and its overly heavy shader dragged performance down to just 15 frames per second."
        transition: flash
        show:
          - clip: pathtracer_bvh
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [100, 56, 1720, 968]
        gfx:
          - {kind: counter, at: "15", dur: 1.8, p: {from: 0, to: 31, suffix: "MIN", label: "OPUS 5.5 · $5.05 USD · DROPS TO 15 FPS", color: ARGON, accent: ARGON}}

      - id: reto05-04
        say: "Nearly double the frame rate, in less than half the time, at one-third the cost: a decisive victory for Claude Sonnet 5.5."
        show:
          - split:
              flash: {clip: pathtracer_bvh, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: pathtracer_bvh, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "decisive"
            transition: flash
            p:
              winner: flash
              headline: "POINT FOR SONNET 5.5 · 29 FPS & DISPERSION"
              reason: "Sonnet ($1.67, 13.9m) doubled Opus's FPS ($5.05, 31.4m, 15 FPS) with rainbow glass dispersion"
              score: {flash: 2, argon: 3}
        score: {flash: 2, argon: 3}
        score_at: "decisive"

  # ===============================================================================================
  # SCENE 09: CHALLENGE 6 — RETRO CHIP-8 CPU CONSOLE (SONNET WINS: 3-WAY 3-2-1 FINAL)
  # ===============================================================================================
  - id: reto06
    chapter: "Challenge 6: Retro CHIP-8 Console & Assembler"
    music: {cue: battle, gain_db: -5}
    hud: {reto: 6, total: 6, title: "RETRO CHIP-8 CONSOLE"}
    beats:
      - id: reto06-01
        say: "Final challenge: build an emulator and IDE for the classic CHIP-8 console complete with a 35-opcode CPU, phosphor CRT monitor, live disassembler, hex dump, and custom assembler."
        transition: pixel_wipe
        show:
          - card: chapter_card
            p: {n: 6, total: 6, world: "3-2", world_name: "ROUND 06 · CPU EMULATOR & ASSEMBLER", title: "RETRO CHIP-8 CONSOLE", subtitle: "35-opcode CPU, curved CRT monitor, disassembler & 4 playable ROMs", times: {flash: 35, argon: 42}}
          - clip: consola_retro_cpu
            model: flash
            t: 5.0
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            cut_at: "live"
        project_audio:
          wav: "../../../ep04-escalera-claude/grabaciones/06_consola_retro_cpu_audio.wav"
          t0: 0.0
          gain_db: -6.0

      - id: reto06-02
        say: "Look at the split screen: both Haiku for 48 cents and Sonnet for 3 dollars and 75 cents booted straight into live Pong at 60 FPS, with Sonnet adding a curved CRT bezel, register bars, and a syntax-highlighted ASM editor."
        show:
          - clip: consola_retro_cpu
            model: flash
            t: 1.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        project_audio:
          wav: "../../../ep04-escalera-claude/grabaciones/06_consola_retro_cpu_audio.wav"
          t0: 6.0
          gain_db: -5.5
        gfx:
          - {kind: counter, at: "60", dur: 1.8, p: {from: 0, to: 35, suffix: "MIN", label: "HAIKU $0.48 & SONNET $3.75 · LIVE PONG 60 FPS", color: FLASH, accent: FLASH}}
        sfx:
          - {name: coin, at: "60", gain_db: -3}

      - id: reto06-03
        say: "And here came Opus 5.5's most painful stumble: after 42 minutes and nearly 7 dollars in tokens, it forgot to invoke its ROM assembler on boot, leaving memory at zero bytes and the CRT screen dark."
        transition: flash
        show:
          - clip: consola_retro_cpu
            model: argon
            t: 19.5
            rate: 1.0
            roi: [0, 0, 1920, 1080]
            roi_to: [120, 68, 1680, 945]
        gfx:
          - {kind: stamp, at: "forgot", dur: 2.3, p: {text: "0-BYTE ROM BUG", color: FAIL, angle: -8, model: argon}}
          - {kind: counter, at: "42", dur: 1.8, p: {from: 0, to: 42, suffix: "MIN", label: "OPUS 5.5 · $6.93 USD · 0 B ROM ON BOOT", color: ARGON, accent: ARGON}}
        sfx:
          - {name: error, at: "forgot", gain_db: -3}

      - id: reto06-04
        say: "Sonnet 5.5 takes the final point with a flawless retro workstation, bringing the final Claude ladder scoreboard to three points for Opus, two for Sonnet, and one for Haiku."
        show:
          - split:
              flash: {clip: consola_retro_cpu, t: 6.5, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: consola_retro_cpu, t: 24.5, rate: 1.0, roi: [240, 60, 1440, 960]}
          - card: verdict
            cut_at: "final"
            transition: flash
            p:
              winner: flash
              headline: "POINT FOR SONNET 5.5 · FINAL 3 - 2 - 1"
              reason: "Sonnet ($3.75) & Haiku ($0.48) booted Pong at 60 FPS · Opus ($6.93) left ROM at 0 bytes"
              score: {flash: 3, argon: 3}
        score: {flash: 3, argon: 3}
        score_at: "final"

  # ===============================================================================================
  # SCENE 10: FINAL SCOREBOARD & BUYER'S GUIDE
  # ===============================================================================================
  - id: resultados
    chapter: "Final verdict: when to use Haiku, Sonnet, or Opus"
    music: {cue: results, gain_db: 0}
    hud: false
    beats:
      - id: resultados-01
        say: "Three for Opus, two for Sonnet, and one for Haiku: this benchmark proves that paying for the most expensive tier does not guarantee winning every challenge."
        post: 2.8
        transition: flash
        show:
          - {clip: rover_suspension, model: argon, t: 24.0, rate: 1.0, roi: [0, 0, 1920, 1080]}
          - {clip: consola_retro_cpu, model: flash, t: 6.0, rate: 1.0, roi: [0, 0, 1920, 1080]}
          - card: scoreboard_card
            cut_at: "benchmark"
            p:
              title: "FINAL SCORE · OPUS 3 · SONNET 2 · HAIKU 1"
              rows:
                - {n: 1, title: "Planetary Rover Verlet (Opus Wins)", winner: argon, flash_min: 19, argon_min: 42}
                - {n: 2, title: "GPU Physarum Bio-Network (Opus Wins)", winner: argon, flash_min: 7, argon_min: 13}
                - {n: 3, title: "XPBD Structural Bridge (Opus Wins)", winner: argon, flash_min: 17, argon_min: 20}
                - {n: 4, title: "3D Acid Studio $0.21 (Haiku Wins)", winner: flash, flash_min: 9, argon_min: 31}
                - {n: 5, title: "WebGL2 Path Tracer 29 FPS (Sonnet Wins)", winner: flash, flash_min: 14, argon_min: 31}
                - {n: 6, title: "Retro CHIP-8 Console (Sonnet Wins)", winner: flash, flash_min: 35, argon_min: 42}
        sfx:
          - {name: powerup, at: 0.05, gain_db: -4}

      - id: resultados-02
        say: "On the total stopwatch, Haiku finished all six challenges in 87 minutes and Sonnet in 105, while Opus needed 179 minutes—nearly three full hours of compute."
        show:
          - card: timer_race
            p: {flash: 105, argon: 179, title: "TOTAL TIME · 6 REAL CHALLENGES", ratio_text: "HAIKU: 87 MIN · SONNET: 105 MIN · OPUS: 179 MIN"}

      - id: resultados-03
        say: "In reliability, no tier was infallible in a single shot: Haiku missed one GLSL cast, Sonnet truncated one script, and Opus forgot to auto-assemble its ROM in Round 6 after burning nearly seven dollars."
        post: 0.4
        show:
          - card: stats_card
            p:
              title: "HEADLESS CHROME AUDIT (18 DEMOS)"
              rows:
                - {label: "WORKING DEMOS", flash: "5/6 HAIKU · 5/6 SONNET", argon: "5/6 OPUS 5.5", better: flash}
                - {label: "BEST TOURNAMENT ROI", flash: "HAIKU $0.21 (61 FPS)", argon: "OPUS $2.55 (TOKYO)", better: flash}

      - id: resultados-04
        say: "And the API bill changes everything: one dollar and fifty-four cents for the entire tournament on Haiku, twelve dollars and twenty-two cents on Sonnet, and twenty-nine dollars and ninety-four cents on Opus."
        post: 0.8
        show:
          - card: stats_card
            p:
              title: "REAL API BILL (ALL 6 CHALLENGES)"
              rows:
                - {label: "CLAUDE HAIKU / SONNET", flash: "$1.54 / $12.22 USD", argon: "$29.94 USD (OPUS)", better: flash}
                - {label: "SAVINGS VS OPUS 5.5", flash: "19.4X / 2.45X CHEAPER", argon: "1.0X BASELINE", better: flash}
        sfx:
          - {name: coin, at: "fifty-four", gain_db: -3}

  # ===============================================================================================
  # SCENE 11: GOLDEN RULE & OUTRO
  # ===============================================================================================
  - id: cierre
    chapter: "Golden rule for choosing Haiku, Sonnet, or Opus"
    music: {cue: outro, gain_db: 0}
    hud: false
    beats:
      - id: cierre-01
        say: "Here is the golden rule for your wallet: use Haiku 5.5 for rapid prototypes, UI dashboards, and audio synths where it costs twenty times less."
        transition: pixel_wipe
        show:
          - split:
              flash: {clip: sintetizador_acido_3d, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: sintetizador_acido_3d, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}

      - id: cierre-02
        say: "Use Sonnet 5.5 as your daily workhorse for emulators, optimized shaders, and full web apps; and reserve Opus 5.5 strictly for multi-pass physics and heavy architectural math."
        captions: false
        show:
          - card: quote_card
            p:
              text: "Haiku ($1.54) handles 80% of prototypes 20x cheaper. Sonnet ($12.22) is the daily sweet spot in speed and FPS. Reserve Opus ($29.94) for extreme physics and deep architecture."
              author: "Real Buyer's Guide · Mixiuh Labs"

      - id: cierre-03
        say: "I uploaded all eighteen interactive demos, exact prompts, and token breakdowns to labs dot mixiuh dot online so you can test all three tiers side by side in your browser."
        show:
          - split:
              flash: {clip: pathtracer_bvh, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: pathtracer_bvh, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}
          - split:
              flash: {clip: consola_retro_cpu, t: 5.0, rate: 1.0, roi: [240, 60, 1440, 960]}
              argon: {clip: consola_retro_cpu, t: 23.0, rate: 1.0, roi: [240, 60, 1440, 960]}
            cut_at: "prompts"

      - id: cierre-04
        say: "Subscribe to Mixiuh Labs, share this benchmark with your team, and tell me in the comments which model family we should put on the ladder in Episode 05."
        transition: pixel_wipe
        show:
          - card: end_screen
            p: {headline: "Play all 18 live demos now", sub: "labs.mixiuh.online · subscribe to Mixiuh Labs"}
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
        say: "Experiment 04 complete: see you in the next level, right here on Mixiuh Labs."
        dur: 11.0
        show:
          - continue: true
"""

(EP_ES_DIR / "episode.yaml").write_text(YAML_ES, encoding="utf-8")
(EP_EN_DIR / "episode.yaml").write_text(YAML_EN, encoding="utf-8")
print("Wrote:", EP_ES_DIR / "episode.yaml")
print("Wrote:", EP_EN_DIR / "episode.yaml")
