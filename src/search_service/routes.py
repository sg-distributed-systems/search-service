"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .schemas import SearchRequest, SearchResponse
from .service import search

router = APIRouter()


@router.post("/search", response_model=SearchResponse, status_code=200)
def search_route(req: SearchRequest) -> SearchResponse:
    result = search(
        query=req.query,
        filters=req.filters,
        page=req.page,
        page_size=req.page_size,
    )
    return SearchResponse(
        results=result["results"],
        total_count=result["total_count"],
        took_ms=result["took_ms"],
    )
