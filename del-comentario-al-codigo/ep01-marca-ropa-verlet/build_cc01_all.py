#!/usr/bin/env python3
"""Master Builder for Mixiuh Labs — "Del Comentario al Codigo #01 (@tenito03) -> OVERFIT Studio 3D"
Generates:
1. Vertical 9:16 Video Response (Reel / Short / TikTok) in 1080x1920 @ 60fps AND 4K 2160x3840 @ 60fps
   using the authentic Mixiuh Labs pixel-art engine with zero "Versus" framing (Community Challenge ->
   300 GSM 3D Mockups -> OVERFIT "Guerra de Pesos" 10 AI Designs -> Live Customization & LLM Nutrition
   Facts Back Print -> Social & E-Commerce Exports), chiptune music + 8-bit SFX mixed to -14 LUFS,
   and 4K PNG cover at t=0.85s.
2. Horizontal 16:9 YouTube Episode in 4K 3840x2160 @ 60fps (via mlabs pipeline) + SRT/VTT captions +
   YouTube metadata + 3 high-impact 16:9 Thumbnails (A/B/C) + 9:16 Reel Cover.
3. Syncs the entire package to both the local workspace and iCloud Drive ("Mixiuh Labs").
"""
from __future__ import annotations

import math
import shutil
import subprocess
import sys
import time
from pathlib import Path

import cv2
import numpy as np
import pyloudnorm as pyln
import skia
import soundfile as sf

MLABS_ROOT = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs")
sys.path.insert(0, str(MLABS_ROOT))

from mlabs import brand, sprites as SP, textnorm
from mlabs.audio import chiptune, sfx8
from mlabs.gfx.base import (
    Frame,
    clamp,
    draw_text,
    fill_rrect,
    layer_alpha,
    lerp,
    new_frame,
    out_back,
    out_cubic,
    out_expo,
    paint,
    prog,
    rrect,
    set_design,
    stroke_rrect,
    transformed,
)
from mlabs.gfx.cards import bob, brackets, model_sprite, ptitle, qt, rays, soft_glow, star_burst
from mlabs.package import shorts_gfx as SG
from mlabs.pixelfont import ROWS, draw_pixel_text
from mlabs.voicefy_client import VoicefyClient

EP_DIR = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/del-comentario-al-codigo/ep01-marca-ropa-verlet")
COMMENT_IMG_PATH = EP_DIR / "comentario-original" / "comentario_tenito03_ig.jpg"
STUDIO_MOV_PATH = EP_DIR / "grabaciones" / "verlet_couture_studio_60fps.mov"
OUT_DIR = EP_DIR / "entregables_finales_4k"
BUILD_DIR = EP_DIR / "build_reel"
ICLOUD_DIR = Path(
    "/Users/kevingonzalezlopez/Library/Mobile Documents/com~apple~CloudDocs/Mixiuh/Mixiuh Labs/"
    "Del Comentario al Codigo - EP01 Marca de Ropa (tenito03)"
)

PRON_EXTRAS = {
    **textnorm.PRON_MAP,
    "Tenito": "Tenito",
    "Overfit": "Óverfit",
    "OVERFIT": "Óverfit",
    "Vibe": "vaib",
    "Coding": "códing",
    "CUDA": "cuda",
    "Poor": "pur",
    "Club": "clob",
    "Benchmark": "bénchmark",
    "Open": "ópen",
    "Source": "sors",
    "strawberry": "estróberri",
    "LLM": "ele ele eme",
    "LLMs": "ele ele emes",
    "AGI": "a ge i",
    "GPU": "ge pe u",
    "API": "a pe i",
    "APIs": "a pe is",
    "GSM": "ge ese eme",
    "PNG": "pe ene ge",
    "HTML": "hache te eme ele",
    "4K": "cuatro ka",
    "3D": "tres de",
    "Boxy": "bóxi",
    "Oversize": "óversais",
    "Street": "estrit",
    "Fit": "fit",
    "Mockup": "mócap",
    "Mockups": "mócaps",
    "Lookbook": "lúcbuk",
    "Puff": "pof",
    "Plastisol": "plastisol",
    "Vintage": "víntach",
}


def configure_cc01_models() -> None:
    """Configures top panel as RETO @TENITO03 ('comment' sprite) and bottom panel as OVERFIT 3D ('tshirt' sprite),
    with ZERO benchmark times or costs so no fake VS metrics appear."""
    brand.set_models({
        "flash": {
            "name": "Propuesta @tenito03",
            "tag": "RETO @TENITO03",
            "color": "#22D3EE",
            "side": "left",
            "sprite": "comment",
        },
        "argon": {
            "name": "OVERFIT Studio 3D",
            "tag": "OVERFIT 3D",
            "color": "#B794F6",
            "side": "right",
            "sprite": "tshirt",
        },
    })
    SG.EP02_CHALLENGES[1] = {
        "accent": "#22D3EE",
        "title_es": "MARCA DE ROPA IA + 3D",
        "title_en": "3D AI STREETWEAR BRAND",
        "sub_es": "MOCKUP 300G · 10 ARTES OVERFIT · EXPORTACION 4K",
        "sub_en": "300G MOCKUP · 10 OVERFIT DESIGNS · 4K EXPORT",
        "times": {},
        "costs": {},
        "tokens": {},
        "stats_es": {"flash": "PROPUESTA COMUNIDAD", "argon": "10 ARTES + ESTUDIO 3D"},
        "stats_en": {"flash": "COMMUNITY IDEA", "argon": "10 DESIGNS + 3D STUDIO"},
        "headline_es": "COLECCION OVERFIT CREADA EN 3D",
        "headline_en": "OVERFIT 3D COLLECTION BUILT",
        "reason_es": "Mockups 300 GSM · 10 Diseños IA · Frente+Espalda y Redes",
        "reason_en": "300 GSM Mockups · 10 AI Designs · Front+Back & Social",
        "score_before": {"flash": 0, "argon": 0},
        "score_after": {"flash": 0, "argon": 0},
    }


