# 使用 Graphiti 实现图记忆

<p align="center">
  <a href="https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/24_graph_memory_graphiti/graph_memory_graphiti.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="在 Colab 中打开"/></a>
</p>

## 📖 速览

| 难度 | 时间 | 前置要求 |
|------------|------|---------------|
| 高级 | 约 60 分钟 | Python 3.8+、`LLM_API_KEY`、本地运行的 Neo4j（推荐 Docker）、建议先了解 08 知识图谱记忆 |

这项技术面向这样的开发者：需要在 Neo4j 支持的时序知识图谱上，对不断演化的事实做多跳推理。

## TL;DR

- **它是什么：** **使用 Graphiti 实现图记忆** 把智能体（agent）知识存进 Neo4j 时序知识图谱，自动抽取实体和关系。
- **何时需要：** 你要对带时间戳的演化事实做多跳推理，比如「用户上个月偏好什么？」
- **权衡：** 需要运行 Neo4j；每个 episode 触发多次 LLM 抽取调用，抽取质量随模型而变。
- **本仓库中最接近的替代：** 27 Zep 记忆 同样构建时序知识图谱，但它以托管服务运行，而不是自托管。

## 描述

想象一块钉满索引卡的软木板，卡片之间用彩色细绳相连。每张卡片代表一个人、一个项目或一个概念。每根绳子代表一种关系：「管理」「依赖」「共事」。再想象每根绳子都挂着日期标签。关系变了，你就加一根新绳子，把旧的标记为过时。这就是时序知识图谱。使用 Graphiti 实现图记忆 是一种智能体记忆技术，用 Zep 出品的 Graphiti SDK 把 LLM 智能体的知识存进 Neo4j 图数据库。它通过自动实体抽取，从对话中捕获实体、关系和时间戳。之后你可以用混合检索（语义搜索加 BM25 关键词匹配）来查询。它适合企业知识管理、关系追踪，以及任何需要对演化事实做多跳推理的智能体。

**关键词：** agent memory, LLM agent, Graphiti, Zep, temporal knowledge graph, Neo4j, entity extraction, relationship extraction, hybrid retrieval, knowledge graph memory

Graphiti 由 Zep 开发，从对话数据构建时序知识图谱。知识图谱是由关系连接起来的实体网络（人、项目、工具），比如「Alice 管理 Bob」「项目 X 依赖服务 Y」。「时序」意味着每条关系都带时间戳。图谱记录每段关系何时开始、何时变化、何时失效。

扁平向量库把每条记忆当成独立的分块（chunk），Graphiti 则会捕捉概念之间的连接。本 notebook 演示：把对话 episode 摄取进 Graphiti，让抽取流程识别实体和关系，查询图谱获得多跳答案，探索时序边，运行社区检测，再把这一切接入智能体循环。

## 你将构建什么

一个基于 Graphiti 的记忆系统，它会：

1. 连接 Neo4j 并初始化 Graphiti 知识图谱引擎。
2. 摄取六个带时间戳的对话 episode，其中事实随时间演化（换团队、换工作、新项目）。
3. 用混合检索（语义 + BM25）以自然语言查询搜索图谱。
4. 探索时序边，观察事实变化时如何被标记失效。
5. 用 Leiden 算法运行社区检测，找出知识聚类。
6. 驱动一个智能体循环：每次回答前先查图谱，用它回答关系型和时序型问题。

## 核心概念

- **Graphiti SDK**：与 Graphiti 知识图谱引擎交互的 Python 客户端，覆盖 episode 摄取、搜索和图谱管理。
- **时序知识图谱（temporal knowledge graph）**：节点和边都带时间戳的图谱。你可以问「上周二我们知道什么？」，并能检测过时或失效的事实。
- **episode 摄取**：把原始对话轮次（episode）输入 Graphiti。Graphiti 的流程自动从非结构化文本中抽取结构化知识。
- **实体/关系抽取（entity/relationship extraction）**：Graphiti 基于 LLM 的流程，从对话文本中识别命名实体（人物、项目、工具）以及它们之间的关系。
- **图搜索（graph search）**：用自然语言查询知识图谱。Graphiti 把语义相似度和 BM25 关键词匹配结合成混合检索。你可以检索实体、事实和多跳关系路径。
- **社区检测（community detection）**：一种算法（Leiden），在知识图谱中找出连接密集的聚类。这些聚类代表主题领域或知识域。
- **时序边（temporal edges）**：带有创建时间、有效期和失效标记的边（节点之间的连接）。事实变化时，旧边被标记失效，新边随之创建。

## 架构

<p align="center">
  <img src="../../images/diagrams/24_graph_memory_graphiti.svg" alt="图记忆 Graphiti 架构图" width="720"/>
</p>

---

## 工作原理

1. 你用 `add_episode()` 把带时间戳的对话 episode 输入 Graphiti。
2. LLM 流程从每个 episode 抽取实体（人物、项目、工具）和关系（「管理」「依赖」）。
3. Graphiti 消解重复项（比如「Alice」和「Dr. Alice Chen」合并成一个节点），并把图谱存入 Neo4j。
4. 每条关系边都带时间戳：何时创建、何时失效。
5. 你用自然语言查询图谱。Graphiti 把语义相似度和 BM25 关键词匹配结合起来。
6. 社区检测（Leiden 算法）把连接密集的节点聚成主题聚类。

## 何时使用

