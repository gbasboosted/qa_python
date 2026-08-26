"""Тесты разделов конструктора ингредиентов."""

import pytest
from selenium.webdriver.support import expected_conditions as conditions

from locators import ConstructorLocators
from urls import BASE_URL


class TestConstructor:
    @pytest.mark.parametrize(
        "tab_locator",
        [
            ConstructorLocators.BUNS_TAB,
            ConstructorLocators.SAUCES_TAB,
            ConstructorLocators.FILLINGS_TAB,
        ],
        ids=["buns", "sauces", "fillings"],
    )
    def test_constructor_tab_becomes_active(self, driver, wait, tab_locator):
        driver.get(BASE_URL)
        wait.until(
            conditions.visibility_of_element_located(ConstructorLocators.PAGE_TITLE)
        )

        tab = wait.until(conditions.element_to_be_clickable(tab_locator))

        if tab_locator == ConstructorLocators.BUNS_TAB:
            sauces_tab = wait.until(
                conditions.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)
            )
            driver.execute_script("arguments[0].click();", sauces_tab)
            wait.until(
                lambda _: ConstructorLocators.ACTIVE_TAB_CLASS
                in sauces_tab.get_attribute("class")
            )

        driver.execute_script("arguments[0].click();", tab)

        wait.until(
            lambda _: ConstructorLocators.ACTIVE_TAB_CLASS
            in tab.get_attribute("class")
        )
        assert ConstructorLocators.ACTIVE_TAB_CLASS in tab.get_attribute("class")
