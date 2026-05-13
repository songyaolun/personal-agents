from a_share_analyst.agent import ask_a_share_analyst

EXIT_COMMANDS = {"exit", "quit", "q"}


def main() -> None:
    print("A-Share Analyst 基础问答")
    print("输入问题开始分析，输入 exit / quit / q 退出。")

    messages: list[dict[str, str]] = []

    while True:
        question = input("\n >>input：")
        normalized_question = question.strip()

        if normalized_question.lower() in EXIT_COMMANDS:
            return
        messages.append({"role": "user", "content": normalized_question})

        answer = ask_a_share_analyst(messages)
        messages.append({"role": "assistant", "content": answer})
        print(f"\nA-Share Analyst：\n{answer}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n已退出。")
