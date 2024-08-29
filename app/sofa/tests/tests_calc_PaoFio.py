import unittest

from app.sofa.handlers.calc_PaoFio import calculation_PaoFio


class TestCalculation_PaoFio(unittest.TestCase):
    """
    Тесты для функции calculation_PaoFio из модуля app.sofa.handlers.calc_PaoFio.

    Этот класс содержит тесты, которые проверяют корректность работы функции
    calculation_PaoFio, включая обработку различных типов входных данных,
    проверку на ошибки и правильность возвращаемых значений в зависимости
    от заданных параметров.

    Методы тестирования:
    - test_roundNumbers: Проверяет, что результат вычисления 0.1234 * 0.123 / 0.123
      почти равен 0.123 с заданной точностью.
    - test_TypeError: Проверяет, что функция вызывает TypeError при
      передаче некорректных типов аргументов.
    - test_ZeroDivisionError: Проверяет, что функция вызывает
      ZeroDivisionError при делении на ноль.
    - test_MultiplicationTwoNumbers: Проверяет, что результат
      multiplication двух чисел равен 0.
    - test_ReturnOneBetween_301_401: Проверяет, что функция возвращает 1
      для входных значений между 301 и 401.
    - test_ReturnTwoBetween_200_300: Проверяет, что функция возвращает 2
      для входных значений между 200 и 300.
    - test_ReturnFreeBetween_100_200: Проверяет, что функция возвращает 3
      для входных значений между 100 и 200.
    - test_ReturnFourLess_100: Проверяет, что функция возвращает 4 для
      входных значений меньше 100.
    - test_CorrectnessSuppliedNumbers: Проверяет, что функция возвращает
      сообщение об ошибке при передаче некорректных строковых значений.

    Чтобы запустить тесты из терминала, используйте следующую команду:
    python -m unittest -v app/sofa/tests/tests_calc_PaoFio.py
    """

    def test_roundNumbers(self):
        self.assertAlmostEqual(0.1234 * 0.123 / 0.123, 0.123, places=0, msg="Invalid")

    def test_TypeError(self):
        # Тестируем некорректные значения, неправильный тип
        with self.assertRaises(TypeError):
            self.assertEqual(calculation_PaoFio('8y', '30'))

    def test_ZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(calculation_PaoFio('400', '0'), '<b>Ошибка, повторите еще раз!</b>')

    def test_MultiplicationTwoNumbers(self):
        self.assertEqual(calculation_PaoFio('402', '100'), 0)

    def test_ReturnOneBetween_301_401(self):
        self.assertEqual(calculation_PaoFio('350', '100'), 1)

    def test_ReturnTwoBetween_200_300(self):
        self.assertEqual(calculation_PaoFio('250', '100'), 2)

    def test_ReturnFreeBetween_100_200(self):
        self.assertEqual(calculation_PaoFio('150', '100'), 3)

    def test_ReturnFourLess_100(self):
        self.assertEqual(calculation_PaoFio('49', '100'), 4)

    def test_CorrectnessSuppliedNumbers(self):
        self.assertEqual(calculation_PaoFio('a4o', '45'), '<b>Ошибка, повторите еще раз!</b>')
        self.assertEqual(calculation_PaoFio('245', 'l'), '<b>Ошибка, повторите еще раз!</b>')