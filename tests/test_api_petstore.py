from api.user_data import USER_DATA, USERNAME
import allure


class TestAPIPetStore:

    def test_is_username_changed(self, api_service):
        with allure.step('create user with api request'):
            api_service.create_user(USER_DATA)
        with allure.step('receive user data from database'):
            api_service.receive_user_data(USERNAME)
        update_user_data = USER_DATA.copy()
        update_user_data["firstName"] = "new_client_firstname"
        with allure.step('update user data with api request'):
            api_service.update_client(update_user_data, USERNAME)
        actual_user_data = api_service.receive_user_data(USERNAME)
        with allure.step('checking is data have been updated in database'):
            assert actual_user_data == update_user_data,  'User name must be changed in Database'
