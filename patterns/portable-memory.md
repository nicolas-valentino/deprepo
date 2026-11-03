---
{
  "id": "portable-memory",
  "title": "Memoria durable e índices reemplazables",
  "type": "pattern",
  "tags": [
    "memory",
    "portability",
    "asistente personal"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "context-ownership",
    "separate-human-agent-memory",
    "build-your-agent"
  ],
  "problems": [
    "memoria persistente",
    "modelos intercambiables"
  ],
  "summary": "Separá el conocimiento confirmado de las estructuras que utiliza cada modelo para recuperarlo.",
  "sources": [
    "community",
    "agents"
  ],
  "origin": "community-synthesis"
}
---

# Memoria durable e índices reemplazables

Separá el conocimiento confirmado de las estructuras que utiliza cada modelo para recuperarlo.

## Motivación y evidencia

Guardar hechos y decisiones con fecha, fuente, nivel de confianza y corrección humana permite reconstruir un índice sin perder significado. La comunidad probó vaults compartidos y servicios de memoria; no hay un backend universalmente superior.

## Implementación y prueba

```text
knowledge/decisions.md   # decisiones confirmadas por la persona
knowledge/facts.json     # hechos con fuente y fecha
derived/                # índice reconstruible, fuera del registro durable
```

Prueba: agregá un hecho ficticio, recuperalo con dos lectores, corregilo y verificá que ninguno siga devolviendo la versión vieja. Para evaluar modelos usá el mismo conjunto de preguntas.

## Trade-offs y alternativa

Los resúmenes pierden matices y los embeddings pueden requerir reconstrucción al cambiar de modelo. Una alternativa simple es búsqueda literal sobre archivos pequeños. Separá permiso de lectura de permiso para reescribir hechos.

## Conexiones

`context-ownership`, `separate-human-agent-memory`, `build-your-agent`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
