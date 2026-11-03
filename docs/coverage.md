# Cobertura de la primera edición

La fuente principal fue la exportación más reciente adjunta al pedido, posterior a la versión nombrada en el TXT. Se procesó el único archivo de conversación del ZIP completo: 7.148 registros entre 2025-04-21 y 2026-11-03; 7.110 registros con separador de autor tras deduplicación, 25 sin ese separador y 13 duplicados. El registro no equivale necesariamente a un mensaje sustantivo: incluye eventos y avisos de medios omitidos.

El resumen público de alcance está en [source-coverage.json](source-coverage.json); los conteos mensuales y temáticos permanecen privados. Las expresiones de temas no excluyen períodos: recorren el corpus completo. Son heurísticas superpuestas, no una clasificación semántica exhaustiva. Los mensajes sin keywords también pueden contener conocimiento útil.

## Qué representa esta edición

Se sintetizaron los núcleos recurrentes y casos prácticos identificados: propiedad del contexto, memorias distintas, costos, orquestación, supervisión, evaluación cruzada, seguridad de tools, coordinación por issues, aprendizajes entre proyectos, investigación de alignment, interpretabilidad y debates cognitivos y económicos. Hay 78 entradas sustanciales, no un documento por mensaje.

La curación leyó discusiones y contexto seleccionados a lo largo del período; **no certifica una revisión humana individual de cada registro ni que todas las herramientas o ideas del corpus estén documentadas**. Se conserva una [cola editorial](editorial-backlog.md) para ampliar cobertura. El inventario automatizado sí recorre todos los registros compatibles. Esta distinción evita confundir parsing completo con extracción semántica completa.

La investigación externa contrasta identidad de proyectos y alcance de fuentes primarias. Las síntesis de papers se basan en sus páginas, abstracts y material oficial recuperado; no se reprodujeron experimentos ni se auditó todo el código de las herramientas.

## Limitaciones materiales

- 524 registros authored únicos contienen avisos de medios omitidos; las imágenes, audios y documentos no están incluidos en el ZIP. No se infiere su contenido.
- Enlaces sociales sin descripción suficiente no permiten saber qué se mostró: no se convierten en evidencia técnica.
- Una mención o texto generado por otro modelo no acredita una experiencia real. Las fichas explican qué sí se reportó y qué no.
- Hay referencias compartidas cuyo contenido no se pudo recuperar; permanecen pendientes, sin resultados atribuidos.
- El trabajo previo go-model-router se conserva pero no se validaron sus cifras ni garantías históricas.

## Evolución de conclusiones preservada

En junio apareció la separación de memoria humana y operativa; en agosto se exploraron sistemas de coordinación más amplios; en septiembre se reportó simplificación por exceso de mantenimiento; en octubre se documentaron contratos, revisión cruzada y fallos de cobertura de permisos. Noviembre agregó discusiones sobre medición del progreso, adopción y nuevas comparaciones de modelos. No se impuso una conclusión única a esos recorridos.

## Privacidad

No se distribuyen exportación, nombres, teléfonos, cuerpos, citas atribuidas, invitaciones ni identificadores de mensajes. Los datos públicos de este informe son agregados seleccionados. El estado incremental HMAC es privado y no forma parte del PR. La revisión automatizada es una ayuda y se acompaña de revisión editorial del diff.
