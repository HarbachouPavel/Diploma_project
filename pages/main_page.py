from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    URL = 'http://localhost/litecart/en/'
    ENTER_USERNAME_LOCATOR = '//input[@name="email"]'
    ENTER_PASSWORD_LOCATOR = '//input[@name="password"]'
    LOGIN_BUTTON_LOCATOR = '//button[@type="submit" and @name="login"]'
    EDIT_ACCOUNT_LOCATOR = '//a[contains(@href,"edit_account")]'
    GREEN_DUCK_LOCATOR = '//img[@alt="{} Duck"]'
    TO_CART_LOCATOR = '//a[contains(@href,"checkout") and @class="link"]'

    def open_page(self):
        self.open_url(self.URL)

    def enter_username(self, username: str):
        self.enter_text(self.ENTER_USERNAME_LOCATOR, username)

    def enter_password(self, password: str):
        self.enter_text(self.ENTER_PASSWORD_LOCATOR, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON_LOCATOR)

    @allure.step('login')
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def edit_account(self):
        self.click(self.EDIT_ACCOUNT_LOCATOR)

    @allure.step('go to item page')
    def click_on_item(self, color="Green"):
        self.click(self.GREEN_DUCK_LOCATOR.format(color))

    @allure.step('go to cart page')
    def click_on_cart(self):
        self.click(self.TO_CART_LOCATOR)
