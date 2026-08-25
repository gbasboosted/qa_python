"""Общие фикстуры Selenium-проекта."""

import json
import os
import ssl
from urllib.request import Request, urlopen

import certifi
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from generators import generate_user
from helpers import login_user, open_login_page
from urls import API_REGISTER_URL


@pytest.fixture
def driver():
    """Открыть отдельный браузер для теста и гарантированно закрыть его."""
    browser_name = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS", "1") != "0"

    if browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        web_driver = webdriver.Firefox(options=options)
    elif browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,1000")
        options.add_argument("--disable-dev-shm-usage")
        web_driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("BROWSER должен иметь значение 'chrome' или 'firefox'")

    yield web_driver
    web_driver.quit()


@pytest.fixture
def wait(driver):
    """Предоставить явное ожидание для текущего браузера."""
    return WebDriverWait(driver, 15)


@pytest.fixture
def registered_user() -> dict[str, str]:
    """Создать через API уникального пользователя для независимого теста входа."""
    user = generate_user()
    request = Request(
        API_REGISTER_URL,
        data=json.dumps(user).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    with urlopen(request, timeout=15, context=ssl_context) as response:
        response_data = json.loads(response.read().decode("utf-8"))

    assert response_data.get("success") is True
    return user


@pytest.fixture
def signed_in_user(driver, wait, registered_user) -> dict[str, str]:
    """Авторизовать уникального пользователя перед тестом личного кабинета."""
    open_login_page(driver, wait)
    login_user(driver, wait, registered_user)
    return registered_user
