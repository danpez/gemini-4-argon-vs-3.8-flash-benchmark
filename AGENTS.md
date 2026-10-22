# Reglas Obligatorias de Produccion Audiovisual — Mixiuh Labs

Estas reglas definen el **estandar minimo obligatorio** para todos los episodios, Shorts, Reels y TikToks de Mixiuh Labs (`@MixiuhLabs` / `@labs.mixiuh` / `labs.mixiuh.online`), tanto en Espanol como en Ingles.

## 1. Resolucion, Formato y Bilinguismo
- **Resolucion obligatoria**:
  - Videos horizontales maestros (YouTube): **4K UHD (`3840x2160` @ 60 fps)**.
  - Videos verticales (Shorts / Reels / TikTok): **4K Vertical (`2160x3840` @ 60 fps)** escalado con `lanczos + cas=0.35` a partir del render nativo a 60 fps.
  - Miniaturas independientes de Shorts (`miniaturas_4k` / `thumbnails_4k`): **PNG 4K (`2160x3840`)** exportadas en el segundo `0.85s` de cada Short para poder seleccionarlas como portada en Instagram Reels, TikTok y YouTube Shorts.
- **Bilinguismo**: Todo episodio y lote de Shorts debe generarse completo en **Espanol (`es`)** e **Ingles (`en`)**.
- **Cero emojis**: Prohibido usar emojis Unicode en textos graficos, codigo o subtítulos; todos los iconos (reloj, moneda, corazon, seguir, guardar, compartir, play) deben dibujarse con geometria vectorial o sprites pixel-art en Skia.

## 2. Estandar Minimo para el Gancho / Portada de cada Short (`0.0s .. 1.5s`, `short_hook` + `short_panels`)
Nunca usar portadas genericas que solo digan `"MISMO PROMPT / ¿QUIEN LO HIZO MEJOR?"`. Cada Short debe diferenciarse visualmente desde el cuadro `0.0s` con:
1. **Placa superior de identificacion del capitulo y reto**:
   - Kicker con numero de episodio y numero de prueba (`EP.XX · PRUEBA 0X/06 · MISMO PROMPT.` / `EP.XX · CHALLENGE 0X/06 · SAME PROMPT.`).
   - **Titulo gigante en pixel-art 3D especifico de la prueba** (ej. `FLUIDOS GPU GLSL`, `PINBALL CYBERPUNK`) + subtitulo tecnico (`NAVIER-STOKES + VORTICES · 1 INTENTO`).
   - **Color de acento neon unico por prueba** (ej. `#22D3EE`, `#10B981`, `#F472B6`, `#FBBF24`, `#FB923C`, `#A78BFA`) para distinguir cada miniatura en la cuadricula del perfil de Instagram/TikTok/YouTube.
2. **Identificadores completos dentro del panel de cada IA desde el segundo `0.0`**:
   - **Chip central con el logo/sprite y nombre del modelo** (`OPUS 5.5`, `ARGON`, etc.).
   - **Pildora izquierda con icono de reloj y tiempo de entrega (`XX MIN`)**.
   - **Pildora derecha con icono de moneda y costo real de API (`$X.XX USD`)**.
   - En el gancho (`is_hook=True`), los chips del panel superior van en su borde superior y los del panel inferior en su borde inferior simetrico, dejando el centro libre para la placa `¿QUIEN LO HIZO MEJOR?` flanqueada por los sprites de las IAs.

## 3. Estandar Minimo para la Tarjeta de Veredicto (`short_verdict`)
Cuando se menciona el resultado, tiempo y costo al final del reto, la pantalla de veredicto debe incluir como minimo:
1. **Pildora superior con identificador de episodio, numero de prueba y nombre del reto** con su color de acento.
2. **Marcador global acumulado del episodio** (`OPUS 5.5 [X] - [Y] ARGON`) ubicado en la parte superior (`cy = 372`) con animacion de giro de digito para no chocar nunca con los subtitulos de la costura (`y = 970`).
3. **Sprite del modelo ganador con corona + titular 3D (`PUNTO PARA X`)**.
4. **Tarjeta de motivo tecnico (`Headline + Reason`)** explicando en una linea clara por que gano esa IA (rendimiento, arquitectura, tiempo y costo).
5. **Dashboard de telemetria en 3 bloques debajo de la costura (`y >= 1050`)**:
   - **Bloque 1 — Tiempo de Entrega (`MIN`)**: Barras comparativas animadas + badge de velocidad relativa (`X.XX MAS RAPIDO`).
   - **Bloque 2 — Costo Real API (`$ USD`) y Consumo de Tokens (`TOK`)**: Barras comparativas animadas + badge de porcentaje de ahorro (`-XX% COSTO`).
   - **Bloque 3 — Tarjetas lado a lado de Rendimiento y Codigo**: Comparativa directa de `FPS` y `LINEAS DE CODIGO` / arquitectura de ambos modelos.

## 4. Estandar Minimo para la Pantalla Final de Cierre (`short_endtag`)
Donde aparece `"VIDEO COMPLETO EN MIXIUH LABS"`, la pantalla final (`>= 2.4s`) debe incluir siempre disparadores visuales inconscientes de accion:
1. **Encabezado superior diferenciador**: Episodio, numero y nombre de la prueba + marcador global actualizado.
2. **Sprite Mixiuh + Titular `VIDEO COMPLETO EN MIXIUH LABS`**.
3. **Tarjeta flotante del Canal de YouTube (`MIXIUH LABS`)**: Con boton Play rojo y boton interactivo animado que pasa de `SUSCRIBETE` (`#FF0033`) a `SUSCRITO` (`#10B981`) con pulso de clic y destello.
4. **4 tarjetas flotantes de accion social con iconos vectoriales y animacion pop escalonada**:
   - `DALE LIKE` (`+1 APOYO` / corazon vectorial)
   - `SIGUENOS` (`MIXIUH LABS` / icono usuario + mas)
   - `GUARDALO` (`PARA DESPUES` / icono marcador)
   - `COMPARTE` (`CON UN DEV` / icono avion de papel)
5. **Tarjeta flotante del laboratorio web interactivo (`labs.mixiuh.online`)**: Invitando a probar las demos en vivo, prompts y metricas en el navegador.
