from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def find_element(self, locator: tuple, timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator: tuple) -> WebElement:
        element: WebElement = self.find_element(locator)
        element.click()
        return element

    def insert_value(self, locator: tuple, value: str) -> None:
        self.click_element(locator).send_keys(value)

    def clean_field_value(self, locator: tuple) -> None:
        self.click_element(locator).clear()
