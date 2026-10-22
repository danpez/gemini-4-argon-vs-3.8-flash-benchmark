#!/usr/bin/env python3
"""
Generates side-by-side visual comparison cards (1920x1080) for each completed
challenge in Episode 02: Gemini 4 Argon (High) vs Claude Opus 5.5 (High),
and copies them both to ep02-argon-vs-opus/screenshots/ and the artifacts dir.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep02-argon-vs-opus")
SCREENSHOTS = BASE / "screenshots"
ARTIFACTS = Path("/Users/kevingonzalezlopez/.gemini/antigravity/brain/f7f21679-195b-4060-b55b-03feb3817e4f")


def load_font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Menlo.ttc",
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for c in candidates:
        if Path(c).exists():
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()


META = [
    {
        "num": "01",
        "slug": "01_tela_verlet",
        "title": "RETO 01: TELA FISICA VERLET + DESGARRO EN TIEMPO REAL",
        "argon_stats": "6.68 min (400.7s)  |  2,766 lineas (88.0 KB)  |  120 FPS (2,856 nodos)",
        "opus_stats": "30.87 min (1852.1s)  |  1,352 lineas (65.9 KB)  |  28 FPS (3,168 nodos)",
        "badge": "ARGON 4.62x MAS RAPIDO + 120 FPS vs 28 FPS",
    },
    {
        "num": "02",
        "slug": "02_fluidos_navier_stokes",
        "title": "RETO 02: FLUIDOS EULERIANOS NAVIER-STOKES GPU (WEBGL2 FBOs)",
        "argon_stats": "10.00 min (600.0s)  |  2,506 lineas (83.6 KB)  |  120 FPS (16 FBOs)",
        "opus_stats": "18.47 min (1108.0s)  |  1,444 lineas (62.7 KB)  |  120 FPS (20 FBOs)",
        "badge": "ARGON 1.85x MAS RAPIDO · AMBOS 120 FPS EN GPU",
    },
    {
        "num": "03",
        "slug": "03_cuerpo_blando_sdf",
        "title": "RETO 03: FISICA DE CUERPOS BLANDOS 3D (SOFT-BODY JELLY & SDF)",
        "argon_stats": "34.74 min (2084.6s)  |  2,543 lineas (93.7 KB)  |  120 FPS (Esqueleto + Piel)",
        "opus_stats": "30.87 min (1852.3s)  |  1,701 lineas (101.7 KB)  |  82 FPS (6 Morfologias + Reflejos)",
        "badge": "OPUS 1.13x MAS RAPIDO (6 FORMAS) · ARGON 120 FPS",
    },
    {
        "num": "04",
        "slug": "04_voxel_minecraft",
        "title": "RETO 04: MOTOR VOXEL 3D PROCEDURAL MULTI-BIOMA (THREE.JS)",
        "argon_stats": "6.99 min (419.3s)  |  2,569 lineas (89.7 KB)  |  120 FPS (66.6k voxels)",
        "opus_stats": "23.65 min (1419.3s)  |  1,665 lineas (91.6 KB)  |  120 FPS (2.58M voxels + AO)",
        "badge": "ARGON 3.38x MAS RAPIDO · OPUS ESCALA A 2.58M VOXELS CON AO",
    },
    {
        "num": "05",
        "slug": "05_sintetizador_fm",
        "title": "RETO 05: SINTETIZADOR POLIFONICO FM + SECUENCIADOR Y FFT (WEBAUDIO)",
        "argon_stats": "24.07 min (1444.2s)  |  2,586 lineas (81.0 KB)  |  12 Voces + 6 Pistas + Osciloscopio",
        "opus_stats": "30.23 min (1813.6s)  |  1,933 lineas (106.3 KB)  |  16 Voces + 8 Pistas + 4 Modos FFT/XY",
        "badge": "ARGON 1.26x MAS RAPIDO · OPUS INCLUYE GONIOMETRO Y ESPECTROGRAMA",
    },
    {
        "num": "06",
        "slug": "06_pinball_ccd",
        "title": "RETO 06: MESA DE PINBALL CYBERPUNK CON COLISION CONTINUA (CCD)",
        "argon_stats": "7.65 min (459.0s)  |  2,749 lineas (95.0 KB)  |  20 Sub-pasos CCD + Boton Multiball 3x",
        "opus_stats": "24.57 min (1474.1s)  |  1,508 lineas (79.4 KB)  |  16 Sub-pasos CCD + 120 FPS (DMD LED)",
        "badge": "ARGON 3.21x MAS RAPIDO + MULTIBALL DIRECTO · OPUS 120 FPS",
    },
]


def make_card(item: dict):
    slug = item["slug"]
    p_argon = SCREENSHOTS / f"{slug}_argon.png"
    p_opus = SCREENSHOTS / f"{slug}_opus.png"
    if not p_argon.exists() or not p_opus.exists():
        return None

    W, H = 1920, 1080
    canvas = Image.new("RGB", (W, H), (8, 13, 23))
    draw = ImageDraw.Draw(canvas)

    f_title = load_font(26, bold=True)
    f_model = load_font(22, bold=True)
    f_stats = load_font(16)
    f_badge = load_font(18, bold=True)

    # Top Header Bar
    draw.rectangle([0, 0, W, 86], fill=(13, 23, 38))
    draw.line([(0, 86), (W, 86)], fill=(34, 162, 221), width=2)
    draw.text((28, 18), f"MIXIUH LABS // EPISODIO 02 — {item['title']}", fill=(255, 255, 255), font=f_title)
    draw.text((28, 52), f"VEREDICTO DE RONDA: {item['badge']}", fill=(94, 234, 212), font=f_badge)

    # Left Panel: Gemini 4 Argon (High)
    img_a = Image.open(p_argon).convert("RGB").resize((924, 520), Image.Resampling.LANCZOS)
    canvas.paste(img_a, (24, 175))
    draw.rectangle([24, 110, 948, 170], fill=(14, 38, 60), outline=(34, 162, 221), width=2)
    draw.text((38, 116), "GEMINI 4 ARGON (HIGH) — agy CLI", fill=(94, 234, 212), font=f_model)
    draw.text((38, 144), item["argon_stats"], fill=(220, 232, 245), font=f_stats)
    draw.rectangle([24, 175, 948, 695], outline=(34, 162, 221), width=2)

    # Right Panel: Claude Opus 5.5 (High)
    img_o = Image.open(p_opus).convert("RGB").resize((924, 520), Image.Resampling.LANCZOS)
    canvas.paste(img_o, (972, 175))
    draw.rectangle([972, 110, 1896, 170], fill=(42, 24, 56), outline=(245, 158, 11), width=2)
    draw.text((986, 116), "CLAUDE OPUS 5.5 (HIGH) — claude CLI", fill=(251, 191, 36), font=f_model)
    draw.text((986, 144), item["opus_stats"], fill=(245, 232, 220), font=f_stats)
    draw.rectangle([972, 175, 1896, 695], outline=(245, 158, 11), width=2)

    # Bottom 1.8x Zoom Crop Strip for micro-detail comparison
    raw_a = Image.open(p_argon).convert("RGB")
    raw_o = Image.open(p_opus).convert("RGB")
    cw, ch = raw_a.size
    crop_a = raw_a.crop((int(cw * 0.20), int(ch * 0.22), int(cw * 0.80), int(ch * 0.78))).resize((924, 330), Image.Resampling.LANCZOS)
    crop_o = raw_o.crop((int(cw * 0.20), int(ch * 0.22), int(cw * 0.80), int(ch * 0.78))).resize((924, 330), Image.Resampling.LANCZOS)
    canvas.paste(crop_a, (24, 725))
    canvas.paste(crop_o, (972, 725))
    draw.rectangle([24, 725, 948, 1055], outline=(34, 162, 221), width=1)
    draw.rectangle([972, 725, 1896, 1055], outline=(245, 158, 11), width=1)
    draw.rectangle([28, 729, 320, 758], fill=(8, 13, 23))
    draw.text((34, 734), "ZOOM CENTRAL 1.8x — ARGON", fill=(94, 234, 212), font=f_stats)
    draw.rectangle([976, 729, 1268, 758], fill=(8, 13, 23))
    draw.text((982, 734), "ZOOM CENTRAL 1.8x — OPUS 5.5", fill=(251, 191, 36), font=f_stats)

    out_local = SCREENSHOTS / f"vs_{slug}.png"
    out_art = ARTIFACTS / f"ep02_vs_{slug}.png"
    canvas.save(out_local, "PNG")
    canvas.save(out_art, "PNG")
    print(f"Generated {out_local.name}")
    return out_art


def make_scoreboard():
    W, H = 1920, 1080
    canvas = Image.new("RGB", (W, H), (8, 13, 23))
    draw = ImageDraw.Draw(canvas)

    f_h1 = load_font(32, bold=True)
    f_h2 = load_font(22, bold=True)
    f_row = load_font(18, bold=True)
    f_sub = load_font(15)

    draw.rectangle([0, 0, W, 110], fill=(13, 23, 38))
    draw.line([(0, 110), (W, 110)], fill=(94, 234, 212), width=3)
    draw.text((36, 22), "MIXIUH LABS // EPISODIO 02 — TABLA OFICIAL DE RESULTADOS ZERO-SHOT", fill=(255, 255, 255), font=f_h1)
    draw.text((36, 66), "GEMINI 4 ARGON (HIGH) [agy CLI]  vs.  CLAUDE OPUS 5.5 (HIGH) [claude CLI]  ·  6 RETOS EXTREMOS EN 1 ARCHIVO HTML", fill=(94, 234, 212), font=f_h2)

    # Summary KPI Boxes
    draw.rectangle([36, 135, 936, 275], fill=(14, 38, 60), outline=(34, 162, 221), width=2)
    draw.text((60, 150), "GEMINI 4 ARGON (HIGH) — 90.13 MIN  |  COSTE API: $6.26 USD", fill=(94, 234, 212), font=f_h2)
    draw.text((60, 188), "Tokens Exactos: 1.06M In + 2.26M Cache + 306.9K Out (45 pasos)  |  15,719 lineas (531 KB)", fill=(225, 238, 250), font=f_sub)
    draw.text((60, 216), "Eficiencia: 1.76x mas rapido (-68.5 min) y ~2.60x mas economico que Opus 5.5", fill=(52, 211, 153), font=f_row)
    draw.text((60, 244), "One-Shot limpio en R01, R04 y R06: resueltos en solo 2-3 pasos ($0.65 a $0.70 USD c/u)", fill=(225, 238, 250), font=f_sub)

    draw.rectangle([984, 135, 1884, 275], fill=(42, 24, 56), outline=(245, 158, 11), width=2)
    draw.text((1008, 150), "CLAUDE OPUS 5.5 (HIGH) — 158.66 MIN  |  COSTE EST.: ~$16.26 USD", fill=(251, 191, 36), font=f_h2)
    draw.text((1008, 188), "Tokens Est. (Playwright QA): ~755K In/Write + ~12.25M Cache + ~501K Out  |  9,603 lineas", fill=(245, 232, 220), font=f_sub)
    draw.text((1008, 216), "Por que tardo y gasto mas: ejecuto pruebas Playwright headless + commits en los 6 retos", fill=(251, 191, 36), font=f_row)
    draw.text((1008, 244), "Tarifa oficial CLI (tier_4_20): $4/1M In, $5-$8/1M Cache Write, $0.20/1M Read, $20/1M Out", fill=(244, 63, 94), font=f_sub)

    rows = [
        ("01. Tela Fisica Verlet", "6.68 min", "93K In / 38.5K Out", "$0.65", "30.87 min", "~2.5M In+Cache / 92K Out", "~$3.05", "ARGON (4.6x mas rapido y 4.7x mas barato)"),
        ("02. Fluidos Navier-Stokes", "10.00 min", "901K In+C / 58.4K Out", "$1.40", "18.47 min", "~1.5M In+Cache / 64K Out", "~$2.05", "ARGON (1.85x mas rapido + GPU Bloom)"),
        ("03. Cuerpo Blando 3D SDF", "34.74 min", "1.6M In+C / 88.1K Out", "$1.98", "30.87 min", "~2.4M In+Cache / 96K Out", "~$3.08", "OPUS en Tiempo (6 formas) / ARGON en Coste"),
        ("04. Motor Voxel 3D", "6.99 min", "95K In / 40.4K Out", "$0.67", "23.65 min", "~2.0M In+Cache / 78K Out", "~$2.51", "EMPATE (Argon $0.67 vs Escala 2.58M Voxels)"),
        ("05. Sintetizador FM + FFT", "24.07 min", "471K In+C / 40.3K Out", "$0.85", "30.23 min", "~2.5M In+Cache / 95K Out", "~$3.08", "OPUS en Estudio / ARGON 3.6x mas barato"),
        ("06. Pinball CCD Arcade", "7.65 min", "162K In+C / 41.2K Out", "$0.70", "24.57 min", "~2.0M In+Cache / 76K Out", "~$2.49", "ARGON (3.2x mas rapido y 3.5x mas barato)"),
    ]

    y = 310
    draw.rectangle([36, y, 1884, y + 48], fill=(20, 34, 54))
    headers = [
        (48, "RETO ZERO-SHOT"),
        (355, "ARGON TIEMPO"),
        (505, "ARGON TOKENS"),
        (735, "ARGON USD"),
        (855, "OPUS TIEMPO"),
        (1005, "OPUS TOKENS (EST.)"),
        (1265, "OPUS USD"),
        (1385, "VEREDICTO DE ARBITRAJE"),
    ]
    for x, text in headers:
        draw.text((x, y + 14), text, fill=(94, 234, 212), font=f_sub)

    y += 56
    for idx, r in enumerate(rows):
        bg = (12, 20, 34) if idx % 2 == 0 else (16, 28, 46)
        draw.rectangle([36, y, 1884, y + 96], fill=bg, outline=(35, 55, 82), width=1)
        draw.text((48, y + 34), r[0], fill=(255, 255, 255), font=f_row)
        draw.text((355, y + 34), r[1], fill=(94, 234, 212), font=f_row)
        draw.text((505, y + 36), r[2], fill=(200, 220, 240), font=f_sub)
        draw.text((735, y + 34), r[3], fill=(52, 211, 153), font=f_row)
        draw.text((855, y + 34), r[4], fill=(251, 191, 36), font=f_row)
        draw.text((1005, y + 36), r[5], fill=(240, 225, 205), font=f_sub)
        draw.text((1265, y + 34), r[6], fill=(251, 146, 60), font=f_row)
        v_col = (94, 234, 212) if r[7].startswith("ARGON") else ((251, 191, 36) if r[7].startswith("OPUS") else (192, 132, 252))
        draw.text((1385, y + 36), r[7], fill=v_col, font=f_sub)
        y += 104

    out_local = SCREENSHOTS / "ep02_scoreboard_overview.png"
    out_art = ARTIFACTS / "ep02_scoreboard_overview.png"
    canvas.save(out_local, "PNG")
    canvas.save(out_art, "PNG")
    print(f"Generated {out_local.name}")


def main():
    for item in META:
        make_card(item)
    make_scoreboard()


if __name__ == "__main__":
    main()

