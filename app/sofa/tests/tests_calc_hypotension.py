import unittest

from app.sofa.handlers.calc_hypotension import calculate_hypotension

class TestCalculate_hypotension(unittest.TestCase):
    """
    Тестирование функции расчета гипотонии.

    Модуль содержит класс тестов для проверки корректности работы функции:
    - calculate_hypotension: вычисляет количество баллов на основе входного значения, представляющего собой строку.

    Каждый метод теста проверяет различные сценарии, включая:
    - Пустую строку, которая должна вернуть 0 баллов.
    - Строки, представляющие различные числовые значения, которые должны возвращать соответствующее количество баллов.

    Примеры тестируемых случаев:
    - Пустая строка возвращает 0.
    - Строка '70' возвращает 1.
    - Строка '5' возвращает 2.
    - Строка '50101' возвращает 3.
    - Строка '150101' возвращает 4.

    Для запуска тестов используйте команду:
    python -m unittest -v app/sofa/tests/tests_calc_hypotension.py
    """

    def test_ReturnPointsZero(self):
        self.assertEqual(calculate_hypotension(''), 0)


    def test_ReturnPointsOne(self):
        self.assertEqual(calculate_hypotension('70'), 1)

    def test_ReturnPointsTwo(self):
        self.assertEqual(calculate_hypotension('5'), 2)

    def test_ReturnPointsThree(self):
        self.assertEqual(calculate_hypotension('50101'), 3)

    def test_ReturnPointsFour(self):
        self.assertEqual(calculate_hypotension('150101'), 4)