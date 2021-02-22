class QuoteModel:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    def __repr__(self) -> str:
        return f'{self.quote} -- {self.author}'