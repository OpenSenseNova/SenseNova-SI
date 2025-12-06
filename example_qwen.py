import argparse
import json
import torch

from transformers import (
    AutoProcessor,
    Qwen3VLForConditionalGeneration,
    Qwen2_5_VLForConditionalGeneration,
)


def set_seed(seed=42):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)


def get_response(model, processor, messages, generation_config):
    inputs = processor.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_dict=True,
        return_tensors="pt",
    )
    inputs = inputs.to(model.device)
    generated_ids = model.generate(**inputs, **generation_config)
    generated_ids_trimmed = [
        out_ids[len(in_ids) :]
        for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False,
    )
    return output_text


if __name__ == "__main__":
    set_seed()

    parser = argparse.ArgumentParser(
        description="Examples for SenseNova-SI single-run MCQ"
    )
    parser.add_argument(
        "--model_path",
        type=str,
        default="sensenova/SenseNova-SI-1.1-Qwen3-VL-8B",
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
        default="Please describe the image in detail.",
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

    if "Qwen3-VL" in model_path:
        model = Qwen3VLForConditionalGeneration.from_pretrained(
            model_path,
            dtype="auto",
            device_map="auto",
            trust_remote_code=True,
        ).eval()
    elif "Qwen2.5-VL" in model_path:
        model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            model_path,
            dtype="auto",
            device_map="auto",
            trust_remote_code=True,
        ).eval()

    processor = AutoProcessor.from_pretrained(
        model_path, trust_remote_code=True, use_fast=False
    )

    generation_config = {
        "do_sample": False,
        "max_new_tokens": 8192,
        "top_p": 1.0,
        "repetition_penalty": 1,
        "num_beams": 1,
    }

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

                question = question.replace("<image>", "").strip()
                content_images = [
                    {"type": "image_url", "data": {"url": img_path}}
                    for img_path in image_paths
                ]
                contents = content_images + [{"type": "text", "text": question}]
                messages = [{"role": "user", "content": contents}]

                print(f"Processing question id: {id_}")
                response = get_response(model, processor, messages, generation_config)
                print(f"User: {question}")
                print(f"Assistant: {response}")
                print(f"Ground Truth: {gt}")
                print("-" * 50)
    else:
        question = args.question
        image_contents = [
            {"type": "image_url", "data": {"url": img_path}}
            for img_path in args.image_paths
        ]
        contents = image_contents + [{"type": "text", "text": question}]
        messages = [{"role": "user", "content": contents}]
        response = get_response(model, processor, messages, generation_config)
        print(response)
