import requests

class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def get(self, endpoint):
        url = self.base_url + endpoint
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, payload):
        url = self.base_url + endpoint
        response = requests.put(url, json=payload, headers=self._headers())
        response.raise_for_status()
        return response.json()
