---
{
  "id": "n8n",
  "title": "n8n",
  "type": "tool",
  "tags": [
    "tools",
    "orchestration"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "persistent-agent-operations",
    "issue-based-coordination",
    "minimize-meta-work"
  ],
  "problems": [
    "coordinar agentes",
    "automatizar tareas"
  ],
  "summary": "Plataforma para organizar automatizaciones y conexiones entre servicios.",
  "sources": [
    "community",
    "n8n"
  ],
  "origin": "community-synthesis"
}
---

# n8n

Plataforma para organizar automatizaciones y conexiones entre servicios.

## Qué se observó

Apareció entre herramientas de automatización. La mención no documenta por sí sola una receta del grupo ni una ventaja frente a código.

## Cuándo probar y cómo decidir

Empezá por un trigger y una acción sobre una cuenta de prueba; agregá reintentos e idempotencia. Medí mantenimiento del workflow y posibilidad de exportarlo.

## Límites y alternativas

Revisá licencia, credenciales, hosting y logs por separado. No asumimos que self-hosting elimine llamadas a terceros ni que toda ejecución sea determinista.

## Conexiones

`persistent-agent-operations`, `issue-based-coordination`, `minimize-meta-work`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [n8n](https://docs.n8n.io/): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
