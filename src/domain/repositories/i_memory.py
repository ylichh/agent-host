from abc import ABC, abstractmethod
from src.domain.entities import Message


class IConversationMemory(ABC):
    @abstractmethod
    def add_message(self, message_text: str, emitter: str, user_id: str):
        pass

    @abstractmethod
    def add_user_message(self, message_text: str, user_id: str):
        pass

    @abstractmethod
    def add_assistant_message(self, message_text: str, user_id: str):
        pass

    @abstractmethod
    def get_conversation_by_user_id(self, user_id: str) -> list[Message]:
        pass

    @abstractmethod
    def create_conversation(self, user_id: str) -> bool:
        pass
