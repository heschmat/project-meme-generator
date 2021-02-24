"""Encapsulate the quotes fetched from files."""
class QuoteModel:
    """Encapsulate the body/quote and author."""
    
    def __init__(self, quote, author):
        """Initialize by getting the quote and author."""
        self.body = quote
        self.author = author

    def __repr__(self) -> str:
        """Respresent quotes like: 'this is quote. -- the author'."""
        return f'{self.body} -- {self.author}'