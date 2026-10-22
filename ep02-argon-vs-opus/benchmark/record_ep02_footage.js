#!/usr/bin/env node
/**
 * Deterministic 60.00 FPS Interactive Footage Recorder for Mixiuh Labs Episode 02
 * Records 1920x1080 @ 60fps H.264 (.mov) comparative videos (0..18s Opus 5.5, 18..36s Argon 4)
 * for all 6 Zero-Shot challenges and writes shotlog JSONs for mlabs.
 */

const { chromium } = require("playwright");
const { spawn } = require("child_process");
const http = require("http");
const fs = require("fs");
const path = require("path");

const ROOT_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep02-argon-vs-opus";
let BASE_URL = "http://127.0.0.1:8788";
const OUT_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep02-argon-vs-opus/grabaciones";
const SHOTLOG_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/research/footage";
const AUDIO_OUT_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/claude-mixiuh-labs/episodes/ep02-argon-vs-opus/build/project_audio";
const FFMPEG = "/opt/homebrew/bin/ffmpeg";

const FPS = 60;
const SEG_SEC = 18.0; // 18s Opus 5.5 + 18s Gemini 4 Argon = 36.0s total @ 60fps
const FRAMES_PER_MODEL = Math.round(SEG_SEC * FPS); // 1080 frames
const AUDIO_SR = 48000;

fs.mkdirSync(OUT_DIR, { recursive: true });
fs.mkdirSync(SHOTLOG_DIR, { recursive: true });
fs.mkdirSync(AUDIO_OUT_DIR, { recursive: true });

// Helper to click a button containing text
async function clickBtnText(page, textSubstr) {
  await page.evaluate((sub) => {
    const btns = Array.from(document.querySelectorAll("button, .btn, [role='button']"));
    const b = btns.find(el => (el.textContent || "").toLowerCase().includes(sub.toLowerCase()));
    if (b) b.click();
  }, textSubstr);
}

async function clickId(page, id) {
  await page.evaluate((elId) => {
    const el = document.getElementById(elId);
    if (el) el.click();
  }, id);
}

