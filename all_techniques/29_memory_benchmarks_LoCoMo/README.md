# 记忆基准测试（LoCoMo & LongMemEval）

<p align="center">
  <a href="https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/29_memory_benchmarks_LoCoMo/memory_benchmarks_locomo.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="在 Colab 中打开"/></a>
</p>

## 📖 速览

| 难度 | 时间 | 前置要求 |
|------------|------|---------------|
| 高级 | 约 60 分钟 | Python 3.8+、`LLM_API_KEY`，建议先读 28 记忆评估 |

本技术面向想在 LoCoMo 数据集上给智能体记忆做基准测试的开发者，用标准化指标检验长对话中的记忆回想能力。

## TL;DR

- **是什么：** **记忆基准测试（LoCoMo 和 LongMemEval）** 把智能体记忆放到标准化的多会话数据集上检验，并给出分类别得分。
- **什么时候需要：** 你想用一个可复现的基准测试，把自己的记忆系统和已发表的基线做对比。
- **权衡：** 跑一次带 LLM 评委的完整基准测试要花 5-15 美元，而且固定的对话集未必匹配你的领域。
- **本仓库中最接近的替代：** 28 记忆评估，它让你构建贴合自身用例的自定义评估数据集。

## 描述

想象你雇了一位新助理，入职一周后给他做一套测验。第一部分考他记不记得你点的咖啡。第二部分考他能不能把两次分开的谈话联系起来。第三部分问你什么时候从茶换成了咖啡。记忆基准测试（LoCoMo & LongMemEval）对 LLM 智能体记忆起同样的作用。LoCoMo 和 LongMemEval 是标准化的基准数据集，测试智能体在多会话对话中存储和检索信息的能力。每个基准都给出分类别得分，覆盖单跳检索、多跳推理和时序推理，让你拿到具体数字去比较记忆系统、跟踪改进。

LoCoMo（Long-Context Conversational Memory）和 LongMemEval 提供多会话对话，并配上标准答案（ground truth）问题。每个问题针对一种特定的记忆能力：单跳检索、多跳推理、时序推理、开放式生成，或对抗性抵抗。用你的系统跑这些基准测试，会得到分类别得分，把「记忆质量」变成一个可以跟踪、可以改进的数字。

**关键词：** agent memory, LoCoMo, LongMemEval, memory benchmark, multi-session conversation, BLEU, ROUGE, LLM agent, temporal reasoning, multi-hop reasoning

## 你将学到

- 如何从 HuggingFace 加载并探索 LoCoMo 基准数据集。
- 如何构建预测流程，用检索到的上下文回答基准问题。
- 如何用 BLEU、ROUGE-L、token F1 和 LLM 评委给预测打分。
- 如何分析分类别结果，并与无记忆基线对比。
- LongMemEval 如何用用户与助手的聊天历史和额外的问题类型补充 LoCoMo。

## 关键概念

- **LoCoMo 基准**：10 段多会话对话，约 2,000 组问答对，覆盖五个问题类别。
- **LongMemEval**：500 个用户与助手聊天历史实例，测试五项核心记忆能力。
- **问题类型**：单跳（single-hop，直接回想事实）、多跳（multi-hop，连接跨会话的事实）、时序（temporal，带时间意识的推理）、开放式（open-ended，从散落的事实中综合）、对抗性（adversarial，抵抗误导性上下文）。
- **评分方法**：BLEU（n-gram 重合度）、ROUGE-L（最长公共子序列）、token F1（查准率与查全率的平衡），以及 LLM 评委（语义正确性）。
- **基线对比**：在没有任何记忆上下文的情况下回答同样的问题，衡量检索带来多少价值。

## 架构

<p align="center">
  <img src="../../images/diagrams/29_memory_benchmarks_LoCoMo.svg" alt="记忆基准测试架构图" width="720"/>
</p>

---

## 工作原理

1. 你从 HuggingFace 加载基准数据集（LoCoMo 或 LongMemEval）。每个样本包含多会话对话和标准答案问答对。
2. 你把结构化对话转成纯文本，供记忆系统摄取。
3. 对每个基准问题，你的系统检索相关上下文并生成预测答案。
4. 评分流程对照参考答案，计算 BLEU（n-gram 重合度）、ROUGE-L（最长公共子序列）和 token F1（查准率与查全率的平衡）。
5. LLM 评委检查语义正确性，覆盖措辞不同、但含义一致的情况。
6. 你按问题类别（单跳、多跳、时序、开放式）给分数分组，定位具体弱点。

## 何时使用

- 你想在同一套标准化测试集上客观比较两种记忆架构。
- 你需要分类别的诊断得分，看清系统是在时序推理、多跳连接还是直接回想上吃力。
- 你在迭代记忆系统，需要回归测试确认每次改动是变好而不是变坏。
- 你想要一个共享、可复现的指标，让团队用具体数字而非印象来讨论「记忆质量」。

