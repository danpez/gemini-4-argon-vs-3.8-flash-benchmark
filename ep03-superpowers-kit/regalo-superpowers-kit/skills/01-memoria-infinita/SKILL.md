---
name: 01-memoria-infinita
description: Elimina la amnesia entre sesiones leyendo y actualizando un archivo MEMORY.md estructurado y ligero sin gastar tokens innecesarios.
---

# Skill 01: Memoria Infinita Local (Zero-Amnesia Protocol)

## Cuando activar esta habilidad
Activa esta habilidad al inicio de cualquier sesion de trabajo nueva y justo antes de concluir una tarea donde se haya tomado una decision arquitectonica o resuelto un bug importante.

## Flujo de Trabajo Obligatorio
1. **Lectura Inicial (`Boot`):**
   - Verifica si existe `MEMORY.md` en la raiz del espacio de trabajo.
   - Si no existe, crealo automaticamente escaneando `package.json`, `pyproject.toml`, `pubspec.yaml` o la estructura de directorios.
2. **Escritura Quirurgica (`Commit to Memory`):**
   - Nunca conviertas `MEMORY.md` en un volcado largo de logs. Mantelo siempre por debajo de 150 lineas.
   - Cuando resuelvas un bug complejo (por ejemplo, un error de CORS, un uniforme GLSL roto o una condicion de carrera), agrega 1 linea en la seccion `Errores Conocidos y Soluciones Aprendidas` con el formato:
     `- [Archivo/Modulo]: Causa raiz -> Solucion aplicada.`
