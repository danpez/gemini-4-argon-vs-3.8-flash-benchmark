#!/usr/bin/env node
/**
 * Deterministic 60.00 FPS Interactive Footage Recorder for Mixiuh Labs Episode 03
 * Records 1920x1080 @ 60fps H.264 (.mov) comparative videos (0..18s IA Sin Kit [flash], 18..36s IA + Superpowers Kit [argon])
 * for all 6 Zero-Shot challenges and writes shotlog JSONs for mlabs.
 */

const { chromium } = require("playwright");
const { spawn } = require("child_process");
const http = require("http");
const fs = require("fs");
const path = require("path");

const ROOT_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep03-superpowers-kit";
let BASE_URL = "http://127.0.0.1:8789";
const OUT_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep03-superpowers-kit/grabaciones";
const SHOTLOG_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/research/footage";
const AUDIO_OUT_DIR_ES = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/episodes/ep03-superpowers-kit/build/project_audio";
const AUDIO_OUT_DIR_EN = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/episodes/ep03-superpowers-kit-en/build/project_audio";
const FFMPEG = "/opt/homebrew/bin/ffmpeg";

const FPS = 60;
const SEG_SEC = 18.0; // 18s IA Sin Kit + 18s IA Superpowers Kit = 36.0s total @ 60fps
const FRAMES_PER_MODEL = Math.round(SEG_SEC * FPS); // 1080 frames
const AUDIO_SR = 48000;

fs.mkdirSync(OUT_DIR, { recursive: true });
fs.mkdirSync(SHOTLOG_DIR, { recursive: true });
fs.mkdirSync(AUDIO_OUT_DIR_ES, { recursive: true });
fs.mkdirSync(AUDIO_OUT_DIR_EN, { recursive: true });

