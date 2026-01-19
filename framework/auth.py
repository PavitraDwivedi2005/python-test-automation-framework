import requests


def login(base_url, login_endpoint, username, password):
    url = base_url + login_endpoint
    response = requests.post(url, auth=(username, password))
    response.raise_for_status()
    return response.json()["token"]
