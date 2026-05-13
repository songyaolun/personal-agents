import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class AgentConfig:
    anthropic_api_key: str
    anthropic_base_url: str | None
    model: str


def _optional_env(name: str) -> str | None:
    value = os.getenv(name, "").strip()
    return value or None


def load_agent_config() -> AgentConfig:
    load_dotenv()

    api_key = _optional_env("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("缺少 ANTHROPIC_API_KEY，请在环境变量或 .env 文件中配置。")

    base_url = _optional_env("ANTHROPIC_BASE_URL")
    model = _optional_env("MODEL_ID") or "claude-sonnet-4-20250514"

    return AgentConfig(
        anthropic_api_key=api_key,
        anthropic_base_url=base_url,
        model=model,
    )