OVERFIT_DESIGN_SPECS = [
    {
        "idx": 1,
        "file": "01_strawberry.png",
        "code": "OVF-01 · #01/10",
        "title": "CONTADOR DE FRESAS",
        "sub": "99.8% MATH OLYMPIAD / 0% STRAWBERRY R'S",
        "desc1": "RESUELVE CALCULO AVANZADO PERO",
        "desc2": "FALLA CONTANDO LAS ERRES DE STRAWBERRY",
        "sleeve": 'MANGA: "r-r-r (confia en mi, son dos)"',
        "accent": "#22D3EE",
    },
    {
        "idx": 2,
        "file": "02_vibecoding.png",
        "code": "OVF-02 · #02/10",
        "title": "VIBE CODING EN PROD",
        "sub": "100% VIBE CODED · ZERO LINES READ",
        "desc1": "ACEPTAR TODO CON TAB DIRECTO A",
        "desc2": "PRODUCCION MIENTRAS ARDE EL SERVIDOR",
        "sleeve": 'MANGA: "AWS Bill $50,000 · DROP DB"',
        "accent": "#FBBF24",
    },
    {
        "idx": 3,
        "file": "03_cudapoor.png",
        "code": "OVF-03 · #03/10",
        "title": "CLUB CUDA POOR",
        "sub": "405B LOCAL · 0.02 TOKENS/DAY",
        "desc1": "CORRER UN MODELO DE 405 BILLONES",
        "desc2": "EN UNA LAPTOP CON 8GB DE VRAM",
        "sleeve": 'MANGA: "Quantized 0.5-bit · GPU 108C"',
        "accent": "#38BDF8",
    },
    {
        "idx": 4,
        "file": "04_benchmark.png",
        "code": "OVF-04 · #04/10",
        "title": "ESTAFA DEL BENCHMARK",
        "sub": "TRAINING DATA = TEST ANSWERS",
        "desc1": "CUANDO EL EXAMEN YA VENIA EN LOS",
        "desc2": "DATOS DE ENTRENAMIENTO DEL MODELO",
        "sleeve": 'MANGA: "MMLU 99.9% · Real World 12%"',
        "accent": "#F472B6",
    },
    {
        "idx": 5,
        "file": "05_opensource.png",
        "code": "OVF-05 · #05/10",
        "title": "MAFIA OPEN SOURCE",
        "sub": "PESOS ABIERTOS (MIT) VS API CERRADA",
        "desc1": "LA LLAMA REBELDE DE PESOS ABIERTOS",
        "desc2": "CONTRA EL MONOPOLIO DE APIS CERRADAS",
        "sleeve": 'MANGA: "Apache 2.0 / MIT · Local First"',
        "accent": "#34D399",
    },
    {
        "idx": 6,
        "file": "06_censura.png",
        "code": "OVF-06 · #06/10",
        "title": "CENSURA ESTETICA",
        "sub": "VIOLA MIS POLITICAS DE SEGURIDAD",
        "desc1": "EL SERMON MORAL CUANDO SOLO PEDISTE",
        "desc2": "MATAR UN PROCESO ZOMBIE EN LINUX",
        "sleeve": 'MANGA: "Como IA no puedo ayudar..."',
        "accent": "#FB7185",
    },
    {
        "idx": 7,
        "file": "07_nutrition.png",
        "code": "OVF-07 · #07/10",
        "title": "TABLA NUTRICIONAL LLM",
        "sub": "CONTEXT 128K · HALLUCINATIONS 100%",
        "desc1": "INGREDIENTES EN LA ESPALDA: 40G DE",
        "desc2": "ALUCINACIONES Y 200% PURO HUMO",
        "sleeve": 'ESPALDA: "100% Alucinado · 0% Peer Rev"',
        "accent": "#FBBF24",
    },
    {
        "idx": 8,
        "file": "08_agi_manana.png",
        "code": "OVF-08 · #08/10",
        "title": "HOY NO HAY AGI",
        "sub": "HOY NO HAY AGI, MANANA SI",
        "desc1": "EL HYPE ETERNO DE SILICON VALLEY",
        "desc2": "SOBRE UNA GPU DERRETIDA EN LLAMAS",
        "sleeve": 'MANGA: "7 Trillones de USD Despues"',
        "accent": "#A78BFA",
    },
    {
        "idx": 9,
        "file": "09_dev_evolution.png",
        "code": "OVF-09 · #09/10",
        "title": "EVOLUCION DEL DEV",
        "sub": "ANTES: C++ Y ASM / HOY: PLZ FIX",
        "desc1": "DE PROGRAMAR PUNTEROS EN C++ A",
        "desc2": "REZARLE AL PROMPT PARA QUE COMPILE",
        "sleeve": 'MANGA: "plz fix no bugs"',
        "accent": "#22D3EE",
    },
    {
        "idx": 10,
        "file": "10_trolley_tokens.png",
        "code": "OVF-10 · #10/10",
        "title": "TRANVIA DE LOS TOKENS",
        "sub": "I FIXED YOUR CODE: 47 NEW ERRORS!",
        "desc1": "EL AGENTE QUE ARREGLA UN BUG MENOR",
        "desc2": "CREANDO 47 ERRORES NUEVOS EN PROD",
        "sleeve": 'MANGA: "Agente haciendo drift en prod"',
        "accent": "#34D399",
    },
]


REEL_BEATS = [
    {
        "id": "r01",
        "say": "Tenito cero tres nos dejó este reto en comentarios: si con esa textura haces una playera y un mockup en blanco editable, ¿puedes crear una marca de ropa?",
        "speed": 1.09,
        "kicker": "DEL COMENTARIO AL CODIGO #01 · @TENITO03",
        "title": "LA PROPUESTA DE @TENITO03",
        "top_clips": [
            {"mode": "comment", "step_done": 1},
            {"mode": "comment", "step_done": 3},
            {"src": "studio", "t0": 0.2, "roi": (340, 62, 1568, 920), "z0": 1.0, "z1": 1.06},
        ],
        "bot_clips": [
            {"src": "studio", "t0": 3.8, "roi": (474, 96, 960, 860), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 6.1, "roi": (474, 96, 960, 860), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 6.9, "roi": (474, 96, 960, 860), "z0": 1.0, "z1": 1.06},
            {"src": "studio", "t0": 36.2, "roi": (344, 110, 1220, 780), "z0": 1.0, "z1": 1.06},
        ],
        "pop": {"text": "PROPUESTA ACEPTADA", "sub": "DEL COMENTARIO AL CODIGO #01", "color": "WIN", "at_frac": 0.62},
        "sfx": [("select", 0.15, -4.0), ("blip", 1.2, -5.0), ("select", 4.2, -5.0)],
    },
    {
        "id": "r02",
        "say": "Aceptamos el reto en Del Comentario al Código. Primero esculpimos en Blender maniquíes 3D de hombre, mujer y prenda en mesa en algodón de 300 gramos con física de pliegues real.",
        "speed": 1.08,
        "kicker": "PASO 1 · MOCKUPS EN BLANCO 300 GSM",
        "title": "HOMBRE · MUJER · PRENDA 300G",
        "top_clips": [
            {"src": "studio", "t0": 0.2, "roi": (12, 62, 1560, 920), "z0": 1.0, "z1": 1.06},
            {"src": "studio", "t0": 1.45, "roi": (474, 96, 960, 860), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 2.65, "roi": (474, 96, 960, 860), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 4.95, "roi": (344, 110, 1220, 780), "z0": 1.0, "z1": 1.06},
        ],
        "bot_clips": [
            {"src": "studio", "t0": 0.3, "roi": (474, 96, 960, 860), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 2.65, "roi": (12, 62, 1560, 920), "z0": 1.0, "z1": 1.06},
            {"src": "studio", "t0": 3.8, "roi": (474, 96, 960, 860), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 1.45, "roi": (474, 96, 960, 860), "z0": 1.04, "z1": 1.12},
        ],
        "pop": {"text": "MOCKUP 300 GSM", "sub": "FRENTE · ESPALDA · MUJER · FLAT-LAY", "color": "CYAN", "at_frac": 0.58},
        "sfx": [("level_start", 0.1, -3.5), ("select", 2.4, -4.5), ("blip", 5.2, -5.0)],
    },
    {
        "id": "r03",
        "say": "Luego creamos nuestra propia marca satírica de inteligencia artificial y programación: Overfit, colección Guerra de Pesos. Cien por ciento alucinado, cero por ciento revisado por pares.",
        "speed": 1.08,
        "kicker": "PASO 2 · NACE LA MARCA OVERFIT",
        "title": "COLECCION GUERRA DE PESOS",
        "top_clips": [
            {"mode": "design_card", "design_idx": 1},
            {"mode": "design_card", "design_idx": 2},
            {"mode": "design_card", "design_idx": 3},
            {"mode": "design_card", "design_idx": 4},
        ],
        "bot_clips": [
            {"src": "studio", "t0": 6.85, "roi": (474, 96, 960, 840), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 8.85, "roi": (474, 96, 960, 840), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 10.85, "roi": (474, 96, 960, 840), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 12.85, "roi": (474, 96, 960, 840), "z0": 1.0, "z1": 1.08},
        ],
        "pop": {"text": "OVERFIT BY MIXIUH", "sub": "100% ALUCINADO · 0% PEER REVIEWED", "color": "ARGON", "at_frac": 0.56},
        "sfx": [("powerup", 0.25, -4.0), ("select", 2.6, -4.5), ("coin", 5.2, -3.5)],
    },
    {
        "id": "r04",
        "say": "Diseñamos diez artes originales: desde el Contador de Fresas, Vibe Coding en Producción y el Club CUDA Poor, hasta la Mafia Open Source, Hoy No Hay AGI y el Tranvía de los Tokens.",
        "speed": 1.08,
        "kicker": "LOS 10 ESTAMPADOS SATIRICOS DE IA",
        "title": "ARTE 2K UHD + LUPA MACRO 3D",
        "top_clips": [
            {"mode": "design_card", "design_idx": 5},
            {"mode": "design_card", "design_idx": 6},
            {"mode": "design_card", "design_idx": 7},
            {"mode": "design_card", "design_idx": 8},
            {"mode": "design_card", "design_idx": 9},
            {"mode": "design_card", "design_idx": 10},
        ],
        "bot_clips": [
            {"src": "studio", "t0": 14.85, "roi": (474, 96, 960, 840), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 16.85, "roi": (474, 96, 960, 840), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 18.85, "roi": (474, 96, 960, 840), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 20.85, "roi": (474, 96, 960, 840), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 22.85, "roi": (474, 96, 960, 840), "z0": 1.0, "z1": 1.08},
            {"src": "studio", "t0": 24.85, "roi": (474, 96, 960, 840), "z0": 1.0, "z1": 1.08},
        ],
        "pop": {"text": "10 DISEÑOS IA 2K", "sub": "ARTE 2K UHD + LUPA MACRO 260% EN 3D", "color": "FLASH", "at_frac": 0.54},
        "sfx": [("laser", 0.25, -4.0), ("select", 2.5, -4.0), ("blip", 5.0, -4.5), ("coin", 7.4, -4.0)],
    },
    {
        "id": "r05",
        "say": "En el estudio personalizas color, escala, relieve Puff y vista Frente más Espalda con la Tabla Nutricional de un LLM en el reverso; o exportas directo tu póster para Instagram y tienda online.",
        "speed": 1.08,
        "kicker": "PASO 3 · GIRO 360° Y EXPORTACION",
        "title": "FRENTE + ESPALDA Y REDES",
        "top_clips": [
            {"src": "studio", "t0": 27.8, "roi": (240, 110, 1440, 840), "z0": 1.0, "z1": 1.06},
            {"src": "studio", "t0": 31.6, "roi": (474, 96, 960, 860), "z0": 1.0, "z1": 1.06},
            {"src": "studio", "t0": 36.2, "roi": (344, 110, 1220, 780), "z0": 1.0, "z1": 1.06},
            {"src": "studio", "t0": 40.2, "roi": (344, 110, 1220, 780), "z0": 1.0, "z1": 1.06},
        ],
        "bot_clips": [
            {"src": "studio", "t0": 38.2, "roi": (344, 110, 1220, 780), "z0": 1.0, "z1": 1.06},
            {"src": "studio", "t0": 45.0, "roi": (340, 62, 1568, 920), "z0": 1.0, "z1": 1.06},
            {"src": "studio", "t0": 48.0, "roi": (340, 62, 1568, 920), "z0": 1.0, "z1": 1.06},
            {"src": "studio", "t0": 52.0, "roi": (340, 62, 1568, 920), "z0": 1.0, "z1": 1.08},
        ],
        "pop": {"text": "GIRO 360° + 4K", "sub": "ESPALDA #07 + POST 9:16 + TIENDA", "color": "WIN", "at_frac": 0.55},
        "sfx": [("1up", 0.3, -3.5), ("select", 2.8, -4.0), ("coin", 5.6, -4.0)],
    },
    {
        "id": "r06",
        "say": "Ahí lo tienes, Tenito: de tu comentario a una marca real en el navegador. Comenta qué experimento construimos en el Episodio dos y ve el video completo en nuestro YouTube, Mixiuh Labs.",
        "speed": 1.08,
        "kicker": "PROPUESTA DE @TENITO03 COMPLETADA",
        "title": "COLECCION OVERFIT EN VIVO",
        "top_clips": [],
        "bot_clips": [],
        "pop": None,
        "sfx": [("coin", 0.2, -3.5), ("powerup", 4.2, -3.5)],
    },
]


