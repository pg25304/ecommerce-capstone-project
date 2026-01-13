"""The BaseRepository class will serve as an abstract base class or blueprint for all repositories in your project.
 This will help demonstrate inheritance by providing shared behaviors and enforcing a consistent API."""
# data/base_repository.py
from abc import ABC, abstractmethod

class BaseRepository(ABC):
    """Base class for all repositories."""

    @abstractmethod
    def save(self, entity):
        """Save an entity to the repository."""
        pass

    @abstractmethod
    def find(self, identifier):
        """Find an entity by an identifier."""
        pass