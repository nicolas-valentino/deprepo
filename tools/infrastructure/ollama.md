---
{
  "id": "ollama",
  "title": "Ollama",
  "type": "tool",
  "tags": [
    "tools",
    "infrastructure"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "local-inference",
    "model-routing",
    "portable-memory"
  ],
  "problems": [
    "infraestructura",
    "agentes persistentes"
  ],
  "summary": "Herramienta para ejecutar y utilizar modelos abiertos, con documentación de integración en aplicaciones.",
  "sources": [
    "community",
    "ollama"
  ],
  "origin": "community-synthesis"
}
---

# Ollama

Herramienta para ejecutar y utilizar modelos abiertos, con documentación de integración en aplicaciones.

## Qué se observó

Se sugirió para tareas locales y se reportaron límites de velocidad en equipos concretos. Esos relatos no fijan un mínimo universal de RAM ni una calidad común a todos los modelos.

## Cuándo probar y cómo decidir

Elegí modelo y cuantización, ejecutá un caso representativo y comprobá red, memoria y latencia. Usá el mismo criterio de aceptación que en una alternativa remota.

## Límites y alternativas

Ollama no se convierte por sí solo en un orquestador inteligente o en una memoria persistente. Verificá si tu configuración usa inferencia local o un servicio remoto.

## Conexiones

`local-inference`, `model-routing`, `portable-memory`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Ollama](https://docs.ollama.com/): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
