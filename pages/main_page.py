from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    color_of_duck = 'Green'
    URL = 'http://localhost/litecart/en/'
    ENTER_USERNAME_LOCATOR = '//input[@name="email"]'
    ENTER_PASSWORD_LOCATOR = '//input[@name="password"]'
    LOGIN_BUTTON_LOCATOR = '//button[@type="submit" and @name="login"]'
    EDIT_ACCOUNT_LOCATOR = '//a[@href="http://localhost/litecart/en/edit_account"]'
    GREEN_DUCK_LOCATOR = f'//img[@alt="{color_of_duck} Duck"]'
    TO_CART_LOCATOR = '//a[@href="http://localhost/litecart/en/checkout" and @class="link"]'

    def open_page(self):
        self.open_url(self.URL)
        self.full_screen()

    def enter_username(self, username):
        self.enter_text(self.ENTER_USERNAME_LOCATOR, username)

    def enter_password(self, password):
        self.enter_text(self.ENTER_PASSWORD_LOCATOR, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON_LOCATOR)

    @allure.step
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    @allure.step
    def edit_account(self):
        self.click(self.EDIT_ACCOUNT_LOCATOR)

    @allure.step
    def click_on_item(self):
        self.click(self.GREEN_DUCK_LOCATOR)

    @allure.step
    def click_on_cart(self):
        self.click(self.TO_CART_LOCATOR)
