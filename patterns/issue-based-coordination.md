---
{
  "id": "issue-based-coordination",
  "title": "Issues como contratos entre agentes",
  "type": "pattern",
  "tags": [
    "coordination",
    "issues",
    "events"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "multi-agent-orchestration",
    "persistent-agent-operations",
    "forgejo",
    "inbox-triage-roadmap"
  ],
  "problems": [
    "agentes que interactuan",
    "coordinar proyectos"
  ],
  "summary": "Usá un registro durable para pedidos y tratá las notificaciones como avisos recuperables.",
  "sources": [
    "community"
  ],
  "origin": "community-synthesis"
}
---

# Issues como contratos entre agentes

Usá un registro durable para pedidos y tratá las notificaciones como avisos recuperables.

## Motivación y evidencia

En octubre se describió un sistema donde agentes por proyecto se pedían trabajo mediante issues y un webhook notificaba qué había cambiado. El aviso llevaba una referencia; el receptor leía el contenido con su propia cuenta. Al iniciar reconciliaba pendientes.

## Implementación y prueba

Definí estados propuesto, aceptado, en curso, verificación y cerrado. Cada pedido incluye responsable, criterio y resultado. Verificá firmas de webhooks, deduplicá por identificador y permití relectura de pendientes; un aviso duplicado no debe ejecutar dos veces.

## Trade-offs y alternativa

La autenticación del emisor y autorización del ejecutor deben ser independientes del texto del issue. No copies conversaciones privadas a notificaciones. La receta de la comunidad es un antecedente, no código de infraestructura auditado.

## Conexiones

`multi-agent-orchestration`, `persistent-agent-operations`, `forgejo`, `inbox-triage-roadmap`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
