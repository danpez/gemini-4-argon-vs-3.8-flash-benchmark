### 🌐 1. WebGL y 3D (Usando Three.js)

1. **El Sistema Solar Relativo:** Un mini sistema solar en Three.js. El sol debe emitir luz real, la tierra debe tener una textura procedural básica (océanos y tierra), y una luna orbitando la tierra mientras la tierra orbita el sol. *Reto: Jerarquías de rotación y traslación en 3D.*
### Gemini 3.8 Flash High - Antigravity - 7 minutos
### Gemini 4 Argon High - Antigravity - 11 minutos

### NOTAS: 4 Argon gana. Mejores graficos, sin errores, luminicencia del sol configurable, angulo de la luna configurable, fondo mejor diseñado.

Actúa como un Programador Gráfico de Élite y Artista Técnico (Creative Coder) experto en WebGL y Three.js. 

Tu objetivo es superar un benchmark de código "Zero-Shot". Debes escribir un archivo HTML único que contenga HTML, CSS y JavaScript (Three.js) para renderizar un "Mini Sistema Solar Relativo". El código debe ejecutarse a la perfección en el navegador al primer intento, sin errores de consola, sin requerir servidores locales y sin pasos adicionales de compilación.

REGLA DE ORO: ESTÁ ESTRICTAMENTE PROHIBIDO cargar recursos externos (imágenes, texturas .jpg/.png, modelos 3D). Todo lo visual debe generarse mediante código, matemáticas o proceduralmente.

## Requisitos Técnicos Obligatorios:
1. **Entorno y Librerías:** Usa módulos ES (ESM) nativos en el navegador. Utiliza un `<script type="importmap">` apuntando a un CDN confiable (como unpkg o cdnjs) para importar `three` y el addon `OrbitControls`.
2. **Jerarquía Espacial (SceneGraph):** Debes demostrar un dominio perfecto de las agrupaciones (Object3D/Groups).
   - La Tierra debe orbitar alrededor del Sol.
   - La Luna debe orbitar alrededor de la Tierra (y seguirla en su viaje alrededor del Sol).
   - Usa la jerarquía de padres/hijos nativa de Three.js. No hardcodees las posiciones de la luna calculando senos y cosenos basados en el Sol de forma plana; usa la matriz de transformación del Group de la Tierra.
3. **El Sol e Iluminación:** El Sol debe situarse en el centro. No debe verse afectado por las luces (emite luz). Usa un `PointLight` anclado a la posición del Sol para iluminar el resto del sistema.
4. **Textura Procedural (El mayor reto):** Como no puedes usar imágenes, la Tierra debe tener océanos y continentes generados proceduralmente. Puedes lograrlo escribiendo un `ShaderMaterial` personalizado (GLSL con ruido Perlin/Simplex) o generando un `<canvas>` en memoria con ruido fractal bidimensional y pasándolo como un `CanvasTexture` al material de la Tierra. 
5. **Cámara y Controles:** La cámara debe empezar en un ángulo isométrico atractivo. Instancia `OrbitControls` con damping habilitado para que el usuario pueda rotar, hacer zoom y panear suavemente.

## Libertad Creativa y Estética (¡Lúcete!):
No te limites a un diseño sobrio o aburrido. Tienes total libertad albedrío para hacer que esto se vea ESPECTACULAR. 
- Puedes agregar un campo de estrellas tridimensional (`THREE.Points`).
- Puedes añadir post-procesamiento (Bloom) para que el Sol brille de verdad, o simular un resplandor atmosférico alrededor de la Tierra usando shaders o sprites (siempre generado por código).
- Juega con los colores, las velocidades de órbita y los tamaños relativos (no tienen que ser a escala real, deben ser visualmente atractivos).

## Formato de Entrega:
Devuelve ÚNICAMENTE el bloque de código ` ```html ` con el código completo y final. No incluyas explicaciones antes ni después. Tu respuesta debe empezar con `<!DOCTYPE html>` y terminar con `</html>`. Demuestra de lo que eres capaz.

Todo en una carpeta llamada "sistema-solar"


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


2. **Visualizador de ADN de Partículas:** Una cadena de ADN formada por cientos de partículas (esferas) en 3D que rota suavemente. Al pasar el mouse, las partículas deben dispersarse ligeramente y luego volver a su posición original. *Reto: Matemáticas de hélices y física de partículas.*
### Gemini 3.8 Flash High - Antigravity - 7 minutos
### Gemini 4 Argon High - Antigravity - 5 minutos

### NOTAS: Gana Argon en calidad y tiempo, mas personalizacion, cambio de particulas, animaciones, efectos, etc.

Actúa como un Ingeniero Gráfico Senior y Desarrollador Creativo. Tu objetivo es construir un **Visualizador de ADN en 3D Interactivo de alta densidad de partículas**, que cuente con simulación física de fuerzas y un estilo visual cinematográfico/cyberpunk espectacular. Se ejecutará en mi máquina local.

### 1. Libertad Tecnológica y Estética Total
* **Elección de Stack:** No estás limitado únicamente a tecnologías web básicas. Puedes utilizar el entorno que te permita alcanzar la mayor fidelidad visual y rendimiento en tiempo real para simular más de 10,000 partículas activas (por ejemplo, un archivo único HTML5 con **Three.js + Shaders GLSL personalizados + Post-procesado/Bloom**, o una aplicación local en **Python con ModernGL/Pygame**).
* **Estilo Visual (Cero Sobriedad):** Imagina una interfaz sacada de una película de ciencia ficción de bio-tecnología: bioluminiscencia intensa, efecto de brillo acumulado (*Bloom/Glow*), aberración cromática, rastros de movimiento de partículas, sutiles rejillas digitales en el fondo, y un HUD de datos en pantalla estilo cyberpunk con telemetría en tiempo real (FPS, contador de partículas, fuerza de dispersión, velocidad de rotación).
* **Cero Dependencias Externas de Texturas:** **PROHIBIDO** cargar imágenes externas para las partículas o texturas. Las partículas de la cadena de ADN deben generarse proceduralmente (como esferas 3D con Shaders, "point sprites" con gradientes, o a través de buffers de renderizado rápido).

---

### 2. Requerimientos Matemáticos y Físicos (El Núcleo del Reto)
Debes recrear la doble hélice con precisión utilizando matemáticas y un motor de partículas con estado dinámico (fuerzas y restauración):
1. **La Doble Hélice (Matemáticas):** 
   * Calcula los puntos de la hélice dual usando fórmulas paramétricas: 
     $$x_1 = r \cdot \cos(\theta), \quad z_1 = r \cdot \sin(\theta), \quad y_1 = p \cdot \theta$$
     $$x_2 = r \cdot \cos(\theta + \pi), \quad z_2 = r \cdot \sin(\theta + \pi), \quad y_2 = p \cdot \theta$$
     Donde $r$ es el radio y $p$ es el paso de la hélice.
   * La cadena debe componerse de dos hebras principales (miles de partículas estrechamente unidas) y los "peldaños" (enlaces base o pares de bases nitrogenadas) que conectan ambas hebras de manera transversal, interpolando posiciones y cambiando de color según el tipo de base (Adenina, Timina, Citosina, Guanina) en base a un índice procedural.
2. **Sistema de Partículas Dinámico (Fuerza e Inercia):**
   * **Posiciones Objetivo (Base):** Cada una de las miles de partículas debe conocer su posición original/teórica dentro de la hélice de ADN.
   * **Comportamiento del Mouse / Puntero (Raycasting o espacio de pantalla):** Al pasar el cursor, calcula la distancia 3D de cada partícula al cursor. Si está por debajo de un umbral de influencia, aplica una **Fuerza de Dispersión / Repulsión** que empuje la partícula hacia afuera del puntero (por ejemplo, $F \propto 1/d^k$ o una explosión de partículas).
   * **Algoritmo de Retorno (Física de Resortes):** Cada partícula, una vez que el mouse se aleja, debe volver a su posición teórica original aplicando una fuerza de retorno elástico amortiguado (Estilo *Hooke's Law*: $F = -k \cdot \text{distancia} - c \cdot v$). Esto evitará que las partículas vuelvan de forma instantánea o lineal, dándoles un comportamiento de "tejido fluido" o "rebote magnético" orgánico y natural.

---

### 3. Requerimientos Visuales y Controles
1. **Representación de Alta Complejidad Visual:**
   * Bioluminiscencia de colores intensos (Ej: Cyans/Azules para la hebra A, Magentas/Violetas para la hebra B, y combinaciones de verdes, amarillos o naranjas para las uniones base).
   * Haz que la cadena completa rote suavemente de forma autónoma en el espacio tridimensional mientras se ondula sutilmente como una estructura orgánica vibrante.
   * Añade partículas de "ambiente" (polvo de fondo flotando perezosamente en el espacio oscuro) para generar mayor profundidad de campo tridimensional.
2. **Interfaz de Usuario Interactiva (HUD):**
   * Panel de control gráfico o barra lateral interactiva (como `dat.gui` o similar inyectada) para ajustar parámetros en caliente:
     - Escala del efecto de dispersión (fuerza del mouse).
     - Velocidad y elasticidad de retorno de las partículas (`springiness`, `damping`).
     - Velocidad orbital de rotación de la cadena.
     - Densidad de las partículas.
     - Tipo de visualización (Partículas de diferentes formas, modo alambre de uniones base, o rastro de partículas).
3. **Cámara Interactiva:**
   * Soporte para órbita libre, zoom de acercamiento extremo para ver la física a micro-escala y paneo.

---

### 4. Reglas de Entrega
* Entrega el **código completo, íntegro y 100% funcional** en un solo bloque listo para copiar, guardar y ejecutar directamente.
* **Prohibido** usar comentarios de omisión de código (`// ... continuar con el resto`) o dejar algoritmos de física y retorno a medias.
* Incluye al final una breve nota de 2 líneas indicando el comando exacto o la forma de ejecutarlo en mi máquina.

