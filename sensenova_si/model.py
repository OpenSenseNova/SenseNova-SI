from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def generate(self, question: str, images: list[str] | None = None, **kwargs) -> str:
        raise NotImplementedError