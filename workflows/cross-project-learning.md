---
{
  "id": "cross-project-learning",
  "title": "Aprendizajes entre proyectos sin propagación ciega",
  "type": "workflow",
  "tags": [
    "workflow",
    "learning",
    "maintenance"
  ],
  "status": "active",
  "evidence": "experience",
  "last_reviewed": "2026-11-03",
  "related": [
    "self-improving-systems",
    "inbox-triage-roadmap",
    "benchmark-hygiene"
  ],
  "problems": [
    "aprender de errores",
    "coordinar proyectos",
    "mejorar agentes"
  ],
  "summary": "Convertí un hallazgo local en una propuesta revisable antes de aplicarlo a otros contextos.",
  "sources": [
    "community"
  ],
  "origin": "community-synthesis"
}
---

# Aprendizajes entre proyectos sin propagación ciega

Convertí un hallazgo local en una propuesta revisable antes de aplicarlo a otros contextos.

## Entrada y contrato

Entrada: un fallo reproducible o una mejora medida en un proyecto. Salida: decisión local o propuesta de regla común con alcance y excepciones. El registro compartido debe permitir saber dónde se aplicó y cómo revertirlo.

## Procedimiento

Describí problema y contexto mínimo sin datos privados. Extraé una regla candidata y un test que falle antes. Clasificá si depende de lenguaje, dominio, herramientas o permisos. Evaluá en un segundo proyecto antes de generalizar. Publicá una propuesta con diff, evidencia, responsables y rollback.

## Qué aprendió el grupo

Se intentó centralizar prácticas y sincronizar roadmaps. La continuidad útil fue que los agentes aprendieran responsabilidades y convenciones; la sincronización manual de múltiples artefactos resultó costosa. El aprendizaje es transferir invariantes, no copiar todos los archivos.

## Aceptación y límites

Una regla transversal debe resolver el problema original, no romper un caso reservado y tener un mecanismo de retirada. Medí mantenimiento del sistema de aprendizaje. Un modelo que agrega reglas a su memoria no ha mejorado automáticamente su rendimiento; comprobalo.

## Conexiones

`self-improving-systems`, `inbox-triage-roadmap`, `benchmark-hygiene`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
