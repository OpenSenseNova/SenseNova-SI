from abc import ABC, abstractmethod
from transformers import AutoModel

class Model(ABC):
    @abstractmethod
    def generate(self, question: str, images: list[str] | None = None, **kwargs) -> str:
        raise NotImplementedError