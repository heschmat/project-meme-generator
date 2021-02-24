from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Convert ms word documents to a list of `QuoteModel` objects."""
    available_formats = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse ms word documents."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception!')

        quotes = []
        doc = docx.Document(path)
        for row in doc.paragraphs:
            if row.text == '':
                continue
            quote, author = row.text.split('-')
            quotes.append(QuoteModel(quote.strip(), author.strip()))
        
        return quotes