from .model import Model
from .utils import split_model

class InternVLModel(Model):
    def __init__(self, model_path):
        self.device_map = split_model(model_path)
        self.model = AutoModel.from_pretrained(
            model_path,
            dtype=torch.bfloat16,
            # use_flash_attn=True,
            attn_implementation="flash_attention_2",
            load_in_8bit=False,
            low_cpu_mem_usage=True,
            trust_remote_code=True,
            device_map=self.device_map,
        ).eval()

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path, trust_remote_code=True, use_fast=False
        )

        self.default_generation_config = {
            "do_sample": False,
            "max_new_tokens": 8192,
            "top_p": 1.0,
            "temperature": 0.0,
            "repetition_penalty": 1,
            "num_beams": 1,
        }
    
    def generate(self, question: str, images: list[str] | None = None, **kwargs) -> str:
        generation_config = self.default_generation_config.copy()
        generation_config.update(kwargs)
        pixel_values = None
        if images:
            pixel_values = get_pixel_values(images)
        
        response = self.model.chat(
            self.tokenizer, pixel_values, question, generation_config, history=None
        )
        return response
        