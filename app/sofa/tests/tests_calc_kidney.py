import unittest

from app.sofa.handlers.calc_kidney import calculation_creatinin


class TestCalculation_creatinin(unittest.TestCase):
    """
    Юнит-тесты для функции calculation_creatinin из модуля app.sofa.handlers.calc_kidney.

    Этот набор тестов проверяет функциональность функции calculation_creatinin, которая оценивает уровень креатинина на основе входных строк, представляющих различные диапазоны значений креатинина.
    Функция возвращает соответствующий балл в зависимости от указанных критериев.

    Тестовые случаи:
    - test_ReturnPointsZeroCreatinin: Проверяет случай, когда входное значение '< 110', ожидая возврат 0.
    - test_ReturnPointsOneCreatinin: Проверяет случай, когда входное значение '110 - 170', ожидая возврат 1.
    - test_ReturnPointsTwoCreatinin: Проверяет случай, когда входное значение '171 - 299', ожидая возврат 2.
    - test_ReturnPointsThreeCreatinin: Проверяет случай, когда входное значение '300 - 440 или диурез <500 мл в сутки', ожидая возврат 3.
    - test_ReturnPointsFourCreatinin: Проверяет случай, когда входное значение '> 440 или < 200 мл мочи/сутки', ожидая возврат 4.

    Чтобы запустить тесты, используйте следующую команду в терминале:
        python -m unittest -v app/sofa/tests/tests_calc_kidney.py
    """

    def test_ReturnPointsZeroCreatinin(self):
        self.assertEqual(calculation_creatinin('< 110'), 0)

    def test_ReturnPointsOneCreatinin(self):
        self.assertEqual(calculation_creatinin('110 - 170'), 1)

    def test_ReturnPointsTwoCreatinin(self):
        self.assertEqual(calculation_creatinin('171 - 299'), 2)

    def test_ReturnPointsThreeCreatinin(self):
        self.assertEqual(calculation_creatinin('300 - 440 или диурез <500 мл в сутки'), 3)

    def test_ReturnPointsFourCreatinin(self):
        self.assertEqual(calculation_creatinin('> 440 или < 200 мл мочи/сутки'), 4)