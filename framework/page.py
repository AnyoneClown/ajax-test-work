from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator: tuple):
        element = self.find_element(locator)
        element.click()
        return element

    def insert_value(self, locator: tuple, value: str):
        self.click_element(locator).send_keys(value)

    def clean_field_value(self, locator: tuple):
        self.click_element(locator).clear()
