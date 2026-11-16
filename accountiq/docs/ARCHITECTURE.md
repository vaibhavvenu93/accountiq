# Architecture

Browser (Next.js) → HTTP POST /score (FastAPI) → deterministic Python scoring → fictional JSON account store.

The API validates ICP inputs. The scoring engine is isolated from transport and data storage, enabling unit tests and future connectors. Signal records contain type, description, strength, observed_at, source_url. A URL field does not itself prove a source is trustworthy: future versions must verify retrieval, provenance, freshness, and deduplication.

## Security considerations
- No secrets are required in v0.1.
- CORS is restricted to localhost:3000 for local development.
- No emails are sent and no third-party websites are scraped.
- Before deployment: add auth, rate limiting, production CORS, persistent storage and access controls.
