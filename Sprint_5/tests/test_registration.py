"""Тесты регистрации пользователя."""

from selenium.webdriver.support import expected_conditions as conditions

from generators import generate_email, generate_password
from locators import LoginLocators, RegistrationLocators
from urls import LOGIN_URL, REGISTER_URL


class TestRegistration:
    def test_successful_registration_redirects_to_login(self, driver, wait):
        email = generate_email()
        password = generate_password()
        driver.get(REGISTER_URL)

        wait.until(
            conditions.visibility_of_element_located(RegistrationLocators.PAGE_TITLE)
        )
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Test Student")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

        assert wait.until(
            conditions.visibility_of_element_located(LoginLocators.PAGE_TITLE)
        )
        assert driver.current_url.rstrip("/") == LOGIN_URL

    def test_registration_with_short_password_shows_error(self, driver, wait):
        driver.get(REGISTER_URL)

        wait.until(
            conditions.visibility_of_element_located(RegistrationLocators.PAGE_TITLE)
        )
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Test Student")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(
            generate_email()
        )
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

        error = wait.until(
            conditions.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR)
        )
        assert error.text == "Некорректный пароль"
        assert driver.current_url.rstrip("/") == REGISTER_URL
