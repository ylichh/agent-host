from src.domain.services.llm_manager.i_llm_manager import ILLMManager
from ...domain.services.tools.i_tool import Tool
from openai import OpenAI


class OpenAiManager(ILLMManager):
    def __init__(self, openai_api_key: str, gpt_model: str):
        self.client = OpenAI(api_key=openai_api_key)
        self.gpt_model = gpt_model

    def get_client(self):
        return self.client

    def get_response(self, messages, tools: list[Tool]):
        response = self.client.responses.create(
            model=self.gpt_model,
            tools=[
                tool.tool_information.model_dump() for tool in tools.values()
            ],
            input=messages,
        )
        output_text = response.output_text
        output = response.output

        return output, output_text
