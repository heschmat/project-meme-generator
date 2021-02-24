"""Abstract Base Class for the Ingestors responsible for parsing files."""
from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract Base Class for parsing external files."""
    
    available_formats = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Make sure if file format matches the parser."""
        ext = path.split('.')[-1]
        return ext in cls.available_formats

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parser is implemented in sub-classes based on the file format.""" 
        pass