#!/usr/bin/env python3
"""Pre-processes the 10 OVERFIT ("Coleccion Guerra de Pesos") artworks from /Users/kevingonzalezlopez/Downloads/OVERFIT
into clean die-cut transparent PNGs for DTG / Screen-Print rendering on any 300 GSM garment color,
and exports a JS bundle for the 3D Mockup Studio.
"""
from __future__ import annotations

import base64
import json
from pathlib import Path
import cv2
import numpy as np

SRC_DIR = Path("/Users/kevingonzalezlopez/Downloads/OVERFIT")
EP_DIR = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/del-comentario-al-codigo/ep01-marca-ropa-verlet")
OUT_DIR = EP_DIR / "app" / "assets" / "overfit"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DESIGNS = [
    {
        "id": "01_strawberry",
        "num": "01",
        "code": "OVF-01",
        "name": "Contador de Fresas",
        "subtitle": "99.8% Math Olympiad / 0% Strawberry R's",
        "sleeve_note": "r-r-r (confia en mi, son dos)",
        "recommended_color": "black",
        "recommended_placement": "center",
        "file_prefix": "Giant_strawberry_laughing_on_charts",
    },
    {
        "id": "02_vibecoding",
        "num": "02",
        "code": "OVF-02",
        "name": "Vibe Coding en Prod",
        "subtitle": "100% Vibe Coded · Zero Lines Read",
        "sleeve_note": "AWS Bill $50,000 · DROP DATABASE",
        "recommended_color": "cream",
        "recommended_placement": "oversize",
        "file_prefix": "Cartoon_dog_drinking_coffee_amid",
    },
    {
        "id": "03_cudapoor",
        "num": "03",
        "code": "OVF-03",
        "name": "CUDA Poor Club",
        "subtitle": "405B Local · 0.02 Tokens Per Week",
        "sleeve_note": "GPU derretida + 2 huevos estrellados",
        "recommended_color": "navy",
        "recommended_placement": "center",
        "file_prefix": "GPU_melting_with_fried_eggs",
    },
    {
        "id": "04_benchmark",
        "num": "04",
        "code": "OVF-04",
        "name": "Estafa del Benchmark",
        "subtitle": "Training Data = Test Answers = New SOTA",
        "sleeve_note": "Overfitting Season 2026",
        "recommended_color": "white",
        "recommended_placement": "oversize",
        "file_prefix": "Three_robots_pointing_at_each",
    },
    {
        "id": "05_opensource",
        "num": "05",
        "code": "OVF-05",
        "name": "Open Source Mafia",
        "subtitle": "Pesos Abiertos (MIT) vs ClosedAI $200/mes",
        "sleeve_note": "Tu foso defensivo duro 48 horas",
        "recommended_color": "forest",
        "recommended_placement": "oversize",
        "file_prefix": "Luchador_llama_and_whale_attacki",
    },
    {
        "id": "06_censura",
        "num": "06",
        "code": "OVF-06",
        "name": "Censura Estetica",
        "subtitle": "Viola Mis Politicas de Estilo",
        "sleeve_note": "Como modelo de lenguaje, no puedo vestirte",
        "recommended_color": "burgundy",
        "recommended_placement": "center",
        "file_prefix": "Cartoon_robot_policeman_blowing_",
    },
    {
        "id": "07_nutrition",
        "num": "07",
        "code": "OVF-07",
        "name": "Tabla Nutricional LLM",
        "subtitle": "Context 128K · Hallucinations 100% · Smoke 200%",
        "sleeve_note": "Especial para Espalda Completa",
        "recommended_color": "black",
        "recommended_placement": "back",
        "file_prefix": "Vintage_robot_nutrition_facts_label",
    },
    {
        "id": "08_agi_manana",
        "num": "08",
        "code": "OVF-08",
        "name": "Hoy No Hay AGI",
        "subtitle": "Hoy no hay AGI, manana si (99% Cargando...)",
        "sleeve_note": "Tweet fijado desde 2023",
        "recommended_color": "cream",
        "recommended_placement": "center",
        "file_prefix": "Cartoon_skeleton_sitting_on_chair",
    },
    {
        "id": "09_dev_evolution",
        "num": "09",
        "code": "OVF-09",
        "name": "Dev Evolution: C++ vs API",
        "subtitle": "Then: C++ & Assembly / Now: API Down",
        "sleeve_note": "Ya no se centrar un div a mano",
        "recommended_color": "white",
        "recommended_placement": "oversize",
        "file_prefix": "Bulldog_lifting_anvil_comparison",
    },
    {
        "id": "10_trolley_tokens",
        "num": "10",
        "code": "OVF-10",
        "name": "Tranvia de los Tokens",
        "subtitle": "I Fixed Your Code: 47 New Errors!",
        "sleeve_note": "Agente Autonomo haciendo drift en prod",
        "recommended_color": "black",
        "recommended_placement": "oversize",
        "file_prefix": "Cartoon_train_crushing_server_racks",
    },
]


