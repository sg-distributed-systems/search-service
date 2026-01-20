"""
Service entrypoint with lifecycle management.

Initializes configuration, correlation ID, and signal handlers before running
the main service logic. Provides structured error handling for all exceptions.
"""
from core_logger import get_logger

from search_service.config import load_config
from search_service.errors import AppError
from search_service.lifecycle import install_signal_handlers
from search_service.observability import init_correlation_id

logger = get_logger("search-service")


def index_document(doc_id: str) -> None:
    logger.info("document_indexed", doc_id=doc_id)


def run() -> None:
    cfg = load_config("search-service")
    cid = init_correlation_id()
    install_signal_handlers("search-service")

    logger.info("service_starting", env=cfg.env, correlation_id=cid)

    try:
        index_document("doc-001")
        logger.info("service_completed")
    except AppError as e:
        logger.warning("app_error", **e.to_log_fields())
        raise
    except Exception as e:
        logger.exception("unhandled_exception", exc=e)
        raise


def main() -> None:
    run()


if __name__ == "__main__":
    main()
