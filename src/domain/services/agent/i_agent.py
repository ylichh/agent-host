from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.repositories.i_memory import IConversationMemory
from src.domain.entities import UserInteraction, Message


class IAgent(ABC):
    @abstractmethod
    def answer_question(self, question: UserInteraction, conversation: list) -> Message:
        pass
