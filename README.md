<div align="center">

# SenseNova-SI: Scaling Spatial Intelligence with Multimodal Foundation Models

</div>

<div align="center">


English | [简体中文](README_CN.md) 

<p align="center">
    <a href="https://huggingface.co/collections/sensenova/sensenova-si" target="_blank">
        <img alt="SenseNova-SI" src="https://img.shields.io/badge/%F0%9F%A4%97%20_SenseNova_SI-Models-ffc107?color=ffc107&logoColor=white" height="20" />
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
Despite remarkable progress, leading multimodal models still exhibit notable deficiencies in spatial intelligence:
the ability to make metric estimations, understand spatial relationships, handle viewpoint changes, and integrate information across complex scenes.
We take a scaling perspective: constructing and curating a large-scale, comprehensive collection of spatial intelligence data, 
and through continued training on powerful multimodal foundations, 
cultivating multi-faceted spatial understanding within the SenseNova-SI family of models.
*In the future, SenseNova-SI will be integrated with larger-scale in-house models.*

## Release Information
Currently, we build SenseNova-SI upon popular open-source foundation models to maximize compatibility with existing research pipelines.
In this release, we present 
[**SenseNova-SI-1.1-InternVL3-2B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-2B) and 
[**SenseNova-SI-1.1-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B), 
which achieve state-of-the-art performance among open-source models of comparable size across four recent spatial intelligence benchmarks: 
**VSI**, **MMSI**, **MindCube**, and **ViewSpatial**.

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>VSI</th>
      <th>MMSI</th>
      <th>MindCube-Tiny</th>
      <th>ViewSpatial</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5" align="center"><em>Open-source Models (~2B)</em></td>
    </tr>
    <tr>
      <td>InternVL3-2B</td><td>32.98</td><td>26.50</td><td>37.50</td><td>32.56</td>
    </tr>
    <tr>
      <td>Qwen3-VL-2B-Instruct</td><td>50.36</td><td>28.90</td><td>34.52</td><td>36.97</td>
    </tr>
    <tr>
      <td>MindCube-3B-RawQA-SFT</td><td>17.24</td><td>1.70</td><td>51.73</td><td>24.14</td>
    </tr>
    <tr>
      <td>MindCube-3B-Aug-CGMap-FFR-Out-SFT</td><td>29.60</td><td>29.10</td><td>41.06</td><td>30.90</td>
    </tr>
    <tr>
      <td>MindCube-3B-Plain-CGMap-FFR-Out-SFT</td><td>29.93</td><td>30.40</td><td>39.90</td><td>31.20</td>
    </tr>
    <tr>
      <td>SpatialLadder-3B</td><td>44.86</td><td>27.40</td><td>43.46</td><td>39.85</td>
    </tr>
    <tr>
      <td>SpatialMLLM-4B</td><td>45.98</td><td>26.10</td><td>33.46</td><td>34.66</td>
    </tr>
    <tr>
      <td><strong>SenseNova-SI-1.1-InternVL3-2B</strong></td>
      <td><strong>58.47</strong></td>
      <td><strong>35.50</strong></td>
      <td><strong>71.35</strong></td>
      <td><strong>40.62</strong></td>
    </tr>
    <tr>
      <td colspan="5" align="center"><em>Open-source Models (~8B)</em></td>
    </tr>
    <tr>
      <td>InternVL3-8B</td><td>42.14</td><td>28.00</td><td>41.54</td><td>38.66</td>
    </tr>
    <tr>
      <td>Qwen3-VL-8B-Instruct</td><td>57.90</td><td>31.10</td><td>29.42</td><td>42.20</td>
    </tr>
    <tr>
      <td>BAGEL-7B</td><td>30.90</td><td>33.10</td><td>34.71</td><td>41.32</td>
    </tr>
    <tr>
      <td>SpaceR-7B</td><td>36.29</td><td>27.40</td><td>37.98</td><td>35.85</td>
    </tr>
    <tr>
      <td>ViLaSR-7B</td><td>44.63</td><td>30.20</td><td>35.10</td><td>35.71</td>
    </tr>
    <tr>
      <td><strong>SenseNova-SI-1.1-InternVL3-8B</strong></td>
      <td><strong>62.80</strong></td>
      <td><strong>37.90</strong></td>
      <td><strong>89.33</strong></td>
      <td><strong>53.92</strong></td>
    </tr>
    <tr>
      <td colspan="5" align="center"><em>Proprietary Models</em></td>
    </tr>
    <tr>
      <td>Gemini-2.5-pro-2025-06</td><td>53.57</td><td>38.00</td><td>57.60</td><td>46.06</td>
    </tr>
    <tr>
      <td>Grok-4-2025-07-09</td><td>47.92</td><td>37.80</td><td>63.56</td><td>43.23</td>
    </tr>
    <tr>
      <td>GPT-5-2025-08-07</td><td>55.03</td><td>41.80</td><td>56.30</td><td>45.59</td>
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

#### Test Single-Image MCQ

This example is from the `MultiV` subset of [SITE-Bench](https://wenqi-wang20.github.io/SITE-Bench.github.io/):

```bash
python example.py \
  --image_paths examples/Q1_1.png \
  --question "<image>\nWhich figure is a top-down view of the given shape?\nOptions:\nA: A\nB: B\nC: C\nD: D" \
  --model_path sensenova/SenseNova-SI-1.1-InternVL3-8B 
# --model_path OpenGVLab/InternVL3-8B 
```

<!-- Example 1 -->
<details open>
  <summary><strong>Details of Example 1</strong></summary>
  <p><strong>Q:</strong> Which figure is a top-down view of the given shape?\nOptions:\nA: A\nB: B\nC: C\nD: D</p>
  <div align="center">
    <img src="./examples/Q1_1.png" style="width:40%; height:auto;">
  </div>
</details>


#### Test Multi-Image MCQ

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


## What's next?

We will release the accompanying technical report shortly. Please stay tuned!