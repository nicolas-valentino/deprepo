#!/usr/bin/env python3
"""Inventory a private WhatsApp export. Never write message bodies or author names."""
import argparse
import collections
import datetime as dt
import hashlib
import hmac
import json
import os
import re
import secrets
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADER = re.compile(r'^[\u200e\u200f]*\[(\d{1,2}/\d{1,2}/\d{4}), (\d{2}:\d{2}:\d{2})\] ', re.M)
ANDROID = re.compile(r'^[\u200e\u200f]*(\d{1,2}/\d{1,2}/\d{4}), (\d{1,2}:\d{2}(?::\d{2})?) - ', re.M)
TOPICS = {
    'agents':r'\bagent[es]*\b|ag[eé]ntic|chatbot',
    'memory':r'memor|second.?brain|obsidian|logseq|gbrain|hindsight|openviking|honcho',
    'orchestration':r'orquest|worktree|multi.?agent|swarm|orca',
    'routing-cost':r'openrouter|ollama|routing|cuota|tokens|cost[os]*',
    'alignment-safety':r'alignment|alineam|seguridad|sandbox|permiso|jailbreak|safety',
    'interpretability-minds':r'interpret|conscien|concien|binding problem|digital minds|emocion',
    'cognition-learning':r'cogniti|pr[oó]tesis|aprend|educa|inteligencia',
    'research-evaluation':r'paper|arxiv|benchmark|evaluaci|prueba|investig',
    'economy-adoption':r'econom|empleo|trabajo|productiv|adopci|progreso|riqueza',
    'creative-multimodal':r'suno|imagen|m[uú]sica|creativ|voz|video|robot|lerobot',
    'methodology':r'bmad|b-mad|\bgsd\b|spec|meta.?work|collector|triage|roadmap',
}

def parse(text):
    matches = list(HEADER.finditer(text))
    if not matches:
        matches = list(ANDROID.finditer(text))
    if not matches:
        raise ValueError('Unsupported export: expected DD/MM/YYYY, 24-hour timestamps')
    if text[:matches[0].start()].strip('\ufeff\n\r\u200e '):
        raise ValueError('Unparsed text before first message')
    rows = []
    for i, match in enumerate(matches):
        chunk = text[match.end():matches[i+1].start() if i+1 < len(matches) else len(text)].strip()
        date = dt.datetime.strptime(match[1], '%d/%m/%Y').date().isoformat()
        author, separator, body = chunk.partition(': ')
        if not separator:
            rows.append((date, match[2], None))
        else:
            rows.append((date, match[2], body))
    return rows


def read_export(path):
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as archive:
            files = [f for f in archive.infolist() if f.filename.endswith('.txt') and not f.filename.startswith('__MACOSX/')]
            if len(files) != 1:
                raise ValueError('Expected exactly one chat TXT in archive')
            if files[0].file_size > 50_000_000:
                raise ValueError('Chat text exceeds 50 MB limit')
            return archive.read(files[0]).decode('utf-8-sig')
    if path.stat().st_size > 50_000_000:
        raise ValueError('Chat text exceeds 50 MB limit')
    return path.read_text(encoding='utf-8-sig')


def outside_repo(path):
    resolved = path.resolve()
    if ROOT == resolved or ROOT in resolved.parents:
        raise ValueError('Private input, state and report must remain outside the repository')
    return resolved


def secure_write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(dir=str(path.parent))
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def inventory(rows, previous):
    key = bytes.fromhex(previous.get('key', secrets.token_hex(32)))
    seen = set(previous.get('seen', []))
    current = set()
    topics, new_topics, months = collections.Counter(), collections.Counter(), collections.Counter()
    new, duplicate, system, media = 0, 0, 0, 0
    matched, unmatched = 0, 0
    for date, time, body in rows:
        months[date[:7]] += 1
        if body is None:
            system += 1
            continue
        identifier = hmac.new(key, (date+' '+time+'\n'+body).encode(), hashlib.sha256).hexdigest()
        if identifier in current:
            duplicate += 1
            continue
        current.add(identifier)
        is_new = identifier not in seen
        new += int(is_new)
        media += int(bool(re.search(r'(?:image|audio|video|sticker|document|GIF) omitted', body)))
        hits = [topic for topic, pattern in TOPICS.items() if re.search(pattern, body, re.I)]
        matched += bool(hits)
        unmatched += not bool(hits)
        topics.update(hits)
        if is_new:
            new_topics.update(hits)
    report = {'schema_version':1,'messages_total':len(rows),'unique_authored_records':len(current),
              'system_records_without_author_separator':system,'duplicate_records':duplicate,
              'media_omission_records':media,'new_records':new,
              'date_start':min(r[0] for r in rows),'date_end':max(r[0] for r in rows),
              'monthly_records':dict(sorted(months.items())),
              'topic_candidates':dict(sorted(topics.items())),
              'new_topic_candidates':dict(sorted(new_topics.items())),
              'matched_records':matched,'unmatched_records':unmatched,
              'limitations':['Keyword hits overlap and are not an exhaustive semantic classification.',
                              'No media content is present; omission notices are not evidence.',
                              'Same timestamp and body are deduplicated even if authors differ.',
                              'HMAC identity includes message body; edited messages appear as new.',
                              'No authors, messages, private URLs or unsalted hashes are exported.']}
    return report, {'schema_version':1,'key':key.hex(),'seen':sorted(seen|current)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('export',type=Path)
    p.add_argument('--state',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True)
    args=p.parse_args()
    try:
        source,state_path,report_path = [outside_repo(x) for x in (args.export,args.state,args.report)]
        if len({source,state_path,report_path}) != 3:
            raise ValueError('Input, state and report must have distinct paths')
        previous=json.loads(state_path.read_text()) if state_path.exists() else {}
        report,state=inventory(parse(read_export(source)),previous)
        secure_write(report_path,report)
        secure_write(state_path,state)
        print(json.dumps(report,ensure_ascii=False,indent=2))
    except (ValueError,OSError,zipfile.BadZipFile) as error:
        p.exit(1,str(error)+'\n')

if __name__=='__main__':
    main()
