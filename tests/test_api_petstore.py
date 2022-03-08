from db.user_data import USER_DATA, USERNAME


class TestAPIPetStore:

    def test_is_username_changed(self, api_service):
        api_service.create_user(USER_DATA)
        api_service.receive_user_data(USERNAME)
        update_user_data = USER_DATA.copy()
        update_user_data["firstName"] = "new_client_firstname"
        api_service.update_client(update_user_data, USERNAME)
        actual_user_data = api_service.receive_user_data(USERNAME)
        assert actual_user_data == update_user_data,  'User name must be changed in Database'
