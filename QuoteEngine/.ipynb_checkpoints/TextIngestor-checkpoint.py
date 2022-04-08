from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    """TXT strategy object."""
    
    def parse(self, path):
        
        list_of_quotes = []
        lines_of_text = []
        
        with open(path, 'r') as infile:
            lines_of_text = infile.readlines()
            
        for line in lines_of_text:
            
            dash_location = line.find('-')
            
            body = line[:dash_location]
            author = line[dash_location:]
            
            list_of_quotes.append(QuoteModel(body, author))
            
        return list_of_quotes