import requests


def complete_revision(quiz_id: str, token: str):
    url = f"https://api.carousel-learning.com/api/student/quizzes/{quiz_id}/questions/revision"

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

    try:
        _ = response["data"]["questions"]
    except KeyError:
        print("Error token key not found: ", response)
        return None

    revision_id = response["data"]["revision"]["id"]
    all_valid = True

    for question in response["data"]["questions"]:
        question_url = (
            f"https://api.carousel-learning.com/api/student/revisions/{revision_id}"
        )

        question_body = {
            "questionId": question["id"],
            "feedback": "right",
        }
        questions_response = requests.post(
            question_url, headers=headers, json=question_body
        )
        if questions_response.status_code != 200:
            all_valid = False
            print("Error in question response: ", questions_response.json())

    return all_valid
