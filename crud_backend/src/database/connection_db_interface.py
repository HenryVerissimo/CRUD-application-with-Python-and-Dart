from typing import Self
from abc import ABC, abstractmethod


class ConnectionDBInterface(ABC):
    """Interface used to create database connection classes"""

    @abstractmethod
    def create_connection(self, *args, **Kwargs):
        pass

    @abstractmethod
    def __enter__(self) -> Self:
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass
