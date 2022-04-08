from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Abstract base class to build ingestor interface."""
    
    @classmethod
    def can_ingest(cls, path):
        """Verify *path* compatility with *ingestor class*:
        a) determine file type using string analysis
        b) verify that the file type is ingestable; return True
        """
        if path[-4] == '.':
            if path[-3:] == 'csv':
                return True
            if path[-3:] == 'pdf':
                return True
            if path[-3:] == 'txt':
                return True
        else:
            if path[-5] == '.':
                if path[-4:] == 'docx':
                    return True
    
    @abstractmethod
    def parse(cls, path):
        pass