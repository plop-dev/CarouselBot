import requests
import json


def get_group_id(quiz_id: str):
    url = f"https://api.carousel-learning.com/api/open/quizzes/{quiz_id}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": "https://app.carousel-learning.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://app.carousel-learning.com/",
    }

    request = requests.get(url, headers=headers)
    response = request.json()

    group_id = response["data"]["teachingGroup"]["data"]["id"]
    return group_id


def get_token(quiz_id: str, forename: str, surname: str):
    url = "https://api.carousel-learning.com/api/auth/student/token"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Origin": "https://app.carousel-learning.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://app.carousel-learning.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "TE": "trailers",
    }

    group_id = get_group_id(quiz_id)

    body = {
        "forename": forename,
        "surname": surname,
        "teachingGroupId": group_id,
    }

    request = requests.post(url, headers=headers, data=json.dumps(body))
    response = request.json()

    try:
        token = response["token"]
        return token
    except KeyError:
        print("Error token key not found: ", response)
        return None
