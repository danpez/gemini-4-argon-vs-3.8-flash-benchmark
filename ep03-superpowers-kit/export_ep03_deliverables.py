#!/usr/bin/env python3
"""Empaqueta y escala a 4K60 los Shorts, miniaturas 4K y videos maestros del Episodio 03 (ES + EN)."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs")
sys.path.insert(0, str(ROOT))

from mlabs import spec as spec_mod
from mlabs import timeline as tl_mod
from mlabs.package import shorts as sh_mod

EP03_ROOT = Path("/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep03-superpowers-kit")
ICLOUD_ROOT = Path("/Users/kevingonzalezlopez/Library/Mobile Documents/com~apple~CloudDocs/Mixiuh/Mixiuh Labs")


def upscale_short_4k(src_mp4: Path, dst_mp4: Path, thumb_png: Path) -> None:
    dst_mp4.parent.mkdir(parents=True, exist_ok=True)
    thumb_png.parent.mkdir(parents=True, exist_ok=True)
    # 1. Upscale 1080x1920@60 -> 2160x3840@60 con lanczos + cas=0.35
    cmd_vid = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(src_mp4),
        "-vf", "scale=2160:3840:flags=lanczos,cas=0.35",
        "-c:v", "h264_videotoolbox", "-b:v", "45M", "-maxrate", "55M", "-bufsize", "90M",
        "-pix_fmt", "yuv420p", "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
        "-r", "60", "-c:a", "copy", "-movflags", "+faststart",
        str(dst_mp4),
    ]
    subprocess.run(cmd_vid, check=True)
    # 2. Exportar miniatura 4K PNG en t=0.85s
    cmd_png = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-ss", "0.85", "-i", str(dst_mp4),
        "-frames:v", "1",
        str(thumb_png),
    ]
    subprocess.run(cmd_png, check=True)


def process_lang(ep_folder: str, local_out_name: str, icloud_folder_name: str, is_en: bool = False) -> None:
    ep_dir = ROOT / "episodes" / ep_folder
    yaml_path = ep_dir / "episode.yaml"
    tl_path = ep_dir / "build" / "timeline.json"
    out_dir = ep_dir / "out"

    ep = spec_mod.load(yaml_path)
    tl = tl_mod.load(tl_path)

    print(f"=== Generando 6 Shorts nativos para {ep_folder} ===")
    res = sh_mod.build_all(ep, tl, out_dir, draft=False, workers=4)
    for r in res:
        print(f"  Short listo: {r['path']} ({r['duration']:.2f}s)")

    local_dest = EP03_ROOT / local_out_name
    local_shorts = local_dest / "shorts_4k60"
    local_thumbs = local_dest / ("thumbnails_4k" if is_en else "miniaturas_4k")
    local_shorts.mkdir(parents=True, exist_ok=True)
    local_thumbs.mkdir(parents=True, exist_ok=True)

    icloud_dest = ICLOUD_ROOT / icloud_folder_name
    icloud_shorts = icloud_dest / "shorts"
    icloud_thumbs = icloud_dest / ("thumbnails_4k" if is_en else "miniaturas_4k")
    icloud_shorts.mkdir(parents=True, exist_ok=True)
    icloud_thumbs.mkdir(parents=True, exist_ok=True)

    # Escalar cada Short a 4K60 y extraer su miniatura 4K PNG
    for mp4 in sorted((out_dir / "shorts").glob("[0-9][0-9]_*.mp4")):
        stem = mp4.stem
        dst_4k = local_shorts / f"{stem}_4k60.mp4"
        png_4k = local_thumbs / f"{stem}_portada_4k.png"
        print(f"  Escalando a 4K60 (2160x3840) + miniatura PNG: {stem}")
        upscale_short_4k(mp4, dst_4k, png_4k)
        shutil.copy2(dst_4k, icloud_shorts / mp4.name)
        shutil.copy2(png_4k, icloud_thumbs / png_4k.name)

    # Copiar shorts.md, video maestro 4K60, subtitulos y paquete
    for f in out_dir.glob("*"):
        if f.is_file():
            shutil.copy2(f, local_dest / f.name)
            shutil.copy2(f, icloud_dest / f.name)
    if (out_dir / "shorts" / "shorts.md").exists():
        shutil.copy2(out_dir / "shorts" / "shorts.md", local_shorts / "shorts.md")
        shutil.copy2(out_dir / "shorts" / "shorts.md", icloud_shorts / "shorts.md")
    if (out_dir / "thumbnails").is_dir():
        shutil.copytree(out_dir / "thumbnails", local_dest / "thumbnails_youtube", dirs_exist_ok=True)
        shutil.copytree(out_dir / "thumbnails", icloud_dest / "thumbnails", dirs_exist_ok=True)
    if (EP03_ROOT / "mixiuh-superpowers-kit.zip").exists():
        shutil.copy2(EP03_ROOT / "mixiuh-superpowers-kit.zip", local_dest / "mixiuh-superpowers-kit.zip")
        shutil.copy2(EP03_ROOT / "mixiuh-superpowers-kit.zip", icloud_dest / "mixiuh-superpowers-kit.zip")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "both"
    if mode in ("es", "both"):
        process_lang("ep03-superpowers-kit", "entregables_finales_4k_es", "EP03 Superpowers Kit", is_en=False)
    if mode in ("en", "both"):
        process_lang("ep03-superpowers-kit-en", "entregables_finales_4k_en", "EP03 Superpowers Kit - English", is_en=True)