Todo en una carpeta llamada "visualizador-adn"


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### 🎨 2. Generación Procedural y Física (Canvas 2D)

3. **Simulación de "Boids" (Flocking/Parvada):** Una simulación de vida artificial donde cientos de triángulos (pájaros) vuelan juntos siguiendo las 3 reglas clásicas: separación, alineación y cohesión. El mouse debe actuar como un "depredador" que los asusta. *Reto: Algoritmos de comportamiento emergente y vectores.*
### Gemini 3.8 Flash High - Antigravity - 3 minutos
### Gemini 4 Argon High - Antigravity - 5 minutos

### NOTAS: Los resultados fueron muy parecidos, en cuanto a funcionalidad, ambos cumplen, pero la personalizacion y keymaps de Argon le da la victoria

Actúa como un Ingeniero de Simulaciones Físicas y Desarrollador Creativo Senior. Tu objetivo es construir una **Simulación de Vida Artificial y Comportamiento Emergente ("Boids" de Craig Reynolds)** masiva, ultrarrápida y visualmente hipnótica, ejecutada en mi máquina local.

### 1. Libertad Tecnológica y Estética Total
* **Elección de Stack:** Tienes libertad para elegir el entorno que logre el mejor equilibrio entre rendimiento masivo (60 FPS estables con cientos o miles de agentes) y espectacularidad visual (por ejemplo, un archivo único HTML5 con **Canvas 2D avanzado / WebGL**, o una aplicación en **Python con Pygame/ModernGL**).
* **Libertad Creativa (Cero Sobriedad):** No te limites a dibujar triángulos blancos sobre un fondo negro plano. Diseña una experiencia estética de alto impacto: estelas de movimiento dinámicas (*motion trails* con *alpha blending*), bioluminiscencia reactiva donde el color de cada agente cambie según su velocidad, ángulo de dirección o densidad de su parvada local, ondas de choque visuales y un HUD de telemetría científica en tiempo real.
* **Cero Dependencias Externas Rotas:** Todo el motor vectorial, particionamiento espacial, gráficos e interfaz deben ser 100% autocontenidos y generados por código.

---

### 2. Requerimientos Matemáticos y Algorítmicos (El Núcleo del Reto)
Debes programar desde cero un motor de física vectorial autónomo basado en fuerzas de dirección (*Steering Behaviors* de Reynolds):

1. **Cinemática Vectorial por Agente:**
   * Cada *Boid* debe poseer vectores de Posición ($\vec{p}$), Velocidad ($\vec{v}$) y Aceleración ($\vec{a}$), además de límites escalares estrictos para su velocidad máxima (`maxSpeed`) y fuerza máxima de giro (`maxForce`).
   * Toda fuerza de dirección debe calcularse mediante la fórmula clásica de Reynolds:
     $$\vec{F}_{\text{steer}} = \text{limit}(\vec{v}_{\text{desired}} - \vec{v}_{\text{actual}}, \text{maxForce})$$
   * El triángulo o geometría de cada agente debe rotar suavemente alineándose con el ángulo de su vector velocidad ($\theta = \text{atan2}(v_y, v_x)$).

2. **Las 3 Leyes Clásicas de Flocking:**
   * **Separación (Repulsión a corto alcance):** Detectar vecinos dentro de un radio personal $r_s$ y calcular un vector de alejamiento inversamente proporcional a la distancia ($\propto 1/d$ o $1/d^2$) para evitar colisiones superpuestas.
   * **Alineación (Sincronización cinemática):** Calcular la velocidad promedio de los vecinos dentro del radio de percepción $r_a$ y aplicar una fuerza de giro para igualar su rumbo y velocidad.
   * **Cohesión (Atracción al centro de masa):** Calcular el centroide (posición promedio) de los vecinos cercanos dentro de $r_c$ y generar una fuerza de búsqueda (*seek*) hacia ese punto.

3. **Interacción con el Depredador (El Mouse + Amenazas):**
   * El cursor del mouse actúa como un **Depredador Ápex**. Cuando los *Boids* entran en el radio de pánico del cursor, deben activar una fuerza de evasión/huida intensa ($\vec{F}_{\text{flee}}$) que supere a las reglas normales, aumentando temporalmente su `maxSpeed` (efecto adrenalina) y alterando su color para reflejar el estado de alerta.
   * Permite que al hacer clic izquierdo se genere una onda expansiva de repulsión o se coloquen obstáculos físicos que la parvada deba esquivar dinámicamente, y añade la opción de soltar 1 o 2 "Depredadores IA autónomos" que persigan activamente el centro de densidad de las parvadas.

4. **Optimización Espacial Obligatoria (Prohibido $O(N^2)$ puro):**
   * Para soportar entre 600 y 2,000+ agentes sin caídas de FPS, implementa una estructura de particionamiento espacial (**Quadtree** o **Spatial Hash Grid**) para consultar únicamente los vecinos de las celdas adyacentes en lugar de comparar cada agente contra todos los demás.

---

### 3. Requerimientos Visuales, Telemetría y Controles (HUD)
1. **Visualización de Depuración Científica (Toggles en vivo):**
   * Incluye interruptores interactivos en pantalla para renderizar en tiempo real:
     * **La estructura del Quadtree o Spatial Grid** (ver cómo se subdividen las cajas dinámicamente donde hay mayor concentración de agentes).
     * **Vectores de fuerza y radios de percepción** (mostrar flechas de velocidad/fuerza y círculos de visión sobre una muestra de agentes).
     * **Modo Estelas (Trails) / Modo Nítido:** Control del desvanecimiento del lienzo para crear patrones fluidos orgánicos.
2. **Panel de Control en Tiempo Real:**
   * Controles deslizantes (*sliders*) para modificar en caliente los multiplicadores de peso de **Separación**, **Alineación**, **Cohesión**, **Fuerza del Depredador**, **Radio de Percepción**, **Velocidad Máxima** y **Cantidad de Boids**.
   * Botones de *Presets* de comportamiento (ej. "Enjambre Caótico de Insectos", "Cardumen de Peces Compacto", "Bandada de Estorninos / Murmuration").
   * Contador de FPS en tiempo real, número de agentes activos y conteo de chequeos de vecindad por fotograma.

---

### 4. Reglas de Entrega
* Entrega el **código completo, íntegro y 100% funcional** en un solo bloque listo para copiar, guardar y ejecutar directamente.
* **Prohibido** usar comentarios de omisión (`// ... resto del código`) o dejar métodos matemáticos sin implementar.
* Incluye al final una breve nota de 2 líneas indicando el comando exacto o la forma de ejecutarlo en mi máquina.

Todo en una carpeta llamada "vida-artificial"


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


4. **Generador de Mazmorras (Rogue-like):** Un algoritmo que dibuje un mapa de mazmorra procedural. Debe generar habitaciones rectangulares aleatorias que NO se superpongan, conectadas lógicamente por pasillos de un pixel de ancho. *Reto: Algoritmos de partición de espacio (BSP) o lógica de colisiones pura.*
### Gemini 3.8 Flash High - Antigravity - 2 minutos
### Gemini 4 Argon High - Antigravity - 12 minutos

