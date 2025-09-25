"""
utils.py
Contains helper functions and utilities used across the framework.
Centralizes reusable code to avoid duplication and improve maintainability.
"""

import logging
import os
from datetime import datetime
from openpyxl import load_workbook

# ----------------------------
# Logger setup
# ----------------------------
def setup_logger(name="framework_logger", log_level=logging.INFO):
    """
    Creates and configures a logger.
    
    Args:
        name (str): Name of the logger
        log_level (int): Logging level (default: INFO)
    
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent duplicate handlers if called multiple times
    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger

# Example usage:
# logger = setup_logger()
# logger.info("Framework started")

# ----------------------------
# Screenshot capture
# ----------------------------
def take_screenshot(driver, file_name="screenshot"):
    """
    Captures a screenshot of the current browser window.
    
    Args:
        driver (WebDriver): Selenium WebDriver instance
        file_name (str): Base name for the screenshot file
    
    Returns:
        str: Full path to the saved screenshot
    """
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join("screenshots", f"{file_name}_{timestamp}.png")
    driver.save_screenshot(path)
    return path

# ----------------------------
# Excel utilities
# ----------------------------
def read_excel(file_path, sheet_name):
    """
    Reads data from an Excel file (.xlsx) and returns it as a list of dictionaries.
    
    Args:
        file_path (str): Path to the Excel file
        sheet_name (str): Name of the sheet to read
    
    Returns:
        list[dict]: List of rows with column headers as keys
    """
    workbook = load_workbook(filename=file_path)
    sheet = workbook[sheet_name]
    data = []
    headers = [cell.value for cell in sheet[1]]  # First row = headers

    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(dict(zip(headers, row)))
    return data

# Example usage:
# test_data = read_excel("testdata/test_data.xlsx", "login")
# print(test_data)

# ----------------------------
# File / folder utilities
# ----------------------------
def ensure_folder_exists(folder_path):
    """
    Creates a folder if it does not exist.
    
    Args:
        folder_path (str): Path to the folder
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Example usage:
# ensure_folder_exists("reports")
