---
{
  "id": "orca",
  "title": "Orca",
  "type": "tool",
  "tags": [
    "tools",
    "orchestration"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "multi-agent-orchestration",
    "worktree-per-agent",
    "tailscale"
  ],
  "problems": [
    "coordinar agentes",
    "automatizar tareas"
  ],
  "summary": "Entorno para coordinar coding agents, sesiones y árboles de trabajo.",
  "sources": [
    "community",
    "orca"
  ],
  "origin": "community-synthesis"
}
---

# Orca

Entorno para coordinar coding agents, sesiones y árboles de trabajo.

## Qué se observó

Se reportó continuidad de sesiones entre escritorio y celular y uso de orquestación. Otra experiencia volvió a la herramienta nativa porque no encontraba valor adicional.

## Cuándo probar y cómo decidir

Probá dos tareas independientes y la revisión de sus diffs. Compará tiempo de supervisión e integración con dos terminales. Para acceso remoto, verificá autenticación y alcance de red.

## Límites y alternativas

La página del proyecto describe worktrees; estos no son aislamiento de procesos. El marketing de velocidad no se toma como resultado medido.

## Conexiones

`multi-agent-orchestration`, `worktree-per-agent`, `tailscale`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Orca](https://www.onorca.dev/): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
