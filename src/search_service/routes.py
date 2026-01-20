"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .main import index_document
from .schemas import IndexDocumentRequest, IndexDocumentResponse

router = APIRouter()


@router.post("/search/index", response_model=IndexDocumentResponse)
def index_document_route(req: IndexDocumentRequest) -> IndexDocumentResponse:
    index_document(req.doc_id)
    return IndexDocumentResponse(status="ok")
