# 术语表（GLOSSARY）

翻译本仓库时使用的统一术语表。规则见 [TRANSLATION_STANDARD.md](TRANSLATION_STANDARD.md)。概念定义（英文原意）另见 `docs/glossary.md`，本表只管翻译用词。

## A. 不翻译的专有名词

原则：产品、框架、公司、模型、基准、数据集、课程、书、人名，一律保留英文原文。

| 原文 | 类别 |
|---|---|
| Mem0、Letta、MemGPT、Zep、Graphiti、MemOS、Memori、Cognee | 记忆框架与产品 |
| LoCoMo、LongMemEval | 记忆基准 |
| LangChain、LlamaIndex、Chroma、FAISS、Qdrant、Pinecone、Neo4j、NetworkX、Redis、Postgres、pgvector、tiktoken、SQLite | 库与工具 |
| OpenAI、Anthropic、Claude、GPT | 公司与模型 |
| RAG、LLM、API、CI、GDPR、TTL、ASCII、Mermaid、CRUD、PII、NER、ANN、LRU、FIFO、MMR、NER | 通用缩写，业界惯例不译；首次出现可加中文注释，如「检索增强生成（RAG）」 |
| Jupyter、Colab、GitHub、pytest、nbformat、matplotlib、deque | 工具与类型 |
| Prompt to Production、Agent Memory Made Simple、RAG Made Simple | 课程与书名 |
| Nir Diamant | 作者名 |
| notebook、token、schema、embedding 之外的惯用英文词（如 cross-encoder、n-gram、upsert、gist token、lost in the middle、LLM-as-judge） | 业界惯用，不译或首次加注 |

## B. 统一译法

| 英文 | 中文译法 | 备注 |
|---|---|---|
| agent | 智能体 | 仓库名 Agent Memory Techniques 保留英文 |
| agent memory | 智能体记忆 | |
| memory | 记忆 | |
| short-term memory | 短期记忆 | |
| long-term memory | 长期记忆 | |
| working memory | 工作记忆 | |
| context window | 上下文窗口 | |
| conversation buffer memory | 对话缓冲记忆 | 技术 01 |
| sliding window memory | 滑动窗口记忆 | 技术 02 |
| summary memory | 摘要记忆 | 技术 03 |
| summary buffer memory | 摘要缓冲记忆 | 技术 04 |
| token buffer memory | token 缓冲记忆 | 技术 05 |
| vector store memory | 向量库记忆 | 技术 06 |
| entity memory | 实体记忆 | 技术 07 |
| knowledge graph memory | 知识图谱记忆 | 技术 08 |
| episodic memory | 情景记忆 | 心理学标准译法，技术 09 |
| semantic memory | 语义记忆 | 技术 10 |
| procedural memory | 程序性记忆 | 技术 11 |
| working memory & context window | 工作记忆与上下文窗口 | 技术 12 |
| hierarchical memory layers | 分层记忆 | 技术 13 |
| memory consolidation | 记忆巩固 | 神经科学标准译法，技术 14 |
| memory compaction | 记忆压缩 | 技术 15 |
| self-reflection memory | 自我反思记忆 | 技术 16 |
| memory routing | 记忆路由 | 技术 17 |
| temporal memory | 时序记忆 | 技术 18 |
| forgetting and decay | 遗忘与衰减 | 技术 19 |
| memory retrieval patterns | 记忆检索模式 | 技术 20 |
| cross-session memory | 跨会话记忆 | 技术 21 |
| multi-agent shared memory | 多智能体共享记忆 | 技术 22 |
| memory with tools | 工具化记忆 | 技术 23 |
| Memory-as-a-Tool | 记忆即工具 | 技术 23 模式别名，首次出现标注英文 |
| graph memory | 图记忆 | 技术 24 |
| patterns | 模式 | |
| production memory patterns | 生产级记忆模式 | 技术 30 |
| memory evaluation | 记忆评估 | 技术 28 |
| memory benchmarks | 记忆基准测试 | 技术 29 |
| session | 会话 | |
| turn | 轮次 | |
| message | 消息 | |
| state | 状态 | |
| retrieval | 检索 | |
| embedding | 嵌入 | |
| vector | 向量 | |
| chunk / chunking | 分块 | |
| re-ranking | 重排序 | |
| recency | 新近度 | |
| precision / recall | 查准率 / 查全率 | recall 作检索指标时 |
| recall | 回忆 | 指智能体想起先前信息的能力时；作指标仍译查全率 |
| recall memory | 召回记忆 | MemGPT 三层的温层；first occurrence 标注英文 |
| core memory | 核心记忆 | MemGPT 三层的常驻热层 |
| archival memory | 归档记忆 | MemGPT 三层的冷层 / 长期存储 |
| three-tier memory | 三层记忆 | core / recall / archival 结构 |
| virtual memory | 虚拟内存 | MemGPT 的核心类比 |
| paging / page in / page out | 换页 / 换入 / 换出 | 上下文与归档之间移动信息 |
| staleness | 陈旧度 | |
| contradiction | 矛盾 | |
| contradiction detection | 矛盾检测 | |
| conflict resolution | 冲突解决 | 三种译法统一为此 |
| last-write-wins | 后写胜出 | 冲突解决策略 |
| recency-wins | 新近度优先 | 冲突解决策略 |
| source priority | 来源优先 | 用户陈述 > 推断 > 工具输出 |
| version check / optimistic locking | 版本检查 / 乐观锁 | 同义策略 |
| distillation | 蒸馏 | |
| deduplication | 去重 | |
| eviction | 淘汰 | |
| eviction policy | 淘汰策略 | |
| message-level eviction | 消息级淘汰 | |
| orphaned message | 孤立消息 | 只剩回答、没有对应提问的消息 |
| promotion / demotion | 升级 / 降级 | 分层存储场景 |
| hot / warm / cold layers | 热 / 温 / 冷层 | |
| tier / tiered storage | 层 / 分层存储 | |
| workhorse tier | 主力层 | 承担主要存储负载的一层 |
| cascading retrieval | 级联检索 | L1 未命中逐级落到 L2/L3 |
| rebalancing | 再均衡 | 分片场景 |
| cross-shard queries | 跨分片查询 | |
| sharding | 分片 | |
| caching | 缓存 | |
| cache hit rate | 缓存命中率 | |
| backup | 备份 | |
| benchmark | 基准测试 | |
| cell / code cell / markdown cell | 单元格 / 代码单元格 / Markdown 单元格 | |
| prompt | 提示词 | |
| system prompt | 系统提示词 | role=system 的提示 |
| knowledge graph | 知识图谱 | |
| cognitive architecture | 认知架构 | |
| taxonomy | 分类 | |
| decision tree | 决策树 | |
| learning path | 学习路径 | |
| Associative Memory | 联想记忆 | 仅见于 08 notebook 页脚链接的旧称；09 目录实为情景记忆（Episodic Memory） |

