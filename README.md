# AccountIQ — Evidence-first GTM intelligence

> Prioritise the right accounts, understand why they matter, and inspect the evidence behind every recommendation.

**Status:** v0.1 demonstration. **All account and signal data is fictional.** No live enrichment, web research, outreach or CRM sync is implemented yet.

## Why this exists
Most outbound software focuses on writing more messages. AccountIQ starts earlier: which accounts deserve attention, what signals support that decision, and how can a GTM operator verify the reasoning?

## Working features
- Interactive Next.js account intelligence dashboard
- FastAPI scoring endpoint with configurable industry, geography and headcount ICP
- Deterministic 100-point scoring with transparent component breakdown
- Source URL and observation date fields for signals (demo URLs are placeholders)
- 12 explicitly fictional companies across SaaS, agencies and freight
- Python unit tests and GitHub Actions CI

## Quick start
Requires Python 3.10+ and Node 20+.

**Terminal 1 — API**
```bash
cd services/api
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Terminal 2 — dashboard**
```bash
cd apps/web
npm install
npm run dev
```
Visit http://localhost:3000. API documentation: http://localhost:8000/docs.

**Tests**
```bash
python -m unittest discover -s tests -v
```

## Scoring formula
Industry match (30) + employee-size fit (20) + region match (15) + capped signal strength (25) + evidenced-signal count (10). This is an illustrative heuristic, **not a validated probability of conversion**. See [methodology](docs/GTM_METHODOLOGY.md).

## Roadmap
- v0.2: CSV import, saved ICP profiles, account briefs
- v0.3: permitted public data connectors, real provenance and freshness controls
- v0.4: model-assisted GTM hypotheses with human approval and grounded evaluations
- v0.5: CRM integrations and audit trail

## Provenance
This implementation is written as an original demonstration using standard open-source frameworks. It does not incorporate code from the previously discussed prospecting-agent repository. See [UPSTREAM.md](UPSTREAM.md).

## Author
[vaibhavvenu93](https://github.com/vaibhavvenu93) · GTM Engineering Lab · 8Labs

## License
MIT. See LICENSE.