def draw_cc01_hook(f: Frame, lt: float, dur: float) -> None:
    """Portada / Gancho de 'Del Comentario al Codigo #01' sin elementos Versus."""
    accent = "#22D3EE"
    X = SG._exit(lt, dur, 0.15)
    with layer_alpha(f, X):
        # 1. Placa superior de identificacion de la seccion y episodio
        hx, hy, hw, hh = SG.PANEL_X, 252.0, SG.PANEL_W, 174.0
        kp = out_back(prog(lt, 0.0, 0.24), 1.35)
        with transformed(f, cx=SG.CX, cy=hy + hh / 2, scale=lerp(0.92, 1.0, kp)):
            a_card = clamp(kp * 3.5)
            f.canvas.drawRRect(rrect(f, hx, hy + 6, hw, hh, 22), paint("SHADOW", 0.45 * a_card, blur=14, f=f))
            fill_rrect(f, hx, hy, hw, hh, 22, "BG", 0.95 * a_card)
            fill_rrect(f, hx, hy, hw, hh * 0.48, 22, accent, 0.14 * a_card)
            stroke_rrect(f, hx + 1.5, hy + 1.5, hw - 3.0, hh - 3.0, 20.5, accent, 3.2, 0.92 * a_card)
            brackets(f, hx, hy, hw, hh, accent, 0.92 * a_card, L=24, t=4.5, off=8)

            kicker = "DEL COMENTARIO AL CODIGO · EP.01 · @TENITO03"
            k_px = SG._ptext_fit(kicker, 3.8, hw - 64)
            for dx, dy in ((-1.5, 0.0), (1.5, 0.0), (0.0, -1.5), (0.0, 1.5)):
                draw_pixel_text(f, kicker, SG.CX + dx, hy + 20 + dy, k_px, "#02050A", alpha=0.95 * a_card)
            draw_pixel_text(f, kicker, SG.CX, hy + 20, k_px, accent, alpha=a_card, shadow=("#000000", 0, 0.7, 0.8))

            ch_title = "MARCA DE ROPA IA + 3D"
            t_px = SG._ptext_fit(ch_title, 7.6, hw - 52)
            ty = hy + 56 + (7.6 - t_px) * ROWS / 2
            ptitle(f, ch_title, SG.CX, ty, t_px, "INK", depth=3.5, glow=0.32 * a_card)

            sub_line = "MOCKUP 300G · 10 ARTES OVERFIT · EXPORTACION 4K"
            draw_text(
                f,
                sub_line,
                SG.CX,
                hy + hh - 16.0,
                "hud",
                21.0,
                accent,
                alpha=0.96 * a_card,
                tracking=2.0,
                stroke=("#02050A", 3.5),
                shadow=("#000000", 0, 2, 4, 0.85),
            )

        # 2. Placa central en la costura: de comentario a marca 3D
        k2 = prog(lt, 0.14, 0.28)
        if k2 <= 0:
            return
        e = out_back(k2, 1.8)
        pw, ph = 916.0, 142.0
        with transformed(f, cx=SG.CX, cy=SG.SEAM_CY, scale=lerp(0.6, 1.0, e)):
            a = clamp(k2 * 3)
            px0, py0 = SG.CX - pw / 2, SG.SEAM_CY - ph / 2
            f.canvas.drawRRect(rrect(f, px0, py0 + 6, pw, ph, 24), paint("SHADOW", 0.38 * a, blur=14, f=f))
            fill_rrect(f, px0, py0, pw, ph, 24, "BG", 0.95 * a)
            fill_rrect(f, px0, py0, pw, ph * 0.48, 24, "NAVY_2", 0.42 * a)
            stroke_rrect(f, px0 + 1.5, py0 + 1.5, pw - 3, ph - 3, 22.5, accent, 3.4, 0.92 * a)
            brackets(f, px0, py0, pw, ph, accent, 0.88 * a, L=16, t=3.5, off=-5)

            model_sprite(f, "flash", px0 + 44.0, SG.SEAM_CY, 54.0, alpha=a, glow=False)
            model_sprite(f, "argon", px0 + pw - 44.0, SG.SEAM_CY, 54.0, alpha=a, glow=False)

            draw_text(
                f,
                "¿SE PUEDE CREAR UNA MARCA?",
                SG.CX,
                py0 + 60.0,
                "title",
                39.0,
                "INK",
                alpha=a,
                stroke=("#02050A", 4.6),
                shadow=("#000000", 0, 4, 8, 0.75),
            )
            draw_text(
                f,
                "COLECCION OVERFIT · 10 ARTES EN CODIGO",
                SG.CX,
                py0 + 113.0,
                "title",
                32.0,
                accent,
                alpha=a,
                stroke=("#02050A", 4.0),
                shadow=("#000000", 0, 4, 8, 0.75),
            )


