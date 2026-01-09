<div align="center">

# SenseNova-SI: 探索空间智能在多模态基座模型上的尺度效应

</div>

<div align="center">


[English](README.md) | 简体中文

<p align="center">
    <a href="https://arxiv.org/abs/2511.13719" target="_blank">
        <img alt="arXiv" src="https://img.shields.io/badge/arXiv-SenseNova_SI-red?logo=arxiv" height="20" />
    </a>
    <a href="https://huggingface.co/collections/sensenova/sensenova-si" target="_blank">
        <img alt="SenseNova-SI" src="https://img.shields.io/badge/%F0%9F%A4%97%20_SenseNova_SI-Models-ffc107?color=ffc107&logoColor=white" height="20" />
    </a>
    <a href="https://modelscope.cn/collections/SenseNova-SI-a1d78333be8d42" target="_blank">
        <img alt="SenseNova-SI" src="https://img.shields.io/badge/🤖 ModelScope-Models-blue" height="20" />
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


## 概览
尽管多模态基础模型已取得显著进展，但在空间智能方面仍存在明显不足。
本研究基于成熟的多模态基础，包括视觉理解模型（如Qwen3-VL、InternVL3）和统一理解生成模型（如Bagel），从尺度效应（Scaling）的视角构建了[**SenseNova-SI系列模型**](https://huggingface.co/collections/sensenova/sensenova-si)。
我们采用系统化方法构建了包含800万样本的SenseNova-SI-8M数据集，通过严格的空间能力分类体系培养高性能、高鲁棒性的空间能力。
该系列模型在多项空间智能基准测试中取得突破性表现，同时保持强大的通用多模态理解能力。
本研究进一步分析了数据规模的影响，揭示了多样化数据训练带来的涌现泛化能力，探讨了过拟合与语言捷径的风险，提出了空间思维链推理的初步研究，并验证了下游应用潜力。
SenseNova-SI是一个持续迭代的项目，所有新训练的多模态空间智能基础模型均将陆续开源，以推动空间智能领域的研究发展。
*后续 SenseNova-SI 将与更大规模的内部模型进行集成。*

## 新闻
- [2026-01-09] 我们发布了 [**SenseNova-SI-1.3-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.3-InternVL3-8B)，提升了开放式空间简答题能力。
- [2025-12-06] 为推进空间智能领域的研究，我们先发布一个高效的数据子集, [**SenseNova-SI-800K**](https://huggingface.co/datasets/sensenova/SenseNova-SI-800K), 以及发布模型 [**SenseNova-SI-1.1-InternVL3-8B-800K**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B-800K)。该模型仅使用 SenseNova-SI-800K 子集进行训练，为使用 800K 规模数据进行实验的研究者提供参考。
- [2025-12-06] 在本次发布中，我们推出[**SenseNova-SI-1.2-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.2-InternVL3-8B), [**SenseNova-SI-1.1-Qwen2.5-VL-3B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen2.5-VL-3B), [**SenseNova-SI-1.1-Qwen2.5-VL-7B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen2.5-VL-7B), 与[**SenseNova-SI-1.1-Qwen3-VL-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen3-VL-8B). **SenseNova-SI-1.2-InternVL3-8B** 在八个近期发布的空间智能基准测试（VSI、MMSI、MindCube、ViewSpatial、SITE、BLINK、3DSRBench、EmbSpatial-Bench）上， 在同等模型规模下均取得了开源模型的最新最优性能。
- [2025-11-15] 我们发布了 [**SenseNova-SI-1.1-InternVL3-2B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-2B)与[**SenseNova-SI-1.1-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B)， 在五个近期发布的空间智能基准测试（VSI、MMSI、MindCube、ViewSpatial、SITE）上， 在同等模型规模下均取得了开源模型的最新最优性能（state-of-the-art）。

## 模型库


<table>
  <thead>
    <tr>
      <th>模型</th>
      <th>基础架构</th>
      <th>数据集规模</th>
      <th>其他说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.3-InternVL3-8B/">
          SenseNova-SI-1.3-InternVL3-8B
        </a>
      </td>
      <td>InternVL3</td>
      <td>14M</td>
      <td>最优模型</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.2-InternVL3-8B/">
          SenseNova-SI-1.2-InternVL3-8B
        </a>
      </td>
      <td>InternVL3</td>
      <td>10M</td>
      <td>-</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B/">
          SenseNova-SI-1.1-InternVL3-8B
        </a>
      </td>
      <td>InternVL3</td>
      <td>8M</td>
      <td>-</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-2B/">
          SenseNova-SI-1.1-InternVL3-2B
        </a>
      </td>
      <td>InternVL3</td>
      <td>8M</td>
      <td>-</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen3-VL-8B/">
          SenseNova-SI-1.1-Qwen3-VL-8B
        </a>
      </td>
      <td>Qwen3-VL</td>
      <td>8M</td>
      <td>-</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen2.5-VL-7B">
          SenseNova-SI-1.1-Qwen2.5-VL-7B
        </a>
      </td>
      <td>Qwen2.5-VL</td>
      <td>8M</td>
      <td>-</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen2.5-VL-3B/">
          SenseNova-SI-1.1-Qwen2.5-VL-3B
        </a>
      </td>
      <td>Qwen2.5-VL</td>
      <td>8M</td>
      <td>-</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.1-BAGEL-7B-MoT">
          SenseNova-SI-1.1-BAGEL-7B-MoT
        </a>
      </td>
      <td>BAGEL</td>
      <td>8M</td>
      <td>统一的理解与生成模型</td>
    </tr>
  </tbody>
</table>

## 发布信息

### 模型

目前，我们基于流行的开源基础模型构建 SenseNova-SI，以最大化与现有研究流程的兼容性。
在本次发布中，我们推出
[**SenseNova-SI-1.3-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.3-InternVL3-8B),
[**SenseNova-SI-1.2-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.2-InternVL3-8B),
[**SenseNova-SI-1.1-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B),
[**SenseNova-SI-1.1-Qwen3-VL-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen3-VL-8B),
[**SenseNova-SI-1.1-Qwen2.5-VL-7B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen2.5-VL-7B),
[**SenseNova-SI-1.1-Qwen2.5-VL-3B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen2.5-VL-3B), 与
[**SenseNova-SI-1.1-InternVL3-2B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-2B)。
其中**SenseNova-SI-1.3-InternVL3-8B**在八个近期发布的空间智能基准测试（**VSI**、**MMSI**、**MindCube**、**ViewSpatial**、**SITE**、**BLINK**、**3DSRBench**、**EmbSpatial-Bench**）上，
在同等模型规模下均取得了开源模型的最新最优性能（state-of-the-art），并显著提升了开放式空间问答能力。

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>VSI</th>
      <th>MMSI</th>
      <th>MindCube-Tiny</th>
      <th>ViewSpatial</th>
      <th>SITE</th>
      <th>BLINK</th>
      <th>3DSRBench</th>
      <th>EmbSpatial-Bench</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#F2F0EF;font-weight:700;text-align:center;">
      <td colspan="9"><em>Open-source Models (~2B)</em></td>
    </tr>
    <tr>
      <td>InternVL3-2B</td><td>32.9</td><td>26.5</td><td>37.5</td><td>32.5</td><td>30.0</td><td>50.8</td><td>47.7</td><td>60.1</td>
    </tr>
    <tr>
      <td>Qwen3-VL-2B-Instruct</td><td>50.3</td><td>28.9</td><td>34.5</td><td>36.9</td><td>35.6</td><td>53.2</td><td>47.5</td><td>70.1</td>
    </tr>
    <tr>
      <td>MindCube-3B-RawQA-SFT</td><td>17.2</td><td>1.7</td><td>51.7</td><td>24.1</td><td>6.3</td><td>35.1</td><td>2.8</td><td>37.0</td>
    </tr>
    <tr>
      <td>SpatialLadder-3B</td><td>44.8</td><td>27.4</td><td>43.4</td><td>39.8</td><td>27.9</td><td>43.0</td><td>42.8</td><td>58.2</td>
    </tr>
    <tr>
      <td>SpatialMLLM-4B</td><td>46.3</td><td>26.1</td><td>33.4</td><td>34.6</td><td>18.0</td><td>40.5</td><td>36.2</td><td>50.0</td>
    </tr>
    <tr>
      <td>VST-3B-SFT</td><td>57.9</td><td>30.2</td><td>35.9</td><td>52.8</td><td>35.8</td><td>58.8</td><td>54.1</td><td>69.0</td>
    </tr>
    <tr>
      <td>Cambrian-S-3B</td><td>57.3</td><td>25.2</td><td>32.5</td><td>39.0</td><td>28.3</td><td>37.7</td><td>50.9</td><td>63.5</td>
    </tr>
    <tr style="background:#F2F0EF;font-weight:700;text-align:center;">
      <td colspan="9"><em>Open-source Models (~8B)</em></td>
    </tr>
    <tr>
      <td>InternVL3-8B</td><td>42.1</td><td>28.0</td><td>41.5</td><td>38.6</td><td>41.1</td><td>53.5</td><td>44.3</td><td>76.4</td>
    </tr>
    <tr>
      <td>Qwen3-VL-8B-Instruct</td><td>57.9</td><td>31.1</td><td>29.4</td><td>42.2</td><td>45.8</td><td>66.7</td><td>53.9</td><td>77.7</td>
    </tr>
    <tr>
      <td>BAGEL-7B-MoT</td><td>31.4</td><td>31.0</td><td>34.7</td><td>41.3</td><td>37.0</td><td>63.7</td><td>50.2</td><td>73.1</td>
    </tr>
    <tr>
      <td>SpaceR-7B</td><td>41.5</td><td>27.4</td><td>37.9</td><td>35.8</td><td>34.2</td><td>49.6</td><td>40.5</td><td>66.9</td>
    </tr>
    <tr>
      <td>ViLaSR-7B</td><td>44.6</td><td>30.2</td><td>35.1</td><td>35.7</td><td>38.7</td><td>51.4</td><td>46.6</td><td>67.3</td>
    </tr>
    <tr>
      <td>VST-7B-SFT</td><td>60.6</td><td>32.0</td><td>39.7</td><td>50.5</td><td>39.6</td><td>61.9</td><td>54.6</td><td>73.7</td>
    </tr>
    <tr>
      <td>Cambrian-S-7B</td><td>67.5</td><td>25.8</td><td>39.6</td><td>40.9</td><td>33.0</td><td>37.9</td><td>54.8</td><td>72.8</td>
    </tr>
    <tr>
      <td><strong>SenseNova-SI-1.3-InternVL3-8B</strong></td>
      <td><strong>68.6</strong></td>
      <td><strong>42.5</strong></td>
      <td><strong>89.9</strong></td>
      <td><strong>61.3</strong></td>
      <td><strong>47.5</strong></td>
      <td><strong>68.0</strong></td>
      <td><strong>62.4</strong></td>
      <td><strong>81.0</strong></td>
    </tr>
    <tr style="background:#F2F0EF;color:#6b7280;font-weight:600;text-align:center;">
      <td colspan="9"><em>Proprietary Models</em></td>
    </tr>
    <tr style="color:#6b7280;">
      <td>Gemini-2.5-pro-2025-06</td><td>53.5</td><td>38.0</td><td>57.6</td><td>46.0</td><td>57.0</td><td>73.5</td><td>59.3</td><td>78.9</td>
    </tr>
    <tr style="color:#6b7280;">
      <td>Grok-4-2025-07-09</td><td>47.9</td><td>37.8</td><td>63.5</td><td>43.2</td><td>47.0</td><td>56.4</td><td>54.9</td><td>75.7</td>
    </tr>
    <tr style="color:#6b7280;">
      <td>GPT-5-2025-08-07</td><td>55.0</td><td>41.8</td><td>56.3</td><td>45.5</td><td>61.8</td><td>68.0</td><td>60.3</td><td>81.6</td>
    </tr>
  </tbody>
</table>

### 数据集

为推进空间智能领域的研究，我们先发布一个高效的子集 [SenseNova-SI-800K](https://huggingface.co/datasets/sensenova/SenseNova-SI-800K)。
由于 SenseNova-SI 专为研究扩展规律而设计，我们观察到这个子集已经取得了显著的性能提升。

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>SI Dataset</th>
      <th>VSI</th>
      <th>MMSI</th>
      <th>MindCube-Tiny</th>
      <th>ViewSpatial</th>
      <th>SITE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>InternVL3-8B</td><td>-</td><td>42.1</td><td>28.0</td><td>41.5</td><td>38.6</td><td>41.1</td>
    </tr>
    <tr>
      <td>VST-7B-SFT</td><td>VST-P-4.1M</td><td>60.6</td><td>32.0</td><td>39.7</td><td>50.5</td><td>39.6</td>
    </tr>
    <tr>
      <td>Cambrian-S-7B</td><td>VSI-590K</td><td>67.5</td><td>25.8</td><td>39.6</td><td>40.9</td><td>33.0</td>
    </tr>
    <tr>
      <td><strong><a href="https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B-800K/">*SenseNova-SI-1.1-InternVL3-8B-800K</a></strong></td>
      <td><strong><a href="https://huggingface.co/datasets/sensenova/SenseNova-SI-800K">SenseNova-SI-800K</a></strong></td>
      <td><strong>60.9</strong></td>
      <td><strong>36.4</strong></td>
      <td><strong>56.9</strong></td>
      <td><strong>52.5</strong></td>
      <td><strong>47.7</strong></td>
    </tr>
    <tr>
      <td><strong><a href="https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B/">SenseNova-SI-1.1-InternVL3-8B</a></strong></td>
      <td><strong>SenseNova-SI-8M</strong></td>
      <td><strong>68.7</strong></td>
      <td><strong>43.3</strong></td>
      <td><strong>85.6</strong></td>
      <td><strong>54.6</strong></td>
      <td><strong>47.7</strong></td>
    </tr>
  </tbody>
</table>

请注意，*SenseNova-SI-1.1-InternVL3-8B-800K 是基于 SenseNova-SI-800K 子集训练的，旨在为研究人员提供 800K 规模训练数据的性能参考。该模型仅用于规模定律分析和研究验证，不作为 SenseNova-SI 系列的主要推荐模型。

#### 数据格式

我们的数据存储在 **SenseNova-SI-800K.jsonl** 文件中，采用 JSONL（JSON Lines）格式，其中每一行表示一个独立的数据条目。每个条目是一个包含以下三个主要字段的字典：**`id`**, **`conversations`**, and **`image`**. 

- `id`: 每条数据的唯一标识符。
- `image`: 一个字符串列表，指定图像路径，路径相对于数据根目录。
- `conversations`: 一个对话轮次列表，每轮对话是一个包含两个键值对的字典：
  - `from`: 表示说话者身份（例如 human 或 gpt）。
  - `value`: i表示文本内容。在`value`中，`<image>`占位符表示插入图像的位置，且`<image>`的数量与 image 字段中列出的图像数量相匹配。

```json
{
  "id": 0,
  "conversations": [
    {"from": "human", "value": "<image>\nuser input <image>\nuser input"},
    {"from": "gpt", "value": "assistant output"},
    {"from": "human", "value": "<image>\nuser input"},
    {"from": "gpt", "value": "assistant output"}
  ],
  "image": ["path/to/image1.jpg", "path/to/image2.jpg", "path/to/image3.jpg"],
}
```


## 🛠️ 快速上手

### 安装

我们推荐使用 [uv](https://docs.astral.sh/uv/) 来管理环境。

> uv 安装指南: <https://docs.astral.sh/uv/getting-started/installation/#installing-uv>

```bash
git clone git@github.com:OpenSenseNova/SenseNova-SI.git
cd SenseNova-SI/
uv sync --extra cu124 # 或以下值之一: [cu118|cu121|cu124|cu126|cu128|cu129], 取决于您的 CUDA 版本
source .venv/bin/activate
```

#### Hello World

无需图像的简单测试，以验证环境是否正确配置，并下载模型。

```bash
python example.py \
  --question "Hello" \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```
#### 切换已支持的模型

我们已**完整支持多种模型架构**。如需使用不同模型，仅需修改 `--model_path` 参数，其余代码无需任何改动。

使用 **BAGEL-MoT** 模型：
```bash
--model_path sensenova/SenseNova-SI-1.1-BAGEL-7B-MoT
```

使用 **Qwen3-VL** 模型：
```bash
--model_path sensenova/SenseNova-SI-1.1-Qwen3-VL-8B
```

### 示例

#### BAGEL 图像生成示例
若要运行针对 BAGEL-7B-MoT 架构的图像生成示例，请使用以下命令：
```bash
python example_bagel.py \
  --model_path sensenova/SenseNova-SI-1.1-BAGEL-7B-MoT \
  --mode generate
```

#### 示例1

该例题源自[SITE-Bench](https://github.com/wenqi-wang20/SITE-Bench):

```bash
python example.py \
  --image_paths examples/Q1_1.png \
  --question "Consider the real-world 3D locations of the objects. Which is closer to the sink, the toilet paper or the towel?\nOptions: \nA. toilet paper\nB. towel\nGive me the answer letter directly. The best answer is:" \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
# --model_path sensenova/SenseNova-SI-1.1-Qwen3-VL-8B
```



<!-- Example 1 -->
<details open>
  <summary><strong>示例1详情</strong></summary>
  <p><strong>Q:</strong>Consider the real-world 3D locations of the objects. Which is closer to the sink, the toilet paper or the towel?\nOptions: \nA. toilet paper\nB. towel\nGive me the answer letter directly. The best answer is:</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q1_1.png" alt="First image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>正确答案: A</strong></p>
</details>

#### 示例2

该例题源自[MMSI-Bench](https://github.com/InternRobotics/MMSI-Bench):


```bash
python example.py \
  --image_paths examples/Q2_1.png examples/Q2_2.png \
  --question "If the landscape painting is on the east side of the bedroom, where is the window located in the bedroom?\nOptions: A. North side, B. South side, C. West side, D. East side\nAnswer with the option's letter from the given choices directly. Enclose the option's letter within ``." \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B 
# --model_path sensenova/SenseNova-SI-1.1-Qwen3-VL-8B
```

<!-- Example 2 -->
<details open>
  <summary><strong>示例2详情</strong></summary>
  <p><strong>Q:</strong>If the landscape painting is on the east side of the bedroom, where is the window located in the bedroom?\nOptions: A. North side, B. South side, C. West side, D. East side\nAnswer with the option's letter from the given choices directly. Enclose the option's letter within ``.</p>
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
  <p><strong>正确答案: C</strong></p>
</details>


#### 示例3

该例题源自 [MMSI-Bench](https://github.com/InternRobotics/MMSI-Bench)，测试模型在开放式简答题上的能力：

```bash
python example.py \
  --image_paths examples/Q3_1.png examples/Q3_2.png examples/Q3_3.png \
  --question "The robot is making tea. What is the order in which the pictures were taken?" \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```

<!-- Example 3 -->
<details open>
  <summary><strong>示例3详情</strong></summary>
  <p><strong>Q:</strong>The robot is making tea. What is the order in which the pictures were taken?</p>
  <table>
    <tr>
      <td align="center" width="33%" style="padding:4px;">
        <img src="./examples/Q3_1.png" alt="First image" width="100%">
      </td>
      <td align="center" width="33%" style="padding:4px;">
        <img src="./examples/Q3_2.png" alt="Second image" width="100%">
      </td>
      <td align="center" width="33%" style="padding:4px;">
        <img src="./examples/Q3_3.png" alt="Third image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>正确答案: Second, first, third</strong></p>
</details>


#### 一次测试多个问题

构建类似于[examples/examples.jsonl](examples/examples.jsonl)的文件，每一行代表一个问题。

模型只加载一次，按逐行的顺序逐个回答问题，问题之间互不干扰。

> `jsonl`更详细的格式可以参考[单图数据](https://internvl.readthedocs.io/en/latest/get_started/chat_data_format.html#single-image-data)和[多图数据](https://internvl.readthedocs.io/en/latest/get_started/chat_data_format.html#multi-image-data)

```bash
python example.py \
  --jsonl_path examples/examples.jsonl \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B 
# --model_path sensenova/SenseNova-SI-1.1-Qwen3-VL-8B
```

### 评测

如需复现上述基准测试结果，请参考 [EASI](https://github.com/EvolvingLMMs-Lab/EASI) 在主流空间智能基准上评估 SenseNova-SI 的表现。

EASI 支持超过 20 种空间智能模型和 10 多种空间基准，并提供 Docker 实现一键式空间智能评估。


## 🖊️ 引用

```bib
@article{sensenova-si,
  title = {Scaling Spatial Intelligence with Multimodal Foundation Models},
  author = {Cai, Zhongang and Wang, Ruisi and Gu, Chenyang and Pu, Fanyi and Xu, Junxiang and Wang, Yubo and Yin, Wanqi and Yang, Zhitao and Wei, Chen and Sun, Qingping and Zhou, Tongxi and Li, Jiaqi and Pang, Hui En and Qian, Oscar and Wei, Yukun and Lin, Zhiqian and Shi, Xuanke and Deng, Kewang and Han, Xiaoyang and Chen, Zukai and Fan, Xiangyu and Deng, Hanming and Lu, Lewei and Pan, Liang and Li, Bo and Liu, Ziwei and Wang, Quan and Lin, Dahua and Yang, Lei},
  journal = {arXiv preprint arXiv:2511.13719},
  year = {2025}
}
```
