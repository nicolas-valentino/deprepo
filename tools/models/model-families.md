---
{
  "id": "model-families",
  "title": "Familias de modelos: elegir por pruebas, no por nombre",
  "type": "tool",
  "tags": [
    "models",
    "routing",
    "evaluation"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "model-routing",
    "benchmark-hygiene",
    "cross-model-review",
    "local-inference"
  ],
  "problems": [
    "comparar modelos",
    "modelos intercambiables",
    "modelos locales"
  ],
  "summary": "Claude, GPT, Gemini, DeepSeek, Qwen, Llama, Kimi, GLM y Grok aparecen en conversaciones con tareas y condiciones diferentes.",
  "sources": [
    "community",
    "openrouter",
    "ollama"
  ],
  "origin": "community-synthesis"
}
---

# Familias de modelos: elegir por pruebas, no por nombre

Claude, GPT, Gemini, DeepSeek, Qwen, Llama, Kimi, GLM y Grok aparecen en conversaciones con tareas y condiciones diferentes.

## Qué aprendimos

Los relatos del grupo cambian por tarea, presupuesto, permisos y versión del producto. Los nombres comerciales de chat, harness y modelo se mezclan. Una mejora percibida no prueba degradación intencional del modelo anterior ni un ranking general.

## Ficha de decisión

Para cada candidato registrá proveedor oficial, identificador exacto, fecha, licencia de pesos si aplica, capacidades de tools, límites y política de datos. Probá la misma muestra reservada. Distinguí precio por token de costo por tarea aprobada; contá revisiones y reintentos.

## Inventario y vigencia

Las nueve familias son candidatos de evaluación, no recomendaciones equivalentes. Verificá su catálogo oficial antes de elegir una versión. No se transcriben nombres de modelos, límites, precios ni garantías ZDR del chat como hechos vigentes. Consultá también las fuentes enlazadas en los clientes y routers.

## Alternativas

Un script determinista, una búsqueda o un modelo pequeño pueden resolver parte del flujo. La alternativa remota puede superar a local en calidad; local puede ganar en control. Elegí la combinación que cumpla tu requisito medido, no la que gane una discusión.

## Conexiones

`model-routing`, `benchmark-hygiene`, `cross-model-review`, `local-inference`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Provider logging](https://openrouter.ai/docs/guides/privacy/provider-logging): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
- [Ollama](https://docs.ollama.com/): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
