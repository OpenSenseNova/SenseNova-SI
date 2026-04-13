# Training SenseNova-SI-Qwen3-VL-8B

This document covers fine-tuning SenseNova-SI models on the **SenseNova-SI-800K** spatial intelligence dataset.

The training framework is [lmms-engine](https://github.com/EvolvingLMMs-Lab/lmms-engine), included as a git submodule under `training/lmms-engine/`.

## Directory layout

```
training/
├── lmms-engine/          # lmms-engine
└── qwen3_vl/
    ├── run.sh            # one-click launch script
    ├── train_config.yaml # full training config
    └── data.yaml         # dataset config template
```

## Quick start

### Step 1 — Install dependencies

```bash
# Initialize the lmms-engine submodule (first time only)
git submodule update --init --recursive

# From the repo root, inside your existing venv / conda env
pip install -e training/lmms-engine

# Optional: Performance optimizations
pip install flash-attn --no-build-isolation
pip install liger-kernel
```

### Step 2 — Download SenseNova-SI-800K

```bash
hf download sensenova/SenseNova-SI-800K \
  --repo-type dataset \
  --local-dir data/SenseNova-SI-800K
```

The dataset contains a single `SenseNova-SI-800K.jsonl` file plus image files referenced by relative paths inside it.

### Step 3 - Prepare dataset YAML
```YAML
datasets:
  - path: /path/to/SenseNova-SI-800K/SenseNova-SI-800K.jsonl
    data_folder: /path/to/SenseNova-SI-800K/
    data_type: jsonl
```

### Step 4 - Configure training
See [training/qwen3_vl/train_config.yaml](training/qwen3_vl/train_config.yaml)

### Step 5 — Launch training

```bash
# Single node, 8 GPUs (default)
bash training/qwen3_vl/run.sh
```

## Data format

SenseNova-SI-800K uses the same JSONL format as the training data described in the main README:

```json
{
  "id": 0,
  "conversations": [
    {"from": "human", "value": "<image>\nQuestion text"},
    {"from": "gpt",   "value": "Answer text"}
  ],
  "image": ["relative/path/to/image.jpg"]
}
```

`data_folder` in `data.yaml` is prepended to every relative image path.
