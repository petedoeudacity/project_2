from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

import csv

class CSVIngestor(IngestorInterface):
    """CSV strategy object."""
    
    allowed_extensions = ['csv']
    
    @classmethod
    def parse(self, path):
        
        list_of_quotes = []
        
        with open(path, 'r') as infile:
            reader = csv.reader(infile)
            next(reader) # skip body, author heading
            
            for row in reader:
                
                body = row[0]
                author = row[1]
                list_of_quotes.append(QuoteModel(body, author))
                
        return list_of_quotes