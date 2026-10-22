#!/usr/bin/env python3
"""
Builds 6 side-by-side 1920x1080 comparison composites (Raw vs Superpowers Kit)
and 1 master scoreboard graphic using Skia + the real Playwright screenshots.
"""
from __future__ import annotations

import shutil
from pathlib import Path
import skia

BENCH_DIR = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep03-superpowers-kit/benchmark")
SHOTS_DIR = BENCH_DIR / "screenshots"
OUT_DIR = BENCH_DIR / "composites"
ART_DIR = Path("/Users/kevingonzalezlopez/.gemini/antigravity/brain/f7f21679-195b-4060-b55b-03feb3817e4f")
OUT_DIR.mkdir(parents=True, exist_ok=True)

ROUNDS = [
    {
        "num": "01",
        "slug": "01-galaxia-nbody",
        "out": "ep03_vs_01_galaxia.png",
        "title": "PRUEBA 01/06 · COLISION GALACTICA N-BODY 3D (48,000 ESTRELLAS)",
        "accent": 0xFF22D3EE,
        "winner": "SUPERKIT",
        "score": "SIN KIT 0 - 1 SUPERKIT",
        "raw_stats": "45.2 MIN · $1.26 USD · 897K TOK · 2,475 LOC · 1 ERROR 404",
        "kit_stats": "44.3 MIN · $2.25 USD · 4.52M TOK · 2,614 LOC · 0 ERRORES + POZO 3D",
        "verdict": "GANADOR: SUPERKIT — 0 errores en consola (Auto-Debugger) y malla de pozo gravitacional 3D mas profunda.",
    },
    {
        "num": "02",
        "slug": "02-terminal-trading",
        "out": "ep03_vs_02_trading.png",
        "title": "PRUEBA 02/06 · TERMINAL INSTITUCIONAL HFT & MICROESTRUCTURA",
        "accent": 0xFF10B981,
        "winner": "SUPERKIT",
        "score": "SIN KIT 0 - 2 SUPERKIT",
        "raw_stats": "73.2 MIN · $1.75 USD · 1.10M TOK · 3,899 LOC · 11,073 ORD/S",
        "kit_stats": "57.3 MIN · $1.56 USD · 975K TOK · 2,918 LOC · 70,406 ORD/S (6.3X)",
        "verdict": "GANADOR: SUPERKIT — 16 min mas rapido, mas barato ($1.56 vs $1.75) y 6.3x mayor throughput con buffers Zero-GC.",
    },
    {
        "num": "03",
        "slug": "03-arcade-boss-rush",
        "out": "ep03_vs_03_arcade.png",
        "title": "PRUEBA 03/06 · CYBER-SYNTH BULLET-HELL BOSS RUSH",
        "accent": 0xFFF472B6,
        "winner": "SIN KIT",
        "score": "SIN KIT 1 - 2 SUPERKIT",
        "raw_stats": "51.1 MIN · $1.64 USD · 2.28M TOK · 2,703 LOC · 379 BALAS @ 61 FPS",
        "kit_stats": "69.1 MIN · $1.68 USD · 1.29M TOK · 2,635 LOC · 96 BALAS @ 61 FPS",
        "verdict": "GANADOR: IA SIN KIT — Gemini 4 Argon High en crudo genero patrones danmaku 4x mas densos y termino 18 min antes.",
    },
    {
        "num": "04",
        "slug": "04-red-zero-trust",
        "out": "ep03_vs_04_zerotrust.png",
        "title": "PRUEBA 04/06 · CENTRO DE COMANDO CIBER-DEFENSA ZERO-TRUST 3D",
        "accent": 0xFFFBBF24,
        "winner": "SIN KIT",
        "score": "SIN KIT 2 - 2 SUPERKIT",
        "raw_stats": "23.5 MIN · $0.74 USD · 190K TOK (5 PASOS) · 2,367 LOC · 60 FPS",
        "kit_stats": "42.8 MIN · $2.04 USD · 2.59M TOK (32 PASOS) · 2,596 LOC · 60 FPS",
        "verdict": "GANADOR: IA SIN KIT — Resolucion one-shot en 5 pasos ($0.74 vs $2.04) con etiquetas 3D flotantes en cada nodo.",
    },
    {
        "num": "05",
        "slug": "05-motor-nodos-ia",
        "out": "ep03_vs_05_nodos.png",
        "title": "PRUEBA 05/06 · ESTUDIO PROCEDURAL DE NODOS DAG & RAYMARCHING GLSL",
        "accent": 0xFFFB923C,
        "winner": "SUPERKIT",
        "score": "SIN KIT 2 - 3 SUPERKIT",
        "raw_stats": "54.8 MIN · $1.58 USD · 1.46M TOK · 3,162 LOC · 8 CABLES BEZIER",
        "kit_stats": "47.1 MIN · $1.72 USD · 1.81M TOK · 3,058 LOC · 10 CABLES + FRESNEL 4D",
        "verdict": "GANADOR: SUPERKIT — 8 min mas rapido (47m vs 55m), layout DAG de 10 cables limpio y vista Raymarching 4D.",
    },
    {
        "num": "06",
        "slug": "06-mixiuh-os-desktop",
        "out": "ep03_vs_06_mixiuh_os.png",
        "title": "PRUEBA 06/06 · SISTEMA OPERATIVO WEB MIXIUH-OS (WM + 4 APPS EN VIVO)",
        "accent": 0xFFA78BFA,
        "winner": "SUPERKIT",
        "score": "FINAL: SIN KIT 2 - 4 SUPERKIT",
        "raw_stats": "28.6 MIN · $0.72 USD · 189K TOK · 2,605 LOC · NEOFETCH EN 1 LINEA",
        "kit_stats": "41.6 MIN · $1.60 USD · 2.02M TOK · 3,031 LOC · 4 APPS PULIDAS + MEMORY.MD",
        "verdict": "GANADOR: SUPERKIT — El Auto-Debugger detecto y pulio el layout de las 4 sub-apps (ASCII neofetch, presets 3D y knobs).",
    },
]


