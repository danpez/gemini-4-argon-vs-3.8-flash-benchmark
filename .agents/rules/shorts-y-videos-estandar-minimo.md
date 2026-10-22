---
trigger: always_on
description: Estandar minimo obligatorio para todos los Shorts, Reels, TikToks y videos 4K60 de Mixiuh Labs (portadas diferenciadas con logo/tiempo/costo, veredicto con telemetria completa y cierre con CTA flotantes animados).
---

# Estandar Minimo de Shorts y Videos 4K60 — Mixiuh Labs

Todo Short, Reel, TikTok y episodio de Mixiuh Labs (`claude-mixiuh-labs` y carpetas de episodios) debe cumplir obligatoriamente con las especificaciones definidas en `/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/AGENTS.md`:

1. **Portada / Gancho (`0.0s .. 1.5s`)**: Placa superior con `EP.XX · PRUEBA 0X/06`, titulo gigante de la prueba con color de acento unico por reto, y chips en ambos paneles mostrando `[RELOJ + MIN]`, `[SPRITE + NOMBRE IA]` y `[MONEDA + $ USD]` desde el segundo `0.0`, mas exportacion automatica de miniaturas PNG en 4K (`2160x3840`).
2. **Veredicto (`short_verdict`)**: Identificador de reto arriba, marcador acumulado (`OPUS [X] - [Y] ARGON`) en `cy = 372`, tarjeta de razon tecnica, barras de tiempo (`MIN`), barras de costo real (`$ USD` + `TOK`) y tarjetas lado a lado de `FPS` + `LINEAS`.
3. **Cierre (`short_endtag`)**: Identificador de reto + marcador arriba, tarjeta flotante de YouTube (`MIXIUH LABS` con boton animado `SUSCRIBETE -> SUSCRITO`), 4 botones flotantes animados (`DALE LIKE`, `SIGUENOS`, `GUARDALO`, `COMPARTE`) y banner flotante de `labs.mixiuh.online`.
