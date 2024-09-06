import unittest

from app.skf.handlers.get_gender_user import get_gender


class Test_get_gender(unittest.TestCase):
    """
    Тестовый класс для проверки функции get_gender.

    Этот класс содержит тесты, которые проверяют корректность работы
    функции get_gender, определенной в модуле app.skf.handlers.get_gender_user.

    Методы:
    - test_get_gender: Проверяет, что функция возвращает 'Ошибка'
      для некорректных значений пола, таких как 'Ошибка' и
      список ['Другой гендер'].
    - test_getNone_gender: Проверяет, что функция возвращает None
      для корректных значений пола: 'мужской', 'муж', 'женский' и
      'жен'.
    """


    def test_get_gender(self):
        self.assertEqual(get_gender('Ошибка'), 'Ошибка')
        self.assertEqual(get_gender('Другой гендер'), 'Ошибка')

    def test_getNone_gender(self):
        self.assertEqual(get_gender('мужской'), 'мужской')
        self.assertEqual(get_gender('муж'), 'муж')
        self.assertEqual(get_gender('женский'), 'женский')
        self.assertEqual(get_gender('жен'), 'жен')
