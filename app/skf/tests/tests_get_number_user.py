import unittest

from app.skf.handlers.get_number_user import get_answer_age_creatinin


class TestGetNumberUser(unittest.TestCase):
    """
    Тестовый класс для проверки функции get_number_user.

    Этот класс содержит тесты, которые проверяют корректность работы функции
    get_number_user, которая извлекает числовое значение из строки, представляющей
    возраст. Тесты проверяют различные сценарии, включая строки с разными
    форматами и значениями.

    Методы:
    - test_valid_age: Проверяет корректность извлечения числовых значений
      из строк, содержащих текст и числа.
    """
    def test_valid_age(self):
        self.assertEqual(get_answer_age_creatinin('мне 120 лет'), 120)
        self.assertEqual(get_answer_age_creatinin('Возраст 45'), 45)
        self.assertEqual(get_answer_age_creatinin('Я 30'), 30)
        self.assertEqual(get_answer_age_creatinin('30'), 30)