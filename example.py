import argparse
import json

import torch
from transformers import AutoModel, AutoTokenizer

from utils import load_image, split_model


def set_seed(seed=42):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)


def get_pixel_values(image_paths):
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


if __name__ == "__main__":
    set_seed()

    parser = argparse.ArgumentParser(
        description="Examples for SenseNova-SI single-run MCQ"
    )
    parser.add_argument(
        "--model_path",
        type=str,
        default="sensenova/SenseNova-SI-1.1-InternVL3-8B",
        help="Model path",
    )
    parser.add_argument(
        "--image_paths",
        type=str,
        nargs="+",
        default=[],
        help="Path to image files, can specify multiple",
    )
    parser.add_argument(
        "--question",
        type=str,
        default="<image>\nPlease describe the image in detail.",
        help="Question to ask the model",
    )
    parser.add_argument(
        "--jsonl_path",
        type=str,
        default=None,
        help="Path to jsonl file containing examples",
    )
    args = parser.parse_args()

    model_path = args.model_path

    device_map = split_model(model_path)
    model = AutoModel.from_pretrained(
        model_path,
        dtype=torch.bfloat16,
        # use_flash_attn=True,
        attn_implementation="flash_attention_2",
        load_in_8bit=False,
        low_cpu_mem_usage=True,
        trust_remote_code=True,
        device_map=device_map,
    ).eval()

    tokenizer = AutoTokenizer.from_pretrained(
        model_path, trust_remote_code=True, use_fast=False
    )

    generation_config = dict(
        do_sample=False,
        max_new_tokens=8192,
        top_p=1.0,
        temperature=0.0,
        repetition_penalty=1,
        num_beams=1,
    )

    if args.jsonl_path:
        with open(args.jsonl_path, "r") as f:
            for line in f:
                entry = json.loads(line.strip())
                image_paths = entry.get("image", [])
                conversations = entry.get("conversations", [])
                if conversations:
                    question = conversations[0].get("value", "")
                else:
                    question = ""
                id_ = entry.get("id", "")
                gt = entry.get("GT", "")

                if not image_paths or not question:
                    print(f"Skipping invalid entry id {id_}")
                    continue

                print(f"Processing question id: {id_}")
                pixel_values = get_pixel_values(image_paths)
                response = model.chat(
                    tokenizer, pixel_values, question, generation_config, history=None
                )
                print(f"User: {question}")
                print(f"Assistant: {response}")
                print(f"Ground Truth: {gt}")
                print("-" * 50)
    else:
        question = args.question
        pixel_values = None
        if len(args.image_paths) > 0:
            pixel_values = get_pixel_values(args.image_paths)

        response = model.chat(
            tokenizer, pixel_values, question, generation_config, history=None
        )
        print(f"User: {question}")
        print(f"Assistant: {response}")