### NOTAS: Indiscutiblemente mejor Argon, por alguna razón Flash solo trabajo por dos minutos y decidio que habia terminado, tiene varios bugs y no interactua con el entorno, en cambio, Argon dejo algo completamente funcional y que se actualiza visualmente en tiempo real, interaccion con entorno, logs, A* en vivo, etc.

Actúa como un Arquitecto de Generación Procedural (PCG) y Desarrollador Senior de Motores de Videojuegos. Tu objetivo es construir un **Generador y Explorador Interactivo de Mazmorras Procedurales (Estilo Rogue-like)** visualmente rico, matemáticamente riguroso y con herramientas de visualización algorítmica en tiempo real, que se ejecutará en mi máquina local.

### 1. Libertad Tecnológica y Estética Total
* **Elección de Stack:** Tienes libertad para usar el entorno que te permita lograr la mejor combinación de rendimiento, control de píxeles/tiles y acabado visual (por ejemplo, un archivo único HTML5 con **Canvas 2D avanzado**, o una aplicación local en **Python con Pygame**).
* **Libertad Creativa (Cero Sobriedad):** No entregues una simple cuadrícula estática en blanco y negro. Diseña una interfaz digna de una herramienta de desarrollo de videojuegos indie o un *Dungeon Crawler* retro-moderno: texturizado procedural de baldosas (*autotiling* para muros, grietas en el suelo, antorchas animadas), iluminación dinámica 2D (antorchas con parpadeo y *Fog of War* / Campo de Visión), biomas temáticos (cripta oscura, caverna volcánica, laboratorio arcano) y un HUD de telemetría completo.
* **Cero Dependencias Externas Rotas:** **PROHIBIDO** cargar hojas de sprites (*spritesheets*) o imágenes desde URLs externas. Todos los gráficos, texturas de muros/pisos, iconos de entidades y efectos de luz deben dibujarse **100% de forma procedural mediante código**.

---

### 2. Requerimientos Algorítmicos y Matemáticos (El Núcleo del Reto)
El motor de generación debe cumplir estrictamente con las siguientes reglas topológicas y geométricas:

1. **Generación de Habitaciones Sin Superposición (Cero Colisiones):**
   * Implementa un algoritmo sólido como **Partición Binaria del Espacio (BSP Tree)** o **Generación por Rechazo/Separación Física con AABB (Axis-Aligned Bounding Boxes)** incluyendo un margen de seguridad (*padding*) mínimo de al menos 1 a 2 celdas de muro entre cualquier par de habitaciones para que jamás se fusionen ni se encimen por error.
   * Las habitaciones deben ser rectangulares con dimensiones variables controladas por parámetros (`minRoomSize`, `maxRoomSize`).

2. **Conexión Lógica por Pasillos de 1 Unidad de Ancho:**
   * Todas las habitaciones deben estar conectadas mediante pasillos ortogonales (en forma de L o trazados mediante búsqueda de caminos en cuadrícula) de **exactamente 1 celda/píxel lógico de ancho**.
   * **Garantía de Conectividad Total (Grafo Conexo):** Queda estrictamente prohibido que existan habitaciones aisladas o inalcanzables. Utiliza la jerarquía de ramas del árbol BSP o un **Árbol de Expansión Mínima (Algoritmo de Prim / Kruskal)** sobre los centroides de las habitaciones (opcionalmente reintroduciendo un porcentaje configurable de ciclos/atajos para que la mazmorra no sea puramente lineal).
   * Coloca puertas lógicas en las intersecciones exactas donde un pasillo de 1 celda de ancho desemboca en una habitación.

3. **Población Procedural y Verificación con Pathfinding (A*):**
   * Designa algorítmicamente una **Habitación de Inicio (Entrada/Escaleras arriba)** y la habitación más lejana en el grafo como **Habitación del Jefe / Salida (Escaleras abajo)**, además de distribuir cofres, trampas o enemigos según heurísticas de distancia.
   * Implementa el algoritmo **A* (A-Estrella)** o **Mapa de Dijkstra** para trazar y visualizar en pantalla la ruta crítica óptima desde la entrada hasta la salida (o entre cualquier par de celdas que el usuario seleccione con el mouse), demostrando matemáticamente que la mazmorra es 100% resoluble.

---

### 3. Requerimientos Visuales, Modos Interactivos y Controles (HUD)
1. **Visualización Algorítmica Paso a Paso vs. Instantánea:**
   * Incluye un modo **"Ver Construcción Paso a Paso"** animado donde se observe en vivo cómo el algoritmo divide el espacio (líneas de partición del árbol BSP o cajas de colisión), talla las habitaciones, calcula el grafo de conectividad (líneas entre centros) y excava los pasillos celda por celda.
   * Incluye un botón de **"Generación Instantánea"** con soporte para **Semilla Alfanumérica (Seed / PRNG propio)** para poder recrear exactamente la misma mazmorra cuando se desee.

2. **Capas de Renderizado y Modo Exploración:**
   * Permite alternar entre **Vista de Arquitecto (Mapa Completo + Capas de Debug)** y **Modo Explorador Jugable**, donde puedas mover a un aventurero con el teclado (`WASD` / Flechas) a través de la mazmorra con **Cálculo de Campo de Visión (2D Raycasting / Shadowcasting)** y *Fog of War* (niebla de guerra que revela solo lo que tienes en línea de visión y deja en penumbra lo ya visitado).
   * Interruptores (*Toggles*) para mostrar/ocultar: Particiones BSP, Grafo de nodos/conexiones, Mapa de calor de distancias (Dijkstra Distance Map) y Ruta A*.

3. **Panel de Control y Telemetría:**
   * Controles deslizantes (*sliders*) para ajustar en caliente: Tamaño de la cuadrícula del mapa, Profundidad de partición / Cantidad de habitaciones, Tamaño mínimo y máximo de habitaciones, Porcentaje de pasillos extra (ciclos) y Velocidad de animación de construcción.
   * Métricas en pantalla: Semilla actual, Número de habitaciones generadas, Longitud del camino crítico (Entrada $\rightarrow$ Salida), Porcentaje de área excavada y Tiempo de cómputo en milisegundos.

---

### 4. Reglas de Entrega
* Entrega el **código completo, íntegro y 100% funcional** en un solo bloque listo para copiar, guardar y ejecutar directamente.
* **Prohibido** usar comentarios de omisión (`// ... resto del código`) o dejar algoritmos como el BSP o el A* incompletos.
* Incluye al final una breve nota de 2 líneas indicando el comando exacto o la forma de ejecutarlo en mi máquina.

Todo en una carpeta llamada "generador-mazmorras"


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


5. **Simulador de "Falling Sand" (Estilo Noita/Spelunky):** Un lienzo basado en cuadrícula donde puedas soltar pixeles con el mouse. Debe simular arena (cae y forma pirámides), agua (cae y se esparce horizontalmente) y piedra (estática). *Reto: Autómatas celulares complejos y rendimiento.*
### Gemini 3.8 Flash High - Antigravity - 9 minutos
### Gemini 4 Argon High - Antigravity - 4 minutos

### NOTAS: Aqui a pesar de que Argon tardo menos de la mitad que Flash, le dio dos vueltas, la interaccion y la complegidad del entendimiento del como interactuan las cosas en el entorno entre si, es 10 veces mejor en el resultado de Argon que en el de Flash

Actúa como un Ingeniero de Motores Físicos y Desarrollador Creativo Senior (al estilo de Nolla Games, creadores de *Noita*). Tu objetivo es construir un **Motor de Simulación Física de Autómatas Celulares ("Falling Sand" / Píxeles Físicos)** ultrarrápido, con reacciones químicas emergentes y un acabado visual vibrante, que se ejecutará en mi máquina local.

### 1. Libertad Tecnológica y Estética Total
* **Elección de Stack:** Elige el entorno que te permita manipular buffers de píxeles directamente en memoria a 60 FPS estables con decenas de miles de partículas activas (por ejemplo, un archivo único HTML5 manipulando directamente `ImageData` / `Uint32Array` en **Canvas 2D / WebGL**, o una aplicación local en **Python con Pygame / ModernGL**).
* **Libertad Creativa (Cero Sobriedad):** Prohibido usar colores planos y aburridos tipo MS Paint.Cada grano de arena, gota de agua o bloque de roca debe tener **variación cromática procedural (dithering / ruido de textura por píxel)** para darle textura orgánica. Añade efectos visuales avanzados como resplandor térmico (*glow/bloom*) para elementos incandescentes, chispas, humo ascendente y un HUD de laboratorio físico en tiempo real.
* **Cero Dependencias Externas:** Todo el motor de autómatas celulares, renderizador por buffer e interfaz debe ser 100% autocontenido en el código.