// Per-challenge interactive choreography per frame f in [0..1079] (0..18s)
const CHOREO = {
  "01_tela_verlet": {
    dir: "01-tela-verlet",
    opusStep: [35.7, 1],  // ~28 FPS authentic CPU solver load
    argonStep: [8.3333, 2], // 120 FPS
    act: async (page, model, f) => {
      if (f === 1) {
        await page.mouse.move(960, 420);
      }
      // Phase 1 (0..6s, f 0..360): Elastic grab & stretch in Tension Heatmap mode (gentle so cloth stays on hooks)
      if (f === 25) {
        await page.mouse.move(820, 440);
        await page.mouse.down({ button: "left" });
      } else if (f > 25 && f < 160) {
        const t = (f - 25) / 135;
        await page.mouse.move(820 + Math.sin(t * Math.PI * 2) * 120, 440 + Math.sin(t * Math.PI) * 95);
      } else if (f === 160) {
        await page.mouse.up({ button: "left" });
      } else if (f === 210) {
        // Switch to Volumetric Shaded mode
        await clickBtnText(page, "Volumétrico");
      } else if (f > 225 && f < 345) {
        const a = (f - 225) * 0.08;
        if (f === 226) {
          await page.mouse.move(900, 450);
          await page.mouse.down({ button: "left" });
        }
        await page.mouse.move(900 + Math.cos(a) * 110, 450 + Math.sin(a) * 80);
        if (f === 344) await page.mouse.up({ button: "left" });
      }
      // Phase 2 (6..12s, f 360..720): Laser Scalpel partial lower cuts (cloth stays hanging on top hooks!)
      if (f === 365) {
        await clickBtnText(page, "Tensión");
        await clickBtnText(page, "Bisturí");
      } else if (f === 385) {
        await page.mouse.move(680, 560);
        await page.mouse.down({ button: "right" });
      } else if (f > 385 && f < 490) {
        const u = (f - 385) / 105;
        await page.mouse.move(680 + u * 240, 560 + Math.sin(u * Math.PI) * 50);
      } else if (f === 490) {
        await page.mouse.up({ button: "right" });
      } else if (f === 530) {
        await page.mouse.move(960, 580);
        await page.mouse.down({ button: "right" });
      } else if (f > 530 && f < 640) {
        const u = (f - 530) / 110;
        await page.mouse.move(960 + u * 220, 580 - u * 60);
      } else if (f === 640) {
        await page.mouse.up({ button: "right" });
      }
      // Phase 3 (12..18s, f 720..1080): Reset fresh cloth + Cyberpunk Neon mode + elastic waves
      if (f === 722) {
        await clickBtnText(page, "Reiniciar");
        await clickBtnText(page, "Neón");
        await clickBtnText(page, "Agarrar");
        await clickBtnText(page, "Agarre");
      } else if (f === 755) {
        await page.mouse.move(880, 440);
        await page.mouse.down({ button: "left" });
      } else if (f > 755 && f < 940) {
        const a = (f - 755) * 0.08;
        await page.mouse.move(880 + Math.cos(a) * 130, 440 + Math.sin(a) * 95);
      } else if (f === 940) {
        await page.mouse.up({ button: "left" });
      } else if (f === 980 && model === "flash") {
        await clickBtnText(page, "Onda");
      }
    }
  },

  "02_fluidos_navier_stokes": {
    dir: "02-fluidos-navier-stokes",
    opusStep: [8.3333, 2],
    argonStep: [8.3333, 2],
    act: async (page, model, f) => {
      if (f === 1) {
        await page.mouse.move(860, 540);
        await page.mouse.down({ button: "left" });
      }
      // Phase 1 (0..6s, f 0..360): Bioluminescent swirling figure-8 vortices + multicolor burst
      if (f > 1 && f < 340) {
        if (f === 120) {
          await page.keyboard.press("Space");
          if (model === "argon") await clickBtnText(page, "Explosión Multicolor");
        }
        const t = f * 0.055;
        const x = 860 + Math.sin(t) * 380;
        const y = 540 + Math.sin(t * 2) * 240;
        await page.mouse.move(x, y);
      }
      // Phase 2 (6..12s, f 360..720): Kármán Vortex Street + Vorticity Curl / Velocity visualization
      if (f === 360) {
        await page.mouse.up({ button: "left" });
        if (model === "flash") {
          await page.keyboard.press("t");
          await page.keyboard.press("o");
          await page.keyboard.press("3"); // Vorticity mode
        } else {
          await clickBtnText(page, "Preset Calle Kármán");
          await clickBtnText(page, "3. Vorticidad");
        }
        await page.mouse.move(700, 540);
        await page.mouse.down({ button: "left" });
      } else if (f > 365 && f < 700) {
        if (f === 540) {
          if (model === "flash") await page.keyboard.press("2"); // Velocity
          else await clickBtnText(page, "2. Velocidad");
        }
        const t = (f - 360) * 0.06;
        await page.mouse.move(780 + Math.cos(t) * 320, 540 + Math.sin(t * 1.5) * 220);
      }
      // Phase 3 (12..18s, f 720..1080): Pressure heatmap -> Bioluminescent HDR finale + Wall drawing
      if (f === 720) {
        if (model === "flash") await page.keyboard.press("4"); // Pressure
        else await clickBtnText(page, "4. Presión");
      } else if (f === 840) {
        if (model === "flash") {
          await page.keyboard.press("1");
          await page.keyboard.press("Space");
        } else {
          await clickBtnText(page, "1. Bioluminiscente");
          await clickBtnText(page, "Explosión Multicolor");
        }
      } else if (f > 720 && f < 1070) {
        const t = f * 0.07;
        await page.mouse.move(880 + Math.cos(t) * 360, 540 + Math.sin(t * 2) * 250);
      } else if (f === 1075) {
        await page.mouse.up({ button: "left" });
      }
    }
  },

  "03_cuerpo_blando_sdf": {
    dir: "03-cuerpo-blando-sdf",
    opusStep: [12.2, 1], // ~82 FPS authentic tetrahedral XPBD load
    argonStep: [8.3333, 2], // 120 FPS
    act: async (page, model, f) => {
      // Phase 1 (0..6s, f 0..360): Grab soft body, fling it, spawn rain of gummies
      if (f === 20) {
        await page.mouse.move(820, 520);
        await page.mouse.down({ button: "left" });
      } else if (f > 20 && f < 110) {
        const u = (f - 20) / 90;
        await page.mouse.move(820 + Math.sin(u * Math.PI * 2) * 220, 520 - u * 240);
      } else if (f === 110) {
        await page.mouse.up({ button: "left" });
      } else if (f === 140) {
        if (model === "flash") await clickId(page, "bRain");
        else await clickId(page, "spawn-rain");
      } else if (f === 260) {
        if (model === "flash") await clickId(page, "bStomp");
        else await clickId(page, "btn-stomp");
      }
      // Phase 2 (6..12s, f 360..720): Skeleton + Skin internal springs view & Radial Blast
      if (f === 370) {
        if (model === "flash") await clickId(page, "tSkel");
        else await clickBtnText(page, "Esqueleto + Piel");
      } else if (f === 430) {
        await page.mouse.move(780, 560);
        await page.mouse.down({ button: "left" });
      } else if (f > 430 && f < 560) {
        const a = (f - 430) * 0.08;
        await page.mouse.move(780 + Math.cos(a) * 220, 500 + Math.sin(a) * 160);
      } else if (f === 560) {
        await page.mouse.up({ button: "left" });
      } else if (f === 600) {
        if (model === "flash") await clickId(page, "bBlast");
        else await clickId(page, "btn-blast");
      }
      // Phase 3 (12..18s, f 720..1080): Restore glossy skin + Zero-G + Bullet Time + Massive Stomp
      if (f === 730) {
        if (model === "flash") {
          await clickId(page, "tSkel");
          await clickId(page, "tZeroG");
        } else {
          await clickBtnText(page, "Esqueleto + Piel");
          await clickId(page, "btn-zero-g");
        }
      } else if (f === 830) {
        if (model === "flash") await clickId(page, "bBlast");
        else await clickId(page, "btn-blast");
      } else if (f === 920) {
        if (model === "flash") {
          await clickId(page, "tZeroG");
          await clickId(page, "bStomp");
        } else {
          await clickId(page, "btn-zero-g");
          await clickId(page, "btn-stomp");
        }
      }
    }
  },

  "04_voxel_minecraft": {
    dir: "04-voxel-minecraft",
    opusStep: [8.3333, 2],
    argonStep: [8.3333, 2],
    act: async (page, model, f) => {
      // Phase 1 (0..3.5s, f 0..210): Smooth orbital pan around voxel world
      if (f === 10) {
        await page.mouse.move(700, 500);
        await page.mouse.down({ button: "left" });
      } else if (f > 10 && f < 195) {
        const u = (f - 10) / 185;
        await page.mouse.move(700 + u * 480, 500 + Math.sin(u * Math.PI) * 70);
      } else if (f === 195) {
        await page.mouse.up({ button: "left" });
      }
      // Phase 2 (3.5..10.5s, f 210..630): Frame-locked block breaking, placing & glowing lanterns!
      // Every click at f_click is preceded by mouse.move at f_click - 4 so raycast highlights the block first.
      if (f === 225) {
        await page.keyboard.press("Digit8"); // Select Glow / Farol block
      } else if (f === 227) {
        await page.mouse.move(960, 580);
      } else if (f === 231) {
        await page.mouse.click(960, 580, { button: "right" }); // t_beat = 0.350s (lantern)
      } else if (f === 257) {
        await page.mouse.move(890, 600);
      } else if (f === 261) {
        await page.mouse.click(890, 600, { button: "left" });  // t_beat = 0.850s (break)
      } else if (f === 290) {
        await page.mouse.move(1030, 600);
      } else if (f === 294) {
        await page.mouse.click(1030, 600, { button: "left" }); // t_beat = 1.400s (break)
      } else if (f === 329) {
        await page.mouse.move(950, 620);
      } else if (f === 333) {
        await page.mouse.click(950, 620, { button: "right" }); // t_beat = 2.050s (lantern)
      } else if (f === 348) {
        // t_beat = 2.300s: Switch to Sunset & select Wood/Brick slot
        if (model === "flash") await page.evaluate(() => { const b = document.querySelector('[data-t="0.745"]'); if (b) b.click(); });
        else await clickBtnText(page, "Atardecer");
        await page.keyboard.press("Digit4");
      } else if (f === 352) {
        await page.mouse.move(1080, 520);
        await page.mouse.down({ button: "left" });
      } else if (f > 352 && f < 392) {
        const u = (f - 352) / 40;
        await page.mouse.move(1080 - u * 240, 520 - Math.sin(u * Math.PI) * 35);
      } else if (f === 392) {
        await page.mouse.up({ button: "left" });
      } else if (f === 401) {
        await page.mouse.move(900, 590);
      } else if (f === 405) {
        await page.mouse.click(900, 590, { button: "right" }); // t_beat = 3.250s (place)
      } else if (f === 437) {
        await page.mouse.move(1020, 610);
      } else if (f === 441) {
        await page.mouse.click(1020, 610, { button: "left" }); // t_beat = 3.850s (break)
      } else if (f === 462) {
        // t_beat = 4.200s: Switch to Night & select Glow / Farol slot
        if (model === "flash") await page.evaluate(() => { const b = document.querySelector('[data-t="0.0"]'); if (b) b.click(); });
        else await clickBtnText(page, "Noche");
        await page.keyboard.press("Digit8");
      } else if (f === 479) {
        await page.mouse.move(940, 580);
      } else if (f === 483) {
        await page.mouse.click(940, 580, { button: "right" }); // t_beat = 4.550s (lantern)
      } else if (f === 518) {
        await page.mouse.move(1000, 620);
      } else if (f === 522) {
        await page.mouse.click(1000, 620, { button: "right" }); // t_beat = 5.200s (lantern)
      } else if (f === 557) {
        await page.mouse.move(880, 610);
      } else if (f === 561) {
        await page.mouse.click(880, 610, { button: "left" });  // t_beat = 5.850s (break)
      } else if (f === 593) {
        await page.mouse.move(960, 600);
      } else if (f === 597) {
        await page.mouse.click(960, 600, { button: "right" }); // t_beat = 6.450s (lantern)
      } else if (f === 610) {
        await page.mouse.move(1100, 520);
        await page.mouse.down({ button: "left" });
      } else if (f > 610 && f < 715) {
        const u = (f - 610) / 105;
        await page.mouse.move(1100 - u * 320, 520 - Math.sin(u * Math.PI) * 40);
      } else if (f === 715) {
        await page.mouse.up({ button: "left" });
      }
      // Phase 3 (12..18s, f 720..1080): Daylight + New Procedural Seed regeneration + pan
      if (f === 725) {
        if (model === "flash") {
          await page.evaluate(() => { const b = document.querySelector('[data-t="0.5"]'); if (b) b.click(); });
          await clickId(page, "rnd");
        } else {
          await clickBtnText(page, "Mediodía");
          await clickId(page, "btn-random-seed");
        }
      } else if (f === 770) {
        await page.mouse.move(760, 480);
        await page.mouse.down({ button: "left" });
      } else if (f > 770 && f < 1050) {
        const u = (f - 770) / 280;
        await page.mouse.move(760 + u * 420, 480 + Math.cos(u * Math.PI) * 50);
      } else if (f === 1050) {
        await page.mouse.up({ button: "left" });
      }
    }
  },

  "05_sintetizador_fm": {
    dir: "05-sintetizador-fm",
    opusStep: [8.3333, 2],
    argonStep: [8.3333, 2],
    captureAudio: {
      flash: { file: "reto05_opus.wav", t0: 3.0, dur: 12.0 },
      argon: { file: "reto05_argon.wav", t0: 3.0, dur: 10.5 }
    },
    act: async (page, model, f) => {
      const keys = ["z", "x", "c", "v", "b", "n", "m", "q", "w", "e", "r", "t", "y", "u"];
      // Start sequencer at f=5
      if (f === 5) {
        if (model === "flash") await clickId(page, "btnPlay");
        else await clickId(page, "playBtn");
      }
      // Trigger live polyphonic notes every 24 frames synced to the visual keyboard
      if (f % 24 === 4) {
        const k1 = keys[(f / 24 | 0) % keys.length];
        const k2 = keys[((f / 24 | 0) + 4) % keys.length];
        await page.keyboard.down(k1);
        await page.keyboard.down(k2);
      } else if (f % 24 === 16) {
        const k1 = keys[(f / 24 | 0) % keys.length];
        const k2 = keys[((f / 24 | 0) + 4) % keys.length];
        await page.keyboard.up(k1);
        await page.keyboard.up(k2);
      }
      // Switch visualizer / demo songs at exact frames inside the showcase windows
      if (f === 360) {
        if (model === "flash") {
          await clickBtnText(page, "GONIÓMETRO");
          await page.evaluate(() => { if (window.FM16 && window.FM16.loadSong) window.FM16.loadSong(1); });
        } else {
          await clickBtnText(page, "2. 8-Bit Boss Battle");
        }
      } else if (f === 540) {
        if (model === "flash") {
          await clickBtnText(page, "ESPECTROGRAMA");
          await page.evaluate(() => { if (window.FM16 && window.FM16.loadSong) window.FM16.loadSong(2); });
        } else {
          await clickBtnText(page, "3. Acid Techno Lab");
        }
      } else if (f === 740) {
        if (model === "flash") {
          await clickBtnText(page, "DUAL");
        } else {
          await clickBtnText(page, "1. Cyberpunk Outrun");
          await clickId(page, "randomBtn");
        }
      }
      // Move cursor across matrix/knobs
      if (f % 6 === 0) {
        const a = f * 0.04;
        await page.mouse.move(960 + Math.cos(a) * 340, 540 + Math.sin(a * 1.3) * 220);
      }
    }
  },

  "06_pinball_ccd": {
    dir: "06-pinball-ccd",
    opusStep: [8.3333, 2],
    argonStep: [8.3333, 2],
    captureAudio: {
      flash: { file: "reto06_opus.wav", t0: 2.0, dur: 9.0 },
      argon: { file: "reto06_argon.wav", t0: 4.0, dur: 10.5 }
    },
    act: async (page, model, f) => {
      // Unlock audio at f=2
      if (f === 2) {
        await page.mouse.click(500, 500);
      }
      // Phase 1 (0..6s, f 0..360): Pull plunger & launch ball, active flipper action
      if (f === 10) {
        await page.keyboard.down("Space");
      } else if (f === 65) {
        await page.keyboard.up("Space");
      }
      // Trigger Multiball in both Opus and Argon so bumper/slingshot collisions are nonstop!
      if (f === 150) {
        if (model === "argon") {
          await clickId(page, "btnMultiball");
        } else {
          await page.evaluate(() => {
            if (window.__pinball) {
              window.__pinball.G.multiball = true;
              window.__pinball.G.autoQueue = 2;
              window.__pinball.G.autoDelay = 0.15;
              const b = window.__pinball.spawnBall(280, 260, true);
              if (b) { b.vx = 240; b.vy = -380; b.passedGate = true; }
            }
          });
        }
      }
      if (f === 265 && model === "argon") {
        // Right inside reto06-04b (starts at f=240 = 4.0s): fire Multiball 3X!
        await clickId(page, "btnMultiball");
      }
      // Keep balls actively bouncing in the upper/mid playfield if they ever drain during showcase
      if (f >= 180 && f <= 840 && f % 90 === 0) {
        if (model === "flash") {
          await page.evaluate(() => {
            if (window.__pinball && window.__pinball.balls().length < 2) {
              const b = window.__pinball.spawnBall(290, 250, true);
              if (b) { b.vx = -220; b.vy = -340; b.passedGate = true; }
            }
          });
        } else {
          await page.evaluate(() => {
            // If fewer than 2 balls active in Argon, click btnMultiball
            const btn = document.getElementById("btnMultiball");
            if (btn) btn.click();
          });
        }
      }
      // Periodic left/right flipper actuation
      if (f > 80 && f % 42 === 0) {
        await page.keyboard.down("ArrowLeft");
        if (model === "flash") await page.mouse.move(480, 960);
      } else if (f > 80 && f % 42 === 12) {
        await page.keyboard.up("ArrowLeft");
      }
      if (f > 80 && f % 50 === 20) {
        await page.keyboard.down("ArrowRight");
        if (model === "flash") await page.mouse.move(760, 960);
      } else if (f > 80 && f % 50 === 32) {
        await page.keyboard.up("ArrowRight");
      }
      // Phase 2 (6..12s, f 360..720): Turn ON Physics CCD Debug Mode (vectors, normals, spatial grid)
      if (f === 365) {
        if (model === "flash") await clickId(page, "bDebug");
        else await clickId(page, "btnDebug");
      }
      // Relaunch plunger if ball in lane
      if (f === 480) {
        await page.keyboard.down("Space");
      } else if (f === 525) {
        await page.keyboard.up("Space");
      }
      // Phase 3 (12..18s, f 720..1080): Turn OFF Debug Mode + Multiball / Nudge finale
      if (f === 730) {
        if (model === "flash") await clickId(page, "bDebug");
        else {
          await clickId(page, "btnDebug");
          await clickId(page, "btnMultiball");
        }
      }
      if (f === 850) {
        await page.keyboard.press("ArrowUp");
      }
    }
  }
};

