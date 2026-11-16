import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'services/api'))
from scoring import score_account,rank_accounts
class ScoringTests(unittest.TestCase):
 def setUp(self):
  self.icp={'industries':['B2B SaaS'],'regions':['UK'],'min_employees':10,'max_employees':100}
  self.account={'name':'Example','industry':'B2B SaaS','region':'UK','employees':50,'signals':[{'strength':8,'source_url':'https://example.com','observed_at':'2026-11-01'}]}
 def test_components_sum(self):
  x=score_account(self.account,self.icp);self.assertEqual(x['score'],78);self.assertEqual(sum(x['components'].values()),78)
 def test_missing_evidence(self):
  a={**self.account,'signals':[{'strength':8}]};self.assertEqual(score_account(a,self.icp)['components']['evidence'],0)
 def test_cap(self):
  a={**self.account,'signals':[{'strength':10,'source_url':'x','observed_at':'today'}]*20};self.assertEqual(score_account(a,self.icp)['score'],100)
 def test_rank(self):
  bad={**self.account,'name':'Bad','industry':'Other','region':'US','employees':1000,'signals':[]};self.assertEqual(rank_accounts([bad,self.account],self.icp)[0]['name'],'Example')
 def test_demo_data(self):
  data=json.loads((ROOT/'data/demo/accounts.json').read_text());self.assertGreaterEqual(len(data),10);self.assertTrue(all(a['demo'] for a in data))
if __name__=='__main__':unittest.main()
