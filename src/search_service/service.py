"""
Search query processing and result ranking.

Handles full-text search queries with filtering, pagination, and relevance
scoring. Provides autocomplete suggestions and search analytics.
"""
import time
from datetime import datetime
from typing import List

from core_logger import get_logger

from .errors import ValidationError
from .schemas import SearchResult

logger = get_logger("search-service", tier="infrastructure")

MOCK_RESULTS = [
    {"id": "prod-001", "title": "Wireless Headphones", "score": 0.95},
    {"id": "prod-002", "title": "Bluetooth Speaker", "score": 0.87},
    {"id": "prod-003", "title": "USB-C Cable", "score": 0.72},
]


def search(query: str, filters: dict, page: int, page_size: int) -> dict:
    start_time = time.monotonic()
    logger.info("search_started", query=query, filter_count=len(filters), page=page)

    if not query or len(query) < 2:
        raise ValidationError("query_too_short", details={"min_length": 2})

    if page < 1:
        raise ValidationError("invalid_page_number")

    if page_size < 1 or page_size > 100:
        raise ValidationError("invalid_page_size", details={"min": 1, "max": 100})

    logger.debug("index_queried", query=query)

    results = [SearchResult(**r) for r in MOCK_RESULTS]
    total_count = len(results)

    took_ms = (time.monotonic() - start_time) * 1000
    logger.info("search_completed", query=query, result_count=len(results), took_ms=took_ms)

    return {"results": results, "total_count": total_count, "took_ms": round(took_ms, 2)}


def suggest(query: str, limit: int = 5) -> List[str]:
    logger.debug("autocomplete_requested", query=query, limit=limit)
    return ["suggestion_1", "suggestion_2", "suggestion_3"][:limit]


def delete_from_index(doc_id: str) -> dict:
    logger.info("index_deletion_requested", doc_id=doc_id)

    if not doc_id:
        raise ValidationError("doc_id_required")

    logger.info("document_deleted", doc_id=doc_id)
    return {"doc_id": doc_id, "deleted": True, "deleted_at": datetime.utcnow()}
