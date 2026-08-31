"""Общие фикстуры Selenium для UI-тестов."""

import os
from pathlib import Path

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver(request):
    options = Options()
    firefox_binary = os.getenv("FIREFOX_BINARY")
    macos_firefox = Path("/Applications/Firefox.app/Contents/MacOS/firefox")
    if firefox_binary:
        options.binary_location = firefox_binary
    elif macos_firefox.exists():
        options.binary_location = str(macos_firefox)
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("-headless")

    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1440, 1000)
    yield browser

    try:
        if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="failure-state",
                attachment_type=allure.attachment_type.PNG,
            )
    finally:
        browser.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
