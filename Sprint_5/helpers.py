"""Повторно используемые действия в Selenium-тестах."""

from selenium.webdriver.support import expected_conditions as conditions

from locators import ConstructorLocators, LoginLocators
from urls import BASE_URL, LOGIN_URL


def login_user(driver, wait, user: dict[str, str]) -> None:
    """Войти через открытую форму авторизации и дождаться конструктора."""
    wait.until(conditions.visibility_of_element_located(LoginLocators.PAGE_TITLE))
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(user["email"])
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(user["password"])
    driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

    wait.until(conditions.url_to_be(f"{BASE_URL}/"))
    wait.until(conditions.visibility_of_element_located(ConstructorLocators.PAGE_TITLE))


def open_login_page(driver, wait) -> None:
    """Открыть форму входа напрямую и дождаться её появления."""
    driver.get(LOGIN_URL)
    wait.until(conditions.visibility_of_element_located(LoginLocators.PAGE_TITLE))
