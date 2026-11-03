---
{
  "id": "worktree-per-agent",
  "title": "Un worktree por cambio concurrente",
  "type": "pattern",
  "tags": [
    "git",
    "parallel",
    "coding"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "multi-agent-orchestration",
    "orca",
    "agentic-coding"
  ],
  "problems": [
    "coding agents en paralelo",
    "conflictos git"
  ],
  "summary": "Separar directorios y ramas reduce colisiones entre agentes que modifican código en paralelo.",
  "sources": [
    "community",
    "git"
  ],
  "origin": "community-synthesis"
}
---

# Un worktree por cambio concurrente

Separar directorios y ramas reduce colisiones entre agentes que modifican código en paralelo.

## Motivación y evidencia

El valor de varias sesiones depende de que no pisen los mismos archivos y de que exista una integración final. Git ofrece árboles de trabajo vinculados con ramas distintas; siguen compartiendo el repositorio subyacente.

## Implementación y prueba

```bash
git worktree add ../feature-search -b feature/search
git worktree add ../feature-map -b feature/map
git worktree list
```

Asigná una tarea y rama a cada sesión. Integra un cambio por vez, revisá el diff y ejecutá pruebas del producto combinado. Para retirar un worktree comprobá primero que su trabajo esté guardado.

## Trade-offs y alternativa

Worktree no es sandbox: los procesos pueden acceder a otros directorios, credenciales y red. El aislamiento de puertos, bases de prueba y secretos se configura aparte. Si las tareas editan el mismo contrato, resolvé dependencias antes de paralelizar.

## Conexiones

`multi-agent-orchestration`, `orca`, `agentic-coding`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Git worktree](https://git-scm.com/docs/git-worktree): Semántica de árboles de trabajo vinculados; no aislamiento de procesos.
