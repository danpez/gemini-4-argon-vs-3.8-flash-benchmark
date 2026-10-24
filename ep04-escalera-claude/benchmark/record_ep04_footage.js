#!/usr/bin/env node
/**
 * Deterministic 60.00 FPS Interactive Footage Recorder for Mixiuh Labs Episode 04:
 * La Escalera Completa de Claude 5.5 (Haiku 5.5 vs. Sonnet 5.5 vs. Opus 5.5)
 *
 * Records 1920x1080 @ 60fps H.264 (.mov) comparative videos:
 *   - 0.0s .. 18.0s (flash slot): Dual Split-Screen [HAIKU 5.5 (Left) | SONNET 5.5 (Right)] running simultaneously at 60fps
 *   - 18.0s .. 36.0s (argon slot): Full-Screen [OPUS 5.5] running at 60fps
 * Also writes shotlog JSONs for mlabs and synthesizes 48kHz project_audio WAVs.
 */

const { chromium } = require("playwright");
const { spawn } = require("child_process");
const http = require("http");
const fs = require("fs");
const path = require("path");

const ROOT_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep04-escalera-claude";
let BASE_URL = "http://127.0.0.1:8790";
const OUT_DIR = path.join(ROOT_DIR, "grabaciones");
const SHOTLOG_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/research/footage";
const AUDIO_OUT_DIR_ES = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/episodes/ep04-escalera-claude/build/project_audio";
const AUDIO_OUT_DIR_EN = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/episodes/ep04-escalera-claude-en/build/project_audio";
const FFMPEG = "/opt/homebrew/bin/ffmpeg";

const FPS = 60;
const SEG_SEC = 18.0;
const FRAMES_PER_SLOT = Math.round(SEG_SEC * FPS); // 1080 frames per 18s slot (2160 frames = 36.0s total)

fs.mkdirSync(OUT_DIR, { recursive: true });
fs.mkdirSync(SHOTLOG_DIR, { recursive: true });
fs.mkdirSync(AUDIO_OUT_DIR_ES, { recursive: true });
fs.mkdirSync(AUDIO_OUT_DIR_EN, { recursive: true });

const TELEMETRY = {
  "01-rover-suspension": {
    haiku: { min: "19.2 MIN", cost: "$0.35 USD", loc: "952 LOC", fps: "60 FPS", err: null },
    sonnet: {
      min: "20.1 MIN",
      cost: "$2.51 USD",
      loc: "1,024 LOC",
      fps: "0 FPS (ROTO)",
      err: "[ERROR JS · LINEA 1024] SyntaxError: Unexpected end of input — Sonnet 5.5 trunco el cierre de su bloque JS y dejo el canvas vacio"
    },
    opus: { min: "42.1 MIN", cost: "$6.81 USD", loc: "1,222 LOC", fps: "61 FPS", err: null }
  },
  "02-slime-feromonas": {
    haiku: {
      min: "5.7 MIN",
      cost: "$0.06 USD",
      loc: "867 LOC",
      fps: "0 FPS (ROTO)",
      err: "[ERROR GPU WEBGL2 · LINEA 17] '=' : dimension mismatch — cannot convert from vec3 to out vec4 fragColor"
    },
    sonnet: { min: "6.6 MIN", cost: "$0.79 USD", loc: "827 LOC", fps: "60 FPS", err: null },
    opus: { min: "13.4 MIN", cost: "$2.55 USD", loc: "1,275 LOC", fps: "60 FPS", err: null }
  },
  "03-puente-estructural": {
    haiku: { min: "17.9 MIN", cost: "$0.30 USD", loc: "877 LOC", fps: "61 FPS", err: null },
    sonnet: { min: "17.0 MIN", cost: "$1.98 USD", loc: "1,311 LOC", fps: "60 FPS", err: null },
    opus: { min: "19.7 MIN", cost: "$3.58 USD", loc: "1,535 LOC", fps: "61 FPS", err: null }
  },
  "04-sintetizador-acido-3d": {
    haiku: { min: "8.7 MIN", cost: "$0.21 USD", loc: "948 LOC", fps: "61 FPS (GANADOR ROI)", err: null },
    sonnet: { min: "12.2 MIN", cost: "$1.52 USD", loc: "1,176 LOC", fps: "50 FPS", err: null },
    opus: { min: "31.0 MIN", cost: "$5.00 USD", loc: "1,440 LOC", fps: "61 FPS", err: null }
  },
  "05-pathtracer-bvh": {
    haiku: { min: "14.6 MIN", cost: "$0.13 USD", loc: "1,136 LOC", fps: "37 FPS", err: null },
    sonnet: { min: "13.9 MIN", cost: "$1.67 USD", loc: "1,556 LOC", fps: "29 FPS (GANADOR)", err: null },
    opus: { min: "31.4 MIN", cost: "$5.05 USD", loc: "1,163 LOC", fps: "15 FPS", err: null }
  },
  "06-consola-retro-cpu": {
    haiku: { min: "21.3 MIN", cost: "$0.48 USD", loc: "1,218 LOC", fps: "60 FPS (PONG ACTIVO)", err: null },
    sonnet: { min: "35.2 MIN", cost: "$3.75 USD", loc: "2,111 LOC", fps: "60 FPS (GANADOR)", err: null },
    opus: {
      min: "41.6 MIN",
      cost: "$6.93 USD",
      loc: "2,265 LOC",
      fps: "CRT VACIO (ROM 0 B)",
      err: "[BUG DE ARRANQUE OPUS 5.5] ROM: 0 BYTES · PC=0x200: 0000 -> SYS 0x000 (Su ensamblador fallo al compilar la ROM inicial)"
    }
  }
};

