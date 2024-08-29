import unittest

from app.sofa.handlers.calc_platelet import calculation_platelet


class TestСalculation_platelet(unittest.TestCase):
    """
    Юнит-тесты для функции calculation_platelet из модуля app.sofa.handlers.calc_platelet.

    Этот набор тестов проверяет корректность работы функции calculation_platelet,
    которая вычисляет баллы на основе уровня тромбоцитов в крови. Каждый тестовый случай
    проверяет выходные данные функции на соответствие ожидаемым значениям для
    различных диапазонов входных данных.

    Тестовые случаи:
        - test_returnZero_Platelet: Тестирует ввод '> 151', чтобы убедиться, что возвращается 0 баллов.
        - test_returnOne_Platelet: Тестирует ввод '< 110', чтобы убедиться, что возвращается 1 балл.
        - test_returnTwo_Platelet: Тестирует ввод '< 61', чтобы убедиться, что возвращается 2 балла.
        - test_returnFree_Platelet: Тестирует ввод '< 32', чтобы убедиться, что возвращается 3 балла.
        - test_returnFour_Platelet: Тестирует ввод '< 12', чтобы убедиться, что возвращается 4 балла.

    Чтобы запустить тесты из терминала, используйте следующую команду:
        python -m unittest -v app/sofa/tests/tests_calc_platelet.py
    """

    def test_returnZero_Platelet(self):
        self.assertEqual(calculation_platelet('> 151'), 0)  # Тромбоциты >= 151

    def test_returnOne_Platelet(self):
        self.assertEqual(calculation_platelet('< 110'), 1)  # 101 < Тромбоциты <= 100

    def test_returnTwo_Platelet(self):
        self.assertEqual(calculation_platelet('< 61'), 2)  # 51 < Тромбоциты <= 100:

    def test_returnFree_Platelet(self):
        self.assertEqual(calculation_platelet('< 32'), 3)  # 21 < Тромбоциты <= 50

    def test_returnFour_Platelet(self):
        self.assertEqual(calculation_platelet('< 12'), 4)  # 0 < Тромбоциты <= 20