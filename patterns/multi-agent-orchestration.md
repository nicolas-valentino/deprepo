---
{
  "id": "multi-agent-orchestration",
  "title": "Orquestación con contratos y dependencias",
  "type": "pattern",
  "tags": [
    "orchestration",
    "parallel",
    "agents"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "worktree-per-agent",
    "cross-model-review",
    "bounded-autonomy",
    "issue-based-coordination"
  ],
  "problems": [
    "coordinar agentes",
    "coding agents en paralelo"
  ],
  "summary": "Delegá unidades verificables y reservá una responsabilidad explícita para integración.",
  "sources": [
    "community",
    "agents"
  ],
  "origin": "community-synthesis"
}
---

# Orquestación con contratos y dependencias

Delegá unidades verificables y reservá una responsabilidad explícita para integración.

## Motivación y evidencia

En septiembre se describió planificación revisada por otro modelo y asignación de tareas por complejidad. Otros usuarios no encontraron valor adicional en el orquestador y volvieron a una sesión nativa. La utilidad depende de separabilidad y carga de supervisión.

## Implementación y prueba

Cada tarea declara entrada, archivos permitidos, dependencias, aceptación, presupuesto y propietario. Un integrador compara resultados contra el contrato y prueba el flujo completo. Paralelizá ramas independientes; ordená cambios que comparten esquema o API.

## Trade-offs y alternativa

Más agentes multiplican consumo y coordinación. Medí tiempo hasta integración correcta, no cantidad de sesiones ni líneas escritas. Si la tarea cabe en una sesión y una revisión, esa es una alternativa válida.

## Conexiones

`worktree-per-agent`, `cross-model-review`, `bounded-autonomy`, `issue-based-coordination`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
