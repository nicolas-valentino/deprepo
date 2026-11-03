# Validación de la edición inicial

Revisión: 2026-11-03. Base de implementación: rama predeterminada `feat/add-go-model-router`, commit `9d885480e480657383926993a24c8ceca7078b7c`. El árbol completo de `go-model-router/` se conserva sin modificaciones.

## Resultados ejecutados

| Control | Resultado |
| --- | --- |
| Generación del catálogo | 78 entradas; generación determinista desde front matter |
| Metadatos | IDs, tipos, evidencia, fecha, campos requeridos y esquema válidos |
| Relaciones | Todos los IDs resuelven; backlinks generados y verificados |
| Enlaces internos | Rutas existentes, sin destinos fuera del checkout |
| Pruebas automatizadas | 22 tests aprobados |
| Fuentes externas del registro | 45 accesibles, 0 enlaces rotos confirmados, 0 inaccesibles en la ejecución |
| Exportación completa | 7.148 registros parseados; duplicados y omisiones contabilizados |
| Reingestión de la misma exportación | 0 registros nuevos |
| Privacidad | Sin coincidencias de identidades de participantes de varias palabras ni emails en contenido nuevo; scanner y revisión editorial del material publicado |
| Trabajo previo | Directorio go-model-router sin cambios |

El chequeo de fuentes usa respuestas HTTP; no valida la verdad de una página. El scanner de privacidad es heurístico y no garantiza anonimización. Los tests de recuperación verifican el índice y las relaciones; **no son una evaluación experimental de recomendaciones ejecutadas por distintos LLMs**.

## Escenario A: asistente personal

Consulta: `asistente memoria persistente modelos intercambiables`.

Primeros resultados: build-your-agent, portable-memory, context-ownership, model-families y separate-human-agent-memory. Desde sus relaciones se llega a model-routing y bounded-autonomy.

Recomendación que permite construir el recorrido: conservar hechos confirmados en un registro exportable, reconstruir índices, empezar con lectura y probar corrección/borrado antes de sumar integraciones. La prueba de aceptación cambia lector/modelo y comprueba que un dato corregido no reaparezca obsoleto. No exige elegir un proveedor particular.

## Escenario B: agentes de desarrollo en paralelo

Consulta: `coding agents paralelo worktree`.

Primeros resultados: worktree-per-agent, agentic-coding, multi-agent-orchestration, opencode y agents-not-chatbots. Se conectan revisión cruzada, pruebas e integración.

Recomendación: dividir tareas independientes, usar ramas/directorios separados y un responsable de integración. No confundir worktrees con aislamiento de procesos. Criterio de aceptación: ambos cambios funcionan juntos y no producen regresiones, con costo de supervisión medido. La alternativa simple es una sola sesión con revisión.

## Escenario C: riesgos de autonomía

Consulta: `riesgos agentes autonomos alignment`.

Primeros resultados: alignment-training, capability-is-not-alignment, research-with-agents, autonomous-risk y agentic-coding. Las relaciones alcanzan permission-enforcement y functional-emotions.

Recomendación: separar éxito funcional de cumplimiento de límites, probar todas las rutas equivalentes de una acción y leer resultados de estudios bajo sus condiciones. No inferir conciencia de representaciones emocionales ni un incidente real de una evaluación controlada de capacidad.

## Cómo repetir

```bash
python3 scripts/kb.py build
python3 scripts/kb.py check
python3 -m unittest discover -s tests -v
python3 scripts/kb.py search "memoria persistente"
python3 scripts/kb.py search "coding agents paralelo"
python3 scripts/kb.py search "riesgos agentes autonomos alignment"
```

El script check_sources permite repetir la verificación HTTP con red. La CI ejecuta checks internos y tests sin dependencias ni llamadas a proveedores. Quedan pendientes revisión humana del PR, mayor cobertura semántica del corpus y verificación de candidatos de la cola editorial. No se hace merge automático.
