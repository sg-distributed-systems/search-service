# search-service

Handles search and document indexing operations.

## Why this repo exists

Search functionality requires specialized infrastructure for indexing and querying, separate from transactional databases used by other services.

## Core Components

### `index_document(doc_id: str)`
Indexes a document to make it searchable.

**Logs:**
- `document_indexed` — Logged when a document is successfully added to the search index

### `load_config(service_name: str) -> ServiceConfig`
Loads service configuration from environment variables including `APP_ENV` and `SHUTDOWN_TIMEOUT_SECONDS`.

### `AppError`
Base exception class for application errors. Provides `to_log_fields()` for structured error logging.

### `install_signal_handlers(service_logger_name: str)`
Installs SIGINT/SIGTERM handlers for graceful shutdown with logging.

### `init_correlation_id() -> str`
Initializes a correlation ID from the `CORRELATION_ID` environment variable or generates a UUID4.

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
