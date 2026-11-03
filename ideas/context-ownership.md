---
{
  "id": "context-ownership",
  "title": "El contexto debe poder cambiar de proveedor",
  "type": "idea",
  "tags": [
    "memory",
    "portability",
    "privacy"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "portable-memory",
    "obsidian",
    "logseq",
    "openrouter"
  ],
  "problems": [
    "memoria persistente",
    "modelos intercambiables",
    "evitar dependencia"
  ],
  "summary": "Separar conocimiento durable del proveedor permite cambiar modelos sin reconstruir la historia del usuario.",
  "sources": [
    "community",
    "obsidian"
  ],
  "origin": "community-synthesis"
}
---

# El contexto debe poder cambiar de proveedor

Separar conocimiento durable del proveedor permite cambiar modelos sin reconstruir la historia del usuario.

## Aprendizaje de la comunidad

En marzo se pidió para el contexto una portabilidad comparable a elegir modelos. En agosto se discutió file over app: importa poder recuperar y migrar el contenido, además de la licencia del editor. La afirmación de que cerrar Obsidian haría perder automáticamente los Markdown fue discutida; sus notas locales son archivos.

## Aplicación

Guardá hechos confirmados, decisiones y fuentes en un formato exportable. Separá el registro durable de los índices derivados, que se pueden reconstruir. Hacé una prueba de restauración en otro lector y con otro modelo.

## Límites y posiciones

Propiedad local no implica privacidad completa: al recuperar notas y enviarlas a una API se comparte su contenido. Los plugins y sincronizadores agregan accesos. Exigí exportación verificable, borrado y trazabilidad, no solo el rótulo local.

## Conexiones

`portable-memory`, `obsidian`, `logseq`, `openrouter`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [How Obsidian stores data](https://obsidian.md/help/Files%2Band%2Bfolders/How%2BObsidian%2Bstores%2Bdata): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