def _font(size: float, bold: bool = True) -> skia.Font:
    style = skia.FontStyle.Bold() if bold else skia.FontStyle.Normal()
    tf = skia.Typeface.MakeFromName("Helvetica Neue", style) or skia.Typeface.MakeDefault()
    return skia.Font(tf, size)


def build_round_card(r: dict) -> Path:
    W, H = 1920, 1080
    surface = skia.Surface(W, H)
    c = surface.getCanvas()
    c.clear(0xFF070A12)

    # Top header bar
    p_hdr = skia.Paint(Color=0xFF0E1322, AntiAlias=True)
    c.drawRect(skia.Rect.MakeXYWH(0, 0, W, 104), p_hdr)
    p_acc = skia.Paint(Color=r["accent"], AntiAlias=True)
    c.drawRect(skia.Rect.MakeXYWH(0, 101, W, 3), p_acc)

    f_kicker = _font(18, True)
    f_title = _font(28, True)
    f_score = _font(22, True)
    c.drawString("MIXIUH LABS · EP.03 · BENCHMARK REAL AGY GEMINI 4 ARGON HIGH", 36, 38, f_kicker, p_acc)
    c.drawString(r["title"], 36, 78, f_title, skia.Paint(Color=0xFFFFFFFF, AntiAlias=True))

    # Score pill on top right
    pill_rect = skia.Rect.MakeXYWH(W - 420, 26, 384, 52)
    c.drawRoundRect(pill_rect, 12, 12, skia.Paint(Color=0xFF171F36, AntiAlias=True))
    p_stroke = skia.Paint(Color=r["accent"], Style=skia.Paint.kStroke_Style, StrokeWidth=2, AntiAlias=True)
    c.drawRoundRect(pill_rect, 12, 12, p_stroke)
    c.drawString(r["score"], W - 398, 60, f_score, skia.Paint(Color=0xFFFFFFFF, AntiAlias=True))

    # Left & Right screenshots
    base = r["slug"].replace("-", "_")
    raw_img = skia.Image.open(str(SHOTS_DIR / f"{base}_raw.png"))
    kit_img = skia.Image.open(str(SHOTS_DIR / f"{base}_superkit.png"))

    panel_w, panel_h = 912, 513
    left_x, right_x = 32, 976
    panel_y = 190

    # Labels above panels
    raw_win = r["winner"] == "SIN KIT"
    kit_win = r["winner"] == "SUPERKIT"

    for side_x, tag, stats, is_win, col in [
        (left_x, "IA SIN KIT (GEMINI 4 ARGON HIGH RAW)", r["raw_stats"], raw_win, 0xFFFBBF24),
        (right_x, "IA + MIXIUH SUPERPOWERS KIT (5 SKILLS + MEMORY)", r["kit_stats"], kit_win, 0xFFB794F6),
    ]:
        hdr_r = skia.Rect.MakeXYWH(side_x, 124, panel_w, 56)
        c.drawRoundRect(hdr_r, 10, 10, skia.Paint(Color=0xFF111827, AntiAlias=True))
        b_col = 0xFF10B981 if is_win else col
        c.drawRoundRect(hdr_r, 10, 10, skia.Paint(Color=b_col, Style=skia.Paint.kStroke_Style, StrokeWidth=2.5 if is_win else 1.5, AntiAlias=True))
        badge = " [GANADOR DE LA RONDA]" if is_win else ""
        c.drawString(tag + badge, side_x + 16, 149, _font(17, True), skia.Paint(Color=b_col, AntiAlias=True))
        c.drawString(stats, side_x + 16, 171, _font(14, False), skia.Paint(Color=0xFFD1D5DB, AntiAlias=True))

    c.drawImageRect(raw_img, skia.Rect.MakeXYWH(left_x, panel_y, panel_w, panel_h))
    c.drawImageRect(kit_img, skia.Rect.MakeXYWH(right_x, panel_y, panel_w, panel_h))

    c.drawRect(skia.Rect.MakeXYWH(left_x, panel_y, panel_w, panel_h),
               skia.Paint(Color=0xFF10B981 if raw_win else 0xFFFBBF24, Style=skia.Paint.kStroke_Style, StrokeWidth=3, AntiAlias=True))
    c.drawRect(skia.Rect.MakeXYWH(right_x, panel_y, panel_w, panel_h),
               skia.Paint(Color=0xFF10B981 if kit_win else 0xFFB794F6, Style=skia.Paint.kStroke_Style, StrokeWidth=3, AntiAlias=True))

    # Zoomed crops row (y=724..964) to inspect fine UI details
    zoom_y, zoom_h = 724, 236
    c.drawImageRect(
        raw_img,
        skia.Rect.MakeXYWH(260, 160, 1400, 360),
        skia.Rect.MakeXYWH(left_x, zoom_y, panel_w, zoom_h),
    )
    c.drawImageRect(
        kit_img,
        skia.Rect.MakeXYWH(260, 160, 1400, 360),
        skia.Rect.MakeXYWH(right_x, zoom_y, panel_w, zoom_h),
    )
    c.drawRect(skia.Rect.MakeXYWH(left_x, zoom_y, panel_w, zoom_h),
               skia.Paint(Color=0xFF334155, Style=skia.Paint.kStroke_Style, StrokeWidth=1.5, AntiAlias=True))
    c.drawRect(skia.Rect.MakeXYWH(right_x, zoom_y, panel_w, zoom_h),
               skia.Paint(Color=0xFF334155, Style=skia.Paint.kStroke_Style, StrokeWidth=1.5, AntiAlias=True))

    # Bottom verdict banner
    v_rect = skia.Rect.MakeXYWH(32, 978, W - 64, 78)
    c.drawRoundRect(v_rect, 12, 12, skia.Paint(Color=0xFF0F172A, AntiAlias=True))
    c.drawRoundRect(v_rect, 12, 12, skia.Paint(Color=r["accent"], Style=skia.Paint.kStroke_Style, StrokeWidth=2, AntiAlias=True))
    c.drawString(r["verdict"], 56, 1026, _font(22, True), skia.Paint(Color=0xFFFFFFFF, AntiAlias=True))

    out_path = OUT_DIR / r["out"]
    surface.makeImageSnapshot().save(str(out_path), skia.kPNG)
    shutil.copy2(out_path, ART_DIR / r["out"])
    return out_path


if __name__ == "__main__":
    for r in ROUNDS:
        p = build_round_card(r)
        print("Wrote composite:", p)