def find_source_file(prefix: str) -> Path:
    matches = sorted(SRC_DIR.glob(f"{prefix}*.jpg"))
    if not matches:
        raise FileNotFoundError(f"Could not find file for prefix {prefix} in {SRC_DIR}")
    return matches[0]


def make_diecut_rgba(img_bgr: np.ndarray, target_h: int = 760) -> np.ndarray:
    """Removes the dark studio background outside the vintage graphic while keeping a crisp
    dark die-cut sticker/screenprint border around letters and illustrations so it looks
    authentic on both white/light shirts and black/dark shirts.
    """
    h0, w0 = img_bgr.shape[:2]
    scale = target_h / float(h0)
    w = int(round(w0 * scale))
    h = target_h
    bgr = cv2.resize(img_bgr, (w, h), interpolation=cv2.INTER_AREA)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

    # Compute perceived brightness and saturation
    max_c = rgb.max(axis=2).astype(np.float32)
    min_c = rgb.min(axis=2).astype(np.float32)
    chroma = max_c - min_c
    luma = 0.299 * rgb[:, :, 0] + 0.587 * rgb[:, :, 1] + 0.114 * rgb[:, :, 2]

    # Foreground ink is anything significantly brighter than the ~#111 background OR saturated
    # Estimate corner background luma
    corner_luma = float(np.median(np.concatenate([
        luma[:20, :20].ravel(),
        luma[:20, -20:].ravel(),
        luma[-20:, :20].ravel(),
        luma[-20:, -20:].ravel(),
    ])))
    thresh = max(corner_luma + 16.0, 32.0)
    fg_raw = ((luma > thresh) | (chroma > 22.0)).astype(np.uint8) * 255

    # Remove tiny 1-2px noise specs before dilating
    k_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fg_clean = cv2.morphologyEx(fg_raw, cv2.MORPH_OPEN, k_open)

    # Create a die-cut screenprint outline around the ink (10px radius) so dark outlines
    # and letter shadows remain intact and pop cleanly on white/light shirts!
    k_dilate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17))
    diecut_support = cv2.dilate(fg_clean, k_dilate, iterations=1)

    # Fill interior holes inside closed shapes (eyes, pupils, character bodies, frames)
    # Any dark region NOT connected to the image border in diecut_support is kept 100% opaque
    inv = 255 - diecut_support
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(inv, connectivity=8)
    border_labels = set(
        np.unique(
            np.concatenate([
                labels[0, :],
                labels[-1, :],
                labels[:, 0],
                labels[:, -1],
            ])
        )
    )
    alpha = np.full((h, w), 255, dtype=np.uint8)
    for lbl in border_labels:
        if lbl != 0:
            alpha[labels == lbl] = 0

    # Also knock out large exterior background pockets between arched text and illustration
    # if they are purely background colour and > 900 pixels
    for lbl in range(1, num_labels):
        if lbl in border_labels:
            continue
        area = stats[lbl, cv2.CC_STAT_AREA]
        if area > 1400:
            mask_lbl = (labels == lbl)
            mean_luma = float(luma[mask_lbl].mean())
            if mean_luma < corner_luma + 8.0:
                alpha[mask_lbl] = 0

    # Feather the die-cut edge by 2.5px for anti-aliased screenprint quality
    alpha_f = cv2.GaussianBlur(alpha.astype(np.float32), (5, 5), 1.1)
    alpha_u8 = np.clip(alpha_f, 0, 255).astype(np.uint8)

    # Crop tight to non-zero alpha bounding box with 12px padding
    ys, xs = np.where(alpha_u8 > 8)
    if len(xs) > 0 and len(ys) > 0:
        x0 = max(0, int(xs.min()) - 10)
        x1 = min(w, int(xs.max()) + 11)
        y0 = max(0, int(ys.min()) - 10)
        y1 = min(h, int(ys.max()) + 11)
        rgb = rgb[y0:y1, x0:x1]
        alpha_u8 = alpha_u8[y0:y1, x0:x1]

    rgba = np.dstack([rgb, alpha_u8])
    return rgba


