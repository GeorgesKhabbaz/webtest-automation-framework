"""
test_login.py
Test cases for the Login functionality using Pytest and Page Object Model (POM).
Includes:
- Browser fixture
- Logging
- Screenshot capture on failure
- Parametrized test data from Excel
- Pytest-html report integration
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from configfiles.config import config
from utilities.utils import setup_logger, take_screenshot, read_excel

# ----------------------------
# Fixtures
# ----------------------------
@pytest.fixture(scope="function")
def browser(request): # pylint: disable=W0613
    """Initialize browser before each test and quit after"""
    browser_type = config.get("browser", "chrome")
    if browser_type.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_type.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()

    driver.maximize_window()

    yield driver

    driver.quit()


# ----------------------------
# Pytest hook for screenshots in HTML report
# ----------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call): # pylint: disable=W0613
    """Attach screenshot to pytest-html report on test failure"""
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshot_path = take_screenshot(driver, item.name)
            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                extra = getattr(rep, "extra", [])
                from pytest_html import extras # pylint: disable=C0415
                extra.append(extras.image(screenshot_path))
                rep.extra = extra


# ----------------------------
# Load test data
# ----------------------------
excel_path = os.path.join(os.path.dirname(__file__), "..", "testdata", "test_data.xlsx")
login_data = read_excel(excel_path, "login") if os.path.exists(excel_path) else []

# ----------------------------
# Logger
# ----------------------------
logger = setup_logger("login_tests")

# ----------------------------
# Test Cases
# ----------------------------
@pytest.mark.parametrize("data", login_data)
def test_valid_login(browser, data):  # pylint: disable=W0621
    """Example test for successful login with Excel data"""
    driver = browser
    base_url = config.get("base_url", "https://example.com/login")
    driver.get(base_url)
    logger.info("Navigating to %s", base_url)

    login_page = LoginPage(driver)
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()
    logger.info("Attempted login with username: %s", data["username"])

    # Placeholder assertion using BasePage method
    success_message_locator = (By.ID, "success_id")  # update with real locator
    assert login_page.is_element_visible(success_message_locator), "Login failed!"
    logger.info("Login successful - element is visible")
