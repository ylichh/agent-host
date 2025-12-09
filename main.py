import os
from dotenv import load_dotenv
from datetime import datetime
from src.adapters.langchain.langchain_agent import Agent
from src.aplicacion.answer_message import AnswerMessage
from src.infraestructure.memory.in_memory_conversation_manager import InMemoryManager
from src.domain.entities import UserInteraction
from constants import OrchestationConstants

AGENT_PROMPT = """Eres un asistente que coordina herramientas 
para responder preguntas de los usuarios.
Puedes utilizar la herramienta obtener_tiempo para responder a las preguntas sobre el clima"""
if __name__ == "__main__":
    load_dotenv()
    llm_server = os.environ.get(OrchestationConstants.OPENAI_KEY)
    system_prompt = AGENT_PROMPT
    model = os.environ.get(OrchestationConstants.LLM_MODEL)
    user_id = "random_id"
    conversation_memory_manager = InMemoryManager()
    conversation_memory_manager.create_conversation(user_id)
    agente = Agent(
        openai_key=llm_server,
        system_prompt=system_prompt,
        model=model,
    )
    use_case = AnswerMessage(
        agent=agente, conversation_manager=conversation_memory_manager
    )
    date = datetime.now()
    user_interaction = UserInteraction(
        user_id=user_id, text="Que tiempo hace en lima", timestamp=date
    )
    print(use_case.execute(user_interaction=user_interaction))
