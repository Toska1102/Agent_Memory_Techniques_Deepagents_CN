# 🧠 Agent Memory Techniques

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="images/hero_dark.png">
    <img src="images/banner.png" alt="Agent Memory Techniques：30 个可直接运行的 Jupyter notebook，覆盖每一种主要记忆模式" width="100%"/>
  </picture>
</p>

**系统学习 LLM 智能体的每一种记忆技术。**

> ⭐  **如果这个仓库对你有帮助，请给它点个 Star**，让更多学习者能看到它。

> 🧭  **第一次来？** 从 [01 对话缓冲记忆](all_techniques/01_conversation_buffer_memory/) 开始，或挑一条[学习路径](#-学习路径)。喜欢看图？看下面的[决策树](#-我需要哪种技术)。30 个可直接运行的 Jupyter notebook，覆盖对话缓冲、向量库、知识图谱、情景与语义记忆、工作记忆、MemGPT、Mem0、Letta、Zep、Graphiti、LoCoMo 基准测试和生产级记忆模式。

<p align="center">
  <a href="https://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+"></a>
  <a href="https://jupyter.org/"><img src="https://img.shields.io/badge/Jupyter-Notebook-orange.svg" alt="Jupyter"></a>
  <a href="https://github.com/NirDiamant/Agent_Memory_Techniques/stargazers"><img src="https://img.shields.io/github/stars/NirDiamant/Agent_Memory_Techniques?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/NirDiamant/Agent_Memory_Techniques/issues"><img src="https://img.shields.io/github/issues/NirDiamant/Agent_Memory_Techniques" alt="Issues"></a>
  <a href=".github/CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg" alt="Contributions Welcome"></a>
</p>

---

<p align="center">
  <a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=social-linkedin&target=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fnir-diamant-759323134%2F&text=LinkedIn"><img src="https://img.shields.io/badge/LinkedIn-Connect-blue" alt="LinkedIn"></a>
  <a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=social-twitter&target=https%3A%2F%2Ftwitter.com%2FNirDiamantAI&text=Twitter"><img src="https://img.shields.io/twitter/follow/NirDiamantAI?label=Follow%20%40NirDiamantAI&style=social" alt="Twitter"></a>
  <a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=social-reddit&target=https%3A%2F%2Fwww.reddit.com%2Fr%2FEducationalAI%2F&text=Reddit"><img src="https://img.shields.io/badge/Reddit-Join%20our%20subreddit-FF4500?style=flat-square&logo=reddit&logoColor=white" alt="Reddit"></a>
  <a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=social-discord&target=https%3A%2F%2Fdiscord.gg%2FcA6Aa4uyDX&text=Discord"><img src="https://img.shields.io/badge/Discord-Join%20our%20community-7289da?style=flat-square&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=sponsor-github&target=https%3A%2F%2Fgithub.com%2Fsponsors%2FNirDiamant&text=Sponsor"><img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=ff69b4" alt="Sponsor"></a>
</p>

<h2 align="center">🎓 从记忆 Demo 到生产级智能体</h2>

<div align="center">

**[Prompt to Production](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=course-free-module-cta&target=https%3A%2F%2Fwww.diamant-ai.com%2Fcourses%3Futm_source%3Dgithub%26utm_medium%3Dreadme%26utm_campaign%3Dagent-memory-techniques&retarget=0&text=course-free-module-cta)**：我的完整课程，教你像专业开发者那样用 AI 构建软件，系统讲授可靠、高效、模块化生产系统背后的方法与思维方式。共 17 个模块，每个模块配一节视频讲座和一个动手实验，从你写出的第一条结构化提示词，一直到一套能跑的生产系统。

**课程已全部上线。**每个模块都发布了，讲座和实验都有。

### 🎁 在你自己的仓库上免费试一次

你的编程智能体每次会话启动时对你的项目一无所知，只能靠猜。在你已经打开的智能体里粘贴一行提示词，大约十五分钟后，你的仓库就会多出一层从代码本身提炼的文档，外加一张卡片，给智能体前后的了解程度打分。

我们在六个你每天都在依赖的仓库上跑了一遍。每个仓库先冷启动回答五个关于它自己的问题，写完文档层之后再答一次。最后一列统计的是：该项目**自己的文档**里有多少条陈述被它**自己的代码**推翻：

| 仓库 | 之前 | 之后 | 被自身代码推翻的文档陈述 |
|---|---|---|---|
| fastapi | 2 / 5 | **5 / 5** | 2 |
| flask | 3 / 5 | **5 / 5** | 6 |
| django | 3 / 5 | **4 / 5** | 1 |
| express | 2 / 5 | **4 / 5** | 4 |
| requests | 2 / 5 | **4 / 5** | 0 |
| langchain | 5 / 5 | **4 / 5** | 5 |

Flask 那 6 条里有 4 条是文档示例，一运行就抛 `TypeError`。Langchain 的分数事后反而*更低*，因为它本来就带了一份 380 行的智能体指令文件，冷启动那次的打分对象就是它；这一行还是照实放在表里。

克隆其中任何一个仓库，粘贴同一行提示词，自己去核对那个数字。无需注册。

<a href="https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=course-free-module-direct&target=https%3A%2F%2Fp2p-course.diamant-ai.com%2Flectures%2F00-present%3Futm_source%3Dgithub%26utm_medium%3Dreadme%26utm_campaign%3Dagent-memory-techniques-direct&retarget=0&text=course-free-module-direct"><img src="images/free-module-button.svg" alt="领取你的免费模块" width="420"></a>

### 👉 [**获取完整课程**](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=course-full-cta&target=https%3A%2F%2Fwww.diamant-ai.com%2Fcourses%3Futm_source%3Dgithub%26utm_medium%3Dreadme%26utm_campaign%3Dagent-memory-techniques&retarget=0&text=course-full-cta)

</div>

## 📖 本仓库的配套书

<div align="center">

**[Agent Memory Made Simple](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=book-buy-amazon-am-cta&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB0HCRMGHCM%3Fmaas%3Dmaas_adg_api_580351185840460851_static_9_573%26ref_%3Daa_maas%26tag%3Dmaas%26aa_campaignid%3Dam-en%26aa_adgroupid%3Dgithub-readme%26aa_creativeid%3Dbook-section&retarget=0&text=book-buy-amazon-am-cta)**：464 页图解指南，覆盖本仓库的全部内容：30 种技术一网打尽，184 幅定制插图，全程不需要代码基础。

**[去 Amazon 购买（平装 · Kindle · Kindle Unlimited 免费）→](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=book-buy-amazon-am-cta&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB0HCRMGHCM%3Fmaas%3Dmaas_adg_api_580351185840460851_static_9_573%26ref_%3Daa_maas%26tag%3Dmaas%26aa_campaignid%3Dam-en%26aa_adgroupid%3Dgithub-readme%26aa_creativeid%3Dbook-section&retarget=0&text=book-buy-amazon-am-cta)**

**系列其他作品：** [RAG Made Simple](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=book-buy-amazon-rag-cta&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB0GWDH8JJL%3Fmaas%3Dmaas_adg_api_580351185840460851_static_9_573%26ref_%3Daa_maas%26tag%3Dmaas%26aa_campaignid%3Drag-en%26aa_adgroupid%3Dgithub-readme%26aa_creativeid%3Dbook-section&retarget=0&text=book-buy-amazon-rag-cta) - Amazon 生成式 AI 类畅销书 · 1,500+ 读者 · ⭐ 4.6

</div>


---

## 📫 获取最新动态

<div align="center">
<table>
<tr>
<td align="center">🚀<br><b>每周<br>更新</b></td>
<td align="center">💡<br><b>专家<br>洞见</b></td>
<td align="center">🎯<br><b>前 0.1%<br>的内容</b></td>
</tr>
</table>

<a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=newsletter-subscribe-button&target=https%3A%2F%2Fnewsletter.diamant-ai.com%2F%3Fr%3D336pe4%26utm_campaign%3Dpub-share-checklist&text=Subscribe%20to%20DiamantAI%20Newsletter"><img src="images/subscribe-button.svg" alt="订阅 DiamantAI Newsletter"></a>

*每周有超过 50,000 名读者收到清晰的 AI 教程。***订阅者还能抢先看到新内容，并以 33% 的折扣购买我的书。***
</div>

<a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=newsletter-subscribe-image&target=https%3A%2F%2Fnewsletter.diamant-ai.com%2F%3Fr%3D336pe4%26utm_campaign%3Dpub-share-checklist&text=DiamantAI%20newsletter"><img src="images/substack_image.png" alt="DiamantAI newsletter"></a>

---

## 💡 为什么智能体记忆很重要
> ### 💡 快速答案（给搜索引擎和快速浏览的人）
>
> **Agent Memory（智能体记忆）**是一组技术，让基于 LLM 的智能体（围绕大语言模型构建的系统）能够跨轮次、跨会话、跨任务地记住信息。没有记忆，智能体每次都要重新推导上下文，无法个性化，无法学习，也无法在长交互中保持连贯。本仓库整理了 30 种彼此独立的记忆技术，分为六大家族：短期上下文管理、长期存储、认知架构、检索与多智能体模式、开箱即用的框架，以及生产部署模式。

想象一个朋友，把你聊过的每一句话都忘光。每天早上见面，你们都是陌生人。今天的大多数 AI 智能体就是这样。

每个 AI 智能体最终都会撞上同一堵墙：**它会忘事**。

2026 年，AI 智能体无处不在。但大多数智能体仍然记不住你昨天说过的话。没有可靠的记忆，智能体就无法在对话之间保留上下文，无法从过往聊天中学习，也无法和你建立持久的关系。

这个领域变化很快：

- **Anthropic 的 7 Layers of Memory**（2026 年 3 月）：从对话上下文到跨项目知识，为 Claude Code 定义了记忆层级
- **Mem0**：托管记忆层，在个性化 AI 领域被快速采用
- **Letta (MemGPT)**：可自我编辑的记忆，采用内心独白/外部独白架构
- **Zep**：面向智能体长期记忆的时序知识图谱
- **Graphiti**：从情景记忆到语义记忆的知识图谱抽取
- **MemOS 与 Memori**：把记忆当作基础设施的生产级智能体平台

但市面上没有一份亲手实践的指南，告诉你每种技术如何工作、什么时候该用、以及如何自己动手实现。

这就是本仓库存在的原因。**30 种技术。可直接运行的 notebook。今天就能用的真实代码。**

---

## 🗺️ 智能体记忆技术分类

<p align="center">
  <img src="images/taxonomy.png" alt="智能体记忆分类：6 大家族 30 种技术（短期、长期、认知架构、检索、框架、生产）" width="720"/>
</p>

这 30 种技术分为六大家族。每个家族解决不同的记忆问题。每种技术都在自己的 notebook 里。

| 家族 | 解决什么问题 | 技术编号 |
|---|---|---|
| **短期记忆** | 把最近的对话轮次留在内存里，又不撑爆上下文窗口。 | 01 - 05 |
| **长期记忆** | 让知识跨会话、跨用户、跨时间保存下来。 | 06 - 11 |
| **认知架构** | 工作记忆、分层记忆和反思式记忆系统。 | 12 - 19 |
| **检索与路由** | 决定回忆什么、什么时候回忆。 | 20 - 23 |
| **框架** | 生产可用的记忆库（Mem0、Letta、Zep、Graphiti）。 | 24 - 27 |
| **评估与生产** | 度量、跑分并部署记忆系统。 | 28 - 30 |

---

## 🧭 我需要哪种技术？

30 种技术，按你要构建的东西分组。先挑出和你目标一致的分组，再打开里面的具体技术。

<p align="center">
  <img src="images/decision_tree.svg" alt="决策树：我需要哪种智能体记忆技术？" width="100%"/>
</p>

<!-- decision-tree-text-fallback -->
**纯文字版：**

- 要管理当前这段对话？从 **01-05**（短期记忆）开始。
- 要跨会话保存信息？从 **06 向量库记忆**或 **21 跨会话记忆**开始。
- 在搭建带多个存储的认知架构？看 **12-19**。
- 直接用框架？直奔 **24 Graphiti**、**25 Mem0**、**26 Letta** 或 **27 Zep**。
- 要做评估或上生产？看 **28-30**。

**还是拿不准？** 从 [01 对话缓冲](all_techniques/01_conversation_buffer_memory/) 开始。几乎所有其他技术都建立在它之上。

---

## 📐 一张表对比所有技术

想按约束条件筛选（是否持久化、检索方式、token 开销、适用场景）？看这份[逐项对比矩阵](docs/comparison.md)，30 种技术汇成一张表。

---

## 📚 全部 30 种技术

<p align="center">
  <img src="images/sections/short_term.png" alt="LLM 智能体的短期记忆技术：对话缓冲、滑动窗口、摘要、token 预算" width="100%"/>
</p>

### 🔄 短期记忆（技术 1-5）

管理单次聊天中的对话。

| # | 技术 | 描述 | Notebook |
|---|-----------|-------------|----------|
| 01 | [对话缓冲记忆](all_techniques/01_conversation_buffer_memory/) | 把完整对话一字不落地保存下来。最简单的模式，也是其他一切的基础。 | ✅ [Notebook](all_techniques/01_conversation_buffer_memory/conversation_buffer_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/01_conversation_buffer_memory/conversation_buffer_memory.ipynb) |
| 02 | [滑动窗口记忆](all_techniques/02_sliding_window_memory/) | 只保留最近几条消息。限制了大小，但留下了最近的内容。 | ✅ [Notebook](all_techniques/02_sliding_window_memory/sliding_window_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/02_sliding_window_memory/sliding_window_memory.ipynb) |
| 03 | [摘要记忆](all_techniques/03_summary_memory/) | 用模型写的短摘要替换旧的轮次。损失了篇幅，保住了含义。 | ✅ [Notebook](all_techniques/03_summary_memory/summary_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/03_summary_memory/summary_memory.ipynb) |
| 04 | [摘要缓冲记忆](all_techniques/04_summary_buffer_memory/) | 旧的轮次做摘要，最近的消息保留原文。两头都占到。 | ✅ [Notebook](all_techniques/04_summary_buffer_memory/summary_buffer_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/04_summary_buffer_memory/summary_buffer_memory.ipynb) |
| 05 | [token 缓冲记忆](all_techniques/05_token_buffer_memory/) | 把历史裁剪到严格的 token 预算内。优先丢弃最老的消息。 | ✅ [Notebook](all_techniques/05_token_buffer_memory/token_buffer_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/05_token_buffer_memory/token_buffer_memory.ipynb) |

<p align="center">
  <img src="images/sections/long_term.png" alt="LLM 智能体的长期记忆技术：向量库、实体、知识图谱、情景、语义、程序性" width="100%"/>
</p>

### 💾 长期记忆（技术 6-11）

跨会话、跨用户长期保存的存储。

| # | 技术 | 描述 | Notebook |
|---|-----------|-------------|----------|
| 06 | [向量库记忆](all_techniques/06_vector_store_memory/) | 把过往消息变成向量（捕捉语义的数字列表）。之后按相似度检索。 | ✅ [Notebook](all_techniques/06_vector_store_memory/vector_store_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/06_vector_store_memory/vector_store_memory.ipynb) |
| 07 | [实体记忆](all_techniques/07_entity_memory/) | 抽出并跟踪关于人物、项目和偏好的事实，随对话推进不断更新。 | ✅ [Notebook](all_techniques/07_entity_memory/entity_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/07_entity_memory/entity_memory.ipynb) |
| 08 | [知识图谱记忆](all_techniques/08_knowledge_graph_memory/) | 把实体之间的关系建成图。沿图遍历，对智能体学到的内容做推理。 | ✅ [Notebook](all_techniques/08_knowledge_graph_memory/knowledge_graph_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/08_knowledge_graph_memory/knowledge_graph_memory.ipynb) |
| 09 | [情景记忆](all_techniques/09_episodic_memory/) | 连同时间地点背景完整保存每次交互。适合回答「什么时候发生了什么」。 | ✅ [Notebook](all_techniques/09_episodic_memory/episodic_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/09_episodic_memory/episodic_memory.ipynb) |
| 10 | [语义记忆](all_techniques/10_semantic_memory/) | 从交互中提炼出一般性事实，单独存储，与原始情景分开。 | ✅ [Notebook](all_techniques/10_semantic_memory/semantic_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/10_semantic_memory/semantic_memory.ipynb) |
| 11 | [程序性记忆](all_techniques/11_procedural_memory/) | 沉淀「怎么做」的知识：智能体随时间积累的流程和工作方法。 | ✅ [Notebook](all_techniques/11_procedural_memory/procedural_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/11_procedural_memory/procedural_memory.ipynb) |

<p align="center">
  <img src="images/sections/cognitive.png" alt="认知架构记忆模式：工作记忆、分层记忆、记忆巩固、记忆压缩、自我反思、记忆路由、时序记忆、遗忘与衰减" width="100%"/>
</p>

### 🧩 认知架构（技术 12-19）

借鉴人类记忆方式的模式。

| # | 技术 | 描述 | Notebook |
|---|-----------|-------------|----------|
| 12 | [工作记忆与上下文窗口](all_techniques/12_working_memory_context_window/) | 管理智能体有限的注意力。动态排定优先级、固定和淘汰上下文。 | ✅ [Notebook](all_techniques/12_working_memory_context_window/working_memory_context_window.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/12_working_memory_context_window/working_memory_context_window.ipynb) |
| 13 | [分层记忆](all_techniques/13_hierarchical_memory_layers/) | 热、温、冷三层分级存储。条目随时间老化，升降级管理。 | ✅ [Notebook](all_techniques/13_hierarchical_memory_layers/hierarchical_memory_layers.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/13_hierarchical_memory_layers/hierarchical_memory_layers.ipynb) |
| 14 | [记忆巩固](all_techniques/14_memory_consolidation/) | 合并、去重、强化记忆。灵感来自大脑在睡眠中巩固记忆的方式。 | ✅ [Notebook](all_techniques/14_memory_consolidation/memory_consolidation.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/14_memory_consolidation/memory_consolidation.ipynb) |
| 15 | [记忆压缩](all_techniques/15_memory_compaction/) | 用摘要、实体抽取或蒸馏来压缩已存储的记忆。省存储，也省 token。 | ✅ [Notebook](all_techniques/15_memory_compaction/memory_compaction.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/15_memory_compaction/memory_compaction.ipynb) |
| 16 | [自我反思记忆](all_techniques/16_self_reflection_memory/) | 智能体回顾自己的行动，把哪些做法有效记成笔记，下次再用。 | ✅ [Notebook](all_techniques/16_self_reflection_memory/self_reflection_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/16_self_reflection_memory/self_reflection_memory.ipynb) |
| 17 | [记忆路由](all_techniques/17_memory_routing/) | 挑选合适的记忆存储来读或写。按内容类型和意图路由。 | ✅ [Notebook](all_techniques/17_memory_routing/memory_routing.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/17_memory_routing/memory_routing.ipynb) |
| 18 | [时序记忆](all_techniques/18_temporal_memory/) | 给记忆打上时间戳。带着时间意识检索，越新的条目权重越高。 | ✅ [Notebook](all_techniques/18_temporal_memory/temporal_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/18_temporal_memory/temporal_memory.ipynb) |
| 19 | [遗忘与衰减](all_techniques/19_forgetting_and_decay/) | 有目的地遗忘。用衰减、访问次数或相关性来修剪。 | ✅ [Notebook](all_techniques/19_forgetting_and_decay/forgetting_and_decay.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/19_forgetting_and_decay/forgetting_and_decay.ipynb) |

<p align="center">
  <img src="images/sections/retrieval.png" alt="记忆检索与多智能体模式：检索模式、跨会话记忆、多智能体共享记忆、工具化记忆" width="100%"/>
</p>

### 🔍 检索与多智能体（技术 20-23）

智能体如何找到并共享记忆。

| # | 技术 | 描述 | Notebook |
|---|-----------|-------------|----------|
| 20 | [记忆检索模式](all_techniques/20_memory_retrieval_patterns/) | 对比多种检索策略：语义搜索、按新近度、混合打分、多样性和重排序。 | ✅ [Notebook](all_techniques/20_memory_retrieval_patterns/memory_retrieval_patterns.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/20_memory_retrieval_patterns/memory_retrieval_patterns.ipynb) |
| 21 | [跨会话记忆](all_techniques/21_cross_session_memory/) | 跨会话保存和恢复智能体状态。用户从上次中断的地方继续。 | ✅ [Notebook](all_techniques/21_cross_session_memory/cross_session_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/21_cross_session_memory/cross_session_memory.ipynb) |
| 22 | [多智能体共享记忆](all_techniques/22_multi_agent_shared_memory/) | 面向多智能体团队的共享存储、消息传递和一致性协议。 | ✅ [Notebook](all_techniques/22_multi_agent_shared_memory/multi_agent_shared_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/22_multi_agent_shared_memory/multi_agent_shared_memory.ipynb) |
| 23 | [工具化记忆](all_techniques/23_memory_with_tools/) | 给智能体一组可调用的记忆工具：保存、搜索、遗忘。像普通工具一样对待。 | ✅ [Notebook](all_techniques/23_memory_with_tools/memory_with_tools.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/23_memory_with_tools/memory_with_tools.ipynb) |

<p align="center">
  <img src="images/sections/frameworks.png" alt="智能体记忆框架与库：Graphiti、Mem0、Letta (MemGPT)、Zep" width="100%"/>
</p>

### 🔧 框架与平台（技术 24-27）

上手主流的记忆框架。

| # | 技术 | 描述 | Notebook |
|---|-----------|-------------|----------|
| 24 | [Graphiti 图记忆](all_techniques/24_graph_memory_graphiti/) | 用 Zep 的 Graphiti 从聊天记录构建带时间意识的知识图谱，抽取情景和一般性事实。 | ✅ [Notebook](all_techniques/24_graph_memory_graphiti/graph_memory_graphiti.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/24_graph_memory_graphiti/graph_memory_graphiti.ipynb) |
| 25 | [Mem0 模式](all_techniques/25_mem0_patterns/) | 使用 Mem0 的托管记忆层。它会替你抽取、存储和取回用户级记忆。 | ✅ [Notebook](all_techniques/25_mem0_patterns/mem0_patterns.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/25_mem0_patterns/mem0_patterns.ipynb) |
| 26 | [Letta (MemGPT) 模式](all_techniques/26_letta_memgpt_patterns/) | 搭建 MemGPT 式的自我编辑记忆。涵盖内心独白、心跳事件和记忆压力。 | ✅ [Notebook](all_techniques/26_letta_memgpt_patterns/letta_memgpt_patterns.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/26_letta_memgpt_patterns/letta_memgpt_patterns.ipynb) |
| 27 | [Zep 记忆](all_techniques/27_zep_memory/) | 用 Zep 做对话分类、实体抽取和时序感知图谱。为生产环境而生。 | ✅ [Notebook](all_techniques/27_zep_memory/zep_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/27_zep_memory/zep_memory.ipynb) |

<p align="center">
  <img src="images/sections/evaluation.png" alt="智能体记忆评估与生产：记忆评估、LoCoMo 和 LongMemEval 基准测试、生产部署模式" width="100%"/>
</p>

### 📊 评估与生产（技术 28-30）

先度量你的记忆系统，再把它上线。

| # | 技术 | 描述 | Notebook |
|---|-----------|-------------|----------|
| 28 | [记忆评估](all_techniques/28_memory_evaluation/) | 度量记忆质量。检查检索的查准率和查全率、陈旧度、矛盾和用户满意度。 | ✅ [Notebook](all_techniques/28_memory_evaluation/memory_evaluation.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/28_memory_evaluation/memory_evaluation.ipynb) |
| 29 | [记忆基准测试（LoCoMo）](all_techniques/29_memory_benchmarks_LoCoMo/) | 让你的记忆系统跑 LoCoMo 和 LongMemEval 基准。看看它在长对话下的表现。 | ✅ [Notebook](all_techniques/29_memory_benchmarks_LoCoMo/memory_benchmarks_locomo.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/29_memory_benchmarks_LoCoMo/memory_benchmarks_locomo.ipynb) |
| 30 | [生产级记忆模式](all_techniques/30_production_memory_patterns/) | 规模化运行记忆系统。缓存、TTL（存活时间）、分片、备份、GDPR 和可观测性。 | ✅ [Notebook](all_techniques/30_production_memory_patterns/production_memory_patterns.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/30_production_memory_patterns/production_memory_patterns.ipynb) |

---

## 🎯 学习路径

### 初级：打基础

刚接触智能体记忆？从这里开始。这些是基本积木。

```
01 对话缓冲 → 02 滑动窗口 → 03 摘要记忆 →
05 token 缓冲 → 06 向量库记忆 → 21 跨会话记忆
```

### 中级：结构化记忆

想更进一步？加入实体、图谱和更聪明的检索。

```
07 实体记忆 → 08 知识图谱 → 09 情景记忆 →
10 语义记忆 → 20 检索模式 → 22 多智能体共享记忆
```

### 高级：认知架构

为高级智能体构建受人类启发的记忆模式。

```
12 工作记忆 → 13 分层记忆 → 14 记忆巩固 →
16 自我反思 → 17 记忆路由 → 19 遗忘与衰减
```

### 实战：框架与生产

接入生产级工具，并度量你构建的成果。

```
25 Mem0 → 26 Letta/MemGPT → 24 Graphiti → 27 Zep →
28 记忆评估 → 29 基准测试 → 30 生产模式
```

---

## 🚀 快速开始

> 💡  **不想安装任何东西？** 每个 notebook 都能在 GitHub 上直接渲染。点上面表格里的技术名就能在浏览器里读。或者用 Colab 徽章在云端运行。

```bash
# 克隆仓库
git clone https://github.com/NirDiamant/Agent_Memory_Techniques.git
cd Agent_Memory_Techniques

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 配置 API 密钥
cp .env.example .env
# 编辑 .env，填入你的 OPENAI_API_KEY 和/或 ANTHROPIC_API_KEY

# 启动 Jupyter，从第一个技术开始
jupyter notebook all_techniques/01_conversation_buffer_memory/
```

---

## 📁 项目结构

```
Agent_Memory_Techniques/
├── README.md                           # 你在这里
├── ROADMAP.md                          # 当前状态与后续计划
├── LICENSE                             # Apache 2.0
├── CITATION.cff                        # 如何引用本仓库
├── requirements.txt                    # Python 依赖
├── .env.example                        # API 密钥模板
├── llms.txt                            # 面向 LLM 的可发现性索引
│
├── all_techniques/                     # 30 个技术文件夹，每个包含 notebook + README
│   ├── 01_conversation_buffer_memory/
│   ├── 02_sliding_window_memory/
│   ├── ...
│   └── 30_production_memory_patterns/
│
├── docs/                               # 项目文档
│   ├── architecture.md                 # 记忆系统设计模式
│   ├── comparison.md                   # 30 种技术的逐项对比
│   ├── glossary.md                     # 关键术语与定义
│   ├── learning_path.md                # 详细的学习路径指南
│   ├── topics.md                       # 关键词索引
│   ├── roadmap.md                      # 最初的规划存档
│   ├── FAQ.md                          # 常见问题
│   └── CONTENT_STANDARDS.md            # 写作风格规范
│
├── .github/                            # GitHub 社区文件
│   ├── CONTRIBUTING.md                 # 如何参与贡献
│   ├── CODE_OF_CONDUCT.md              # 社区准则
│   ├── SECURITY.md                     # 安全策略
│   ├── FUNDING.yml                     # 赞助配置
│   ├── ISSUE_TEMPLATE/                 # Issue 模板
│   ├── pull_request_template.md        # PR 模板
│   └── workflows/                      # CI 工作流
│
├── utils/                              # 共享工具函数与校验器
│   ├── helpers.py                      # 环境变量加载、LLM 客户端、余弦相似度、token 计数
│   ├── validate_cells.py               # notebook 单元格结构校验器
│   └── validate_style.py               # 文风校验器
│
├── tests/                              # pytest 冒烟测试
├── data/                               # 小型示例数据集
└── images/                             # 图表与配图
```

---

## 📚 同一作者的更多内容

*运营课程、newsletter 或开发者社区？你可以向你的读者[推荐 RAG Made Simple，赚取 25% 分成](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=affiliate-signup&target=https%3A%2F%2Fnirdiamant.gumroad.com%2Faffiliates&retarget=0&text=affiliate-signup)。*

## 🤝 参与贡献

<a href="https://github.com/NirDiamant/Agent_Memory_Techniques/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=NirDiamant/Agent_Memory_Techniques" alt="Contributors" />
</a>

欢迎贡献。你可以补充一个 notebook、修一个 bug、改进文档，或提出一种新技术。每一份贡献都在帮助下一位读者。

详见 [CONTRIBUTING.md](.github/CONTRIBUTING.md)。

**最需要人手的地方：**
- 我们还没覆盖到的技术（通过 issue 提议）
- 架构图（Mermaid 或 ASCII）
- 更多记忆基准测试和评估指标
- 新框架的集成示例

---

## 💖 赞助者

支持这个项目，能让教育向的 AI 内容保持免费开放。如果贵公司在生产环境中使用智能体记忆，欢迎赞助，把贵司 logo 展示在下方。

<a href="https://github.com/sponsors/NirDiamant"><img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=ff69b4" alt="Become a Sponsor"/></a>

---

## 🔗 相关项目

本仓库是一个更大的 AI 技术教程系列的一部分。

| 仓库 | Stars | 方向 |
|-----------|-------|-------|
| [RAG Techniques](https://github.com/NirDiamant/RAG_Techniques) | 26k+ | 检索增强生成（RAG）技术 |
| [GenAI Agents](https://github.com/NirDiamant/GenAI_Agents) | 21k+ | 生成式 AI 智能体架构 |
| [Agents Towards Production](https://github.com/NirDiamant/agents-towards-production) | 18k+ | 生产级智能体部署 |
| [Prompt Engineering](https://github.com/NirDiamant/Prompt_Engineering) | 7k+ | 提示词工程技术 |

---

## 🏷️ 覆盖的主题

本仓库是 LLM 应用中智能体记忆的实用参考。完整的关键词索引（覆盖短期、长期、认知架构、检索、框架、评估与生产模式）见 [docs/topics.md](docs/topics.md)。

---

## ⚠️ 免责声明

本仓库仅用于教学目的。这里的代码用来展示智能体记忆技术的工作原理，不是生产级软件。未经仔细审查，不要把它原样用于处理受监管的数据、医疗决策、法律建议或任何高风险场景。作者对你如何使用这些材料不承担责任。

---

## 📄 许可证

本项目基于 Apache License 2.0 许可。详见 [LICENSE](LICENSE) 文件。

---

## 📖 引用

如果你在研究或教学中使用了本仓库，请引用：

```bibtex
@misc{diamant2026agentmemory,
    title={Agent Memory Techniques: A Cookbook for LLM Agent Memory},
    author={Nir Diamant},
    year={2026},
    url={https://github.com/NirDiamant/Agent_Memory_Techniques}
}
```

---

**由 [Nir Diamant](https://github.com/NirDiamant) 用心打造**，让每个人都能接触前沿 AI。

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme)
# Agent_Memory_Techniques_Deepagents_CN
