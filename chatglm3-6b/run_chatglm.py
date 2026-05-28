from transformers import AutoTokenizer, AutoModel

model_name = "/mnt/data/chatglm3-6b"

print("正在加载 ChatGLM3-6B 模型...")
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True).eval()
print("模型加载完成！\n" + "="*50)

# 与 Qwen 相同的测试问题
questions = [
    "请说出以下两句话区别在哪里？1、冬天：能穿多少穿多少 2、夏天：能穿多少穿多少，100字以内",
    "讲一个简短的中国古代寓言故事，并说明寓意，100字以内",
    "用一句话解释什么是人工智能，100字以内",
    "推荐一本值得一读的中国经典文学作品，100字以内",
    "如果我是初学者，想学Python编程，你有什么建议？100字以内"
]

for i, question in enumerate(questions, 1):
    print(f"\n【问题 {i}】{question}")
    print("-" * 40)

    response, history = model.chat(tokenizer, question, max_length=100)
    print(response)
    print("\n" + "="*50)

print("\nChatGLM3-6B 所有问题回答完成！")
