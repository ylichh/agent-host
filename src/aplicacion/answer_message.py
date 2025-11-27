###El agente responde la pregunta
from src.domain.services.agent.i_agent import IAgent
from src.domain.repositories.i_memory import IMemory
from src.domain.entities import UserInteraction


class AnswerMessage:
    def __init__(self, agent: IAgent, memory_manager=IMemory):
        self.agent = agent
        self.memory_manager = memory_manager

    def execute(self, question: UserInteraction, memory_manager: IMemory):
        stored_messages = memory_manager.messages
        agent_answer = self.agent.answer_question(question, memory_manager)
        return agent_answer
