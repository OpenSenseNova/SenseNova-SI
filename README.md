<div align="center">

# SenseNova-SI: Scaling Spatial Intelligence with Multimodal Foundation Models

</div>

<div align="center">


English | [简体中文](README_CN.md) 

<p align="center">
    <a href="https://huggingface.co/collections/sensenova/sensenova-si" target="_blank">
        <img alt="SenseNova-SI" src="https://img.shields.io/badge/%F0%9F%A4%97%20_SenseNova_SI-Models-ffc107?color=ffc107&logoColor=white" height="20" />
    </a>
    <a href="https://arxiv.org/abs/2511.13719" target="_blank">
        <img alt="arXiv" src="https://img.shields.io/badge/arXiv-SenseNova_SI-red?logo=arxiv" height="20" />
    </a>
    <a href="https://huggingface.co/spaces/lmms-lab-si/EASI-Leaderboard" target="_blank">
        <img alt="Leaderboard" src="https://img.shields.io/badge/%F0%9F%A4%97%20_EASI-Leaderboard-ffc107?color=ffc107&logoColor=white" height="20" />
    </a>
    <a href="https://github.com/EvolvingLMMs-Lab/EASI" target="_blank">
        <img alt="Code" src="https://img.shields.io/badge/EASI-Code-100000?style=flat-square&logo=github&logoColor=white" height="20" />
    </a>
    <a href="https://github.com/OpenSenseNova/SenseNova-SI/blob/main/LICENSE"><img src="https://img.shields.io/github/license/OpenSenseNova/SenseNova-SI"></a>
</p>

</div>


## Overview
Despite remarkable progress, multimodal foundation models still exhibit surprising deficiencies in spatial intelligence.
In this work, we explore scaling up multimodal foundation models to cultivate spatial intelligence within the **SenseNova-SI family**,
built upon established multimodal foundations including visual understanding models (i.e., Qwen3-VL and InternVL3) and unified understanding and generation models (i.e., Bagel).
We take a principled approach to constructing high-performing and robust spatial intelligence by systematically curating SenseNova-SI-8M:
eight million diverse data samples under a rigorous taxonomy of spatial capabilities.
SenseNova-SI demonstrates unprecedented performance across a broad range of spatial intelligence benchmarks: 68.7% on VSI-Bench, 43.3% on MMSI, 85.6% on MindCube,
54.6% on ViewSpatial, and 50.1% on SITE, while maintaining strong general multimodal understanding (e.g., 84.9% on MMBench-En).
More importantly, we analyze the impact of data scaling, discuss early signs of emergent generalization capabilities enabled by diverse data training,
analyze the risk of overfitting and language shortcuts, present a preliminary study on spatial chain-of-thought reasoning, and validate the potential downstream application. SenseNova-SI is an ongoing project, and this report will be updated continuously.
All newly trained multimodal foundation models are publicly released to facilitate further research in this direction.
*In the future, SenseNova-SI will be integrated with larger-scale in-house models.*

## Release Information
Currently, we build SenseNova-SI upon popular open-source foundation models to maximize compatibility with existing research pipelines.
In this release, we present 
[**SenseNova-SI-1.1-InternVL3-2B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-2B) and 
[**SenseNova-SI-1.1-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B), 
which achieve state-of-the-art performance among open-source models of comparable size across five recent spatial intelligence benchmarks: 
**VSI**, **MMSI**, **MindCube**, **ViewSpatial** and **SITE**.


