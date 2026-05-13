import datetime
import traceback
from pathlib import Path


def create_session_log_path() -> Path:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return log_dir / f"session_{timestamp}.log"


def _now() -> str:
    return datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")


def add_message(messages: list[dict[str, str]], role: str, content: str, log_file: Path) -> None:
    messages.append({"role": role, "content": content})
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{_now()}] [{role}]\n{content}\n{'─' * 60}\n")


def log_error(error: Exception, log_file: Path) -> None:
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{_now()}] [error] {type(error).__name__}: {error}\n{traceback.format_exc()}\n\n")
