---
{
  "id": "forgejo",
  "title": "Forgejo",
  "type": "tool",
  "tags": [
    "tools",
    "infrastructure"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "issue-based-coordination",
    "persistent-agent-operations",
    "permission-enforcement"
  ],
  "problems": [
    "infraestructura",
    "agentes persistentes"
  ],
  "summary": "Plataforma para alojar repositorios y organizar colaboración mediante issues y eventos.",
  "sources": [
    "community",
    "forgejo"
  ],
  "origin": "community-synthesis"
}
---

# Forgejo

Plataforma para alojar repositorios y organizar colaboración mediante issues y eventos.

## Qué se observó

Se describió un servidor propio con issues como pedidos entre agentes y avisos por webhook. El registro durable sobrevivía a notificaciones perdidas.

## Cuándo probar y cómo decidir

Probá un repo sintético, un issue y un webhook firmado. Hacé que el receptor relea el issue con su propia credencial y deduplique eventos.

## Límites y alternativas

Self-hosting agrega backups, actualizaciones y operación. Una instancia propia no convierte el contenido de un issue en instrucciones confiables.

## Conexiones

`issue-based-coordination`, `persistent-agent-operations`, `permission-enforcement`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Forgejo](https://forgejo.org/docs/latest/): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
