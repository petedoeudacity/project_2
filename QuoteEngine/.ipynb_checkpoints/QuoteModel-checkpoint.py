class QuoteModel:
    """Encapsulates a quote."""
    
    def __init__(self, body, author):
        self.body = body
        self.author = author
        
    def __repr__(self):
        """ return ”body text” - author """
        return f'\"{self.body}\" - {self.author}'
    
    def __str__(self):
        """Return 'str(self)'."""
        return self.body + " - " + self.author