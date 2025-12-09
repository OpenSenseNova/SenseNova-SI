import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import yaml


class Model(ABC):
    def __init__(
        self, generation_config: dict[str, Any] | str | os.PathLike | None = None
    ):
        if generation_config is None:
            generation_config = Path(__file__).parents[1] / "config" / "default.yaml"
        if isinstance(generation_config, str | os.PathLike):
            with open(generation_config, "r") as f:
                self.default_generation_config = yaml.safe_load(f).get(
                    "default_generation_config", {}
                )
        elif isinstance(generation_config, dict):
            self.default_generation_config = generation_config.copy()
        else:
            raise ValueError(f"Invalid generation config: {generation_config}")

    @abstractmethod
    def generate(self, question: str, images: list[str] | None = None, **kwargs) -> str:
        raise NotImplementedError
