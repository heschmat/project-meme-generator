from typing import List
import pandas as pd

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    available_formats = ['csv']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception!')
            
        quotes = []
        df = pd.read_csv(path)
        for row in df.values:
            quote, author = row
            quotes.append(QuoteModel(quote, author))
        
        return quotes
