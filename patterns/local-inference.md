---
{
  "id": "local-inference",
  "title": "Inferencia local con una prueba representativa",
  "type": "pattern",
  "tags": [
    "local",
    "models",
    "privacy"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "ollama",
    "model-routing",
    "privacy-by-boundary"
  ],
  "problems": [
    "modelos locales",
    "proteger datos",
    "reducir costo"
  ],
  "summary": "Medí memoria, velocidad y calidad en la tarea objetivo antes de asumir que local será mejor o más barato.",
  "sources": [
    "community",
    "ollama"
  ],
  "origin": "community-synthesis"
}
---

# Inferencia local con una prueba representativa

Medí memoria, velocidad y calidad en la tarea objetivo antes de asumir que local será mejor o más barato.

## Motivación y evidencia

Hubo relatos de lentitud en equipos de 16 GB y comparaciones desfavorables con suscripciones remotas; son mediciones informales, no requisitos universales. El caso de uso puede justificar un modelo menor para destilar datos antes de enviarlos afuera.

## Implementación y prueba

Elegí un modelo y cuantización que entren en la memoria disponible. Usá documentos sintéticos de tamaño real, medí latencia inicial, tokens por segundo, consumo y exactitud. Desconectá la red para verificar qué funciones siguen operando localmente.

## Trade-offs y alternativa

Pesos abiertos no equivalen siempre a licencia open source; revisá condiciones por modelo. Incluir un backend cloud en una app local cambia privacidad y costo. El valor puede estar en control o disponibilidad, aunque la calidad sea menor.

## Conexiones

`ollama`, `model-routing`, `privacy-by-boundary`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Ollama](https://docs.ollama.com/): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
