import re
import allure
from pages.base_page import BasePage


class CartPage(BasePage):
    INPUT_QUANTITY_OF_ITEMS_LOCATOR = '//input[@name="quantity"]'
    UPDATE_BUTTON_LOCATOR = '//button[@name="update_cart_item"]'
    TOTAL_COST_LOCATOR = '//td[@class="sum"]'
    COST_OF_ONE_ELEMENT_LOCATOR = '//p[contains(@style,"margin-top")]/following-sibling::*[1]'
    REMOVE_BUTTON_LOCATOR = '//button[@name="remove_cart_item"]'
    EMPTY_CART_LOCATOR = '//div[@id="checkout-cart-wrapper"]'
    ITEM_IN_CART_LOCATOR = '//a[@class="image-wrapper shadow"]'
    TOTAL_PRICE_LOCATOR = '//td[@class="sum"]'

    def _send_new_quantity_in_quantity_field(self, new_quantity):
        self.clear_input_line(self.INPUT_QUANTITY_OF_ITEMS_LOCATOR)
        self.enter_text(self.INPUT_QUANTITY_OF_ITEMS_LOCATOR, new_quantity)

    def _click_update_button(self):
        self.click(self.UPDATE_BUTTON_LOCATOR)

    def _receive_total_price(self):
        total_price_with_special_symbol = self.return_text_of_element(self.TOTAL_COST_LOCATOR)
        regex_num = re.compile('\d+.\d+')
        total_price = regex_num.findall(total_price_with_special_symbol)[0]
        return total_price

    def _receive_check_of_one_element(self):
        price_of_one_element_with_special_symbol = self.return_text_of_element(self.COST_OF_ONE_ELEMENT_LOCATOR)
        regex_num = re.compile('\d+')
        price_of_one_element = regex_num.findall(price_of_one_element_with_special_symbol)[0]
        return price_of_one_element

    @allure.step('check_is_total_price_valid')
    def is_total_price_valid(self, number_of_items: int, text):
        one_element_price = int(self._receive_check_of_one_element())
        self.wait_text_to_be_present_in_element(self.TOTAL_PRICE_LOCATOR,
                                                text)
        actual_total_price = float(self._receive_total_price())
        expected_total_price = one_element_price * number_of_items
        return expected_total_price == actual_total_price

    @allure.step('delete_item_from_cart')
    def delete_item_from_cart(self):
        self.click(self.REMOVE_BUTTON_LOCATOR)

    @allure.step('check_is_cart_empty')
    def is_cart_empty(self):
        return self.is_element_present(self.REMOVE_BUTTON_LOCATOR)

    @allure.step('change_quantity_of_item')
    def change_quantity_of_item(self, new_quantity):
        self._send_new_quantity_in_quantity_field(new_quantity)
        self._click_update_button()
