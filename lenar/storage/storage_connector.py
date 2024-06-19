from abc import ABC, abstractmethod
from typing import Any


class StorageConnector(ABC):

    @abstractmethod
    def __init__(self, client: Any):
        self.client = client

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def find(self, *args, **kwargs):
        pass

    @abstractmethod
    def insert_one(self, *args, **kwargs):
        pass