// Helper to click a button containing text inside a target window/document (or all frames)
async function clickBtnInFrames(page, textSubstr) {
  for (const frame of page.frames()) {
    try {
      await frame.evaluate((sub) => {
        const norm = (s) => (s || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
        const target = norm(sub);
        const btns = Array.from(document.querySelectorAll("button, .btn, [role='button'], label, option"));
        const b = btns.find((el) => norm(el.textContent).includes(target));
        if (b) {
          const r = b.getBoundingClientRect();
          window.dispatchEvent(new MouseEvent("mousemove", { clientX: r.left + r.width / 2, clientY: r.top + r.height / 2 }));
          window.dispatchEvent(new MouseEvent("mousedown", { clientX: r.left + r.width / 2, clientY: r.top + r.height / 2 }));
          b.click();
          window.dispatchEvent(new MouseEvent("mouseup", { clientX: r.left + r.width / 2, clientY: r.top + r.height / 2 }));
        }
      }, textSubstr);
    } catch (e) {}
  }
}

async function dispatchCanvasDragInFrames(page, normX, normY, type = "move") {
  for (const frame of page.frames()) {
    try {
      await frame.evaluate(([nx, ny, evType]) => {
        const c = document.querySelector("canvas");
        if (!c) return;
        const r = c.getBoundingClientRect();
        const cx = r.left + r.width * nx;
        const cy = r.top + r.height * ny;
        const opts = { bubbles: true, cancelable: true, clientX: cx, clientY: cy, button: 0, buttons: evType === "up" ? 0 : 1 };
        c.dispatchEvent(new MouseEvent(evType === "down" ? "mousedown" : evType === "up" ? "mouseup" : "mousemove", opts));
        window.dispatchEvent(new MouseEvent(evType === "down" ? "mousedown" : evType === "up" ? "mouseup" : "mousemove", opts));
        if (evType === "click") {
          c.dispatchEvent(new MouseEvent("mousedown", opts));
          c.dispatchEvent(new MouseEvent("mouseup", opts));
          c.dispatchEvent(new MouseEvent("click", opts));
        }
      }, [normX, normY, type]);
    } catch (e) {}
  }
}

const CHOREO = {
  "01_rover_suspension": {
    dir: "01-rover-suspension",
    stepCfg: [8.3333, 2],
    act: async (page, slot, f) => {
      if (f === 90) {
        await clickBtnInFrames(page, "Vectores");
      } else if (f === 180) {
        await clickBtnInFrames(page, "Obstaculos");
        await dispatchCanvasDragInFrames(page, 0.58, 0.62, "click");
      } else if (f === 320) {
        await clickBtnInFrames(page, "Explosion");
        await dispatchCanvasDragInFrames(page, 0.48, 0.68, "click");
      } else if (f === 460) {
        await clickBtnInFrames(page, "6x6");
        await clickBtnInFrames(page, "Marte");
      } else if (f === 620) {
        await clickBtnInFrames(page, "Plasma");
        await clickBtnInFrames(page, "Explosion");
      } else if (f === 780) {
        await clickBtnInFrames(page, "Luna");
        await clickBtnInFrames(page, "4x4");
      } else if (f === 920) {
        await clickBtnInFrames(page, "Tierra");
        await clickBtnInFrames(page, "Explosion");
      }
      if (f % 6 === 0) {
        const a = f * 0.04;
        await dispatchCanvasDragInFrames(page, 0.5 + Math.cos(a) * 0.18, 0.55 + Math.sin(a) * 0.12, "move");
      }
    }
  },

  "02_slime_feromonas": {
    dir: "02-slime-feromonas",
    stepCfg: [8.3333, 2],
    act: async (page, slot, f) => {
      if (f === 30) {
        await dispatchCanvasDragInFrames(page, 0.45, 0.45, "down");
      } else if (f > 30 && f < 180 && f % 3 === 0) {
        const u = (f - 30) / 150;
        await dispatchCanvasDragInFrames(page, 0.45 + Math.cos(u * Math.PI * 2) * 0.18, 0.5 + Math.sin(u * Math.PI * 2) * 0.18, "move");
      } else if (f === 180) {
        await dispatchCanvasDragInFrames(page, 0.45, 0.45, "up");
      } else if (f === 260) {
        await clickBtnInFrames(page, "Guerra de 3 Colonias");
      } else if (f === 480) {
        await clickBtnInFrames(page, "Mitosis Celular");
      } else if (f === 680) {
        await clickBtnInFrames(page, "Red Neuronal");
      } else if (f === 860) {
        await clickBtnInFrames(page, "Red Ferroviaria de Tokio");
      }
    }
  },

  "03_puente_estructural": {
    dir: "03-puente-estructural",
    stepCfg: [8.3333, 2],
    act: async (page, slot, f) => {
      if (f === 40) {
        await clickBtnInFrames(page, "Lanzar Convoy");
      } else if (f === 340) {
        await clickBtnInFrames(page, "Colapso");
        await clickBtnInFrames(page, "Lanzar Convoy");
      } else if (f === 680) {
        await clickBtnInFrames(page, "Sobrecargado");
        await clickBtnInFrames(page, "Lanzar Convoy");
      } else if (f === 920) {
        await clickBtnInFrames(page, "Arco de Acero");
        await clickBtnInFrames(page, "Lanzar Convoy");
      }
    }
  },

  "04_sintetizador_acido_3d": {
    dir: "04-sintetizador-acido-3d",
    stepCfg: [8.3333, 2],
    act: async (page, slot, f) => {
      if (f === 10) {
        await clickBtnInFrames(page, "PLAY");
        await clickBtnInFrames(page, "AUDIO");
      } else if (f === 260) {
        await clickBtnInFrames(page, "Cyberpunk Phonk");
        await clickBtnInFrames(page, "SQR");
      } else if (f === 520) {
        await clickBtnInFrames(page, "Hypnotic Modular");
        await clickBtnInFrames(page, "RANDOM");
      } else if (f === 780) {
        await clickBtnInFrames(page, "Detroit Electro");
        await clickBtnInFrames(page, "SAW");
      }
      if (f > 40 && f < 1040 && f % 4 === 0) {
        const a = f * 0.035;
        await dispatchCanvasDragInFrames(page, 0.5 + Math.cos(a) * 0.22, 0.38 + Math.sin(a) * 0.12, "move");
      }
    }
  },

  "05_pathtracer_bvh": {
    dir: "05-pathtracer-bvh",
    stepCfg: [16.6667, 1],
    act: async (page, slot, f) => {
      if (f === 20) {
        await clickBtnInFrames(page, "Rotacion automatica");
      } else if (f === 360) {
        await clickBtnInFrames(page, "Lentes Opticos");
      } else if (f === 720) {
        await clickBtnInFrames(page, "Anillo de Metales");
      } else if (f === 920) {
        await clickBtnInFrames(page, "Cornell Box");
      }
    }
  },

  "06_consola_retro_cpu": {
    dir: "06-consola-retro-cpu",
    stepCfg: [8.3333, 2],
    act: async (page, slot, f) => {
      if (f === 360) {
        await clickBtnInFrames(page, "STAR INVADERS");
        await clickBtnInFrames(page, "ASSEMBLE");
      } else if (f === 720) {
        await clickBtnInFrames(page, "MATRIX");
        await clickBtnInFrames(page, "MAZE");
        await clickBtnInFrames(page, "ASSEMBLE");
      } else if (f === 920) {
        await clickBtnInFrames(page, "CYBER PONG");
        await clickBtnInFrames(page, "ASSEMBLE");
      }
    }
  }
};

function renderSplitHtml(dir) {
  const t = TELEMETRY[dir];
  const hErrHtml = t.haiku.err
    ? `<div class="err-box err-haiku"><div class="err-kicker">FALLO EN ZERO-SHOT · CLAUDE HAIKU 5.5</div><div class="err-msg">${t.haiku.err}</div></div>`
    : "";
  const sErrHtml = t.sonnet.err
    ? `<div class="err-box err-sonnet"><div class="err-kicker">FALLO EN ZERO-SHOT · CLAUDE SONNET 5.5</div><div class="err-msg">${t.sonnet.err}</div></div>`
    : "";

  return `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { width: 1920px; height: 1080px; overflow: hidden; background: #050811; font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace; }
  .split-wrap { position: relative; width: 1920px; height: 1080px; display: flex; }
  .pane { position: relative; width: 958px; height: 1080px; overflow: hidden; background: #050811; }
  .divider { width: 4px; height: 1080px; background: linear-gradient(180deg, #22D3EE 0%, #F59E0B 50%, #22D3EE 100%); box-shadow: 0 0 18px rgba(34,211,238,0.85); z-index: 50; }
  iframe {
    width: 1440px;
    height: 1080px;
    border: 0;
    transform: scale(0.665277, 1.0);
    transform-origin: 0 0;
    display: block;
  }
  .hud-pill {
    position: absolute;
    bottom: 16px;
    left: 20px;
    right: 20px;
    height: 46px;
    border-radius: 12px;
    background: rgba(5, 8, 18, 0.92);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 18px;
    z-index: 40;
    box-shadow: 0 8px 24px rgba(0,0,0,0.75);
  }
  .hud-haiku { border: 2px solid #22D3EE; }
  .hud-sonnet { border: 2px solid #F59E0B; }
  .m-name { font-size: 17px; font-weight: 800; letter-spacing: 1.2px; }
  .c-haiku { color: #22D3EE; }
  .c-sonnet { color: #F59E0B; }
  .m-stats { font-size: 15px; font-weight: 700; color: #F8FAFC; letter-spacing: 0.8px; }
  .m-cost { color: #10B981; font-weight: 800; }
  .err-box {
    position: absolute;
    top: 46%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 82%;
    padding: 22px 24px;
    background: rgba(24, 6, 14, 0.94);
    border: 2.5px solid #F43F5E;
    border-radius: 16px;
    box-shadow: 0 0 36px rgba(244, 63, 94, 0.55);
    z-index: 45;
    text-align: center;
  }
  .err-kicker { color: #F43F5E; font-size: 16px; font-weight: 900; letter-spacing: 2px; margin-bottom: 10px; }
  .err-msg { color: #FFE4E6; font-size: 14px; line-height: 1.45; font-weight: 600; }
</style>
</head>
<body>
  <div class="split-wrap">
    <div class="pane">
      <iframe id="if_haiku" src="/claude-haiku-5.5/${dir}/index.html"></iframe>
      ${hErrHtml}
      <div class="hud-pill hud-haiku">
        <span class="m-name c-haiku">CLAUDE HAIKU 5.5 ($)</span>
        <span class="m-stats">${t.haiku.min} · <span class="m-cost">${t.haiku.cost}</span> · ${t.haiku.loc} · ${t.haiku.fps}</span>
      </div>
    </div>
    <div class="divider"></div>
    <div class="pane">
      <iframe id="if_sonnet" src="/claude-sonnet-5.5/${dir}/index.html"></iframe>
      ${sErrHtml}
      <div class="hud-pill hud-sonnet">
        <span class="m-name c-sonnet">CLAUDE SONNET 5.5 ($$)</span>
        <span class="m-stats">${t.sonnet.min} · <span class="m-cost">${t.sonnet.cost}</span> · ${t.sonnet.loc} · ${t.sonnet.fps}</span>
      </div>
    </div>
  </div>
  <script>
    window.__stepAll = async (dtMs, substeps) => {
      const f1 = document.getElementById("if_haiku");
      const f2 = document.getElementById("if_sonnet");
      if (f1 && f1.contentWindow && f1.contentWindow.__stepFrame) {
        await f1.contentWindow.__stepFrame(dtMs, substeps);
      }
      if (f2 && f2.contentWindow && f2.contentWindow.__stepFrame) {
        await f2.contentWindow.__stepFrame(dtMs, substeps);
      }
    };
  </script>
</body>
</html>`;
}

function renderOpusWrapperHtml(dir) {
  const t = TELEMETRY[dir];
  const oErrHtml = t.opus.err
    ? `<div class="err-box"><div class="err-kicker">AUDITORIA DE CONSOLA · CLAUDE OPUS 5.5 ($6.93 USD)</div><div class="err-msg">${t.opus.err}</div></div>`
    : "";
  return `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { width: 1920px; height: 1080px; overflow: hidden; background: #050811; font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace; }
  iframe { width: 1920px; height: 1080px; border: 0; display: block; }
  .err-box {
    position: absolute;
    top: 28%;
    left: 29%;
    transform: translate(-50%, -50%);
    width: 46%;
    padding: 20px 24px;
    background: rgba(24, 6, 14, 0.94);
    border: 2.5px solid #F43F5E;
    border-radius: 16px;
    box-shadow: 0 0 36px rgba(244, 63, 94, 0.55);
    z-index: 45;
    text-align: center;
    pointer-events: none;
  }
  .err-kicker { color: #F43F5E; font-size: 16px; font-weight: 900; letter-spacing: 2px; margin-bottom: 8px; }
  .err-msg { color: #FFE4E6; font-size: 14px; line-height: 1.45; font-weight: 600; }
</style>
</head>
<body>
  <iframe id="if_opus" src="/claude-opus-5.5/${dir}/index.html"></iframe>
  ${oErrHtml}
  <script>
    window.__stepAll = async (dtMs, substeps) => {
      const f1 = document.getElementById("if_opus");
      if (f1 && f1.contentWindow && f1.contentWindow.__stepFrame) {
        await f1.contentWindow.__stepFrame(dtMs, substeps);
      }
    };
  </script>
</body>
</html>`;
}

async function setupPage(browser, url, stepCfg) {
  const context = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
  await context.addInitScript(() => {
    let virtualNow = 1000.0;
    let rafQueue = [];
    let rafId = 1;

    window.performance.now = () => virtualNow;
    Date.now = () => Math.floor(1700000000000 + virtualNow);
    window.requestAnimationFrame = (cb) => {
      const id = rafId++;
      rafQueue.push({ id, cb });
      return id;
    };
    window.cancelAnimationFrame = (id) => {
      rafQueue = rafQueue.filter((item) => item.id !== id);
    };

    window.__stepFrame = async (dtMs = 8.333333, substeps = 2) => {
      for (let s = 0; s < substeps; s++) {
        virtualNow += dtMs;
        const batch = rafQueue;
        rafQueue = [];
        for (const item of batch) {
          try {
            item.cb(virtualNow);
          } catch (e) {}
        }
      }
    };

    window.__stepAll = async (dtMs = 8.333333, substeps = 2) => {
      await window.__stepFrame(dtMs, substeps);
      const iframes = document.querySelectorAll("iframe");
      for (const ifr of iframes) {
        try {
          if (ifr.contentWindow && ifr.contentWindow.__stepFrame) {
            await ifr.contentWindow.__stepFrame(dtMs, substeps);
          }
        } catch (e) {}
      }
    };
  });

  const page = await context.newPage();
  await page.goto(url, { waitUntil: "load", timeout: 30000 });
  await page.waitForTimeout(600);
  await page.evaluate(([dt, sub]) => window.__stepAll && window.__stepAll(dt, sub * 45), [stepCfg[0], stepCfg[1]]);
  return { context, page };
}

function writeShotlog(slug, movPath) {
  const shotlog = {
    slug,
    file: movPath,
    duration: SEG_SEC * 2,
    fps: FPS,
    size: [1920, 1080],
    content_box: [0, 0, 1920, 1080],
    segments: [
      { t0: 0.0, t1: 6.0, model: "flash", desc: "Claude Haiku 5.5 (Izq) vs Claude Sonnet 5.5 (Der) - Fase 1", interest: 5, motion: "high" },
      { t0: 6.0, t1: 12.0, model: "flash", desc: "Claude Haiku 5.5 (Izq) vs Claude Sonnet 5.5 (Der) - Fase 2", interest: 5, motion: "high" },
      { t0: 12.0, t1: 18.0, model: "flash", desc: "Claude Haiku 5.5 (Izq) vs Claude Sonnet 5.5 (Der) - Fase 3", interest: 5, motion: "high" },
      { t0: 18.0, t1: 24.0, model: "argon", desc: "Claude Opus 5.5 - Fase 1: Simulacion frontera a 60 FPS", interest: 5, motion: "high" },
      { t0: 24.0, t1: 30.0, model: "argon", desc: "Claude Opus 5.5 - Fase 2: Modos avanzados y telemetria", interest: 5, motion: "high" },
      { t0: 30.0, t1: 36.0, model: "argon", desc: "Claude Opus 5.5 - Fase 3: Prueba de estres final", interest: 5, motion: "high" }
    ],
    highlights: [
      { t0: 0.5, t1: 6.0, model: "flash", use: "hero", why: "Fase 1 Haiku 5.5 vs Sonnet 5.5", roi: [0, 0, 1920, 1080] },
      { t0: 6.0, t1: 12.0, model: "flash", use: "detail", why: "Fase 2 Haiku 5.5 vs Sonnet 5.5", roi: [0, 0, 1920, 1080] },
      { t0: 12.0, t1: 17.5, model: "flash", use: "action", why: "Fase 3 Haiku 5.5 vs Sonnet 5.5", roi: [0, 0, 1920, 1080] },
      { t0: 18.5, t1: 24.0, model: "argon", use: "hero", why: "Fase 1 Opus 5.5", roi: [0, 0, 1920, 1080] },
      { t0: 24.0, t1: 30.0, model: "argon", use: "detail", why: "Fase 2 Opus 5.5", roi: [0, 0, 1920, 1080] },
      { t0: 30.0, t1: 35.5, model: "argon", use: "action", why: "Fase 3 Opus 5.5", roi: [0, 0, 1920, 1080] }
    ],
    split_pairs: [
      { flash: [0.5, 6.0], argon: [18.5, 24.0], why: "Comparativa directa Fase 1 (Haiku+Sonnet vs Opus 5.5)." },
      { flash: [6.0, 12.0], argon: [24.0, 30.0], why: "Comparativa directa Fase 2 (Haiku+Sonnet vs Opus 5.5)." },
      { flash: [12.0, 17.5], argon: [30.0, 35.5], why: "Comparativa directa Fase 3 (Haiku+Sonnet vs Opus 5.5)." }
    ],
    avoid: []
  };
  const outJson = path.join(SHOTLOG_DIR, `${slug}.json`);
  fs.writeFileSync(outJson, JSON.stringify(shotlog, null, 2));
}

function writeProceduralAudioWav(slug) {
  const sr = 48000;
  const dur = 36.0;
  const numSamples = Math.floor(sr * dur);
  const dataSize = numSamples * 2 * 2; // stereo 16-bit
  const buf = Buffer.alloc(44 + dataSize);

  buf.write("RIFF", 0);
  buf.writeUInt32LE(36 + dataSize, 4);
  buf.write("WAVE", 8);
  buf.write("fmt ", 12);
  buf.writeUInt32LE(16, 16);
  buf.writeUInt16LE(1, 20); // PCM
  buf.writeUInt16LE(2, 22); // 2 channels
  buf.writeUInt32LE(sr, 24);
  buf.writeUInt32LE(sr * 4, 28);
  buf.writeUInt16LE(4, 32);
  buf.writeUInt16LE(16, 34);
  buf.write("data", 36);
  buf.writeUInt32LE(dataSize, 40);

  const isAcid = slug.includes("sintetizador") || slug.includes("acido");
  const notes = [55.0, 55.0, 110.0, 55.0, 65.41, 73.42, 55.0, 98.0, 55.0, 55.0, 110.0, 82.41, 65.41, 55.0, 73.42, 87.31];
  const stepDur = 60.0 / 138.0 / 4.0;

  for (let i = 0; i < numSamples; i++) {
    const t = i / sr;
    let sL = 0.0;
    let sR = 0.0;
    if (isAcid) {
      const stepIdx = Math.floor(t / stepDur) % 16;
      const stepPhase = (t % stepDur) / stepDur;
      const freq = notes[stepIdx];
      const env = Math.exp(-stepPhase * 6.5);
      const saw = 2.0 * ((t * freq) - Math.floor(0.5 + t * freq));
      const res = Math.sin(2.0 * Math.PI * freq * (2.0 + 4.0 * env) * t) * 0.45 * env;
      const kickPhase = (t % (stepDur * 4)) / (stepDur * 4);
      const kick = Math.sin(2.0 * Math.PI * (140 * Math.exp(-kickPhase * 18) + 42) * kickPhase) * Math.exp(-kickPhase * 8.0) * 0.55;
      const sig = Math.tanh((saw * 0.35 * env + res + kick) * 1.6) * 0.32;
      sL = sig;
      sR = sig * 0.96;
    } else {
      const pulse = Math.sin(2 * Math.PI * 60 * t) * Math.exp(-((t % 0.5) * 9.0)) * 0.06;
      sL = pulse;
      sR = pulse;
    }
    const pcmL = Math.max(-32767, Math.min(32767, Math.floor(sL * 32767)));
    const pcmR = Math.max(-32767, Math.min(32767, Math.floor(sR * 32767)));
    buf.writeInt16LE(pcmL, 44 + i * 4);
    buf.writeInt16LE(pcmR, 44 + i * 4 + 2);
  }

  const cleanSlug = slug.replace(/^\d+_/, "");
  for (const d of [AUDIO_OUT_DIR_ES, AUDIO_OUT_DIR_EN]) {
    fs.writeFileSync(path.join(d, `${slug}.wav`), buf);
    fs.writeFileSync(path.join(d, `${cleanSlug}.wav`), buf);
  }
}

async function recordChallenge(slug, cfg) {
  const tStart = Date.now();
  const movPath = path.join(OUT_DIR, `${slug}_comparativa.mov`);
  console.log(`[start] ${slug} -> ${movPath}`);

  const browser = await chromium.launch({
    channel: "chrome",
    headless: true,
    args: ["--use-gl=angle", "--enable-webgl", "--ignore-gpu-blocklist", "--autoplay-policy=no-user-gesture-required"]
  });

  const ff = spawn(FFMPEG, [
    "-y", "-hide_banner", "-loglevel", "error",
    "-f", "image2pipe", "-vcodec", "mjpeg", "-framerate", String(FPS), "-i", "-",
    "-c:v", "h264_videotoolbox", "-b:v", "36M", "-profile:v", "high",
    "-pix_fmt", "yuv420p", "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
    "-r", String(FPS), "-movflags", "+faststart",
    movPath
  ]);

  // 1) Record Slot 1 (0..18s = 1080 frames): Split-Screen Haiku 5.5 (Left) + Sonnet 5.5 (Right)
  const splitUrl = `${BASE_URL}/__split_runner?dir=${cfg.dir}`;
  const splitPage = await setupPage(browser, splitUrl, cfg.stepCfg);
  for (let f = 0; f < FRAMES_PER_SLOT; f++) {
    await cfg.act(splitPage.page, "flash", f);
    await splitPage.page.evaluate(([dt, sub]) => window.__stepAll(dt, sub), [cfg.stepCfg[0], cfg.stepCfg[1]]);
    const buf = await splitPage.page.screenshot({ type: "jpeg", quality: 92 });
    ff.stdin.write(buf);
  }
  await splitPage.context.close();

  // 2) Record Slot 2 (18..36s = 1080 frames): Full-Screen Opus 5.5
  const opusUrl = `${BASE_URL}/__opus_runner?dir=${cfg.dir}`;
  const opusPage = await setupPage(browser, opusUrl, cfg.stepCfg);
  for (let f = 0; f < FRAMES_PER_SLOT; f++) {
    await cfg.act(opusPage.page, "argon", f);
    await opusPage.page.evaluate(([dt, sub]) => window.__stepAll(dt, sub), [cfg.stepCfg[0], cfg.stepCfg[1]]);
    const buf = await opusPage.page.screenshot({ type: "jpeg", quality: 92 });
    ff.stdin.write(buf);
  }
  await opusPage.context.close();

  ff.stdin.end();
  await new Promise((res) => ff.on("close", res));
  await browser.close();

  const cleanSlug = slug.replace(/^\d+_/, "");
  const cleanMovPath = path.join(OUT_DIR, `${cleanSlug}_comparativa.mov`);
  try {
    if (fs.existsSync(cleanMovPath)) fs.unlinkSync(cleanMovPath);
    fs.symlinkSync(path.basename(movPath), cleanMovPath);
  } catch (e) {}

  writeShotlog(slug, movPath);
  writeShotlog(cleanSlug, cleanMovPath);
  writeProceduralAudioWav(slug);

  const sec = ((Date.now() - tStart) / 1000).toFixed(1);
  console.log(`[done]  ${slug} (${FRAMES_PER_SLOT * 2} frames @ 60fps = ${SEG_SEC * 2}s) in ${sec}s`);
}

function startStaticServer() {
  const mime = {
    ".html": "text/html; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".json": "application/json",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".svg": "image/svg+xml"
  };
  const srv = http.createServer((req, res) => {
    const u = new URL(req.url || "/", "http://127.0.0.1");
    if (u.pathname === "/favicon.ico") {
      res.writeHead(204);
      res.end();
      return;
    }
    if (u.pathname === "/__split_runner") {
      const dir = u.searchParams.get("dir") || "01-rover-suspension";
      res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      res.end(renderSplitHtml(dir));
      return;
    }
    if (u.pathname === "/__opus_runner") {
      const dir = u.searchParams.get("dir") || "01-rover-suspension";
      res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      res.end(renderOpusWrapperHtml(dir));
      return;
    }
    const rel = decodeURIComponent(u.pathname);
    const p = path.join(ROOT_DIR, rel);
    if (fs.existsSync(p) && fs.statSync(p).isFile()) {
      res.writeHead(200, { "Content-Type": mime[path.extname(p)] || "application/octet-stream" });
      fs.createReadStream(p).pipe(res);
    } else {
      res.writeHead(404);
      res.end("Not found");
    }
  });
  return new Promise((resolve) => {
    srv.listen(0, "127.0.0.1", () => {
      BASE_URL = `http://127.0.0.1:${srv.address().port}`;
      console.log(`[server] Serving ${ROOT_DIR} at ${BASE_URL}`);
      resolve(srv);
    });
  });
}

(async () => {
  const srv = await startStaticServer();
  const filters = process.argv.slice(2);
  const entries = Object.entries(CHOREO).filter(([k]) => !filters.length || filters.some((f) => k.includes(f)));
  for (let i = 0; i < entries.length; i += 3) {
    const batch = entries.slice(i, i + 3);
    console.log(`=== Starting batch ${i / 3 + 1}: ${batch.map((b) => b[0]).join(", ")} ===`);
    await Promise.all(batch.map(([slug, cfg]) => recordChallenge(slug, cfg)));
  }
  srv.close();
  console.log("=== ALL EP04 REAL 60FPS COMPARATIVE MOVIES + SHOTLOGS READY ===");
})();
