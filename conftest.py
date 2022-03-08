import allure
import mysql.connector
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_page import CartPage
from pages.edit_account_page import EditAccountPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from api.api_service import APIService
from db.sql_service import SQLService


@pytest.fixture()
def chromedriver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.close()


@pytest.fixture()
def main_page(chromedriver):
    return MainPage(chromedriver)


@pytest.fixture()
def edit_account_page(chromedriver):
    return EditAccountPage(chromedriver)


@pytest.fixture()
def main_page_navigate(main_page):
    main_page.open_page()


@pytest.fixture(scope='session')
def setup_sql_service():
    connection = mysql.connector.connect(
        database='litecart',
        host='127.0.0.1',
        user='root',
        password=''
    )
    yield SQLService(connection)
    connection.close()


@pytest.fixture()
def product_page(chromedriver):
    return ProductPage(chromedriver)


@pytest.fixture()
def cart_page(chromedriver):
    return CartPage(chromedriver)


@pytest.fixture()
def api_service():
    return APIService()


@pytest.fixture(autouse=True)
def do_screenshot_in_end_of_test(request, chromedriver):
    yield
    screenshot_name = f"{request.node.name}.png"
    chromedriver.save_screenshot(screenshot_name)
    allure.attach.file(screenshot_name, attachment_type=allure.attachment_type.PNG)
