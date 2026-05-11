import asyncio

from a_share_analyst.agent import ask_a_share_analyst

EXIT_COMMANDS = {"exit", "quit", "q"}


async def run() -> None:
    print("A-Share Analyst 基础问答")
    print("输入问题开始分析，输入 exit / quit / q 退出。")

    while True:
        question = await asyncio.to_thread(input, "\n你：")
        normalized_question = question.strip()

        if normalized_question.lower() in EXIT_COMMANDS:
            return

        answer = await ask_a_share_analyst(normalized_question)
        print(f"\nA-Share Analyst：\n{answer}")


def main() -> None:
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\n已退出。")

