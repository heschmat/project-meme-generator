"""Ingest CSV file format. Create a list of `QuoteModel` objects."""
from typing import List
import pandas as pd

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """Convert CSV files to a list of `QuoteModel` objects."""
    
    available_formats = ['csv']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV files."""
        if not cls.can_ingest(path):
            raise Exception('Expected CSV format. Please check the file.')
            
        quotes = []
        df = pd.read_csv(path)
        for row in df.values:
            quote, author = row
            quotes.append(QuoteModel(quote, author))
        
        return quotes