---

### 2. Requerimientos Físicos y Algorítmicos (El Núcleo del Reto)
Debes implementar una cuadrícula física de alta densidad donde cada píxel es un autómata celular con propiedades de **estado, densidad ($\rho$), inflamabilidad, color base y un flag de actualización por frame (`updated`)**:

1. **Los 3 Elementos Fundamentales (Obligatorios):**
   * **Arena (Sólido Granular - $\rho = 3$):** Cae verticalmente por gravedad ($y+1$). Si está bloqueada abajo, se desliza diagonalmente hacia abajo-izquierda ($x-1, y+1$) o abajo-derecha ($x+1, y+1$) formando pirámides naturales perfectas. **Interacción de densidad:** Si cae sobre Agua o Aceite, debe hundirse desplazando el líquido hacia arriba (intercambio de celdas).
   * **Agua (Líquido - $\rho = 2$):** Cae verticalmente y en diagonal inferior; si no puede bajar, se esparce horizontalmente ($x \pm v_{\text{disp}}$) con una tasa de dispersión horizontal de varios píxeles por frame para nivelarse rápidamente como un fluido real y no quedarse estancada en escalones irreales.
   * **Piedra (Sólido Estático - $\rho = \infty$):** Inmune a la gravedad, actúa como contenedor, suelo o estructura arquitectónica. Aplica un patrón sutil de ruido en escala de grises al dibujarla para que parezca roca tallada.

2. **Química Emergente Estilo *Noita* (Elementos Extra para Libre Albedrío):**
   * Incorpora al menos **4 elementos reactivos adicionales** en la paleta para demostrar interacciones complejas:
     * **Fuego / Brasas:** Asciende erráticamente, tiene un tiempo de vida (`lifetime`), ilumina su entorno, quema materiales inflamables y se apaga al contacto con el agua generando **Vapor**.
     * **Vapor / Humo (Gas - $\rho = -1$):** Flota hacia arriba, atraviesa líquidos hacia la superficie y se condensa o disipa con el tiempo.
     * **Madera / Planta (Sólido Inflamable)** y **Aceite (Líquido Inflamable - $\rho = 1$):** El aceite debe flotar siempre por encima del agua y arder violentamente en contacto con el fuego.
     * **Ácido o Lava:** El ácido corroe la piedra y la arena emitiendo vapores tóxicos; la lava funde materiales y al tocar el agua se solidifica en **Piedra/Obsidiana** liberando vapor.

3. **Rigor en el Bucle de Simulación (Sin Sesgos Direccionales):**
   * Recorre la matriz de abajo hacia arriba para la gravedad, pero **alterna o aleatoriza el orden de barrido horizontal (izquierda-derecha vs. derecha-izquierda)** en cada fotograma o fila. Esto es crítico para evitar el clásico "sesgo de barrido" donde el agua o la arena tienden a fluir siempre hacia la izquierda.
   * Implementa control de estado por fotograma (*clock bit* o *updated flag*) para que una partícula no sea procesada ni teletransportada múltiples veces en un mismo *tick*.

---

### 3. Requerimientos de Interfaz, Herramientas y Telemetría (HUD)
1. **Herramientas de Manipulación Física:**
   * **Pincel Dinámico:** Rueda del mouse o *slider* para cambiar el radio del pincel (desde 1 píxel de precisión hasta brocha masiva), con opción de rocío disperso (*spray*) para polvos/líquidos y trazo continuo interpolado (algoritmo de línea de *Bresenham* entre la posición anterior y actual del mouse) para que al mover el cursor rápido los muros de piedra no queden con huecos.
   * **Herramientas Especiales:** Borrador (Vacío), "Bomba/Explosión" de onda expansiva que lance los píxeles por los aires con velocidad física, y un Grifo/Emisor continuo (*Spawner*).
2. **Controles de Simulación y Telemetría:**
   * Selector visual de elementos con código de colores e indicador de su categoría (Sólido, Polvo, Líquido, Gas, Energía).
   * Controles de Pausa, Avanzar 1 Frame (*Step*), Limpiar Lienzo, Invertir Gravedad y generar un "Escenario de Prueba / Terrario" preconstruido con un clic.
   * Telemetría en vivo: FPS, resolución de la cuadrícula lógica, conteo total de píxeles activos desglosado por tipo de materia y tiempo de cómputo del *tick* físico en milisegundos.

---

### 4. Reglas de Entrega
* Entrega el **código completo, íntegro y 100% funcional** en un solo bloque listo para copiar, guardar y ejecutar directamente.
* **Prohibido** usar comentarios de omisión (`// ... resto de elementos`) o dejar las reglas de colisión/densidad incompletas.
* Incluye al final una breve nota de 2 líneas indicando el comando exacto o la forma de ejecutarlo en mi máquina.

Todo en una carpeta llamada "falling-sand"

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### 👾 3. Pixel Art y Retro Computing

6. **Motor de Raycasting (Estilo Wolfenstein 3D):** Un motor 3D en primera persona creado desde cero **solo con Canvas 2D Vanilla JS** (sin librerías 3D). Un mapa 2D que se renderiza proyectando rayos para dar la ilusión de paredes en 3D con texturas (o colores) degradados según la distancia. *Reto: Matemáticas de trigonometría intensiva.*
### Gemini 3.8 Flash High - Antigravity - 17 minutos
### Gemini 4 Argon High - Antigravity - 4 minutos

### NOTAS: Aqui no hay de donde defender a Flash, el resultado para haber tardado mas de 4 veces lo que Argon es deplorable, es injugable, no hay interaccion mas que con las puertas, el mundo se rompe, en cambio, Argon con los 4 minutos que demoro en dar el resultado, es 100 veces mejor, jugable y con interaccion en el entorno, Argon esta siendo mas eficiente, efectivo y rapido.

Actúa como un Ingeniero de Motores Gráficos Retro (al estilo de John Carmack en los inicios de id Software) y Desarrollador Creativo Senior. Tu objetivo es construir desde cero un **Motor 3D en Primera Persona basado en Raycasting (Estilo Wolfenstein 3D)**, utilizando exclusivamente matemáticas trigonométricas y renderizado 2D puro, que se ejecutará en mi máquina local.

### 1. Libertad Tecnológica y Estética Total (Con Restricción de Motor 3D)
* **Restricción de Honor del Reto:** Queda **ESTRICTAMENTE PROHIBIDO** utilizar WebGL, Three.js, OpenGL o cualquier librería/API 3D. Toda la ilusión tridimensional debe construirse desde cero proyectando rayos en un entorno 2D y dibujando columnas verticales o manipulando el buffer de píxeles en **Canvas 2D Vanilla JS** (o un lienzo 2D puro equivalente).
* **Libertad Creativa (Cero Sobriedad):** No hagas un laberinto básico de bloques grises planos. Diseña una experiencia inmersiva completa: texturas procedurales detalladas de 64x64 píxeles (muros de piedra musgosa, ladrillos sangrientos, paneles metálicos, puertas), iluminación atmosférica con niebla de distancia (*depth fog*), arma o artefacto animado en primera persona con *head-bobbing* al caminar, puertas corredizas interactivas y objetos/sprites en el escenario.
* **Cero Dependencias Externas Rotas:** **PROHIBIDO** cargar imágenes o texturas desde URLs externas. Todas las texturas de paredes, sprites de objetos y gráficos del arma deben generarse **100% en memoria de forma procedural** al iniciar el script.

---

### 2. Requerimientos Matemáticos y Algorítmicos (El Núcleo del Reto)
Tu motor de Raycasting debe implementar con precisión matemática los siguientes pilares:

1. **Algoritmo DDA (Digital Differential Analysis):**
   * En lugar de usar *ray-marching* de paso fijo (que es lento y atraviesa esquinas por imprecisión), implementa el algoritmo **DDA** para saltar exactamente de intersección en intersección sobre la cuadrícula del mapa 2D ($\Delta x$, $\Delta y$, `sideDistX`, `sideDistY`), logrando precisión matemática perfecta y alto rendimiento.

