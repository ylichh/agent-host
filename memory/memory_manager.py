from abc import ABC, abstractmethod


class MemoryManagerInterface(ABC):
    @abstractmethod
    def add_message(self, message: dict):
        pass

    @property
    @abstractmethod
    def messages(self) -> list[dict]:
        pass


class InMemoryManager(MemoryManagerInterface):
    def __init__(self):
        self._messages = []

    def add_message(self, message: dict):
        self._messages.append(message)

    @property
    def messages(self) -> list[dict]:
        return self._messages
