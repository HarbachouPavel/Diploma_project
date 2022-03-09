import json
import requests
from constants.swagger_petstore_constants import BASE_URL, HEADER


class APIService:
    @staticmethod
    def create_user(data):
        response = requests.post(BASE_URL, data=json.dumps(data), headers=HEADER)
        return response.status_code

    @staticmethod
    def receive_user_data(endpoint: str):
        url = f'{BASE_URL}/{endpoint}'
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    @staticmethod
    def update_client(data, endpoint: str):
        url = f'{BASE_URL}/{endpoint}'
        response = requests.put(url, data=json.dumps(data), headers=HEADER)
        return response.status_code
