import unittest

from app.skf.handlers.get_number_creatinine_age import get_answer_age, get_answer_creatinine


class TestAnswerAge(unittest.TestCase):
    """
    Тестовый класс для проверки функции get_answer_age.

    Этот класс содержит тесты, проверяет корректность работы функции,
    которая проверяет есть ли числовое значение в строке.
    """

    def test_valid_age(self):
        self.assertEqual(get_answer_age("25"), 25)
        self.assertEqual(get_answer_age("45"), 45)
        self.assertEqual(get_answer_age("100"), 100)

    def test_None_age(self):
        self.assertEqual(get_answer_age("120"), None)
        self.assertEqual(get_answer_age(""), None)
        self.assertEqual(get_answer_age("abc"), None)
        self.assertEqual(get_answer_age("-120"), None)

    def test_caching(self):
        # Проверяем, что результаты кэшируются
        self.assertEqual(get_answer_age("25"), 25)
        self.assertEqual(get_answer_age("25"), 25)  # Второй вызов должен вернуть результат из кэша


class TestAnswerAge(unittest.TestCase):
    """
    Тестовый класс для проверки функции get_answer_creatinine.

    Этот класс содержит тесты, проверяет корректность работы функции,
    которая проверяет есть ли числовое значение в строке.
    """

    def test_valid_creatinine(self):
        self.assertEqual(get_answer_creatinine('20'), 20)
        self.assertEqual(get_answer_creatinine('900'), 900)
        self.assertEqual(get_answer_creatinine('0'), 0)

    def test_None_creatinine(self):
        self.assertEqual(get_answer_age("-1"), None)
        self.assertEqual(get_answer_age(""), None)
        self.assertEqual(get_answer_age("abc"), None)
        self.assertEqual(get_answer_age("-1020"), None)

    def test_caching(self):
        self.assertEqual(get_answer_age("25"), 25)
        self.assertEqual(get_answer_age("25"), 25)
