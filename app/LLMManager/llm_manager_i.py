from abc import abstractmethod, ABC


class LLMManagerInterface(ABC):

    @abstractmethod
    def get_client(self):
        pass

    @abstractmethod
    def get_response(self, messages, tools: list[dict]):
        pass
