#!/usr/bin/env node
/**
 * Audits all completed EP03 HTML applications in headless Chrome (1920x1080),
 * records console errors, page errors, measured FPS, and saves full 1920x1080 PNG screenshots.
 */

const { chromium } = require("playwright");
const http = require("http");
const fs = require("fs");
const path = require("path");

const ROOT_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/ep03-superpowers-kit";
const SCREENSHOTS_DIR = path.join(ROOT_DIR, "benchmark/screenshots");
fs.mkdirSync(SCREENSHOTS_DIR, { recursive: true });

const CHALLENGES = [
  { slug: "01_galaxia_nbody", dir: "01-galaxia-nbody" },
  { slug: "02_terminal_trading", dir: "02-terminal-trading" },
  { slug: "03_arcade_boss_rush", dir: "03-arcade-boss-rush" },
  { slug: "04_red_zero_trust", dir: "04-red-zero-trust" },
  { slug: "05_motor_nodos_ia", dir: "05-motor-nodos-ia" },
  { slug: "06_mixiuh_os_desktop", dir: "06-mixiuh-os-desktop" }
];

const MODES = [
  { key: "raw", folder: "ia-sin-kit" },
  { key: "superkit", folder: "ia-superpowers-kit" }
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
    for (const m of MODES) {
      const htmlPath = path.join(ROOT_DIR, m.folder, ch.dir, "index.html");
      if (!fs.existsSync(htmlPath) || fs.statSync(htmlPath).size < 1000) {
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
        // Measure live RAF framerate over 1 second
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

  fs.writeFileSync(path.join(ROOT_DIR, "benchmark/audit_report_ep03.json"), JSON.stringify(auditReport, null, 2));
  await browser.close();
  srv.close();
})();
