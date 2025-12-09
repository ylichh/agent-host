###El agente responde la pregunta
from src.domain.services.agent.i_agent import IAgent
from src.domain.repositories.i_memory import IConversationMemory
from src.domain.entities import UserInteraction


class AnswerMessage:
    def __init__(self, agent: IAgent, conversation_manager: IConversationMemory):
        self.agent = agent
        self.conversation_manager = conversation_manager

    def execute(self, user_interaction: UserInteraction):
        self.conversation_manager.create_conversation(user_interaction.user_id)
        stored_messages = self.conversation_manager.get_conversation_by_user_id(
            user_interaction.user_id
        )
        try:
            agent_answer = self.agent.answer_question(user_interaction, stored_messages)
            self.conversation_manager.add_user_message(
                user_interaction.text, user_interaction.user_id
            )
            self.conversation_manager.add_assistant_message(
                user_interaction.text, user_interaction.user_id
            )
            return agent_answer.text
        except Exception as e:
            return "error"
