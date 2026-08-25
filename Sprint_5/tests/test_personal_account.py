"""Тесты личного кабинета, навигации и выхода."""

import pytest
from selenium.webdriver.support import expected_conditions as conditions

from locators import AccountLocators, ConstructorLocators, HeaderLocators, LoginLocators
from urls import BASE_URL, LOGIN_URL


def test_personal_account_link_opens_profile(driver, wait, signed_in_user):
    wait.until(
        conditions.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_LINK)
    ).click()

    wait.until(conditions.url_contains("/account/profile"))
    name_input = wait.until(
        conditions.visibility_of_element_located(AccountLocators.NAME_INPUT)
    )
    assert name_input.get_attribute("value") == signed_in_user["name"]


@pytest.mark.parametrize(
    "navigation_locator",
    [HeaderLocators.CONSTRUCTOR_LINK, HeaderLocators.LOGO_LINK],
    ids=["constructor-link", "stellar-burgers-logo"],
)
def test_navigation_from_account_to_constructor(
    driver,
    wait,
    signed_in_user,
    navigation_locator,
):
    wait.until(
        conditions.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_LINK)
    ).click()
    wait.until(conditions.url_contains("/account/profile"))

    wait.until(conditions.element_to_be_clickable(navigation_locator)).click()

    wait.until(conditions.url_to_be(f"{BASE_URL}/"))
    assert wait.until(
        conditions.visibility_of_element_located(ConstructorLocators.PAGE_TITLE)
    )


def test_logout_from_personal_account(driver, wait, signed_in_user):
    wait.until(
        conditions.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_LINK)
    ).click()
    wait.until(conditions.url_contains("/account/profile"))

    wait.until(
        conditions.element_to_be_clickable(AccountLocators.LOGOUT_BUTTON)
    ).click()

    wait.until(conditions.url_to_be(LOGIN_URL))
    assert wait.until(conditions.visibility_of_element_located(LoginLocators.PAGE_TITLE))
