---
{
  "id": "cross-model-review",
  "title": "Revisión independiente entre modelos",
  "type": "pattern",
  "tags": [
    "review",
    "evaluation",
    "models"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "benchmark-hygiene",
    "multi-agent-orchestration",
    "evidence-before-hype"
  ],
  "problems": [
    "evaluacion cruzada",
    "validar planes",
    "reducir errores"
  ],
  "summary": "Una segunda perspectiva puede detectar errores si usa criterios y evidencias independientes.",
  "sources": [
    "community",
    "agents"
  ],
  "origin": "community-synthesis"
}
---

# Revisión independiente entre modelos

Una segunda perspectiva puede detectar errores si usa criterios y evidencias independientes.

## Motivación y evidencia

El grupo reportó rondas entre planificador y revisor de otra familia, y luego revisiones cruzadas del resultado. Son experiencias útiles para diseñar un experimento. Acuerdo entre modelos no equivale a verdad: pueden compartir sesgos y datos.

## Implementación y prueba

Pasá al revisor el problema, restricciones y artefactos; pedí fallos concretos con evidencia y prueba que los detecte. Para reducir anclaje, hacé que proponga primero su criterio sin leer la conclusión del autor. Limitá a dos rondas y llevá desacuerdos al criterio externo.

## Trade-offs y alternativa

No uses votación para validar hechos científicos ni corrección de programas. Preferí ejecución, fuentes originales y revisión de dominio cuando existan. Compará contra una revisión con el mismo modelo para saber si el costo adicional aporta.

## Conexiones

`benchmark-hygiene`, `multi-agent-orchestration`, `evidence-before-hype`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
