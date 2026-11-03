---
{
  "id": "agents-not-chatbots",
  "title": "Del chatbot al agente",
  "type": "idea",
  "tags": [
    "agents",
    "architecture"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "harness-over-model",
    "bounded-autonomy",
    "build-your-agent"
  ],
  "problems": [
    "automatizar tareas",
    "asistente personal"
  ],
  "summary": "Un agente agrega acciones y realimentación al diálogo; su utilidad depende de completar objetivos verificables.",
  "sources": [
    "community",
    "agents"
  ],
  "origin": "community-synthesis"
}
---

# Del chatbot al agente

Un agente agrega acciones y realimentación al diálogo; su utilidad depende de completar objetivos verificables.

## Aprendizaje de la comunidad

En enero de 2026 el interés pasó del chat a asistentes persistentes; después aparecieron relatos de operación real y de fallos. Una sesión conversacional por sí sola no demuestra autonomía. Separar un workflow de pasos prefijados de un sistema que elige pasos evita comprar complejidad innecesaria.

## Aplicación

Definí una tarea con entrada, resultado observable y condición de parada. Probá primero un flujo determinista; agregá decisión por modelo donde las entradas varíen. Una tarea de clasificación repetitiva puede necesitar un script y una llamada, no un equipo de agentes.

## Límites y posiciones

Cada acción adicional introduce permisos, latencia y posibilidad de error acumulado. Medí finalización correcta, intervenciones y costo por resultado. Los relatos del grupo son experiencias, no una comparación controlada entre productos.

## Conexiones

`harness-over-model`, `bounded-autonomy`, `build-your-agent`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
