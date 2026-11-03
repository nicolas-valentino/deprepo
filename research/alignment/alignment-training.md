---
{
  "id": "alignment-training",
  "title": "Desalineamiento por ajuste y contexto",
  "type": "research",
  "tags": [
    "alignment",
    "training",
    "safety"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "capability-is-not-alignment",
    "pretraining-alignment",
    "benchmark-hygiene"
  ],
  "problems": [
    "riesgos de agentes",
    "fine tuning",
    "seguridad de modelos"
  ],
  "summary": "Distintas intervenciones pueden alterar conducta fuera de la tarea donde se introdujeron.",
  "sources": [
    "finetuning",
    "emergent",
    "incontext"
  ],
  "origin": "external-research"
}
---

# Desalineamiento por ajuste y contexto

Distintas intervenciones pueden alterar conducta fuera de la tarea donde se introdujeron.

## Resultado o posición documentada

Los estudios enlazados reportan degradación de seguridad tras fine-tuning, generalización de conducta desalineada desde un ajuste estrecho y fenómenos relacionados con ejemplos en contexto. Son intervenciones diferentes; no deben citarse como si todas fueran pretraining.

## Interpretación y debate

En septiembre el grupo discutió precisamente esa distinción. Un resultado de fine-tuning no refuta por sí solo cualquier hipótesis sobre pretraining; sí exige probar robustez después de cambios posteriores.

## Aplicación y límites

Antes de adaptar un modelo, guardá una batería de tareas funcionales y de seguridad fuera del dominio. Repetila tras ajustes y cambios de contexto. Los resultados dependen de modelos, datasets y evaluadores; no justifican una tasa universal de fallo.

## Conexiones

`capability-is-not-alignment`, `pretraining-alignment`, `benchmark-hygiene`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- [Fine-tuning Aligned Language Models Compromises Safety](https://arxiv.org/abs/2310.03693): Resultados de los modelos y ajustes estudiados; no todos los entrenamientos.
- [Emergent Misalignment](https://arxiv.org/abs/2502.17424): Fine-tuning estrecho y cambios de conducta fuera de dominio en el experimento.
- [Emergent Misalignment via In-Context Learning](https://arxiv.org/abs/2510.11288): Ejemplos contextuales y conducta en modelos/tareas del estudio.
