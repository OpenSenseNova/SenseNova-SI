import math

import torch
import torchvision.transforms as T
from PIL import Image
from torchvision.transforms.functional import InterpolationMode
from transformers import AutoConfig

IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)


def to_openai_format(
    question: str, images: list[str] | None = None, image_token: str = "<image>"
):
    if images is None:
        images = []
    content = []
    text_split = question.split(image_token)
    assert len(text_split) == len(images) + 1, (
        f"Number of images {len(images)} does not match number of text splits {len(text_split)}"
    )
    for i, text in enumerate(text_split):
        text = text.strip()
        if text:
            content.append({"type": "text", "text": text})
        if i < len(images):
            content.append({"type": "image", "image": images[i]})
    return [{"role": "user", "content": content}]


def reorganize_prompt(message, image_num):
    if image_num == 1:
        prompt = "<image>\n" + "\n".join(
            [x["value"] for x in message if x["type"] == "text"]
        )
    else:
        prompt = ""
        for x in message:
            if x["type"] == "text":
                prompt += x["value"]
        prompt = (
            "".join([f"Image-{i + 1}: <image>\n" for i in range(image_num)]) + prompt
        )
    return prompt


def build_transform(input_size):
    MEAN, STD = IMAGENET_MEAN, IMAGENET_STD
    transform = T.Compose(
        [
            T.Lambda(lambda img: img.convert("RGB") if img.mode != "RGB" else img),
            T.Resize((input_size, input_size), interpolation=InterpolationMode.BICUBIC),
            T.ToTensor(),
            T.Normalize(mean=MEAN, std=STD),
        ]
    )
    return transform


def find_closest_aspect_ratio(aspect_ratio, target_ratios, width, height, image_size):
    best_ratio_diff = float("inf")
    best_ratio = (1, 1)
    area = width * height
    for ratio in target_ratios:
        target_aspect_ratio = ratio[0] / ratio[1]
        ratio_diff = abs(aspect_ratio - target_aspect_ratio)
        if ratio_diff < best_ratio_diff:
            best_ratio_diff = ratio_diff
            best_ratio = ratio
        elif ratio_diff == best_ratio_diff:
            if area > 0.5 * image_size * image_size * ratio[0] * ratio[1]:
                best_ratio = ratio
    return best_ratio


def dynamic_preprocess(
    image, min_num=1, max_num=6, image_size=448, use_thumbnail=False
):
    orig_width, orig_height = image.size
    aspect_ratio = orig_width / orig_height

    # calculate the existing image aspect ratio
    target_ratios = set(
        (i, j)
        for n in range(min_num, max_num + 1)
        for i in range(1, n + 1)
        for j in range(1, n + 1)
        if i * j <= max_num and i * j >= min_num
    )
    target_ratios = sorted(target_ratios, key=lambda x: x[0] * x[1])

    # find the closest aspect ratio to the target
    target_aspect_ratio = find_closest_aspect_ratio(
        aspect_ratio, target_ratios, orig_width, orig_height, image_size
    )

    # calculate the target width and height
    target_width = image_size * target_aspect_ratio[0]
    target_height = image_size * target_aspect_ratio[1]
    blocks = target_aspect_ratio[0] * target_aspect_ratio[1]

    # resize the image
    resized_img = image.resize((target_width, target_height))
    processed_images = []
    for i in range(blocks):
        box = (
            (i % (target_width // image_size)) * image_size,
            (i // (target_width // image_size)) * image_size,
            ((i % (target_width // image_size)) + 1) * image_size,
            ((i // (target_width // image_size)) + 1) * image_size,
        )
        # split the image
        split_img = resized_img.crop(box)
        processed_images.append(split_img)
    assert len(processed_images) == blocks
    if use_thumbnail and len(processed_images) != 1:
        thumbnail_img = image.resize((image_size, image_size))
        processed_images.append(thumbnail_img)
    return processed_images


def load_image(image_file, input_size=448, max_num=6):
    image = Image.open(image_file).convert("RGB")
    transform = build_transform(input_size=input_size)
    images = dynamic_preprocess(
        image, image_size=input_size, use_thumbnail=True, max_num=max_num
    )
    pixel_values = [transform(image) for image in images]
    pixel_values = torch.stack(pixel_values)
    return pixel_values


def split_model(model_name):
    device_map = {}
    world_size = torch.cuda.device_count()
    config = AutoConfig.from_pretrained(model_name, trust_remote_code=True)
    num_layers = config.llm_config.num_hidden_layers
    # Since the first GPU will be used for ViT, treat it as half a GPU.
    num_layers_per_gpu = math.ceil(num_layers / (world_size - 0.5))
    num_layers_per_gpu = [num_layers_per_gpu] * world_size
    num_layers_per_gpu[0] = math.ceil(num_layers_per_gpu[0] * 0.5)
    layer_cnt = 0
    for i, num_layer in enumerate(num_layers_per_gpu):
        for j in range(num_layer):
            device_map[f"language_model.model.layers.{layer_cnt}"] = i
            layer_cnt += 1
    device_map["vision_model"] = 0
    device_map["mlp1"] = 0
    device_map["language_model.model.tok_embeddings"] = 0
    device_map["language_model.model.embed_tokens"] = 0
    device_map["language_model.output"] = 0
    device_map["language_model.model.norm"] = 0
    device_map["language_model.model.rotary_emb"] = 0
    device_map["language_model.lm_head"] = 0
    device_map[f"language_model.model.layers.{num_layers - 1}"] = 0

    return device_map


def add_special_tokens(tokenizer):
    all_special_tokens = []
    for k, v in tokenizer.special_tokens_map.items():
        if isinstance(v, str):
            all_special_tokens.append(v)
        elif isinstance(v, list):
            all_special_tokens += v

    new_tokens = []

    if "<|im_start|>" not in all_special_tokens:
        new_tokens.append("<|im_start|>")

    if "<|im_end|>" not in all_special_tokens:
        new_tokens.append("<|im_end|>")

    if "<|vision_start|>" not in all_special_tokens:
        new_tokens.append("<|vision_start|>")

    if "<|vision_end|>" not in all_special_tokens:
        new_tokens.append("<|vision_end|>")

    num_new_tokens = tokenizer.add_tokens(new_tokens)
    bos_token_id = tokenizer.convert_tokens_to_ids("<|im_start|>")
    eos_token_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
    start_of_image = tokenizer.convert_tokens_to_ids("<|vision_start|>")
    end_of_image = tokenizer.convert_tokens_to_ids("<|vision_end|>")

    new_token_ids = dict(
        bos_token_id=bos_token_id,
        eos_token_id=eos_token_id,
        start_of_image=start_of_image,
        end_of_image=end_of_image,
    )

    return tokenizer, new_token_ids, num_new_tokens