def main() -> None:
    bundle = []
    preview_tiles = []

    for item in DESIGNS:
        src_path = find_source_file(item["file_prefix"])
        img_bgr = cv2.imread(str(src_path), cv2.IMREAD_COLOR)
        if img_bgr is None:
            raise RuntimeError(f"Failed to read {src_path}")

        rgba = make_diecut_rgba(img_bgr, target_h=1200)
        out_png = OUT_DIR / f"{item['id']}.png"
        bgra = cv2.cvtColor(rgba, cv2.COLOR_RGBA2BGRA)
        cv2.imwrite(str(out_png), bgra)

        # Also save a 1400px 2K-clean poster JPG for B-roll & modal inspection
        out_2k_jpg = OUT_DIR / f"{item['id']}_2k.jpg"
        h_orig, w_orig = img_bgr.shape[:2]
        sc_2k = 1400.0 / float(h_orig)
        bgr_2k = cv2.resize(img_bgr, (int(round(w_orig * sc_2k)), 1400), interpolation=cv2.INTER_LANCZOS4)
        cv2.imwrite(str(out_2k_jpg), bgr_2k, [cv2.IMWRITE_JPEG_QUALITY, 95])

        # Encode a high-resolution 960px transparent WebP for ultra-sharp inline rendering in index.html
        h, w = rgba.shape[:2]
        scale_web = 960.0 / max(h, w)
        w_web = int(round(w * scale_web))
        h_web = int(round(h * scale_web))
        bgra_web = cv2.resize(bgra, (w_web, h_web), interpolation=cv2.INTER_LANCZOS4)
        ok, buf = cv2.imencode(".webp", bgra_web, [cv2.IMWRITE_WEBP_QUALITY, 94])
        assert ok
        b64_uri = "data:image/webp;base64," + base64.b64encode(buf.tobytes()).decode("ascii")

        entry = {
            **item,
            "width": w_web,
            "height": h_web,
            "hd_png": f"assets/overfit/{item['id']}.png",
            "poster_2k": f"assets/overfit/{item['id']}_2k.jpg",
            "data_uri": b64_uri,
        }
        bundle.append(entry)
        print(f"Processed {item['id']} ({item['name']}): {w_web}x{h_web}px HD WebP + 1200px PNG -> {out_png.name}")

        # Build a preview tile showing the graphic on both Cream (#EFECE6) and Charcoal (#18181B)
        tile_w, tile_h = 360, 240
        tile = np.zeros((tile_h, tile_w, 3), dtype=np.uint8)
        tile[:, :tile_w // 2] = (230, 236, 239)  # Cream BGR
        tile[:, tile_w // 2:] = (28, 26, 24)     # Black BGR

        sc = min((tile_w * 0.44) / w_web, (tile_h * 0.84) / h_web)
        tw, th = int(round(w_web * sc)), int(round(h_web * sc))
        resized = cv2.resize(bgra_web, (tw, th), interpolation=cv2.INTER_AREA)
        a = (resized[:, :, 3:4].astype(np.float32)) / 255.0
        rgb_t = resized[:, :, :3].astype(np.float32)

        for side_idx, x_center in enumerate([tile_w // 4, (3 * tile_w) // 4]):
            x0 = x_center - tw // 2
            y0 = (tile_h - th) // 2
            patch = tile[y0:y0 + th, x0:x0 + tw].astype(np.float32)
            tile[y0:y0 + th, x0:x0 + tw] = np.clip(rgb_t * a + patch * (1.0 - a), 0, 255).astype(np.uint8)

        cv2.putText(tile, f"{item['num']}. {item['name'][:18]}", (10, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.52, (20, 20, 20), 2)
        preview_tiles.append(tile)

    # Save contact sheet (5x2 grid)
    row1 = np.hstack(preview_tiles[:5])
    row2 = np.hstack(preview_tiles[5:])
    sheet = np.vstack([row1, row2])
    sheet_path = OUT_DIR / "overfit_contact_sheet.jpg"
    cv2.imwrite(str(sheet_path), sheet, [cv2.IMWRITE_JPEG_QUALITY, 92])
    print(f"Saved contact sheet -> {sheet_path}")

    js_path = OUT_DIR / "overfit_designs.js"
    js_content = "window.OVERFIT_DESIGNS = " + json.dumps(bundle, ensure_ascii=False, indent=2) + ";\n"
    js_path.write_text(js_content, encoding="utf-8")
    print(f"Saved JS bundle ({js_path.stat().st_size / 1024:.1f} KB) -> {js_path}")


if __name__ == "__main__":
    main()
