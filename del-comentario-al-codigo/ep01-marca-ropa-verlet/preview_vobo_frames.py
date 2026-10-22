#!/usr/bin/env python3
"""Generates high-resolution preview frames (9:16 Vertical and 16:9 Horizontal)
using the authentic Mixiuh Labs pixel-art engine (mlabs.package.shorts_gfx, mlabs.gfx.cards,
mlabs.sprites with the new 'comment' and 'tshirt' sprites) so Kevin can inspect and give
his VoBo BEFORE rendering the full videos.
"""
from __future__ import annotations

import sys
from pathlib import Path

import cv2
import numpy as np
import skia

MLABS_ROOT = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs")
sys.path.insert(0, str(MLABS_ROOT))

from mlabs import brand, sprites as SP
from mlabs.gfx.base import Frame, draw_text, fill_rrect, new_frame, paint, rrect, set_design, stroke_rrect
from mlabs.gfx.background import draw_lab_bg
from mlabs.gfx.cards import brackets, pblock, ptitle
from mlabs.gfx.overlays import hud, model_label, vs_badge
from mlabs.package import shorts_gfx as SG
from mlabs.pixelfont import draw_pixel_text, measure_pixel_text

EP_DIR = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/del-comentario-al-codigo/ep01-marca-ropa-verlet")
GRAB_DIR = EP_DIR / "grabaciones"
COMMENT_IMG_PATH = EP_DIR / "comentario-original" / "comentario_tenito03_ig.jpg"
VOBO_DIR = EP_DIR / "vobo_previews"


def configure_cc01_models() -> None:
    """Sets the left side to @TENITO03 ('comment' sprite) and right side to MOCKUP STUDIO ('tshirt' sprite).
    Never reuses the Gemini Flash lightning bolt.
    """
    brand.set_models({
        "flash": {
            "name": "Reto @tenito03",
            "tag": "TENITO03",
            "color": "#22D3EE",
            "side": "left",
            "sprite": "comment",
        },
        "argon": {
            "name": "Mixiuh Mockup Studio",
            "tag": "STUDIO 3D",
            "color": "#B794F6",
            "side": "right",
            "sprite": "tshirt",
        },
    })
    SG.EP02_CHALLENGES[1] = {
        "accent": "#22D3EE",
        "title_es": "CREA TU MARCA Y MOCKUPS",
        "title_en": "BUILD YOUR BRAND & MOCKUPS",
        "sub_es": "SUBE TU LOGO · EXPORTA A REDES · 100% CODIGO",
        "sub_en": "UPLOAD LOGO · SOCIAL EXPORT · 100% CODE",
        "times": {"flash": 45, "argon": 1},
        "costs": {"flash": 29.00, "argon": 0.00},
        "tokens": {"flash": "SUSCRIPCION", "argon": "1 ARCHIVO HTML"},
        "stats_es": {"flash": "PLANTILLAS FIJAS", "argon": "FISICA 3D + REDES"},
        "stats_en": {"flash": "STATIC TEMPLATES", "argon": "3D PHYSICS + SOCIAL"},
        "headline_es": "DE COMENTARIO A ESTUDIO REAL",
        "headline_en": "FROM COMMENT TO REAL STUDIO",
        "reason_es": "Sube tu PNG · Doblado fisico Verlet · Exporta a Instagram y Tienda",
        "reason_en": "Upload PNG · Verlet cloth drape · Export to Instagram & Store",
        "score_before": {"flash": 0, "argon": 0},
        "score_after": {"flash": 0, "argon": 1},
    }


