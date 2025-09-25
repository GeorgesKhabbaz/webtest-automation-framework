"""
functions.py
Reusable project-specific functions to avoid repeating flows in testcases.
Examples:
- login_user
- submit_form
- search_item
"""

from pages.login_page import LoginPage

def login_user(driver, username: str, password: str):
    """
    Reusable function to perform login.
    Keeps testcases clean by avoiding repeated steps.
    """
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    return login_page
