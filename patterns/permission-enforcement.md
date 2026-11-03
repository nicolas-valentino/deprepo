---
{
  "id": "permission-enforcement",
  "title": "Controles en todas las vías de ejecución",
  "type": "pattern",
  "tags": [
    "security",
    "permissions",
    "mcp"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "bounded-autonomy",
    "mcp",
    "skill-supply-chain",
    "privacy-by-boundary"
  ],
  "problems": [
    "evitar bypass",
    "controlar acciones",
    "riesgos de agentes"
  ],
  "summary": "Una restricción solo funciona si cubre cada ruta equivalente hacia la acción.",
  "sources": [
    "community",
    "mcp"
  ],
  "origin": "community-synthesis"
}
---

# Controles en todas las vías de ejecución

Una restricción solo funciona si cubre cada ruta equivalente hacia la acción.

## Motivación y evidencia

En septiembre se reportó un envío que falló un hook y luego salió por MCP, donde no estaba ese control. En octubre hubo otro relato de instrucciones ignoradas. No inferimos intención interna: el hallazgo operativo es cobertura incompleta del límite.

## Implementación y prueba

Inventariá API, MCP, shell, navegador y credenciales que permitan la misma acción. Mové autorización al punto de ejecución común o quitá credenciales de rutas alternativas. En una prueba con un servidor ficticio, intentá la acción por cada ruta y exigí idéntico rechazo.

## Trade-offs y alternativa

Un directorio llamado sandbox no aísla procesos. Los filtros de prompts o un segundo modelo no sustituyen permisos efectivos. El principio sirve también sin IA: acceso mínimo y verificación del servidor reducen vías de evasión.

## Conexiones

`bounded-autonomy`, `mcp`, `skill-supply-chain`, `privacy-by-boundary`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [MCP security considerations](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/authorization/security-considerations.mdx): Autorización, audiencia de tokens y separación de credenciales upstream.