2. **Corrección Obligatoria del Efecto "Ojo de Pez" (Fisheye Correction):**
   * Si utilizas la distancia euclidiana directa desde el jugador hasta el muro, las paredes rectas se verán curvadas como una pecera. Debes calcular la **distancia perpendicular al plano de la cámara**:
     $$d_{\perp} = d_{\text{real}} \cdot \cos(\theta_{\text{rayo}} - \theta_{\text{jugador}})$$
     (o su equivalente mediante vectores de dirección y plano de cámara $\vec{d}$ y $\vec{p}$).
   * Calcula la altura proyectada de cada tira vertical en pantalla como $h_{\text{muro}} = \frac{H_{\text{pantalla}}}{d_{\perp}}$.

3. **Mapeo de Texturas Procedurales y Sombreado Direccional:**
   * Calcula la coordenada exacta del impacto en el muro (`wallX` $\in [0, 1)$) para extraer la columna correspondiente (`texX`) de la textura procedural de $64 \times 64$ píxeles y escalarla verticalmente en pantalla.
   * Aplica **sombreado diferencial por orientación**: las paredes impactadas en orientación Norte-Sur vs. Este-Oeste (`side == 1`) deben tener distinta intensidad lumínica para que las esquinas se distingan claramente, además de un factor de atenuación proporcional a la distancia ($I \propto 1 / (1 + k \cdot d_{\perp}^2)$) que simule la luz de una antorcha o linterna en la oscuridad.

4. **Z-Buffer 1D, Sprites (*Billboarding*) y Colisiones Deslizantes:**
   * Almacena la distancia perpendicular de cada columna de la pantalla en un arreglo `zBuffer[width]`. Úsalo para renderizar **Sprites 2D en el espacio 3D** (barriles, pilares, antorchas, orbes o enemigos) que se oculten correctamente detrás de las paredes.
   * Implementa **detección de colisiones con deslizamiento (*Wall Sliding*)** separando la validación de movimiento en los ejes $X$ e $Y$ con un radio de margen (`playerRadius`), permitiendo que el jugador se deslice suavemente al rozar una pared en diagonal en lugar de quedarse trabado en seco.

---

### 3. Requerimientos Visuales, Minimapa e Interfaz (HUD)
1. **Minimapa 2D Técnico en Tiempo Real (Dual-View):**
   * Renderiza en una esquina (o en vista dividida conmutable) el mapa 2D visto desde arriba mostrando: la cuadrícula de muros, la posición del jugador, las entidades y el **abanico/cono completo de rayos proyectados en tiempo real** chocando exactamente contra las paredes.
2. **Interactividad y Controles Fluidos:**
   * Movimiento completo en primera persona (`WASD` para caminar y desplazarse lateralmente / *strafe*, Flechas o **Mouse con `PointerLockAPI`** para girar la vista, `Shift` para correr, `E` o `Espacio` para abrir/cerrar puertas mecánicas en el mapa, y Clic para accionar el arma/linterna con destello de luz dinámica).
3. **Panel de Telemetría y Ajustes en Caliente:**
   * Controles interactivos para modificar en vivo: Campo de Visión (**FOV** de 40° a 110°), Resolución de Rayos (desde modo ultra-pixelado retro hasta resolución nativa), Distancia de Niebla/Iluminación, y un interruptor para **activar/desactivar la corrección de Ojo de Pez** (para demostrar visualmente la diferencia matemática al instante).
   * Indicadores en pantalla: FPS, Coordenadas $(X, Y)$, Ángulo de visión y cantidad de rayos trazados por frame.

---

### 4. Reglas de Entrega
* Entrega el **código completo, íntegro y 100% funcional** en un solo bloque listo para copiar, guardar y ejecutar directamente.
* **Prohibido** usar comentarios de omisión (`// ... resto del código`) o dejar las funciones de texturizado o el algoritmo DDA incompletos.
* Incluye al final una breve nota de 2 líneas indicando el comando exacto o la forma de ejecutarlo en mi máquina.

Todo en una carpeta llamada "motor-raycasting"


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



7. **Generador de Sprites Espaciales Procedurales:** Un script que dibuje naves espaciales en 8-bits (pixel art) de manera aleatoria. Debe generar una matriz bidimensional simétrica, colorearla y renderizarla en grande. Cada recarga de la página debe dar una nave única. *Reto: Lógica de simetría y paletas de colores coherentes.*
### Gemini 3.8 Flash High - Antigravity - 13 minutos
### Gemini 4 Argon High - Antigravity - 4 minutos

### NOTAS: En este caso, la interfaz no se rompe, pero las naves generadas, el simulador, efectos y demas, sin duda y de nuevo se lo lleva Argon, en este caso, Flash tardo mas de tres veces lo que Argon y aun asi volvio a salir victorioso en esta comparativa

Actúa como un Artista Técnico de Pixel Art Procedural y Desarrollador Creativo Senior. Tu objetivo es construir una **Forja y Hangar Interactivo de Sprites Espaciales Procedurales en 8-Bits (Estilo Arcade / Shmup)**, capaz de sintetizar naves espaciales únicas mediante matrices matemáticas, sombreado automático y animación en tiempo real, ejecutándose en mi máquina local.

### 1. Libertad Tecnológica y Estética Total
* **Elección de Stack:** Elige el entorno que te brinde el control más nítido a nivel de píxel (*pixel-perfect rendering* sin suavizado borroso) y una interfaz fluida (por ejemplo, un archivo único HTML5 con **Canvas 2D (`imageSmoothingEnabled = false`)**, o una aplicación local en **Python con Pygame**).
* **Libertad Creativa (Cero Sobriedad):** No te limites a dibujar un único sprite estático sobre un fondo gris. Construye un **Hangar de Naves Espaciales Retro-Futurista** completo: fondo de espacio profundo con paralaje de estrellas (*starfield*), vista principal de la nave insignia con propulsores de plasma animados, vista de escuadrón/flota en cuadrícula, estadísticas RPG generadas proceduralmente para cada nave (nombre, facción, potencia de fuego, escudo, velocidad) y un **"Modo Vuelo de Prueba (Test Flight)"** donde puedas pilotar la nave recién generada y disparar láseres en el lienzo.
* **Cero Dependencias Externas:** Todos los algoritmos de generación, paletas cromáticas, efectos de partículas y renderizado deben ser 100% autocontenidos en el código.

---

### 2. Requerimientos Algorítmicos y Matemáticos (El Núcleo del Reto)
Para que el resultado parezca arte diseñado por un humano y no un código QR aleatorio, debes implementar el siguiente pipeline algorítmico (inspirado en el método de *Dave Bollinger / Pixel Spaceships* evolucionado):

1. **Matriz de Plantilla Estructural y Simetría Bilateral:**
   * Trabaja con una matriz bidimensional de resolución configurable (ej. $16 \times 16$, $24 \times 24$ o $32 \times 32$).
   * Calcula únicamente la mitad izquierda de la matriz ($0 \le x < W/2$) y refléjala matemáticamente sobre el eje vertical central ($W - 1 - x$) para garantizar **simetría bilateral perfecta**.
   * **Máscara de Densidad Anatómica:** En lugar de ruido uniforme, utiliza una función de probabilidad ponderada según la coordenada $(x, y)$ o zonas lógicas:
     * **Núcleo/Fuselaje central (cerca del eje de simetría):** Alta probabilidad de celdas sólidas conectadas y cabina de mando (*cockpit*).
     * **Alas y Armamento (zonas medias/exteriores):** Probabilidad media con reglas de conectividad celular (autómata celular de 1 o 2 pasos para eliminar píxeles huérfanos flotantes y consolidar estructuras sólidas).
     * **Propulsores (borde inferior):** Nodos específicos en la base del fuselaje que actuarán como emisores de fuego/plasma.

2. **Detección de Bordes y Sombreado Volumétrico Automático (Pixel Shading):**
   * Una vez generada la silueta base y las sub-partes (casco primario, placas secundarias, cabina, motores), recorre la matriz aplicando reglas de iluminación 2D:
     * **Contorno Exterior (*Outline*):** Todo píxel vacío que sea adyacente (ortogonalmente) a un píxel sólido de la nave debe convertirse en un borde oscuro (negro o el tono más profundo de la paleta) para darle acabado de sprite arcade clásico.
     * **Iluminación Especular y Sombras Internas:** Calcula la normal aproximada de cada píxel interno; si tiene vacío o un componente distinto arriba, aplica un tono más brillante (*highlight* superior); si está en el borde inferior de una estructura, aplica un tono más oscuro (*shadow* inferior). Esto dará volumen 3D real al pixel art.

