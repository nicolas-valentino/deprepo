![Meme sobre la complejidad innecesaria de los sistemas de agentes](WhatsApp%20Image%202026-10-27%20at%2020.16.23%20%282%29.jpeg)

# Deprepo

Conocimiento colectivo sobre inteligencia artificial, conectado para personas y agentes.

Deprepo transforma experiencias y debates de DepreIA en **ideas → patrones → herramientas → guías → pruebas de aplicación**. No convierte mensajes en verdades ni recomienda una herramienta por cantidad de menciones.

La primera edición reúne **78 entradas**: 14 ideas, 14 patrones, 33 herramientas, 11 investigaciones, 4 guías y 2 workflows. Parte de una exportación con 7.148 registros entre el 21 de abril de 2025 y el 3 de noviembre de 2026. El texto original y los participantes permanecen privados. Consultá [cobertura y límites](docs/coverage.md).

## Empezar en dos minutos

Elegí un problema:

| Necesidad | Recorrido inicial |
| --- | --- |
| Asistente con memoria y modelos intercambiables | [Guía de asistente](guides/build-your-agent.md) → [Memoria portable](patterns/portable-memory.md) → [Routing](patterns/model-routing.md) |
| Varios coding agents en paralelo | [Guía de desarrollo](guides/agentic-coding.md) → [Worktrees](patterns/worktree-per-agent.md) → [Orquestación](patterns/multi-agent-orchestration.md) |
| Comprender riesgos y debates | [Guía de investigación](guides/research-with-agents.md) → [Alignment](research/alignment/alignment-training.md) → [Autonomía](research/safety/autonomous-risk.md) |
| Demasiadas notas y procesos | [Collector’s Fallacy](ideas/collectors-fallacy.md) → [Meta-work](ideas/minimize-meta-work.md) → [Captura y triage](workflows/inbox-triage-roadmap.md) |

Con Python 3.9+ y sin instalar dependencias:

```bash
git clone https://github.com/nicolas-valentino/deprepo.git
cd deprepo
python3 scripts/kb.py search "memoria persistente"
python3 scripts/kb.py search "coding agents paralelo"
python3 scripts/kb.py check
python3 -m unittest discover -s tests -v
```

Si esta edición todavía está en revisión, cambiá a la rama del pull request. El repositorio conserva su rama predeterminada existente; no asumas que se llama main.

## Dárselo a tu agente

Copiá este pedido:

> Analizá https://github.com/nicolas-valentino/deprepo. Leé AGENTS.md y buscá en catalog.json por mi problema antes de abrir documentos. Quiero mejorar [objetivo] y hoy uso [sistema]. Identificá hasta tres mejoras justificadas, con evidencia, limitaciones y archivos fuente. Proponé una prueba pequeña, costo esperado y rollback. Consultá fuentes actuales para productos o datos que puedan haber cambiado. No instales herramientas ni ejecutes acciones externas fuera de mis permisos.

El catálogo se genera desde Markdown; incluye problemas, resúmenes, etiquetas, fuentes, relaciones y backlinks. No necesita una base vectorial, una API key ni un proveedor específico. Las relaciones permiten pasar de una herramienta a la idea que la justifica. Consultá [AGENTS.md](AGENTS.md) y la [guía de inicio](guides/getting-started.md).

## Cómo leer la evidencia

| Valor | Significado |
| --- | --- |
| `validated` | Afirmación delimitada con evidencia verificable; no verdad universal |
| `experience` | Experiencia práctica reportada, sin replicación independiente |
| `hypothesis` | Propuesta que necesita contrastarse |
| `open-debate` | Posiciones o preguntas aún abiertas |
| `mixed` | Combina categorías; leer la distinción dentro del documento |

Una fuente oficial verifica identidad y capacidades documentadas; no certifica superioridad, seguridad ni cumplimiento de todas sus promesas. Las investigaciones distinguen resultados, interpretación y aplicación. [Política editorial](docs/editorial-policy.md).

## Estructura y mantenimiento

- [Ideas](ideas), [investigación](research), [patrones](patterns), [herramientas](tools), [guías](guides) y [workflows](workflows): documentos autocontenidos.
- [catalog.json](catalog.json): índice generado; no editar a mano.
- [Fuentes](resources/sources.json): procedencia y alcance de verificación.
- [Esquema](schema/entry.schema.json), [validación](scripts/kb.py) y [tests](tests): metadatos, referencias y recorridos.
- [Actualizaciones](docs/updating.md): exportación privada → novedades → contraste → propuesta → PR → revisión humana.
- [Pendientes editoriales](docs/editorial-backlog.md): menciones sin evidencia suficiente para una ficha completa.

Para contribuir: [CONTRIBUTING.md](CONTRIBUTING.md). Para regenerar y validar:

```bash
python3 scripts/kb.py build
python3 scripts/kb.py check
python3 scripts/kb.py stale
```

## Proyecto conservado y licencia

[go-model-router](go-model-router/README.md) se conserva íntegro. Está [indexado](tools/infrastructure/go-model-router.md), pero esta edición no audita sus tablas de modelos, precios, cuotas o retención.

La documentación nueva se ofrece bajo CC BY 4.0 y el código nuevo bajo MIT. El trabajo previo y las fuentes de terceros mantienen su situación y términos propios. [Alcance de licencia](LICENSE).
