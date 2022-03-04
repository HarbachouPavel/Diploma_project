LOGIN = 'client@gmail.com'
PASSWORD = 'Password'


class Test:
    CHANGED_FIRST_NAME = 'changed_client_first_name'
    SELECT_QUERY = 'SELECT firstname FROM lc_customers WHERE email = "client@gmail.com"'

    def test_change_username(self, main_page, edit_account_page, setup_sql_service):
        main_page.login(LOGIN, PASSWORD)
        main_page.edit_account()
        edit_account_page.change_first_name(self.CHANGED_FIRST_NAME)
        client_first_name_from_database = setup_sql_service.sql_query(self.SELECT_QUERY)
        assert edit_account_page.search_for_changed_name_in_list(client_first_name_from_database,
                                                                 self.CHANGED_FIRST_NAME), \
            f'User name must be changed to {self.CHANGED_FIRST_NAME}'

    def test_is_price_valid_of_any_items(self, main_page, product_page, cart_page):
        main_page.click_on_duck()
        product_page.add_to_cart('1')
        main_page.click_on_cart()
        cart_page.change_quantity_of_item(3)
        cart_page.click_update_button()
        # soft assert in progress
        assert cart_page.is_total_price_price_valid(3, '$60.00'), f'Price of 3 items must be valid'
        cart_page.delete_item_from_cart()
        assert not cart_page.is_cart_empty('There are no items in your cart.'), 'Cart must be empty'

    # test in progress
    def test_is_username_changed(self, api_service):
        api_service.create_user()
        api_service.receive_user_data()
        api_service.change_user_name("changed_client_username")
        assert api_service.is_user_name_had_changed("changed_client_username"), \
            'User name must be changed in Database'
