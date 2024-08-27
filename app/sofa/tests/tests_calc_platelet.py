import unittest

from app.sofa.handlers.calc_platelet import calculation_platelet


class Test_calculation_platelet(unittest.TestCase):

    def test_returnZero(self):
        self.assertEqual(calculation_platelet('> 151'), 0)  # Тромбоциты >= 151

    def test_returnOne(self):
        self.assertEqual(calculation_platelet('< 110'), 1)  # 101 < Тромбоциты <= 100

    def test_returnTwo(self):
        self.assertEqual(calculation_platelet('< 61'), 2)  # 51 < Тромбоциты <= 100:

    def test_returnFree(self):
        self.assertEqual(calculation_platelet('< 32'), 3)  # 21 < Тромбоциты <= 50

    def test_returnFour(self):
        self.assertEqual(calculation_platelet('< 12'), 4)  # 0 < Тромбоциты <= 20