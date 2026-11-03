# Contribuir

Partí de un problema o evidencia que cambie una decisión. Una mención nueva no exige una ficha nueva.

1. Buscá el ID o problema en el catálogo y proponé ampliar una entrada antes de duplicarla.
2. Escribí Markdown con metadatos conforme a [entry.schema.json](schema/entry.schema.json). Usamos JSON dentro de front matter YAML para validar sin dependencias.
3. Distinguí observación, experiencia, hipótesis y debate; indicá condiciones y limitaciones.
4. Agregá fuentes en [sources.json](resources/sources.json). El campo supports delimita qué verificaste. Si no accediste al recurso, registralo como pendiente y no como fuente recuperada.
5. Relacioná al menos una entrada existente. Cada herramienta debe justificar cuándo probarla y cómo decidir.
6. Regenerá el catálogo, ejecutá los checks y revisá el diff completo.
7. Abrí un PR con problema, cambio de conclusión, verificación y pendientes. No hacer merge automático.

```bash
python3 scripts/kb.py build
python3 scripts/kb.py check
python3 -m unittest discover -s tests -v
git diff --check
```

No subas exportaciones, capturas privadas, nombres, citas atribuidas, teléfonos, credenciales ni URLs con tokens. Las experiencias se sintetizan impersonalmente. No copies prompts de una conversación privada palabra por palabra.

El directorio go-model-router es previo y queda fuera del alcance de esta implementación. Su código y documentos no se relicencian. Al aportar material nuevo, confirmás que podés ofrecerlo bajo las licencias indicadas en [LICENSE](LICENSE).
