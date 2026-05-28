from transformers import TextStreamer, AutoTokenizer, AutoModelForCausalLM

model_name = "/mnt/data/Qwen-7B-Chat"

print("正在加载模型，请稍候...")
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype="auto").eval()
print("模型加载完成!\n" + "="*50)

# 测试问题列表
questions = [
    "请说出以下两句话区别在哪里？1、冬天：能穿多少穿多少 2、夏天：能穿多少穿多少，100字以内",
    "讲一个简短的中国古代寓言故事，并说明寓意，100字以内",
    "用一句话解释什么是人工智能，100字以内",
    "推荐三本值得一读的中国经典文学作品，100字以内",
    "如果我是初学者，想学Python编程，你有什么建议？100字以内"
]

for i, question in enumerate(questions, 1):
    print(f"\n【问题 {i}】{question}")
    print("-" * 40)

    inputs = tokenizer(question, return_tensors="pt").input_ids
    streamer = TextStreamer(tokenizer, skip_prompt=True)

    outputs = model.generate(
        inputs,
        streamer=streamer,
        max_new_tokens=100,
        temperature=0.7,
        top_p=0.9
    )
    print("\n" + "="*50)

print("\n所有问题回答完成！")
