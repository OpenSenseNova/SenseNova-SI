# Copyright 2025 Bytedance Ltd. and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0

import glob
import json
import os
import os.path as osp

from .edit_dataset_jsonl import EditJSONLIterableDataset
from .interleave_datasets import UnifiedEditIterableDataset
from .t2i_dataset import T2IIterableDataset
from .t2i_dataset_jsonl import T2IJSONLIterableDataset
from .vlm_dataset import SftJSONLIterableDataset

DATASET_REGISTRY = {
    "sensenova_si_800K": SftJSONLIterableDataset,
    "sensenova_si_8M": SftJSONLIterableDataset,
}

DATASET_INFO = {}

# load additional dataset info from the dataset_info/ directory
dataset_info_path = osp.join(osp.dirname(__file__), "dataset_info")
dataset_info_files = glob.glob(osp.join(dataset_info_path, "*.json"))
training_root = os.environ.get(
    "TRAINING_ROOT",
    osp.abspath(osp.join(osp.dirname(__file__), "..", "..", "..")),
)


def _resolve_training_root_path(value):
    if isinstance(value, str):
        return value.replace("__TRAINING_ROOT__", training_root)
    if isinstance(value, list):
        return [_resolve_training_root_path(v) for v in value]
    if isinstance(value, dict):
        return {k: _resolve_training_root_path(v) for k, v in value.items()}
    return value


for dataset_info_file in dataset_info_files:
    with open(dataset_info_file, "r") as f:
        base_name = osp.splitext(osp.basename(dataset_info_file))[0]
        dataset_info = _resolve_training_root_path(json.load(f))
        for key in dataset_info.keys():
            if key in DATASET_INFO:
                raise ValueError(f"Key {key} already exists in DATASET_INFO")
        DATASET_INFO.update({base_name: dataset_info})
