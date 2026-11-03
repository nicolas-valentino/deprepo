---
{
  "id": "harness-over-model",
  "title": "Modelo, harness y sistema completo",
  "type": "idea",
  "tags": [
    "harness",
    "architecture",
    "evaluation"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "agents-not-chatbots",
    "model-routing",
    "harness2"
  ],
  "problems": [
    "elegir herramientas",
    "mejorar fiabilidad"
  ],
  "summary": "El sistema que rodea al modelo puede cambiar tanto la experiencia como la elección del modelo.",
  "sources": [
    "community",
    "agents"
  ],
  "origin": "community-synthesis"
}
---

# Modelo, harness y sistema completo

El sistema que rodea al modelo puede cambiar tanto la experiencia como la elección del modelo.

## Aprendizaje de la comunidad

En octubre hubo un desacuerdo terminológico: algunos llamaban harness a la aplicación; otros, a la personalización agregada. Usamos una definición operativa: instrucciones, herramientas, memoria, políticas y ciclo de ejecución alrededor del modelo. La aplicación puede incluir ese sistema y también permitir extenderlo.

## Aplicación

Antes de cambiar de modelo, localizá el fallo: falta de contexto, herramienta ambigua, acceso ausente, criterio de aceptación o razonamiento. Compará el mismo modelo con un cambio de harness y el mismo harness con otro modelo.

## Límites y posiciones

La frase del título es una heurística, no una ley de superioridad. Un modelo mejor puede absorber complejidad antes resuelta con prompts; un harness sofisticado tampoco reemplaza criterio de negocio. Evitá benchmarks que cambien simultáneamente modelo, contexto y permisos.

## Conexiones

`agents-not-chatbots`, `model-routing`, `harness2`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
