from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """PDF strategy object."""
    
    def parse(self, path):
        
        list_of_quotes = []
        
        p = subprocess.run(['pdftotext', path['-']], stdout=subprocess.PIPE)
        output, err = p.communicate()
        
        # output should be our text file, no?
        
        # If text-file is ´-’, the text is sent to stdout.
        
        with open(output, 'r') as infile:
            lines_of_text = infile.readlines()
            
        for line in lines_of_text:
            
            dash_location = line.find('-')
            
            body = line[:dash_location]
            author = line[dash_location:]
            
            list_of_quotes.append(QuoteModel(body, author))
            
        return list_of_quotes