function writeWavSliceFloat32Stereo(filePath, leftArr, rightArr, sr, t0Sec, durSec, targetPeak = 0.78) {
  const i0 = Math.max(0, Math.round(t0Sec * sr));
  const n = Math.round(durSec * sr);
  const L = new Float32Array(n);
  const R = new Float32Array(n);
  let mx = 0;
  for (let i = 0; i < n; i++) {
    const srcIdx = i0 + i;
    const lv = srcIdx < leftArr.length ? leftArr[srcIdx] : 0;
    const rv = srcIdx < rightArr.length ? rightArr[srcIdx] : 0;
    L[i] = lv;
    R[i] = rv;
    const a = Math.max(Math.abs(lv), Math.abs(rv));
    if (a > mx) mx = a;
  }
  const scale = mx > 1e-6 ? targetPeak / mx : 1.0;
  const fadeIn = Math.round(0.03 * sr);
  const fadeOut = Math.round(0.05 * sr);
  for (let i = 0; i < n; i++) {
    let env = scale;
    if (i < fadeIn) env *= i / fadeIn;
    else if (i >= n - fadeOut) env *= (n - 1 - i) / fadeOut;
    L[i] = Math.max(-1, Math.min(1, L[i] * env));
    R[i] = Math.max(-1, Math.min(1, R[i] * env));
  }

  const numChannels = 2;
  const bytesPerSample = 4;
  const blockAlign = numChannels * bytesPerSample;
  const byteRate = sr * blockAlign;
  const dataSize = n * blockAlign;
  const buf = Buffer.alloc(44 + dataSize);

  buf.write("RIFF", 0);
  buf.writeUInt32LE(36 + dataSize, 4);
  buf.write("WAVE", 8);
  buf.write("fmt ", 12);
  buf.writeUInt32LE(16, 16);
  buf.writeUInt16LE(3, 20); // IEEE float
  buf.writeUInt16LE(numChannels, 22);
  buf.writeUInt32LE(sr, 24);
  buf.writeUInt32LE(byteRate, 28);
  buf.writeUInt16LE(blockAlign, 32);
  buf.writeUInt16LE(32, 34);
  buf.write("data", 36);
  buf.writeUInt32LE(dataSize, 40);

  let offset = 44;
  for (let i = 0; i < n; i++) {
    buf.writeFloatLE(L[i], offset);
    buf.writeFloatLE(R[i], offset + 4);
    offset += 8;
  }
  fs.writeFileSync(filePath, buf);
  console.log(`[audio] ${path.basename(filePath)}: sliced [${t0Sec.toFixed(2)}s..${(t0Sec + durSec).toFixed(2)}s] (${durSec.toFixed(2)}s @ ${sr}Hz, rawPeak=${mx.toFixed(3)})`);
}