def draw_cropped_image_in_panel(
    f: Frame,
    img_path: Path,
    crop_box: tuple[int, int, int, int],
    panel_rect: list[float],
    radius: float = 18.0,
    inset_top: float = 0.0,
    inset_bottom: float = 0.0,
) -> None:
    bgr = cv2.imread(str(img_path))
    if bgr is None:
        return
    cx, cy, cw, ch = crop_box
    crop = bgr[cy : cy + ch, cx : cx + cw]
    px, py, pw, ph = panel_rect
    c = f.canvas
    c.save()
    c.clipRRect(rrect(f, px, py, pw, ph, radius), skia.ClipOp.kIntersect, True)
    fill_rrect(f, px, py, pw, ph, radius, "#060E1B", 1.0)

    dy = py + inset_top
    dh = max(10.0, ph - inset_top - inset_bottom)
    src_aspect = cw / max(1.0, float(ch))
    dst_aspect = pw / dh

    if abs(src_aspect - dst_aspect) < 0.08:
        tw = max(1, int(round(pw * f.s)))
        th = max(1, int(round(dh * f.s)))
        resized = cv2.resize(crop, (tw, th), interpolation=cv2.INTER_AREA)
        rgba = cv2.cvtColor(resized, cv2.COLOR_BGR2RGBA)
        sk_img = skia.Image.fromarray(rgba)
        c.drawImageRect(sk_img, f.rect(px, dy, pw, dh))
    else:
        # Preservar proporcion 1:1 exacta sin achatar el maniqui 3D y extender el fondo de estudio a los lados
        target_cw = int(round(ch * dst_aspect))
        pad_total = max(0, target_cw - cw)
        pad_l = pad_total // 2
        pad_r = pad_total - pad_l
        padded = cv2.copyMakeBorder(crop, 0, 0, pad_l, pad_r, cv2.BORDER_REPLICATE)
        tw = max(1, int(round(pw * f.s)))
        th = max(1, int(round(dh * f.s)))
        resized = cv2.resize(padded, (tw, th), interpolation=cv2.INTER_AREA)
        rgba = cv2.cvtColor(resized, cv2.COLOR_BGR2RGBA)
        sk_img = skia.Image.fromarray(rgba)
        c.drawImageRect(sk_img, f.rect(px, dy, pw, dh))
    c.restore()


def draw_mobile_comment_panel(f: Frame, panel_rect: list[float], right_pad: float = 22.0) -> None:
    """Draws @tenito03's comment HUGE and crystal-clear inside a panel for mobile legibility,
    with authentic Mixiuh Labs pixel-art framing.
    """
    px, py, pw, ph = panel_rect
    c = f.canvas
    c.save()
    c.clipRRect(rrect(f, px, py, pw, ph, 18.0), skia.ClipOp.kIntersect, True)

    # Fondo laboratorio profundo con resplandor cian
    fill_rrect(f, px, py, pw, ph, 18.0, "#071426", 0.98)

    # Captura real de @tenito03 recortada para eliminar espacios muertos y maximizar el texto en movil
    bgr = cv2.imread(str(COMMENT_IMG_PATH))
    if bgr is not None:
        ih, iw = bgr.shape[:2]
        # Recorte enfocado en el avatar, usuario y las 4 lineas del comentario (sin el espacio vacio derecho)
        crop = bgr[0:ih, 0 : int(iw * 0.86)]
        card_w = pw - 22.0 - right_pad
        card_h = card_w * (crop.shape[0] / crop.shape[1])
        card_x = px + 22.0
        card_y = py + 84.0

        # Sombra y marco pixel-art blanco alrededor del comentario
        fill_rrect(f, card_x - 6, card_y - 6, card_w + 12, card_h + 12, 14.0, "#FFFFFF", 1.0)
        stroke_rrect(f, card_x - 6, card_y - 6, card_w + 12, card_h + 12, 14.0, "#22D3EE", 4.0, 1.0)

        tw = max(1, int(round(card_w * f.s)))
        th = max(1, int(round(card_h * f.s)))
        resized = cv2.resize(crop, (tw, th), interpolation=cv2.INTER_CUBIC)
        rgba = cv2.cvtColor(resized, cv2.COLOR_BGR2RGBA)
        sk_img = skia.Image.fromarray(rgba)
        c.drawImageRect(sk_img, f.rect(card_x, card_y, card_w, card_h))

        # 3 Badges Pixel-Art grandes debajo del comentario
        badges = [
            ("1. PLAYERA 3D", "#34D399"),
            ("2. MOCKUP BLANCO", "#22D3EE"),
            ("3. EXPORTAR REDES", "#FBBF24"),
        ]
        by = card_y + card_h + 22.0
        bw = (card_w - 24.0) / 3.0
        bh = 52.0
        for idx, (btxt, bcol) in enumerate(badges):
            bx = card_x + idx * (bw + 12.0)
            fill_rrect(f, bx, by, bw, bh, 10.0, "#060B14", 0.96)
            stroke_rrect(f, bx, by, bw, bh, 10.0, bcol, 3.0, 0.95)
            draw_text(f, btxt, bx + bw / 2, by + 33.0, "hud", 21.0, bcol, stroke=("#02050A", 3.0))

    c.restore()


