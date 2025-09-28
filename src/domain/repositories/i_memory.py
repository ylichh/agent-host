from abc import ABC, abstractmethod


class IMemory(ABC):
    @abstractmethod
    def add_message(self, message: dict):
        pass

    @property
    @abstractmethod
    def messages(self) -> list[dict]:
        pass
