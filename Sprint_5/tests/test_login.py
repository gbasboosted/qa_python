"""Тесты входа в аккаунт через разные точки интерфейса."""

from selenium.webdriver.support import expected_conditions as conditions

from helpers import login_user
from locators import (
    ConstructorLocators,
    ForgotPasswordLocators,
    HeaderLocators,
    LoginLocators,
    RegistrationLocators,
)
from urls import BASE_URL, FORGOT_PASSWORD_URL, REGISTER_URL


def test_login_from_main_page(driver, wait, registered_user):
    driver.get(BASE_URL)
    wait.until(
        conditions.element_to_be_clickable(ConstructorLocators.LOGIN_BUTTON)
    ).click()
    wait.until(conditions.visibility_of_element_located(LoginLocators.PAGE_TITLE))

    login_user(driver, wait, registered_user)

def test_login_from_personal_account_link(driver, wait, registered_user):
    driver.get(BASE_URL)
    wait.until(
        conditions.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_LINK)
    ).click()
    wait.until(conditions.visibility_of_element_located(LoginLocators.PAGE_TITLE))

    login_user(driver, wait, registered_user)


def test_login_from_registration_form(driver, wait, registered_user):
    driver.get(REGISTER_URL)
    wait.until(
        conditions.element_to_be_clickable(RegistrationLocators.LOGIN_LINK)
    ).click()
    wait.until(conditions.visibility_of_element_located(LoginLocators.PAGE_TITLE))

    login_user(driver, wait, registered_user)


def test_login_from_forgot_password_form(driver, wait, registered_user):
    driver.get(FORGOT_PASSWORD_URL)
    wait.until(
        conditions.element_to_be_clickable(ForgotPasswordLocators.LOGIN_LINK)
    ).click()
    wait.until(conditions.visibility_of_element_located(LoginLocators.PAGE_TITLE))

    login_user(driver, wait, registered_user)
