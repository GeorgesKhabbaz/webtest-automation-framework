"""
conftest.py
Central configuration file for pytest.
Contains:
- Browser fixture initialization (Chrome/Firefox/Edge)
- Teardown with screenshot capture
- Hooks for attaching test results to reports
"""

import pytest
from selenium import webdriver
from utilities.utils import setup_logger, take_screenshot
from configfiles.config import config

logger = setup_logger("conftest")

@pytest.fixture(scope="function")
def browser(request):
    """Fixture to initialize and quit the browser before/after each test"""
    browser_type = config.get("browser", "chrome")

    if browser_type.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_type.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()

    driver.maximize_window()
    logger.info("Browser launched: %s", browser_type)

    yield driver

    # Screenshot on failure
    if request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_path = take_screenshot(driver, test_name)
        logger.error("Test failed: %s. Screenshot saved: %s", test_name, screenshot_path)

        # Attach to pytest-html report if available
        if hasattr(request.node.config, "_html"):
            extra = getattr(request.node.config, "_html").extras
            extra.append(request.node.config._html.extras.image(screenshot_path)) # pylint: disable=W0212

    driver.quit()
    logger.info("Browser closed.")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call): # pylint: disable=W0613
    """
    Hook to detect test status (pass/fail).
    Adds report object to each test item for use in fixtures.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
