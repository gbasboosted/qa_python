"""Проверки выпадающего списка «Вопросы о важном»."""

import allure
import pytest

from data import FAQ_DATA
from pages.main_page import MainPage


@allure.feature("Вопросы о важном")
class TestFaq:
    @allure.title("Ответ на вопрос: {question}")
    @pytest.mark.parametrize(
        "question_index, question, expected_answer",
        [
            (index, question, answer)
            for index, (question, answer) in enumerate(FAQ_DATA)
        ],
        ids=[f"question-{index + 1}" for index in range(len(FAQ_DATA))],
    )
    def test_question_opens_corresponding_answer(
        self,
        driver,
        question_index,
        question,
        expected_answer,
    ):
        page = MainPage(driver).open_main_page()

        actual_answer = page.open_faq_answer(question_index)

        assert actual_answer == expected_answer
