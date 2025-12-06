from transformers import AutoProcessor, Qwen3VLForConditionalGeneration

model_path = "sensenova/SenseNova-SI-1.1-Qwen3-VL-8B"

model = Qwen3VLForConditionalGeneration.from_pretrained(model_path, dtype="auto", device_map="auto")
processor = AutoProcessor.from_pretrained("sensenova/SenseNova-SI-1.1-Qwen3-VL-8B")

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://raw.githubusercontent.com/OpenSenseNova/SenseNova-SI/refs/heads/main/examples/Q1_1.png",
            },
            {
                "type": "image",
                "image": "https://raw.githubusercontent.com/OpenSenseNova/SenseNova-SI/refs/heads/main/examples/Q1_2.png",
            },
            {
                "type": "text",
                "text": "You are standing in front of the dice pattern and observing it. Where is the desk lamp approximately located relative to you?\nOptions:\nA: 90 degrees counterclockwise\nB: 90 degrees clockwise\nC: 135 degrees counterclockwise\nD: 135 degrees clockwise",
            },
        ],
    }
]

inputs = processor.apply_chat_template(
    messages, tokenize=True, add_generation_prompt=True, return_dict=True, return_tensors="pt"
)
inputs = inputs.to(model.device)

generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
