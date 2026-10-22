# MEMORIA PERSISTENTE DEL PROYECTO (MEMORY.md)
> **INSTRUCCION PARA EL AGENTE DE IA:** Lee este archivo al inicio de CADA sesion antes de tocar cualquier archivo. Al finalizar cualquier cambio arquitectonico o resolver un bug no trivial, actualiza las secciones correspondientes manteniendo este archivo por debajo de 150 lineas.

## 1. Identidad y Objetivo del Proyecto
- **Nombre del Proyecto:** QUANTUM-HFT // Terminal Institucional de Trading Cuantitativo y Microestructura L3
- **Descripcion en 1 linea:** Terminal interactiva de alta frecuencia (60-120 FPS) con motor de emparejamiento CLOB L3, modelo de volatilidad estocastica de Heston con saltos de Poisson, superficie 3D de volatilidad implicita, velas japonesas con Heatmap L3 + VPVR, escalera DOM y osciloscopio VPIN/OFI.
- **URL de Produccion / Puerto Local:** `http://localhost:8812/index.html` (100% autocontenido para apertura directa en navegador)

## 2. Stack Tecnologico y Comandos Verificados
- **Lenguaje / Runtime:** HTML5 + CSS3 Grid + ES2024 Vanilla JavaScript (Zero-Dependency, 100% Single-File)
- **Framework Principal:** Motor Canvas 2D/3D Hardware-Accelerated con buffers tipados (`Float32Array` / `Float64Array` / `Uint8Array`) Zero-GC
- **Comando para levantar entorno local:** `python3 -m http.server 8812`
- **Comando de pruebas / verificacion:** Headless Chrome (`--virtual-time-budget=2500 --dump-dom`) + `node --check`

## 3. Reglas Inquebrantables de Arquitectura y Diseño
1. **Cero Codigo Incompleto:** Prohibido dejar comentarios como `// TODO`, `// implementar despues` o funciones vacias.
2. **Verificacion Real Antes de Entregar:** Ninguna tarea se reporta como terminada hasta que el codigo compile sin errores y se haya verificado con cero errores en consola del navegador.
3. **Rendimiento y Limpieza (60-120 FPS):** Todos los historiales de velas (`MAX_CANDLES=90`), mapa de calor L3 (`90x32`), libro de ordenes (`28 niveles x 2`), sistema de particulas (`450 slots`) y osciloscopio (`240 muestras`) operan con `Float32Array` pre-asignados y desplazamientos en bloque via `.copyWithin()` para evitar pausas del Garbage Collector.
4. **Cero Emojis Unicode:** Toda la iconografia utiliza geometria vectorial SVG en linea y tipografia monoespaciada tabular.

## 4. Mapa de Archivos Clave
- `index.html` — Aplicacion monolitica autocontenida (Layout institucional, Motor Estocastico Heston + Jump-Diffusion, CLOB L3, 4 Visualizadores Canvas y Desk de Ejecucion DMA).
- `GEMINI.md` — Protocolo Maestro de Agente Mixiuh Labs Superpowers.
- `MEMORY.md` — Este archivo de memoria persistente entre sesiones.

## 5. Bitacora de Decisiones Tecnicas (ADR Corto)
- **[2026-10-22]:** Se instalo el **Mixiuh Labs AI Superpowers Kit v1.0** para eliminar la amnesia entre sesiones y exigir auto-verificacion de codigo.
- **[2026-10-22]:** Se implemento en `index.html` el motor HFT completo con 4 activos (`BTC-PERP`, `NVDA-AI`, `ETH-PERP`, `SOL-HFT`), 5 botones de estres extremo en vivo (`Flash Crash -25%`, `Ballena $50M`, `Short Squeeze`, `Cascada de Liquidaciones`, `Calmar Mercado`), ejecucion manual Market/Limit con apalancamiento 1x-100x y calculo automatico de precio de liquidacion.

## 6. Errores Conocidos y Soluciones Aprendidas (No Repetir)
- `[index.html / Bucle de Velas y Heatmap]`: Reasignar arreglos con `.shift()` y `.push()` a 120 Hz generaba presion en el GC -> Solucion aplicada: Uso de `Float32Array.prototype.copyWithin()` sobre buffers circulares y lineales de tamano fijo.
- `[Verificacion Browser Headless]`: El perfil compartido de Chrome MCP puede estar bloqueado por otra instancia -> Solucion aplicada: Usar `--user-data-dir` efimero aislado en `/tmp` sobre el puerto exclusivo `8812` y cerrar el servidor al concluir.
