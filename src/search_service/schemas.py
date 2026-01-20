"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from typing import Dict, List

from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    id: str
    title: str
    score: float


class SearchRequest(BaseModel):
    query: str
    filters: Dict = Field(default_factory=dict)
    page: int = Field(ge=1, default=1)
    page_size: int = Field(ge=1, le=100, default=20)


class SearchResponse(BaseModel):
    results: List[SearchResult]
    total_count: int
    took_ms: float
