import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

import torch
from accelerate import (
    infer_auto_device_map,
    init_empty_weights,
    load_checkpoint_and_dispatch,
)
from huggingface_hub import snapshot_download
from PIL import Image

from .bagel_utils.data.transforms import ImageTransform
from .bagel_utils.inferencer import InterleaveInferencer
from .bagel_utils.modeling.autoencoder import load_ae
from .bagel_utils.modeling.bagel import (
    Bagel,
    BagelConfig,
    Qwen2Config,
    Qwen2ForCausalLM,
    SiglipVisionConfig,
    SiglipVisionModel,
)
from .bagel_utils.modeling.qwen2 import Qwen2Tokenizer
from .model import Model
from .utils import add_special_tokens

BASE_PARAMS: Dict[str, Dict[str, Any]] = {
    "generate": dict(
        cfg_text_scale=4.0,
        cfg_img_scale=1.0,
        cfg_interval=[0.4, 1.0],
        timestep_shift=3.0,
        num_timesteps=50,
        cfg_renorm_min=1.0,
        cfg_renorm_type="global",
    ),
    "think_generate": dict(
        max_think_token_n=1000,
        do_sample=False,
        cfg_text_scale=4.0,
        cfg_img_scale=1.0,
        cfg_interval=[0.4, 1.0],
        timestep_shift=3.0,
        num_timesteps=50,
        cfg_renorm_min=1.0,
        cfg_renorm_type="global",
        think=True,
    ),
    "edit": dict(
        cfg_text_scale=4.0,
        cfg_img_scale=2.0,
        cfg_interval=[0.0, 1.0],
        timestep_shift=3.0,
        num_timesteps=50,
        cfg_renorm_min=0.0,
        cfg_renorm_type="text_channel",
    ),
    "think_edit": dict(
        max_think_token_n=1000,
        do_sample=False,
        cfg_text_scale=4.0,
        cfg_img_scale=2.0,
        cfg_interval=[0.0, 1.0],
        timestep_shift=3.0,
        num_timesteps=50,
        cfg_renorm_min=0.0,
        cfg_renorm_type="text_channel",
        think=True,
    ),
    "understanding": dict(
        max_think_token_n=1000,
        do_sample=False,
        understanding_output=True,
    ),
    "think_understanding": dict(
        max_think_token_n=1000,
        do_sample=False,
        understanding_output=True,
        think=True,
    ),
}


