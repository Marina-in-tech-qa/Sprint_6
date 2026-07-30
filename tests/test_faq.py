import pytest

from data import FAQ_ANSWERS
from pages.main_page import MainPage
from urls import BASE_URL


class TestFAQ:

    @pytest.mark.parametrize(
        "question_index, expected_answer",
        list(enumerate(FAQ_ANSWERS))
    )
    def test_faq_answer_matches_question(
        self,
        driver,
        question_index,
        expected_answer
    ):
        main_page = MainPage(driver)

        main_page.open_main_page(BASE_URL)
        main_page.accept_cookies()
        main_page.click_question(question_index)

        actual_answer = main_page.get_answer_text(question_index)

        assert actual_answer == expected_answer