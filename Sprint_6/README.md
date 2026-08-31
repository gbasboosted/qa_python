# Sprint_6 — UI-тесты сервиса «Яндекс.Самокат»

Проект покрывает автотестами учебный сервис
[«Яндекс.Самокат»](https://qa-scooter.praktikum-services.ru/). Тесты написаны
на Python с Selenium и pytest, построены по Page Object Model и формируют
результаты для Allure.

## Что проверяется

- каждый из восьми вопросов в разделе «Вопросы о важном» открывает свой ответ;
- заказ успешно оформляется с двумя наборами данных;
- обе точки входа в заказ — верхняя и нижняя кнопки — работают;
- логотип Самоката ведёт на главную страницу;
- логотип Яндекса открывает Дзэн в новом окне.

## Структура

- `pages/` — Page Object главной страницы, формы заказа и базовые действия;
- `tests/` — тесты, сгруппированные по функциональности;
- `data.py` — параметры FAQ и два набора данных заказа;
- `conftest.py` — создание и закрытие Firefox;
- `allure-results/` — результаты последнего тестового запуска для Allure.

## Подготовка и запуск

Нужны Python 3.10+ и Mozilla Firefox.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

По умолчанию Firefox запускается без интерфейса. Для видимого запуска:

```bash
HEADLESS=false pytest
```

На macOS Firefox ожидается по адресу
`/Applications/Firefox.app/Contents/MacOS/firefox`. Другой путь можно передать
через переменную `FIREFOX_BINARY`.

## Allure-отчёт

Pytest сохраняет результаты в `allure-results/`. После установки Allure CLI
отчёт открывается командой:

```bash
allure serve allure-results
```

Для сохранения статического HTML-отчёта:

```bash
allure generate allure-results --clean -o allure-report
```
