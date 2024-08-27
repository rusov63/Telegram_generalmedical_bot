import unittest

from app.sofa.handlers.calc_platelet import calculation_platelet


class Test_calculation_platelet(unittest.TestCase):

    def test_calculation(self):
        self.assertGreaterEqual(calculation_platelet('> 151'), 0)