---
{
  "id": "benchmark-hygiene",
  "title": "Evaluaciones comparables y regresiones",
  "type": "pattern",
  "tags": [
    "evaluation",
    "benchmarks",
    "testing"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "evidence-before-hype",
    "cross-model-review",
    "long-context-limits"
  ],
  "problems": [
    "comparar modelos",
    "medir calidad",
    "evaluacion cruzada"
  ],
  "summary": "Compará tareas y resultados bajo condiciones registradas, con casos que el sistema no vio al ajustarse.",
  "sources": [
    "community",
    "agents"
  ],
  "origin": "community-synthesis"
}
---

# Evaluaciones comparables y regresiones

Compará tareas y resultados bajo condiciones registradas, con casos que el sistema no vio al ajustarse.

## Motivación y evidencia

Preferencias entre modelos cambiaban según el proyecto. También se reportó reducir suites conservando cobertura, con una advertencia correcta: mantener cobertura no conserva necesariamente detección de bugs. Un benchmark debe declarar qué mide y qué deja afuera.

## Implementación y prueba

Guardá casos, versión, prompts, tools, límite de tokens, costo y repeticiones. Separá aceptación funcional de seguridad. Incluí errores históricos, casos extremos y regresiones reservadas. Reportá fallos y variabilidad, no solo la mejor ejecución.

## Trade-offs y alternativa

El propio agente no debe inventar la respuesta esperada de la prueba que pasa. Una mejora de benchmark puede no transferirse al trabajo real. Para investigación, verificá el alcance del paper antes de traducirlo a una decisión práctica.

## Conexiones

`evidence-before-hype`, `cross-model-review`, `long-context-limits`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
