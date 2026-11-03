---
{
  "id": "langgraph",
  "title": "LangGraph",
  "type": "tool",
  "tags": [
    "tools",
    "orchestration"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "persistent-agent-operations",
    "multi-agent-orchestration",
    "build-your-agent"
  ],
  "problems": [
    "coordinar agentes",
    "automatizar tareas"
  ],
  "summary": "Framework para construir agentes y flujos con estado.",
  "sources": [
    "community",
    "langgraph"
  ],
  "origin": "community-synthesis"
}
---

# LangGraph

Framework para construir agentes y flujos con estado.

## Qué se observó

Se compartió formación sobre agentes profundos; no se obtuvo del chat una comparación controlada con otros frameworks. Su inclusión facilita investigar una opción de implementación.

## Cuándo probar y cómo decidir

Elegilo si necesitás estado explícito, reanudación y ramas de ejecución. Dibujá primero estados y transiciones y probá una interrupción con una acción sintética.

## Límites y alternativas

Un framework no define por vos política de permisos, calidad ni idempotencia. Para una tarea lineal puede ser suficiente un script.

## Conexiones

`persistent-agent-operations`, `multi-agent-orchestration`, `build-your-agent`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [LangGraph](https://github.com/langchain-ai/langgraph): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
