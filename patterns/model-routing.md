---
{
  "id": "model-routing",
  "title": "Routing por tarea, costo y privacidad",
  "type": "pattern",
  "tags": [
    "routing",
    "cost",
    "privacy"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "openrouter",
    "ollama",
    "go-model-router",
    "cross-model-review"
  ],
  "problems": [
    "reducir costo",
    "elegir modelos",
    "modelos intercambiables"
  ],
  "summary": "Asigná modelos según requisitos medidos, con presupuesto y condiciones explícitas de escalamiento.",
  "sources": [
    "community",
    "openrouter"
  ],
  "origin": "community-synthesis"
}
---

# Routing por tarea, costo y privacidad

Asigná modelos según requisitos medidos, con presupuesto y condiciones explícitas de escalamiento.

## Motivación y evidencia

En marzo se relató que inferencia local lenta y llamadas costosas llevaron a probar routing. En octubre se recomendó reservar modelos caros para planificación y revisión. Son estrategias para probar, no rankings permanentes ni ahorros garantizados.

## Implementación y prueba

```json
{"task":"classify","data":"public","budget_usd":0.05,"max_attempts":2,"on_failure":"escalate","fallback_requires_same_privacy":true}
```

Armá un conjunto de casos con respuesta esperada. Medí costo total, latencia y tasa de aprobación. Escalá por fallos verificables, no porque un modelo declare baja confianza. En 429 reintentá con backoff acotado o una alternativa autorizada.

## Trade-offs y alternativa

El costo de revisiones y contexto repetido puede borrar el ahorro. Las políticas de retención deben cumplirse también en fallback. El proyecto existente go-model-router es una implementación específica; su inventario, precios y garantías necesitan revisión independiente.

## Conexiones

`openrouter`, `ollama`, `go-model-router`, `cross-model-review`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Provider logging](https://openrouter.ai/docs/guides/privacy/provider-logging): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
