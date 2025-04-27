import gettoken
import getanswers
import re
from rich.console import Console
from rich.padding import Padding
import dotenv
import os
import argparse

dotenv.load_dotenv()

global console
console = Console()

INFO = os.getenv("INFO")
SUCCESS = os.getenv("SUCCESS")

FORENAME = os.getenv("FORENAME")
SURNAME = os.getenv("SURNAME")


def get_quiz_id(link):
    pattern = r"[a-f0-9\-]{20,50}"
    match = re.search(pattern, link)

    if match:
        return match.group(0)
    return "No match found"


def main():
    parser = argparse.ArgumentParser(description="CarouselBot - Quiz Answer Fetcher")
    parser.add_argument("link", help="Quiz link")
    args = parser.parse_args()

    link = args.link

    console.print("[*] Starting the script...", style=INFO)

    console.print("[*] Getting the quiz ID...", style=INFO)
    quiz_id = get_quiz_id(link)
    console.print(f"[+] Quiz ID: {quiz_id}", style=SUCCESS)

    console.print("[*] Getting the token...", style=INFO)
    token = gettoken.get_token(quiz_id, FORENAME, SURNAME)
    console.print(f"[+] Token: {token}", style=SUCCESS)

    console.print("[*] Getting the answers...", style=INFO)
    answers = getanswers.get_answers(quiz_id, token)
    console.print(f"[+] Answers: {len(answers)}", style=SUCCESS)

    for i in range(len(answers)):
        console.print(
            Padding(
                f"[u][{INFO}]Question {i + 1}[/]:[/]\n{answers[i]['question']}\n",
                (0, 2),
            )
        )
        console.print(
            Padding(f"[u][{SUCCESS}]Answer[/]:[/]\n{answers[i]['answer']}", (0, 2))
        )

        if i + 1 != len(answers):
            console.rule()


if __name__ == "__main__":
    main()
