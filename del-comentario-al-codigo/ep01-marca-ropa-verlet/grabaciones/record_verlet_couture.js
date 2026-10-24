#!/usr/bin/env node
/**
 * Records the upgraded OVERFIT by Mixiuh Labs 3D Mockup Studio (app/index.html) at 1920x1080 @ 60fps
 * showcasing:
 * - Direct 2K UHD (1792x2400) chest & back prints rendered onto the Retina canvas with zero pixelation
 * - 360° interactive turntable rotation (0° Front <-> 180° Back with OVF-07 LLM Nutrition Facts)
 * - Macro HD Zoom (185% Detalle & 260% Macro) + 2K Artwork Inspection Modal
 * - All 10 "Guerra de Pesos" satirical AI/Programming designs (OVF-01 .. OVF-10) in crisp close-up
 * - Social & Store exports (Instagram Reel 9:16, Dual Catalog, Transparent 4K PNG)
 */
const { chromium } = require('/Users/kevingonzalezlopez/Work/Mixiuh/keruvin-store/node_modules/playwright');
const { spawn } = require('child_process');
const path = require('path');

const APP_URL = 'file://' + path.resolve(__dirname, '../app/index.html');
const OUT_MOV = path.resolve(__dirname, 'verlet_couture_studio_60fps.mov');

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
  const TOTAL_SEC = 54;
  const TOTAL_FRAMES = FPS * TOTAL_SEC;

  const actions = {
    // 0.0s .. 6.0s: Blank 300 GSM Mockup (Frente -> Giro 360° -> Mujer -> Flat-Lay -> Hombre+Mujer)
    5: async () => {
      await page.evaluate(() => {
        setStudioStep(1);
        selectBodyModel('male');
        selectGarmentColor('white');
        selectArtwork('none');
        setPlacement('center');
        setViewLayout('single');
      });
    },
    55: async () => {
      await page.screenshot({ path: path.resolve(__dirname, 'shot_01_blank_mockup.png') });
    },
    85: async () => {
      await page.evaluate(() => {
        setViewLayout('back');
        impulseClothWave();
      });
    },
    155: async () => {
      await page.evaluate(() => {
        selectBodyModel('female');
        selectGarmentColor('cream');
        setViewLayout('single');
        impulseClothWave();
      });
    },
    225: async () => {
      await page.evaluate(() => {
        selectBodyModel('flat');
        selectGarmentColor('white');
        setViewLayout('single');
        impulseClothWave();
      });
    },
    295: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('black');
        setViewLayout('dual');
      });
    },

    // 6.0s .. 26.0s: All 10 OVERFIT ("Guerra de Pesos") Designs in 185% Chest Detail + 260% Macro 2K Zoom!
    // #01 Contador de Fresas (6.0s: 185% Detalle -> 6.8s: 260% Macro HD)
    360: async () => {
      await page.evaluate(() => {
        setStudioStep(2);
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('01_strawberry');
        setViewLayout('chest');
        impulseClothWave();
      });
    },
    405: async () => {
      await page.screenshot({ path: path.resolve(__dirname, 'shot_02_overfit_01_strawberry.png') });
    },
    410: async () => {
      await page.evaluate(() => {
        setCameraZoom(2.6);
      });
    },

    // #02 Vibe Coding en Produccion (8.0s: 185% Detalle -> 8.8s: 260% Macro HD)
    480: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('cream');
        setPlacement('center');
        selectArtwork('02_vibecoding');
        setViewLayout('chest');
      });
    },
    520: async () => {
      await page.screenshot({ path: path.resolve(__dirname, 'shot_03_overfit_02_vibecoding.png') });
    },
    528: async () => {
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // #03 Club de los GPU Pobres (10.0s: 185% Detalle Cobalto -> 10.8s: 260% Macro HD)
    600: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('cobalt');
        setPlacement('center');
        selectArtwork('03_cudapoor');
        setViewLayout('chest');
        impulseClothWave();
      });
    },
    648: async () => {
      await page.evaluate(() => {
        setCameraZoom(2.6);
      });
    },

    // #04 La Gran Estafa del Benchmark (12.0s: Mujer 185% Detalle -> 12.8s: 260% Macro HD)
    720: async () => {
      await page.evaluate(() => {
        selectBodyModel('female');
        selectGarmentColor('white');
        setPlacement('center');
        selectArtwork('04_benchmark');
        setViewLayout('chest');
      });
    },
    768: async () => {
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // #05 Pelea de Callejon: Open Source Mafia (14.0s: Bosque 185% Detalle -> 14.8s: 260% Macro HD)
    840: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('emerald');
        setPlacement('center');
        selectArtwork('05_opensource');
        setViewLayout('chest');
        impulseClothWave();
      });
    },
    880: async () => {
      await page.screenshot({ path: path.resolve(__dirname, 'shot_04_overfit_05_opensource.png') });
    },
    888: async () => {
      await page.evaluate(() => {
        setCameraZoom(2.6);
      });
    },

    // #06 Censura Estetica (16.0s: Mujer Burdeos 185% Detalle -> 16.8s: 260% Macro HD)
    960: async () => {
      await page.evaluate(() => {
        selectBodyModel('female');
        selectGarmentColor('crimson');
        setPlacement('center');
        selectArtwork('06_censura');
        setViewLayout('chest');
      });
    },
    1008: async () => {
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // #07 Etiqueta Nutricional del Modelo (18.0s: Vista Espalda 185% -> 18.8s: 260% Macro Espalda)
    1080: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('07_nutrition');
        setViewLayout('back');
        setCameraZoom(1.85);
      });
    },
    1128: async () => {
      await page.evaluate(() => {
        setCameraZoom(2.5);
        impulseClothWave();
      });
    },

    // #08 Hoy No Hay AGI, Manana Si (20.0s: Crema 185% Detalle -> 20.8s: 260% Macro HD)
    1200: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('cream');
        setPlacement('center');
        selectArtwork('08_agi_manana');
        setViewLayout('chest');
        impulseClothWave();
      });
    },
    1248: async () => {
      await page.evaluate(() => {
        setCameraZoom(2.6);
      });
    },

    // #09 Prompt Engineer vs Ingeniero de Verdad (22.0s: Blanco 185% Detalle -> 22.8s: 260% Macro HD)
    1320: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('white');
        setPlacement('center');
        selectArtwork('09_dev_evolution');
        setViewLayout('chest');
      });
    },
    1368: async () => {
      await page.evaluate(() => {
        setCameraZoom(2.6);
        impulseClothWave();
      });
    },

    // #10 El Dilema del Tranvia de los Tokens (24.0s: Negro 185% Detalle -> 24.8s: 260% Macro HD)
    1440: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('10_trolley_tokens');
        setViewLayout('chest');
        impulseClothWave();
      });
    },
    1480: async () => {
      await page.screenshot({ path: path.resolve(__dirname, 'shot_05_overfit_10_trolley.png') });
    },
    1488: async () => {
      await page.evaluate(() => {
        setCameraZoom(2.6);
      });
    },

    // 26.0s .. 36.0s: Deep Customization, 2K Modal & 360° Turntable Rotation
    1560: async () => {
      await page.evaluate(() => {
        setStudioStep(3);
        selectBodyModel('male');
        selectGarmentColor('black');
        selectArtwork('01_strawberry');
        setViewLayout('single');
        setPlacement('pocket');
      });
    },
    1615: async () => {
      await page.evaluate(() => {
        setPlacement('center');
        setViewLayout('chest');
      });
    },
    1665: async () => {
      await page.evaluate(() => {
        openArtModal();
      });
    },
    1720: async () => {
      await page.evaluate(() => {
        closeArtModal();
        setPlacement('oversize');
        setViewLayout('single');
        impulseClothWave();
      });
    },
    1765: async () => {
      await page.evaluate(() => {
        setPlacement('center');
        selectGarmentColor('cream');
        selectArtwork('02_vibecoding');
        selectBrandPreset(1); // CUDA POOR CLUB
        setInkFinish('vintage');
        setViewLayout('chest');
      });
    },
    1890: async () => {
      await page.evaluate(() => {
        selectBrandPreset(2); // PURO SESGO LABS
        setInkFinish('puff');
        setViewLayout('single');
        cyclePrice();
      });
    },
    2015: async () => {
      await page.evaluate(() => {
        selectBrandPreset(0); // OVERFIT BY MIXIUH
        setInkFinish('plastisol');
        setLogoScale(105);
        setLogoPosY(0);
        setRotationAngle(180);
        setCameraZoom(1.85);
        impulseClothWave();
      });
    },

    // 36.0s .. 40.0s: Front + Back View (Front #02 Vibe Coding + Back #07 Tabla Nutricional LLM)
    2160: async () => {
      await page.evaluate(() => {
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('02_vibecoding');
        setViewLayout('frontback');
      });
    },
    2220: async () => {
      await page.screenshot({ path: path.resolve(__dirname, 'shot_06_front_back_nutrition.png') });
    },
    2280: async () => {
      await page.evaluate(() => {
        selectGarmentColor('cream');
        selectArtwork('01_strawberry');
        setViewLayout('frontback');
        impulseClothWave();
      });
    },

    // 40.0s .. 44.0s: Dual Male + Female 3D Silhouette Comparison
    2400: async () => {
      await page.evaluate(() => {
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('05_opensource');
        setViewLayout('dual');
      });
    },
    2460: async () => {
      await page.screenshot({ path: path.resolve(__dirname, 'shot_07_dual_male_female.png') });
    },
    2520: async () => {
      await page.evaluate(() => {
        selectGarmentColor('white');
        selectArtwork('04_benchmark');
        setViewLayout('dual');
        impulseClothWave();
      });
    },

    // 44.0s .. 54.0s: Social & Store Exports (Instagram Reel 9:16, Catalog, Blank PNG, Download Toast)
    2640: async () => {
      await page.evaluate(() => {
        setStudioStep(4);
        selectBodyModel('male');
        selectGarmentColor('black');
        setPlacement('center');
        selectArtwork('01_strawberry');
        setSocialFormat('igreel');
      });
    },
    2720: async () => {
      await page.screenshot({ path: path.resolve(__dirname, 'shot_08_ig_reel_overfit.png') });
    },
    2760: async () => {
      await page.evaluate(() => {
        selectBodyModel('female');
        selectGarmentColor('cream');
        selectArtwork('02_vibecoding');
        setSocialFormat('igreel');
      });
    },
    2850: async () => {
      await page.evaluate(() => {
        selectGarmentColor('black');
        selectArtwork('10_trolley_tokens');
        setSocialFormat('catalog');
      });
    },
    2920: async () => {
      await page.screenshot({ path: path.resolve(__dirname, 'shot_09_catalog_overfit.png') });
    },
    3030: async () => {
      await page.evaluate(() => {
        selectGarmentColor('white');
        selectArtwork('08_agi_manana');
        setSocialFormat('blank');
      });
    },
    3120: async () => {
      await page.evaluate(() => {
        selectGarmentColor('black');
        selectArtwork('01_strawberry');
        setSocialFormat('igreel');
        triggerExportPack();
      });
    }
  };

  for (let f = 0; f < TOTAL_FRAMES; f++) {
    if (actions[f]) {
      await actions[f]();
    }
    // Smooth 360° turntable rotation & slider animation during customization segment (f = 1890 .. 2010)
    if (f >= 1765 && f < 1890) {
      const prog = (f - 1765) / 125.0;
      const scVal = Math.round(104 + Math.sin(prog * Math.PI * 2) * 12);
      const pyVal = Math.round(Math.cos(prog * Math.PI * 2) * 10);
      await page.evaluate(({ s, p }) => {
        const slS = document.getElementById('sliderScale');
        const slP = document.getElementById('sliderPosY');
        if (slS) slS.value = s;
        if (slP) slP.value = p;
        setLogoScale(s);
        setLogoPosY(p);
      }, { s: scVal, p: pyVal });
    } else if (f >= 1890 && f <= 2010) {
      const prog = (f - 1890) / 120.0;
      const deg = Math.round(Math.sin(prog * Math.PI * 2) * 180);
      await page.evaluate((d) => {
        setRotationAngle(d);
      }, deg);
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

  console.log('Recorded', OUT_MOV, 'Errors:', errors.length);
  if (errors.length) console.error(errors);
})();
