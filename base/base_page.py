"""
Contains the BasePage class with common Selenium actions.
All page objects will inherit from this class to avoid code duplication.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """
    Base class for all page objects. Provides reusable Selenium methods.
    """

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        """
        Wait for an element to be present and return it.
        :param locator: Tuple (By, locator_string)
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Element not found: {locator}")
            return None

    def click(self, locator):
        """
        Wait for an element to be clickable and click it.
        """
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def send_keys(self, locator, text):
        """
        Wait for an element and send keys.
        """
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        """
        Return text of an element.
        """
        element = self.find_element(locator)
        if element:
            return element.text
        return ""

    def is_element_visible(self, locator):
        """
        Check if element is visible. Returns the element if visible, else False.
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False
