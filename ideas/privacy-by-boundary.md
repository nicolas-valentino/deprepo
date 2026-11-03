---
{
  "id": "privacy-by-boundary",
  "title": "Privacidad por límites verificables",
  "type": "idea",
  "tags": [
    "privacy",
    "security",
    "permissions"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "portable-memory",
    "permission-enforcement",
    "openrouter",
    "local-inference"
  ],
  "problems": [
    "proteger datos",
    "memoria privada"
  ],
  "summary": "La privacidad depende del recorrido efectivo de los datos y de las credenciales disponibles.",
  "sources": [
    "community",
    "openrouter"
  ],
  "origin": "community-synthesis"
}
---

# Privacidad por límites verificables

La privacidad depende del recorrido efectivo de los datos y de las credenciales disponibles.

## Aprendizaje de la comunidad

Se reportó separar historiales crudos de una versión destilada para modelos remotos. También se discutieron políticas de retención y proveedores intermedios. Son decisiones de arquitectura diferentes: dónde se almacena, dónde se procesa y qué terceros lo reciben.

## Aplicación

Dibujá el flujo desde fuente a índice, prompt, logs y copia de seguridad. Usá una cuenta y credenciales por agente; concedé únicamente los recursos requeridos. Probá revocación y eliminación de un dato de sus derivados.

## Límites y posiciones

Un proveedor que no entrena con datos puede retenerlos para otros fines. ZDR debe verificarse por endpoint, proveedor y condiciones actuales. No se heredan garantías por usar un router o por guardar el vault en una computadora propia.

## Conexiones

`portable-memory`, `permission-enforcement`, `openrouter`, `local-inference`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Provider logging](https://openrouter.ai/docs/guides/privacy/provider-logging): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
