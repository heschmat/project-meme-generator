from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    available_formats = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception!')

        quotes = []
        with open(path, 'r') as f:
            content = f.readlines()
        for row in content:
            quote, author = row.split('- ')
            quotes.append(QuoteModel(quote.strip(), author.strip()))

        return quotes