from datetime import datetime

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from src.domain.services.agent.i_agent import IAgent
from src.domain.entities import UserInteraction, AssistantResponse, Message
from src.adapters.langchain.weather_tool import obtener_tiempo
from src.adapters.utilities.openai_utilities import parse_to_openai_spec


class Agent(IAgent):
    def __init__(
        self,
        system_prompt: str,
        openai_key: str,
        model: str,
    ):

        self.agent_model = ChatOpenAI(api_key=openai_key, model=model)
        self.agent = create_agent(model=self.agent_model, tools=[obtener_tiempo])
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
