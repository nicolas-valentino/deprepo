---
{
  "id": "openrouter",
  "title": "OpenRouter",
  "type": "tool",
  "tags": [
    "tools",
    "infrastructure"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "model-routing",
    "privacy-by-boundary",
    "context-ownership"
  ],
  "problems": [
    "infraestructura",
    "agentes persistentes"
  ],
  "summary": "Intermediario de acceso a modelos con selección de proveedores y políticas documentadas.",
  "sources": [
    "community",
    "openrouter"
  ],
  "origin": "community-synthesis"
}
---

# OpenRouter

Intermediario de acceso a modelos con selección de proveedores y políticas documentadas.

## Qué se observó

Se usó para probar modelos y balancear costo; también disparó la discusión sobre propiedad del contexto. Routing y memoria son capas diferentes.

## Cuándo probar y cómo decidir

Para un conjunto sintético fijá proveedor, política de datos y fallback. Medí costo total y calidad aprobada; probá explícitamente qué sucede si el proveedor falla.

## Límites y alternativas

No asumas que una sola API key implica una sola política de retención. Consultá condiciones por proveedor y ruta; no transfieras garantías del antiguo catálogo a endpoints actuales.

## Conexiones

`model-routing`, `privacy-by-boundary`, `context-ownership`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Provider logging](https://openrouter.ai/docs/guides/privacy/provider-logging): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
