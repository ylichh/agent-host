from ...domain.services.tools.i_tool import Tool
from ...domain.services.tools.tool_schemas import (
    Parameters,
    Property,
    FunctionSchema,
)


class WheaterAgent(Tool):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def tool_information(self) -> FunctionSchema:
        return FunctionSchema(
            type="function",
            name=self.name,
            description="Provides weather information for a given location.",
            parameters=Parameters(
                type="object",
                properties={
                    "location": Property(
                        type="string",
                        description="The location to get the weather for",
                    ),
                },
                required=["location"],
                additionalProperties=False,
            ),
            strict=True,
        )

    def execute(self, location):
        # Simulate a weather API call

        result = location | {
            "temperature": 20,
            "condition": "Sunny",
        }

        return result
