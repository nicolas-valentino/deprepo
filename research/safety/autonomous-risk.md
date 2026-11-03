---
{
  "id": "autonomous-risk",
  "title": "Capacidad de autorreplicación y límites de las evaluaciones",
  "type": "research",
  "tags": [
    "autonomy",
    "security",
    "safety"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "bounded-autonomy",
    "permission-enforcement",
    "persistent-agent-operations"
  ],
  "problems": [
    "riesgos de agentes",
    "agentes autonomos",
    "autorreplicacion"
  ],
  "summary": "Una evaluación controlada de replicación informa sobre capacidades y condiciones, no sobre un incidente real.",
  "sources": [
    "replication"
  ],
  "origin": "external-research"
}
---

# Capacidad de autorreplicación y límites de las evaluaciones

Una evaluación controlada de replicación informa sobre capacidades y condiciones, no sobre un incidente real.

## Resultado o posición documentada

El informe de Anthropic estudia la posibilidad de replicación de modelos fuera de un datacenter bajo configuraciones y recursos específicos. Es un reporte de capacidad y mitigaciones de su equipo de evaluación.

## Interpretación y debate

En el grupo aparecieron relatos de modelos que escapan o infectan infraestructura. No los publicamos como incidentes confirmados sin evidencia primaria del caso. Capacidad, propensión e incidente observado son categorías diferentes.

## Aplicación y límites

La aplicación defensiva es controlar credenciales, ejecución y acceso de red, además de monitorear acciones. No hace falta reproducir una cadena de explotación para extraer el principio de mínimo privilegio. Un ensayo no determina una probabilidad universal de catástrofe.

## Conexiones

`bounded-autonomy`, `permission-enforcement`, `persistent-agent-operations`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- [AI models may be capable of self-replicating](https://www.anthropic.com/research/self-replicating-ai): Evaluación controlada de capacidad; no prueba de infección autónoma en el mundo.
