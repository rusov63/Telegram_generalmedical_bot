import unittest

from aiogram.types import ReplyKeyboardMarkup

from app.sofa.keyboards.kb_verbal import kb_verbal


class TestKb_verbal(unittest.TestCase):

    def test_kb_verbal(self):
        """
         Создает клавиатуру для выбора вербального ответа пользователя.

         Возвращает объект типа ReplyKeyboardMarkup с кнопками, представляющими
         различные варианты вербального ответа. Клавиатура настраивается так,
         чтобы быть одноразовой и изменяемой по размеру. Поле ввода содержит
         подсказку "Выберите ответ".

         Кнопки:
         - Ориентирован и контактен (осмысленный ответ)
         - Произносит фразы, но речь бессвязная
         - Произносит отдельные слова
         - Издает звуки, но не слова
         - Отсутствие речи

         Returns:
             ReplyKeyboardMarkup: Клавиатура с кнопками для выбора вербального ответа.
         """

        keyboard = kb_verbal()

        self.assertTrue(keyboard.resize_keyboard)
        self.assertTrue(keyboard.input_field_placeholder)
        self.assertIsInstance(keyboard, ReplyKeyboardMarkup)
        self.assertEqual(keyboard.input_field_placeholder, 'Выберите ответ')

        buttons = [
            'Ориентирован и контактен (осмысленный ответ)',
            'Произносит фразы, но речь бессвязная',
            'Произносит отдельные слова',
            'Издает звуки, но не слова',
            'Отсутствие речи'
        ]

        actual_buttons = [button[0].text for button in keyboard.keyboard]

        self.assertListEqual(actual_buttons, buttons)