"""Локаторы элементов Stellar Burgers."""

from selenium.webdriver.common.by import By


class HeaderLocators:
    # Ссылка «Конструктор» в шапке
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//header//p[normalize-space()='Конструктор']/ancestor::a",
    )
    # Логотип Stellar Burgers со ссылкой на главную страницу
    LOGO_LINK = (By.CSS_SELECTOR, "header nav div a[href='/']")
    # Ссылка «Личный кабинет» в шапке
    PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, "header a[href='/account']")


class ConstructorLocators:
    # Часть класса, которая обозначает активную вкладку конструктора
    ACTIVE_TAB_CLASS = "tab_tab_type_current"
    # Заголовок страницы конструктора
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")
    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Войти в аккаунт']",
    )
    # Вкладка раздела «Булки»
    BUNS_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab') and normalize-space()='Булки']",
    )
    # Вкладка раздела «Соусы»
    SAUCES_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab') and normalize-space()='Соусы']",
    )
    # Вкладка раздела «Начинки»
    FILLINGS_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab') and normalize-space()='Начинки']",
    )


class LoginLocators:
    # Заголовок формы входа
    PAGE_TITLE = (By.XPATH, "//h2[normalize-space()='Вход']")
    # Поле Email в форме входа
    EMAIL_INPUT = (
        By.XPATH,
        "//form//label[normalize-space()='Email']/following-sibling::input",
    )
    # Поле «Пароль» в форме входа
    PASSWORD_INPUT = (
        By.XPATH,
        "//form//label[normalize-space()='Пароль']/following-sibling::input",
    )
    # Кнопка «Войти» в форме входа
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")


class RegistrationLocators:
    # Заголовок формы регистрации
    PAGE_TITLE = (By.XPATH, "//h2[normalize-space()='Регистрация']")
    # Поле «Имя» в форме регистрации
    NAME_INPUT = (
        By.XPATH,
        "//form//label[normalize-space()='Имя']/following-sibling::input",
    )
    # Поле Email в форме регистрации
    EMAIL_INPUT = (
        By.XPATH,
        "//form//label[normalize-space()='Email']/following-sibling::input",
    )
    # Поле «Пароль» в форме регистрации
    PASSWORD_INPUT = (
        By.XPATH,
        "//form//label[normalize-space()='Пароль']/following-sibling::input",
    )
    # Кнопка «Зарегистрироваться»
    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Зарегистрироваться']",
    )
    # Сообщение об ошибке под полем с некорректным паролем
    PASSWORD_ERROR = (By.CSS_SELECTOR, ".input__error")
    # Ссылка «Войти» под формой регистрации
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")


class ForgotPasswordLocators:
    # Заголовок формы восстановления пароля
    PAGE_TITLE = (
        By.XPATH,
        "//h2[normalize-space()='Восстановление пароля']",
    )
    # Ссылка «Войти» под формой восстановления пароля
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")


class AccountLocators:
    # Поле имени пользователя в личном кабинете
    NAME_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Имя']/following-sibling::input",
    )
    # Кнопка выхода из личного кабинета (в интерфейсе подписана «Выход»)
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")