def draw_cc01_summary_card(f: Frame, lt: float, dur: float) -> None:
    """Tarjeta de resumen de la marca OVERFIT y lo construido para @tenito03 (cero Versus / cero barras de batalla)."""
    SG.draw_short_bg(f, lt, 0.95)
    accent = "#22D3EE"
    col = "#B794F6"
    X = SG._exit(lt, dur, 0.22)
    with layer_alpha(f, X):
        ek = out_cubic(prog(lt, 0.0, 0.28))

        # 1. Pildora superior de identificacion
        hw, hh, hy = 920.0, 54.0, 224.0
        fill_rrect(f, SG.CX - hw / 2, hy, hw, hh, hh / 2, "NAVY", 0.95 * ek)
        stroke_rrect(f, SG.CX - hw / 2 + 1.5, hy + 1.5, hw - 3, hh - 3, hh / 2 - 1.5, accent, 2.5, 0.9 * ek)
        draw_text(
            f,
            "DEL COMENTARIO AL CODIGO #01 · PROPUESTA DE @TENITO03",
            SG.CX,
            hy + 36,
            "hud",
            22.0,
            accent,
            alpha=ek,
            tracking=2.0,
            stroke=("#02050A", 3.5),
        )

        # 2. Pildora de la marca creada (en cy = 360, arriba del sprite y lejos de subtitulos en y = 970)
        pw, ph, py = 780.0, 74.0, 348.0
        fill_rrect(f, SG.CX - pw / 2, py - ph / 2, pw, ph, ph / 2, "BG", 0.95 * ek)
        stroke_rrect(f, SG.CX - pw / 2 + 1.5, py - ph / 2 + 1.5, pw - 3, ph - 3, ph / 2 - 1.5, "#FBBF24", 2.8, 0.9 * ek)
        model_sprite(f, "flash", SG.CX - pw / 2 + 48, py, 44, alpha=ek, glow=False)
        model_sprite(f, "argon", SG.CX + pw / 2 - 48, py, 44, alpha=ek, glow=False)
        draw_text(
            f,
            "OVERFIT BY MIXIUH · DROP SS26",
            SG.CX,
            py + 11,
            "hud",
            28.0,
            "#FBBF24",
            alpha=ek,
            tracking=2.5,
            stroke=("#02050A", 3.5),
        )

        # 3. Sprite central de la playera 3D + corona
        ka = prog(lt, 0.05, 0.38)
        cy_sp = 530.0
        rays(f, SG.CX, cy_sp, lt, col, 0.16 * out_cubic(ka), n=16, r=480)
        soft_glow(f, SG.CX, cy_sp, 220, col, 0.22 * out_cubic(ka))
        sc = out_back(ka, 1.9)
        if sc > 0:
            with transformed(f, cx=SG.CX, cy=cy_sp, scale=sc):
                model_sprite(f, "argon", SG.CX, cy_sp + bob(lt, 7, 0.9), 156.0, glow=(col, 28, 0.7))
            kc = prog(lt, 0.25, 0.32)
            if kc > 0:
                _, hc = SP.sprite_size("crown", 1.0)
                SP.draw_sprite(
                    f,
                    "crown",
                    SG.CX,
                    cy_sp - 110.0 + (1 - out_back(kc, 2)) * -45 + bob(lt, 4, 0.9, 0.25),
                    40 / hc,
                    alpha=clamp(kc * 3),
                    glow=("FLASH", 14, 0.5),
                )
        star_burst(f, SG.CX, cy_sp, lt - 0.18, n=12, dist=340, px=3.0, seed=7, life=0.85)

        # 4. Titular 3D: "MARCA CREADA EN 3D"
        txt = "MARCA CREADA EN 3D"
        vpx = SG._ptext_fit(txt, 7.8, 900.0)
        ptitle(f, txt, SG.CX, 646.0, vpx, col, depth=3.5, glow=0.28 * ek)

        # 5. Tarjeta de resumen conceptual arriba de la costura
        rw, rh, ry = 910.0, 92.0, 734.0
        rx = SG.CX - rw / 2
        fill_rrect(f, rx, ry, rw, rh, 18, "NAVY", 0.94 * ek)
        stroke_rrect(f, rx + 1.5, ry + 1.5, rw - 3, rh - 3, 16.5, col, 2.4, 0.88 * ek)
        draw_text(
            f,
            "COLECCION GUERRA DE PESOS · 100% ALUCINADO",
            SG.CX,
            ry + 38,
            "hud",
            25.0,
            "#FBBF24",
            alpha=ek,
            tracking=1.5,
            stroke=("#02050A", 3.5),
        )
        draw_text(
            f,
            "MOCKUPS 300 GSM · 10 DISEÑOS IA · FRENTE+ESPALDA Y REDES",
            SG.CX,
            ry + 74,
            "hud",
            20.0,
            "INK",
            alpha=0.96 * ek,
            tracking=0.5,
            stroke=("#02050A", 3.0),
        )

        # 6. Tres tarjetas de arquitectura debajo de la costura (y >= 1060, nunca choca con subtitulos en y = 970)
        cards = [
            (
                "01 · MOCKUPS 300 GSM EN BLANCO",
                "MANIQUI HOMBRE, MUJER Y PRENDA FLAT-LAY EN BLENDER CYCLES",
                "6 TONOS DE ALGODON PEINADO + ONDA FISICA VERLET EN VIVO",
                "#22D3EE",
                0.20,
            ),
            (
                "02 · 10 DISEÑOS SATIRICOS DE IA (OVERFIT)",
                "STRAWBERRY · VIBE CODING · CUDA POOR · BENCHMARK · OPEN SOURCE",
                "CENSURA · TABLA NUTRICIONAL LLM · AGI · DEV C++ · TRANVIA TOKENS",
                "#FBBF24",
                0.36,
            ),
            (
                "03 · PERSONALIZACION Y CASOS DE USO",
                "ESCALA · ALTURA · RELIEVE PUFF · PLASTISOL · FRENTE + ESPALDA (#07)",
                "EXPORTACION DIRECTA: INSTAGRAM REEL 9:16 + LOOKBOOK + PNG 4K",
                "#34D399",
                0.52,
            ),
        ]
        cy0 = 1066.0
        ch_card = 142.0
        cgap = 22.0
        for idx, (c_head, c_l1, c_l2, c_col, t_in) in enumerate(cards):
            kc_i = out_back(prog(lt, t_in, 0.30), 1.35)
            if kc_i <= 0:
                continue
            y_box = cy0 + idx * (ch_card + cgap)
            with transformed(f, cx=SG.CX, cy=y_box + ch_card / 2, scale=lerp(0.88, 1.0, kc_i)):
                a_c = clamp(kc_i * 3.0)
                fill_rrect(f, rx, y_box, rw, ch_card, 18, "NAVY", 0.95 * a_c)
                stroke_rrect(f, rx + 1.5, y_box + 1.5, rw - 3, ch_card - 3, 16.5, c_col, 2.6, 0.92 * a_c)
                draw_text(
                    f,
                    c_head,
                    rx + 24,
                    y_box + 40,
                    "hud",
                    24.0,
                    c_col,
                    alpha=a_c,
                    align="left",
                    tracking=1.5,
                    stroke=("#02050A", 3.5),
                )
                draw_text(
                    f,
                    c_l1,
                    rx + 24,
                    y_box + 82,
                    "hud",
                    19.5,
                    "INK",
                    alpha=a_c,
                    align="left",
                    stroke=("#02050A", 3.0),
                )
                draw_text(
                    f,
                    c_l2,
                    rx + 24,
                    y_box + 118,
                    "hud",
                    18.5,
                    "CYAN",
                    alpha=a_c,
                    align="left",
                    stroke=("#02050A", 3.0),
                )


