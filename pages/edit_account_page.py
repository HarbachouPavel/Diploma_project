import allure
from pages.base_page import BasePage


class EditAccountPage(BasePage):
    USER_FIRST_NAME_FIELD_LOCATOR = '//input[@name="firstname"]'
    SAVE_BUTTON_LOCATOR = '//button[@name="save"]'

    def write_first_name(self, changed_first_name):
        self.enter_text(self.USER_FIRST_NAME_FIELD_LOCATOR, changed_first_name)

    def click_save_button(self):
        self.click(self.SAVE_BUTTON_LOCATOR)

    @allure.step('change_first_name')
    def change_first_name(self, changed_first_name: str):
        self.clear_input_line(self.USER_FIRST_NAME_FIELD_LOCATOR)
        self.write_first_name(changed_first_name)
        self.click_save_button()
