#!/usr/bin/env python3
"""Generates a 12-second 1920x1080 @ 60fps hero clip showing @tenito03's real Instagram comment
framed in the authentic Mixiuh Labs pixel-art RPG dialog box over the live Verlet cloth simulation
from Episode 02, for use in both the 16:9 YouTube episode and thumbnails.
"""
from __future__ import annotations

import math
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
import skia

MLABS_ROOT = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs")
sys.path.insert(0, str(MLABS_ROOT))

from mlabs import sprites as SP
from mlabs.gfx.base import Frame, draw_text, fill_rrect, new_frame, rrect, set_design, stroke_rrect
from mlabs.gfx.cards import brackets

COMMENT_IMG_PATH = Path(
    "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/del-comentario-al-codigo/"
    "ep01-marca-ropa-verlet/comentario-original/comentario_tenito03_ig.jpg"
)
BG_VIDEO_PATH = Path(
    "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep02-argon-vs-opus/"
    "grabaciones/01_tela_verlet_comparativa.mov"
)
OUT_CLIP_PATH = Path(
    "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/del-comentario-al-codigo/"
    "ep01-marca-ropa-verlet/grabaciones/comentario_tenito03_hero.mov"
)


def out_back(t: float) -> float:
    t = max(0.0, min(1.0, t))
    c1 = 1.70158
    c3 = c1 + 1.0
    return 1.0 + c3 * pow(t - 1.0, 3) + c1 * pow(t - 1.0, 2)


def main() -> None:
    W, H = 1920, 1080
    FPS = 60
    DUR = 12.0
    TOTAL_FRAMES = int(DUR * FPS)

    bgr_comment = cv2.imread(str(COMMENT_IMG_PATH))
    if bgr_comment is None:
        raise RuntimeError(f"Could not open {COMMENT_IMG_PATH}")
    ih, iw = bgr_comment.shape[:2]
    crop_comment = bgr_comment[0:ih, 0 : int(iw * 0.86)]
    rgba_comment = cv2.cvtColor(crop_comment, cv2.COLOR_BGR2RGBA)
    comment_skia = skia.Image.fromarray(rgba_comment)

    cap = cv2.VideoCapture(str(BG_VIDEO_PATH))
    bg_fps = cap.get(cv2.CAP_PROP_FPS) or 60.0
    start_frame = int(19.0 * bg_fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    set_design(W, H)

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
            "35M",
            "-pix_fmt",
            "yuv420p",
            str(OUT_CLIP_PATH),
        ],
        stdin=subprocess.PIPE,
    )

    for f_idx in range(TOTAL_FRAMES):
        t = f_idx / FPS
        ret, frame_bgr = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            ret, frame_bgr = cap.read()

        frame_rgba = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGBA)
        bg_img = skia.Image.fromarray(frame_rgba)

        f, _, surf = new_frame(W, H, t=t, fps=FPS)
        c = f.canvas
        c.drawImageRect(bg_img, skia.Rect.MakeWH(W, H))

        # Dark laboratory vignette overlay so the pixel-art RPG box pops with high contrast
        c.drawRect(skia.Rect.MakeWH(W, H), skia.Paint(Color=skia.Color(5, 11, 20, 205)))

        # Subtle cyan grid lines
        p_grid = skia.Paint(Color=skia.Color(34, 211, 238, 20), StrokeWidth=1.0, AntiAlias=True)
        for gx in range(0, W, 64):
            c.drawLine(gx, 0, gx, H, p_grid)
        for gy in range(0, H, 64):
            c.drawLine(0, gy, W, gy, p_grid)

        s_in = out_back(min(1.0, t / 0.42))
        float_y = math.sin(t * 2.4) * 5.0

        box_w, box_h = 1280.0, 620.0
        bx = (W - box_w) * 0.5
        by = (H - box_h) * 0.5 - 24.0 + float_y

        c.save()
        c.translate(W * 0.5, by + box_h * 0.5)
        c.scale(s_in, s_in)
        c.translate(-W * 0.5, -(by + box_h * 0.5))

        # Authentic Mixiuh Labs double-border RPG frame + corner brackets
        fill_rrect(f, bx, by, box_w, box_h, 14.0, "#071426", 0.97)
        stroke_rrect(f, bx, by, box_w, box_h, 14.0, "INK", 5.0, 0.94)
        stroke_rrect(f, bx + 10, by + 10, box_w - 20, box_h - 20, 8.0, "#22D3EE", 3.5, 0.90)
        brackets(f, bx, by, box_w, box_h, "#22D3EE", 0.96, L=32, t=5, off=10)

        # Header kicker + comment sprite
        SP.draw_sprite(f, "comment", bx + 64, by + 48, 3.2)
        draw_text(
            f,
            "DEL COMENTARIO AL CODIGO #01 · RETO DE @TENITO03",
            W * 0.5 + 16,
            by + 56,
            "hud",
            25.0,
            "#22D3EE",
            stroke=("#02050A", 4.0),
        )

        # Cropped comment card inside white frame
        card_w = box_w - 110.0
        card_h = card_w * (comment_skia.height() / comment_skia.width())
        card_x = bx + 55.0
        card_y = by + 84.0
        fill_rrect(f, card_x - 6, card_y - 6, card_w + 12, card_h + 12, 14.0, "#FFFFFF", 1.0)
        stroke_rrect(f, card_x - 6, card_y - 6, card_w + 12, card_h + 12, 14.0, "#22D3EE", 4.0, 1.0)
        c.drawImageRect(comment_skia, f.rect(card_x, card_y, card_w, card_h))

        # 3 Pixel-Art Challenge Pills
        badges = [
            ("1. PLAYERA 3D", "#34D399"),
            ("2. MOCKUP BLANCO", "#22D3EE"),
            ("3. EXPORTAR REDES", "#FBBF24"),
        ]
        p_y = card_y + card_h + 26.0
        p_w = (card_w - 32.0) / 3.0
        p_h = 56.0
        for idx, (btxt, bcol) in enumerate(badges):
            active = t > (0.45 + idx * 0.55)
            p_x = card_x + idx * (p_w + 16.0)
            fill_rrect(f, p_x, p_y, p_w, p_h, 10.0, "#050B14", 0.96 if active else 0.65)
            stroke_rrect(f, p_x, p_y, p_w, p_h, 10.0, bcol, 3.5 if active else 2.0, 0.96 if active else 0.45)
            draw_text(
                f,
                btxt,
                p_x + p_w * 0.5,
                p_y + 36.0,
                "hud",
                23.0,
                bcol if active else "MUTED",
                stroke=("#02050A", 3.5),
            )

        c.restore()
        ff.stdin.write(surf.makeImageSnapshot().tobytes())

    ff.stdin.close()
    ff.wait()
    cap.release()
    print(f"Created {OUT_CLIP_PATH} ({OUT_CLIP_PATH.stat().st_size / (1024*1024):.1f} MB)")


if __name__ == "__main__":
    main()
