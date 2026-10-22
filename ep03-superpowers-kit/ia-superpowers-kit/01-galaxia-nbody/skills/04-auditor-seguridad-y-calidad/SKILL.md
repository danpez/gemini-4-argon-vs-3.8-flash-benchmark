---
name: 04-auditor-seguridad-y-calidad
description: Checklist automatico de seguridad, tipado estricto, manejo de errores y prevencion de fuga de credenciales antes de hacer commit o desplegar a produccion.
---

# Skill 04: Auditor de Seguridad y Calidad de Codigo

## Cuando activar esta habilidad
Activa esta habilidad antes de realizar cualquier `git commit`, abrir un Pull Request o dar por cerrado un modulo de backend/frontend.

## Checklist de Verificacion Obligatoria
1. **Cero Secretos en Codigo Fuente:**
   - Verifica que ninguna API Key (`sk-...`, `AIza...`, tokens de servicio) este escrita en duro. Todo secreto debe leerse de variables de entorno (`.env.local`) ignoradas en `.gitignore`.
2. **Sanitizacion y Seguridad DOM / SQL:**
   - Evita el uso inseguro de `innerHTML` con datos de usuario no escapados. Usa parametros preparados en consultas de base de datos.
3. **Manejo Defensivo de Errores:**
   - Envuelve llamadas de red (`fetch`), lectura de archivos y parseo de JSON (`JSON.parse`) o `localStorage` en bloques `try/catch` con estados de recuperacion claros para el usuario.
4. **Limpieza de Recursos:**
   - Asegura que todo `addEventListener`, `setInterval`, `requestAnimationFrame` o conexion WebSocket tenga su correspondiente limpieza (`removeEventListener`, `clearInterval`, `cancelAnimationFrame`) al desmontar.
