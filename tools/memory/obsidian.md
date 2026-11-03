---
{
  "id": "obsidian",
  "title": "Obsidian",
  "type": "tool",
  "tags": [
    "tools",
    "memory"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "context-ownership",
    "portable-memory",
    "separate-human-agent-memory"
  ],
  "problems": [
    "memoria persistente",
    "recuperar conocimiento"
  ],
  "summary": "Aplicación de notas cuyo vault contiene archivos de texto Markdown locales.",
  "sources": [
    "community",
    "obsidian"
  ],
  "origin": "community-synthesis"
}
---

# Obsidian

Aplicación de notas cuyo vault contiene archivos de texto Markdown locales.

## Qué se observó

Se usó para notas, enlaces y vistas de conocimiento. El grupo corrigió la idea de que la licencia propietaria del editor impide conservar los archivos.

## Cuándo probar y cómo decidir

Abrí una copia del vault con otro editor y buscá notas sin plugins. Probá exportar adjuntos y enlaces; un cambio de aplicación no debería borrar el registro durable.

## Límites y alternativas

Markdown portable no garantiza portabilidad de plugins, consultas o vistas. Si el agente envía fragmentos a una API, esos fragmentos salen de tu equipo aunque el vault permanezca local.

## Conexiones

`context-ownership`, `portable-memory`, `separate-human-agent-memory`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [How Obsidian stores data](https://obsidian.md/help/Files%2Band%2Bfolders/How%2BObsidian%2Bstores%2Bdata): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