## B2. 并行翻译补充术语（技术 02-30 汇总，冲突已裁决）

| 英文 | 中文译法 | 备注 |
|---|---|---|
| semantic search | 语义检索 | 部分目录作「语义搜索」，均为可接受表达 |
| lexical search | 词法检索 | 基于关键词匹配，BM25 属此类 |
| hybrid retrieval / hybrid search | 混合检索 | 语义 + 词法/图遍历等组合 |
| cosine similarity | 余弦相似度 | |
| BM25 | BM25 | 不译；词频 × 逆文档频率 × 文档长度 |
| term frequency / inverse document frequency | 词频 / 逆文档频率 | |
| similarity search | 相似度搜索 | |
| approximate nearest neighbor (ANN) | 近似最近邻 | 缩写保留英文 |
| cross-encoder | 交叉编码器 | |
| Maximal Marginal Relevance (MMR) | 最大边际相关性（MMR） | |
| Reciprocal Rank Fusion (RRF) | 倒数排名融合（RRF） | |
| Mean Reciprocal Rank (MRR) | 平均倒数排名（MRR） | |
| Precision@K / Recall@K | 保留英文 | 首次出现加（查准率/查全率）注释 |
| ground truth | 标准答案 | 评估语境 |
| LLM judge / LLM-as-judge | 保留英文 | 首次加注「让语言模型给质量打分」 |
| faithfulness | 忠实度 | 回答只陈述源记忆能支撑的内容 |
| hallucination | 幻觉 | |
| abstention | 拒答 | LongMemEval 能力 |
| coverage | 覆盖率 | |
| ablation | 消融实验 | |
| baseline | 基线 | |
| control run | 对照组 | |
| no-memory baseline | 无记忆基线 | |
| full-context baseline | 全上下文基线 | |
| confusion matrix | 混淆矩阵 | |
| true/false positive, false negative | 真阳性 / 假阳性 / 漏报 | PII、评估语境 |
| F1 score | F1 分数 | |
| stratified sampling | 分层抽样 | |
| regression | 回归 | 改动导致变差的评估场景 |
| evidence | 证据 | LoCoMo 问答标注 |
| single-hop / multi-hop | 单跳 / 多跳 | LoCoMo 问题类别 |
| temporal reasoning | 时序推理 | LoCoMo 类别 2 |
| knowledge update | 知识更新 | LongMemEval 能力 |
| information extraction | 信息提取 | LongMemEval 能力 |
| as-of retrieval / query | 时点检索 / 时点查询 | 排除某时间点之后的记忆 |
| triple (subject-predicate-object) | 三元组（主谓宾） | |
| triple extraction | 三元组抽取 | |
| subgraph retrieval | 子图检索 | |
| graph traversal | 图遍历 | |
| node / edge | 节点 / 边 | 图论标准译法 |
| adjacency list | 邻接表 | |
| node degree | 节点度 | |
| community detection | 社区检测 | |
| breadth-first search (BFS) | 广度优先搜索（BFS） | |
| union-find | 并查集 | |
| entity resolution | 实体消解 | 知识图谱标准译法 |
| entity extraction | 实体抽取 | |
| named entity recognition (NER) | 命名实体识别（NER） | |
| disambiguation | 消歧 | |
| relationship extraction | 关系抽取 | |
| temporal knowledge graph | 时序知识图谱 | Graphiti 核心概念，全仓库统一 |
| temporal edge | 时序边 | |
| ingestion | 摄取 | Graphiti 写入流程 |
| episode | episode | Graphiti 术语/API 名保留英文；泛指交互单元时译「片段」 |
| thread | 线程 | Zep 的对话容器，首次出现写「线程（thread）」 |
| assembled context | 组装上下文 | Zep 预生成的注入文本块 |
| dialog classification | 对话分类 | Zep 能力 |
| managed memory layer | 托管记忆层 | |
| managed service | 托管服务 | |
| self-improving memory | 自我改进的记忆 | Mem0 |
| reconciliation | 核对合并 | Mem0 处理矛盾与重复 |
| upsert | upsert | 不译 |
| self-editing memory | 自编辑记忆 | Letta/MemGPT |
| self-editing memory blocks | 自编辑记忆块 | |
| inner / outer monologue | 内心独白 / 外部独白 | |
| heartbeat / heartbeat chaining | 心跳 / 心跳串联 | MemGPT 语境 |
| memory pressure | 记忆压力 | |
| persona block / human block | persona 块 / human 块 | 块名保留英文 |
| recall memory（MemGPT 分层名） | 召回记忆 | 首次出现标注英文 |
| blackboard system | 黑板系统 | 经典分布式 AI 架构 |
| message passing | 消息传递 | |
| private scratchpad | 私人草稿本 | 其他智能体不可见 |
| namespace | 命名空间 | 共享记忆的逻辑分区 |
| race condition / lock / thread safety | 竞态条件 / 锁 / 线程安全 | |
| single point of failure | 单点故障 | |
| cross-contamination | 串数据 | 用户间记忆互相泄漏 |
| user-scoped | 按用户隔离 | |
| access control | 访问控制 | |
| audit log / audit trail | 审计日志 / 审计线索 | |
| data retention | 数据保留 | |
| differential privacy | 差分隐私 | |
| soft delete / hard delete | 软删除 / 硬删除 | |
| right to forget | 被遗忘权 | GDPR Article 17 |
| redaction | 脱敏 | 敏感信息替换为占位符 |
| placeholder | 占位符 | |
| PII (personally identifiable information) | 个人身份信息（PII） | |
| TTL (time-to-live) | TTL（存活时间） | 缩写保留 |
| GDPR | GDPR | |
| observability | 可观测性 | |
| cache hit rate / miss | 缓存命中率 / 未命中 | |
| connection pooling | 连接池 | |
| pre-fetching | 预取 | |
| point-in-time recovery | 时间点恢复 | |
| write-ahead log (WAL) | 预写日志 | Postgres 语境 |
| vendor lock-in | 供应商锁定 | |
| drop-in | 即插即用 | |
| bill shock | 账单失控 | |
| spend cap | 支出上限 | |
| token budget | token 预算 | |
| token overhead | token 开销 | |
| per-message overhead | 单条消息开销 | 每条约 4 token 的格式开销 |
| salience / salience scoring | 显著性 / 显著性评分 | 技术 12 |
| attention management | 注意力管理 | |
| attentional controller | 注意控制器 | Baddeley 工作记忆模型 |
| context prioritization | 上下文优先级排序 | |
| pinned / pinning | 固定 / 置顶 | 受保护、不参与淘汰 |
| pinned zone / dynamic zone / buffer zone | 固定区 / 动态区 / 缓冲区 | 技术 12 的区域划分 |
| priority queue | 优先级队列 | |
| importance scoring / weighting | 重要性打分 / 加权 | |
| access counter / access frequency | 访问计数器 / 访问频率 | |
| reinforcement / reinforcement boost | 强化 / 强化增益 | 记忆被检索后提升强度 |
| recency decay / score / scoring | 新近度衰减 / 得分 / 评分 | |
| recency-weighted retrieval | 新近度加权检索 | |
| strength | 强度 | 记忆的重要性分数 |
| decay function | 衰减函数 | 指数 / 线性 |
| exponential / linear decay | 指数 / 线性衰减 | |
| half-life | 半衰期 | 衰减得分的调参参数 |
| time decay / temporal decay | 时间衰减 | |
| evergreen knowledge / facts | 常青知识 / 常青事实 | 不该被衰减惩罚的长期事实 |
| Ebbinghaus forgetting curve | 艾宾浩斯遗忘曲线 | |
| forgetting curve | 遗忘曲线 | |
| spaced repetition | 间隔重复 | |
| prune / pruning threshold | 修剪 / 修剪阈值 | |
| sweep | 扫描 | 定期遍历执行修剪的一轮操作 |
| noise | 噪声 | |
| thrashing | 抖动 | 记忆在层间来回移动 |
| cold start (problem) | 冷启动（问题） | |
| onboarding | 引导 | 冷启动时收集初始偏好 |
| hybrid retrieval | 混合检索 | |
| rolling summary / running summary | 滚动摘要 | 两词统一 |
| incremental summarization | 增量摘要 | |
| progressive summarization | 渐进式摘要 | Tiago Forte 方法名 |
| narrative summary | 叙事式摘要 | |
| abstractive compression | 抽象式压缩 | |
| lossy / lossless | 有损 / 无损 | |
| compression ratio | 压缩比 | |
| fidelity / fidelity level | 保真度 / 保真度级别 | |
| fact retention | 事实保留率 | 原始事实在摘要中存活的比例 |
| summary drift | 摘要漂移 | 反复摘要导致事实失真 |
| refresh trigger | 刷新触发器 | 何时重新生成摘要 |
| key points / one-liner | 要点 / 一句话摘要 | L1/L2 压缩级别 |
| tags / entity reference | 标签 / 实体引用 | L3 压缩级别 |
| compaction level / engine / scheduler | 压缩级别 / 压缩引擎 / 压缩调度器 | 技术 15 组件 |
| age-based / idle-based policy | 按存留时间 / 按空闲时间的策略 | 压缩触发策略 |
| storage pressure | 存储压力 | |
| insight | 洞见 | 反思记忆的存储单元 |
| insight extraction | 洞见提取 | |
| reflection prompt | 反思提示词 | |
| reflection memory store | 反思记忆库 | |
| reflect-then-store loop | 反思存储循环 | |
| reflection-triggered learning | 反思触发学习 | |
| meta-cognition | 元认知 | |
| verbal reinforcement learning | 语言强化学习 | Reflexion 论文术语 |
| fine-tuning | 微调 | |
| execution trace / trace | 执行轨迹 / 轨迹 | |
| procedure extraction / generalization / adaptation | 过程抽取 / 过程泛化 / 过程适配 | 技术 11 |
| skill library | 技能库 | |
| procedural / declarative knowledge | 程序性知识 / 陈述性知识 | |
| workflow template | 工作流模板 | |
| tool-use pattern | 工具使用模式 | |
| learning curve | 学习曲线 | |
| root cause | 根本原因 | |
| outcome evaluation | 结果评估 | |
| episode boundary / summary / store | 片段边界 / 片段摘要 / 片段库 | episode 泛指交互单元时译「片段」 |
| dispatcher | 分发器 | 工具分发器；17 的调度义译「调度器」 |
| fan-out | 扇出 | |
| read routing / write routing | 读取路由 / 写入路由 | |
| misrouting | 误路由 | |
| multi-label classification | 多标签分类 | |
| fallback (strategy) | 回退（策略） | |
| keyword overlap | 关键词重叠 | |
| memory store / memory entry | 记忆存储 / 记忆条目 | 类名 MemoryStore 保留英文 |
| store registry | 存储注册表 | |
| metadata / metadata filtering | 元数据 / 元数据过滤 | |
| memory profile | 记忆画像 | 某用户的全部记忆集合 |
| user profile | 用户画像 | |
| fact accumulation | 事实积累 | |
| declarative fact | 陈述式事实 | |
| entity store | 实体存储 | |
| entity-context injection | 实体上下文注入 | |
| prompt assembly | 提示词组装 | |
| context injection | 上下文注入 | |
| query transformation | 查询转换 | |
| HyDE | 假设文档嵌入（HyDE） | |
| flat memory store | 扁平记忆库 | |
| knowledge base | 知识库 | |
| merge | 合并 | |
| near-duplicate / duplicate group | 近似重复 / 重复组 | |
| cluster / cluster engine | 簇 / 聚类引擎 | |
| batch processing | 批处理 | |
| consolidation cycle / trigger / scheduled | 一轮巩固 / 巩固触发条件 / 计划巩固 | |
| external memory store | 外部记忆库 | |
| archival storage | 归档存储 | |
| cold storage | 冷存储 | |
| blob store | 对象存储 | |
| vector database | 向量数据库 | |
| format lock-in | 格式锁定 | |
| schema evolution | 模式演进 | |
| distribution mismatch | 分布不匹配 | 基准对话与目标用例不一致 |
| adversarial question | 对抗性问题 | LoCoMo 类别 5 |
| open-ended question | 开放式问题 | LoCoMo 类别 4 |
| narrative continuity | 叙事连续性 | |
| autobiographical memory | 自传体记忆 | 心理学标准译法 |
| behavioral patterns | 行为模式 | |
| encoding（tiktoken 语境） | 编码 | 模型使用的 token 词表 |
| tokenizer / word-piece | 分词器 / 词片段 | |
| fallback | 回退 | 检索失败或置信度低时的备选方案 |

