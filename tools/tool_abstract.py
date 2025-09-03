from abc import ABC, abstractmethod
from tools.tool_schemas import FunctionSchema


class Tool(ABC):
    @property
    @abstractmethod
    def tool_information(self) -> FunctionSchema:
        """Return the tool information."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the tool."""
        pass

    @abstractmethod
    def execute(self, **kwargs):
        pass
