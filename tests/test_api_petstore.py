class TestAPIPetStore:
    USERNAME = 'api_client_username'
    CHANGED_CLIENTS_FIRSTNAME = 'changed_client_first_name'
    ENDPOINT = f'{USERNAME}'

    def test_is_username_changed(self, api_service):
        api_service.create_user()
        api_service.receive_user_data(self.ENDPOINT)
        api_service.change_clients_firstname(self.ENDPOINT)
        assert api_service.is_clients_firstname_had_changed(self.CHANGED_CLIENTS_FIRSTNAME, self.USERNAME), \
            'User name must be changed in Database'