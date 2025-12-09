from .internvl import SenseNovaSIInternVLModel
from .qwen import SenseNovaSIQwenModel


def get_default_model_type(model_path):
    if "qwen" in model_path.lower():
        return "qwen"
    elif "internvl" in model_path.lower():
        return "internvl"
    else:
        raise ValueError(f"Unknown model type for {model_path}")


def get_model(model_path, model_type="auto"):
    if model_type == "auto":
        model_type = get_default_model_type(model_path)
    if model_type == "qwen":
        return SenseNovaSIQwenModel(model_path)
    elif model_type == "internvl":
        return SenseNovaSIInternVLModel(model_path)
    else:
        raise ValueError(f"Unknown model type: {model_type}")


__all__ = [
    "get_default_model_type",
    "get_model",
    "SenseNovaSIInternVLModel",
    "SenseNovaSIQwenModel",
]
