import requests


def get_answers(quiz_id: str, token: str):
    url = (
        f"https://api.carousel-learning.com/api/student/quizzes/{quiz_id}/attempts/last"
    )

    headers = {
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "dnt": "1",
        "origin": "https://app.carousel-learning.com",
        "priority": "u=1, i",
        "referer": "https://app.carousel-learning.com/",
        "Authorization": f"Bearer {token}",
    }

    request = requests.get(url, headers=headers)
    response = request.json()

    # Example question:
    # {
    #     "id": "45176a43-6479-47f4-a17d-bf9050fa1b5c",
    #     "number": 1,
    #     "answerType": "free-text",
    #     "question": "A list contains the following items: \n(a) A binary search is performed to find the item Okapi. State the items which will be examined. [3]",
    #     "perfectAnswer": "Giraffe, Lion, Okapi.",
    #     "wrongAnswers": [],
    #     "topic": "Computer Science",
    #     "picture": "462871f8-59ac-4ef2-a617-2256a91643ed.png",
    #     "credit": null,
    #     "creditUrl": null
    # },

    try:
        _ = response["data"]["quiz"]["data"]["questions"]["data"]
    except KeyError:
        print("Error token key not found: ", response)
        return None

    answers = []
    for question in response["data"]["quiz"]["data"]["questions"]["data"]:
        answers.append(
            {
                "question": question["question"],
                "answer": question["perfectAnswer"],
            }
        )

    return answers
