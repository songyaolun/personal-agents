# Personal Agents

这个仓库用于沉淀我在学习和实践过程中搭建的各种 Agent。内容会围绕「能运行的 Agent 示例」「效果图展示」「技术架构拆解」和「实现经验总结」展开，方便自己复盘，也方便对 Agent 开发感兴趣的朋友参考。

## 仓库定位

- 收集不同场景下的个人 Agent 实践案例
- 展示 Agent 的运行效果、交互流程和关键能力
- 记录每个 Agent 的技术选型、架构设计和实现细节
- 总结 Prompt、工具调用、工作流编排、记忆管理等方向的实践经验

## 内容规划

```text
personal-agents/
├── agents/                 # Agent 示例项目
│   └── example-agent/
│       ├── README.md        # 单个 Agent 的说明文档
│       ├── src/             # 源码
│       ├── assets/          # 效果图、架构图、演示素材
│       └── docs/            # 设计说明、实现笔记
├── docs/                    # 通用文档和技术总结
├── assets/                  # 仓库级展示素材
└── README.md
```

> 当前仓库还在持续整理中，目录会随着 Agent 示例逐步补齐。

## Agent 列表

| Agent | 场景 | 技术栈 | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| [A-Share Analyst](./agents/a-share-analyst/) | A 股分析 | Python, uv, Claude Agent SDK | 开发中 | 面向 A 股市场的信息收集、分析和总结 Agent |

## 展示内容

每个 Agent 会尽量包含以下内容：

- 效果图：展示 Agent 的界面、运行结果或关键交互过程
- 架构图：说明 Agent、模型、工具、数据源和外部服务之间的关系
- 核心流程：拆解任务理解、计划生成、工具调用、结果校验等关键步骤
- 代码说明：介绍主要模块职责和关键实现
- 复盘记录：记录有效做法、踩坑点和可优化方向

## 技术方向

这个仓库会重点关注以下方向：

- LLM 应用开发
- Agent 工作流编排
- Tool Calling / Function Calling
- RAG 与外部知识接入
- 多 Agent 协作
- 长短期记忆设计
- 浏览器、文件系统、API 等工具集成
- 评测、可观测性与调试

## 文档规范

新增 Agent 时建议保持统一结构：

```text
agents/<agent-name>/
├── README.md
├── src/
├── assets/
│   ├── screenshots/
│   └── architecture/
└── docs/
```

单个 Agent 的 `README.md` 建议包含：

- 背景与目标
- 功能特性
- 效果展示
- 技术架构
- 本地运行方式
- 关键实现说明
- 后续计划

## 许可证

本仓库使用 [LICENSE](./LICENSE) 中声明的许可证。
