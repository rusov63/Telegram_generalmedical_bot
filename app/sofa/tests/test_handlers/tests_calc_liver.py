import unittest

from app.sofa.handlers.calc_liver import calculation_liver


class TestCalculation_liver(unittest.TestCase):
    """
    Юнит-тесты для функции calculation_liver из модуля app.sofa.handlers.calc_liver.

    Этот набор тестов проверяет корректность работы функции calculation_liver,
    которая вычисляет баллы на основе оценок состояния печени. Каждый тестовый случай
    проверяет выходные данные функции на соответствие ожидаемым значениям для
    конкретных диапазонов входных данных.

    Тестовые случаи:
        - test_ReturnZeroPoints_Liver: Тестирует ввод '< 20', чтобы убедиться, что возвращается 0 баллов.
        - test_ReturnOnePoint_Liver: Тестирует ввод '20 - 32', чтобы убедиться, что возвращается 1 балл.
        - test_ReturnTwoPoints_Liver: Тестирует ввод '33 - 101', чтобы убедиться, что возвращается 2 балла.
        - test_ReturnThreePoints_Liver: Тестирует ввод '102 - 204', чтобы убедиться, что возвращается 3 балла.
        - test_ReturnFourPoints_Liver: Тестирует ввод '> 204', чтобы убедиться, что возвращается 4 балла.

    Чтобы запустить тесты из терминала, используйте следующую команду:
        python -m unittest -v app/sofa/tests/tests_calc_liver.py
    """
    def test_ReturnZeroPoints_Liver(self):
        self.assertEqual(calculation_liver('< 20'), 0)

    def test_ReturnOnePoint_Liver(self):
        self.assertEqual(calculation_liver('20 - 32'), 1)

    def test_ReturnTwoPoints_Liver(self):
        self.assertEqual(calculation_liver('33 - 101'), 2)

    def test_ReturnThreePoints_Liver(self):
        self.assertEqual(calculation_liver('102 - 204'), 3)

    def test_ReturnFourPoints_Liver(self):
        self.assertEqual(calculation_liver('> 204'), 4)