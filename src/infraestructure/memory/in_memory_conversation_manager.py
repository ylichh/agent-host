from src.domain.repositories.i_memory import IConversationMemory
from src.domain.entities import Message


class InMemoryManager(IConversationMemory):
    def __init__(self):
        self.conversation: dict[str, list[Message]] = {}

    def get_conversation_by_user_id(self, user_id):
        return self.conversation[user_id]

    def add_message(self, message_text, emitter, user_id):
        self.conversation[user_id].append(
            Message(
                order=len(self.conversation),
                text=message_text,
                emitter=emitter,
            )
        )

    def add_user_message(self, message_text, user_id):
        self.add_message(message_text, "user", user_id)

    def add_assistant_message(self, message_text, user_id):
        self.add_message(message_text, "assistant", user_id)

    def create_conversation(self, user_id: str):
        self.conversation[user_id] = []
