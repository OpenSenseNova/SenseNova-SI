from abc import ABC, abstractmethod
import os
import yaml
from typing import Any
from pathlib import Path

class Model(ABC):
    def __init__(self, generation_config: dict[str, Any] | str | os.PathLike | None = None):
        if generation_config is None:
            generation_config = Path(__file__).parents[1] / "config" / "generation_config.yaml"
        if isinstance(generation_config, str | os.PathLike):
            with open(generation_config, "r") as f:
                self.generation_config = yaml.safe_load(f)
        elif isinstance(generation_config, dict):
            self.generation_config = generation_config
        else:
            raise ValueError(f"Invalid generation config: {generation_config}")
        print("Generation config:", self.generation_config)
    
    @abstractmethod
    def generate(self, question: str, images: list[str] | None = None, **kwargs) -> str:
        raise NotImplementedError