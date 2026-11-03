---
{
  "id": "agentic-coding",
  "title": "Desarrollar con varios agentes y una integración responsable",
  "type": "guide",
  "tags": [
    "coding",
    "parallel",
    "git"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "worktree-per-agent",
    "multi-agent-orchestration",
    "cross-model-review",
    "benchmark-hygiene"
  ],
  "problems": [
    "desarrollo de software",
    "coding agents en paralelo",
    "coordinar agentes"
  ],
  "summary": "La unidad de trabajo es un cambio verificable; el resultado es el producto integrado.",
  "sources": [
    "community",
    "git",
    "agents"
  ],
  "origin": "editorial-guide"
}
---

# Desarrollar con varios agentes y una integración responsable

La unidad de trabajo es un cambio verificable; el resultado es el producto integrado.

## Escenario B: preparar

Elegí dos cambios que no compartan contrato. Escribí objetivo, rutas permitidas, no objetivos, pruebas y presupuesto. Si comparten una API, acordá primero su forma y secuenciá dependencias. Usá una rama y worktree por cambio, con credenciales de prueba.

## Ejecutar y revisar

El responsable de cada cambio entrega diff, pruebas, decisiones y pendientes. Un revisor recibe el problema y verifica la solución, no solo el resumen del autor. La segunda familia de modelos es opcional; una prueba determinista suele aportar más que otra opinión.

## Integrar

Integrá primero un cambio y probá. Incorporá el siguiente y ejecutá los flujos que cruzan ambos. Comprobá estado persistido, API y UI donde corresponda. Una prueba por componente no valida el producto completo. Evitá contar líneas de código como productividad.

## Aceptación y recuperación

Medí tiempo hasta aceptación, regresiones, costo y minutos humanos. Ante conflicto revisá contratos antes de pedir más agentes. Conservá ramas hasta verificar el resultado; retirarlas requiere comprobar que el trabajo esté guardado. Worktrees no aíslan red ni secretos.

## Conexiones

`worktree-per-agent`, `multi-agent-orchestration`, `cross-model-review`, `benchmark-hygiene`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Git worktree](https://git-scm.com/docs/git-worktree): Semántica de árboles de trabajo vinculados; no aislamiento de procesos.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
