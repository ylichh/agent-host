from dataclasses import dataclass, field
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
class AssistantResponse:
    text: str
    payload: dict
    timestamp: datetime


@dataclass
class Message:
    order: int
    text: str
    emitter: str  # "bot" o "user"
    payload: dict = field(default_factory=dict)
    timestamp: datetime = None


@dataclass
class Conversacion:
    id: str
    user_id: str
    mensajes: List[Message]
