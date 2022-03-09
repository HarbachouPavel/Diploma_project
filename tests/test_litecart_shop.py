import allure
import pytest
from constants.litecart_constants import LOGIN, PASSWORD
from sql_service.querries import select_query


@pytest.mark.usefixtures('do_screenshot_in_end_of_test')
@pytest.mark.usefixtures('main_page_navigate')
class TestLiteCartShop:

    def test_change_username(self, main_page, edit_account_page, setup_sql_service):
        changed_first_name = 'changed_client_first_name'

        main_page.login(LOGIN, PASSWORD)
        main_page.edit_account()
        edit_account_page.change_first_name(changed_first_name)
        client_first_name_from_database = setup_sql_service.execute_select_query(select_query)[0][0]
        with allure.step('checking is name changed in  database'):
            assert client_first_name_from_database == changed_first_name,\
                "Client first name must be changed in database"

    def test_is_price_valid_of_any_items(self, main_page, product_page, cart_page):
        quantity_of_items = 3
        expected_count_of_items = '1'
        total_price = '$60.00'

        main_page.click_on_item()
        product_page.add_to_cart(expected_count_of_items)
        main_page.click_on_cart()
        cart_page.change_quantity_of_item(quantity_of_items)
        with allure.step('check is total price correct'):
            assert cart_page.is_total_price_correct(quantity_of_items, total_price), \
                f'Price of 3 items must be valid'
        cart_page.delete_item_from_cart()
        with allure.step('check is cart empty'):
            assert not cart_page.is_cart_empty(), 'Cart must be empty'
