#!/usr/bin/env node
/**
 * Audits all 18 completed EP04 HTML applications (Haiku 5.5, Sonnet 5.5, Opus 5.5)
 * in headless Chrome (1920x1080), records console errors, page errors, measured FPS,
 * and saves full 1920x1080 PNG screenshots.
 */

const { chromium } = require("playwright");
const http = require("http");
const fs = require("fs");
const path = require("path");

const ROOT_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep04-escalera-claude";
const SCREENSHOTS_DIR = path.join(ROOT_DIR, "benchmark/screenshots");
fs.mkdirSync(SCREENSHOTS_DIR, { recursive: true });

const CHALLENGES = [
  { slug: "01_rover_suspension", dir: "01-rover-suspension" },
  { slug: "02_slime_feromonas", dir: "02-slime-feromonas" },
  { slug: "03_puente_estructural", dir: "03-puente-estructural" },
  { slug: "04_sintetizador_acido_3d", dir: "04-sintetizador-acido-3d" },
  { slug: "05_pathtracer_bvh", dir: "05-pathtracer-bvh" },
  { slug: "06_consola_retro_cpu", dir: "06-consola-retro-cpu" }
];

const MODELS = [
  { key: "haiku", folder: "claude-haiku-5.5" },
  { key: "sonnet", folder: "claude-sonnet-5.5" },
  { key: "opus", folder: "claude-opus-5.5" }
];

function startServer() {
  const mime = {
    ".html": "text/html; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".json": "application/json"
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
    srv.listen(0, "127.0.0.1", () => resolve({ srv, port: srv.address().port }));
  });
}

(async () => {
  const { srv, port } = await startServer();
  const baseUrl = `http://127.0.0.1:${port}`;
  const browser = await chromium.launch({
    channel: "chrome",
    headless: true,
    args: ["--use-gl=angle", "--enable-webgl", "--ignore-gpu-blocklist", "--autoplay-policy=no-user-gesture-required"]
  });

  const auditReport = {};

  for (const ch of CHALLENGES) {
    auditReport[ch.dir] = {};
    for (const m of MODELS) {
      const htmlPath = path.join(ROOT_DIR, m.folder, ch.dir, "index.html");
      if (!fs.existsSync(htmlPath) || fs.statSync(htmlPath).size < 500) {
        console.log(`[SKIP] ${ch.dir} (${m.key}) not ready yet`);
        continue;
      }
      const context = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
      const page = await context.newPage();
      const consoleErrors = [];
      const pageErrors = [];
      page.on("console", (msg) => {
        if (msg.type() === "error") consoleErrors.push(msg.text());
      });
      page.on("pageerror", (err) => {
        pageErrors.push(String(err));
      });

      const url = `${baseUrl}/${m.folder}/${ch.dir}/index.html`;
      try {
        await page.goto(url, { waitUntil: "load", timeout: 25000 });
        await page.waitForTimeout(2500);
        const fps = await page.evaluate(() => new Promise((resolve) => {
          let frames = 0;
          const t0 = performance.now();
          function tick() {
            frames++;
            const dt = performance.now() - t0;
            if (dt >= 900) resolve(Math.round((frames * 1000) / dt));
            else requestAnimationFrame(tick);
          }
          requestAnimationFrame(tick);
        }));
        const outPng = path.join(SCREENSHOTS_DIR, `${ch.slug}_${m.key}.png`);
        await page.screenshot({ path: outPng, type: "png" });
        const info = await page.evaluate(() => ({
          title: document.title,
          canvases: document.querySelectorAll("canvas").length,
          buttons: document.querySelectorAll("button").length,
          inputs: document.querySelectorAll("input, select").length
        }));
        auditReport[ch.dir][m.key] = {
          fps,
          consoleErrors,
          pageErrors,
          ...info,
          screenshot: outPng
        };
        console.log(`[OK] ${ch.dir} (${m.key}): FPS=${fps} | canvases=${info.canvases} | btns=${info.buttons} | inputs=${info.inputs} | errs=${consoleErrors.length + pageErrors.length}`);
        if (consoleErrors.length || pageErrors.length) {
          console.log(`     Errors:`, [...consoleErrors, ...pageErrors].slice(0, 3));
        }
      } catch (e) {
        console.log(`[ERR] ${ch.dir} (${m.key}):`, e.message);
      }
      await context.close();
    }
  }

  fs.writeFileSync(path.join(ROOT_DIR, "benchmark/audit_report_ep04.json"), JSON.stringify(auditReport, null, 2));
  await browser.close();
  srv.close();
})();
