"""Ingest TXT file format. Create a list of `QuoteModel` objects."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Convert text file to a list of `QuoteModel` objects."""
    
    available_formats = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt file to a list of `QuoteModel` objects."""
        if not cls.can_ingest(path):
            raise Exception('Expected TXT format. Please check the file.')

        quotes = []
        with open(path, 'r') as f:
            content = f.readlines()
        for row in content:
            quote, author = row.split('- ')
            quotes.append(QuoteModel(quote.strip(), author.strip()))

        return quotes