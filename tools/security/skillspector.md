---
{
  "id": "skillspector",
  "title": "SkillSpector",
  "type": "tool",
  "tags": [
    "tools",
    "security"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "skill-supply-chain",
    "skills",
    "permission-enforcement"
  ],
  "problems": [
    "auditar herramientas",
    "riesgos de agentes"
  ],
  "summary": "Scanner del proyecto NVIDIA para detectar patrones de riesgo en skills de agentes.",
  "sources": [
    "community",
    "skillspector"
  ],
  "origin": "community-synthesis"
}
---

# SkillSpector

Scanner del proyecto NVIDIA para detectar patrones de riesgo en skills de agentes.

## Qué se observó

Se compartió para revisar antes de instalar. El chat no aportó tasas de detección ni prueba independiente de ausencia de falsos negativos.

## Cuándo probar y cómo decidir

Analizá una copia fijada por commit y revisá manualmente los hallazgos. Contrastá con permisos y destinos de red reales. No ejecutes la skill objetivo para inspeccionarla.

## Límites y alternativas

Un resultado limpio no certifica seguridad. Debe complementar aislamiento, revisión de dependencias y credenciales mínimas.

## Conexiones

`skill-supply-chain`, `skills`, `permission-enforcement`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [SkillSpector](https://github.com/NVIDIA/SkillSpector): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
