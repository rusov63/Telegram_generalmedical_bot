import unittest

from app.skf.handlers.calc_GenAgeCreatinin import calc_skf


class Test_calc_skf(unittest.TestCase):
    """
    Тестовый класс для проверки функции calc_skf.

    Данный класс содержит тесты для функции calc_skf, которая рассчитывает
    скорость клубочковой фильтрации (СКФ) по формуле CKD-EPI. Тесты проверяют
    корректность расчетов для различных комбинаций пола, возраста и уровня
    креатинина, а также обработку некорректных входных данных.

    Тесты включают:
    - Проверку для женщин с низким уровнем креатинина.
    - Проверку для женщин с высоким уровнем креатинина.
    - Проверку для мужчин с низким уровнем креатинина.
    - Проверку для мужчин с высоким уровнем креатинина.
    - Проверку на некорректный возраст.
    - Проверку на некорректный уровень креатинина.
    """

    def test_female_low_creatinine(self):
        self.assertEqual(calc_skf('женский', "56", "56"), 'Скорость клубочковой фильтрации: <b>100 мл/мин/1.73м²</b>')

    def test_female_high_creatinine(self):
        self.assertEqual(calc_skf('жен', '56', '63'), 'Скорость клубочковой фильтрации: <b>95 мл/мин/1.73м²</b>')

    def test_male_low_creatinine(self):
        self.assertEqual(calc_skf('мужской', "63", "79"), 'Скорость клубочковой фильтрации: <b>91 мл/мин/1.73м²</b>')

    def test_male_high_creatinine(self):
        self.assertEqual(calc_skf('муж', "63", "81"), 'Скорость клубочковой фильтрации: <b>89 мл/мин/1.73м²</b>')


    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            calc_skf('женский', 'двадцать', '70')

    def test_invalid_creatinine(self):
        with self.assertRaises(ValueError):
            calc_skf('мужской', '50', 'недопустимо')