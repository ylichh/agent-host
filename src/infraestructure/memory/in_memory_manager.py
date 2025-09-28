from ...domain.repositories.i_memory import IMemory


class InMemoryManager(IMemory):
    def __init__(self):
        self._messages = []

    def add_message(self, message: dict):
        self._messages.append(message)

    @property
    def messages(self) -> list[dict]:
        return self._messages
