---
{
  "id": "wacli",
  "title": "wacli",
  "type": "tool",
  "tags": [
    "tools",
    "infrastructure"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "privacy-by-boundary",
    "permission-enforcement",
    "issue-based-coordination"
  ],
  "problems": [
    "infraestructura",
    "agentes persistentes"
  ],
  "summary": "CLI de WhatsApp que documenta sincronización, búsqueda y envío.",
  "sources": [
    "community",
    "wacli"
  ],
  "origin": "community-synthesis"
}
---

# wacli

CLI de WhatsApp que documenta sincronización, búsqueda y envío.

## Qué se observó

Se compartió como herramienta de acceso al historial. Leer una exportación consentida y conectar una cuenta viva son operaciones diferentes.

## Cuándo probar y cómo decidir

Para construir conocimiento del grupo preferí una exportación fuera del repositorio y síntesis sin atribución. Si evaluás la CLI, usá una cuenta de prueba y el alcance mínimo.

## Límites y alternativas

La herramienta también puede enviar: no es inherentemente de solo lectura. No autorizamos mensajes, extracción de otros grupos ni publicación de teléfonos.

## Conexiones

`privacy-by-boundary`, `permission-enforcement`, `issue-based-coordination`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [wacli](https://github.com/openclaw/wacli): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
