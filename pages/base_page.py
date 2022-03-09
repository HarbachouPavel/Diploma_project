from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url: str):
        self.driver.get(url)

    def enter_text(self, locator: str, text):
        element = self._wait_presence_of_element_located(locator)
        element.send_keys(text)

    def click(self, locator: str):
        element = self._wait_presence_of_element_located(locator)
        element.click()

    def _find_element(self, locator: str):
        element = self._wait_presence_of_element_located(locator)
        return element

    def clear_input_line(self, locator: str):
        element = self._wait_presence_of_element_located(locator)
        element.clear()

    def maximize_window(self):
        self.driver.maximize_window()

    def return_text_of_element(self, locator: str):
        element = self._wait_presence_of_element_located(locator)
        return element.text

    def _wait_presence_of_element_located(self, locator: str):
        locator_type = self._define_type_of_locator(locator)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator_type, locator)))

    def wait_text_to_be_present_in_element(self, locator: str, text: str):
        locator_type = self._define_type_of_locator(locator)
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element
                                                    ((locator_type, locator), text_=text))

    def is_element_present(self, locator: str):
        locator_type = self._define_type_of_locator(locator)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((locator_type, locator)))
        return len(self.driver.find_elements(locator_type, locator)) > 0

    @staticmethod
    def _define_type_of_locator(locator: str):
        if '//' in locator:
            return By.XPATH
        else:
            return By.CSS_SELECTOR
