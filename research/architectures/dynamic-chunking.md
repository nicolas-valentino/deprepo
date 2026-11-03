---
{
  "id": "dynamic-chunking",
  "title": "Chunking aprendido y modelos de secuencias",
  "type": "research",
  "tags": [
    "architecture",
    "tokenization",
    "research"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "model-families",
    "long-context-limits",
    "research-with-agents"
  ],
  "problems": [
    "comprender modelos",
    "tokenizacion"
  ],
  "summary": "La segmentación de entrada también puede formar parte de una arquitectura aprendida.",
  "sources": [
    "chunking"
  ],
  "origin": "external-research"
}
---

# Chunking aprendido y modelos de secuencias

La segmentación de entrada también puede formar parte de una arquitectura aprendida.

## Resultado o posición documentada

El paper Dynamic Chunking for End-to-End Hierarchical Sequence Modeling propone segmentación aprendida en una arquitectura jerárquica, en contraste con depender únicamente de tokenización fija como preprocesamiento.

## Interpretación y debate

Fue compartido en 2025 como investigación de arquitectura. No es una receta de fragmentación de documentos para RAG: ambos usan la palabra chunking pero resuelven problemas distintos.

## Aplicación y límites

Antes de aplicar, diferenciá cambios en entrenamiento del modelo de cambios en un pipeline de retrieval. Para un proyecto de agentes suele ser más directo medir recuperación que intentar reproducir una arquitectura de entrenamiento. Los resultados del paper requieren sus condiciones.

## Conexiones

`model-families`, `long-context-limits`, `research-with-agents`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- [Dynamic Chunking for End-to-End Hierarchical Sequence Modeling](https://arxiv.org/abs/2507.07955): Arquitectura y resultados específicos del paper.
