---
{
  "id": "getting-started",
  "title": "Empezar por un problema y una prueba",
  "type": "guide",
  "tags": [
    "onboarding",
    "retrieval",
    "knowledge"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "build-your-agent",
    "agentic-coding",
    "research-with-agents"
  ],
  "problems": [
    "empezar",
    "encontrar conocimiento",
    "mejorar proyecto"
  ],
  "summary": "Buscá una mejora concreta, leé su evidencia y probala antes de instalar una colección de herramientas.",
  "sources": [
    "community"
  ],
  "origin": "editorial-guide"
}
---

# Empezar por un problema y una prueba

Buscá una mejora concreta, leé su evidencia y probala antes de instalar una colección de herramientas.

## Inicio rápido

Necesitás Python 3.9 o posterior; los comandos de catálogo y validación usan solo biblioteca estándar. Cloná el repositorio y ejecutá:

```bash
python3 scripts/kb.py search "memoria persistente"
python3 scripts/kb.py check
```

Si no podés ejecutar código, abrí catalog.json, filtrá problems/tags y seguí las rutas de las primeras entradas.

## Lectura progresiva

Leé primero resumen, evidencia, fecha y problemas. Elegí hasta tres documentos; después ampliá por related y backlinks solo si falta contexto. Las fuentes están en cada documento y resources/sources.json. Una fuente privada acredita un relato, no una prueba independiente.

## De lectura a aplicación

Elegí una hipótesis con resultado verificable: por ejemplo, corregir un recuerdo y recuperarlo sin la versión vieja. Compará la alternativa actual con la nueva. Registrá costo y mantenimiento, además de calidad. La salida útil es adoptar, ajustar, descartar o identificar información faltante.

## Usar con tu agente

Dale la URL del repositorio y pedile leer AGENTS.md y el catálogo. Indicá tu objetivo, sistema actual y permisos. El agente debe proponer un cambio pequeño con verificación y rollback; leer esta base no concede nuevos accesos.

## Conexiones

`build-your-agent`, `agentic-coding`, `research-with-agents`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
