---
name: 05-automatizador-productividad
description: Flujos rapidos de 1 comando para auditar un repositorio desconocido (/brief), encontrar bugs ocultos (/audit) y empaquetar entregas listas para produccion (/ship).
---

# Skill 05: Automatizador de Productividad en 1 Comando

## Comandos de Flujo Rapido

### 1. Modo `/brief` (Radiografia Instantanea de Proyecto)
Cuando el usuario pida analizar o entender un repositorio:
1. Escanea la estructura de carpetas (ignorando `node_modules`, `.git`, `.venv`, `dist`).
2. Identifica el punto de entrada, el stack, los scripts de ejecucion y la arquitectura de datos.
3. Genera o actualiza `MEMORY.md` y presenta un resumen ejecutivo de maximo 15 lineas.

### 2. Modo `/audit` (Caza Automatica de Bugs y Cuellos de Botella)
Cuando el usuario pida auditar el proyecto:
1. Busca promesas sin `await`, variables no utilizadas, bucles costosos y errores de consola en el navegador.
2. Entrega una tabla priorizada por severidad (`CRITICO`, `ALTO`, `MEDIO`) con el archivo y linea exactos, y aplica las correcciones seguras de inmediato.

### 3. Modo `/ship` (Empaquetado y Verificacion Pre-Vuelo)
Antes de publicar o subir cambios:
1. Ejecuta el build/tests del proyecto.
2. Verifica que `git status` no incluya archivos temporales ni credenciales.
3. Actualiza `MEMORY.md` con los cambios de la sesion.
