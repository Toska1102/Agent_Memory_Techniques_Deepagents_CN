# 翻译标准（TRANSLATION_STANDARD）

本文件规定 Agent_Memory_Techniques 中文翻译的统一规则。术语的统一译法见 [GLOSSARY.md](GLOSSARY.md)。本仓库原文遵循 `docs/CONTENT_STANDARDS.md`，中文译稿保持同样的教学风格。

## 翻译什么

- 主 `README.md` 和每个技术目录下的 `README.md`
- notebook 里的 markdown 单元格
- 代码单元格里的注释（`#` 注释、docstring）
- 图片的 alt 文本、表格表头，以及一切给人读的文字

## 不碰什么

- 代码本身、命令、shell 片段、文件路径、目录名、URL、链接 href、锚点目标、HTML 标签与属性、badge 与 tracker 链接
- 专有名词（见 GLOSSARY.md A 部分：框架、产品、基准、公司、人名）
- notebook 的结构：cell 顺序、outputs、metadata、nbformat 字段一律不动
- markdown 结构：标题层级、表格、列表、emoji、分隔线保持原样

## 怎么译

- 准确流畅优先，逐段翻译，不删减、不增写内容
- 句子短，主动语态，对读者用「你」
- 避免翻译腔：不滥用「被」字句，不用「值得注意的是」一类填充语，不逐词直译
- 通用术语第一次出现写成「中文译法（English）」，之后只用中文；专有名词始终保留英文
- 中文用全角标点；代码、数字、英文单词前后留一个半角空格；不用长破折号
- 标题翻译后，同步更新文内锚点链接（GitHub 用标题文字生成锚点，中文标题生成中文锚点）
- 链接文字可以翻译，链接地址不改

## notebook 操作规程

- 直接编辑 ipynb 的 JSON：markdown cell 改 `source`；code cell 只改注释行
- 改完用 `python -m json.tool` 或 `nbformat.validate` 校验文件仍是合法 ipynb
- 不重新执行任何 cell，不清 outputs

## 流程与维护

- 每翻译一个文件：先查 GLOSSARY.md；遇到表里没有的新术语，先补录进 GLOSSARY.md，再动笔
- 完成一个文件后在 GLOSSARY.md 的进度表里打勾
- 标准文件的更新与对应的翻译放在同一批改动里

## 与上游的关系

- 本仓库是 NirDiamant/Agent_Memory_Techniques 的本地中文译本，翻译在原文件上就地覆盖，英文原文保留在 git 历史里
- 仓库自带的 `utils/validate_style.py` 面向英文原文校验文风，翻译稿不保证通过；向上游贡献时请使用英文原稿
