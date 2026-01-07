from core_logger import get_logger

logger = get_logger("search-service")


def index_document(doc_id: str) -> None:
    logger.info("document_indexed", doc_id=doc_id)


def main() -> None:
    index_document("doc-001")


if __name__ == "__main__":
    main()
