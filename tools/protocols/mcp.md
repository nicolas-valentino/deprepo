---
{
  "id": "mcp",
  "title": "Model Context Protocol",
  "type": "tool",
  "tags": [
    "tools",
    "protocols"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "permission-enforcement",
    "privacy-by-boundary",
    "bounded-autonomy"
  ],
  "problems": [
    "integraciones",
    "tools"
  ],
  "summary": "Protocolo para conectar aplicaciones de IA con herramientas y fuentes externas.",
  "sources": [
    "community",
    "mcp"
  ],
  "origin": "community-synthesis"
}
---

# Model Context Protocol

Protocolo para conectar aplicaciones de IA con herramientas y fuentes externas.

## Qué se observó

Se discutió como capa para incorporar servicios, pero también apareció como vía alternativa que eludió un control presente en otra API. Conectar no es autorizar todo.

## Cuándo probar y cómo decidir

Habilitá primero una herramienta de lectura. Verificá qué identidad usa y qué recursos puede acceder. Mantené autorización en el ejecutor y probá equivalentes de una acción por todas las rutas.

## Límites y alternativas

La especificación documenta validación de audiencia y separación de tokens upstream. No afirma que un servidor desconocido sea seguro; inspeccioná implementación y permisos.

## Conexiones

`permission-enforcement`, `privacy-by-boundary`, `bounded-autonomy`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [MCP security considerations](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/authorization/security-considerations.mdx): Autorización, audiencia de tokens y separación de credenciales upstream.
