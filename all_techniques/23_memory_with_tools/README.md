# 工具化记忆（Memory with Tools / Memory-as-a-Tool）

<p align="center">
  <a href="https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/23_memory_with_tools/memory_with_tools.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="在 Colab 中打开"/></a>
</p>

## 📖 速览

| 难度 | 用时 | 前置要求 |
|------------|------|---------------|
| 中级 | 约 35 分钟 | Python 3.8+、`LLM_API_KEY`，建议先了解 06 向量库记忆 |

本技术面向构建工具使用型智能体的开发者：这类智能体会持久化工具结果，并用已存的知识指导后续的工具调用。

## TL;DR

- **是什么：** **工具化记忆**把记忆 CRUD 操作暴露为可调用的工具，由智能体自己决定何时保存、检索、更新或删除记忆。
- **适用时机：** 你想让智能体自己控制记住什么，而不是依赖自动抽取。
- **权衡：** 每次工具调用都多一次 API 往返；如果没人提醒，智能体可能忘记保存重要事实。
- **本仓库中最接近的替代方案：** 25 Mem0 Patterns 用自动抽取代替智能体显式调用工具。

## 说明

想象一位图书管理员：她决定哪些书上架、替你查找哪些书、淘汰哪些过时的书。她不按固定流程办事，而是根据你的请求自行判断。工具化记忆（也叫记忆即工具，Memory-as-a-Tool）让 LLM 智能体对自己的智能体记忆拥有同样的控制权。你不再在幕后管理记忆，而是把增查改删（CRUD）操作暴露为智能体工具使用循环中的可调用工具。智能体借助语义检索决定何时保存、检索、更新或删除记忆。这种做法适合自主智能体、对话助手，以及任何需要模型主动打理自己知识库的系统。

**关键词：** agent memory, LLM agent, memory-as-a-tool, tool-use, memory CRUD, semantic search, agent-driven memory, save memory, search memory, Anthropic tool use

这项技术不再靠提示词工程或框架层代码在幕后管理记忆，而是给智能体一组显式、可调用的记忆工具。四个工具分别是 `save_memory`、`search_memory`、`update_memory` 和 `delete_memory`。智能体通过标准的工具使用循环调用它们，就像调用网页搜索或执行代码一样。

何时记住、记住什么、查什么、忘什么，都由智能体决定。这让记忆管理成为智能体推理中的一等公民。这项技术使用 OpenAI 兼容的工具调用。「tool_use 模式」指智能体可以在生成过程中请求一次工具调用，由系统执行并把结果返回。记忆操作与其他工具一起出现在智能体的动作空间里。

最终得到的是一个主动打理自己知识库的智能体。用户提到重要事实后它会保存。回答之前它会检索相关上下文。收到更正时它会修剪过时的信息。

## 核心概念

- **工具 schema（tool schema）**：对可调用函数的结构化描述，包含工具名称、用途和期望的输入（采用 JSON Schema 格式）。
- **记忆 CRUD（memory CRUD）**：四个核心操作（创建 Create、读取 Read、更新 Update、删除 Delete），分别暴露为 `save_memory`、`search_memory`、`update_memory`、`delete_memory` 四个工具。
- **智能体工具使用循环（agentic tool-use loop）**：LLM 生成响应、可选择发起工具调用、接收结果、继续生成的循环。反复进行，直到模型产出不含工具调用的最终文本响应。
- **`tool_use` / `tool_result` 块**：Anthropic 用于工具调用的内容块类型。模型发出 `tool_use` 请求一次调用；你的代码返回 `tool_result` 并附上输出。
- **语义检索（semantic search）**：按含义而非精确关键词查找存储内容。我们对查询做嵌入，找出余弦相似度最高的记忆。
- **智能体自主记忆（agent-driven memory）**：LLM 根据对话上下文自行决定何时存储、检索、修改或丢弃信息。

## Notebook

[实现本技术的 notebook](./memory_with_tools.ipynb) 包含以下内容：

1. **工具定义**：四个兼容 Anthropic 的记忆 CRUD 工具 schema。
2. **记忆库**：一个 `MemoryStore` 类，带基于哈希的嵌入和余弦相似度检索。
3. **工具分发器**：把工具调用路由到正确记忆操作的函数。
4. **系统提示词**：引导模型何时保存、检索、更新、删除的指令。
5. **智能体循环**：完整的 `chat_with_memory` 函数，驱动带工具调用的多轮对话。
6. **运行示例**：一段贴近真实的对话，覆盖全部四个操作，包括工具链式调用。

## 架构

<p align="center">
  <img src="../../images/diagrams/23_memory_with_tools.svg" alt="工具化记忆架构图" width="720"/>
</p>

## 工作原理

