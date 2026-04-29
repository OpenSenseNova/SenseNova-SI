"""Preprocess SenseNova-SI dataset JSONL into lmms-engine compatible format.

This script fixes two schema incompatibilities:
1. `image` mixed types (`str` and `list[str]`) -> normalized to `list[str]`.
2. `conversations` format -> converted to `messages` with structured `content`.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def normalize_image_field(sample: dict[str, Any]) -> bool:
    """Normalize `image` to list[str] for Arrow/HF Dataset compatibility."""
    image = sample.get("image")

    if isinstance(image, str):
        sample["image"] = [image]
        return True

    if isinstance(image, list):
        return False

    if image is None:
        return False

    raise ValueError(f"Unsupported image type: {type(image).__name__}")


def map_conversations_to_messages(sample: dict[str, Any]) -> bool:
    """Convert OpenAI-like `conversations` into lmms-engine `messages`."""
    conversations = sample.get("conversations")
    if conversations is None:
        return False

    if not isinstance(conversations, list):
        raise ValueError("`conversations` must be a list.")

    mapped_messages: list[dict[str, Any]] = []
    for conversation in conversations:
        if not isinstance(conversation, dict):
            raise ValueError("Each `conversations` item must be an object.")

        sender = conversation.get("from")
        text = conversation.get("value", "")

        if sender == "human":
            role = "user"
        elif sender == "gpt":
            role = "assistant"
        else:
            role = str(sender) if sender is not None else "user"

        mapped_messages.append(
            {
                "role": role,
                "content": [{"type": "text", "text": text}],
            }
        )

    sample["messages"] = mapped_messages
    del sample["conversations"]
    return True


def default_output_path(src_path: Path) -> Path:
    """Build default output path with `_qwen3vl_format` suffix."""
    return src_path.with_name(
        f"{src_path.stem}_qwen3vl_format{src_path.suffix or '.jsonl'}"
    )


def preprocess_jsonl(src_path: Path, dst_path: Path) -> None:
    """Read JSONL, normalize each sample, and write mapped JSONL."""
    image_fixed_count = 0
    conversation_fixed_count = 0
    total_count = 0

    dst_path.parent.mkdir(parents=True, exist_ok=True)

    with (
        src_path.open("r", encoding="utf-8") as source,
        dst_path.open("w", encoding="utf-8") as target,
    ):
        for line_number, line in enumerate(source, start=1):
            stripped = line.strip()
            if not stripped:
                continue

            try:
                sample = json.loads(stripped)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid JSON at line {line_number}: {error}"
                ) from error

            if not isinstance(sample, dict):
                raise ValueError(f"Line {line_number} is not a JSON object.")

            if normalize_image_field(sample):
                image_fixed_count += 1
            if map_conversations_to_messages(sample):
                conversation_fixed_count += 1

            target.write(json.dumps(sample, ensure_ascii=False) + "\n")
            total_count += 1

    print(
        "Done."
        f" total={total_count},"
        f" image_fixed={image_fixed_count},"
        f" conversations_mapped={conversation_fixed_count},"
        f" output='{dst_path}'"
    )


def build_args() -> argparse.Namespace:
    """Build and parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Preprocess SenseNova-SI dataset JSONL for lmms-engine training."
    )
    parser.add_argument(
        "--src",
        required=True,
        type=Path,
        help="Path to original SenseNova-SI dataset JSONL.",
    )
    parser.add_argument(
        "--dst",
        type=Path,
        default=None,
        help="Output JSONL path. Default: <src_stem>_qwen3vl_format.jsonl",
    )
    return parser.parse_args()


def main() -> None:
    """Script entrypoint."""
    args = build_args()
    dst_path = args.dst if args.dst is not None else default_output_path(args.src)
    preprocess_jsonl(src_path=args.src, dst_path=dst_path)


if __name__ == "__main__":
    main()
