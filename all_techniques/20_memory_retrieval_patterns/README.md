# 记忆检索模式（Memory Retrieval Patterns）

<p align="center">
  <a href="https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/20_memory_retrieval_patterns/memory_retrieval_patterns.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="在 Colab 中打开"/></a>
</p>

## 📖 速览

| 难度 | 时间 | 前置要求 |
|------------|------|---------------|
| 中级 | 约 40 分钟 | Python 3.8+、`LLM_API_KEY`，建议先了解技术 06 向量库记忆 |

本技术面向想用混合检索、重排序和查询转换策略提升记忆召回准确率的开发者。

## TL;DR

- **它是什么：** **记忆检索模式**把语义检索、BM25 关键词匹配、重排序和 MMR 多样性过滤组合成一条多阶段流程。
- **何时需要：** 基础向量检索会漏掉依赖关键词或需要多样性的结果，而你需要更高的召回准确率。
- **代价：** 交叉编码器重排序增加 50-200ms 延迟；大量可调参数（RRF 的 k、MMR 的 lambda）带来配置出错的风险。
- **本仓库中最接近的技术：** 06 向量库记忆是单阶段语义检索的基础构件，本技术在它之上扩展。

## 概述

想想搜索引擎。你输入查询，得到结果。幕后它同时使用多种策略：关键词匹配、含义分析、热度信号和多样性过滤。每一层都能接住其他层漏掉的东西。记忆检索模式就是把这套多阶段方法引入 LLM 智能体记忆的技术。它组合语义检索（通过嵌入按含义查找记忆）、BM25 关键词匹配、基于交叉编码器模型的重排序，以及 MMR 多样性过滤。这些组件组装成一条混合检索流程。任何知识密集型应用都用得上：研究助手、客服智能体，或者拥有大型记忆库的长期运行的聊天机器人。

记忆系统的好坏，取决于它能否在正确的时机呈现正确的信息。检索策略的选择对智能体的表现影响深远。

在本 notebook 中，你将从零构建一条多阶段检索流程。它组合语义检索（基于嵌入）、BM25 关键词匹配、倒数排名融合（RRF）、交叉编码器重排序和 MMR 多样性过滤。每个组件都实现为独立模块，最后组装成一个 `HybridRetriever` 类。

**关键词：** 智能体记忆、LLM 智能体、混合检索、语义检索、BM25、重排序、倒数排名融合（Reciprocal Rank Fusion）、MMR 多样性、交叉编码器（cross-encoder）、检索流程

## 核心概念

- **语义相似度（semantic similarity）**：用嵌入向量（表示含义的数字）找到含义与查询接近的记忆。用余弦相似度度量。
- **BM25 词法检索**：基于词频的排序函数，擅长精确关键词匹配，能很好地处理领域专业术语。
- **混合检索（hybrid retrieval）**：用倒数排名融合（RRF）合并语义检索和词法检索的结果，同时捕捉含义匹配和关键词匹配。
- **最大边际相关性（Maximal Marginal Relevance，MMR）**：一种平衡相关性与多样性的重排序策略，减少最终输出里的重复结果。
- **交叉编码器重排序（cross-encoder re-ranking）**：用一个把 (查询, 文档) 对放在一起打分的模型，得到比单纯嵌入相似度更高的精度。
- **HyDE（Hypothetical Document Embeddings，假设文档嵌入）**：一种查询转换技术。先生成一个假设性答案，再搜索与它相似的文档，弥合短查询和较长已存记忆之间的词汇差异。

## 架构

<p align="center">
  <img src="../../images/diagrams/20_memory_retrieval_patterns.svg" alt="记忆检索模式架构图" width="720"/>
</p>

---

## 工作原理

1. 查询可选地先用 HyDE 转换（LLM 写出一个假设性答案）。
2. 转换后的查询并行通过两个索引：语义检索（嵌入 + 余弦相似度）和 BM25（关键词匹配）。
3. 倒数排名融合把两份排名列表合并成一份融合排名。
4. 交叉编码器重排序器以更高的精度对头部候选重新打分。
5. MMR 在最大化多样性的同时选出最终的前 K 条结果。
6. 结果被格式化后注入智能体的上下文窗口。

## 何时使用

- 任何需要从记忆中检索的智能体系统。检索质量在哪里都重要。
- 朴素语义检索返回重复或跑题结果的系统。
- 术语专业的领域：纯嵌入检索不如关键词匹配时。
- 大型记忆库（数百到数千条）：多阶段流程能提升精度。

## 局限