class SenseNovaSIBagelModel(Model):
    def __init__(
        self,
        model_path="sensenova/SenseNova-SI-1.1-BAGEL-7B-MoT",
        generation_config: dict[str, Any] | str | os.PathLike | None = None,
        mode="understanding",
        out_img_dir="./output_image/test_bagel/",
        dtype: str = "bf16",
    ):
        super().__init__(generation_config)
        # 1. Parse params
        self.precision = dtype

        cache_path = snapshot_download(repo_id=model_path)
        self.model_path = cache_path
        self.checkpoint_path = os.path.join(self.model_path, "model.safetensors")

        # Bagel mode
        env_mode = os.getenv("BAGEL_MODE")
        mode = env_mode.strip() if env_mode and env_mode.strip() else mode
        if mode not in BASE_PARAMS:
            raise ValueError(
                f"Invalid mode '{mode}'. "
                f"Bagel Supported modes: {list(BASE_PARAMS.keys())}"
            )
        self.mode = mode

        env_out_img_dir = os.getenv("BAGEL_OUT_IMG_DIR")
        self.out_img_dir = (
            env_out_img_dir.strip()
            if env_out_img_dir and env_out_img_dir.strip()
            else out_img_dir
        )

        msg = (
            f"[Bagel] mode = '{self.mode}' "
            f"(can be overridden with env var BAGEL_MODE); "
            f"out_img_dir = '{self.out_img_dir}' "
            f"(can be overridden with env var BAGEL_OUT_IMG_DIR)"
        )
        print(msg)

        # 2. Build model
        model, vae_model, tokenizer, new_token_ids, vit_transform, vae_transform = (
            self._build_model()
        )

        # 3. Load Checkpoint
        model = self._load_model_weights(model)

        # 4. Build inferencer
        self.tokenizer = tokenizer
        self.new_token_ids = new_token_ids
        self.vit_transform = vit_transform

        self.inferencer = InterleaveInferencer(
            model=model,
            vae_model=vae_model,
            tokenizer=tokenizer,
            vae_transform=vae_transform,
            vit_transform=vit_transform,
            new_token_ids=new_token_ids,
        )

        torch.cuda.empty_cache()

    def _build_model(self):
        # build llm config
        llm_config = Qwen2Config.from_json_file(
            os.path.join(self.model_path, "llm_config.json")
        )
        llm_config.qk_norm = True
        llm_config.tie_word_embeddings = False
        llm_config.layer_module = "Qwen2MoTDecoderLayer"

        # build vit config
        vit_config = SiglipVisionConfig.from_json_file(
            os.path.join(self.model_path, "vit_config.json")
        )
        vit_config.rope = False
        vit_config.num_hidden_layers -= 1

        vit_transform = ImageTransform(980, 224, 14)
        vae_transform = ImageTransform(1024, 512, 16)

        # build vae config
        vae_model, vae_config = load_ae(
            local_path=os.path.join(self.model_path, "ae.safetensors")
        )

        # build tokenizer
        tokenizer = Qwen2Tokenizer.from_pretrained(self.model_path)
        tokenizer, new_token_ids, _ = add_special_tokens(tokenizer)

        # build model
        model_config = BagelConfig(
            visual_gen=True,
            visual_und=True,
            llm_config=llm_config,
            vit_config=vit_config,
            vae_config=vae_config,
            latent_patch_size=2,
            max_latent_size=64,
            vit_max_num_patch_per_side=70,
            connector_act="gelu_pytorch_tanh",
        )

        with init_empty_weights():
            language_model = Qwen2ForCausalLM(llm_config)
            vit_model = SiglipVisionModel(vit_config)

            model = Bagel(language_model, vit_model, model_config)
            model.vit_model.vision_model.embeddings.convert_conv2d_to_linear(vit_config)

        return model, vae_model, tokenizer, new_token_ids, vit_transform, vae_transform

    def _load_model_weights(self, model):
        device_map = infer_auto_device_map(
            model, no_split_module_classes=["Bagel", "Qwen2MoTDecoderLayer"]
        )

        same_device_modules = [
            "language_model.model.embed_tokens",
            "time_embedder",
            "latent_pos_embed",
            "vae2llm",
            "llm2vae",
            "connector",
            "vit_pos_embed",
        ]

        if torch.cuda.device_count() == 1:
            first_device = device_map.get(same_device_modules[0], "cuda:0")
            for k in same_device_modules:
                if k in device_map:
                    device_map[k] = first_device
                else:
                    device_map[k] = "cuda:0"
        else:
            first_device = device_map.get(same_device_modules[0])
            for k in same_device_modules:
                if k in device_map:
                    device_map[k] = first_device

        if self.precision == "bf16":
            model = load_checkpoint_and_dispatch(
                model,
                checkpoint=self.checkpoint_path,
                device_map=device_map,
                offload_buffers=True,
                offload_folder="offload",
                dtype=torch.bfloat16,
                force_hooks=True,
            ).eval()

        elif self.precision == "nf4":
            from accelerate.utils import BnbQuantizationConfig, load_and_quantize_model

            model = load_and_quantize_model(
                model,
                weights_location=self.checkpoint_path,
                bnb_quantization_config=BnbQuantizationConfig(
                    load_in_4bit=True,
                    bnb_4bit_compute_dtype=torch.bfloat16,
                    bnb_4bit_use_double_quant=False,
                    bnb_4bit_quant_type="nf4",
                ),
                device_map=device_map,
                offload_folder="offload",
            ).eval()

        elif self.precision == "int8":
            from accelerate.utils import BnbQuantizationConfig, load_and_quantize_model

            model = load_and_quantize_model(
                model,
                weights_location=self.checkpoint_path,
                bnb_quantization_config=BnbQuantizationConfig(
                    load_in_8bit=True, torch_dtype=torch.float32
                ),
                device_map=device_map,
                offload_folder="offload",
            ).eval()

        else:
            raise NotImplementedError(f"Unsupported precision: {self.precision}")

        return model

    def _save_output_image(
        self,
        image: Image.Image,
        mode: str,
        img_path: Optional[str],
    ) -> str:
        if image is None:
            raise ValueError(
                f"[OutputError] Mode={mode} expected an image output, but got None."
            )

        root = Path(self.out_img_dir)
        images_root = root / (f"images")
        images_root.mkdir(parents=True, exist_ok=True)

        if mode in ["edit", "think_edit"]:
            if img_path:
                src = Path(img_path)
                parent_name = src.parent.name or "default"
                out_dir = images_root / parent_name
                out_dir.mkdir(parents=True, exist_ok=True)
                filename = src.name
            else:
                out_dir = images_root / "edit"
                out_dir.mkdir(parents=True, exist_ok=True)
                ts = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
                base = "sample"
                filename = f"{base}_edit_{ts}_{uuid.uuid4().hex[:8]}.jpg"

            out_path = out_dir / filename

        elif mode in ["generate", "think_generate"]:
            out_dir = images_root
            out_dir.mkdir(parents=True, exist_ok=True)

            ts = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
            base = "sample"
            filename = f"{base}_{ts}_{uuid.uuid4().hex[:8]}.jpg"
            out_path = out_dir / filename

        else:
            raise ValueError(f"[OutputError] Unexpected mode for image saving: {mode}")

        image.save(out_path)
        return str(out_path)

    def generate(self, question: str, images: list[str] | None = None, **kwargs):
        mode = self.mode

        images = images or []

        text_parts = question.split("<image>")
        if len(text_parts) != len(images) + 1:
            raise ValueError(f"Text iamge tokens and number of images not match! ")

        input_lists = []
        input_img_paths = []

        for i, part in enumerate(text_parts):
            text = part.strip()

            if text:
                input_lists.append(text)

            if i < len(images):
                img_path = images[i]
                try:
                    image = Image.open(img_path)
                    input_lists.append(image)
                    input_img_paths.append(img_path)
                except Exception as e:
                    raise RuntimeError(f"Can not load image {img_path}: {e}") from e

        params = dict(BASE_PARAMS[mode])
        understanding_output_flag = params.pop("understanding_output", False)
        think_flag = params.pop("think", False)

        res = self.inferencer.interleave_inference(
            input_lists=input_lists,
            think=think_flag,
            understanding_output=understanding_output_flag,
            **params,
        )

        ret = {"image": [], "text": []}
        for i in res:
            if isinstance(i, Image.Image):
                ret["image"].append(i)
            elif isinstance(i, str):
                ret["text"].append(i)

        img_cnt, txt_cnt = len(ret["image"]), len(ret["text"])
        if img_cnt + txt_cnt != 1:
            raise ValueError(
                f"[OutputError] Current expect exactly 1 image or 1 text. Got images={img_cnt}, texts={txt_cnt}"
            )

        ret["image"] = ret["image"][0] if img_cnt else None
        ret["text"] = ret["text"][0] if txt_cnt else None

        if mode in ["edit", "think_edit", "generate", "think_generate"]:
            if ret["image"] is not None:
                if len(input_img_paths) == 1:
                    ref_img_path = input_img_paths[0]
                else:
                    ref_img_path = None

                img_path_out = self._save_output_image(
                    image=ret["image"],
                    mode=mode,
                    img_path=ref_img_path,
                )
                ret["image"] = img_path_out
                res = img_path_out
            else:
                res = None
        else:
            res = ret["text"]

        return res
