---
{
  "id": "openevolve",
  "title": "OpenEvolve",
  "type": "tool",
  "tags": [
    "tools",
    "research-tools"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "alphaevolve-research",
    "self-improving-systems",
    "benchmark-hygiene"
  ],
  "problems": [
    "investigacion",
    "mejorar agentes"
  ],
  "summary": "Implementación abierta de búsqueda evolutiva de programas inspirada en enfoques como AlphaEvolve.",
  "sources": [
    "community",
    "openevolve"
  ],
  "origin": "community-synthesis"
}
---

# OpenEvolve

Implementación abierta de búsqueda evolutiva de programas inspirada en enfoques como AlphaEvolve.

## Qué se observó

Fue compartida en mayo de 2025 junto al paper de AlphaEvolve. No se reportó aquí una réplica de los resultados de DeepMind.

## Cuándo probar y cómo decidir

Diseñá un evaluador determinista de corrección y rendimiento sobre una función pequeña. Reservá tests contra sobreajuste y conservá presupuesto de búsqueda.

## Límites y alternativas

Un programa más rápido que falla casos ocultos no es una mejora. Ni compartir una idea arquitectónica ni un nombre similar implica paridad con el sistema original.

## Conexiones

`alphaevolve-research`, `self-improving-systems`, `benchmark-hygiene`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [OpenEvolve](https://github.com/codelion/openevolve): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
