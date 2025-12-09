import argparse
import json

import torch

from sensenova_si import get_model


def set_seed(seed=42):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)


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
    parser.add_argument(
        "--model_type",
        type=str,
        default="auto",
        choices=["qwen", "internvl", "auto"],
        help="Model type",
    )
    args = parser.parse_args()

    model_path = args.model_path
    model = get_model(model_path, model_type=args.model_type)

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
                response = model.generate(question, images=image_paths)
                print(f"User: {question}")
                print(f"Assistant: {response}")
                print(f"Ground Truth: {gt}")
                print("-" * 50)
    else:
        question = args.question
        response = model.generate(question, images=args.image_paths)
        print(f"User: {question}")
        print(f"Assistant: {response}")
