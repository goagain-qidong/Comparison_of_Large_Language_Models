from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "/mnt/data/Baichuan2-7B-Chat"

print("正在加载 Baichuan2-7B-Chat 模型...")
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True,
    torch_dtype=torch.float16,      # 半精度节省内存
    device_map="cpu",               # 强制使用 CPU
    low_cpu_mem_usage=True
).eval()
print("模型加载完成！\n" + "="*50)

# 与之前相同的问题列表
questions = [
    "请说出以下两句话区别在哪里？1、冬天：能穿多少穿多少 2、夏天：能穿多少穿多少",
    "讲一个简短的中国古代寓言故事，并说明寓意，100字以内",
    "用一句话解释什么是人工智能，100字以内",
    "推荐三本值得一读的中国经典文学作品，100字以内",
    "如果我是初学者，想学Python编程，你有什么建议？100字以内"
]

for i, question in enumerate(questions, 1):
    print(f"\n【问题 {i}】{question}")
    print("-" * 40)

    # Baichuan2 使用 apply_chat_template 构造对话格式
    messages = [{"role": "user", "content": question}]
    input_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    inputs = tokenizer(input_text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )

    # 解码并去掉输入部分
    full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # 提取模型回答（去掉用户输入部分）
    response = full_response[len(input_text):].strip()
    print(response)
    print("\n" + "="*50)

print("\nBaichuan2-7B-Chat 所有问题回答完成！")
