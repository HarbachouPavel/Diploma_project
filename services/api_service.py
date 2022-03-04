import json
import requests

# This service in development


class APIService:
    URL = 'http://localhost/litecart/en/'
    username = 'client_username'
    changed_username = 'changed_client_username'
    USER_DATA = {
        "id": 1,
        "username": f"{username}",
        "firstName": "client_firstname",
        "lastName": "client_lastname",
        "email": "client@gmail.com",
        "password": "Password",
        "phone": "+375111111111",
        "userStatus": 1
    }
    CHANGED_USER_DATA = {
        "id": 1,
        "username": f"{changed_username}",
        "firstName": "client_firstname",
        "lastName": "client_lastname",
        "email": "client@gmail.com",
        "password": "Password",
        "phone": "+375111111111",
        "userStatus": 1
    }

    def create_user(self):
        response = requests.post(self.URL, data=self.USER_DATA)
        return response.status_code

    def receive_user_data(self):
        response = requests.get(self.URL, self.username)
        return response.json()

    def change_user_name(self):
        response = requests.put(self.URL, data=self.CHANGED_USER_DATA)
        return response.status_code

    def is_user_name_had_changed(self, name):
        changed_user_data = self.receive_user_data()
        if name in changed_user_data:
            return True
        else:
            return False
