import datetime
import traceback
from pathlib import Path

from a_share_analyst.agent import ask_a_share_analyst

EXIT_COMMANDS = {"exit", "quit", "q"}


def _session_log_path() -> Path:
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


def main() -> None:
    print("A-Share Analyst 基础问答")
    print("输入问题开始分析，输入 exit / quit / q 退出。")

    messages: list[dict[str, str]] = []
    log_file = _session_log_path()

    while True:
        question = input("\n >>input：")
        normalized_question = question.strip()

        if normalized_question.lower() in EXIT_COMMANDS:
            return
        add_message(messages, "user", normalized_question, log_file)

        try:
            print("\nA-Share Analyst：")
            chunks = []
            for chunk in ask_a_share_analyst(messages):
                print(chunk, end="", flush=True)
                chunks.append(chunk)
            print()
            answer = "".join(chunks)
        except Exception as e:
            log_error(e, log_file)
            print(f"\n发生错误：{e}")
            continue
        add_message(messages, "assistant", answer, log_file)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n已退出。")
