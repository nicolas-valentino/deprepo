#!/usr/bin/env python3
"""Dependency-free catalog builder, retrieval CLI and repository validation (Python 3.9+)."""
import argparse
import datetime as dt
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DIRS = ('ideas', 'patterns', 'tools', 'research', 'guides', 'workflows')


def metadata(path):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise ValueError(f'{path}: missing front matter')
    raw, body = text[4:].split('\n---\n', 1)
    return json.loads(raw), body


def validate_schema(value, schema, location='$'):
    """Validate the exact JSON Schema vocabulary used by entry.schema.json.

    Not a general-purpose JSON Schema implementation: unknown keywords fail closed.
    """
    supported = {'$schema', 'title', 'description', 'type', 'required', 'properties',
                 'additionalProperties', 'enum', 'pattern', 'format', 'minLength',
                 'minItems', 'uniqueItems', 'items'}
    unknown = set(schema) - supported
    if unknown:
        raise ValueError(f'Unsupported schema keywords: {unknown}')
    types = {'object': dict, 'array': list, 'string': str, 'integer': int}
    if 'type' in schema and type(value) is not types[schema['type']]:
        raise ValueError(f'{location}: expected {schema["type"]}')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f'{location}: invalid enum {value!r}')
    if isinstance(value, dict):
        missing = set(schema.get('required', [])) - value.keys()
        if missing:
            raise ValueError(f'{location}: missing {missing}')
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False and set(value) - props.keys():
            raise ValueError(f'{location}: unknown fields {set(value) - props.keys()}')
        for key, item in value.items():
            if key in props:
                validate_schema(item, props[key], location + '.' + key)
    if isinstance(value, str):
        if len(value) < schema.get('minLength', 0):
            raise ValueError(f'{location}: too short')
        if 'pattern' in schema and not re.search(schema['pattern'], value):
            raise ValueError(f'{location}: pattern mismatch')
        if schema.get('format') == 'date':
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
                raise ValueError(f'{location}: invalid ISO date')
            dt.date.fromisoformat(value)
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0):
            raise ValueError(f'{location}: too few items')
        if schema.get('uniqueItems') and len({json.dumps(x, sort_keys=True) for x in value}) != len(value):
            raise ValueError(f'{location}: duplicate items')
        for i, item in enumerate(value):
            validate_schema(item, schema.get('items', {}), f'{location}[{i}]')


def build(root=ROOT):
    schema = json.loads((root / 'schema/entry.schema.json').read_text())
    sources = json.loads((root / 'resources/sources.json').read_text())
    entries = []
    for directory in DIRS:
        for path in sorted((root / directory).rglob('*.md')):
            meta, body = metadata(path)
            validate_schema(meta, schema, str(path.relative_to(root)))
            if dt.date.fromisoformat(meta['last_reviewed']) > dt.date.today():
                raise ValueError(f'{path}: review date is in the future')
            for source in meta['sources']:
                if source not in sources:
                    raise ValueError(f'{path}: unknown source {source}')
            if len(body.split()) < 65:
                raise ValueError(f'{path}: entry lacks substantive content')
            entries.append(dict(meta, path=path.relative_to(root).as_posix(), backlinks=[]))
    by_id = {e['id']: e for e in entries}
    if len(by_id) != len(entries):
        raise ValueError('Duplicate entry IDs')
    for entry in entries:
        for related in entry['related']:
            if related not in by_id or related == entry['id']:
                raise ValueError(f'{entry["id"]}: invalid relation {related}')
            by_id[related]['backlinks'].append(entry['id'])
    for entry in entries:
        entry['backlinks'].sort()
    return {'schema_version': 1, 'entries': sorted(entries, key=lambda x: x['id']),
            'counts': dict(sorted(Counter(e['type'] for e in entries).items()))}


def normalized(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text.lower()) if not unicodedata.combining(c))


def search(catalog, query, kind=None, limit=8):
    words = normalized(query).split()
    scored = []
    for entry in catalog['entries']:
        if kind and entry['type'] != kind:
            continue
        weighted = [(entry['id'] + ' ' + entry['title'], 4),
                    (' '.join(entry['tags'] + entry['problems']), 3), (entry['summary'], 1)]
        score = sum(weight for text, weight in weighted for word in words if word in normalized(text))
        if score:
            scored.append((score, entry))
    return [e for _, e in sorted(scored, key=lambda p: (-p[0], p[1]['id']))[:limit]]


def check_links(root=ROOT):
    failures = []
    for path in sorted(root.rglob('*.md')):
        if '.git' in path.parts or 'go-model-router' in path.parts:
            continue  # Preserved third-party project, outside new KB validation scope.
        text = path.read_text(encoding='utf-8')
        text = re.sub(r'```.*?```', '', text, flags=re.S)
        for dest in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
            parsed = urlsplit(dest)
            if parsed.scheme or dest.startswith('#'):
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if root.resolve() not in (target, *target.parents) or not target.exists():
                failures.append(f'{path.relative_to(root)} -> {dest}')
    if failures:
        raise ValueError('Broken/escaping internal links:\n' + '\n'.join(failures))


def privacy_scan(root=ROOT):
    # Heuristics are a review aid, not an anonymization guarantee.
    patterns = [r'\[\d{1,2}/\d{1,2}/\d{4}, \d{2}:\d{2}',
                r'chat\.whatsapp\.com/', r'\bsk-[A-Za-z0-9]{20,}',
                r'\bgh[pousr]_[A-Za-z0-9]{20,}', r'\+54[\s\d()-]{10,}']
    for path in root.rglob('*'):
        if not path.is_file() or '.git' in path.parts or 'go-model-router' in path.parts:
            continue
        if path.suffix.lower() in {'.zip', '.sqlite', '.db'} or path.name == '_chat.txt':
            raise ValueError(f'Private/binary input in public tree: {path}')
        if path.suffix in {'.md', '.json', '.yml'}:
            text = path.read_text(encoding='utf-8')
            if any(re.search(p, text) for p in patterns):
                raise ValueError(f'Potential private data: {path}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('build')
    sub.add_parser('check')
    search_parser = sub.add_parser('search')
    search_parser.add_argument('query')
    search_parser.add_argument('--type', choices=['idea','pattern','tool','research','guide','workflow'])
    search_parser.add_argument('--limit', type=int, default=8)
    sub.add_parser('stale').add_argument('--as-of', default=dt.date.today().isoformat())
    args = parser.parse_args()
    try:
        if args.command in ('build', 'check'):
            catalog = build()
            serialized = json.dumps(catalog, ensure_ascii=False, indent=2) + '\n'
            if args.command == 'build':
                (ROOT / 'catalog.json').write_text(serialized, encoding='utf-8')
            else:
                if (ROOT / 'catalog.json').read_text(encoding='utf-8') != serialized:
                    raise ValueError('catalog.json is stale; run python3 scripts/kb.py build')
                check_links()
                privacy_scan()
            print(json.dumps({'ok': True, 'counts': catalog['counts']}, ensure_ascii=False))
        else:
            catalog = json.loads((ROOT / 'catalog.json').read_text())
            if args.command == 'search':
                rows = search(catalog, args.query, args.type, args.limit)
            else:
                today = dt.date.fromisoformat(args.as_of)
                rows = [e for e in catalog['entries'] if
                        (today - dt.date.fromisoformat(e['last_reviewed'])).days >
                        (30 if e['type'] == 'tool' else 90 if e['type'] == 'research' else 180)]
            print(json.dumps(rows, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