<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>VSI</th>
      <th>MMSI</th>
      <th>MindCube-Tiny</th>
      <th>ViewSpatial</th>
      <th>SITE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="6" align="center"><em>Open-source Models (~2B)</em></td>
    </tr>
    <tr>
      <td>InternVL3-2B</td><td>32.9</td><td>26.5</td><td>37.5</td><td>32.5</td><td>30.0</td>
    </tr>
    <tr>
      <td>Qwen3-VL-2B-Instruct</td><td>50.3</td><td>28.9</td><td>34.5</td><td>36.9</td><td>35.6</td>
    </tr>
    <tr>
      <td>MindCube-3B-RawQA-SFT</td><td>17.2</td><td>1.7</td><td>51.7</td><td>24.1</td><td>6.3</td>
    </tr>
    <tr>
      <td>SpatialLadder-3B</td><td>44.8</td><td>27.4</td><td>43.4</td><td>39.8</td><td>27.9</td>
    </tr>
    <tr>
      <td>SpatialMLLM-4B</td><td>46.3</td><td>26.1</td><td>33.4</td><td>34.6</td><td>18.0</td>
    </tr>
    <tr>
      <td>VST-3B-SFT</td><td>57.9</td><td>30.2</td><td>35.9</td><td>52.8</td><td>35.8</td>
    </tr>
    <tr>
      <td>Cambrian-S-3B</td><td>57.3</td><td>25.2</td><td>32.5</td><td>39.0</td><td>28.3</td>
    </tr>
    <tr>
      <td><strong>SenseNova-SI-1.1-InternVL3-2B</strong></td>
      <td><strong>63.7</strong></td>
      <td><strong>34.2</strong></td>
      <td><strong>41.8</strong></td>
      <td><strong>52.6</strong></td>
      <td><strong>36.7</strong></td>
    </tr>
    <tr>
      <td colspan="6" align="center"><em>Open-source Models (~8B)</em></td>
    </tr>
    <tr>
      <td>InternVL3-8B</td><td>42.1</td><td>28.0</td><td>41.5</td><td>38.6</td><td>41.1</td>
    </tr>
    <tr>
      <td>Qwen3-VL-8B-Instruct</td><td>57.9</td><td>31.1</td><td>29.4</td><td>42.2</td><td>45.8</td>
    </tr>
    <tr>
      <td>BAGEL-7B-MoT</td><td>31.4</td><td>31.0</td><td>34.7</td><td>41.3</td><td>37.0</td>
    </tr>
    <tr>
      <td>SpaceR-7B</td><td>41.5</td><td>27.4</td><td>37.9</td><td>35.8</td><td>34.2</td>
    </tr>
    <tr>
      <td>ViLaSR-7B</td><td>44.6</td><td>30.2</td><td>35.1</td><td>35.7</td><td>38.7</td>
    </tr>
    <tr>
      <td>VST-7B-SFT</td><td>60.6</td><td>32.0</td><td>39.7</td><td>50.5</td><td>39.6</td>
    </tr>
    <tr>
      <td>Cambrian-S-7B</td><td>67.5</td><td>25.8</td><td>39.6</td><td>40.9</td><td>33.0</td>
    </tr>
    <tr>
      <td><strong>SenseNova-SI-1.1-InternVL3-8B</strong></td>
      <td><strong>68.7</strong></td>
      <td><strong>43.3</strong></td>
      <td><strong>85.6</strong></td>
      <td><strong>54.6</strong></td>
      <td><strong>47.7</strong></td>
    </tr>
    <tr>
      <td colspan="6" align="center"><em>Proprietary Models</em></td>
    </tr>
    <tr>
      <td>Gemini-2.5-pro-2025-06</td><td>53.5</td><td>38.0</td><td>57.6</td><td>46.0</td><td>57.0</td>
    </tr>
    <tr>
      <td>Grok-4-2025-07-09</td><td>47.9</td><td>37.8</td><td>63.5</td><td>43.2</td><td>47.0</td>
    </tr>
    <tr>
      <td>GPT-5-2025-08-07</td><td>55.0</td><td>41.8</td><td>56.3</td><td>45.5</td><td>61.8</td>
    </tr>
  </tbody>
</table>


## 🛠️ QuickStart

### Installation

