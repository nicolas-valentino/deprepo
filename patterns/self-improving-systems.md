---
{
  "id": "self-improving-systems",
  "title": "Mejora continua por evidencia y versiones",
  "type": "pattern",
  "tags": [
    "learning",
    "harness",
    "evaluation"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "harness2",
    "cross-project-learning",
    "benchmark-hygiene"
  ],
  "problems": [
    "mejorar agentes",
    "aprender de errores"
  ],
  "summary": "Convertí un fallo observado en una propuesta de cambio y una prueba de regresión antes de modificar el sistema.",
  "sources": [
    "community",
    "harness2"
  ],
  "origin": "community-synthesis"
}
---

# Mejora continua por evidencia y versiones

Convertí un fallo observado en una propuesta de cambio y una prueba de regresión antes de modificar el sistema.

## Motivación y evidencia

El grupo propuso auditar skills tras ejecutarlas y propagar aprendizajes entre proyectos. También discutió si un modelo nuevo vuelve innecesario parte del harness. Mejorar el sistema requiere comparar contra la versión anterior, no acumular reglas por cada anécdota.

## Implementación y prueba

Registrá fallo, contexto mínimo, resultado esperado y prueba. Proponé una regla pequeña; evaluá el conjunto de regresión y un conjunto reservado. Versioná la modificación y mantené rollback. Adoptá solo si mejora la métrica sin incumplir restricciones.

## Trade-offs y alternativa

Cambiar memoria o instrucciones no es modificar pesos. Harness² y OpenEvolve exploran estrategias específicas; sus resultados no demuestran una auto-mejora general. Las reglas nuevas pueden sobreajustar y contradecir otras.

## Conexiones

`harness2`, `cross-project-learning`, `benchmark-hygiene`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Harness²](https://github.com/google-research/harness2): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