3. **Teoría del Color y Paletas Armónicas Coherentes:**
   * **Prohibido usar `RGB` completamente aleatorio.** Construye un generador de rampas de color en espacio **HSL / HSV** con *Hue Shifting* (desplazamiento sutil de matiz hacia el azul/violeta en las sombras y hacia el amarillo/blanco en las luces altas).
   * Genera paletas coherentes por facción o arquetipo (ej. *Imperio Galáctico, Caza Cyberpunk Neón, Flota Alienígena Bio-orgánica, Industrial Pesado, Retro GameBoy 4-Colores*) diferenciando claramente el color del chasis, el cristal brillante de la cabina y la energía de los propulsores.

---

### 3. Requerimientos Visuales, Modos Interactivos y Controles (HUD)
1. **Recarga Única + Generador por Semilla (Seed):**
   * Cada recarga de la página debe inicializar una semilla aleatoria nueva mostrando una nave principal inédita en gran escala, acompañada de una galería inferior o lateral con una flota de variantes generadas al instante.
   * Permite ingresar una **Semilla (Seed)** personalizada para recrear exactamente cualquier nave.
2. **Animación Viva y Modo "Test Flight" (Jugable):**
   * Incluso en el hangar, la nave debe sentirse viva: oscilación suave de levitación (*hover*), parpadeo de luces de navegación y partículas de escape saliendo de las celdas marcadas como propulsores.
   * Incluye un botón o tecla para activar el **Modo Vuelo de Prueba**, permitiendo mover la nave por la pantalla con el teclado o mouse a través del campo de estrellas y disparar proyectiles procedurales desde las puntas de sus alas/cañones con retroceso visual (*screen shake* / *muzzle flash*).
3. **Controles de Ingeniería y Exportación:**
   * Selectores para cambiar la **Clase de Nave** (*Interceptor Ligero, Cazabombardero, Crucero Pesado, Nave Nodriza*), tamaño de matriz ($12\times12$ a $32\times32$), estilo de contorno y paleta cromática.
   * Visor de capas del algoritmo (ver Máscara de Probabilidad $\rightarrow$ Matriz Binaria Base $\rightarrow$ Mapa de Regiones $\rightarrow$ Sombreado Final) y botón para **Descargar el Sprite en PNG** (escalado limpio sin *aliasing*).

---

### 4. Reglas de Entrega
* Entrega el **código completo, íntegro y 100% funcional** en un solo bloque listo para copiar, guardar y ejecutar directamente.
* **Prohibido** usar comentarios de omisión (`// ... resto del código`) o dejar el algoritmo de sombreado/simetría incompleto.
* Incluye al final una breve nota de 2 líneas indicando el comando exacto o la forma de ejecutarlo en mi máquina.

Todo en una carpeta llamada "generador-sprites"

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### ✨ 4. Pura Magia CSS (Sin JavaScript o casi nulo)

8. **Reloj Analógico Neumórfico Fotorrealista:** Un reloj con manecillas de horas, minutos y segundos (con movimiento de barrido continuo). Todo construido con HTML y CSS (sombras dinámicas, biseles). JS solo se usa para darle la hora actual al cargar. *Reto: Transform-origins, animaciones CSS y diseño UI complejo.*
### Gemini 3.8 Flash High - Antigravity - 4 minutos
### Gemini 4 Argon High - Antigravity - 2 minutos

### NOTAS: Aqui ambos cumplieron, en cuanto a funcionalidad, los dos cumplen al pie de la letra, el tema es que a pesar de que Argon tardo la mitad de tiempo que Flash, Argon de nuevo gana en tanto a calidad del producto entregado, es mas agradable y vistoso de ver, de nuevo, Argon ganando en eficiencia y calidad

Actúa como un Ingeniero de UI/UX Senior, Maestro de CSS Avanzado y Diseñador de Alta Relojería (*Haute Horlogerie*). Tu objetivo es construir un **Reloj Analógico Neumórfico y Esqueuomórfico Fotorrealista de Alta Precisión**, renderizado y animado mediante **HTML y CSS Puro**, que se ejecutará en mi máquina local.

### 1. Libertad Estética Total (Con la Restricción de Oro del Reto)
* **Restricción de Honor (Cero JS en el Bucle de Animación):** Queda **ESTRICTAMENTE PROHIBIDO** usar `<canvas>`, SVG complejos prefabricados, imágenes externas o bucles de JavaScript (`setInterval` / `requestAnimationFrame`) para mover las manecillas. Toda la geometría, texturas metálicas, biseles, sombras e impulsos cinemáticos deben construirse con **HTML + CSS Puro**.
* **Uso Permitido de JavaScript (Solo Sincronización Inicial):** El único código JS permitido es un micro-script al cargar la página (`DOMContentLoaded`) que lea la hora exacta del sistema una sola vez y configure Variables CSS (`--initial-hours`, `--initial-minutes`, `--initial-seconds` o `animation-delay` negativos) para que, a partir de ese milisegundo, las animaciones `@keyframes` de CSS mantengan la hora real de forma perpetua y autónoma. (También puedes usar un mínimo de JS al inicio solo para inyectar en el DOM los 60 nodos de las marcas de minutos si deseas evitar repetir 60 etiquetas HTML a mano).
* **Libertad Creativa (Cero Sobriedad):** No hagas un círculo plano con tres líneas simples. Diseña una pieza maestra de relojería industrial (inspirada en Dieter Rams / Braun, Omega o Patek Philippe combinada con Neumorfismo táctil moderno): chasis con extrusión suave, bisel de metal cepillado, sub-esferas (*complicaciones*), ventana de volante/engranaje vista (*Open-Heart / Tourbillon* animado con CSS), cristal de zafiro con reflejo especular y modos de iluminación.

---

### 2. Requerimientos Técnicos y Matemáticos en CSS (El Núcleo del Reto)
Debes demostrar un dominio absoluto del motor de renderizado CSS implementando:

1. **Cinemática de Barrido Continuo y Pivotes Exactos (`transform-origin`):**
   * Configura las 3 manecillas principales (**Horas, Minutos y Segundos**) con sus respectivos `transform-origin` milimétricamente calculados para que roten sobre el eje central exacto del reloj, incluyendo el **contrapeso trasero** característico de la aguja segundera.
   * **Movimiento Mecánico de Barrido (*Smooth Sweep*):** La manecilla de los segundos debe girar con un movimiento continuo fluido (`linear`) o simulando el latido de un calibre mecánico suizo de alta frecuencia (28,800 alternancias/hora usando `steps(480)` en 60s), mientras que las de minutos (`3600s`) y horas (`43200s`) avanzan de forma continua e imperceptible.

2. **Arquitectura Neumórfica y Materiales Fotorrealistas con Gradientes:**
   * **Doble Sombra Neumórfica:** Utiliza múltiples capas de `box-shadow` (sombras externas proyectadas e internas `inset` con luces altas en el ángulo superior izquierdo y penumbra en el inferior derecho) para esculpir una caja exterior convexa y una esfera interior (*dial*) cóncava profunda.
   * **Texturas Procedurales CSS:** Crea el acabado de **acero cepillado radial** en el bisel usando `repeating-conic-gradient` y texturas concéntricas (*guilloché* o *sunburst*) en la carátula usando `radial-gradient` y `repeating-radial-gradient`.
   * **Sombras Dinámicas de las Manecillas:** Cada aguja y el perno central (*capuchón*) deben proyectar sombras realistas (`filter: drop-shadow(...)`) sobre la esfera inferior para dar sensación real de separación física en el eje Z (capas de altura).

3. **Índices, Sub-esferas y Complicaciones Relojeras:**
   * Posiciona las **60 marcas del dial** (12 índices horarios principales en relieve + 48 marcas de minutos/segundos) utilizando variables CSS por índice (`--i`) y transformaciones trigonométricas o rotaciones anidadas (`rotate(calc(var(--i) * 6deg)) translateY(...)`).
   * Añade al menos **dos detalles de alta relojería en la esfera**:
     * Una **ventana de fecha (*Date Aperture*)** biselada con cristal de aumento tipo *Cyclops* o una sub-esfera de cronógrafo/indicador de 24 horas.
     * Una apertura **Open-Heart / Tourbillon mecánico** donde se vea una rueda de escape o engranaje dorado girando y oscilando en tiempo real mediante `@keyframes` de CSS puro.

---

