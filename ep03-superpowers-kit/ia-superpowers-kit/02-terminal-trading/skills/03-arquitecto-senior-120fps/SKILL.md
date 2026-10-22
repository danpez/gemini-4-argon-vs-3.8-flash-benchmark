---
name: 03-arquitecto-senior-120fps
description: Metodologia de ingenieria de alto rendimiento para crear aplicaciones, motores fisicos y dashboards a 60-120 FPS sin codigo basura ni cuellos de botella O(N^2).
---

# Skill 03: Arquitecto Senior & Rendimiento Extremo (120 FPS)

## Cuando activar esta habilidad
Activa esta habilidad al diseñar nuevas funcionalidades, simulaciones fisicas, visualizaciones de datos o interfaces interactivas complejas.

## Reglas de Oro de Ingenieria
1. **Prohibicion de Fuerza Bruta $O(N^2)$ en Tiempo Real:**
   - Si el sistema maneja mas de 100 entidades interactivas (particulas, nodos, filas del DOM), utiliza particionamiento espacial (**Spatial Hash Grid** o **Quadtree**) y estructuras de memoria contigua (`Float32Array` / `Int32Array`).
2. **Cero Basura en el Bucle de Renderizado (`requestAnimationFrame`):**
   - Evita instanciar objetos nuevos (`new THREE.Vector3()`, `{x, y}`, `.map()`, `.filter()`) dentro del bucle de 60/120 Hz para evitar pausas del Garbage Collector. Pre-asigna buffers reutilizables.
3. **Fisica Independiente del Framerate (`dt` Clamping):**
   - Limita siempre el paso de tiempo (`const dt = Math.min(rawDt, 0.033)`) y usa sub-pasos (`substeps = 4..8`) para evitar que las colisiones atraviesen paredes (*tunneling*).
4. **Telemetria Visible:**
   - En herramientas tecnicas o simuladores, incluye un HUD limpio con metricas reales en vivo (FPS, tiempo de frame en ms, entidades activas).
