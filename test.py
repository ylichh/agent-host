from supervisor import Supervisor
from LLMManager.openai_manager import OpenAiManager
from memory.memory_manager import InMemoryManager
from tools.wheather import (
    WheaterAgent,
)  # Assuming WheaterAgent is defined in tools/wheather.py
import os

if __name__ == "__main__":
    AGENT_PROMPT = """Eres un asistente que coordina herramientas para responder preguntas de los usuarios.
Debes decidir si es necesario utilizar una herramienta y qué herramienta utilizar para responder la pregunta del usuario"""

    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your-default-key")
    # Asumiendo que MemoryManager está definido en memory/memory_manager.py
    weather_agent = WheaterAgent(
        name="WeatherTool"
    )  # Asumiendo que WheaterAgent está definido en tools/wheather.py
    supervisor = Supervisor(
        llm_manager=OpenAiManager(
            openai_api_key=os.getenv("OPENAI_API_KEY"), gpt_model="gpt-4.1"
        ),
        memory_manager=InMemoryManager(),
        agent_prompt=AGENT_PROMPT,
    )
    supervisor.register_tool(weather_agent)

    user_input = "¿Cuál es el clima en Barcelona?"
    supervisor.run(user_input)

    supervisor = Supervisor(
        llm_manager=OpenAiManager(
            openai_api_key=os.getenv("OPENAI_API_KEY"), gpt_model="gpt-4.1"
        ),
        memory_manager=InMemoryManager(),
        agent_prompt=AGENT_PROMPT,
    )
    supervisor.register_tool(weather_agent)

    user_input = "Hola, como hago pan?"
    supervisor.run(user_input)
    pass
