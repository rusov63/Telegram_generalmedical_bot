import unittest

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.sofa.keyboards.inline_kb_sofa import inline_sofa


class TestInlineKbSkf(unittest.TestCase):
    def test_inline_kb_sofa(self):
        """
        Проверяет, что функция 'inline_kb_sofa()' возвращает ожидаемый объект InlineKeyboardMarkup.
        """

        ожидаемая_разметка = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='🚀 На стартовую', callback_data='/start')],
            [InlineKeyboardButton(text='🔙 Вернуться назад', callback_data='/sofa')]
        ])

        фактическая_разметка = inline_sofa()

        self.assertEqual(ожидаемая_разметка, фактическая_разметка)