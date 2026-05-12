<div align="center">

# SenseNova-SI: Scaling Spatial Intelligence with Multimodal Foundation Models

</div>

<div align="center">


English | [简体中文](README_CN.md) 

<p align="center">
    <a href="https://arxiv.org/abs/2511.13719" target="_blank">
        <img alt="arXiv" src="https://img.shields.io/badge/arXiv-SenseNova_SI-red?logo=arxiv" height="20" />
    </a>
    <a href="https://huggingface.co/collections/sensenova/sensenova-si" target="_blank">
        <img alt="SenseNova-SI" src="https://img.shields.io/badge/%F0%9F%A4%97%20_SenseNova_SI-Models-ffc107?color=ffc107&logoColor=white" height="20" />
    </a>
    <a href="https://huggingface.co/datasets/sensenova/SenseNova-SI-8M" target="_blank">
        <img alt="SenseNova-SI-8M" src="https://img.shields.io/badge/%F0%9F%A4%97%20_SenseNova_SI_8M-Data-ffc107?color=ffc107&logoColor=white" height="20" />
    </a>
    <a href="https://modelscope.cn/collections/SenseNova-SI-a1d78333be8d42" target="_blank">
        <img alt="SenseNova-SI" src="https://img.shields.io/badge/🤖 ModelScope-Models-blue" height="20" />
    </a>
    <a href="https://easi.lmms-lab.com/leaderboard/" target="_blank">
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
In this work, we explore scaling up multimodal foundation models to cultivate spatial intelligence within the [**SenseNova-SI family**](https://huggingface.co/collections/sensenova/sensenova-si),
built upon established multimodal foundations including visual understanding models (i.e., Qwen3-VL and InternVL3) and unified understanding and generation models (i.e., Bagel).
We take a principled approach to constructing high-performing and robust spatial intelligence by systematically curating SenseNova-SI-8M:
eight million diverse data samples under a rigorous taxonomy of spatial capabilities.
SenseNova-SI demonstrates unprecedented performance across a broad range of spatial intelligence benchmarks, while maintaining strong general multimodal understanding.
More importantly, we analyze the impact of data scaling, discuss early signs of emergent generalization capabilities enabled by diverse data training,
analyze the risk of overfitting and language shortcuts, present a preliminary study on spatial chain-of-thought reasoning, and validate the potential downstream application. SenseNova-SI is an ongoing project, and this report will be updated continuously.
All newly trained multimodal foundation models are publicly released to facilitate further research in this direction.
*In the future, SenseNova-SI will be integrated with larger-scale in-house models.*

## News
- [2026-05-12] We have released official full-scale training dataset of the SenseNova-SI series, [**SenseNova-SI-8M**](https://huggingface.co/datasets/sensenova/SenseNova-SI-8M). SenseNova-SI-8M contains ~8.16 million carefully curated training samples spanning ~2.72 million unique images across 151 datasets.
- [2026-04-13] We have released [**SenseNova-SI-1.3-Qwen3-VL-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.3-Qwen3-VL-8B), built on **Qwen3-VL** with **14M** SI training data, demonstrating strong spatial intelligence across benchmarks and improved **open-ended spatial question-answering** compared to earlier SenseNova-SI Qwen variants.
- [2026-04-01] We have released [**SenseNova-SI-1.5-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.5-InternVL3-8B), which significantly improves **solid geometric** question-answering and analyzing capabilities, achieving an accuracy of **63.5** on SolidGeo MCQ.
- [2026-03-27] We have released [**SenseNova-SI-1.4-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.4-InternVL3-8B), which significantly improves **grounding** and **depth estimation** capabilities, achieving **89.21** on RefCOCO avg and **78.64** on CountBench.
- [2026-02-21] Our work got accepted to CVPR 2026! A paper is just a step. what truly matters is continuing to push the boundaries of spatial intelligence models and sharing our work with the community.
- [2026-01-09] We have released [**SenseNova-SI-1.3-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.3-InternVL3-8B), which improves open-ended spatial question-answering capabilities.
- [2025-12-06] As a first step, we have released a highly effective data subset, [**SenseNova-SI-800K**](https://huggingface.co/datasets/sensenova/SenseNova-SI-800K), as well as [**SenseNova-SI-1.1-InternVL3-8B-800K**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B-800K), a model trained exclusively on the **SenseNova-SI-800K** subset.
- [2025-12-06] We present models starting from more base models, namely[**SenseNova-SI-1.2-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.2-InternVL3-8B), [**SenseNova-SI-1.1-Qwen2.5-VL-3B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen2.5-VL-3B), [**SenseNova-SI-1.1-Qwen2.5-VL-7B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen2.5-VL-7B), and [**SenseNova-SI-1.1-Qwen3-VL-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen3-VL-8B). **SenseNova-SI-1.2-InternVL3-8B** achieve SOTA across eight recent spatial intelligence benchmarks.
- [2025-11-15] We have released [**SenseNova-SI-1.1-InternVL3-2B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-2B) and 
[**SenseNova-SI-1.1-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B), 
which achieve state-of-the-art(SOTA) performance among open-source models of comparable size across five recent spatial intelligence benchmarks: 
**VSI**, **MMSI**, **MindCube**, **ViewSpatial** and **SITE**.
## Models Zoo

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Base Architecture</th>
      <th>SI Dataset Scale</th>
      <th>EASI-8</th>
      <th>Other Remarks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.5-InternVL3-8B/">
          SenseNova-SI-1.5-InternVL3-8B
        </a>
      </td>
      <td>SenseNova-SI-1.4-InternVL3-8B</td>
      <td>1.5M</td>
      <td>64.4</td>
      <td>Enhanced capability in solid geometry</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.4-InternVL3-8B/">
          SenseNova-SI-1.4-InternVL3-8B
        </a>
      </td>
      <td>InternVL3</td>
      <td>29M</td>
      <td>63.7</td>
      <td>Enhanced capability in grounding and depth estimation</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.3-InternVL3-8B/">
          SenseNova-SI-1.3-InternVL3-8B
        </a>
      </td>
      <td>InternVL3</td>
      <td>14M</td>
      <td>65.2</td>
      <td>Best in spatial intelligence, with enhanced capabilities for open-ended short QA</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.3-Qwen3-VL-8B/">
          SenseNova-SI-1.3-Qwen3-VL-8B
        </a>
      </td>
      <td>Qwen3-VL</td>
      <td>14M</td>
      <td>61.4</td>
      <td>Enhanced capability for open-ended short QA</td>
    </tr>
    <tr>
      <td>
        <a href="https://huggingface.co/sensenova/SenseNova-SI-1.2-InternVL3-8B/">
          SenseNova-SI-1.2-InternVL3-8B
        </a>
      </td>
      <td>InternVL3</td>
      <td>10M</td>
      <td>64.5</td>
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
      <td>61.5</td>
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
      <td>49.4</td>
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
      <td>58.1</td>
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
      <td>51.0</td>
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
      <td>45.7</td>
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
      <td>48.6</td>
      <td>Unified understanding and generation model</td>
    </tr>
  </tbody>
</table>

## Release Information

### Models

Currently, we build SenseNova-SI upon popular open-source foundation models to maximize compatibility with existing research pipelines.
In this release, we present 
[**SenseNova-SI-1.5-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.5-InternVL3-8B),
[**SenseNova-SI-1.4-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.4-InternVL3-8B),
[**SenseNova-SI-1.3-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.3-InternVL3-8B),
[**SenseNova-SI-1.3-Qwen3-VL-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.3-Qwen3-VL-8B),
[**SenseNova-SI-1.2-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.2-InternVL3-8B),
[**SenseNova-SI-1.1-InternVL3-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-8B),
[**SenseNova-SI-1.1-Qwen3-VL-8B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen3-VL-8B),
[**SenseNova-SI-1.1-Qwen2.5-VL-7B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen2.5-VL-7B),
[**SenseNova-SI-1.1-Qwen2.5-VL-3B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-Qwen2.5-VL-3B), and
[**SenseNova-SI-1.1-InternVL3-2B**](https://huggingface.co/sensenova/SenseNova-SI-1.1-InternVL3-2B), of which **SenseNova-SI-1.3-InternVL3-8B** achieve state-of-the-art performance among open-source models of comparable size across eight recent spatial intelligence benchmarks: VSI, MMSI, MindCube, ViewSpatial, SITE, BLINK, 3DSRBench, EmbSpatial-Bench. It also improves open-ended spatial question-answering capabilities compared to previous versions.
**SenseNova-SI-1.4-InternVL3-8B** demonstrates strong spatial intelligence across a wide range of benchmarks, with improved **grounding** performance, achieving an average score of **89.21** across all RefCOCO splits and **78.64** on CountBench. On our depth estimation task constructed from the Ibims dataset, it reaches **95.56** in relative depth and **80.31** in absolute depth.
**SenseNova-SI-1.5-InternVL3-8B** exhibits strong spatial intelligence as well as notable improvements in analyzing and solving **solid geometric** problems, achieving an accuracy of **63.5** on SolidGeo MCQ. On our internal benchmarks constructed from K12 question banks, SolidMath and Math3D, it reaches an accuracy of **72.7** and **68.9** respectively.

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
    <tr>
      <td><strong>SenseNova-SI-1.3-Qwen3-VL-8B</strong></td>
      <td><strong>67.8</strong></td>
      <td><strong>39.5</strong></td>
      <td><strong>68.3</strong></td>
      <td><strong>55.8</strong></td>
      <td><strong>57.5</strong></td>
      <td><strong>63.0</strong></td>
      <td><strong>57.3</strong></td>
      <td><strong>82.1</strong></td>
    </tr>
    <tr>
      <td><strong>SenseNova-SI-1.4-InternVL3-8B</strong></td>
      <td><strong>66.6</strong></td>
      <td><strong>40.1</strong></td>
      <td><strong>88.8</strong></td>
      <td><strong>55.7</strong></td>
      <td><strong>47.9</strong></td>
      <td><strong>68.1</strong></td>
      <td><strong>60.4</strong></td>
      <td><strong>81.7</strong></td>
    </tr>
    <tr>
      <td><strong>SenseNova-SI-1.5-InternVL3-8B</strong></td>
      <td><strong>67.3</strong></td>
      <td><strong>38.3</strong></td>
      <td><strong>92.1</strong></td>
      <td><strong>59.0</strong></td>
      <td><strong>47.5</strong></td>
      <td><strong>69.5</strong></td>
      <td><strong>61.3</strong></td>
      <td><strong>80.3</strong></td>
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

For grounding and depth estimation benchmarks, we report the following results.
RefCOCO and CountBench are reproduced using [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval), while the depth estimation results are evaluated on our internally constructed test set.

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>RefCOCO avg</th>
      <th>CountBench</th>
      <th>Ibims Relative Depth</th>
      <th>Ibims Absolute Depth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>InternVL3-8B</td><td>89.01</td><td>81.31</td><td>52.22</td><td>13.45</td>
    </tr>
    <tr>
      <td>SenseNova-SI-1.3-InternVL3-8B</td><td>83.85</td><td>73.92</td><td>68.60</td><td>59.23</td>
    </tr>
    <tr>
      <td><strong>SenseNova-SI-1.4-InternVL3-8B</strong></td>
      <td><strong>89.21</strong></td>
      <td><strong>78.64</strong></td>
      <td><strong>95.56</strong></td>
      <td><strong>80.31</strong></td>
    </tr>
  </tbody>
</table>

For solid geometry benchmarks, we report the following results.
SolidGeo MCQ contains multiple choice questions extracted from [SolidGeo](https://huggingface.co/datasets/SolidGeo/SolidGeo).
SolidMath and Math3D are internally benchmarks constructed from K12 question banks, containing multiple-choice problems in Chinese on solid geometry. SolidMath is built from in-domain data and Math3D is derived from out-of-domain data.

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>SolidGeo MCQ</th>
      <th>SpatialViz-Bench</th>
      <th>SolidMath</th>
      <th>Math3D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>InternVL3-8B</td><td>36.4</td><td>32.0</td><td>42.5</td><td>43.7</td>
    </tr>
    <tr>
      <td>SenseNova-SI-1.3-InternVL3-8B</td><td>36.5</td><td>29.6</td><td>39.6</td><td>40.3</td>
    </tr>
    <tr>
      <td><strong>SenseNova-SI-1.5-InternVL3-8B</strong></td>
      <td><strong>63.5</strong></td>
      <td><strong>33.0</strong></td>
      <td><strong>72.7</strong></td>
      <td><strong>68.9</strong></td>
    </tr>
  </tbody>
</table>


### Datasets

To further facilitate the research in spatial intelligence, we have released a highly effective subset, [SenseNova-SI-800K](https://huggingface.co/datasets/sensenova/SenseNova-SI-800K).
Since SenseNova-SI is designed to study scaling laws, we observe that this initial release captures a substantial portion of the gains.

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

Note that *SenseNova-SI-1.1-InternVL3-8B-800K is trained on the SenseNova-SI-800K subset to provide a reference for researchers working with the 800K-scale dataset. It is released exclusively for scaling-law analysis and research validation, and is not intended to serve as a primary recommended model of the SenseNova-SI series.

#### Data Format

Our data is stored in the **SenseNova-SI-800K.jsonl** file using the JSONL (JSON Lines) format, where each line represents an independent data entry. Each entry is a dictionary organized in the following format,containing three main fields: **`id`**, **`conversations`**, and **`image`**.

- The `id` serves as a unique identifier for each data sample.
- The `image` field is a list of strings specifying image paths, all given as paths relative to the root data directory.
- The `conversations` field is a list of dialogue turns, where each turn is a dictionary with two key-value pairs: `from`, indicating the speaker identity (e.g., human or gpt), and `value`, indicating the textual content. Within `value`, the `<image>` placeholder marks where images are inserted, and the number of `<image>` placeholders match the number of images listed in the `image` field.

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


## 🛠️ QuickStart

### Inference Installation

We recommend using [uv](https://docs.astral.sh/uv/) to manage the environment.

> uv installation guide: <https://docs.astral.sh/uv/getting-started/installation/#installing-uv>

```bash
git clone git@github.com:OpenSenseNova/SenseNova-SI.git
cd SenseNova-SI/
uv sync --extra cu124 # or one of [cu118|cu121|cu124|cu126|cu128|cu129], depending on your CUDA version
source .venv/bin/activate
```

#### Hello World

A simple image-free test to verify environment setup and download the model.

```bash
python example.py \
  --question "Hello" \
  --model_path sensenova/SenseNova-SI-1.4-InternVL3-8B
```

#### Switching Between Supported Models

We fully support multiple model architectures.
To use a different model, simply change the value of the --model_path argument, no other code changes are required.

To use BAGEL-MoT:
```bash
--model_path sensenova/SenseNova-SI-1.1-BAGEL-7B-MoT
```

To use Qwen3-VL:
```bash
--model_path sensenova/SenseNova-SI-1.3-Qwen3-VL-8B
```
### Examples

For more examples, see [example](docs/en/example.md).

#### Example for BAGEL generation

To run the image generation example specifically for the BAGEL-7B-MoT structure, use the following command:

```bash
python example_bagel.py \
  --model_path sensenova/SenseNova-SI-1.1-BAGEL-7B-MoT \
  --prompt "A chubby cat made of 3D point clouds, stretching its body, translucent with a soft glow." \
  --mode generate
```

Use `--mode think_generate` to activate the thinking before generation. Below is a comparison of two modes for the same prompt：

<table>
  <tr>
    <th>mode=generate</th>
    <th>mode=think_generate</th>
  </tr>
  <tr>
    <td align="center" width="50%" style="padding:4px;">
      <img src="./examples/bagel-generate-example.jpg" alt="First image" width="100%">
    </td>
    <td align="center" width="50%" style="padding:4px;">
      <img src="./examples/bagel-think_generate-example.jpg" alt="Second image" width="100%">
    </td>
  </tr>
</table>

#### Example 1

This example is from [SITE-Bench](https://github.com/wenqi-wang20/SITE-Bench):


```bash
python example.py \
  --image_paths examples/Q1_1.png \
  --question "Question: Consider the real-world 3D locations of the objects. Which is closer to the sink, the toilet paper or the towel?\nOptions: \nA. toilet paper\nB. towel\nGive me the answer letter directly. The best answer is:" \
  --model_path sensenova/SenseNova-SI-1.5-InternVL3-8B
# --model_path sensenova/SenseNova-SI-1.3-Qwen3-VL-8B
```



<!-- Example 1 -->
<details open>
  <summary><strong>Details of Example 1</strong></summary>
  <p><strong>Q: </strong>Question: Consider the real-world 3D locations of the objects. Which is closer to the sink, the toilet paper or the towel?\nOptions: \nA. toilet paper\nB. towel\nGive me the answer letter directly. The best answer is:</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q1_1.png" alt="First image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>GT: A</strong></p>
</details>


#### Example 2

This example is from [MMSI-Bench](https://github.com/InternRobotics/MMSI-Bench):


```bash
python example.py \
  --image_paths examples/Q2_1.png examples/Q2_2.png \
  --question "If the landscape painting is on the east side of the bedroom, where is the window located in the bedroom?\nOptions: A. North side, B. South side, C. West side, D. East side\nAnswer with the option's letter from the given choices directly. Enclose the option's letter within ``." \
  --model_path sensenova/SenseNova-SI-1.5-InternVL3-8B
# --model_path sensenova/SenseNova-SI-1.3-Qwen3-VL-8B
```

<!-- Example 2 -->
<details open>
  <summary><strong>Details of Example 2</strong></summary>
  <p><strong>Q: </strong>If the landscape painting is on the east side of the bedroom, where is the window located in the bedroom?\nOptions: A. North side, B. South side, C. West side, D. East side\nAnswer with the option's letter from the given choices directly. Enclose the option's letter within ``.</p>
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
  <p><strong>GT: C</strong></p>
</details>


#### Example 3

This example is from [MMSI-Bench](https://github.com/InternRobotics/MMSI-Bench) and test the model's capability in open-ended short-answer questions:

```bash
python example.py \
  --image_paths examples/Q3_1.png examples/Q3_2.png examples/Q3_3.png \
  --question "The robot is making tea. What is the order in which the pictures were taken?" \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```

<!-- Example 3 -->
<details open>
  <summary><strong>Details of Example 3</strong></summary>
  <p><strong>Q: </strong>The robot is making tea. What is the order in which the pictures were taken?</p>
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
  <p><strong>GT: Second, first, third</strong></p>
</details>


#### Example 4

This example demonstrates the model's **grounding** capability, from [RefCOCO](https://github.com/lichengunc/refer):

```bash
python example.py \
  --image_paths examples/Q4.png \
  --question "Please provide the bounding box coordinate of the region this sentence describes: <ref>blue shirt lady</ref>" \
  --model_path sensenova/SenseNova-SI-1.4-InternVL3-8B
```

<!-- Example 4 -->
<details open>
  <summary><strong>Details of Example 4</strong></summary>
  <p><strong>Q: </strong>Please provide the bounding box coordinate of the region this sentence describes: &lt;ref&gt;blue shirt lady&lt;/ref&gt;</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q4.png" alt="First image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>GT: [0.096234, 0.161229, 0.436516, 1.000000]</strong></p>
</details>


#### Example 5

This example demonstrates the model's **depth estimation** capability:

```bash
python example.py \
  --image_paths examples/Q5.png \
  --question "Identify the minimal distance between the point and the camera, in meters." \
  --model_path sensenova/SenseNova-SI-1.4-InternVL3-8B
```

<!-- Example 5 -->
<details open>
  <summary><strong>Details of Example 5</strong></summary>
  <p><strong>Q: </strong>Identify the minimal distance between the point and the camera, in meters.</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q5.png" alt="First image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>GT: 4.4</strong></p>
</details>



#### Example 6

This example demonstrates the model's capability in **solid geometry(Three views)**:

```bash
python example.py \
  --image_paths examples/Q6.png \
  --question "Enclose your thinking process in <think> </think> tags and your final answer in <answer> </answer>" \
  --model_path sensenova/SenseNova-SI-1.5-InternVL3-8B
```


<!-- Example 6 -->
<details open>
  <summary><strong>Details of Example 6</strong></summary>
  <p><strong>Q: </strong>Enclose your thinking process in &lt;think> &lt;/think> tags and your final answer in &lt;answer> &lt;/answer></p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q6.png" alt="First image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>GT: D</strong></p>
</details>


#### Example 7

This example demonstrates the model's capability in **solid geometry(Nets of 3D Shapes)**:

```bash
python example.py \
  --image_paths examples/Q7.png \
  --question "请将你的思考过程放在<think></think>标签内，并将你的最终答案放在<answer></answer>标签内。" \
  --model_path sensenova/SenseNova-SI-1.5-InternVL3-8B
```


<!-- Example 7 -->
<details open>
  <summary><strong>Details of Example 7</strong></summary>
  <p><strong>Q: </strong>Enclose your thinking process in &lt;think> &lt;/think> tags and your final answer in &lt;answer> &lt;/answer></p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q7.png" alt="First image" width="100%">
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
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```

### Training

#### 1. Download Dataset

User may choose to download [SenseNova-SI-800K](https://huggingface.co/datasets/sensenova/SenseNova-SI-800K) (a downsampled subset of SenseNova-SI-8M, specifically designed for studying scaling laws) or [SenseNova-SI-8M](https://huggingface.co/datasets/sensenova/SenseNova-SI-8M) (official full-scale training dataset).
Download [SenseNova-SI-800K](https://huggingface.co/datasets/sensenova/SenseNova-SI-800K) into `training/data/`:

```bash
pip install huggingface_hub
huggingface-cli download sensenova/SenseNova-SI-800K --repo-type dataset --local-dir training/data/SenseNova-SI-800K
```

Download [SenseNova-SI-8M](https://huggingface.co/datasets/sensenova/SenseNova-SI-8M) into `training/data/`:

```bash
pip install huggingface_hub
huggingface-cli download sensenova/SenseNova-SI-8M --repo-type dataset --local-dir training/data/SenseNova-SI-8M
```

#### 2(a). Training with InternVL

**Download pretrained model**

Download [InternVL3-8B](https://huggingface.co/OpenGVLab/InternVL3-8B) into `training/pretrained_models/`:

```bash
huggingface-cli download OpenGVLab/InternVL3-8B --local-dir training/pretrained_models/OpenGVLab/InternVL3-8B
```

**Install dependencies**

```bash
conda create -n internvl python=3.10 -y
conda activate internvl
pip install uv
uv pip install -r training/intern_vl/requirements.txt
uv pip install flash-attn==2.3.6
```

**Run training**

```bash
bash training/intern_vl/internvl_chat/shell/sensenova_si_800K_internvl3_8b.sh  #Train with SenseNova-SI-800K data

bash training/intern_vl/internvl_chat/shell/sensenova_si_8M_internvl3_8b.sh  # Or train with SenseNova-SI-8M data
```

#### 2(b). Training with Qwen3-VL

The training framework is [lmms-engine](https://github.com/EvolvingLMMs-Lab/lmms-engine), included as a git submodule under `training/lmms-engine/`.

**Download pretrained model**

Download [Qwen3VL-8B](https://github.com/QwenLM/Qwen3-VL) into `training/pretrained_models/`:

```bash
huggingface-cli download Qwen/Qwen3-VL-8B-Instruct --local-dir training/pretrained_models/Qwen/Qwen3-VL-8B-Instruct
```

**Install dependencies**

```bash
# Initialize the lmms-engine submodule (first time only)
git submodule update --init --recursive

conda create -n qwen3vl python=3.10 -y
uv pip install -e training/lmms-engine

# Optional: Performance optimizations
uv pip install flash-attn --no-build-isolation
uv pip install liger-kernel
```

**Preprocess dataset**

Convert `SenseNova-SI-800K.jsonl` and `SenseNova-SI-8M.jsonl` to Qwen3-VL training format:

```bash
python training/qwen3_vl/preprocess_sensenova_si_dataset.py \
  --src data/SenseNova-SI-800K/SenseNova-SI-800K.jsonl \
  --dst data/SenseNova-SI-800K/SenseNova-SI-800K_qwen3vl_format.jsonl  #Preprocess SenseNova-SI-800K data

python training/qwen3_vl/preprocess_sensenova_si_dataset.py \
  --src data/SenseNova-SI-8M/SenseNova-SI-8M.jsonl \
  --dst data/SenseNova-SI-8M/SenseNova-SI-8M_qwen3vl_format.jsonl  #Preprocess SenseNova-SI-8M data
```

**Prepare dataset YAML**
see [training/qwen3_vl/data_800K.yaml](training/qwen3_vl/data_800K.yaml) and [training/qwen3_vl/data_8M.yaml](training/qwen3_vl/data_8M.yaml)

**Configure training**
See [training/qwen3_vl/train_config_800K.yaml](training/qwen3_vl/train_config_800K.yaml) and [training/qwen3_vl/train_config_8M.yaml](training/qwen3_vl/train_config_8M.yaml)

**Run training**

```bash
# Single node, 8 GPUs (default)
bash training/qwen3_vl/run.sh 800K  #Train with SenseNova-SI-800K data

bash training/qwen3_vl/run.sh 8M  # Or train with SenseNova-SI-8M data
```


#### 2(c). Training with Bagel

**Download pretrained model**

Download [BAGEL-7B-MoT](https://huggingface.co/ByteDance-Seed/BAGEL-7B-MoT) into `training/pretrained_models/`:

```bash
huggingface-cli download ByteDance-Seed/BAGEL-7B-MoT --local-dir training/pretrained_models/BAGEL-7B-MoT
```

**Install dependencies**

```bash
conda create -n bagel python=3.10 -y
conda activate bagel
pip install uv
uv pip install -r training/bagel/requirements.txt
uv pip install flash_attn==2.5.8 --no-build-isolation
```

**Run training**

```bash
bash training/bagel/scripts/train_sensenova_si_800K.sh  #Train with SenseNova-SI-800K data

bash training/bagel/scripts/train_sensenova_si_8M.sh  # Or train with SenseNova-SI-8M data
```

For details on training hyperparameters (learning rate, batch size, FSDP config, etc.), refer to [training/bagel/TRAIN.md](training/bagel/TRAIN.md).


### Evaluation

To reproduce the benchmark results above, please refer to [EASI](https://github.com/EvolvingLMMs-Lab/EASI) to evaluate SenseNova-SI on mainstream spatial intelligence benchmarks.

EASI supports over 20 spatial intelligence models and more than 20 spatial benchmarks, offering Docker for one-click spatial intelligence evaluation.

## Acknowledgements

This project includes code that is modified from the original code by the BAGEL, InternVL, lmms-engine team.

* Source repository: [BAGEL](https://github.com/bytedance-seed/BAGEL), [InternVL](https://github.com/opengvlab/internvl), [lmms-engine](https://github.com/EvolvingLMMs-Lab/lmms-engine)

We gratefully acknowledge the authors and contributors for their work.
Please refer to the original repositories for full details, updates, and licensing information.

## 🖊️ Citation

```bib
@InProceedings{sensenova-si,
  title = {Scaling Spatial Intelligence with Multimodal Foundation Models},
  author = {Cai, Zhongang and Wang, Ruisi and Gu, Chenyang and Pu, Fanyi and Xu, Junxiang and Wang, Yubo and Yin, Wanqi and Yang, Zhitao and Wei, Chen and Sun, Qingping and Zhou, Tongxi and Li, Jiaqi and Pang, Hui En and Qian, Oscar and Wei, Yukun and Lin, Zhiqian and Shi, Xuanke and Deng, Kewang and Han, Xiaoyang and Chen, Zukai and Fan, Xiangyu and Deng, Hanming and Lu, Lewei and Pan, Liang and Li, Bo and Liu, Ziwei and Wang, Quan and Lin, Dahua and Yang, Lei},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2026}
}
```
