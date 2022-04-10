from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Abstract base class to build ingestor interface."""
    
    allowed_extensions = []
    
    @classmethod
    def can_ingest(cls, path):
        """Verify *path* compatility with *ingestor class*:
        a) determine file type using string analysis
        b) verify that the file type is ingestable; return True
        """
        ext = path.split('.')[-1]
        if ext == cls.allowed_extensions[0]:
            return True

    @abstractmethod
    def parse(cls, path):
        pass