from pydantic import BaseModel


class IndexDocumentRequest(BaseModel):
    doc_id: str


class IndexDocumentResponse(BaseModel):
    status: str
