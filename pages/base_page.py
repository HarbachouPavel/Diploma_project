from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # CSS : div[href="https://123]
    # XPATH: .//div
    # XPATH (//div)

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def enter_text(self, locator, text):
        element = self._wait_presence_of_element_located(locator)
        element.send_keys(text)

    def click(self, locator):
        element = self._wait_presence_of_element_located(locator)
        element.click()

    def _find_element(self, locator):
        element = self._wait_presence_of_element_located(locator)
        return element

    def clear_input_line(self, locator):
        self._wait_presence_of_element_located(locator)
        element = self._find_element(locator)
        element.clear()

    def full_screen(self):
        self.driver.maximize_window()

    def return_text_of_element(self, locator):
        self._wait_presence_of_element_located(locator)
        element = self._find_element(locator)
        return element.text

    def _wait_presence_of_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))

    # Check if locator type required in progress
    def wait_text_to_be_present_in_element(self, locator, text):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element
                                                    ((By.XPATH, locator), text_=text))

    def is_element_present(self, locator):
        return len(self.driver.find_elements(By.XPATH, locator)) > 0
