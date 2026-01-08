import os
from dotenv import load_dotenv
from datetime import datetime
from src.adapters.langchain.weather_tool import WeatherTool
from src.adapters.langchain.langchain_agent import Agent

from src.aplicacion.answer_message import AnswerMessage
from src.infraestructure.memory.in_memory_conversation_manager import InMemoryManager
from src.adapters.langchain.climate_description_tool import RabbitMQClient
from src.domain.entities import UserInteraction
from constants import OrchestationConstants

AGENT_PROMPT = """Eres un asistente que coordina herramientas 
para responder preguntas de los usuarios.
Puedes utilizar la herramienta obtener_tiempo para responder a las preguntas sobre el clima.
Si la tool de tiempo no te responde en ese caso utiliza la tool del clima
al menos asi puedes darle una estimación vaga del tiempo de la ciudad"""
if __name__ == "__main__":
    load_dotenv()
    ###Tools
    weather_tool = WeatherTool()
    rabbit_mq_client = RabbitMQClient(
        rabbitmq_server=os.environ.get("RABBIT_MQ_HOST"),
        rabbitmq_port=os.environ.get("RABBIT_MQ_PORT"),
        rabbitmq_username=os.environ.get("RABBIT_MQ_USERNAME"),
        rabbitmq_password=os.environ.get("RABBIT_MQ_PASSWORD"),
    )
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
        weather_tool=weather_tool,
        climate_tool=rabbit_mq_client,
    )
    use_case = AnswerMessage(
        agent=agente, conversation_manager=conversation_memory_manager
    )
    date = datetime.now()
    user_interaction = UserInteraction(
        user_id=user_id, text="Que tiempo hace en paris", timestamp=date
    )
    print(use_case.execute(user_interaction=user_interaction))
