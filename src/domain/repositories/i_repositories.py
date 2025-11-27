from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.entities import Usuario

class IUserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[Usuario]:
        pass
    
    @abstractmethod
    def create_user(self, user: Usuario) -> Usuario:
        pass