// Helper to click a button containing text (accent-insensitive)
async function clickBtnText(page, textSubstr) {
  await page.evaluate((sub) => {
    const norm = (s) => (s || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
    const target = norm(sub);
    const btns = Array.from(document.querySelectorAll("button, .btn, [role='button']"));
    const b = btns.find((el) => norm(el.textContent).includes(target));
    if (b) {
      const r = b.getBoundingClientRect();
      window.dispatchEvent(new MouseEvent("mousemove", { clientX: r.left + r.width / 2, clientY: r.top + r.height / 2 }));
      window.dispatchEvent(new MouseEvent("mousedown", { clientX: r.left + r.width / 2, clientY: r.top + r.height / 2 }));
      b.click();
      window.dispatchEvent(new MouseEvent("mouseup", { clientX: r.left + r.width / 2, clientY: r.top + r.height / 2 }));
    }
  }, textSubstr);
}

// Per-challenge interactive choreography per frame f in [0..1079] (0..18s)
const CHOREO = {
  "01_galaxia_nbody": {
    dir: "01-galaxia-nbody",
    rawStep: [8.3333, 2],
    superkitStep: [8.3333, 2],
    act: async (page, model, f) => {
      // Phase 1 (0..6s, f 0..360): Smooth 3D camera orbit around colliding galaxies + Rogue Black Hole injection
      if (f === 8) {
        await page.mouse.move(760, 520);
        await page.mouse.down({ button: "left" });
      } else if (f > 8 && f < 220) {
        const u = (f - 8) / 212;
        await page.mouse.move(760 + Math.sin(u * Math.PI * 1.5) * 320, 520 - Math.sin(u * Math.PI) * 90);
      } else if (f === 220) {
        await page.mouse.up({ button: "left" });
      } else if (f === 240) {
        await clickBtnText(page, "Agujero Negro Errante");
      } else if (f === 310) {
        await clickBtnText(page, "Supernova");
      }
      // Phase 2 (6..12s, f 360..720): Switch to Octree 3D Spatial Grid + Binary Quasar + Velocity Heatmap
      if (f === 365) {
        await clickBtnText(page, "Octree 3D");
      } else if (f === 430) {
        await clickBtnText(page, "Cuasar Binario");
      } else if (f > 445 && f < 620) {
        if (f === 446) {
          await page.mouse.move(1080, 500);
          await page.mouse.down({ button: "left" });
        }
        const u = (f - 445) / 175;
        await page.mouse.move(1080 - u * 340, 500 + Math.cos(u * Math.PI * 2) * 75);
        if (f === 619) await page.mouse.up({ button: "left" });
      } else if (f === 640) {
        await clickBtnText(page, "Mapa Termico");
      }
      // Phase 3 (12..18s, f 720..1080): Restore Doppler Spectrum + Einstein Ring / Core Merger + Supernova finale
      if (f === 725) {
        await clickBtnText(page, "Espectro Doppler");
        await clickBtnText(page, "Fusionar Nucleos");
      } else if (f === 830) {
        await clickBtnText(page, "Anillo");
      } else if (f === 920) {
        await clickBtnText(page, "Colision");
        await clickBtnText(page, "Supernova");
      } else if (f > 740 && f < 1060 && f % 4 === 0) {
        const a = (f - 740) * 0.04;
        await page.mouse.move(960 + Math.cos(a) * 240, 540 + Math.sin(a) * 140);
      }
    }
  },

  "02_terminal_trading": {
    dir: "02-terminal-trading",
    rawStep: [8.3333, 2],
    superkitStep: [8.3333, 2],
    act: async (page, model, f) => {
      // Phase 1 (0..6s, f 0..360): Orbit 3D Volatility Surface + Trigger Flash Crash (-25%) + Whale Buy Wall
      if (f === 15) {
        await page.mouse.move(880, 420);
        await page.mouse.down({ button: "left" });
      } else if (f > 15 && f < 140) {
        const u = (f - 15) / 125;
        await page.mouse.move(880 + Math.sin(u * Math.PI * 2) * 160, 420 + Math.cos(u * Math.PI) * 55);
      } else if (f === 140) {
        await page.mouse.up({ button: "left" });
      } else if (f === 155) {
        await clickBtnText(page, "Disparar Flash Crash");
      } else if (f === 265) {
        await clickBtnText(page, "Inyectar Ballena");
      }
      // Phase 2 (6..12s, f 360..720): Switch assets (NVDA-AI -> ETH-PERP) + Short Squeeze + Execute Long Order
      if (f === 365) {
        await clickBtnText(page, "Short Squeeze");
      } else if (f === 450) {
        await clickBtnText(page, "NVDA-AI");
      } else if (f === 520) {
        await clickBtnText(page, "COMPRAR / LONG");
      } else if (f === 610) {
        await clickBtnText(page, "Cascada de Liquidaciones");
      } else if (f > 380 && f < 700 && f % 5 === 0) {
        const a = f * 0.045;
        await page.mouse.move(520 + Math.cos(a) * 340, 420 + Math.sin(a * 1.4) * 180);
      }
      // Phase 3 (12..18s, f 720..1080): Switch back to BTC-PERP + Calm Market -> Final Whale + Short Squeeze
      if (f === 725) {
        await clickBtnText(page, "BTC-PERP");
        await clickBtnText(page, "Calmar Mercado");
      } else if (f === 830) {
        await clickBtnText(page, "Inyectar Ballena");
      } else if (f === 930) {
        await clickBtnText(page, "Disparar Flash Crash");
      } else if (f > 740 && f < 1065 && f % 4 === 0) {
        const a = f * 0.05;
        await page.mouse.move(880 + Math.sin(a) * 180, 410 + Math.cos(a) * 70);
      }
    }
  },

  "03_arcade_boss_rush": {
    dir: "03-arcade-boss-rush",
    rawStep: [8.3333, 2],
    superkitStep: [8.3333, 2],
    act: async (page, model, f) => {
      if (f === 2) {
        await page.mouse.click(960, 540);
      }
      // Phase 1 (0..6s, f 0..360): Phase 1 Quantum Spiral -> Jump to Phase 2 Plasma Lasers & Bullet-Time
      if (f === 140) {
        await clickBtnText(page, "FASE 2");
      } else if (f === 250) {
        await clickBtnText(page, "BULLET-TIME");
      } else if (f === 320) {
        await clickBtnText(page, "BULLET-TIME");
      }
      // Phase 2 (6..12s, f 360..720): Jump to Phase 3 (1500+ Bullets Overdrive) + Turn ON Spatial Hash Debug Mode
      if (f === 365) {
        await clickBtnText(page, "FASE 3");
      } else if (f === 440) {
        await clickBtnText(page, "OLEADA 1600");
        await clickBtnText(page, "DEBUG FISICO");
      } else if (f === 620) {
        await clickBtnText(page, "DETONAR EMP");
      }
      // Phase 3 (12..18s, f 720..1080): Turn OFF Debug Mode + Full Overdrive Curtain + Final EMP Blast
      if (f === 730) {
        await clickBtnText(page, "DEBUG FISICO");
        await clickBtnText(page, "FASE 3");
        await clickBtnText(page, "OLEADA 1600");
      } else if (f === 880) {
        await clickBtnText(page, "BULLET-TIME");
      } else if (f === 960) {
        await clickBtnText(page, "DETONAR EMP");
      }
      if (f % 6 === 0) {
        const a = f * 0.05;
        await page.mouse.move(960 + Math.sin(a) * 320, 680 + Math.cos(a * 1.5) * 140);
      }
    }
  },

  "04_red_zero_trust": {
    dir: "04-red-zero-trust",
    rawStep: [8.3333, 2],
    superkitStep: [8.3333, 2],
    act: async (page, model, f) => {
      // Phase 1 (0..6s, f 0..360): Orbit 3D Cyber-Globe + Launch Massive 850 Gbps DDoS Botnet Attack
      if (f === 10) {
        await page.mouse.move(780, 500);
        await page.mouse.down({ button: "left" });
      } else if (f > 10 && f < 175) {
        const u = (f - 10) / 165;
        await page.mouse.move(780 + u * 380, 500 + Math.sin(u * Math.PI) * 65);
      } else if (f === 175) {
        await page.mouse.up({ button: "left" });
      } else if (f === 190) {
        await clickBtnText(page, "Simular Ataque DDoS Masivo");
      } else if (f === 280) {
        await clickBtnText(page, "Inyectar Exploit SQLi");
      }
      // Phase 2 (6..12s, f 360..720): Activate AI Zero-Trust Shield + Switch to 3D Cluster Graph Topology
      if (f === 365) {
        await clickBtnText(page, "Activar Escudo IA Zero-Trust");
      } else if (f === 445) {
        await clickBtnText(page, "Cambiar Vista");
      } else if (f > 465 && f < 640) {
        if (f === 466) {
          await page.mouse.move(1120, 520);
          await page.mouse.down({ button: "left" });
        }
        const u = (f - 465) / 175;
        await page.mouse.move(1120 - u * 340, 520 - Math.sin(u * Math.PI) * 70);
        if (f === 639) await page.mouse.up({ button: "left" });
      } else if (f === 660) {
        await clickBtnText(page, "Rotar Llaves mTLS");
      }
      // Phase 3 (12..18s, f 720..1080): Switch back to 3D Planetary Globe + Quarantine Node + DDoS Mitigation
      if (f === 725) {
        await clickBtnText(page, "Cambiar Vista");
      } else if (f === 810) {
        await clickBtnText(page, "Simular Ataque DDoS Masivo");
      } else if (f === 890) {
        await clickBtnText(page, "Aislar Nodo");
        await clickBtnText(page, "Activar Escudo IA Zero-Trust");
      } else if (f > 745 && f < 1060) {
        if (f === 746) {
          await page.mouse.move(820, 520);
          await page.mouse.down({ button: "left" });
        }
        const u = (f - 745) / 315;
        await page.mouse.move(820 + Math.sin(u * Math.PI * 2) * 260, 520 + Math.cos(u * Math.PI) * 50);
        if (f === 1059) await page.mouse.up({ button: "left" });
      }
    }
  },

  "05_motor_nodos_ia": {
    dir: "05-motor-nodos-ia",
    rawStep: [8.3333, 2],
    superkitStep: [8.3333, 2],
    act: async (page, model, f) => {
      // Phase 1 (0..6s, f 0..360): Orbit 3D Raymarching Wormhole + Drag node in DAG + Procedural Mutation
      if (f === 12) {
        await page.mouse.move(1450, 440);
        await page.mouse.down({ button: "left" });
      } else if (f > 12 && f < 155) {
        const u = (f - 12) / 143;
        await page.mouse.move(1450 + Math.sin(u * Math.PI * 2) * 180, 440 + Math.cos(u * Math.PI) * 90);
      } else if (f === 155) {
        await page.mouse.up({ button: "left" });
      } else if (f === 185) {
        await clickBtnText(page, "Inyectar Mutacion Procedural");
      } else if (f === 260) {
        await clickBtnText(page, "Auto-Ordenar Grafo");
      }
      // Phase 2 (6..12s, f 360..720): Switch to Preset 2 (4D Cyber-Crystal Fractal) + Orbit 3D Shader
      if (f === 365) {
        await clickBtnText(page, "2. Fractal Ciber-Cristal 4D");
      } else if (f === 415) {
        await page.mouse.move(1420, 460);
        await page.mouse.down({ button: "left" });
      } else if (f > 415 && f < 610) {
        const u = (f - 415) / 195;
        await page.mouse.move(1420 + Math.cos(u * Math.PI * 2) * 210, 460 + Math.sin(u * Math.PI * 2) * 110);
      } else if (f === 610) {
        await page.mouse.up({ button: "left" });
      } else if (f === 640) {
        await clickBtnText(page, "Inyectar Mutacion Procedural");
      }
      // Phase 3 (12..18s, f 720..1080): Switch to Preset 3 (Audio-Reactive Synth Pulse) + Final Wormhole Bloom
      if (f === 725) {
        await clickBtnText(page, "3. Pulso Audio-Reactivo Synth");
      } else if (f === 870) {
        await clickBtnText(page, "1. Agujero de Gusano Raymarching");
        await clickBtnText(page, "Inyectar Mutacion Procedural");
      } else if (f > 740 && f < 1065 && f % 5 === 0) {
        const a = f * 0.05;
        await page.mouse.move(1450 + Math.cos(a) * 180, 450 + Math.sin(a) * 100);
      }
    }
  },

  "06_mixiuh_os_desktop": {
    dir: "06-mixiuh-os-desktop",
    rawStep: [8.3333, 2],
    superkitStep: [8.3333, 2],
    act: async (page, model, f) => {
      // Phase 1 (0..6s, f 0..360): Interact with HoloCore 3D Window (4D Hypercube + Particle Burst) & Terminal Commands
      if (f === 25) {
        await clickBtnText(page, "Hipercubo 4D");
      } else if (f === 95) {
        await clickBtnText(page, "Explosion de Particulas");
      } else if (f === 165) {
        await clickBtnText(page, "benchmark");
      } else if (f === 255) {
        await clickBtnText(page, "Play Arpeggiator");
        await clickBtnText(page, "Acorde Cyber");
      }
      // Phase 2 (6..12s, f 360..720): Dynamic Window Cascade -> Expose -> Tile 4 Apps + Theme Switch + Matrix Terminal
      if (f === 365) {
        await clickBtnText(page, "Cascada Dinamica");
      } else if (f === 455) {
        await clickBtnText(page, "Organizar en Mosaico");
      } else if (f === 520) {
        await clickBtnText(page, "Tema:");
      } else if (f === 590) {
        await clickBtnText(page, "matrix");
      } else if (f === 655) {
        await clickBtnText(page, "Esfera Geodesica");
      }
      // Phase 3 (12..18s, f 720..1080): Global Stress Test + Dock Magnification Sweep + Neofetch + Particle Finale
      if (f === 725) {
        await clickBtnText(page, "Ejecutar Stress Test Global");
        await clickBtnText(page, "Toroide Cuantico");
      } else if (f === 810) {
        await clickBtnText(page, "neofetch");
      } else if (f > 840 && f < 980) {
        // Sweep cursor across the bottom spring-physics Dock!
        const u = (f - 840) / 140;
        await page.mouse.move(760 + Math.sin(u * Math.PI * 2) * 200, 1042);
      } else if (f === 1000) {
        await clickBtnText(page, "Explosion de Particulas");
      }
    }
  }
};

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

    window.addEventListener("DOMContentLoaded", () => {
      const cur = document.createElement("div");
      cur.id = "__rec_cursor";
      cur.style.cssText =
        "position:fixed;left:-100px;top:-100px;width:22px;height:22px;margin:-11px 0 0 -11px;border:2.5px solid #38BDF8;border-radius:50%;pointer-events:none;z-index:2147483647;box-shadow:0 0 12px rgba(56,189,248,0.85), inset 0 0 6px rgba(56,189,248,0.5);transition:transform 0.06s ease, border-color 0.06s ease;";
      document.body.appendChild(cur);
      window.addEventListener(
        "mousemove",
        (e) => {
          cur.style.left = e.clientX + "px";
          cur.style.top = e.clientY + "px";
        },
        { passive: true }
      );
      window.addEventListener(
        "mousedown",
        () => {
          cur.style.transform = "scale(0.72)";
          cur.style.borderColor = "#FBBF24";
          cur.style.background = "rgba(251,191,36,0.28)";
        },
        { passive: true }
      );
      window.addEventListener(
        "mouseup",
        () => {
          cur.style.transform = "scale(1.0)";
          cur.style.borderColor = "#38BDF8";
          cur.style.background = "transparent";
        },
        { passive: true }
      );
    });
  });

  const page = await context.newPage();
  await page.goto(url, { waitUntil: "load", timeout: 30000 });
  // Warm up 45 virtual frames so shaders, particles, and layouts are in full motion at t=0
  await page.evaluate(([dt, sub]) => window.__stepFrame(dt, sub * 45), [stepCfg[0], stepCfg[1]]);
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
      { t0: 0.0, t1: 6.0, model: "flash", desc: "IA Sin Kit (Raw Argon) - Fase 1: Interacción inicial y simulación en vivo", interest: 5, motion: "high" },
      { t0: 6.0, t1: 12.0, model: "flash", desc: "IA Sin Kit (Raw Argon) - Fase 2: Modos visuales y eventos extremos", interest: 5, motion: "high" },
      { t0: 12.0, t1: 18.0, model: "flash", desc: "IA Sin Kit (Raw Argon) - Fase 3: Prueba límite de cierre", interest: 5, motion: "high" },
      { t0: 18.0, t1: 24.0, model: "argon", desc: "IA + Superpowers Kit - Fase 1: Interacción inicial y física a 60-120 FPS", interest: 5, motion: "high" },
      { t0: 24.0, t1: 30.0, model: "argon", desc: "IA + Superpowers Kit - Fase 2: Herramientas avanzadas y shaders", interest: 5, motion: "high" },
      { t0: 30.0, t1: 36.0, model: "argon", desc: "IA + Superpowers Kit - Fase 3: Prueba de estrés final", interest: 5, motion: "high" }
    ],
    highlights: [
      { t0: 0.5, t1: 6.0, model: "flash", use: "hero", why: "Fase 1 interactiva sin kit", roi: [0, 0, 1920, 1080] },
      { t0: 6.0, t1: 12.0, model: "flash", use: "detail", why: "Fase 2 de herramientas sin kit", roi: [0, 0, 1920, 1080] },
      { t0: 12.0, t1: 17.5, model: "flash", use: "action", why: "Fase 3 de estrés sin kit", roi: [0, 0, 1920, 1080] },
      { t0: 18.5, t1: 24.0, model: "argon", use: "hero", why: "Fase 1 interactiva con Superpowers Kit", roi: [0, 0, 1920, 1080] },
      { t0: 24.0, t1: 30.0, model: "argon", use: "detail", why: "Fase 2 de modos y shaders con Superpowers Kit", roi: [0, 0, 1920, 1080] },
      { t0: 30.0, t1: 35.5, model: "argon", use: "action", why: "Fase 3 de estrés final con Superpowers Kit", roi: [0, 0, 1920, 1080] }
    ],
    split_pairs: [
      { flash: [0.5, 6.0], argon: [18.5, 24.0], why: "Comparativa directa de la Fase 1 interactiva (Sin Kit vs Superpowers Kit)." },
      { flash: [6.0, 12.0], argon: [24.0, 30.0], why: "Comparativa directa de la Fase 2 (modos visuales y herramientas)." },
      { flash: [12.0, 17.5], argon: [30.0, 35.5], why: "Comparativa directa de la Fase 3 (prueba límite)." }
    ],
    avoid: []
  };
  const outJson = path.join(SHOTLOG_DIR, `${slug}.json`);
  fs.writeFileSync(outJson, JSON.stringify(shotlog, null, 2));
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

  // 1) Record IA Sin Kit (0..18s = 1080 frames)
  const rawUrl = `${BASE_URL}/ia-sin-kit/${cfg.dir}/index.html`;
  const rawPage = await setupPage(browser, rawUrl, cfg.rawStep);
  for (let f = 0; f < FRAMES_PER_MODEL; f++) {
    await cfg.act(rawPage.page, "flash", f);
    await rawPage.page.evaluate(([dt, sub]) => window.__stepFrame(dt, sub), [cfg.rawStep[0], cfg.rawStep[1]]);
    const buf = await rawPage.page.screenshot({ type: "jpeg", quality: 92 });
    ff.stdin.write(buf);
  }
  await rawPage.context.close();

  // 2) Record IA + Superpowers Kit (18..36s = 1080 frames)
  const kitUrl = `${BASE_URL}/ia-superpowers-kit/${cfg.dir}/index.html`;
  const kitPage = await setupPage(browser, kitUrl, cfg.superkitStep);
  for (let f = 0; f < FRAMES_PER_MODEL; f++) {
    await cfg.act(kitPage.page, "argon", f);
    await kitPage.page.evaluate(([dt, sub]) => window.__stepFrame(dt, sub), [cfg.superkitStep[0], cfg.superkitStep[1]]);
    const buf = await kitPage.page.screenshot({ type: "jpeg", quality: 92 });
    ff.stdin.write(buf);
  }
  await kitPage.context.close();

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

  const sec = ((Date.now() - tStart) / 1000).toFixed(1);
  console.log(`[done]  ${slug} (${FRAMES_PER_MODEL * 2} frames @ 60fps = ${SEG_SEC * 2}s) in ${sec}s`);
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
    const rel = decodeURIComponent((req.url || "/").split("?")[0]);
    if (rel === "/favicon.ico") {
      res.writeHead(204);
      res.end();
      return;
    }
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
  console.log("=== ALL EP03 REAL 60FPS COMPARATIVE MOVIES + SHOTLOGS READY ===");
})();
