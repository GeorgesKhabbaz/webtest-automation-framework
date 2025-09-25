"""
test_login.py
Contains test cases for the Login functionality using Pytest and Page Object Model.
"""

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from configfiles.config import config  # if you store URLs, browser type, etc.

@pytest.fixture(scope="function")
def browser():
    """Initialize browser and quit after test"""
    browser_type = config.get("browser", "chrome")  # default to Chrome
    if browser_type.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_type.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()

    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(browser): # pylint: disable=W0621
    """Example test for successful login"""
    driver = browser
    driver.get(config.get("base_url", "https://example.com/login"))  # placeholder URL

    login_page = LoginPage(driver)
    login_page.enter_username("test_user")      # placeholder username
    login_page.enter_password("password123")    # placeholder password
    login_page.click_login()

    # Example: assert some element visible after login
    # success_message_locator = (By.ID, "success_id")
    # assert login_page.is_element_visible(success_message_locator)
    print("Login test executed - update assertions with real locators")
