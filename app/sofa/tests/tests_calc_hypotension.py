import unittest

from app.sofa.handlers.calc_hypotension import calculate_hypotension

class TestCalculate_hypotension(unittest.TestCase):

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



# Для запуска из терминала
# python -m unittest -v app/sofa/tests/tests_calc_hypotension.py