import unittest

from app.sofa.handlers.result_calculating_functions import total_result_functions


class Test_total_result_functions(unittest.TestCase):
    """
    Класс для тестирования функции total_result_functions из модуля
    app.sofa.handlers.result_calculating_functions.

    Этот класс содержит набор тестов, которые проверяют корректность работы функции
    total_result_functions с различными входными параметрами. Тесты охватывают
    следующие аспекты:

    - Проверка правильности вычисления баллов и смертности для различных комбинаций входных данных.
    - Обработка граничных случаев, таких как нулевые значения и максимальные баллы.
    - Проверка обработки ошибок при передаче некорректных типов данных (например, None или строки).

    Для запуска тестов используйте команду:
    python -m unittest -v app/sofa/tests/tests_result_calculating_functions.py
    """

    def test_MaximumSixPoints(self):
        self.assertEqual(total_result_functions(1, 0, 1, 1, 1, 1, 1),
                         '<b>Баллов: 6 \nСмертность: &lt; 10%</b>\n<b>Множественные органные дисфункции</b>')

    def test_MaximumSevenPoints(self):
        self.assertEqual(total_result_functions(1, 2, 1, 1, 1, 1, 1),
                         '<b>Баллов: 8 \nСмертность: 15-20%</b>\n<b>Множественные органные дисфункции</b>')

    def test_MaximumEightPoints(self):
        self.assertEqual(total_result_functions(2, 2, 1, 2, 1, 1, 2),
                         '<b>Баллов: 11 \nСмертность: 40-50%</b>\n<b>Множественные органные дисфункции</b>')

    def test_MaximumFourteenPoints(self):
        self.assertEqual(total_result_functions(3, 3, 3, 2, 1, 1, 1),
                         '<b>Баллов: 14 \nСмертность: 50-60%</b>\n<b>Переход дисфункции в недостаточность</b>')

    def test_MaximumFiveteenPoints(self):
        self.assertEqual(total_result_functions(3, 3, 3, 2, 1, 1, 2),
                         '<b>Баллов: 15 \nСмертность: &gt; 80%</b>\n<b>Переход дисфункции в недостаточность</b>')

    def test_MaximumNineteenPoints(self):
        self.assertEqual(total_result_functions(5, 3, 1, 2, 4, 5, 3),
                         '<b>Баллов: 23 \nСмертность: &gt; 90%</b>\n<b>Высокая вероятность летального исхода</b>')

    def test_MaximumTwentyFivePoints(self):
        self.assertEqual(total_result_functions(5, 3, 1, 5, 4, 5, 3), '<b>Ошибка, повторите еще раз!</b>')

    def test_ReturnsErrorNone(self):
        self.assertEqual(total_result_functions(None, 5, 3, 1, 2, 4, 5), '<b>Ошибка, повторите еще раз!</b>')

    def test_ReturnsErrorString(self):
        self.assertEqual(total_result_functions('Invalid', None, 3, 1, 2, 4, 5), '<b>Ошибка, повторите еще раз!</b>')

    def test_edge_cases(self):
        self.assertEqual(total_result_functions(0, 0, 0, 0, 0, 0, 0),
                         '<b>Баллов: 0 \nСмертность: &lt; 10%</b>\n<b>Множественные органные дисфункции</b>')

        self.assertEqual(total_result_functions(15, 0, 0, 0, 0, 0, 0),
                         '<b>Баллов: 15 \nСмертность: &gt; 80%</b>\n<b>Переход дисфункции в недостаточность</b>')