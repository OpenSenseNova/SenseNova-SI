# 更多示例

本文档展示了 [README](../../README_CN.md) 之外的更多示例。若需一次性运行全部示例，可使用 [examples/examples.jsonl](../../examples/examples.jsonl) 并配合 `--jsonl_path` 参数（参见 README 中[「一次测试多个问题」](../../README_CN.md#一次测试多个问题)小节）。

---

#### 示例4

该例题源自 [MindCube](https://github.com/mll-lab-nu/MindCube)：

```bash
python example.py \
  --image_paths examples/Q4_1.jpg examples/Q4_2.jpg examples/Q4_3.jpg examples/Q4_4.jpg \
  --question "Based on these four images (image 1, 2, 3, and 4) showing the pink bottle from different viewpoints (front, left, back, and right), with each camera aligned with room walls and partially capturing the surroundings: From the viewpoint presented in image 4, what is to the left of the pink bottle?\nOptions: A. Pink plush toy and headboard B. Window and blue curtain C. Closet and door D. White wall\nAnswer with the option's letter from the given choices directly." \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```

<details open>
  <summary><strong>示例4详情</strong></summary>
  <p><strong>Q: </strong>Based on these four images (image 1, 2, 3, and 4) showing the pink bottle from different viewpoints (front, left, back, and right), with each camera aligned with room walls and partially capturing the surroundings: From the viewpoint presented in image 4, what is to the left of the pink bottle?\nOptions: A. Pink plush toy and headboard B. Window and blue curtain C. Closet and door D. White wall\nAnswer with the option's letter from the given choices directly.</p>
  <table>
    <tr>
      <td align="center" width="25%" style="padding:4px;">
        <img src="../../examples/Q4_1.jpg" alt="Image 1" width="100%">
      </td>
      <td align="center" width="25%" style="padding:4px;">
        <img src="../../examples/Q4_2.jpg" alt="Image 2" width="100%">
      </td>
      <td align="center" width="25%" style="padding:4px;">
        <img src="../../examples/Q4_3.jpg" alt="Image 3" width="100%">
      </td>
      <td align="center" width="25%" style="padding:4px;">
        <img src="../../examples/Q4_4.jpg" alt="Image 4" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>正确答案: C</strong></p>
</details>

---

#### 示例5

该例题源自 [SITE-Bench](https://github.com/wenqi-wang20/SITE-Bench)：

```bash
python example.py \
  --image_paths examples/Q5.jpg \
  --question "Question: Consider the real-world 3D locations and orientations of the objects. Which side of the bus in the center is facing the bus stop?\nOptions: \nA. front\nB. left\nC. back\nD. right\nGive me the answer letter directly. The best answer is:" \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```

<details open>
  <summary><strong>示例5详情</strong></summary>
  <p><strong>Q: </strong>Question: Consider the real-world 3D locations and orientations of the objects. Which side of the bus in the center is facing the bus stop?\nOptions: \nA. front\nB. left\nC. back\nD. right\nGive me the answer letter directly. The best answer is:</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="../../examples/Q5.jpg" alt="Image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>正确答案: D</strong></p>
</details>

---

#### 示例6

该例题源自 [SITE-Bench](https://github.com/wenqi-wang20/SITE-Bench):

```bash
python example.py \
  --image_paths examples/Q6.jpg \
  --question "Question: Consider the real-world 3D orientations of the objects. Are the arrow on street sign and the taxi facing same or similar directions, or very different directions?\nOptions: \nA. same or similar directions\nB. very different directions\nGive me the answer letter directly. The best answer is:" \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```

<details open>
  <summary><strong>示例6详情</strong></summary>
  <p><strong>Q: </strong>Question: Consider the real-world 3D orientations of the objects. Are the arrow on street sign and the taxi facing same or similar directions, or very different directions? Options: A. same or similar directions, B. very different directions. Give me the answer letter directly. The best answer is:</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="../../examples/Q6.jpg" alt="Image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>正确答案: A</strong></p>
</details>

---

#### 示例7

该例题源自 [SITE-Bench](https://github.com/wenqi-wang20/SITE-Bench):

```bash
python example.py \
  --image_paths examples/Q7.jpg \
  --question "Question: What shape are all the men standing in?\nOptions: A. circle B. rectangle C. triangle D. square\nGive me the answer letter directly. The best answer is:" \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```

<details open>
  <summary><strong>示例7详情</strong></summary>
  <p><strong>Q: </strong>Question: What shape are all the men standing in?\nOptions: A. circle B. rectangle C. triangle D. square\nGive me the answer letter directly. The best answer is:</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="../../examples/Q7.jpg" alt="Image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>正确答案: A</strong></p>
</details>

---

#### 示例8

该例题源自 [ViewSpatial-Bench](https://github.com/ZJU-REAL/ViewSpatial-Bench)：

```bash
python example.py \
  --image_paths examples/Q8.jpg \
  --question "From the perspective of this man who doesn't wear glasses, where is the man wearing glasses located beside him?\nOptions: A. left B. back-right C. front D. right\nAnswer with the option's letter from the given choices directly." \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```

<details open>
  <summary><strong>示例8详情</strong></summary>
  <p><strong>Q: </strong>From the perspective of this man who doesn't wear glasses, where is the man wearing glasses located beside him? Options: A. left, B. back-right, C. front, D. right. Answer with the option's letter from the given choices directly.</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="../../examples/Q8.jpg" alt="Image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>正确答案: A</strong></p>
</details>

---

#### 示例9

该例题源自 [MMSI-Bench](https://github.com/InternRobotics/MMSI-Bench)，测试模型在开放式简答题上的能力：

```bash
python example.py \
  --image_paths examples/Q9_1.png examples/Q9_2.png \
  --question "The iMac is in the northern part of the room. In which direction is the area where students do their homework?" \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```

<details open>
  <summary><strong>示例9详情</strong></summary>
  <p><strong>Q: </strong>The iMac is in the northern part of the room. In which direction is the area where students do their homework?</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="../../examples/Q9_1.png" alt="First image" width="100%">
      </td>
      <td align="center" width="50%" style="padding:4px;">
        <img src="../../examples/Q9_2.png" alt="Second image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>正确答案: Northwest corner</strong></p>
</details>

---

#### 示例10

该例题源自 [MMSI-Bench](https://github.com/InternRobotics/MMSI-Bench)，测试模型在开放式简答题上的能力：

```bash
python example.py \
  --image_paths examples/Q10_1.png examples/Q10_2.png \
  --question "How many building models are captured in total in these two pictures?" \
  --model_path sensenova/SenseNova-SI-1.3-InternVL3-8B
```

<details open>
  <summary><strong>示例10详情</strong></summary>
  <p><strong>Q: </strong>How many building models are captured in total in these two pictures?</p>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="../../examples/Q10_1.png" alt="First image" width="100%">
      </td>
      <td align="center" width="50%" style="padding:4px;">
        <img src="../../examples/Q10_2.png" alt="Second image" width="100%">
      </td>
    </tr>
  </table>
  <p><strong>正确答案: 4</strong></p>
</details>
