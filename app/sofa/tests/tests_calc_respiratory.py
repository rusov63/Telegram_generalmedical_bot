import unittest

from app.sofa.handlers.calc_respiratory import calculation_respiratory


class TestCalculation_respiratory(unittest.TestCase):
    """
    Юнит-тесты для функции calculation_respiratory из модуля app.sofa.handlers.calc_respiratory.

    Этот класс содержит тесты, которые проверяют корректность работы функции calculation_respiratory,
    предназначенной для обработки ответов на вопросы о респираторных симптомах. Каждый тестовый случай
    проверяет, правильно ли функция обрабатывает различные входные данные и возвращает ожидаемые результаты.

    Тестовые случаи:
        - test_yes_response: Проверяет, что функция возвращает 1 для ответа 'Да'.
        - test_no_response: Проверяет, что функция возвращает 0 для ответа 'Нет'.
        - test_invalid_response: Проверяет, что функция вызывает ValueError для недопустимого ответа 'Может быть'.

    Чтобы запустить тесты из терминала, используйте следующую команду:
        python -m unittest -v app/sofa/tests/tests_calc_respiratory.py
    """

    def test_yes_response(self):
        self.assertEqual(calculation_respiratory('Да'), 1)

    def test_no_response(self):
        self.assertEqual(calculation_respiratory('Нет'), 0)

    def test_invalid_response(self):
        with self.assertRaises(ValueError):
            calculation_respiratory('Может быть')