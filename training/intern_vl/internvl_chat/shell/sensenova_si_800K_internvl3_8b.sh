set -x

# ============================================================
# SenseNova-SI-800K Training with InternVL3-8B
# ============================================================
#
# Step 1: Download the dataset from Hugging Face:
#   pip install huggingface_hub
#   python -c "
#   from huggingface_hub import snapshot_download
#   snapshot_download(
#       repo_id='sensenova/SenseNova-SI-800K',
#       repo_type='dataset',
#       local_dir='data/SenseNova-SI-800K',
#   )
#   "
#
# Step 2: Run this script from the internvl_chat directory.
# ============================================================


SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(python -c 'import pathlib; print(pathlib.Path("'"${SCRIPT_DIR}"'").parent.resolve())')"
TRAINING_ROOT="$(python -c 'import pathlib; print(pathlib.Path("'"${REPO_DIR}"'").parents[1].resolve())')"
# MODEL_PATH="${MODEL_PATH:-${TRAINING_ROOT}/pretrained_models/InternVL3-8B}"
MODEL_PATH="${MODEL_PATH:-OpenGVLab/InternVL3-8B}"
NPROC_PER_NODE=${NPROC_PER_NODE:-8}
NNODES=${WORLD_SIZE:-1}
RESULTS_DIR="${RESULTS_DIR:-${TRAINING_ROOT}/results/internvl3_8b/sensenova_si_800K}"
META_PATH="${META_PATH:-${REPO_DIR}/shell/data/sensenova_si_800K.json}"

if [ ! -d "$RESULTS_DIR" ]; then
  mkdir -p "$RESULTS_DIR"
fi

BATCH_SIZE=${BATCH_SIZE:-128}
PER_DEVICE_BATCH_SIZE=${PER_DEVICE_BATCH_SIZE:-1}
GRADIENT_ACC=$((BATCH_SIZE / PER_DEVICE_BATCH_SIZE / NPROC_PER_NODE / NNODES))

export TF_CPP_MIN_LOG_LEVEL=3 && \
export LAUNCHER=pytorch && \
export PYTHONPATH=${PYTHONPATH}:${REPO_DIR} && \
export TRAINING_ROOT="${TRAINING_ROOT}" && \
cd ${REPO_DIR} && \
torchrun \
  --nproc_per_node ${NPROC_PER_NODE} \
  --nnodes ${NNODES} \
  --master-addr ${MASTER_ADDR:-127.0.0.1} \
  --master-port ${MASTER_PORT:-29500} \
  --node-rank ${RANK:-0} \
  internvl/train/internvl_chat_finetune.py \
  --model_name_or_path ${MODEL_PATH} \
  --conv_style "internvl2_5" \
  --use_fast_tokenizer False \
  --output_dir ${RESULTS_DIR} \
  --meta_path "${META_PATH}" \
  --overwrite_output_dir True \
  --force_image_size 448 \
  --max_dynamic_patch 12 \
  --down_sample_ratio 0.5 \
  --drop_path_rate 0.0 \
  --freeze_llm False \
  --freeze_mlp False \
  --freeze_backbone True \
  --vision_select_layer -1 \
  --dataloader_num_workers 4 \
  --bf16 True \
  --num_train_epochs 1 \
  --per_device_train_batch_size ${PER_DEVICE_BATCH_SIZE} \
  --gradient_accumulation_steps ${GRADIENT_ACC} \
  --save_strategy "steps" \
  --save_steps 1000 \
  --save_total_limit 3 \
  --learning_rate 5e-6 \
  --weight_decay 0.05 \
  --warmup_ratio 0.03 \
  --lr_scheduler_type "cosine" \
  --logging_steps 1 \
  --max_seq_length 16384 \
  --do_train True \
  --grad_checkpoint True \
  --group_by_length True \
  --dynamic_image_size True \
  --use_thumbnail True \
  --ps_version 'v2' \
  --deepspeed "${REPO_DIR}/zero_stage1_config.json" \
  --report_to "tensorboard" \
  2>&1 | tee -a "${RESULTS_DIR}/training_log.txt"