1. 你定义四个工具 schema（保存、检索、更新、删除），并把它们注册给 LLM。
2. `MemoryStore` 以文本加向量嵌入的形式保存记忆，支持语义检索（按含义查找，而非精确关键词）。
3. 对话过程中，LLM 根据上下文决定何时调用记忆工具。
4. 分发器把每次工具调用路由到正确的 `MemoryStore` 方法，并返回结果。
5. LLM 收到工具结果后继续生成，并可能在同一轮里继续链式调用更多工具。
6. 循环反复进行，直到 LLM 给出不再请求工具的最终文本响应。

## 何时使用

- 你想让智能体自己判断什么值得记，而不是自动保存一切。
- 用户提供新信息时，智能体需要能更正或删除过时的记忆。
- 你在构建一个自主智能体，需要把记忆工具和其他工具（网页搜索、代码执行）组合使用。
- 你需要透明、可审计的记忆操作，让每次保存和删除都出现在对话日志里。

## 局限

- 智能体可能忘记保存重要事实，也可能保存太多噪音。质量取决于模型的判断。
- 每次工具调用都增加一次 API 往返。链式执行多个操作（先检索、再更新、再删除）会拉高延迟。
- 工具 schema 在每次请求中消耗 500-800 个 token。即使没有任何记忆操作，这笔开销也存在。
- 记忆管理只在活跃轮次运行。智能体不会在对话之间巩固或清理记忆。

## FAQ

### 问：智能体记忆中的工具化记忆是什么？

**答：** 工具化记忆（也叫记忆即工具，Memory-as-a-Tool）把记忆 CRUD 操作暴露为可调用工具，智能体通过工具使用接口来调用它们。记忆管理不再是自动的：何时调用 `save_memory`、`search_memory`、`update_memory` 或 `delete_memory` 由智能体自己决定。存储什么、检索什么，控制权完全在智能体手里。这个模式适用于任何支持工具调用的 LLM（GPT-4、Claude、Gemini），工具接口背后的存储后端也可以任意替换。

### 问：什么时候该用工具化记忆而不是 Mem0 Patterns？

**答：** 当你希望智能体对「记住什么」做出显式、可审计的决策时，用工具化记忆。Mem0（技术 25）自动抽取并存储事实，上手更容易，但控制力较弱。工具化方式让智能体精确选择保存什么、何时检索。如果你需要弄清楚智能体为什么存了某条事实，或者出于合规需要可审计性，显式工具调用比自动抽取更合适。

### 问：工具化记忆有哪些局限或失败模式？

**答：** 智能体可能忘记调用保存工具，导致重要信息丢失；也可能保存过多，存入噪音，污染之后的检索。工具调用为每个操作增加延迟（100-300ms）。智能体必须学会何时使用哪个工具，这需要写好工具描述，有时还要给少量示例（few-shot）。如果 LLM 的工具调用能力弱，记忆操作可能失败或返回意外的格式。为工具描述做提示词工程是可靠性的关键。

### 问：工具化记忆可以和其他记忆技术组合吗？

**答：** 可以。工具接口是一层包装，可以对接任何存储技术。把 `save_memory` 接到技术 10（语义记忆）来存事实，把 `search_memory` 接到技术 06（向量库记忆）来做检索，把 `delete_memory` 接到技术 19（遗忘与衰减）来做清理。再在工具后面加上技术 17（记忆路由），保存操作就会自动路由到合适的存储。工具模式是一个控制接口，不是一种存储技术。

### 问：有什么库或框架可以省去自己实现的工作？

**答：** LangChain 通过 `Tool` 或 `StructuredTool` 类支持自定义工具，把任何记忆后端包装成可调用工具都很方便。OpenAI 的 function calling 和 Claude 的 tool use 原生支持这个模式。Mem0（技术 25）提供了对工具友好的 API，10 行代码就能包装起来。Letta/MemGPT（技术 26）完全围绕基于工具的记忆模式构建，内置了智能体可以直接调用的记忆管理函数。

## 参考资料

- [Anthropic 工具使用文档](https://docs.anthropic.com/en/docs/build-with-claude/tool-use?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)
- [OpenAI Function Calling 指南](https://platform.openai.com/docs/guides/function-calling?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)
- [Packer 等人（2023），"MemGPT: Towards LLMs as Operating Systems."](https://arxiv.org/abs/2310.08560)
- [Anthropic：Building Effective Agents（2025）](https://www.anthropic.com/engineering/building-effective-agents?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)
- [Zep 记忆工具集成](https://docs.getzep.com?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)

## 相关技术

- [**06 向量库记忆**](../06_vector_store_memory/) - 许多记忆工具在语义检索下使用的底层存储方式。
- [**25 Mem0 集成模式**](../25_mem0_patterns/) - 一个托管服务，自动完成本技术手动搭建的保存/检索/更新/删除循环。
- [**26 Letta（MemGPT）模式**](../26_letta_memgpt_patterns/) - 智能体通过工具调用管理自身记忆的框架，思路与本文类似，但带分层存储。
- [**16 自我反思记忆**](../16_self_reflection_memory/) - 增加一个反思步骤，让智能体评估什么值得记，与基于工具的记忆控制互补。

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=all-techniques--23-memory-with-tools--readme)
