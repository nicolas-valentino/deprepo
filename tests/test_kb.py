import copy
import datetime as dt
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
kb=module('kb');ingest=module('ingest')

class MetadataTests(unittest.TestCase):
    def setUp(self):
        self.schema=json.loads((ROOT/'schema/entry.schema.json').read_text())
        self.entry=kb.build()['entries'][0].copy()
        self.entry.pop('path');self.entry.pop('backlinks')
    def test_reject_missing_field(self):
        self.entry.pop('evidence')
        with self.assertRaises(ValueError):kb.validate_schema(self.entry,self.schema)
    def test_reject_invalid_evidence(self):
        self.entry['evidence']='everyone-agrees'
        with self.assertRaises(ValueError):kb.validate_schema(self.entry,self.schema)
    def test_reject_impossible_date(self):
        self.entry['last_reviewed']='2026-02-30'
        with self.assertRaises(ValueError):kb.validate_schema(self.entry,self.schema)
    def test_reject_duplicates_unknown_fields_and_bad_ids(self):
        for change in ({'id':'Bad ID'},{'tags':['same','same']},{'extra':True}):
            with self.subTest(change=change),self.assertRaises(ValueError):
                kb.validate_schema(dict(self.entry,**change),self.schema)
    def test_schema_unknown_keyword_fails(self):
        with self.assertRaises(ValueError):kb.validate_schema('x',{'invented':1})
    def test_broken_and_escaping_links(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            for target in ('missing.md','../../outside.md'):
                (root/'x.md').write_text('[link]('+target+')')
                with self.assertRaises(ValueError):kb.check_links(root)
    def test_catalog_matches_sources(self):
        expected=json.loads((ROOT/'catalog.json').read_text())
        self.assertEqual(kb.build(),expected)
    def test_backlinks_and_sources_resolve(self):
        cat=kb.build();by_id={e['id']:e for e in cat['entries']}
        for e in cat['entries']:
            for target in e['related']:
                self.assertIn(e['id'],by_id[target]['backlinks'])
    def test_privacy_guard(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'_chat.txt').write_text('synthetic')
            with self.assertRaises(ValueError):kb.privacy_scan(root)
    def test_internal_links(self):kb.check_links()

class RetrievalScenarios(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.catalog=kb.build();cls.by_id={e['id']:e for e in cls.catalog['entries']}
    def reachable(self,initial):
        found=set(initial)
        for _ in range(2):
            found |= {target for id in list(found) for target in self.by_id[id]['related']+self.by_id[id]['backlinks']}
        return found
    def scenario(self,query,targets):
        hits=kb.search(self.catalog,query,limit=5)
        self.assertTrue(hits)
        reach=self.reachable([e['id'] for e in hits])
        self.assertTrue(set(targets)<=reach,(query,targets,[e['id'] for e in hits]))
    def test_A_personal_assistant(self):
        self.scenario('asistente memoria persistente modelos intercambiables',['portable-memory','model-routing','bounded-autonomy','build-your-agent'])
    def test_B_parallel_coding(self):
        self.scenario('coding agents paralelo worktree',['worktree-per-agent','multi-agent-orchestration','cross-model-review','agentic-coding'])
    def test_C_autonomous_risks(self):
        self.scenario('riesgos agentes autonomos alignment',['autonomous-risk','permission-enforcement','alignment-training','functional-emotions'])
    def test_progressive_reading_not_full_repository(self):
        hits=kb.search(self.catalog,'memoria persistente',limit=3)
        self.assertEqual(len(hits),3)
        self.assertLess(len(hits),len(self.catalog['entries'])/10)
    def test_type_and_no_results(self):
        self.assertTrue(all(e['type']=='tool' for e in kb.search(self.catalog,'memoria',kind='tool')))
        self.assertEqual(kb.search(self.catalog,'zyxwvu-no-match'),[])

class IngestTests(unittest.TestCase):
    # All records are fictional, with identities excluded from expected output.
    CHAT='[01/01/2026, 10:00:00] Synthetic A: memoria portable\nsegunda linea\n\u200e[01/01/2026, 10:01:00] Synthetic B: orquestar agentes\n[01/01/2026, 10:02:00] System event\n'
    def test_ios_bidi_and_multiline(self):
        rows=ingest.parse(self.CHAT)
        self.assertEqual(len(rows),3)
        self.assertEqual(rows[0][2],'memoria portable\nsegunda linea')
        self.assertIsNone(rows[2][2])
    def test_android(self):
        self.assertEqual(ingest.parse('01/01/2026, 10:00 - Synthetic A: memoria\n')[0][2],'memoria')
    def test_overlap_no_new_records(self):
        rows=ingest.parse(self.CHAT)
        first,state=ingest.inventory(rows,{})
        second,state=ingest.inventory(rows,state)
        self.assertEqual(first['new_records'],2)
        self.assertEqual(second['new_records'],0)
        extended=ingest.parse(self.CHAT+'[02/01/2026, 10:00:00] Synthetic A: permisos\n')
        third,_=ingest.inventory(extended,state)
        self.assertEqual(third['new_records'],1)
    def test_duplicate_and_edited(self):
        rows=ingest.parse(self.CHAT)
        report,state=ingest.inventory(rows+[rows[0]],{})
        self.assertEqual(report['duplicate_records'],1)
        report,_=ingest.inventory([(rows[0][0],rows[0][1],'modified')],state)
        self.assertEqual(report['new_records'],1)
    def test_no_private_contents_in_report(self):
        report,state=ingest.inventory(ingest.parse(self.CHAT),{})
        text=json.dumps(report)+json.dumps(state)
        self.assertNotIn('Synthetic',text)
        self.assertNotIn('segunda linea',text)
        self.assertNotIn('memoria portable',text)
    def test_unknown_format_and_repo_paths_rejected(self):
        with self.assertRaises(ValueError):ingest.parse('unsupported')
        with self.assertRaises(ValueError):ingest.outside_repo(ROOT/'private')
    def test_zip_and_secure_state(self):
        import zipfile,stat
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);path=root/'export.zip'
            with zipfile.ZipFile(path,'w') as z:z.writestr('_chat.txt',self.CHAT)
            self.assertEqual(ingest.read_export(path),self.CHAT)
            ingest.secure_write(root/'state.json',{'synthetic':True})
            self.assertEqual((root/'state.json').stat().st_mode&0o777,0o600)
            with zipfile.ZipFile(path,'a') as z:z.writestr('other.txt','x')
            with self.assertRaises(ValueError):ingest.read_export(path)

if __name__=='__main__':unittest.main()
