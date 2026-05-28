# 大语言模型横向对比

本项目用于完成《人工智能导论》课程作业中的大语言模型横向对比实验。仓库整理了多个大语言模型的本地运行脚本、配置截图、回答截图、模型报告以及最终横向对比分析报告，便于复现实验过程并对比不同模型在中文问答任务中的表现。

## 项目内容

本次对比覆盖以下模型：

| 模型 | 类型 | 仓库内容 |
| --- | --- | --- |
| Baichuan2-7B-Chat | 本地开源模型 | 运行脚本、配置截图、回答截图、模型报告 |
| ChatGLM3-6B | 本地开源模型 | 运行脚本、配置截图、回答截图、模型报告 |
| DeepSeek-R1-Distill-Qwen-1.5B | 本地开源模型 | 运行脚本、部署截图、配置截图、回答截图、模型报告 |
| Qwen-7B-Chat | 本地开源模型 | CPU 运行脚本、配置截图、回答截图、模型报告 |
| Gemini 3.1 Pro | 在线闭源模型 | 回答截图 |
| GPT-5.5 Thinking | 在线闭源模型 | 回答截图 |

## 目录结构

```text
.
├── Baichuan2-7B-Chat/
│   ├── run_baichuan2.py
│   ├── Baichuan2-7B-Chat的配置.png
│   ├── Baichuan2-7B-Chat的回答.png
│   └── Baichuan2-7B-Chat模型报告.docx
├── chatglm3-6b/
│   ├── run_chatglm.py
│   ├── chatglm3-6b的配置.png
│   ├── chatglm3-6b的回答.png
│   └── ChatGLM3-6B模型报告.docx
├── DeepSeek-R1-Distill-Qwen-1.5B/
│   ├── run_deepseek.py
│   ├── DeepSeek-R1-Distill-Qwen-1.5B的部署.png
│   ├── DeepSeek-R1-Distill-Qwen-1.5B的配置.png
│   ├── DeepSeek-R1-Distill-Qwen-1.5B的回答.png
│   └── DeepSeek-R1-Distill-Qwen-1.5B模型报告.docx
├── Qwen-7B-Chat/
│   ├── run_qwen_cpu.py
│   ├── Qwen-7B-Chat的配置.png
│   ├── Qwen-7B-Chat的回答.png
│   └── Qwen-7B-Chat模型报告.docx
├── Gemini 3.1 Pro/
│   └── Gemini 3.1 Pro的回答.png
├── GPT-5.5 Thinking/
│   └── GPT-5.5 Thinking的回答.png
└── 大语言模型横向对比/
    └── 大语言模型横向对比分析报告.docx
```

## 测试问题

各本地模型脚本主要使用同一组中文问题进行测试：

1. 请说出以下两句话区别在哪里？1、冬天：能穿多少穿多少 2、夏天：能穿多少穿多少
2. 讲一个简短的中国古代寓言故事，并说明寓意，100字以内
3. 用一句话解释什么是人工智能，100字以内
4. 推荐三本值得一读的中国经典文学作品，100字以内
5. 如果我是初学者，想学 Python 编程，你有什么建议？100字以内

这些问题覆盖语言理解、常识推理、知识表达、内容推荐和学习建议等能力，适合作为轻量级中文问答对比样例。

## 环境依赖

本地模型脚本基于 Python 和 Hugging Face Transformers 运行，建议准备以下环境：

```bash
pip install torch transformers accelerate sentencepiece
```

如果使用 GPU，可根据 CUDA 版本安装对应的 PyTorch 版本；如果使用 CPU，模型加载和推理速度会明显较慢，尤其是 6B/7B 级别模型。

## 模型路径说明

运行脚本默认从 `/mnt/data/` 下读取模型文件，例如：

```text
/mnt/data/Baichuan2-7B-Chat
/mnt/data/chatglm3-6b
/mnt/data/DeepSeek-R1-Distill-Qwen-1.5B
/mnt/data/Qwen-7B-Chat
```

如果模型存放在其他位置，需要修改对应脚本中的 `model_name` 或 `model_path` 变量。

## 运行方法

进入对应模型目录后运行脚本：

```bash
cd Baichuan2-7B-Chat
python run_baichuan2.py
```

```bash
cd chatglm3-6b
python run_chatglm.py
```

```bash
cd DeepSeek-R1-Distill-Qwen-1.5B
python run_deepseek.py
```

```bash
cd Qwen-7B-Chat
python run_qwen_cpu.py
```

运行后，终端会依次输出每个测试问题及模型回答。相关截图和 Word 报告已保存在各模型目录中。

## 对比维度

可从以下角度分析不同模型的回答表现：

- 回答准确性：是否理解问题并给出正确答案。
- 中文表达能力：语言是否自然、流畅、符合中文语境。
- 指令遵循能力：是否遵守字数、格式和任务要求。
- 推理能力：面对双关、歧义或逻辑问题时是否能合理解释。
- 知识覆盖能力：文学、编程、人工智能等知识性问题回答是否可靠。
- 部署与运行成本：模型大小、加载速度、CPU/GPU 资源需求和推理效率。

## 成果文件

- 各模型目录中的 `*.docx` 文件为单模型实验报告。
- 各模型目录中的 `*.png` 文件为配置、部署或回答过程截图。
- `大语言模型横向对比/大语言模型横向对比分析报告.docx` 为最终横向对比分析报告。

## 注意事项

- 本仓库不包含模型权重文件，运行前需要自行下载对应模型并放置到脚本指定路径。
- 在线模型如 Gemini 和 GPT 相关内容以截图形式保存，无法通过本仓库脚本直接复现。
- 不同硬件、依赖版本、采样参数和模型版本可能导致输出结果存在差异。