We recommend using [uv](https://docs.astral.sh/uv/) to manage the environment.

> uv installation guide: <https://docs.astral.sh/uv/getting-started/installation/#installing-uv>

```bash
git clone git@github.com:OpenSenseNova/SenseNova-SI.git
cd SenseNova-SI/
uv sync --extra cu124 # or one of [cu118|cu121|cu124|cu126|cu128|cu129], depending on your CUDA version
uv sync
source .venv/bin/activate
```

#### Hello World

A simple image-free test to verify environment setup and download the model.

```bash
python example.py \
  --question "Hello" \
  --model_path sensenova/SenseNova-SI-1.1-InternVL3-8B
```

### Examples

#### Example 1

This example is from the `Pos-Obj-Obj` subset of [MMSI-Bench](https://github.com/InternRobotics/MMSI-Bench):

```bash
python example.py \
  --image_paths examples/Q1_1.png examples/Q1_2.png \
  --question "<image><image>\nYou are standing in front of the dice pattern and observing it. Where is the desk lamp approximately located relative to you?\nOptions: A: 90 degrees counterclockwise, B: 90 degrees clockwise, C: 135 degrees counterclockwise, D: 135 degrees clockwise" \
  --model_path sensenova/SenseNova-SI-1.1-InternVL3-8B 
# --model_path OpenGVLab/InternVL3-8B 
```

<!-- Example 1 -->
<details open>
  <summary><strong>Details of Example 1</strong></summary>
  <p><strong>Q:</strong> <image><image>\nYou are standing in front of the dice pattern and observing it. Where is the desk lamp approximately located relative to you?\nOptions: A: 90 degrees counterclockwise, B: 90 degrees clockwise, C: 135 degrees counterclockwise, D: 135 degrees clockwise</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q1_1.png" alt="First image" width="100%">
      </td>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q1_2.png" alt="Second image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>GT: C</strong></p>
</details>


#### Example 2

This example is from the `Rotation` subset of [MindCube](https://mind-cube.github.io/):

```bash
python example.py \
  --image_paths examples/Q2_1.png examples/Q2_2.png \
  --question "<image><image>\nBased on these two views showing the same scene: in which direction did I move from the first view to the second view?\nA. Directly left B. Directly right C. Diagonally forward and right D. Diagonally forward and left" \
  --model_path sensenova/SenseNova-SI-1.1-InternVL3-8B 
# --model_path OpenGVLab/InternVL3-8B
```

<!-- Example 2 -->
<details open>
  <summary><strong>Details of Example 2</strong></summary>
  <p><strong>Q:</strong> Based on these two views showing the same scene: in which direction did I move from the first view to the second view?\nDirectly left B. Directly right C. Diagonally forward and right D. Diagonally forward and left</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q2_1.png" alt="First image" width="100%">
      </td>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q2_2.png" alt="Second image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>GT: D</strong></p>
</details>


#### Test Multiple Questions in a Single Run

Prepare a file similar to [examples/examples.jsonl](examples/examples.jsonl), where each line represents a single question.

The model is loaded once and processes questions sequentially. The questions remain independent of each other.

> For more details on the `jsonl` format, refer to the documentation for [Single-Image Data](https://internvl.readthedocs.io/en/latest/get_started/chat_data_format.html#single-image-data) and [Multi-Image Data](https://internvl.readthedocs.io/en/latest/get_started/chat_data_format.html#multi-image-data).


```bash
python example.py \
  --jsonl_path examples/examples.jsonl \
  --model_path sensenova/SenseNova-SI-1.1-InternVL3-8B 
# --model_path OpenGVLab/InternVL3-8B 
```

### Evaluation

To reproduce the benchmark results above, please refer to [EASI](https://github.com/EvolvingLMMs-Lab/EASI) to evaluate SenseNova-SI on mainstream spatial intelligence benchmarks.


## 🖊️ Citation

```bib
@article{sensenova-si,
  title = {Scaling Spatial Intelligence with Multimodal Foundation Models},
  author = {Cai, Zhongang and Wang, Ruisi and Gu, Chenyang and Pu, Fanyi and Xu, Junxiang and Wang, Yubo and Yin, Wanqi and Yang, Zhitao and Wei, Chen and Sun, Qingping and Zhou, Tongxi and Li, Jiaqi and Pang, Hui En and Qian, Oscar and Wei, Yukun and Lin, Zhiqian and Shi, Xuanke and Deng, Kewang and Han, Xiaoyang and Chen, Zukai and Fan, Xiangyu and Deng, Hanming and Lu, Lewei and Pan, Liang and Li, Bo and Liu, Ziwei and Wang, Quan and Lin, Dahua and Yang, Lei},
  journal = {arXiv preprint arXiv:2511.13719},
  year = {2025}
}
```