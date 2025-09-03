from abc import ABC, abstractmethod


# Add other required fields as necessary


class Agent(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        pass