def main() -> None:
    VOBO_DIR.mkdir(parents=True, exist_ok=True)
    configure_cc01_models()

    # =========================================================================
    # 1. PREVIEW 9:16 — GANCHO / PORTADA CON SPRITES NUEVOS Y BORDES PIXEL-ART
    # =========================================================================
    set_design(1080, 1920)
    f, arr, surf = new_frame(1080, 1920, t=0.85, fps=60)
    SG.draw_short_bg(f, 0.85, 1.0)

    # Panel superior: Comentario de @tenito03 maximizado para celular
    draw_mobile_comment_panel(f, SG.FLASH_RECT)

    # Panel inferior: Vista limpia de la columna de disenos + prenda central (sin bordes cortados)
    draw_cropped_image_in_panel(
        f,
        GRAB_DIR / "shot_02_samurai_stamp.png",
        (18, 182, 1422, 620),
        SG.ARGON_RECT,
        inset_top=68.0,
        inset_bottom=72.0,
    )

    p_hook = {
        "ep_id": "CC.01",
        "reto": 1,
        "total": 1,
        "line1": "DEL COMENTARIO AL CODIGO",
        "line2": "¿SE PUEDE CREAR UNA MARCA?",
        "active": "both",
        "chips": True,
        "is_hook": True,
        "times": {"flash": 45, "argon": 1},
    }
    SG.short_panels(f, 0.85, 3.0, p_hook)
    SG.short_hook(f, 0.85, 3.0, p_hook)

    surf.makeImageSnapshot().save(str(VOBO_DIR / "vobo_9x16_01_portada_hook.png"), skia.kPNG)

    # =========================================================================
    # 2. PREVIEW 9:16 — ACCION DINAMICA (ZOOM A PRENDA ARRIBA + EXPORTADOR IG ABAJO)
    # =========================================================================
    f2, _, surf2 = new_frame(1080, 1920, t=12.0, fps=60)
    SG.draw_short_bg(f2, 12.0, 1.0)

    # Arriba: Vista limpia del lienzo central (Comparativa 3D Hombre + Mujer completa)
    draw_cropped_image_in_panel(
        f2,
        GRAB_DIR / "shot_04_dual_male_female.png",
        (486, 225, 940, 585),
        SG.FLASH_RECT,
        inset_top=76.0,
        inset_bottom=6.0,
    )
    # Abajo: Vista limpia del Exportador de Historias/Reels de Instagram + Panel de Redes
    draw_cropped_image_in_panel(
        f2,
        GRAB_DIR / "shot_05_instagram_reel_export.png",
        (680, 182, 1222, 748),
        SG.ARGON_RECT,
        inset_top=78.0,
        inset_bottom=6.0,
    )

    SG.short_panels(f2, 1.2, 10.0, {"active": "argon", "chips": True, "reto": 1, "total": 1})
    SG.short_title(
        f2,
        1.2,
        10.0,
        {
            "ep_id": "CC.01",
            "reto": 1,
            "total": 1,
            "kicker": "DEL COMENTARIO AL CODIGO #01 · @TENITO03",
            "title": "SUBE TU LOGO Y EXPORTA",
        },
    )
    SG.short_pop(
        f2,
        0.8,
        2.5,
        {
            "text": "LISTO PARA IG",
            "sub": "POST 9:16 + CATALOGO + PNG",
            "color": "WIN",
            "cy": 1685,
        },
    )
    SG.short_captions(
        f2,
        12.0,
        30.0,
        {
            "groups": [
                {
                    "t0": 11.2,
                    "t1": 13.0,
                    "text": "Y EXPORTARLO A REDES",
                    "words": [
                        {"w": "Y", "t0": 11.2, "t1": 11.5},
                        {"w": "EXPORTARLO", "t0": 11.5, "t1": 12.3},
                        {"w": "A", "t0": 12.3, "t1": 12.5},
                        {"w": "REDES", "t0": 12.5, "t1": 13.0},
                    ],
                }
            ]
        },
    )
    surf2.makeImageSnapshot().save(str(VOBO_DIR / "vobo_9x16_02_accion_zoom_movil.png"), skia.kPNG)

    # =========================================================================
    # 3. PREVIEW 9:16 — PANTALLA DE VEREDICTO Y PANTALLA FINAL MIXIUH LABS
    # =========================================================================
    f3, _, surf3 = new_frame(1080, 1920, t=2.0, fps=60)
    SG.short_verdict(
        f3,
        2.0,
        4.0,
        {
            "ep_id": "01",
            "reto": 1,
            "total": 1,
            "winner": "argon",
            "kicker": "RETO DE @TENITO03 COMPLETADO",
            "times": {"flash": 45, "argon": 1},
        },
    )
    surf3.makeImageSnapshot().save(str(VOBO_DIR / "vobo_9x16_03_veredicto_pixel.png"), skia.kPNG)

    # =========================================================================
    # 4. PREVIEW 16:9 YOUTUBE — COMENTARIO ESTILO CAJA RPG PIXEL-ART + SPLIT ZOOM
    # =========================================================================
    set_design(1920, 1080)
    f4, _, surf4 = new_frame(1920, 1080, t=2.0, fps=60)
    draw_lab_bg(f4, 2.0, intensity=1.0)

    # Panel Izquierdo 16:9: Comentario en caja RPG de doble borde pixel + 3 pasos grandes
    lx, ly, lw, lh = 64.0, 136.0, 864.0, 712.0
    fill_rrect(f4, lx, ly, lw, lh, 12.0, "#081424", 0.96)
    stroke_rrect(f4, lx, ly, lw, lh, 12.0, "INK", 5.0, 0.92)
    stroke_rrect(f4, lx + 10, ly + 10, lw - 20, lh - 20, 6.0, "CYAN", 3.0, 0.85)
    brackets(f4, lx, ly, lw, lh, "CYAN", 0.95, L=28, t=5, off=10)
    draw_mobile_comment_panel(f4, [lx + 18, ly + 56, lw - 36, lh - 74], right_pad=92.0)

    # Panel Derecho 16:9: Zoom gigante al Escenario 3D (Silueta Masculina + Femenina lado a lado)
    rx, ry, rw, rh = 992.0, 136.0, 864.0, 712.0
    fill_rrect(f4, rx, ry, rw, rh, 12.0, "#081424", 0.96)
    stroke_rrect(f4, rx, ry, rw, rh, 12.0, "ARGON", 5.0, 0.92)
    brackets(f4, rx, ry, rw, rh, "ARGON", 0.95, L=28, t=5, off=10)
    draw_cropped_image_in_panel(
        f4,
        GRAB_DIR / "shot_04_dual_male_female.png",
        (474, 110, 964, 946),
        [rx + 14, ry + 14, rw - 28, rh - 28],
        radius=10.0,
    )

    # HUD Superior y Chips con los nuevos sprites ('comment' y 'tshirt')
    hud(f4, 2.0, 10.0, {"reto": 1, "total": 3, "title": "CREA TU MARCA Y MOCKUPS", "score": {"flash": 0, "argon": 1}, "active": "argon"})
    model_label(f4, 2.0, 10.0, {"model": "flash", "text": "RETO @TENITO03", "pos": "panel", "rect": [lx, ly, lw, lh]})
    model_label(f4, 2.0, 10.0, {"model": "argon", "text": "MOCKUP STUDIO 3D", "pos": "panel", "rect": [rx, ry, rw, lh]})
    vs_badge(f4, 2.0, 10.0, {"x": 960, "y": 492, "beam": True, "beam_y0": 136, "beam_y1": 848})

    surf4.makeImageSnapshot().save(str(VOBO_DIR / "vobo_16x9_01_youtube_layout.png"), skia.kPNG)
    print("Generated all VoBo preview frames in:", VOBO_DIR)


if __name__ == "__main__":
    main()
