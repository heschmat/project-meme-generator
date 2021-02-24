"""Ingest PDF file format. Create a list of `QuoteModel` objects."""
from typing import List

import subprocess
import os
from time import time

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Convert PDF file to a list of `QuoteModel` objects."""
    
    available_formats = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF file to a list of `QuoteModel` objects."""
        if not cls.can_ingest(path):
            raise Exception('Expected PDF format. Please check the file.')
        
        # Utilize a CLI tool, pdftotext, to convert PDF to TXT file.
        path_tmp = f'./tmp{int(time())}.txt'
        call = subprocess.call(['pdftotext', path, path_tmp])
        
        with open(path_tmp, 'r') as f:
            quotes = []
            
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) == 0:
                    continue
                res = line.split('-')
                quotes.append(QuoteModel(res[0].strip(), res[1].strip()))
                
        os.remove(path_tmp)

        return quotes
