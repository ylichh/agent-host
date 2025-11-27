import os
from dotenv import load_dotenv

from src.aplicacion.app import Supervisor
from src.infraestructure.external_services.openai_manager import OpenAiManager
from src.aplicacion.answer_message import AnswerMessage
from src.infraestructure.adapter.wheather import WheaterAgent

AGENT_PROMPT = """Eres un asistente que coordina herramientas 
para responder preguntas de los usuarios.
Debes decidir si es necesario utilizar una herramienta y qué herramienta 
utilizar para responder la pregunta del usuario"""
if __name__ == "__main__":
    load_dotenv()
    use_case = AnswerMessage()
