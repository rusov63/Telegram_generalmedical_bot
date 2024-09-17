import unittest

from app.blood_donor.handlers.check_correct import СheckСorrectPhenotype


class TestCheckCorrectPhenotyp(unittest.TestCase):

    def test_correct_data(self):
        self.assertEqual(СheckСorrectPhenotype('CcDee'), 'CcDee')
        self.assertEqual(СheckСorrectPhenotype('CCDweakee'), 'CCDweakee')
        self.assertEqual(СheckСorrectPhenotype('KK'), 'KK')

    def test_correct_None(self):
        self.assertEqual(СheckСorrectPhenotype('drop'), None)