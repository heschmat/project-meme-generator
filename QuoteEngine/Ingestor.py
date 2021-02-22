from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CSVIngestor, TXTIngestor, PDFIngestor]
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        # If the file format is not supported, return empty list
        return []