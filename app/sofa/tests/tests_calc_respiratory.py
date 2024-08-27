import unittest

from app.sofa.handlers.calc_respiratory import calculation_respiratory


class TestCalculation_respiratory(unittest.TestCase):

    def test_yes_response(self):
        self.assertEqual(calculation_respiratory('Да'), 1)

    def test_no_response(self):
        self.assertEqual(calculation_respiratory('Нет'), 0)

    def test_invalid_response(self):
        with self.assertRaises(ValueError):
            calculation_respiratory('Может быть')


# python -m unittest -v app/sofa/tests/tests_calc_respiratory.py