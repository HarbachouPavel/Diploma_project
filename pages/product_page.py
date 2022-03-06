import allure
from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON_LOCATOR = '//button[@name="add_cart_product"]'
    QUANTITY_OF_ITEMS_LOCATOR = '//span[@class="quantity"]'

    @allure.step
    def add_to_cart(self, expected_count):
        self.click(self.ADD_TO_CART_BUTTON_LOCATOR)
        self.wait_text_to_be_present_in_element(self.QUANTITY_OF_ITEMS_LOCATOR, expected_count)
