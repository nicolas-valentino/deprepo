---
{
  "id": "tailscale",
  "title": "Tailscale",
  "type": "tool",
  "tags": [
    "tools",
    "infrastructure"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "persistent-agent-operations",
    "orca",
    "privacy-by-boundary"
  ],
  "problems": [
    "infraestructura",
    "agentes persistentes"
  ],
  "summary": "Herramientas de red privada para conectar equipos y servicios con control de acceso.",
  "sources": [
    "community",
    "tailscale"
  ],
  "origin": "community-synthesis"
}
---

# Tailscale

Herramientas de red privada para conectar equipos y servicios con control de acceso.

## Qué se observó

Se reportó una conexión remota más estable al usarla con sesiones móviles de Orca. Es una experiencia de una red concreta, no garantía de latencia universal.

## Cuándo probar y cómo decidir

Definí quién puede acceder al host y a qué puertos. Probá desde un usuario permitido y otro rechazado; mantené autenticación de la aplicación además del acceso de red.

## Límites y alternativas

Una red privada no controla qué archivos puede leer un agente dentro del equipo. Revisá ACL, identidad del dispositivo y revocación por separado.

## Conexiones

`persistent-agent-operations`, `orca`, `privacy-by-boundary`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Tailscale](https://tailscale.com/docs): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
