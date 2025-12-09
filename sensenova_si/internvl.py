import os
from typing import Any

import torch
from transformers import AutoModel, AutoTokenizer

from .model import Model
from .utils import load_image, split_model


class SenseNovaSIInternVLModel(Model):
    def __init__(
        self,
        model_path: str,
        generation_config: dict[str, Any] | str | os.PathLike | None = None,
    ):
        super().__init__(generation_config)
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

    def generate(self, question: str, images: list[str] | None = None, **kwargs) -> str:
        generation_config = self.default_generation_config.copy()
        generation_config.update(kwargs)
        pixel_values = None
        if images:
            pixel_values = self.get_pixel_values(images)

        # print(generation_config)
        response = self.model.chat(
            self.tokenizer, pixel_values, question, generation_config, history=None
        )
        return response

    def get_pixel_values(self, image_paths):
        pixel_values_list = []
        print(f"Load {len(image_paths)} images...")
        for path in image_paths:
            print(f"Load image {path}...")
            try:
                pixel_values_list.append(
                    load_image(path, max_num=12).to(torch.bfloat16).cuda()
                )
            except Exception as e:
                print(f"Error loading image {path}: {e}")
                continue

        if len(pixel_values_list) > 1:
            pixel_values = torch.cat(pixel_values_list, dim=0)
        elif len(pixel_values_list) == 1:
            pixel_values = pixel_values_list[0]
        else:
            raise ValueError(f"No valid images found in {image_paths}")
        return pixel_values
