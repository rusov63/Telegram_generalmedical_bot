import unittest

from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from app.skf.inline_kb_skf import inline_kb_skf
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


class TestInlineKbSkf(unittest.TestCase):
    def test_inline_kb_skf(self):
        """
        Проверяет, что функция 'inline_kb_skf()' возвращает ожидаемый объект InlineKeyboardMarkup.
        """

        ожидаемая_разметка = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='На стартовую', callback_data='/start')],
            [InlineKeyboardButton(text='Вернуться назад', callback_data='/skf')]
        ])

        фактическая_разметка = inline_kb_skf()

        self.assertEqual(ожидаемая_разметка, фактическая_разметка)
