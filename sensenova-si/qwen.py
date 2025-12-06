from .model import Model
from .utils import to_openai_format 
from transformers import AutoModel, AutoProcessor

class Qwen(Model):
    def __init__(self, model_path: str):
        self.model = AutoModel.from_pretrained(model_path)
        self.processor = AutoProcessor.from_pretrained(model_path)
        self.default_generation_config = {
            "do_sample": False,
            "max_new_tokens": 8192,
            "top_p": 1.0,
            "repetition_penalty": 1,
            "num_beams": 1,
        }
    
    def generate(self, question: str, images: list[str] | None = None, **kwargs) -> str:
        generation_config = self.default_generation_config.copy()
        generation_config.update(kwargs)
        openai_style_input = to_openai_format(question, images)
        inputs = self.processor.apply_chat_template(openai_style_input, tokenize=True, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(self.model.device)
        generated_ids = self.model.generate(**inputs, **generation_config)
        generated_ids_trimmed = [
            out_ids[len(in_ids) :]
            for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
        ]
        output_text = self.processor.batch_decode(
            generated_ids_trimmed,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False,
        )
        return output_text

