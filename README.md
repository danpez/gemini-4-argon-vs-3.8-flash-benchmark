# Mixiuh Labs — Repositorio Oficial de Benchmarks, Codigo Zero-Shot y Kits de Ingenieria

Portal interactivo en vivo: **[https://labs.mixiuh.online](https://labs.mixiuh.online)**

Este repositorio contiene el codigo fuente original (`index.html`), las auditorias de telemetria (reloj, tokens de entrada/salida/cache y costo real en USD), los kits descargables y la programacion omnicanal de todos los episodios de **Mixiuh Labs** (`@MixiuhLabs`).

---

## Indice de Episodios y Series en este Repositorio

| Serie / Episodio | Carpeta en el Repositorio | Enfrentamiento / Proyecto | Marcador / Resultado | Tiempo Acumulado | Costo API Real |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Episodio 03** | [`ep03-superpowers-kit/`](./ep03-superpowers-kit/) | **Gemini 4 Argon High Sin Kit vs. Mixiuh Superpowers Kit v1.0** (`6 Retos · 12 Corridas agy CLI`) | **SuperKit `4 - 2` Sin Kit** | `276 min` vs `302 min` | `$10.85` vs `$7.69 USD` |
| **Del Comentario al Codigo #01** | [`del-comentario-al-codigo/ep01-marca-ropa-verlet/`](./del-comentario-al-codigo/ep01-marca-ropa-verlet/) | **Reto de `@tenito03` -> OVERFIT Studio 3D (`Coleccion Guerra de Pesos`)** | **3 Maniquies 300 GSM + 10 Artes 2K** | Estudio 3D en Vivo | Exportacion 4K |
| **Episodio 02** | [`ep02-argon-vs-opus/`](./ep02-argon-vs-opus/) | **Gemini 4 Argon (High) vs. Claude Opus 5.5 (High)** (`6 Motores Fisicos, WebGL2 y FM`) | **Argon `4 - 2` Opus 5.5** | `90 min` vs `159 min` | `$6.26` vs `$16.26 USD` |
| **Episodio 01** | [`ep01-argon-vs-flash/`](./ep01-argon-vs-flash/) | **Gemini 4 Argon (High) vs. Gemini 3.8 Flash (High)** (`10 Retos Zero-Shot + Medio Pixel`) | **Argon `10 - 0` Flash** | `55 min` vs `94 min` | `10/10` vs `8/10` func. |

---

## 1. Episodio 03 — Gemini 4 Argon High Sin Kit vs. Mixiuh Superpowers Kit v1.0 (`ep03-superpowers-kit/`)

12 corridas reales y aisladas ejecutadas mediante `agy --model gemini-4-argon-high --effort high` para responder con datos duros: **¿Siguen siendo necesarios los Kits de Skills, bancos de memoria y el Auto-Debugger MCP hoy?**

- **Codigo de las 6 entregas Sin Kit (Raw):** [`ep03-superpowers-kit/ia-sin-kit/`](./ep03-superpowers-kit/ia-sin-kit/)
- **Codigo de las 6 entregas Con Superpowers Kit:** [`ep03-superpowers-kit/ia-superpowers-kit/`](./ep03-superpowers-kit/ia-superpowers-kit/)
- **Kit descargable gratuito (`AGENTS.md` + 5 Skills + `MEMORY_BANK.md`):** [`ep03-superpowers-kit/regalo-superpowers-kit/`](./ep03-superpowers-kit/regalo-superpowers-kit/)
- **Telemetria completa y comparativas lado a lado:** [`ep03-superpowers-kit/benchmark/`](./ep03-superpowers-kit/benchmark/)

| # | Reto | IA Sin Kit (`Argon High Raw`) | IA + Mixiuh Superpowers Kit | Ganador |
| :-: | :--- | :--- | :--- | :-: |
| **01** | **Colision Galactica N-Body 3D** | `42 min` · `$0.88` · `275k tok` (16k sin Bloom) | `46 min` · `$1.61` · `506k tok` (20k GPU + Bloom HDR + Lente Einstein) | **SuperKit (1-0)** |
| **02** | **Terminal de Trading HFT Zero-GC** | `58 min` · `$1.60` · `471k tok` (`11,073 ord/s`) | `42 min` · `$1.40` · `400k tok` (`70,406 ord/s` en `Float64Array`) | **SuperKit (2-0)** |
| **03** | **Arcade Bullet-Hell Boss Rush** | `51 min` · `$1.09` · `381k tok` (`1,829 proyectiles` a 60 FPS) | `69 min` · `$2.32` · `769k tok` (`432 proyectiles`) | **Sin Kit (2-1)** |
| **04** | **Red Ciber-Defensa Zero-Trust 3D** | `48 min` · `$0.74` · `249k tok` (resuelto en `5 pasos`) | `30 min` · `$2.04` · `699k tok` (`21 pasos`) | **Sin Kit (2-2)** |
| **05** | **Motor de Nodos IA + Shaders GLSL (DAG)** | `43 min` · `$1.41` · `513k tok` | `33 min` · `$1.41` · `523k tok` (`10 min mas rapido` + PiP Raymarching 3D) | **SuperKit (3-2)** |
| **06** | **Sistema Operativo Web MixiuhOS** | `60 min` · `$1.97` · `761k tok` (ventanas iniciales solapadas) | `56 min` · `$2.07` · `627k tok` (4 apps limpias verificadas por MCP) | **SuperKit (4-2)** |

---

## 2. Del Comentario al Codigo #01 — OVERFIT Studio 3D (`del-comentario-al-codigo/ep01-marca-ropa-verlet/`)

A partir del comentario de `@tenito03` en el Reel de la tela fisica de Verlet, construimos **OVERFIT Studio 3D** con 3 siluetas de 300 GSM en Blender Cycles (Hombre, Mujer y Mesa) y los 10 artes satiricos en 2K de la coleccion **"Guerra de Pesos"**:
- **Aplicacion interactiva:** [`del-comentario-al-codigo/ep01-marca-ropa-verlet/app/index.html`](./del-comentario-al-codigo/ep01-marca-ropa-verlet/app/index.html)
- **Guion oficial:** [`del-comentario-al-codigo/ep01-marca-ropa-verlet/guion/GUION_OFICIAL_YT_Y_REELS.md`](./del-comentario-al-codigo/ep01-marca-ropa-verlet/guion/GUION_OFICIAL_YT_Y_REELS.md)

---

## 3. Episodio 02 — Gemini 4 Argon vs. Claude Opus 5.5 (`ep02-argon-vs-opus/`)

- **Entregas de Claude Opus 5.5 (`High`):** [`ep02-argon-vs-opus/claude-opus-5.5/`](./ep02-argon-vs-opus/claude-opus-5.5/)
- **Entregas de Gemini 4 Argon (`High`):** [`ep02-argon-vs-opus/gemini-4-argon/`](./ep02-argon-vs-opus/gemini-4-argon/)
- **Telemetria de tokens y costos:** [`ep02-argon-vs-opus/benchmark/benchmark_results.json`](./ep02-argon-vs-opus/benchmark/benchmark_results.json)

---

## 4. Episodio 01 — Gemini 4 Argon vs. Gemini 3.8 Flash (`ep01-argon-vs-flash/`)

- **Entregas de Gemini 4 Argon (`High`):** [`ep01-argon-vs-flash/gemini-4-argon/`](./ep01-argon-vs-flash/gemini-4-argon/)
- **Entregas de Gemini 3.8 Flash (`High`):** [`ep01-argon-vs-flash/gemini-3.8-flash/`](./ep01-argon-vs-flash/gemini-3.8-flash/)
- **Prompts y notas originales:** [`ep01-argon-vs-flash/2026-10-13-laboratorio-comparativo-gemini-3.8-flash-vs-4-argon.md`](./ep01-argon-vs-flash/2026-10-13-laboratorio-comparativo-gemini-3.8-flash-vs-4-argon.md)
