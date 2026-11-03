---
{
  "id": "persistent-agent-operations",
  "title": "Operar un agente que permanece encendido",
  "type": "pattern",
  "tags": [
    "operations",
    "infrastructure",
    "autonomy"
  ],
  "status": "active",
  "evidence": "mixed",
  "last_reviewed": "2026-11-03",
  "related": [
    "bounded-autonomy",
    "issue-based-coordination",
    "tailscale",
    "forgejo"
  ],
  "problems": [
    "agentes persistentes",
    "servidor de agentes"
  ],
  "summary": "La persistencia exige recuperación, observabilidad y presupuesto además de un proceso en segundo plano.",
  "sources": [
    "community"
  ],
  "origin": "community-synthesis"
}
---

# Operar un agente que permanece encendido

La persistencia exige recuperación, observabilidad y presupuesto además de un proceso en segundo plano.

## Motivación y evidencia

Se reportaron instalaciones en máquinas personales y servidores remotos; el remoto facilitaba disponibilidad y separaba archivos personales. También aparecieron rate limits, sesiones interrumpidas y servicios rotos. El hardware elegido no resuelve esas condiciones.

## Implementación y prueba

Guardá trabajos pendientes antes de ejecutarlos. Reanudá desde estados confirmados y usá claves de idempotencia en efectos externos. Añadí health check, copia de seguridad restaurable y alertas de costo. Ensayá reinicio durante una tarea ficticia y verificá que no se duplique la acción.

## Trade-offs y alternativa

Un canal de notificaciones puede perder eventos: mantené el issue o cola como fuente de verdad y reconciliá al iniciar. No expongas paneles de control sin autenticación. Local y cloud son decisiones de acceso, operación y costo.

## Conexiones

`bounded-autonomy`, `issue-based-coordination`, `tailscale`, `forgejo`. Consultá sus rutas y backlinks en [catalog.json](../catalog.json).

## Fuentes y alcance

- Síntesis privada de DepreIA; experiencia reportada, sin atribución.
