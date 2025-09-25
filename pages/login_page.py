"""
login_page.py
Page Object Model for the Login Page.
Contains locators and methods to interact with the login page.
"""

from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    """
    LoginPage inherits from BasePage and provides login-related actions.
    """

    # Locators (replace placeholders with actual locators)
    USERNAME_INPUT = (By.ID, "username_input_id")   # Replace with actual locator
    PASSWORD_INPUT = (By.ID, "password_input_id")   # Replace with actual locator
    LOGIN_BUTTON   = (By.ID, "login_button_id")     # Replace with actual locator
    ERROR_MESSAGE  = (By.ID, "error_message_id")    # Replace with actual locator

    def enter_username(self, username: str):
        """Enter username into the username field"""
        self.send_keys(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """Enter password into the password field"""
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the login button"""
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Return login error message text"""
        return self.get_text(self.ERROR_MESSAGE)