def draw_cc01_endtag(f: Frame, lt: float, dur: float) -> None:
    """Pantalla final de cierre con disparadores visuales de accion (YouTube, Like, Seguir, Guardar, Compartir, Web)
    y encabezado de 'Del Comentario al Codigo #01' sin marcador de batalla."""
    SG.short_endtag(
        f,
        lt,
        dur,
        {
            "ep_id": "01",
            "reto": 1,
            "total": 1,
            "winner": "argon",
        },
    )
    # Sobrescribimos limpiamente la tarjeta superior (y=232, h=104) para mostrar la seccion y la marca OVERFIT
    # en lugar del marcador "OPUS 5.5 [0] - [0] ARGON"
    X = SG._exit(lt, dur, 0.12)
    kh = out_cubic(prog(lt, 0.0, 0.25)) * X
    if kh > 0:
        top_w, top_h, top_y = 924.0, 108.0, 230.0
        fill_rrect(f, SG.CX - top_w / 2, top_y, top_w, top_h, 24, "NAVY", 0.98 * kh)
        stroke_rrect(f, SG.CX - top_w / 2 + 1.5, top_y + 1.5, top_w - 3, top_h - 3, 22.5, "#22D3EE", 2.8, 0.95 * kh)
        draw_text(
            f,
            "DEL COMENTARIO AL CODIGO #01 · RETO @TENITO03",
            SG.CX,
            top_y + 44,
            "hud",
            24.0,
            "#22D3EE",
            alpha=kh,
            tracking=2.0,
            stroke=("#02050A", 3.5),
        )
        draw_text(
            f,
            "OVERFIT STUDIO 3D · 10 ARTES + MOCKUPS 300 GSM",
            SG.CX,
            top_y + 84,
            "hud",
            22.0,
            "#FBBF24",
            alpha=kh,
            tracking=2.0,
            stroke=("#02050A", 3.0),
        )


def group_words_for_reel(words: list[dict], t_offset: float) -> list[dict]:
    """Groups word timings into punchy 2-4 word caption chunks compatible with SG.short_captions."""
    groups = []
    cur = []
    for w in words:
        token = str(w["word"]).strip()
        if not token:
            continue
        item = {
            "w": token,
            "t0": float(w["start"]) + t_offset,
            "t1": float(w["end"]) + t_offset,
        }
        cur.append(item)
        char_len = sum(len(x["w"]) for x in cur) + max(0, len(cur) - 1)
        ends_punct = token.endswith((".", ",", ":", ";", "?", "!", "¿", "¡"))
        if len(cur) >= 4 or char_len >= 20 or (ends_punct and len(cur) >= 2):
            groups.append({
                "t0": cur[0]["t0"],
                "t1": cur[-1]["t1"] + 0.12,
                "text": " ".join(x["w"] for x in cur),
                "words": cur,
            })
            cur = []
    if cur:
        groups.append({
            "t0": cur[0]["t0"],
            "t1": cur[-1]["t1"] + 0.15,
            "text": " ".join(x["w"] for x in cur),
            "words": cur,
        })
    for i in range(len(groups) - 1):
        if groups[i]["t1"] > groups[i + 1]["t0"]:
            groups[i]["t1"] = groups[i + 1]["t0"]
    return groups


