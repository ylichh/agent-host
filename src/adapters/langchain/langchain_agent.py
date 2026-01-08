from datetime import datetime

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from src.domain.services.agent.i_agent import IAgent
from src.domain.entities import UserInteraction, AssistantResponse, Message
from src.adapters.utilities.openai_utilities import parse_to_openai_spec
from src.adapters.langchain.i_tool import ILangTool
from src.adapters.langchain.tool_creation import (
    crear_obtener_clima,
    crear_obtener_tiempo,
)


class Agent(IAgent):
    def __init__(
        self,
        system_prompt: str,
        openai_key: str,
        model: str,
        weather_tool: ILangTool,
        climate_tool: ILangTool,
    ):
        weather_tool = weather_tool
        climate_tool = climate_tool

        self.agent_model = ChatOpenAI(api_key=openai_key, model=model)
        self.agent = create_agent(
            model=self.agent_model,
            tools=[
                crear_obtener_tiempo(weather_tool),
                crear_obtener_clima(climate_tool),
            ],
        )
        self.prompt = system_prompt

    def answer_question(
        self, user_interaction: UserInteraction, stored_messages: list[Message]
    ):
        conversation = parse_to_openai_spec(
            self.prompt, stored_messages, user_interaction.text
        )
        try:
            response = self.agent.invoke(conversation)
            assistant_response = response["messages"][-1].content
            return AssistantResponse(
                text=assistant_response, payload={}, timestamp=datetime.now()
            )
        except Exception as e:
            raise e
