import os
from dotenv import load_dotenv

from src.aplicacion.app import Supervisor
from src.infraestructure.external_services.openai_manager import OpenAiManager
from src.infraestructure.memory.in_memory_manager import InMemoryManager
from src.infraestructure.adapter.wheather import WheaterAgent

AGENT_PROMPT = """Eres un asistente que coordina herramientas 
para responder preguntas de los usuarios.
Debes decidir si es necesario utilizar una herramienta y qué herramienta 
utilizar para responder la pregunta del usuario"""

if __name__ == "__main__":
    load_dotenv()
    agent_prompt = AGENT_PROMPT
    supervisor = Supervisor(
        llm_manager=OpenAiManager(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            gpt_model=os.getenv("OPENAI_GENERATION_MODEL", "gpt-4o"),
        ),
        memory_manager=InMemoryManager(),
        agent_prompt=agent_prompt,
    )
    supervisor.register_tool(agent=WheaterAgent(name="WheaterAgent"))

    supervisor.run("Que tiempo hace en paris?")
