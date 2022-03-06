import pytest

LOGIN = 'client@gmail.com'
PASSWORD = 'Password'


@pytest.mark.usefixtures('main_page_navigate')
class TestLitecartShop:
    CHANGED_FIRST_NAME = 'changed_client_first_name'
    SELECT_QUERY = 'SELECT firstname FROM lc_customers WHERE email = "client@gmail.com"'
    TOTAL_PRICE = '$60.00'
    QUANTITY_OF_ITEMS = 2
    EXPECTED_COUNT_OF_ITEMS = '1'

    def test_change_username(self, main_page, edit_account_page, setup_sql_service):
        main_page.login(LOGIN, PASSWORD)
        main_page.edit_account()
        edit_account_page.change_first_name(self.CHANGED_FIRST_NAME)
        client_first_name_from_database = setup_sql_service.sql_query(self.SELECT_QUERY)
        assert edit_account_page.search_for_changed_name_in_list(client_first_name_from_database,
                                                                 self.CHANGED_FIRST_NAME), \
            f'User name must be changed to {self.CHANGED_FIRST_NAME}'

    def test_is_price_valid_of_any_items(self, main_page, product_page, cart_page):
        main_page.click_on_item()
        product_page.add_to_cart(self.EXPECTED_COUNT_OF_ITEMS)
        main_page.click_on_cart()
        cart_page.change_quantity_of_item(self.QUANTITY_OF_ITEMS)
        assert cart_page.is_total_price_price_valid(self.QUANTITY_OF_ITEMS, self.TOTAL_PRICE),\
            f'Price of 3 items must be valid'
        cart_page.delete_item_from_cart()
        assert not cart_page.is_cart_empty('There are no items in your cart.'), 'Cart must be empty'