## C. 翻译进度

全部完成（2026-02 会话）。

| 内容 | 状态 |
|---|---|
| 主 README.md | ✅ |
| 01_conversation_buffer_memory | ✅ |
| 02_sliding_window_memory | ✅ |
| 03_summary_memory | ✅ |
| 04_summary_buffer_memory | ✅ |
| 05_token_buffer_memory | ✅ |
| 06_vector_store_memory | ✅ |
| 07_entity_memory | ✅ |
| 08_knowledge_graph_memory | ✅ |
| 09_episodic_memory | ✅ |
| 10_semantic_memory | ✅ |
| 11_procedural_memory | ✅ |
| 12_working_memory_context_window | ✅ |
| 13_hierarchical_memory_layers | ✅ |
| 14_memory_consolidation | ✅ |
| 15_memory_compaction | ✅ |
| 16_self_reflection_memory | ✅ |
| 17_memory_routing | ✅ |
| 18_temporal_memory | ✅ |
| 19_forgetting_and_decay | ✅ |
| 20_memory_retrieval_patterns | ✅ |
| 21_cross_session_memory | ✅ |
| 22_multi_agent_shared_memory | ✅ |
| 23_memory_with_tools | ✅ |
| 24_graph_memory_graphiti | ✅ |
| 25_mem0_patterns | ✅ |
| 26_letta_memgpt_patterns | ✅ |
| 27_zep_memory | ✅ |
| 28_memory_evaluation | ✅ |
| 29_memory_benchmarks_LoCoMo | ✅ |
| 30_production_memory_patterns | ✅ |

## B3. 端点迁移补充术语

| 英文 | 中文译法 | 备注 |
|---|---|---|
| OpenAI-compatible endpoint | OpenAI 兼容端点 | 统一用 `LLM_API_KEY` / `LLM_BASE_URL` / `LLM_MODEL_NAME` 接入 |
| local fallback embedding | 本地兜底向量 | 网关没有 `/embeddings` 时的确定性词 + n-gram 哈希向量 |
| tool calling | 工具调用 | 覆盖各家 function calling / tool use 表述 |
