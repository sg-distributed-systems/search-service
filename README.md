# search-service

Handles search and document indexing operations.

## Why this repo exists

Search functionality requires specialized infrastructure for indexing and querying, separate from transactional databases used by other services.

## Core Components

### `index_document(doc_id: str)`
Indexes a document to make it searchable.

**Logs:**
- `document_indexed` — Logged when a document is successfully added to the search index

## HTTP Interface

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Liveness probe |
| `/readyz` | GET | Readiness probe |
| `/search/index` | POST | Indexes a document |

### Running the service

```bash
uvicorn src.search_service.app:app --host 0.0.0.0 --port 8007
```
