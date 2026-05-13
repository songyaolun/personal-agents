from a_share_analyst.agent import ask_a_share_analyst
from a_share_analyst.session import add_message, create_session_log_path, log_error

EXIT_COMMANDS = {"exit", "quit", "q"}


def main() -> None:
    print("A-Share Analyst 基础问答")
    print("输入问题开始分析，输入 exit / quit / q 退出。")

    messages: list[dict[str, str]] = []
    log_file = create_session_log_path()

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