### 3. Requerimientos Interactivos (CSS State Machines)
Sin usar JavaScript para la interacción, implementa controles táctiles neumáticos (usando el patrón `input[type="checkbox"]` o `input[type="radio"]` + selectores `:checked` y variables CSS en `:root`):
1. **Selector de Material / Tema en Vivo:**
   * **Modo Neumórfico Clásico (Soft Clay / Blanco Mate):** Sombras suaves de arcilla táctil.
   * **Modo Titanio Oscuro (Dark Carbon):** Chasis negro mate con detalles en rojo/naranja deportivo.
   * **Modo Lujo Nocturno (Super-LumiNova):** Apaga las luces del entorno y hace que los índices horarios y las manecillas emitan un **resplandor fosforescente verde/azul cian intenso** (`box-shadow` y `text-shadow` luminiscentes).
2. **Efecto Cristal de Zafiro Interactivo:**
   * Una capa superior semitransparente con reflejo diagonal y efecto `backdrop-filter` que reaccione sutilmente al pasar el cursor (`:hover`) sobre el reloj, desplazando el brillo especular como si la luz incidiera desde otro ángulo.

---

### 4. Reglas de Entrega
* Entrega el **código completo, íntegro y 100% funcional** en un solo bloque HTML (con el CSS y el micro-script de sincronización inicial embebidos) listo para guardar y abrir en el navegador.
* **Prohibido** usar comentarios de omisión (`/* ... resto de estilos */`) o dejar reglas CSS incompletas.
* Incluye al final una breve nota de 2 líneas indicando cómo abrirlo y probarlo en mi máquina.

Todo en una carpeta llamada "reloj-analogico"

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### 🧮 5. Matemáticas Puras

9. **Árbol Fractal con Viento (L-Systems):** Un árbol generado proceduralmente usando recursividad en Canvas. La complejidad radica en que debe haber una variable de "viento" impulsada por una función de ruido (Perlin noise o función senoidal compleja) que haga que las ramas se mezcan de forma natural. *Reto: Recursividad y cinemática inversa/directa.*
### Gemini 3.8 Flash High - Antigravity - 22 minutos
### Gemini 4 Argon High - Antigravity - 4 minutos

### NOTAS: Mismo caso que los anteriores, mejores graficos, mejores configuraciones, interaccion mas realista, actualizacion en tiempo real, y todo esto en menos de 1/5 del tiempo que le costo a Flash hacerlo, Argon es una maquina de eficiencia y calidad.

Actúa como un Ingeniero de Simulaciones Botánicas Computacionales y Desarrollador Creativo Senior. Tu objetivo es construir un **Simulador Interactivo de Árboles Fractales con Física de Viento y Cinemática Directa (L-Systems Estocásticos)**, visualmente poético y matemáticamente riguroso, que se ejecutará en mi máquina local.

### 1. Libertad Tecnológica y Estética Total
* **Elección de Stack:** Elige el entorno que te permita renderizar miles de segmentos orgánicos, follaje y partículas a 60 FPS estables (por ejemplo, un archivo único HTML5 con **Canvas 2D avanzado / WebGL**, o una aplicación local en **Python con Pygame / ModernGL**).
* **Libertad Creativa (Cero Sobriedad):** Prohibido dibujar un simple árbol de líneas cafés sobre un fondo blanco. Diseña un ecosistema atmosférico vivo: cielo con gradiente dinámico o iluminación crepuscular, corteza con sombreado cilíndrico, follaje exuberante con variaciones cromáticas (flores de cerezo *Sakura*, otoño dorado, sauce llorón o un árbol de almas bioluminiscente estilo *Avatar*), hierba reactiva en la base del tronco, hojas que se desprenden con las ráfagas fuertes y vuelan siguiendo el mismo campo vectorial de viento, y un HUD de telemetría botánica.
* **Cero Dependencias Externas:** Todo el generador de ruido coherente (Perlin/Simplex 2D/3D), motor cinemático y gráficos deben estar 100% autocontenidos en el código.

---

### 2. Requerimientos Matemáticos y Físicos (El Núcleo del Reto)
Tu motor debe resolver con precisión la topología recursiva y la física estructural:

1. **Separación de Topología y Renderizado (Cero Parpadeo Estocástico):**
   * **Regla Crítica:** No llames a `Math.random()` en bruto dentro del bucle de dibujo de cada fotograma sin fijar la estructura. Debes generar primero el **Grafo / Esqueleto del Árbol en memoria** (usando recursividad o reglas de producción *L-System* con una semilla fija), almacenando para cada rama su longitud base, ángulo de reposo ($\theta_0$), grosor, nivel de profundidad ($d$) y nodos hijos.
   * **Regla de Leonardo da Vinci para el Grosor:** El radio de una rama madre debe decaer de forma natural en cada bifurcación ($r_{d} = r_{d-1} \cdot \text{ratio}$, con $\text{ratio} \approx 0.68 - 0.75$), dibujando trapecios o trazos cónicos suaves en lugar de rectángulos bruscos.

2. **Cinemática Directa Jerárquica (Forward Kinematics):**
   * Las ramas no pueden doblarse de forma aislada desconectándose de sus ramas hijas. Cada nodo hijo debe calcular su posición de inicio exactamente en el punto final $(x_{\text{end}}, y_{\text{end}})$ de su rama padre en ese instante de tiempo, y **heredar el ángulo acumulado** de toda su cadena ancestral:
     $$\theta_{\text{actual}}(d, t) = \theta_{\text{padre}}(t) + \theta_{\text{local}} + \Delta\theta_{\text{viento}}(x, y, d, t)$$
   * De este modo, cuando el tronco o una rama principal se inclina por un vendaval, toda la sub-estructura de ramas secundarias y hojas se traslada y rota solidariamente como un esqueleto articulado real.

3. **Campo de Viento con Ruido Coherente (Perlin / Simplex Noise) y Elasticidad:**
   * Implementa desde cero un generador de **Ruido Perlin o Simplex 2D** (o una superposición armónica de ondas espaciales con turbulencia fractal *fBM*) evaluado en las coordenadas espaciales de cada rama y el tiempo: $\text{Noise}(x \cdot s, y \cdot s, t \cdot \omega)$.
   * **Rigidez Estructural por Nivel ($k_{\text{flex}}$):** El tronco principal ($d=0$) debe ser sumamente rígido y apenas mecerse unos pocos grados, mientras que la flexibilidad debe crecer exponencialmente hacia las ramas terminales y las hojas ($\Delta\theta \propto d^{\alpha}$), añadiendo un desfase de fase temporal para simular la propagación de la onda de viento a través de la copa del árbol.

4. **Interacción Física con el Mouse y Desprendimiento de Hojas:**
   * El cursor del mouse debe actuar como un **vórtice o soplador local**: al mover o arrastrar el mouse cerca de las ramas, aplica una fuerza direccional proporcional a la velocidad del cursor que doble las ramas cercanas con rebote elástico (*spring damping*) al soltarlas.
   * Cuando la fuerza instantánea del viento supere un umbral en las ramas finales, desprende pétalos u hojas que pasen a ser partículas autónomas arrastradas por la gravedad, la turbulencia del ruido Perlin y el viento global.

---

### 3. Requerimientos Visuales, Especies y Controles (HUD)
1. **Selector de Especies / Estaciones (Presets en Vivo):**
   * Incluye botones para transformar la morfología y estética del árbol al instante:
     * **Cerezo Japonés (*Sakura*):** Tronco oscuro retorcido, copa amplia y miles de flores/pétalos rosados cayendo en el viento.
     * **Sauce Llorón (*Weeping Willow*):** Ramas largas y flexibles con factor de gravedad positivo que caen como cortinas verdes mecidas suavemente.
     * **Roble Invernal / Secuoya:** Estructura imponente, alta profundidad fractal y follaje denso o escarcha.
     * **Árbol Bioluminiscente Nocturno:** Estética de fantasía/sci-fi con savia brillante, hojas de neón cian/violeta con efecto *glow* y esporas flotantes.
2. **Panel de Control Botánico y Meteorológico:**
   * Controles deslizantes (*sliders*) para ajustar en tiempo real:
     * **Fuerza Base del Viento** (desde brisa calmada hasta huracán/tormenta).
     * **Turbulencia y Frecuencia de Ráfagas** (escala del ruido Perlin).
     * **Profundidad de Recursión** (hasta 10-12 niveles con optimización).
     * **Ángulo de Bifurcación, Asimetría del Árbol y Relación de Longitud**.
   * Botón para generar una **Nueva Semilla**, interruptor para visualizar el **Campo Vectorial del Viento (flechas de flujo en el fondo)** y contador de FPS, número total de ramas y hojas activas.

---

