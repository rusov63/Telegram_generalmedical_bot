import unittest

from aiogram.types import ReplyKeyboardMarkup

from app.skf.keyboard import kb_skf


class TestKb_skf(unittest.TestCase):
    """
    Тестовый класс для проверки функции kb_skf.

    Этот класс содержит тесты для функции kb_skf, которая создает
    клавиатуру с кнопками выбора пола. Тесты проверяют, что
    возвращаемый объект является экземпляром ReplyKeyboardMarkup,
    а также проверяют настройки клавиатуры и текст кнопок.
    """

    def test_kb_skf(self):
        """
        Тестирует функцию kb_skf.

        Проверяет, что:
        - Возвращаемый объект является экземпляром ReplyKeyboardMarkup.
        - Параметры resize_keyboard и one_time_keyboard установлены в True.
        - Плейсхолдер для ввода соответствует ожидаемому значению.
        - Клавиатура содержит одну строку с двумя кнопками.
        - Текст кнопок соответствует ожидаемым значениям 'Женский' и 'Мужской'.
        """

        keyboard = kb_skf()

        self.assertIsInstance(keyboard, ReplyKeyboardMarkup)
        self.assertTrue(keyboard.resize_keyboard)
        self.assertTrue(keyboard.one_time_keyboard)
        self.assertEqual(keyboard.input_field_placeholder,'Выберите ответ')

        self.assertEqual(len(keyboard.keyboard), 1)

        self.assertEqual(len(keyboard.keyboard[0]), 2)
        self.assertEqual(keyboard.keyboard[0][0].text, "Женский")
        self.assertEqual(keyboard.keyboard[0][1].text, "Мужской")