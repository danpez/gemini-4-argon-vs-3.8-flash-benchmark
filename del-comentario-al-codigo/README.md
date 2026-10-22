# MIXIUH LABS — NUEVA SECCION: "DEL COMENTARIO AL CODIGO"

**Lema Oficial:** *"Tu lanzas la hipotesis en los comentarios. Nosotros la programamos desde cero en el laboratorio."*
**Identificador de Serie:** `DEL COMENTARIO AL CODIGO // LABORATORIO ABIERTO`
**Formatos Nativos por Episodio:**
1. **Video Respuesta Vertical (`9:16` · `2160x3840 4K @ 60fps` y `1080x1920 @ 60fps`):** Diseñado para responder directamente con video al comentario original en Instagram Reels, TikTok y YouTube Shorts (duracion objetivo: `45 a 58 segundos`).
2. **Episodio Demostrativo Horizontal (`16:9` · `3840x2160 4K @ 60fps`):** Version extendida para el canal principal de YouTube (`2:30 a 4:00 minutos`) mostrando la arquitectura matematica, las pruebas en vivo y el codigo descargable/interactivo.

---

## 1. ESENCIA Y REGLAS DE LA SECCION

Esta seccion convierte a la audiencia de **Mixiuh Labs** en co-directores del laboratorio sin perder el rigor tecnico del canal:

1. **Evidencia Real del Comentario:** Todo episodio abre en el segundo `00:00` mostrando en pantalla la captura real del comentario del seguidor (usuario, texto integro y contexto del video donde comento).
2. **Evolucion sobre Codigo del Laboratorio:** Tomamos el motor fisico, shader o algoritmo del episodio donde nacio la duda y construimos la evolucion que pidio el usuario.
3. **Regla Zero-Asset Intacta:** Prohibido usar plantillas de Photoshop, imagenes `.png/.jpg` descargadas o librerias prefabricadas. Si un seguidor pide una marca de ropa o un mockup, la prenda, el tejido de algodon, la iluminacion de estudio y el plano CAD se generan 100% con codigo y matematicas a `120 FPS`.
4. **Doble CTA Estrategico (Bucle Viral de Comentarios + Trafico a YouTube):**
   - **CTA de Participacion (Comunidad):** *"Dejame aqui abajo en los comentarios que locura quieres que llevemos del comentario al codigo en el proximo video; elegire el mejor comentario para programarlo y responderte en video."*
   - **CTA de Conversion (Embudo a YouTube y Web):** *"El video completo en 4K explicando paso a paso como lo construimos y el enlace para probar el estudio en vivo ya estan en el canal de YouTube de Mixiuh Labs."*

---

## 2. INDICE DE EPISODIOS

| # | Codigo | Seguidor / Origen | Reto Planteado en Comentarios | Proyecto Construido | Estado |
| :-: | :--- | :--- | :--- | :--- | :---: |
| **01** | `ep01-marca-ropa-verlet` | `@tenito03` *(IG Reel #01 EP02 — Tela Fisica Verlet)* | *"Si ahora con esa textura le pides hacer una playera y tambien le pides que te de un mockup en blanco para editarlo ahora puedes crear una marca de ropa ?"* | **Verlet Couture Studio 3D:** Motor de tela Verlet acoplado a playera boxy 3D a 120 FPS + Estudio de Mockup en Blanco 300 GSM editable (pecho/espalda/sublimado) + Generador de Tech Pack CAD con medidas en centimetros y vitrina de marca | **COMPLETADO (4K60 YT + 4K60 Reel/Short)** |

---

## 3. ESTRUCTURA DE ARCHIVOS DE CADA EPISODIO

```text
del-comentario-al-codigo/
├── README.md
└── ep01-marca-ropa-verlet/
    ├── comentario-original/
    │   └── comentario_tenito03_ig.jpg
    ├── app/
    │   └── index.html                        # Estudio interactivo 100% autocontenido (120 FPS)
    ├── guion/
    │   └── GUION_OFICIAL_YT_Y_REELS.md       # Guiones completos (Vertical 9:16 + Horizontal 16:9 + CTAs)
    ├── grabaciones/
    │   ├── record_verlet_couture.js          # Grabador determinista a 60 FPS en Playwright
    │   └── verlet_couture_studio_60fps.mov   # Metraje maestro interactivo
    ├── entregables_finales_4k/
    │   ├── del-comentario-al-codigo-01-marca-ropa-verlet_2160p60.mp4   # Master YouTube 16:9 4K60
    │   ├── captions_es.srt / captions_es.vtt                           # Subtitulos CC sincronizados
    │   ├── youtube.md / youtube.json                                   # Metadatos completos de YouTube
    │   ├── thumbnails/                                                 # Miniaturas 16:9 (A/B/C) con el comentario
    │   └── shorts/
    │       ├── 01_respuesta-tenito03-marca-ropa-verlet_4k60.mp4        # Video Respuesta 9:16 4K (2160x3840 @ 60fps)
    │       └── 01_respuesta-tenito03-marca-ropa-verlet_1080p60.mp4     # Video Respuesta 9:16 (1080x1920 @ 60fps)
    └── programacion/
        ├── 00_INDICE_EJECUTIVO.md
        ├── 01_YOUTUBE.md
        ├── 02_INSTAGRAM_REEL_RESPUESTA.md
        ├── 03_TIKTOK.md
        └── 04_TEXTO_RESPUESTA_COMENTARIO_IG.md
```
