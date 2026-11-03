---
{
  "id": "long-context-limits",
  "title": "Contexto largo no es recuperación perfecta",
  "type": "research",
  "tags": [
    "context",
    "retrieval",
    "evaluation"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "portable-memory",
    "collectors-fallacy",
    "benchmark-hygiene"
  ],
  "problems": [
    "recuperar conocimiento",
    "memoria persistente",
    "contexto largo"
  ],
  "summary": "La ubicación de información relevante puede afectar su uso en una ventana de contexto.",
  "sources": [
    "context"
  ],
  "origin": "external-research"
}
---

# Contexto largo no es recuperación perfecta

La ubicación de información relevante puede afectar su uso en una ventana de contexto.

## Resultado o posición documentada

Lost in the Middle evalúa preguntas sobre múltiples documentos y recuperación de claves. Encuentra sensibilidad a la posición de información relevante en los modelos y tareas del estudio.

## Interpretación y debate

El grupo lo relacionó con datos enterrados en sesiones extensas. La conclusión útil es probar recuperación, no afirmar que todo modelo actual olvida exactamente la mitad de su contexto.

## Aplicación y límites

Compará la misma pregunta con el dato al inicio, medio y final; repetí con distractores. Para producción recuperá fragmentos relevantes y sus fuentes. El resultado histórico no fija capacidades de todos los modelos de 2026.

## Conexiones

`portable-memory`, `collectors-fallacy`, `benchmark-hygiene`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- [Lost in the Middle](https://arxiv.org/abs/2307.03172): Sensibilidad a posición en tareas/modelos estudiados; no cifra universal de memoria.
