import json
import requests


class APIService:
    BASE_URL = 'https://petstore.swagger.io/v2/user'
    USERNAME = 'api_client_username'
    CLIENTS_FIRSTNAME = 'client_first_name'
    CHANGED_CLIENTS_FIRSTNAME = 'changed_client_first_name'
    USER_DATA = {
        "id": 10,
        "username": f"{USERNAME}",
        "firstName": f"{CLIENTS_FIRSTNAME}",
        "lastName": "client_last_name",
        "email": "client_email@gmail.com",
        "password": "Password123",
        "phone": "+375178802378",
        "userStatus": 1
    }
    CHANGED_USER_DATA = {
        "id": 10,
        "username": f"{USERNAME}",
        "firstName": f"{CHANGED_CLIENTS_FIRSTNAME}",
        "lastName": "client_last_name",
        "email": "client_email@gmail.com",
        "password": "Password123",
        "phone": "+375178802378",
        "userStatus": 1
    }
    HEADER = {'Content-Type': 'application/json'}

    def create_user(self):
        response = requests.post(self.BASE_URL, data=json.dumps(self.USER_DATA),
                                 headers=self.HEADER)
        return response.status_code

    def receive_user_data(self, endpoint):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    def change_clients_firstname(self, endpoint):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.put(url, data=json.dumps(self.CHANGED_USER_DATA), headers=self.HEADER)
        return response.status_code

    def is_clients_firstname_had_changed(self, clients_firstname, endpoint):
        changed_user_data = self.receive_user_data(endpoint)
        if clients_firstname == changed_user_data['firstName']:
            return True
        else:
            return False
