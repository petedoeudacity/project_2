from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

import docx

class DocxIngestor(IngestorInterface):
    """DOCX strategy object."""
    def parse(self, path):
        
        list_of_quotes = []
        lines_of_text = []
    
        document = docx.Document(path)
        
        for para in document.paragraphs:
            lines_of_text.append(para.text)
            
        for line in lines_of_text:
            
            dash_location = line.find('-')
            
            body = line[:dash_location]
            author = line[dash_location:]
            
            list_of_quotes.append(QuoteModel(body, author))
        
        return list_of_quotes