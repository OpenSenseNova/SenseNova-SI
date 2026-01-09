import os
from typing import Any

import torch
from transformers import AutoModel, AutoTokenizer

from .model import Model
from .utils import load_image, reorganize_prompt, split_model


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

        self.max_num_per_image = 6
        self.total_max_num = 64

    def generate(self, question: str, images: list[str] | None = None, **kwargs) -> str:
        generation_config = self.default_generation_config.copy()
        generation_config.update(kwargs)

        # generate prompt
        message = []
        if images:
            for _ in images:
                message.append({"type": "image", "value": ""})
        message.append({"type": "text", "value": question})

        images_num = len(images) if images else 0

        prompt = reorganize_prompt(message, images_num)

        pixel_values, num_patches_list = None, []
        if images:
            pixel_values, num_patches_list = self.get_pixel_values(images)

        # print(generation_config)
        response = self.model.chat(
            self.tokenizer,
            pixel_values=pixel_values,
            num_patches_list=num_patches_list,
            question=prompt,
            generation_config=generation_config,
            history=None,
        )
        return response

    def get_pixel_values(self, image_paths):
        pixel_values_list = []
        num_patches_list = []

        # dynamic max number
        if len(image_paths) > 1:
            max_num = max(
                1, min(self.max_num_per_image, self.total_max_num // len(image_paths))
            )
        else:
            max_num = self.max_num_per_image

        print(f"Load {len(image_paths)} images...")
        for path in image_paths:
            print(f"Load image {path}...")
            try:
                pixel_values = (
                    load_image(path, max_num=max_num).to(torch.bfloat16).cuda()
                )
                num_patches_list.append(pixel_values.size(0))
                pixel_values_list.append(pixel_values)
            except Exception as e:
                print(f"Error loading image {path}: {e}")
                continue

        if len(pixel_values_list) > 1:
            pixel_values = torch.cat(pixel_values_list, dim=0)
        elif len(pixel_values_list) == 1:
            pixel_values = pixel_values_list[0]
        else:
            raise ValueError(f"No valid images found in {image_paths}")
        return pixel_values, num_patches_list
