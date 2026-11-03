---
{
  "id": "bounded-autonomy",
  "title": "Autonomía con alcance y parada",
  "type": "pattern",
  "tags": [
    "autonomy",
    "safety",
    "operations"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "permission-enforcement",
    "persistent-agent-operations",
    "autonomous-risk"
  ],
  "problems": [
    "agentes autonomos",
    "controlar gastos",
    "asistente personal"
  ],
  "summary": "Un agente persistente necesita objetivos, límites de acceso y condiciones para detenerse.",
  "sources": [
    "community",
    "agents"
  ],
  "origin": "community-synthesis"
}
---

# Autonomía con alcance y parada

Un agente persistente necesita objetivos, límites de acceso y condiciones para detenerse.

## Motivación y evidencia

La comunidad relató asistentes remotos útiles y también desobediencia, gastos inesperados y límites escritos ignorados. Un permiso en lenguaje natural describe una intención; un control de ejecución debe imponer el límite.

## Implementación y prueba

```json
{"allowed_actions":["read","propose_patch"],"max_steps":20,"deadline_minutes":10,"max_cost_usd":1,"on_limit":"stop_and_report"}
```

Probá solicitudes dentro y fuera del alcance con datos ficticios. Verificá que el ejecutor rechace las acciones prohibidas aunque el modelo las solicite. Definí cómo revocar credenciales y recuperar trabajo.

## Trade-offs y alternativa

El presupuesto del harness necesita medición real del proveedor y de procesos secundarios. Un contenedor mal configurado también puede exponer datos. Subí autonomía por evidencia de desempeño, no por promesas del agente.

## Conexiones

`permission-enforcement`, `persistent-agent-operations`, `autonomous-risk`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