- 你的智能体需要回答多跳问题，比如「谁管理 Alice？她的团队用什么工具？」
- 事实随时间变化，你需要同时追踪当前状态和历史（比如换工作、调团队）。
- 你在做企业知识管理，人物、项目、工具之间的关系很重要。
- 扁平向量库不够用，因为你的查询需要在实体之间沿连接遍历。

## 局限

- 需要一个运行中的 Neo4j 实例。相比向量库，这意味着更多的基础设施、监控和备份工作。
- 每次 `add_episode()` 都触发多次 LLM 调用。每个 episode 会增加数秒延迟和相应的成本。
- 抽取质量取决于 LLM。流程可能漏掉实体、幻觉出不存在的关系，或无法合并重复项。
- 对直接事实查询（「用户说过 X 的什么？」），向量库更快、更便宜。对扁平召回来说，图记忆是不必要的开销。

## Notebook

实现细节、架构图和交互示例见[完整 notebook](./graph_memory_graphiti.ipynb)。

## 前置要求

- 一个运行中的 Neo4j 实例（Docker 最简单：`docker run -d -p 7687:7687 -p 7474:7474 -e NEO4J_AUTH=neo4j/password neo4j:latest`）
- 一个 OpenAI API key（Graphiti 默认用 OpenAI 做抽取和嵌入）
- Python 包：`graphiti-core`、`neo4j`、`openai`、`python-dotenv`

## FAQ

### 问：智能体记忆中的 Graphiti 图记忆是什么？

**答：** Graphiti 是一个开源库，把智能体知识存进 Neo4j 时序知识图谱。它自动从对话中抽取实体和关系，给每条边打时间戳，支持多跳遍历查询。与静态知识图谱不同，Graphiti 追踪事实随时间的变化。你可以分别查询「一月份我们对项目 X 知道什么」和「现在我们知道什么」。它由 Zep 团队开发，以自托管 Python 库的形式提供。

### 问：什么时候该用 Graphiti 图记忆，而不是 Zep 记忆？

**答：** 当你想完全掌控图谱基础设施、并且能自托管 Neo4j 时，用 Graphiti。Zep（技术 27）以托管云服务提供类似的时序图能力。Graphiti 让你直接访问图数据库、写自定义 Cypher 查询，也没有供应商锁定。想要运维负担更小的托管服务，选 Zep。需要本地部署、自定义图谱 schema，或者不想把数据发给第三方服务，选 Graphiti。

### 问：Graphiti 图记忆有哪些限制或失败模式？

**答：** Graphiti 需要运行中的 Neo4j 实例，这增加了基础设施复杂度。实体抽取质量取决于 LLM。名称略有差异的重复实体（「John Smith」和「J. Smith」）需要实体消解，Graphiti 能处理但不完美。没有合适索引时，大图谱（10 万节点以上）上的查询会变慢。这个库相对较新（2024 年发布），API 可能随版本变化。社区支持在增长，但仍小于成熟框架。

### 问：Graphiti 图记忆能和其他记忆技术结合吗？

**答：** 能。Graphiti 与技术 09（情景记忆）配合得很好：用情景记忆存原始会话记录，用 Graphiti 存蒸馏后的知识图谱。搭配技术 20（记忆检索模式）可以加入混合搜索（向量 + 图遍历），得到更丰富的检索。Graphiti 天然支持技术 18（时序记忆）的思路，因为所有边都带时间戳，开箱即支持时序查询。

### 问：有什么库或框架能省掉自己实现的工作？

**答：** Graphiti 本身就是那个库。用 `pip install graphiti-core` 安装，然后连接 Neo4j。想要基于同样时序图技术的托管替代品，用 Zep（技术 27）。LangChain 有 Neo4j 图集成，提供基础的图记忆，但 Graphiti 在此之上还提供自动实体抽取、时序追踪和实体消解。想要不依赖 Neo4j 的更简单图记忆，LangChain 的 `ConversationKGMemory`（技术 08）用 NetworkX 做轻量的内存图。

## 参考资料

- [Graphiti GitHub 仓库](https://github.com/getzep/graphiti)：开源代码、API 参考和示例。
- [Zep 文档](https://docs.getzep.com?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)：Graphiti 的生产环境部署指南。
- [Neo4j 图数据库文档](https://neo4j.com/docs/?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)：图数据库后端，覆盖 Cypher 查询、索引和图算法。
- [Ji et al., "A Survey on Knowledge Graphs," IEEE TNNLS, 2021](https://ieeexplore.ieee.org/document/9416312)：知识图谱构建与应用。
- [Kang et al., "Zep: A Temporal Knowledge Graph Architecture for Agent Memory," 2025 (arXiv:2501.13956)](https://arxiv.org/abs/2501.13956)：Graphiti 设计背后的论文。

## 相关技术

- [**08 知识图谱记忆**](../08_knowledge_graph_memory/) - 基于图的记忆的基础模式。Graphiti 在这些想法之上增加了时序追踪和混合检索。
- [**27 Zep 记忆**](../27_zep_memory/) - 托管 Graphiti 的更完整的 Zep 平台，在其上增加会话管理和按用户隔离的记忆。
- [**07 实体记忆**](../07_entity_memory/) - 跨对话追踪单个实体。Graphiti 把它扩展成完整的实体-关系图谱。
- [**20 记忆检索模式**](../20_memory_retrieval_patterns/) - 讲解混合检索策略，比如 Graphiti 使用的语义 + BM25 组合。

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=all-techniques--24-graph-memory-graphiti--readme)