async function setupPage(browser, url, stepCfg, useOfflineAudio = false) {
  const context = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
  await context.addInitScript(({ enableAudio, totalFrames, fps, sr }) => {
    let virtualNow = 1000.0;
    let rafQueue = [];
    let rafId = 1;
    let timers = [];
    let timerId = 1;

    window.performance.now = () => virtualNow;
    Date.now = () => Math.floor(1700000000000 + virtualNow);
    window.requestAnimationFrame = (cb) => {
      const id = rafId++;
      rafQueue.push({ id, cb });
      return id;
    };
    window.cancelAnimationFrame = (id) => {
      rafQueue = rafQueue.filter(item => item.id !== id);
    };

    if (enableAudio) {
      window.setTimeout = (fn, delay = 0, ...args) => {
        const id = timerId++;
        timers.push({ id, fn, time: virtualNow + Math.max(0, Number(delay) || 0), interval: null, args });
        return id;
      };
      window.clearTimeout = (id) => {
        timers = timers.filter(t => t.id !== id);
      };
      window.setInterval = (fn, delay = 10, ...args) => {
        const id = timerId++;
        const d = Math.max(1, Number(delay) || 10);
        timers.push({ id, fn, time: virtualNow + d, interval: d, args });
        return id;
      };
      window.clearInterval = window.clearTimeout;

      const OrigOffline = window.OfflineAudioContext || window.webkitOfflineAudioContext;
      const totalSamples = Math.ceil((totalFrames / fps + 0.5) * sr);
      const offlineCtx = new OrigOffline(2, totalSamples, sr);
      const realResume = offlineCtx.resume.bind(offlineCtx);
      const realSuspend = offlineCtx.suspend.bind(offlineCtx);
      Object.defineProperty(offlineCtx, "state", { get: () => "running" });
      offlineCtx.resume = () => Promise.resolve();
      window.__offlineCtx = offlineCtx;
      window.__realOfflineResume = realResume;
      window.__realOfflineSuspend = realSuspend;
      window.__suspendWaiters = {};
      window.__audioStarted = false;

      window.AudioContext = window.webkitAudioContext = function () {
        return offlineCtx;
      };

      window.__startOfflineAudio = () => {
        if (window.__audioStarted) return;
        window.__audioStarted = true;
        for (let k = 1; k <= totalFrames; k++) {
          const tSusp = k / fps;
          window.__suspendWaiters[k] = new Promise((resolve) => {
            realSuspend(tSusp).then(resolve).catch(resolve);
          });
        }
        window.__renderPromise = offlineCtx.startRendering();
      };
    }

    function runTimers() {
      if (!enableAudio) return;
      let safety = 0;
      while (safety++ < 200) {
        timers.sort((a, b) => a.time - b.time);
        const next = timers[0];
        if (!next || next.time > virtualNow) break;
        if (next.interval !== null) {
          next.time += next.interval;
        } else {
          timers.shift();
        }
        try { next.fn(...(next.args || [])); } catch (e) {}
      }
    }

    window.__stepFrame = async (dtMs = 8.333333, substeps = 2, fNext = null) => {
      for (let s = 0; s < substeps; s++) {
        virtualNow += dtMs;
        runTimers();
        const batch = rafQueue;
        rafQueue = [];
        for (const item of batch) {
          try { item.cb(virtualNow); } catch (e) {}
        }
        // Advance OfflineAudioContext right after substep 0 so substep 1 draws updated AnalyserNode!
        if (enableAudio && s === 0 && fNext !== null && window.__audioStarted) {
          const w = window.__suspendWaiters[fNext];
          if (w) {
            if (fNext > 1) window.__realOfflineResume();
            await w;
          }
        }
      }
    };

    window.__harvestOfflineAudio = async () => {
      if (!enableAudio || !window.__audioStarted) return null;
      window.__realOfflineResume();
      const rendered = await window.__renderPromise;
      const L = Array.from(rendered.getChannelData(0));
      const R = Array.from(rendered.getChannelData(1));
      return { sr: rendered.sampleRate, L, R };
    };

    window.addEventListener("DOMContentLoaded", () => {
      const cur = document.createElement("div");
      cur.id = "__rec_cursor";
      cur.style.cssText = "position:fixed;left:-100px;top:-100px;width:22px;height:22px;margin:-11px 0 0 -11px;border:2.5px solid #38BDF8;border-radius:50%;pointer-events:none;z-index:2147483647;box-shadow:0 0 12px rgba(56,189,248,0.85), inset 0 0 6px rgba(56,189,248,0.5);transition:transform 0.06s ease, border-color 0.06s ease;";
      document.body.appendChild(cur);
      window.addEventListener("mousemove", (e) => {
        cur.style.left = e.clientX + "px";
        cur.style.top = e.clientY + "px";
      }, { passive: true });
      window.addEventListener("mousedown", () => {
        cur.style.transform = "scale(0.72)";
        cur.style.borderColor = "#FBBF24";
        cur.style.background = "rgba(251,191,36,0.28)";
      }, { passive: true });
      window.addEventListener("mouseup", () => {
        cur.style.transform = "scale(1.0)";
        cur.style.borderColor = "#38BDF8";
        cur.style.background = "transparent";
      }, { passive: true });
    });
  }, { enableAudio: useOfflineAudio, totalFrames: FRAMES_PER_MODEL, fps: FPS, sr: AUDIO_SR });

  const page = await context.newPage();
  await page.goto(url, { waitUntil: "load", timeout: 30000 });
  // Warm up virtual frames before starting the f=0..1079 recording
  const warmMult = useOfflineAudio ? 2 : 30;
  await page.evaluate(([dt, sub, wm]) => window.__stepFrame(dt, sub * wm, null), [stepCfg[0], stepCfg[1], warmMult]);
  if (useOfflineAudio) {
    await page.evaluate(() => window.__startOfflineAudio());
  }
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
      { t0: 0.0, t1: 6.0, model: "flash", desc: "Claude Opus 5.5 - Fase 1: Interacción inicial y física en vivo", interest: 5, motion: "high" },
      { t0: 6.0, t1: 12.0, model: "flash", desc: "Claude Opus 5.5 - Fase 2: Herramientas avanzadas, modos de visualización y estrés", interest: 5, motion: "high" },
      { t0: 12.0, t1: 18.0, model: "flash", desc: "Claude Opus 5.5 - Fase 3: Presets secundarios y prueba límite", interest: 5, motion: "high" },
      { t0: 18.0, t1: 24.0, model: "argon", desc: "Gemini 4 Argon - Fase 1: Interacción inicial y física a 120 FPS", interest: 5, motion: "high" },
      { t0: 24.0, t1: 30.0, model: "argon", desc: "Gemini 4 Argon - Fase 2: Modos avanzados, shaders y telemetría", interest: 5, motion: "high" },
      { t0: 30.0, t1: 36.0, model: "argon", desc: "Gemini 4 Argon - Fase 3: Explosión / prueba de estrés final", interest: 5, motion: "high" }
    ],
    highlights: [
      { t0: 0.5, t1: 6.0, model: "flash", use: "hero", why: "Fase 1 interactiva de Claude Opus 5.5", roi: [0, 0, 1920, 1080] },
      { t0: 6.0, t1: 12.0, model: "flash", use: "detail", why: "Fase 2 de herramientas y modos en Claude Opus 5.5", roi: [0, 0, 1920, 1080] },
      { t0: 12.0, t1: 17.5, model: "flash", use: "action", why: "Fase 3 de prueba de estrés en Claude Opus 5.5", roi: [0, 0, 1920, 1080] },
      { t0: 18.5, t1: 24.0, model: "argon", use: "hero", why: "Fase 1 interactiva de Gemini 4 Argon", roi: [0, 0, 1920, 1080] },
      { t0: 24.0, t1: 30.0, model: "argon", use: "detail", why: "Fase 2 de modos y shaders en Gemini 4 Argon", roi: [0, 0, 1920, 1080] },
      { t0: 30.0, t1: 35.5, model: "argon", use: "action", why: "Fase 3 de estrés final en Gemini 4 Argon", roi: [0, 0, 1920, 1080] }
    ],
    split_pairs: [
      { flash: [0.5, 6.0], argon: [18.5, 24.0], why: "Comparativa directa de la Fase 1 interactiva entre Opus 5.5 y Argon 4." },
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
  const useAudio = Boolean(cfg.captureAudio);
  console.log(`[start] ${slug} -> ${movPath} (offlineAudio=${useAudio})`);

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

  // 1) Record Claude Opus 5.5 (0..18s = 1080 frames)
  const opusUrl = `${BASE_URL}/claude-opus-5.5/${cfg.dir}/index.html`;
  const opus = await setupPage(browser, opusUrl, cfg.opusStep, useAudio);
  for (let f = 0; f < FRAMES_PER_MODEL; f++) {
    await cfg.act(opus.page, "flash", f);
    await opus.page.evaluate(([dt, sub, fn]) => window.__stepFrame(dt, sub, fn), [cfg.opusStep[0], cfg.opusStep[1], f + 1]);
    const buf = await opus.page.screenshot({ type: "jpeg", quality: 92 });
    ff.stdin.write(buf);
  }
  if (useAudio && cfg.captureAudio.flash) {
    const audioRes = await opus.page.evaluate(() => window.__harvestOfflineAudio());
    if (audioRes) {
      const spec = cfg.captureAudio.flash;
      writeWavSliceFloat32Stereo(path.join(AUDIO_OUT_DIR, spec.file), audioRes.L, audioRes.R, audioRes.sr, spec.t0, spec.dur);
    }
  }
  await opus.context.close();

  // 2) Record Gemini 4 Argon (18..36s = 1080 frames)
  const argonUrl = `${BASE_URL}/gemini-4-argon/${cfg.dir}/index.html`;
  const argon = await setupPage(browser, argonUrl, cfg.argonStep, useAudio);
  for (let f = 0; f < FRAMES_PER_MODEL; f++) {
    await cfg.act(argon.page, "argon", f);
    await argon.page.evaluate(([dt, sub, fn]) => window.__stepFrame(dt, sub, fn), [cfg.argonStep[0], cfg.argonStep[1], f + 1]);
    const buf = await argon.page.screenshot({ type: "jpeg", quality: 92 });
    ff.stdin.write(buf);
  }
  if (useAudio && cfg.captureAudio.argon) {
    const audioRes = await argon.page.evaluate(() => window.__harvestOfflineAudio());
    if (audioRes) {
      const spec = cfg.captureAudio.argon;
      writeWavSliceFloat32Stereo(path.join(AUDIO_OUT_DIR, spec.file), audioRes.L, audioRes.R, audioRes.sr, spec.t0, spec.dur);
    }
  }
  await argon.context.close();

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
  const entries = Object.entries(CHOREO).filter(([k]) => !filters.length || filters.some(f => k.includes(f)));
  // Run in batches of 3 challenges in parallel so GPU WebGL stays super fast
  for (let i = 0; i < entries.length; i += 3) {
    const batch = entries.slice(i, i + 3);
    console.log(`=== Starting batch ${i / 3 + 1}: ${batch.map(b => b[0]).join(", ")} ===`);
    await Promise.all(batch.map(([slug, cfg]) => recordChallenge(slug, cfg)));
  }
  srv.close();
  console.log("=== ALL COMPARATIVE 60FPS MOVIES + FRAME-LOCKED AUDIO + SHOTLOGS READY ===");
})();
