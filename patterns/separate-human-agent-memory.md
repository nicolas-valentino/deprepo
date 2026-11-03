---
{
  "id": "separate-human-agent-memory",
  "title": "Memoria humana y memoria operativa separadas",
  "type": "pattern",
  "tags": [
    "memory",
    "knowledge",
    "privacy"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "portable-memory",
    "hindsight",
    "gbrain",
    "collectors-fallacy"
  ],
  "problems": [
    "notas legibles",
    "inspeccionar memoria"
  ],
  "summary": "Un espacio personal de conocimiento y el registro operativo del asistente tienen necesidades distintas.",
  "sources": [
    "community",
    "hindsight"
  ],
  "origin": "community-synthesis"
}
---

# Memoria humana y memoria operativa separadas

Un espacio personal de conocimiento y el registro operativo del asistente tienen necesidades distintas.

## Motivación y evidencia

En junio se debatió mezclar todo en Markdown frente a mantener notas personales y memoria vectorizada por separado. Se propuso generar una vista legible de lo que aprendía el agente para poder corregirlo. Esto es una decisión de diseño, no la obligación de usar dos bases.

## Implementación y prueba

Conservá notas aprobadas en una carpeta estable. Permití que el agente proponga nuevos recuerdos en un área de pendientes con su fuente. Promové solo hechos confirmados. Probá borrar un recuerdo y verificá su ausencia en búsquedas, cachés y resúmenes.

## Trade-offs y alternativa

Dos espacios pueden divergir y exigen una regla de promoción. Para un asistente pequeño puede bastar un archivo con secciones y permisos diferentes. Una base vectorial no impide construir una interfaz legible; la experiencia del grupo no define todos los productos.

## Conexiones

`portable-memory`, `hindsight`, `gbrain`, `collectors-fallacy`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Hindsight](https://github.com/vectorize-io/hindsight): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
