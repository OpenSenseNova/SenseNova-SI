#!/bin/bash
set -x

# ============================================================
# SenseNova-SI-8M Training with BAGEL-7B-MoT
# ============================================================
#
# Step 1: Download the dataset from Hugging Face:
#   pip install huggingface_hub
#   python -c "
#   from huggingface_hub import snapshot_download
#   snapshot_download(
#       repo_id='sensenova/SenseNova-SI-8M',
#       repo_type='dataset',
#       local_dir='data/SenseNova-SI-8M',
#   )
#   "
#
# Step 2: Download the BAGEL-7B-MoT model:
#   python -c "
#   from huggingface_hub import snapshot_download
#   snapshot_download(
#       repo_id='ByteDance-Seed/BAGEL-7B-MoT',
#       local_dir='models/BAGEL-7B-MoT',
#   )
#   "
#
# Step 3: Run this script from the bagel-train directory.
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(python -c 'import pathlib; print(pathlib.Path("'"${SCRIPT_DIR}"'").parent.resolve())')"
TRAINING_ROOT="$(python -c 'import pathlib; print(pathlib.Path("'"${REPO_DIR}"'").parent.resolve())')"
MODEL_PATH="${MODEL_PATH:-${TRAINING_ROOT}/pretrained_models/BAGEL-7B-MoT}"
NPROC_PER_NODE=${NPROC_PER_NODE:-8}
NNODES=${NNODES:-1}
RESULTS_DIR="${RESULTS_DIR:-${TRAINING_ROOT}/results/bagel/sensenova_si_8M}"
DATASET_CONFIG_FILE="${DATASET_CONFIG_FILE:-${REPO_DIR}/data/configs/sensenova_si_8M.yaml}"

export PYTHONPATH="${PYTHONPATH}:${REPO_DIR}"
export TRAINING_ROOT="${TRAINING_ROOT}"

cd "${REPO_DIR}"

torchrun \
    --nproc_per_node ${NPROC_PER_NODE} \
    --nnodes ${NNODES} \
    --master-addr ${MASTER_ADDR:-127.0.0.1} \
    --master-port ${MASTER_PORT:-29500} \
    --node-rank ${RANK:-0} \
    "${REPO_DIR}/train/pretrain_unified_navit.py" \
        --dataset_config_file "${DATASET_CONFIG_FILE}" \
        --model_name BAGEL \
        --resume_from_hf ${MODEL_PATH} \
        --layer_module Qwen2MoTDecoderLayer \
        --max_latent_size 64 \
        --resume-from ${MODEL_PATH} \
        --auto_resume True \
        --resume-model-only True \
        --finetune-from-ema True \
        --log_every 1 \
        --lr 1e-6 \
        --num_worker 0 \
        --prefetch_factor 1 \
        --expected_num_tokens 32768 \
        --max_num_tokens 70000 \
        --max_num_tokens_per_sample 50000 \
        --freeze_vit True \
        --visual_und True \
        --visual_gen False \
        --results_dir ${RESULTS_DIR} \
        --checkpoint_dir ${RESULTS_DIR}/checkpoints \
        --total_steps 50000 \
        --save_every 1 \
        --wandb_offline True \
        --num_shard ${NPROC_PER_NODE}
