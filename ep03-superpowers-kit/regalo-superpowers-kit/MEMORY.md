# MEMORIA PERSISTENTE DEL PROYECTO (MEMORY.md)
> **INSTRUCCION PARA EL AGENTE DE IA:** Lee este archivo al inicio de CADA sesion antes de tocar cualquier archivo. Al finalizar cualquier cambio arquitectonico o resolver un bug no trivial, actualiza las secciones correspondientes manteniendo este archivo por debajo de 150 lineas.

## 1. Identidad y Objetivo del Proyecto
- **Nombre del Proyecto:** [Nombre de tu App o Sistema]
- **Descripcion en 1 linea:** [Que problema resuelve y para quien]
- **URL de Produccion / Puerto Local:** `http://localhost:3000`

## 2. Stack Tecnologico y Comandos Verificados
- **Lenguaje / Runtime:** TypeScript / Python / HTML5 + ES2024
- **Framework Principal:** [Next.js / Astro / React / Flutter / Vanilla WebGL]
- **Comando para levantar entorno local:** `npm run dev` (o `python3 -m http.server 8080`)
- **Comando de pruebas / verificacion:** `npm test` / `npm run build`

## 3. Reglas Inquebrantables de Arquitectura y Diseño
1. **Cero Codigo Incompleto:** Prohibido dejar comentarios como `// TODO`, `// implementar despues` o funciones vacias.
2. **Verificacion Real Antes de Entregar:** Ninguna tarea se reporta como terminada hasta que el codigo compile sin errores y, si tiene interfaz visual, se haya verificado con cero errores en consola del navegador.
3. **Rendimiento y Limpieza:** Evitar algoritmos $O(N^2)$ en bucles de renderizado o procesamiento de listas grandes.

## 4. Mapa de Archivos Clave
- `src/` — Codigo fuente principal
- `MEMORY.md` — Este archivo de memoria persistente entre sesiones

## 5. Bitacora de Decisiones Tecnicas (ADR Corto)
- **[Fecha Inicial]:** Se instalo el **Mixiuh Labs AI Superpowers Kit v1.0** para eliminar la amnesia entre sesiones y exigir auto-verificacion de codigo.

## 6. Errores Conocidos y Soluciones Aprendidas (No Repetir)
- *(La IA registrara aqui automaticamente cualquier bug dificil que haya resuelto para no volver a cometerlo en futuras sesiones).*