- 每个流程阶段都会增加延迟。交叉编码器重排序增加 50-200ms，HyDE 还要多一次完整的 LLM 调用。实时聊天可能需要跳过某些阶段。
- 当 LLM 生成的假设性答案是错的，HyDE 会误导检索：搜到的是与错误答案相似的文档，而不是正确的。
- 小型记忆库（少于 50 条）几乎无法从完整流程中获益。这个规模下基础的余弦相似度检索已经够用。
- 系统的可调参数很多：RRF 的 k 常数、MMR 的 lambda、每个阶段的候选数量。参数越多，配置出错的机会越大。

## Notebook

完整讲解、代码和示例查询见 [配套 notebook](./memory_retrieval_patterns.ipynb)。

## 常见问题

### 问：智能体记忆中的记忆检索模式是什么？

**答：** 记忆检索模式是一条多阶段混合检索流程，组合语义检索、BM25 关键词匹配、交叉编码器重排序和 MMR（最大边际相关性）多样性过滤。你不必依赖单一检索方法，而是并行运行多个检索器，用倒数排名融合（RRF）合并它们的结果，再重排序和去重。这种做法稳定优于单一方法，在典型基准测试中能把查全率提升 15-30%。

### 问：什么时候该用记忆检索模式，而不是向量库记忆？

**答：** 当基础向量检索漏掉相关记忆时，用完整的检索流程。向量库记忆（技术 06）用嵌入的余弦相似度，会漏掉关键词精确匹配（比如 "Python 3.11" 对 "latest Python"）。加上 BM25 就能接住这些。当头部结果里有误报时，加重排序。当结果太相似（返回 5 条近似重复的记忆）时，加 MMR。从基础向量检索起步，检索质量问题出现了再逐级加流程阶段。

### 问：记忆检索模式有哪些限制或失效模式？

**答：** 每个流程阶段都会增加延迟。完整流程（向量检索 + BM25 + 重排序 + MMR）大约需要 200-500ms，单纯向量检索只要 20-50ms。交叉编码器重排序是最贵的一步，要把查询和每个候选一一配对打分。为小型记忆库（少于 100 条）过度设计流程，只会增加复杂度，没有可衡量的收益。你还需要按领域调优融合权重和重排序阈值。

### 问：能把记忆检索模式和其他记忆技术结合吗？

**答：** 可以。把这些模式当作检索层，配合技术 06（向量库记忆）、技术 10（语义记忆）或技术 09（情景记忆）使用。配合技术 18（时序记忆）时，在重排序阶段之后加一个时间衰减乘数。配合技术 12（工作记忆）时，把头部结果按优先级评分送入上下文窗口。检索流程是基础设施，能改进任何基于存储的记忆技术。

### 问：有什么库或框架可以省去自己实现？

**答：** LangChain 提供 `EnsembleRetriever` 做 BM25+向量融合，并通过 `CrossEncoderReranker` 类支持交叉编码器重排序。LlamaIndex 有 `QueryFusionRetriever` 做多来源融合。Zep（技术 27）在内部应用混合检索。独立组件方面：rank-bm25 负责 BM25 打分，sentence-transformers 提供交叉编码器模型，FAISS 或 Chroma 负责向量检索层。用这些库大约 50-100 行代码就能组装出完整流程。

## 参考文献

- Robertson, S., & Zaragoza, H. (2009). ["The Probabilistic Relevance Framework: BM25 and Beyond."](https://doi.org/10.1561/1500000019) *Foundations and Trends in Information Retrieval*, 3(4), 333-389.
- Carbonell, J., & Goldstein, J. (1998). ["The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries."](https://doi.org/10.1145/290941.291025) *ACM SIGIR*, 335-336.
- Gao, L., et al. (2022). ["Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE)."](https://arxiv.org/abs/2212.10496)
- Ma, X., et al. (2023). ["Fine-Tuning LLaMA for Multi-Stage Text Retrieval."](https://arxiv.org/abs/2310.08319)

## 相关技术

- [**06 向量库记忆**](../06_vector_store_memory/) - 基础的语义检索构件。本技术在它之上扩展了关键词检索、融合和重排序。
- [**21 跨会话记忆**](../21_cross_session_memory/) - 把检索模式应用到用户会话之间，让智能体记住过去的对话。
- [**18 时序记忆**](../18_temporal_memory/) - 给检索流程加上时间加权评分，适合新近度很重要的场景。
- [**25 Mem0 模式**](../25_mem0_patterns/) - 开箱即用实现智能体记忆混合检索的框架。

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=all-techniques--20-memory-retrieval-patterns--readme)
