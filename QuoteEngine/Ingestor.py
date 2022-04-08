from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor

class Ingestor(IngestorInterface):
    """Use control flow to return a specific ingestor class."""

    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]
        
    @classmethod
    def parse(cls, path):
        """Select the appropriate helper for a given file based on filetype."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
                
    # see: https://knowledge.udacity.com/questions/559464