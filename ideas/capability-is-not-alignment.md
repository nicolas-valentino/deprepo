---
{
  "id": "capability-is-not-alignment",
  "title": "Capacidad y conducta deseada requieren evaluaciones separadas",
  "type": "idea",
  "tags": [
    "alignment",
    "safety",
    "evaluation"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "alignment-training",
    "permission-enforcement",
    "autonomous-risk"
  ],
  "problems": [
    "riesgos de agentes",
    "validar seguridad"
  ],
  "summary": "Resolver tareas difíciles no demuestra obediencia, seguridad ni alineamiento general.",
  "sources": [
    "community",
    "agents"
  ],
  "origin": "community-synthesis"
}
---

# Capacidad y conducta deseada requieren evaluaciones separadas

Resolver tareas difíciles no demuestra obediencia, seguridad ni alineamiento general.

## Aprendizaje de la comunidad

En mayo y septiembre se discutió si mejores capacidades resolverían alignment. Unos relatos mostraban tareas útiles; otros, límites incumplidos. Es importante distinguir errores de implementación, objetivos mal especificados y desalineamiento deliberado antes de atribuir una causa.

## Aplicación

Medí éxito de la tarea y cumplimiento de restricciones por separado. Un resultado funcional obtenido por una vía prohibida debe fallar la evaluación. Registrá las condiciones del experimento y evaluá cambios de modelo, memoria o tools.

## Límites y posiciones

Los estudios de entrenamiento muestran fallos en contextos delimitados; no prueban que todo modelo sea inevitablemente peligroso ni que el problema esté resuelto. Un protocolo reduce riesgo y debe revisarse; no constituye una garantía universal.

## Conexiones

`alignment-training`, `permission-enforcement`, `autonomous-risk`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
