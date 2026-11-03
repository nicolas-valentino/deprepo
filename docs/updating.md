# Incorporar otra exportación

El flujo es nueva exportación privada → novedades → deduplicación conceptual → verificación → propuesta de cambios → PR → revisión humana. No hay tarea programada ni publicación automática de conversaciones.

## Inventario privado incremental

Guardá el ZIP fuera del checkout. El script admite el formato iOS con corchetes y Android con guion, fechas DD/MM/YYYY y hora de 24 horas. No transcribe audios ni interpreta imágenes. Falla ante formato desconocido en lugar de asumir que no hubo mensajes.

```bash
python3 scripts/ingest.py /ruta/privada/export.zip   --state /ruta/privada/state.json   --report /ruta/privada/report.json
```

El estado guarda IDs HMAC con clave aleatoria privada. El reporte contiene fechas y conteos agregados de temas; no autores, cuerpos, URLs extraídas ni hashes sin clave. Se rechazan input, state o report dentro del checkout. Protegé también los backups del estado. El script no modifica documentos públicos.

Repetir la misma exportación produce cero novedades. Una exportación solapada agrega registros nuevos. Mensajes editados cuentan como nuevos; igualdad de fecha, hora y cuerpo se deduplica aunque cambie autor. Los conteos por keywords se superponen y no garantizan detección semántica exhaustiva. Si se pierde el estado, se puede reiniciar un inventario, pero habrá que deduplicar editorialmente.

## Revisión del material

El script identifica períodos y temas candidatos; un editor debe leer la conversación completa relevante y revisar los mensajes sin keywords antes de afirmar cobertura exhaustiva. No publica ni propone resúmenes automáticamente. Las nuevas herramientas pueden quedar pendientes si solo hay una mención. Buscá por problema e ID en catalog.json antes de crear una ficha.

Para cada novedad registrá: entrada afectada, afirmación nueva, tipo de evidencia, fuente primaria, cambio respecto de la recomendación anterior y prueba de aplicación. Una contradicción se explica, no se elimina por popularidad. Las novedades que no se pueden verificar quedan en docs/editorial-backlog.md.

## Verificación y PR

```bash
python3 scripts/kb.py build
python3 scripts/kb.py check
python3 -m unittest discover -s tests -v
python3 scripts/kb.py stale
python3 scripts/check_sources.py --output /ruta/privada/link-report.json
git diff --check
git diff --stat
```

La comprobación externa es opcional y requiere red: distingue enlaces recuperados, fallos HTTP y destinos inaccesibles. 403, bloqueos o timeouts no se presentan como enlace roto confirmado. No se ejecuta en CI para evitar resultados inestables y tráfico innecesario.

Antes de subir, inspeccioná `git diff --cached` completo; no incluyas una exportación para justificar procedencia. Abrí una rama desde la base real del proyecto y un PR con revisión humana. Preservá go-model-router salvo autorización específica. Nunca hacer merge automático.

## Alcance de la automatización

Implementado: parsing, inventario completo de registros, deduplicación incremental, conteos temáticos, esquema, catálogo, relaciones, alertas por edad, checks y CI. Editorial/humano: extracción semántica, contraste de nuevas afirmaciones, deduplicación conceptual, detección de contradicciones y decisión de publicación. No se promete que un script de keywords sustituya esa curación.
