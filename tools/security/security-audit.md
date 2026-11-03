---
{
  "id": "security-audit",
  "title": "Security audit skill de Cloudflare",
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
    "benchmark-hygiene",
    "strix"
  ],
  "problems": [
    "auditar herramientas",
    "riesgos de agentes"
  ],
  "summary": "Procedimiento de auditoría para proyectos, distinto de un scanner de paquetes de skills.",
  "sources": [
    "community",
    "security-audit"
  ],
  "origin": "community-synthesis"
}
---

# Security audit skill de Cloudflare

Procedimiento de auditoría para proyectos, distinto de un scanner de paquetes de skills.

## Qué se observó

Se recomendó al discutir revisión de seguridad. No se publican como hechos resultados de auditorías que el grupo no entregó.

## Cuándo probar y cómo decidir

Aplicá una auditoría de lectura sobre una copia de prueba y exigí archivo, evidencia, impacto y reproducción de cada hallazgo. Priorizá riesgos verificables.

## Límites y alternativas

El agente auditor también puede alucinar o pasar por alto problemas. No confundas cantidad de hallazgos con calidad ni la auditoría con autorización para atacar servicios.

## Conexiones

`skill-supply-chain`, `benchmark-hygiene`, `strix`. Consultá sus rutas y backlinks en [catalog.json](../../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Security audit skill](https://github.com/cloudflare/security-audit-skill): Identidad y alcance documentado; no prueba de superioridad ni auditoría de seguridad.
