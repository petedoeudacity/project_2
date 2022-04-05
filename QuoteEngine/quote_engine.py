from abc import ABC, abstractmethod


class QuoteModel:
    
    def __init__(self, body, author):
        body = self.body
        author = self.author
        
    def __str__(self):
        return f"'{body}' - {author}"
        

class IngestorInterface(ABC):
    
    @classmethod
    def can_ingest(cls, path):
        """Verify *path* compatility with *ingestor class*:
        a) determine file type using string analysis
        b) verify that the file type corresponods to the name
            of the class
        """
        if path[-4] == '.':
            if path[-3] == 'c':
                filetype = 'csv'
            if path[-3] == 'p':
                filetype = 'pdf':
            if path[-3] == 't':
                filetype ='txt'
        else:
            filetype = 'docx'
        
        if cls.__name__ == file_type + 'Ingestor':
            return True
        
        else:
            return False
    
    @abstractmethod
    def parse(cls, path: str):
        pass
    
class csvIngestor(IngestorInterface):
    
    
    
    
    
    
class docxIngestor(IngestorInterface):
    
    
    
class pdfIngestor(IngestorInterface):
    

    
class txtIngestor(IngestorInterface):
    
    
    
    
    
class Ingestor(IngestorInterface):
    
    
        
    