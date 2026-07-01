import requests

BASE_URL = "https://api.github.com/users/"


def get_profile(username):
    url = BASE_URL + username
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        return response.json()

    return None


def get_repositories(username):
    url = BASE_URL + username + "/repos"

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        return response.json()

    return []