from anthropic import Anthropic

from a_share_analyst.config import load_agent_config
from a_share_analyst.prompts import BASE_PROMPT


def ask_a_share_analyst(messages: list[dict[str, str]]) -> str:
    if not messages:
        return "请输入要分析的问题。"

    config = load_agent_config()
    client = Anthropic(
        api_key=config.anthropic_api_key,
        base_url=config.anthropic_base_url,
    )

    response = client.messages.create(
        model=config.model,
        max_tokens=65536,
        system=BASE_PROMPT,
        messages=messages,
    )

    texts = []
    for block in response.content:
        if hasattr(block, "text"):
            texts.append(block.text)

    return "\n".join(texts).strip() or "没有收到有效回复。"
