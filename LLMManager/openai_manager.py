from LLMManager.llm_manager_i import LLMManagerInterface
from tools.tool_abstract import Tool
from openai import OpenAI


class OpenAiManager(LLMManagerInterface):
    def __init__(self, openai_api_key=None, gpt_model=None):
        self.client = OpenAI(api_key=openai_api_key)
        self.gpt_model = gpt_model

    def get_client(self):
        return self.client

    def get_response(self, messages, tools: list[Tool]):
        response = self.client.responses.create(
            model=self.gpt_model,
            tools=[tool.tool_information.model_dump() for tool in tools.values()],
            input=messages,
        )
        output_text = response.output_text
        output = response.output

        return output, output_text