## 局限

- LoCoMo 的对话是朋友间聊日常生活。如果你的系统处理技术支持或企业流程，基准分数可能反映不了真实表现。
- 把 2,000 个 LoCoMo 问题全部过一遍 LLM 评委要花真金白银的 API 费用（用 GPT-4o-mini 跑一次完整评估约 5-15 美元）。
- 文本重合度指标（BLEU、ROUGE、F1）会惩罚换了措辞的正确答案。LLM 评委能补救，但也不完美。
- 这些基准测试的是一组固定的对话，覆盖不了你的系统在生产环境会遇到的所有边界情况。把它们当下限，不要当上限。

## Notebook

完整代码演示见[实现 notebook](./memory_benchmarks_locomo.ipynb)。

## 常见问题

### 问：在智能体记忆基准中，LoCoMo 是什么？

**答：** LoCoMo（Long Conversation Memory）是测试智能体记忆系统的标准化基准数据集。它包含多会话对话和标准答案问题，覆盖单跳检索、多跳推理、时序推理和开放式生成。每个问题都有经过核实的答案，支持自动打分。LoCoMo 于 2024 年提出，已成为比较记忆架构的标准基准。LongMemEval 是一个互补基准，在更长的对话跨度上测试长期记忆。

### 问：什么时候该用 LoCoMo 基准，而不是自定义的记忆评估？

**答：** 当你想在共同基础上，把自己的记忆系统和已发表的基线或其他系统做对比时，用 LoCoMo 和 LongMemEval。自定义评估（技术 28）测的是你领域的具体需求，但结果没法跨团队比较。LoCoMo 给你标准化的分数，可以写进论文，也可以用来在记忆框架之间做选择。系统选型和对外比较用 LoCoMo；领域调优和生产环境监控用自定义评估。

### 问：LoCoMo 有哪些局限或失效模式？

**答：** LoCoMo 测的是一种特定的对话分布，可能和你的领域不匹配。LoCoMo 分数高，不代表在医疗、法律或技术对话上表现就好。数据集偏小（跨会话约 600 组问答对），存在过拟合的可能。时序推理问题假设了特定的时间格式。这个基准只测检索和答案质量，不测写入性能、延迟和成本。把它当作众多信号中的一个，不要当作唯一的质量指标。

### 问：可以把记忆基准测试和其他记忆技术结合吗？

**答：** 可以。让 LoCoMo 跑在不同的记忆配置上，找出最好的组合。比如，先单独测技术 06（向量库记忆），再加上技术 20（记忆检索模式），量一量提升多少。也可以在 LoCoMo 的多跳问题上，比较技术 03（摘要记忆）和技术 04（摘要缓冲记忆）。基准测试是系统性比较的工具。再配合技术 28（记忆评估），就能搭出一套既覆盖标准测试、也覆盖领域测试的完整评估套件。

### 问：有什么库或框架能帮我省掉实现工作？

**答：** LoCoMo 数据集在 GitHub 和 HuggingFace 上都有，LongMemEval 也公开可用。两者都带评估脚本。RAGAS 能在 LoCoMo 结果上计算检索指标。DeepEval 支持自定义基准评估流程。本仓库的评估代码（技术 28）自带一个测试框架，能把记忆系统跑到 LoCoMo 问题上并打分。用这些工具，一小时内就能搭起完整的基准测试流程。

## 参考文献

- Maharana, A., Lee, D., Tulyakov, S., Bansal, M., Barbieri, F., & Fang, Y. (2024).
  "Evaluating Very Long-Term Conversational Memory of LLM Agents." arXiv:2402.17753.
- LoCoMo GitHub:
  [https://github.com/snap-research/LoCoMo](https://github.com/snap-research/LoCoMo)
- Wu, D., et al. (2024). "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive
  Memory." arXiv:2410.10813.
- LongMemEval GitHub:
  [https://github.com/xiaowu0162/LongMemEval](https://github.com/xiaowu0162/LongMemEval)
- HuggingFace evaluate library (BLEU/ROUGE):
  [https://huggingface.co/docs/evaluate](https://huggingface.co/docs/evaluate?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)

## 相关技术

- [**28 记忆评估**](../28_memory_evaluation/) - 通用的评估框架。基准测试为它提供现成的标准数据集。
- [**30 生产级记忆模式**](../30_production_memory_patterns/) - 上生产之前，基准测试结果帮你选对模式。
- [**21 跨会话记忆**](../21_cross_session_memory/) - LoCoMo 和 LongMemEval 都在测跨会话回想能力。
- [**09 情景记忆**](../09_episodic_memory/) - 情景回想是这些基准测量的核心能力之一。

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=all-techniques--29-memory-benchmarks-locomo--readme)
