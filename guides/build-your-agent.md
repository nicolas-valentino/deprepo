---
{
  "id": "build-your-agent",
  "title": "Construir un asistente con memoria portable",
  "type": "guide",
  "tags": [
    "assistant",
    "memory",
    "portability"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "portable-memory",
    "model-routing",
    "bounded-autonomy",
    "separate-human-agent-memory"
  ],
  "problems": [
    "asistente personal",
    "memoria persistente",
    "modelos intercambiables"
  ],
  "summary": "Empezá por una tarea recurrente, memoria corregible y permisos de lectura.",
  "sources": [
    "community",
    "agents"
  ],
  "origin": "editorial-guide"
}
---

# Construir un asistente con memoria portable

Empezá por una tarea recurrente, memoria corregible y permisos de lectura.

## Escenario A: diseño mínimo

Objetivo: un asistente recuerda preferencias y cambia de modelo sin perderlas. Definí qué hechos son explícitos y cuáles inferidos. Usá un registro durable con fuente, fecha y estado; elegí índice reemplazable. Mantené tareas operativas fuera del conocimiento confirmado.

## Secuencia reproducible

1. Creá tres preferencias ficticias en un archivo local.
2. Pedí recuperar cada una con variantes de la pregunta.
3. Cambiá el lector o modelo sin modificar el registro.
4. Corregí una preferencia y eliminá otra.
5. Reconstruí el índice y repetí las consultas.
6. Revisá que no aparezcan datos viejos ni inferencias como hechos.

Para hacerlo sin APIs podés empezar con búsqueda literal; luego comparás recuperación semántica.

## Elección y controles

Evaluá Hermes, OpenClaw o un ciclo propio según tus necesidades, sin instalar los tres. Elegí Obsidian/Logseq si también necesitás notas humanas; Hindsight u otra memoria si el caso justifica su operación. Antes de usar datos reales verificá exportación, permisos y destino de fragmentos.

## Aceptación y rollback

Aceptá solo si los hechos se recuperan, corrigen y eliminan con trazabilidad, y el costo cabe en presupuesto. Restaurá el registro durable y reconstruí derivados si falla. Que una respuesta recuerde algo una vez no prueba persistencia ni portabilidad.

## Conexiones

`portable-memory`, `model-routing`, `bounded-autonomy`, `separate-human-agent-memory`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
