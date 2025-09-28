import json

from ..domain.services.tools.i_tool import Tool

# Assuming WheaterAgent is defined in tools/wheather.py
from ..domain.repositories.i_memory import (
    IMemory,
)  # Assuming you have a memory manager defined
from ..domain.services.llm_manager.i_llm_manager import ILLMManager

GPT_MODEL = "gpt-4.1"

AGENT_PROMPT = """Eres un asistente que coordina herramientas 
para responder preguntas de los usuarios.
Debes decidir si es necesario utilizar una herramienta y qué herramienta 
utilizar para responder la pregunta del usuario"""


class Supervisor:

    def __init__(
        self,
        llm_manager: ILLMManager,
        memory_manager: IMemory,
        agent_prompt,
    ):
        self.name = "Supervisor"
        self.llm_manager = llm_manager
        self.memory_manager = memory_manager
        self.tools: dict[str, Tool] = {}
        self.agent_prompt = agent_prompt
        self.memory_manager.add_message(
            {"role": "assistant", "content": self.agent_prompt}
        )

    def register_tool(self, agent: Tool):
        """Register a tool with the supervisor."""
        self.tools[agent.name] = agent

    def call_function(self, tool_call):
        name = tool_call.name
        args = json.loads(tool_call.arguments)

        result = self.tools.get(name).execute(args)
        return result

    def append_message(self, role, message):
        self.memory_manager.add_message({"role": role, "content": message})

    def manage_call(self, call, original_output_text):
        if call.type == "function_call":
            result = self.call_function(call)
            self.memory_manager.add_message(call)
            self.memory_manager.add_message(
                {
                    "type": "function_call_output",
                    "call_id": call.call_id,
                    "output": json.dumps(result),
                }
            )
            _, output_text = self.llm_manager.get_response(
                self.memory_manager.messages, self.tools
            )
            self.append_message("assistant", output_text)
            print(output_text)

        if call.type == "message":
            self.append_message("assistant", original_output_text)
            print(original_output_text)

    def run(self, user_message):
        # --------- Paso 1: Enviamos el mensaje del usuario a GPT ---------
        self.append_message("user", user_message)

        output, output_text = self.llm_manager.get_response(
            self.memory_manager.messages, self.tools
        )

        for call in output:
            self.manage_call(call, output_text)