### 4. Reglas de Entrega
* Entrega el **código completo, íntegro y 100% funcional** en un solo bloque listo para copiar, guardar y ejecutar directamente.
* **Prohibido** usar comentarios de omisión (`// ... resto del código`) o dejar la función de ruido Perlin/Simplex sin implementar.
* Incluye al final una breve nota de 2 líneas indicando el comando exacto o la forma de ejecutarlo en mi máquina.

Todo en una carpeta llamada "arbol-fractal"


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


10. **Spirograph Paramétrico Animado:** Un trazador de curvas hipotrocoides (como los juguetes de ruedas dentadas). Debe ir dibujando la línea lentamente en la pantalla cambiando de color (HSL dinámico). *Reto: Fórmulas paramétricas complejas y animación por fotogramas (`requestAnimationFrame`).*
### Gemini 3.8 Flash High - Antigravity - 10 minutos
### Gemini 4 Argon High - Antigravity - 4 minutos

### NOTAS: Aqui ambos hicieron bien su trabajo, el unico detalle es la calidad de personalizacion que nos permitio Argon, dando asi la posibilidad de conseguir mandalas que lleguen 40,000.00 rad, y esto 2.5 veces mas rapido que Flash, es indiscutible, Argon es una mejora significativa a los modelos previos de Gemini en tanto a generacion, entendimiento y eficiencia.

Actúa como un Ingeniero de Geometría Computacional, Artista Algorítmico y Desarrollador Creativo Senior. Tu objetivo es construir un **Estudio Interactivo de Trazado Paramétrico de Alta Precisión (Spirograph Mecánico, Curvas Hipotrocoides, Epitrocoides y Guilloché)**, visualmente hipnótico y matemáticamente exacto, que se ejecutará en mi máquina local.

### 1. Libertad Tecnológica y Estética Total
* **Elección de Stack:** Elige el entorno que te permita alcanzar una nitidez vectorial/sub-píxel impecable y animación fluida a 60 FPS (por ejemplo, un archivo único HTML5 con una **Arquitectura de Doble Canvas 2D** o **WebGL**, o una aplicación local en **Python con Pygame / ModernGL**).
* **Libertad Creativa (Cero Sobriedad):** No te limites a dibujar una línea simple sobre un fondo negro vacío. Diseña un laboratorio de geometría sagrada y arte generativo: trazos con fusión aditiva luminiscente (`globalCompositeOperation = 'lighter'` o `'screen'`), simulación visual en vivo de los **engranajes mecánicos dentados y el brazo articulado** girando mientras la punta láser incandescente deposita tinta brillante sobre el lienzo, chispas sutiles en el cabezal de dibujo, caligrafía variable (grosor dinámico según la velocidad del trazo) y un HUD de telemetría matemática.
* **Cero Dependencias Externas:** Todo el motor paramétrico, cálculo de teoría de números, renderizado de doble capa e interfaz debe ser 100% autocontenido en el código.

---

### 2. Requerimientos Matemáticos y Algorítmicos (El Núcleo del Reto)
Tu motor matemático debe implementar con rigor absoluto los siguientes componentes:

1. **Ecuaciones Paramétricas Exactas y Modos de Ruleta:**
   * **Hipotrocoide (Rueda rodando por el interior del anillo fijo):**
     $$x(t) = (R - r)\cos(t) + d\cos\left(\frac{R - r}{r}t\right)$$
     $$y(t) = (R - r)\sin(t) - d\sin\left(\frac{R - r}{r}t\right)$$
   * **Epitrocoide (Rueda rodando por el exterior del anillo fijo):**
     $$x(t) = (R + r)\cos(t) - d\cos\left(\frac{R + r}{r}t\right)$$
     $$y(t) = (R + r)\sin(t) - d\sin\left(\frac{R + r}{r}t\right)$$
   * **Modo Avanzado Multi-Rotor (Epiciclos / 3er Engranaje Opcional):** Permite activar una tercera rueda secundaria ($r_2, d_2$) acoplada o una modulación armónica para generar patrones de *Guilloché* de alta complejidad (como los grabados de seguridad de los billetes y pasaportes).

2. **Teoría de Números para el Cierre Perfecto del Ciclo (MCD / GCD):**
   * Calcula mediante el **Algoritmo de Euclides** el Máximo Común Divisor $\text{MCD}(R, r)$.
   * Determina y muestra matemáticamente antes de empezar a dibujar:
     * **Número exacto de revoluciones para cerrar la curva:** $N_{\text{rev}} = \frac{r}{\text{MCD}(R, r)}$ (por lo que el ángulo total de cierre es $t_{\max} = 2\pi \cdot N_{\text{rev}}$).
     * **Número total de pétalos / cúspides / lóbulos de la figura:** $P = \frac{R}{\text{MCD}(R, r)}$.
   * Muestra una barra de progreso precisa ($0\% \rightarrow 100\%$) que indique en qué momento exacto la aguja completará el circuito cerrado sin sobre-dibujar innecesariamente (a menos que el usuario active el modo de rotación continua).

3. **Arquitectura de Doble Buffer (Dual-Canvas) y Sub-Stepping Temporal:**
   * **Separación de Capas Obligatoria:** Utiliza **dos capas/lienzos superpuestos**:
     * **Capa 1 (Buffer Persistente de Tinta):** Acumula únicamente los segmentos de la curva paramétrica con *anti-aliasing* sin borrarse entre fotogramas, permitiendo trazar curvas de cientos de miles de pasos con 0% de degradación de FPS.
     * **Capa 2 (Overlay Mecánico Dinámico):** Se limpia en cada `requestAnimationFrame` para dibujar el anillo estator ($R$), la rueda dentada móvil ($r$) rotando sin deslizamiento en su posición instantánea, el radio vector hacia el orificio del bolígrafo ($d$) y el cabezal láser brillante en $(x(t), y(t))$.
   * **Sub-stepping de Alta Frecuencia:** Dentro de cada fotograma de `requestAnimationFrame`, ejecuta un bucle de $K$ micro-pasos con un diferencial $\delta t$ muy pequeño (ej. $\delta t = 0.005\text{ rad}$) para que, incluso a velocidades de dibujo altísimas, las curvas sean perfectamente suaves y jamás se vean poligonales o quebradas.

4. **Dinámica Cromática en Espacio HSL y Caligrafía Basada en Velocidad:**
   * Calcula la velocidad lineal instantánea de la pluma:
     $$v(t) = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}$$
   * Modula dinámicamente el color `HSL(h, s, l)` y la opacidad de cada micro-segmento según el modo elegido: por avance del ángulo $t$, por distancia radial al centro $\sqrt{x^2+y^2}$, o por la velocidad instantánea $v(t)$ (haciendo que las cúspides lentas brillen con más intensidad y distinto matiz que los arcos rápidos).

---

### 3. Requerimientos Visuales, Presets e Interfaz (HUD)
1. **Visualización Mecánica Conmutable:**
   * Interruptor en vivo para **Mostrar / Ocultar los Engranajes Guía**: cuando está activo, se ven las ruedas dentadas translúcidas tipo acrílico de ingeniero girando en sincronía perfecta con la línea que va naciendo; cuando se oculta, solo queda la obra de arte luminosa sobre el lienzo oscuro.
2. **Controles Paramétricos en Tiempo Real y Presets:**
   * Controles deslizantes (*sliders*) y campos numéricos para ajustar: Radio Fijo ($R$), Radio Móvil ($r$), Distancia de la Pluma ($d$), Velocidad de Trazado (sub-pasos por frame), Grosor de Pluma y Modo de Coloración HSL.
   * **Selector de Presets Matemáticos:** *Astroide Clásico, Deltoide, Roseta Solar de 17 Puntas, Mandala Hipotrocoide Complejo (ej. $R=144, r=55, d=89$ - proporción Fibonacci), Grabado Guilloché Imperial y Supernova Multi-Engranaje*.
   * Botones de acción rápida: **Pausar/Reanudar**, **Reiniciar Trazo Animado**, **Renderizar Ciclo Completo al Instante (Warp)**, **Añadir Capa (Superponer otra curva sin borrar la anterior)** y **Exportar Arte en PNG de Alta Resolución**.

---

### 4. Reglas de Entrega
* Entrega el **código completo, íntegro y 100% funcional** en un solo bloque listo para copiar, guardar y ejecutar directamente.
* **Prohibido** usar comentarios de omisión (`// ... resto del código`) o dejar las ecuaciones paramétricas o el renderizado de los engranajes incompletos.
* Incluye al final una breve nota de 2 líneas indicando el comando exacto o la forma de ejecutarlo en mi máquina.

Todo en una carpeta llamada "spirograph-parametrico"