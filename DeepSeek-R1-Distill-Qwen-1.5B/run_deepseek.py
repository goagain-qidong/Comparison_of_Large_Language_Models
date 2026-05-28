# run_deepseek.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# 模型路径（请确保已经下载到该目录）
model_path = "/mnt/data/DeepSeek-R1-Distill-Qwen-1.5B"

print("正在加载 DeepSeek-R1-Distill-Qwen-1.5B 模型...")
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype=torch.float32,
    device_map="cpu",
    low_cpu_mem_usage=True
).eval()
print("模型加载完成！\n" + "="*50)

# 测试问题列表（与之前一致）
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

    # 编码输入
    inputs = tokenizer(question, return_tensors="pt")

    # 生成回答
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )

    # 解码并剥离输入部分
    full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = full_response[len(question):].strip()
    print(f"回答：\n{response}\n")
    print("="*50)

print("\nDeepSeek-R1-Distill-Qwen-1.5B 所有问题回答完成！")
