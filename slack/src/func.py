from typing import Any, Union

import requests

base_url: str = "https://test-use-domain.net"


def user_add(group_id: str, user_id: str, user_name: str) -> bool:
    querystring: dict[str, str] = {
        "userId": user_id,
        "slackName": user_name,
        "groupId": group_id,
    }

    response = requests.request("POST", base_url + "/api/users", params=querystring)

    return response.json()["message"] == "ユーザー登録しました"


def get_user_name(user_id: str) -> str:
    querystring: dict[str, str] = {
        "userId": user_id,
    }

    response = requests.request("GET", base_url + "/api/users", params=querystring)

    if response.status_code == 200:
        return response.json()["slackName"]
    else:
        raise ValueError


def user_list(group_id: str) -> dict[Any, Any]:
    response = requests.request("GET", base_url + f"/api/users/{group_id}")

    d = response.json()
    print(d)
    rd: dict[Any, Any] = {}
    for i in d["users"]:
        rd[i["userId"]] = i["slackName"]
    return rd


def submit_menu(user_id: str, menu_id: int, time: int) -> bool:
    querystring: dict[str, Union[str, int]] = {
        "userId": user_id,
        "menuId": menu_id,
        "numberOfTimes": time,
    }

    payload = ""
    response = requests.request(
        "POST", f"{base_url}/api/records", data=payload, params=querystring
    )

    return response.json()  # ["message"] == "登録しました"

def ranking(group_id :str) -> str:
    return f"https://happy-liskov-330f14.netlify.app/group/{group_id}"


if __name__ == "__main__":
    print(get_user_name("catlover"))
    print(get_user_name("catlover"))
    try:
        print(get_user_name("doglover"))
    except ValueError:
        print("No user")
    print(user_list("test01"))
    print(submit_menu(user_id="catlover", menu_id=1, time=3))
