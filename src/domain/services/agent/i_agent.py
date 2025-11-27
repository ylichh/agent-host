from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.repositories.i_memory import IMemory
from src.domain.entities import UserInteraction, Message


class IAgent(ABC):
    @abstractmethod
    def answer_question(
        self, question: UserInteraction, memory_manager=IMemory
    ) -> Message:
        pass
