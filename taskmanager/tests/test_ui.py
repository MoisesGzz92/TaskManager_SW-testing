# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

# tests/test_frontend.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def setup_browser():
    """Set up the Chrome WebDriver."""
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # initiliaze firefox driver
    # driver = webdriver.Firefox(service=FirefoxService(FirefoxDriverManager().install()))
    # Yield the driver to the test function
    yield driver
    # Teardown
    driver.quit()


def test_homepage_title(setup_browser):
    """Test that the homepage title is correct."""
    driver = setup_browser
    driver.get("http://localhost:8080")  # URL of the Vue.js application
    assert driver.title == "TaskManager - Manage Your Tasks"  # Expected title of the page


def test_add_task(setup_browser):
    """Test adding a task."""
    driver = setup_browser
    driver.get("http://localhost:8080")  # Change to your frontend URL

    # Find the input field and button to add a task
    input_field = driver.find_element(By.ID, "create-task-btn")  # Adjust the ID as necessary

    # Add a task
    input_field.click()