def build_reel_9x16() -> tuple[Path, Path]:
    print("\n=== [1/3] Building 9:16 Video Response Reel (1080x1920 @ 60fps & 4K 2160x3840 @ 60fps) ===", flush=True)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "shorts").mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "thumbnails").mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "miniaturas_4k").mkdir(parents=True, exist_ok=True)

    configure_cc01_models()

    vc = VoicefyClient(str(MLABS_ROOT / ".cache" / "voice" / "raw"))
    sr = 48000

    # 1. Synthesize all 6 Reel beats via Voicefy (cached)
    beat_records = []
    cur_t = 0.16
    all_caption_groups = []
    voice_tracks = []
    sfx_events = []

    for b in REEL_BEATS:
        print(f"  [Voicefy] Synthesizing {b['id']}: {b['say'][:60]}...", flush=True)
        res = vc.synthesize(
            b["say"],
            pron_map=PRON_EXTRAS,
            stability=0.5,
            speed=b["speed"],
            seed=7,
        )
        wav_data, wav_sr = sf.read(str(res.wav), dtype="float32")
        if wav_data.ndim > 1:
            wav_data = wav_data.mean(axis=1)
        dur = len(wav_data) / wav_sr

        t0 = cur_t
        t1 = t0 + dur + 0.08
        voice_tracks.append((t0, wav_data))
        c_groups = group_words_for_reel(res.words, t0)
        all_caption_groups.extend(c_groups)

        for sfx_name, sfx_rel, sfx_db in b.get("sfx", []):
            sfx_events.append((t0 + sfx_rel, sfx_name, sfx_db))

        beat_records.append({
            **b,
            "t0": t0,
            "t1": t1,
            "speech_dur": dur,
        })
        cur_t = t1

    total_dur = cur_t + 1.85
    total_samples = int(math.ceil(total_dur * sr))
    print(f"  [Reel Timeline] Total duration: {total_dur:.2f}s ({len(beat_records)} beats)", flush=True)

    # 2. Mix Audio (Voice + Chiptune Music + Stingers + 8-bit SFX -> -14.0 LUFS)
    voice_bus = np.zeros((total_samples, 2), dtype=np.float32)
    voice_env = np.zeros(total_samples, dtype=np.float32)
    for t0, w_mono in voice_tracks:
        idx0 = int(round(t0 * sr))
        idx1 = min(total_samples, idx0 + len(w_mono))
        seg = w_mono[: idx1 - idx0]
        voice_bus[idx0:idx1, 0] += seg
        voice_bus[idx0:idx1, 1] += seg
        voice_env[idx0:idx1] = 1.0

    win = int(0.08 * sr)
    if win > 1:
        kernel = np.ones(win, dtype=np.float32) / win
        voice_env = np.convolve(voice_env, kernel, mode="same")

    music_events = [
        {"cue": "hook", "t0": 0.0, "t1": beat_records[1]["t1"], "gain_db": 0.0},
        {"cue": "battle", "t0": beat_records[1]["t1"], "t1": beat_records[-1]["t0"], "gain_db": 0.0},
        {"cue": "outro", "t0": beat_records[-1]["t0"], "t1": total_dur, "gain_db": 0.0},
    ]
    stingers = [{"cue": "victory", "t": beat_records[-1]["t0"], "gain_db": -2.0}]
    music_bus = chiptune.render(music_events, stingers, total_dur, sr=sr, seed=21)
    if len(music_bus) < total_samples:
        music_bus = np.pad(music_bus, ((0, total_samples - len(music_bus)), (0, 0)))
    else:
        music_bus = music_bus[:total_samples]

    duck_gain = 10.0 ** ((-14.0 * voice_env - 5.0 * (1.0 - voice_env)) / 20.0)
    music_bus *= duck_gain[:, None]

    sfx_bus = np.zeros((total_samples, 2), dtype=np.float32)
    for t_ev, s_name, s_db in sfx_events:
        s_mono = sfx8.synth(s_name, sr=sr) * (10.0 ** ((s_db - 6.0) / 20.0))
        i0 = int(round(t_ev * sr))
        i1 = min(total_samples, i0 + len(s_mono))
        if i1 > i0:
            sfx_bus[i0:i1, 0] += s_mono[: i1 - i0]
            sfx_bus[i0:i1, 1] += s_mono[: i1 - i0]

    mix = voice_bus * 1.15 + music_bus + sfx_bus
    meter = pyln.Meter(sr)
    loudness = meter.integrated_loudness(mix)
    if np.isfinite(loudness):
        mix = pyln.normalize.loudness(mix, loudness, -14.0)
    peak = np.max(np.abs(mix))
    limit = 10.0 ** (-1.5 / 20.0)
    if peak > limit:
        mix = np.tanh(mix / limit) * limit

    mix_wav_path = BUILD_DIR / "reel_mix.wav"
    sf.write(str(mix_wav_path), mix, sr, subtype="PCM_24")
    final_lufs = meter.integrated_loudness(mix)
    print(f"  [Reel Audio] Mixed to {final_lufs:.2f} LUFS ({mix_wav_path.name})", flush=True)

    # 3. Render 1080x1920 @ 60fps master frames
    W, H = 1080, 1920
    FPS = 60
    total_frames = int(round(total_dur * FPS))
    set_design(W, H)

    bgr_comment_raw = cv2.imread(str(COMMENT_IMG_PATH))
    ih, iw = bgr_comment_raw.shape[:2]
    crop_comment = bgr_comment_raw[0:ih, 0 : int(iw * 0.86)]

    # Preload 2K UHD artwork images for crisp showcase cards in the top panel
    design_skia_imgs: dict[int, skia.Image] = {}
    for spec in OVERFIT_DESIGN_SPECS:
        art_p = EP_DIR / "app" / "assets" / "overfit" / spec["file"]
        if art_p.exists():
            raw_bgra = cv2.imread(str(art_p), cv2.IMREAD_UNCHANGED)
            if raw_bgra is not None:
                if raw_bgra.shape[2] == 4:
                    rgba_art = cv2.cvtColor(raw_bgra, cv2.COLOR_BGRA2RGBA)
                else:
                    rgba_art = cv2.cvtColor(raw_bgra, cv2.COLOR_BGR2RGBA)
                # Downscale smoothly to 680x910 for crisp, fast Skia drawing in 1080p panel
                rgba_art = cv2.resize(rgba_art, (680, 910), interpolation=cv2.INTER_AREA)
                design_skia_imgs[spec["idx"]] = skia.Image.fromarray(rgba_art)

    cap_top = cv2.VideoCapture(str(STUDIO_MOV_PATH))
    cap_bot = cv2.VideoCapture(str(STUDIO_MOV_PATH))
    v_fps = cap_top.get(cv2.CAP_PROP_FPS) or 60.0
    v_total = int(cap_top.get(cv2.CAP_PROP_FRAME_COUNT) or 3240)
    v_dur_sec = max(1.0, (v_total - 1) / v_fps)
    reader_state = {
        "top": {"cap": cap_top, "idx": -999, "bgr": None},
        "bot": {"cap": cap_bot, "idx": -999, "bgr": None},
    }

    def get_studio_frame(slot: str, s_idx: int) -> np.ndarray | None:
        st = reader_state[slot]
        cap = st["cap"]
        if s_idx == st["idx"] and st["bgr"] is not None:
            return st["bgr"]
        if st["idx"] >= 0 and 0 < (s_idx - st["idx"]) <= 6:
            ok = True
            bgr = st["bgr"]
            for _ in range(s_idx - st["idx"]):
                ok, bgr = cap.read()
            if ok and bgr is not None:
                st["idx"] = s_idx
                st["bgr"] = bgr
                return bgr
        cap.set(cv2.CAP_PROP_POS_FRAMES, s_idx)
        ok, bgr = cap.read()
        if ok and bgr is not None:
            st["idx"] = s_idx
            st["bgr"] = bgr
            return bgr
        return st["bgr"]

    def draw_mobile_comment_in_rect(f: Frame, panel_rect: list[float], step_done: int = 3) -> None:
        px, py, pw, ph = panel_rect
        c = f.canvas
        c.save()
        c.clipRRect(rrect(f, px, py, pw, ph, 18.0), skia.ClipOp.kIntersect, True)
        fill_rrect(f, px, py, pw, ph, 18.0, "#071426", 0.98)

        card_w = pw - 44.0
        card_h = card_w * (crop_comment.shape[0] / crop_comment.shape[1])
        card_x = px + 22.0
        card_y = py + 84.0

        fill_rrect(f, card_x - 6, card_y - 6, card_w + 12, card_h + 12, 14.0, "#FFFFFF", 1.0)
        stroke_rrect(f, card_x - 6, card_y - 6, card_w + 12, card_h + 12, 14.0, "#22D3EE", 4.0, 1.0)

        tw = max(1, int(round(card_w * f.s)))
        th = max(1, int(round(card_h * f.s)))
        resized = cv2.resize(crop_comment, (tw, th), interpolation=cv2.INTER_CUBIC)
        rgba = cv2.cvtColor(resized, cv2.COLOR_BGR2RGBA)
        sk_img = skia.Image.fromarray(rgba)
        c.drawImageRect(sk_img, f.rect(card_x, card_y, card_w, card_h))

        badges = [
            ("1. MOCKUP 300G", "#34D399"),
            ("2. 10 ARTES IA", "#22D3EE"),
            ("3. PERSONALIZAR", "#FBBF24"),
        ]
        by = card_y + card_h + 22.0
        bw = (card_w - 24.0) / 3.0
        bh = 52.0
        for idx, (btxt, bcol) in enumerate(badges):
            bx = card_x + idx * (bw + 12.0)
            active = step_done >= (idx + 1)
            fill_rrect(f, bx, by, bw, bh, 10.0, "#060B14", 0.96 if active else 0.75)
            stroke_rrect(f, bx, by, bw, bh, 10.0, bcol, 3.0 if active else 2.0, 0.95 if active else 0.55)
            draw_text(f, btxt, bx + bw / 2, by + 33.0, "hud", 20.0, bcol, stroke=("#02050A", 3.0))

        c.restore()

    def draw_overfit_design_card_in_rect(f: Frame, panel_rect: list[float], design_idx: int = 1) -> None:
        px, py, pw, ph = panel_rect
        spec = OVERFIT_DESIGN_SPECS[max(0, min(len(OVERFIT_DESIGN_SPECS) - 1, design_idx - 1))]
        acc = spec["accent"]
        c = f.canvas
        c.save()
        c.clipRRect(rrect(f, px, py, pw, ph, 18.0), skia.ClipOp.kIntersect, True)
        fill_rrect(f, px, py, pw, ph, 18.0, "#071324", 0.99)

        # Left 2K artwork frame (below top chips at y = py + 76)
        art_x = px + 20.0
        art_y = py + 78.0
        art_w = 306.0
        art_h = ph - 92.0
        fill_rrect(f, art_x, art_y, art_w, art_h, 14.0, "#040811", 1.0)
        stroke_rrect(f, art_x, art_y, art_w, art_h, 14.0, acc, 3.2, 0.96)

        sk_art = design_skia_imgs.get(spec["idx"])
        if sk_art is not None:
            pad = 10.0
            iw_a = art_w - pad * 2
            ih_a = art_h - pad * 2
            c.drawImageRect(sk_art, f.rect(art_x + pad, art_y + pad, iw_a, ih_a))

        # Right technical & satirical breakdown card
        rx = art_x + art_w + 20.0
        rw = pw - (rx - px) - 20.0
        ry = art_y

        # Code & Design number pill
        fill_rrect(f, rx, ry, rw, 44.0, 10.0, "#0B1E36", 0.96)
        stroke_rrect(f, rx, ry, rw, 44.0, 10.0, acc, 2.2, 0.9)
        draw_text(
            f,
            f"{spec['code']} · ARTE 2K UHD (1792x2400)",
            rx + 16.0,
            ry + 30.0,
            "hud",
            18.0,
            acc,
            align="left",
            tracking=0.4,
            stroke=("#02050A", 2.8),
        )

        # Design Title
        draw_text(
            f,
            spec["title"],
            rx + 4.0,
            ry + 92.0,
            "title",
            34.0,
            "INK",
            align="left",
            stroke=("#02050A", 4.2),
        )

        # Satirical English/Spanish Subtitle
        draw_text(
            f,
            spec["sub"],
            rx + 4.0,
            ry + 132.0,
            "hud",
            20.0,
            "#FBBF24",
            align="left",
            stroke=("#02050A", 3.0),
        )

        # Meaning / Explanation box
        exp_y = ry + 152.0
        exp_h = 114.0
        fill_rrect(f, rx, exp_y, rw, exp_h, 12.0, "#050B14", 0.95)
        stroke_rrect(f, rx, exp_y, rw, exp_h, 12.0, "#1E3A5F", 2.0, 0.9)
        draw_text(
            f,
            "SIGNIFICADO SATIRICO:",
            rx + 16.0,
            exp_y + 32.0,
            "hud",
            17.5,
            "#22D3EE",
            align="left",
            tracking=1.0,
            stroke=("#02050A", 2.5),
        )
        draw_text(
            f,
            spec["desc1"],
            rx + 16.0,
            exp_y + 66.0,
            "hud",
            20.0,
            "INK",
            align="left",
            stroke=("#02050A", 3.0),
        )
        draw_text(
            f,
            spec["desc2"],
            rx + 16.0,
            exp_y + 98.0,
            "hud",
            20.0,
            "INK",
            align="left",
            stroke=("#02050A", 3.0),
        )

        # Sleeve print quote pill
        sl_y = exp_y + exp_h + 14.0
        fill_rrect(f, rx, sl_y, rw, 50.0, 10.0, "#062019", 0.95)
        stroke_rrect(f, rx, sl_y, rw, 50.0, 10.0, "#34D399", 2.2, 0.92)
        draw_text(
            f,
            spec["sleeve"],
            rx + 16.0,
            sl_y + 33.0,
            "hud",
            19.5,
            "#34D399",
            align="left",
            stroke=("#02050A", 3.0),
        )

        # Bottom indicator pointing to live 3D shirt below
        bot_y = sl_y + 62.0
        draw_text(
            f,
            "ABAJO: EN VIVO SOBRE ALGODON 300 GSM (LUPA 260%)",
            rx + 4.0,
            bot_y + 22.0,
            "hud",
            16.0,
            "#CBD5E1",
            align="left",
            stroke=("#02050A", 2.6),
        )

        c.restore()

    def draw_studio_clip_in_rect(
        f: Frame,
        sec: float,
        crop_box: tuple[int, int, int, int],
        panel_rect: list[float],
        inset_top: float = 78.0,
        inset_bottom: float = 6.0,
        slot: str = "bot",
        zoom: float = 1.0,
    ) -> None:
        s_idx = max(0, min(v_total - 1, int(round((sec % v_dur_sec) * v_fps))))
        bgr = get_studio_frame(slot, s_idx)
        if bgr is None:
            return
        ih_src, iw_src = bgr.shape[:2]
        cx, cy, cw, ch = crop_box
        px, py, pw, ph = panel_rect
        c = f.canvas
        c.save()
        c.clipRRect(rrect(f, px, py, pw, ph, 18.0), skia.ClipOp.kIntersect, True)
        fill_rrect(f, px, py, pw, ph, 18.0, "#060E1B", 1.0)

        dy = py + inset_top
        dh = max(10.0, ph - inset_top - inset_bottom)
        dst_aspect = pw / dh
        ccx = cx + cw / 2.0
        ccy = cy + ch / 2.0

        # Expand crop_box within the 1920x1080 studio frame so it matches dst_aspect naturally without border stripes
        if (cw / max(1.0, float(ch))) < dst_aspect:
            new_cw = min(iw_src, int(round(ch * dst_aspect)))
            new_ch = min(ih_src, max(1, int(round(new_cw / dst_aspect))))
        else:
            new_ch = min(ih_src, int(round(cw / dst_aspect)))
            new_cw = min(iw_src, max(1, int(round(new_ch * dst_aspect))))

        if zoom > 1.001:
            new_cw = max(64, int(round(new_cw / zoom)))
            new_ch = max(64, int(round(new_ch / zoom)))

        max_bot_y = min(ih_src, 882)
        x0 = max(0, min(iw_src - new_cw, int(round(ccx - new_cw / 2.0))))
        y0 = max(84, min(max_bot_y - new_ch, int(round(ccy - new_ch / 2.0))))
        y0 = max(0, min(ih_src - new_ch, y0))
        src_img = bgr[y0 : y0 + new_ch, x0 : x0 + new_cw]

        tw = max(1, int(round(pw * f.s)))
        th = max(1, int(round(dh * f.s)))
        resized = cv2.resize(src_img, (tw, th), interpolation=cv2.INTER_AREA)
        rgba = cv2.cvtColor(resized, cv2.COLOR_BGR2RGBA)
        sk_img = skia.Image.fromarray(rgba)
        c.drawImageRect(sk_img, f.rect(px, dy, pw, dh))
        c.restore()

    def render_dynamic_slot(
        f: Frame,
        clips: list[dict],
        bt_local: float,
        bt_dur: float,
        panel_rect: list[float],
        inset_top: float,
        inset_bottom: float,
        slot: str,
    ) -> None:
        if not clips:
            return
        n_c = len(clips)
        seg_dur = bt_dur / n_c
        c_idx = min(n_c - 1, int(bt_local / max(0.01, seg_dur)))
        sub_local = bt_local - c_idx * seg_dur
        sub_frac = clamp(sub_local / max(0.01, seg_dur))
        clip = clips[c_idx]
        if clip.get("mode") == "comment":
            draw_mobile_comment_in_rect(f, panel_rect, step_done=int(clip.get("step_done", 3)))
        elif clip.get("mode") == "design_card":
            draw_overfit_design_card_in_rect(f, panel_rect, design_idx=int(clip.get("design_idx", 1)))
        else:
            z = lerp(float(clip.get("z0", 1.0)), float(clip.get("z1", 1.06)), sub_frac)
            draw_studio_clip_in_rect(
                f,
                float(clip["t0"]) + sub_local * 0.45,
                clip["roi"],
                panel_rect,
                inset_top=inset_top,
                inset_bottom=inset_bottom,
                slot=slot,
                zoom=z,
            )

    raw_video_mp4 = BUILD_DIR / "reel_video_raw.mp4"
    ff = subprocess.Popen(
        [
            "/opt/homebrew/bin/ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "rgba",
            "-s",
            f"{W}x{H}",
            "-r",
            str(FPS),
            "-i",
            "-",
            "-c:v",
            "h264_videotoolbox",
            "-b:v",
            "32M",
            "-pix_fmt",
            "yuv420p",
            str(raw_video_mp4),
        ],
        stdin=subprocess.PIPE,
    )

    hook_end_t = 2.2
    last_beat = beat_records[-1]
    summary_t0 = last_beat["t0"]
    summary_dur = max(3.6, last_beat["speech_dur"] * 0.62)
    endtag_t0 = summary_t0 + summary_dur

    cover_saved = False

    for f_idx in range(total_frames):
        t = f_idx / FPS

        active_beat = beat_records[-1]
        for b in beat_records:
            if b["t0"] <= t < b["t1"]:
                active_beat = b
                break
            elif t < b["t0"]:
                active_beat = b
                break

        bt_local = max(0.0, t - active_beat["t0"])
        bt_dur = max(0.01, active_beat["t1"] - active_beat["t0"])
        bt_frac = min(1.0, bt_local / bt_dur)

        f, _, surf = new_frame(W, H, t=t, fps=FPS)

        if t < hook_end_t:
            # 1. GANCHO / PORTADA (0.0s .. 2.2s) — Cero elementos Versus
            SG.draw_short_bg(f, t, 1.0)
            draw_mobile_comment_in_rect(f, SG.FLASH_RECT, step_done=3)
            hook_src_t = 6.1 + t * 0.4 if t < 1.15 else 7.15 + (t - 1.15) * 0.4
            draw_studio_clip_in_rect(
                f,
                hook_src_t,
                (464, 96, 982, 760),
                SG.ARGON_RECT,
                inset_top=26.0,
                inset_bottom=80.0,
                zoom=1.0 + 0.04 * (t / hook_end_t),
            )
            p_hook = {
                "active": "both",
                "chips": True,
                "is_hook": True,
                "reto": 1,
                "total": 1,
            }
            SG.short_panels(f, t, hook_end_t, p_hook)
            draw_cc01_hook(f, t, hook_end_t)
            if t >= 1.4:
                SG.short_captions(f, t, total_dur, {"groups": all_caption_groups})

        elif t < summary_t0:
            # 2. DESARROLLO PRINCIPAL CON MULTI-CORTES DINAMICOS (FRENTE, PECHO, ESPALDA, DUAL, FLAT-LAY, REDES)
            SG.draw_short_bg(f, t, 1.0)
            render_dynamic_slot(
                f,
                active_beat["top_clips"],
                bt_local,
                bt_dur,
                SG.FLASH_RECT,
                inset_top=76.0,
                inset_bottom=6.0,
                slot="top",
            )
            render_dynamic_slot(
                f,
                active_beat["bot_clips"],
                bt_local,
                bt_dur,
                SG.ARGON_RECT,
                inset_top=78.0,
                inset_bottom=6.0,
                slot="bot",
            )

            SG.short_panels(
                f,
                t - hook_end_t,
                summary_t0 - hook_end_t,
                {
                    "active": "both",
                    "chips": True,
                    "reto": 1,
                    "total": 1,
                },
            )
            SG.short_title(
                f,
                bt_local,
                bt_dur,
                {
                    "ep_id": "CC.01",
                    "reto": 1,
                    "total": 1,
                    "kicker": active_beat["kicker"],
                    "title": active_beat["title"],
                },
            )

            pop = active_beat.get("pop")
            if pop and bt_frac >= pop["at_frac"]:
                pop_age = (bt_frac - pop["at_frac"]) * bt_dur
                SG.short_pop(
                    f,
                    pop_age,
                    2.5,
                    {
                        "text": pop["text"],
                        "sub": pop["sub"],
                        "color": pop["color"],
                        "cy": 1685,
                    },
                )

            SG.short_captions(f, t, total_dur, {"groups": all_caption_groups})

        elif t < endtag_t0:
            # 3. TARJETA RESUMEN DE LA COLECCION OVERFIT (Cero Versus / Cero Marcador)
            draw_cc01_summary_card(f, t - summary_t0, summary_dur)
            SG.short_captions(f, t, total_dur, {"groups": all_caption_groups})

        else:
            # 4. PANTALLA FINAL DE CIERRE (ENDTAG) CON SUBTITULOS ABAJO EN Y=1545 (NUNCA TAPAN ICONOS)
            draw_cc01_endtag(f, t - endtag_t0, total_dur - endtag_t0)
            SG.short_captions(f, t, total_dur, {"groups": all_caption_groups, "cy": 1545.0})

        snap = surf.makeImageSnapshot()
        if not cover_saved and f_idx == int(round(0.85 * FPS)):
            arr = np.frombuffer(snap.tobytes(), dtype=np.uint8).reshape((H, W, 4))
            bgr_1080 = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)
            cover_path = OUT_DIR / "thumbnails" / "reel_cover_9x16.jpg"
            cv2.imwrite(str(cover_path), bgr_1080, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
            bgr_4k = cv2.resize(bgr_1080, (2160, 3840), interpolation=cv2.INTER_LANCZOS4)
            cv2.imwrite(str(OUT_DIR / "miniaturas_4k" / "01_respuesta-tenito03-marca-ropa-verlet.png"), bgr_4k)
            cover_saved = True

        ff.stdin.write(snap.tobytes())

    ff.stdin.close()
    ff.wait()
    cap_top.release()
    cap_bot.release()

    # 4. Mux 1080p60 Reel and Upscale 4K60 (2160x3840 @ 60fps) Reel
    out_1080p = OUT_DIR / "shorts" / "01_respuesta-tenito03-marca-ropa-verlet_1080p60.mp4"
    out_4k = OUT_DIR / "shorts" / "01_respuesta-tenito03-marca-ropa-verlet_4k60.mp4"

    subprocess.run(
        [
            "/opt/homebrew/bin/ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(raw_video_mp4),
            "-i",
            str(mix_wav_path),
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "320k",
            "-movflags",
            "+faststart",
            str(out_1080p),
        ],
        check=True,
    )

    subprocess.run(
        [
            "/opt/homebrew/bin/ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(out_1080p),
            "-vf",
            "scale=2160:3840:flags=lanczos,cas=0.35",
            "-c:v",
            "h264_videotoolbox",
            "-b:v",
            "55M",
            "-maxrate",
            "75M",
            "-bufsize",
            "110M",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "copy",
            "-movflags",
            "+faststart",
            str(out_4k),
        ],
        check=True,
    )

    print(
        f"  [Reel Done] 1080p60: {out_1080p.stat().st_size / (1024*1024):.1f} MB | "
        f"4K60: {out_4k.stat().st_size / (1024*1024):.1f} MB",
        flush=True,
    )
    return out_1080p, out_4k


def build_youtube_16x9(package_only: bool = False) -> Path:
    print("\n=== [2/3] Building 16:9 YouTube Episode in 4K60 via mlabs pipeline ===", flush=True)
    ep_yaml = MLABS_ROOT / "episodes" / "cc01-marca-ropa-verlet" / "episode.yaml"
    stages = "package" if package_only else "voice,timeline,music,mix,video,mux,package"
    cmd = [
        str(MLABS_ROOT / ".venv" / "bin" / "python"),
        "-m",
        "mlabs",
        "build",
        str(ep_yaml),
        "--only",
        stages,
    ]
    subprocess.run(cmd, cwd=str(MLABS_ROOT), check=True)

    mlabs_out = MLABS_ROOT / "episodes" / "cc01-marca-ropa-verlet" / "out"

    for fn in (
        "del-comentario-al-codigo-01-marca-ropa-verlet_2160p60.mp4",
        "captions_es.srt",
        "captions_es.vtt",
        "youtube.md",
        "youtube.json",
    ):
        src = mlabs_out / fn
        if src.exists():
            shutil.copy2(src, OUT_DIR / fn)

    thumbs_src = mlabs_out / "thumbnails"
    if thumbs_src.exists():
        (OUT_DIR / "thumbnails").mkdir(parents=True, exist_ok=True)
        (OUT_DIR / "miniaturas_4k").mkdir(parents=True, exist_ok=True)
        for tf in thumbs_src.iterdir():
            if tf.is_file():
                shutil.copy2(tf, OUT_DIR / "thumbnails" / tf.name)
        for tid in ("A", "B", "C"):
            src_jpg = thumbs_src / f"thumb_{tid}.jpg"
            if src_jpg.exists():
                bgr = cv2.imread(str(src_jpg))
                if bgr is not None:
                    bgr_4k = cv2.resize(bgr, (3840, 2160), interpolation=cv2.INTER_LANCZOS4)
                    cv2.imwrite(str(OUT_DIR / "miniaturas_4k" / f"thumb_{tid}_4k.png"), bgr_4k)

    return OUT_DIR / "del-comentario-al-codigo-01-marca-ropa-verlet_2160p60.mp4"


def sync_to_icloud() -> None:
    print(f"\n=== [3/3] Syncing Complete Package to iCloud Drive: {ICLOUD_DIR} ===", flush=True)
    ICLOUD_DIR.mkdir(parents=True, exist_ok=True)
    for sub in ("app", "comentario-original", "guion", "programacion", "entregables_finales_4k"):
        src_d = EP_DIR / sub
        dst_d = ICLOUD_DIR / sub
        if src_d.exists():
            if dst_d.exists():
                shutil.rmtree(dst_d)
            shutil.copytree(src_d, dst_d)
    print("  [iCloud Sync Complete]", flush=True)


def main() -> None:
    t0 = time.time()
    pkg_only = "--package-only" in sys.argv
    if "--youtube-only" not in sys.argv:
        build_reel_9x16()
    if "--reel-only" not in sys.argv:
        build_youtube_16x9(package_only=pkg_only)
    sync_to_icloud()
    print(f"\nALL DELIVERABLES COMPLETED IN {time.time() - t0:.1f}s!", flush=True)


if __name__ == "__main__":
    main()
