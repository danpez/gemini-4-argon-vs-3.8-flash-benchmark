#!/usr/bin/env node
/**
 * Records the dedicated 16:9 YouTube master (verlet_couture_yt_60fps.mov, 150s @ 60fps)
 * where every single stage, silhouette, and each of the 10 "Guerra de Pesos" designs (OVF-01 .. OVF-10)
 * has its own isolated, full-duration time window matching the narrator's voiceover in episode.yaml,
 * so no shot ever bleeds into another design.
 */
const { chromium } = require('/Users/kevingonzalezlopez/Work/Mixiuh/keruvin-store/node_modules/playwright');
const { spawn } = require('child_process');
const path = require('path');

const APP_URL = 'file://' + path.resolve(__dirname, '../app/index.html');
const OUT_MOV = path.resolve(__dirname, 'verlet_couture_yt_60fps.mov');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    deviceScaleFactor: 1
  });
  const page = await context.newPage();

  const errors = [];
  page.on('pageerror', err => errors.push(err.message));

  await page.goto(APP_URL, { waitUntil: 'networkidle' });
  await page.waitForFunction(() => window.MANNEQUINS_READY === true && window.OVERFIT_READY === true, { timeout: 15000 });
  await page.waitForTimeout(300);

  const client = await context.newCDPSession(page);

  const ff = spawn('/opt/homebrew/bin/ffmpeg', [
    '-y', '-hide_banner', '-loglevel', 'error',
    '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '60', '-i', '-',
    '-c:v', 'prores_ks', '-profile:v', '2', '-pix_fmt', 'yuv422p10le',
    OUT_MOV
  ]);

  let lastBuf = null;
  client.on('Page.screencastFrame', async ({ data, sessionId }) => {
    lastBuf = Buffer.from(data, 'base64');
    client.send('Page.screencastFrameAck', { sessionId }).catch(() => {});
  });

  await client.send('Page.startScreencast', {
    format: 'jpeg',
    quality: 96,
    maxWidth: 1920,
    maxHeight: 1080,
    everyNthFrame: 1
  });

  const FPS = 60;
  const TOTAL_SEC = 150;
  const TOTAL_FRAMES = FPS * TOTAL_SEC;

  const actions = {
    // =========================================================================
    // 0.0s .. 4.0s (Frames 0 .. 240): Blank 300 GSM Male White (Boxy Oversize)
    // =========================================================================
    2: async () => {
      await page.evaluate(() => {
        setStudioStep(1);
        selectBodyModel('male');
        selectGarmentColor('white');
        selectArtwork('none');
        setPlacement('center');
        setViewLayout('single');
        setRotationAngle(0);
        setCameraZoom(1.0);
        impulseClothWave();
      });
    },
    185: async () => {
      await page.evaluate(() => {
        setRotationAngle(0);
        setCameraZoom(1.85);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 4.0s .. 8.0s (Frames 240 .. 480): Blank 300 GSM Female Street Fit (Cream)
    // =========================================================================
    240: async () => {
      await page.evaluate(() => {
        selectBodyModel('female');
        selectGarmentColor('cream');
        selectArtwork('none');
        setViewLayout('single');
        setRotationAngle(0);
        setCameraZoom(1.0);
        impulseClothWave();
      });
    },
    390: async () => {
      await page.evaluate(() => {
        setRotationAngle(0);
        setCameraZoom(1.85);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 8.0s .. 12.0s (Frames 480 .. 720): Blank 300 GSM Flat-Lay Table (White)
    // =========================================================================
    480: async () => {
      await page.evaluate(() => {
        selectBodyModel('flat');
        selectGarmentColor('white');
        selectArtwork('none');
        setViewLayout('single');
        setRotationAngle(0);
        setCameraZoom(1.0);
        impulseClothWave();
      });
    },
    600: async () => {
      await page.evaluate(() => {
        setCameraZoom(1.85);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 12.0s .. 16.0s (Frames 720 .. 960): Blank 300 GSM Color Swatches & Dual Blank
    // =========================================================================
    720: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('white');
        selectArtwork('none');
        setViewLayout('single');
        setRotationAngle(0);
        setCameraZoom(1.0);
        impulseClothWave();
      });
    },
    785: async () => {
      await page.evaluate(() => {
        selectGarmentColor('cream');
        impulseClothWave();
      });
    },
    850: async () => {
      await page.evaluate(() => {
        selectGarmentColor('black');
        setViewLayout('dual');
        impulseClothWave();
      });
    },

    // =========================================================================
    // 16.0s .. 24.0s (Frames 960 .. 1440): Collection Overview ("Guerra de Pesos")
    // =========================================================================
    960: async () => {
      await page.evaluate(() => {
        setStudioStep(2);
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('01_strawberry');
        setViewLayout('dual');
        impulseClothWave();
      });
    },
    1140: async () => {
      await page.evaluate(() => {
        selectGarmentColor('cream');
        selectArtwork('02_vibecoding');
        setViewLayout('frontback');
        impulseClothWave();
      });
    },
    1300: async () => {
      await page.evaluate(() => {
        selectGarmentColor('emerald');
        selectArtwork('05_opensource');
        setViewLayout('dual');
        impulseClothWave();
      });
    },

    // =========================================================================
    // 24.0s .. 34.0s (Frames 1440 .. 2040, 10.0s): DESIGN #01 — Contador de Fresas
    // =========================================================================
    1440: async () => {
      await page.evaluate(() => {
        setStudioStep(2);
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('01_strawberry');
        setViewLayout('chest');
        setRotationAngle(0);
        impulseClothWave();
      });
    },
    1728: async () => {
      // 28.8s: 260% Macro HD on Design #01 chest
      await page.evaluate(() => {
        setRotationAngle(0);
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },
    1890: async () => {
      // 31.5s: 2K HD Modal on Design #01
      await page.evaluate(() => {
        openArtModal();
      });
    },
    2010: async () => {
      // 33.5s: Close modal, stay on Design #01 260% Macro
      await page.evaluate(() => {
        closeArtModal();
      });
    },

    // =========================================================================
    // 34.0s .. 40.0s (Frames 2040 .. 2400, 6.0s): DESIGN #02 — Vibe Coding en Produccion
    // =========================================================================
    2040: async () => {
      await page.evaluate(() => {
        closeArtModal();
        selectBodyModel('male');
        selectGarmentColor('cream');
        setPlacement('center');
        selectArtwork('02_vibecoding');
        setViewLayout('chest');
        setRotationAngle(0);
        impulseClothWave();
      });
    },
    2172: async () => {
      // 36.2s: 260% Macro HD on Design #02 chest
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 40.0s .. 47.0s (Frames 2400 .. 2820, 7.0s): DESIGN #03 — Club CUDA Poor
    // =========================================================================
    2400: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('cobalt');
        setPlacement('center');
        selectArtwork('03_cudapoor');
        setViewLayout('chest');
        setRotationAngle(0);
        impulseClothWave();
      });
    },
    2568: async () => {
      // 42.8s: 260% Macro HD on Design #03 chest
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 47.0s .. 53.0s (Frames 2820 .. 3180, 6.0s): DESIGN #04 — La Gran Estafa del Benchmark
    // =========================================================================
    2820: async () => {
      await page.evaluate(() => {
        selectBodyModel('female');
        selectGarmentColor('white');
        setPlacement('center');
        selectArtwork('04_benchmark');
        setViewLayout('chest');
        setRotationAngle(0);
        impulseClothWave();
      });
    },
    2964: async () => {
      // 49.4s: 260% Macro HD on Design #04 chest
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 53.0s .. 59.5s (Frames 3180 .. 3570, 6.5s): DESIGN #05 — Open Source Mafia
    // =========================================================================
    3180: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('emerald');
        setPlacement('center');
        selectArtwork('05_opensource');
        setViewLayout('chest');
        setRotationAngle(0);
        impulseClothWave();
      });
    },
    3330: async () => {
      // 55.5s: 260% Macro HD on Design #05 chest
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 59.5s .. 65.0s (Frames 3570 .. 3900, 5.5s): DESIGN #06 — Censura Estetica
    // =========================================================================
    3570: async () => {
      await page.evaluate(() => {
        selectBodyModel('female');
        selectGarmentColor('crimson');
        setPlacement('center');
        selectArtwork('06_censura');
        setViewLayout('chest');
        setRotationAngle(0);
        impulseClothWave();
      });
    },
    3696: async () => {
      // 61.6s: 260% Macro HD on Design #06 chest
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 65.0s .. 73.0s (Frames 3900 .. 4380, 8.0s): DESIGN #07 — Tabla Nutricional LLM (Espalda)
    // =========================================================================
    3900: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('07_nutrition');
        setViewLayout('back');
        setCameraZoom(1.85);
        impulseClothWave();
      });
    },
    4092: async () => {
      // 68.2s: 255% Macro HD on Design #07 Back
      await page.evaluate(() => {
        setCameraZoom(2.55);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 73.0s .. 77.5s (Frames 4380 .. 4650, 4.5s): DESIGN #08 — Hoy No Hay AGI, Manana Si
    // =========================================================================
    4380: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('cream');
        setPlacement('center');
        selectArtwork('08_agi_manana');
        setViewLayout('chest');
        setRotationAngle(0);
        impulseClothWave();
      });
    },
    4488: async () => {
      // 74.8s: 260% Macro HD on Design #08 chest
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 77.5s .. 83.0s (Frames 4650 .. 4980, 5.5s): DESIGN #09 — Evolucion del Desarrollador
    // =========================================================================
    4650: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('white');
        setPlacement('center');
        selectArtwork('09_dev_evolution');
        setViewLayout('chest');
        setRotationAngle(0);
        impulseClothWave();
      });
    },
    4788: async () => {
      // 79.8s: 260% Macro HD on Design #09 chest
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 83.0s .. 90.0s (Frames 4980 .. 5400, 7.0s): DESIGN #10 — Dilema del Tranvia de los Tokens
    // =========================================================================
    4980: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('10_trolley_tokens');
        setViewLayout('chest');
        setRotationAngle(0);
        impulseClothWave();
      });
    },
    5148: async () => {
      // 85.8s: 260% Macro HD on Design #10 chest
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 90.0s .. 96.5s (Frames 5400 .. 5790, 6.5s): Stage 3 Placements (Pocket -> Center -> Oversize -> Full)
    // =========================================================================
    5400: async () => {
      await page.evaluate(() => {
        setStudioStep(3);
        selectBodyModel('male');
        selectGarmentColor('black');
        selectArtwork('01_strawberry');
        setViewLayout('single');
        setPlacement('pocket');
        impulseClothWave();
      });
    },
    5496: async () => {
      await page.evaluate(() => {
        setPlacement('center');
        impulseClothWave();
      });
    },
    5592: async () => {
      await page.evaluate(() => {
        setPlacement('oversize');
        impulseClothWave();
      });
    },
    5688: async () => {
      await page.evaluate(() => {
        setPlacement('allover');
        impulseClothWave();
      });
    },

    // =========================================================================
    // 96.5s .. 104.5s (Frames 5790 .. 6270, 8.0s): Stage 3 Sliders (Scale, Y-Pos, Fold Depth)
    // =========================================================================
    5790: async () => {
      await page.evaluate(() => {
        setPlacement('center');
        selectGarmentColor('black');
        selectArtwork('01_strawberry');
        setViewLayout('chest');
        impulseClothWave();
      });
    },

    // =========================================================================
    // 104.5s .. 111.0s (Frames 6270 .. 6660, 6.5s): Stage 3 Ink Finishes (Plastisol -> Vintage -> Puff)
    // =========================================================================
    6270: async () => {
      await page.evaluate(() => {
        selectGarmentColor('black');
        selectArtwork('01_strawberry');
        setInkFinish('plastisol');
        setViewLayout('chest');
        setCameraZoom(2.1);
        impulseClothWave();
      });
    },
    6400: async () => {
      await page.evaluate(() => {
        selectGarmentColor('cream');
        selectArtwork('02_vibecoding');
        setInkFinish('vintage');
        setCameraZoom(2.1);
        impulseClothWave();
      });
    },
    6530: async () => {
      await page.evaluate(() => {
        selectGarmentColor('cobalt');
        selectArtwork('03_cudapoor');
        setInkFinish('puff');
        setCameraZoom(2.1);
        impulseClothWave();
      });
    },

    // =========================================================================
    // 111.0s .. 115.5s (Frames 6660 .. 6930, 4.5s): Stage 3 Brand Presets & Price
    // =========================================================================
    6660: async () => {
      await page.evaluate(() => {
        setInkFinish('plastisol');
        selectGarmentColor('black');
        selectArtwork('01_strawberry');
        setViewLayout('single');
        selectBrandPreset(1); // CUDA POOR CLUB
        cyclePrice();
      });
    },
    6750: async () => {
      await page.evaluate(() => {
        selectBrandPreset(2); // PURO SESGO LABS
        cyclePrice();
      });
    },
    6840: async () => {
      await page.evaluate(() => {
        selectBrandPreset(0); // OVERFIT BY MIXIUH
        cyclePrice();
      });
    },

    // =========================================================================
    // 115.5s .. 125.5s (Frames 6930 .. 7530, 10.0s): Stage 3 Front + Back View (frontback)
    // =========================================================================
    6930: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('02_vibecoding');
        setViewLayout('frontback');
        impulseClothWave();
      });
    },
    7230: async () => {
      await page.evaluate(() => {
        selectGarmentColor('cream');
        selectArtwork('01_strawberry');
        setViewLayout('frontback');
        impulseClothWave();
      });
    },

    // =========================================================================
    // 125.5s .. 130.0s (Frames 7530 .. 7800, 4.5s): Stage 3 Dual Male + Female View (dual)
    // =========================================================================
    7530: async () => {
      await page.evaluate(() => {
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('05_opensource');
        setViewLayout('dual');
        impulseClothWave();
      });
    },
    7665: async () => {
      await page.evaluate(() => {
        selectGarmentColor('white');
        selectArtwork('04_benchmark');
        setViewLayout('dual');
        impulseClothWave();
      });
    },

    // =========================================================================
    // 130.0s .. 140.5s (Frames 7800 .. 8430, 10.5s): Export 1 — 9:16 Instagram Story/Reel (igreel)
    // =========================================================================
    7800: async () => {
      await page.evaluate(() => {
        setStudioStep(4);
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('01_strawberry');
        setSocialFormat('igreel');
      });
    },
    8115: async () => {
      await page.evaluate(() => {
        selectBodyModel('female');
        selectGarmentColor('cream');
        selectArtwork('02_vibecoding');
        setSocialFormat('igreel');
      });
    },

    // =========================================================================
    // 140.5s .. 144.5s (Frames 8430 .. 8670, 4.0s): Export 2 — Dual Catalog Lookbook (catalog)
    // =========================================================================
    8430: async () => {
      await page.evaluate(() => {
        selectGarmentColor('black');
        selectArtwork('10_trolley_tokens');
        setSocialFormat('catalog');
      });
    },

    // =========================================================================
    // 144.5s .. 150.0s (Frames 8670 .. 9000, 5.5s): Export 3 — 4K Transparent PNG Mockup (blank)
    // =========================================================================
    8670: async () => {
      await page.evaluate(() => {
        selectGarmentColor('white');
        selectArtwork('08_agi_manana');
        setSocialFormat('blank');
      });
    },
    8835: async () => {
      await page.evaluate(() => {
        selectGarmentColor('black');
        selectArtwork('01_strawberry');
        setSocialFormat('blank');
        triggerExportPack();
      });
    }
  };

  for (let f = 0; f < TOTAL_FRAMES; f++) {
    if (actions[f]) {
      await actions[f]();
    }
    // Smooth 3D rotation on Blank Male (f = 50 .. 175)
    if (f >= 50 && f <= 175) {
      const prog = (f - 50) / 125.0;
      const deg = Math.round(Math.sin(prog * Math.PI * 2) * 28);
      await page.evaluate((d) => setRotationAngle(d), deg);
    }
    // Smooth 3D rotation on Blank Female (f = 280 .. 380)
    else if (f >= 280 && f <= 380) {
      const prog = (f - 280) / 100.0;
      const deg = Math.round(Math.sin(prog * Math.PI * 2) * 24);
      await page.evaluate((d) => setRotationAngle(d), deg);
    }
    // Smooth slider animation during Stage 3 Sliders segment (f = 5795 .. 6260)
    else if (f >= 5795 && f <= 6260) {
      const prog = (f - 5795) / 465.0;
      const scVal = Math.round(105 + Math.sin(prog * Math.PI * 4) * 18);
      const pyVal = Math.round(Math.cos(prog * Math.PI * 4) * 12);
      const flVal = Math.round(100 + Math.sin(prog * Math.PI * 2) * 35);
      await page.evaluate(({ s, p, fl }) => {
        const slS = document.getElementById('sliderScale');
        const slP = document.getElementById('sliderPosY');
        const slF = document.getElementById('sliderWarp');
        if (slS) slS.value = s;
        if (slP) slP.value = p;
        if (slF) slF.value = fl;
        setLogoScale(s);
        setLogoPosY(p);
        setWarpStrength(fl);
      }, { s: scVal, p: pyVal, fl: flVal });
    }
    if (lastBuf) {
      ff.stdin.write(lastBuf);
    }
    await page.waitForTimeout(1000 / FPS);
  }

  await client.send('Page.stopScreencast');
  ff.stdin.end();
  await new Promise(res => ff.on('close', res));
  await browser.close();

  console.log('Recorded YT Master:', OUT_MOV, 'Errors:', errors.length);
  if (errors.length) console.error(errors);
})();
