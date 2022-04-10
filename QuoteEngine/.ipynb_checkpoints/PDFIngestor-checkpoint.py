from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

import subprocess
import random
import os

class PDFIngestor(IngestorInterface):
    """PDF strategy object."""
    
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(self, path):
        
        quotes = []
        
        try:
            
            tmp = f'./_data/DogQuotes/{random.randint(0, 1000)}.txt'
            call = subprocess.call(['pdftotext', path, tmp])
            file_ref = open(tmp, "r")
            
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0].strip(),
                                           parse[1].strip())
                    quotes.append(new_quote)
            file_ref.close()
            os.remove(tmp)
            
        except Exception as e:
            raise Exception("pdf parsing issue occured.")
            
        return quotes
    
    
# https://knowledge.udacity.com/questions/572306