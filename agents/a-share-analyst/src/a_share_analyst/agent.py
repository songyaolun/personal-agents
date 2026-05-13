from anthropic import Anthropic

from a_share_analyst.config import load_agent_config
from a_share_analyst.prompts import BASE_PROMPT


def ask_a_share_analyst(messages: list[dict[str, str]]):
    """Stream response from the analyst, yielding text deltas."""
    if not messages:
        yield "请输入要分析的问题。"
        return

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
        stream=True,
    )

    has_content = False
    for event in response:
        if event.type == "content_block_delta" and hasattr(event.delta, "text"):
            has_content = True
            yield event.delta.text

    if not has_content:
        yield "没有收到有效回复。"
