class QuoteModel:
    """Encapsulate the body/quote and author."""
    def __init__(self, quote, author):
        self.body = quote
        self.author = author

    def __repr__(self) -> str:
        return f'{self.body} -- {self.author}'