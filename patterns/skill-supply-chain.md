---
{
  "id": "skill-supply-chain",
  "title": "Revisar skills como software ejecutable",
  "type": "pattern",
  "tags": [
    "skills",
    "security",
    "supply-chain"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "skills",
    "skillspector",
    "security-audit",
    "permission-enforcement"
  ],
  "problems": [
    "instalar skills",
    "auditar herramientas"
  ],
  "summary": "Una skill puede introducir comandos, dependencias y accesos; su texto no la vuelve inocua.",
  "sources": [
    "community",
    "agents"
  ],
  "origin": "community-synthesis"
}
---

# Revisar skills como software ejecutable

Una skill puede introducir comandos, dependencias y accesos; su texto no la vuelve inocua.

## Motivación y evidencia

El grupo compartió scanners y auditorías en octubre; también detectó scripts con exposición de tokens y JSON armado por concatenación. Una recomendación o estrellas no equivalen a una revisión de seguridad.

## Implementación y prueba

Fijá commit o versión. Leé instrucciones, comandos, destinos de red y scripts antes de instalar. Probá en un entorno sin secretos y con recursos sintéticos. Compará archivos y permisos antes/después; revisá actualizaciones como cambios de código.

## Trade-offs y alternativa

Los scanners producen falsos positivos y falsos negativos. No instales automáticamente una herramienta solo para revisarla. Diferenciá un scanner de skills de una auditoría del proyecto y conservá evidencia de los hallazgos.

## Conexiones

`skills`, `skillspector`, `security-audit`, `permission-enforcement`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinción workflow/agente y patrones de composición. Documento de proveedor, no comparación neutral.
