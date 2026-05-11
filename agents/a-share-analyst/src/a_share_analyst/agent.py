from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, TextBlock, query

from a_share_analyst.config import build_sdk_env, load_agent_config
from a_share_analyst.prompts import BASE_PROMPT


async def ask_a_share_analyst(question: str) -> str:
    trimmed_question = question.strip()

    if not trimmed_question:
        return "请输入要分析的问题。"

    config = load_agent_config()
    answer_parts: list[str] = []

    async for message in query(
        prompt=trimmed_question,
        options=ClaudeAgentOptions(
            allowed_tools=[],
            max_turns=1,
            model=config.model,
            system_prompt=BASE_PROMPT,
            env=build_sdk_env(config),
        ),
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    answer_parts.append(block.text)

    return "\n".join(answer_parts).strip() or "没有收到有效回复。"
