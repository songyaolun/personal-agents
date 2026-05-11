# A-Share Analyst

A-Share Analyst 是一个面向 A 股市场分析场景的 Agent。目标是辅助完成个股、行业和市场信息的收集、整理、分析与总结。

## 背景与目标

- 聚合 A 股相关的公开信息、行情数据和研究材料
- 辅助分析公司基本面、行业趋势、市场情绪和风险点
- 输出结构化、可复盘的分析结论

## 功能规划

- 个股基础信息整理
- 财务指标和估值指标分析
- 行业与概念板块信息总结
- 公告、新闻和研报要点提取
- 风险因素和不确定性提示
- 分析过程与引用来源记录

## 技术架构

当前先实现一个基础问答 CLI，后续再接入行情、公告、财报、新闻等工具。

```text
用户输入
  ↓
CLI 交互层 src/a_share_analyst/cli.py
  ↓
A 股分析 Agent 封装 src/a_share_analyst/agent.py
  ↓
提示词约束 src/a_share_analyst/prompts.py
  ↓
Claude Agent SDK query()
```

## 效果展示

待补充。

## 本地运行

### 环境要求

- Python 3.11+
- uv
- Anthropic API Key

### 安装依赖

```bash
uv sync
```

### 配置环境变量

复制示例配置：

```bash
cp .env.example .env
```

然后填写：

```bash
ANTHROPIC_API_KEY=your-api-key
ANTHROPIC_BASE_URL=
CLAUDE_MODEL=
```

也可以直接使用 shell 环境变量：

```bash
export ANTHROPIC_API_KEY=your-api-key
```

配置说明：

- `ANTHROPIC_API_KEY`：必填，用于 Claude / Anthropic 鉴权。
- `ANTHROPIC_BASE_URL`：可选，用于代理网关或兼容 Anthropic API 的服务。
- `CLAUDE_MODEL`：可选，用于指定 Claude 模型；留空时使用 SDK/Claude CLI 默认模型。

### 启动问答

```bash
uv run a-share-analyst
```

## 关键实现

- `src/a_share_analyst/cli.py`：负责命令行输入输出
- `src/a_share_analyst/agent.py`：封装 Claude Agent SDK 的 `query()` 调用
- `src/a_share_analyst/prompts.py`：维护 A 股分析 Agent 的基础提示词

## 后续计划

- 明确数据源和工具调用边界
- 设计标准化分析报告模板
- 增加效果图和架构图
- 接入行情、公告、财报、新闻等外部工具
