from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class Usuario:
    user_id: str
    name: str
    email: Optional[str] = None


@dataclass
class UserInteraction:
    user_id: str
    text: str
    timestamp: datetime


@dataclass
class Message:
    order: str
    text: str
    payload: dict
    timestamp: datetime
    emitter: str  # "bot" o "user"


@dataclass
class Conversacion:
    id: str
    user_id: str
    mensajes: List[Message]
