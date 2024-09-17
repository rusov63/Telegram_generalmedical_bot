import unittest

from aiogram.types import ReplyKeyboardMarkup

from app.sofa.keyboards.kb_respiratory import kb_respiratory


class TestKb_respiratory(unittest.TestCase):

    def test_kb_respiratory(self):
        """
         Создает клавиатуру для выбора ответа на вопрос о респираторной функции.

         Возвращает объект типа ReplyKeyboardMarkup с кнопками 'Да' и 'Нет'.
         Клавиатура настроена на одноразовое использование и изменение размера.
         Поле ввода содержит текст 'Выберите ответ'.

         :return: ReplyKeyboardMarkup - клавиатура с кнопками для выбора ответа.
         """

        keyboard = kb_respiratory()

        self.assertIsInstance(keyboard, ReplyKeyboardMarkup)
        self.assertTrue(keyboard.resize_keyboard)
        self.assertTrue(keyboard.one_time_keyboard)
        self.assertEqual(keyboard.input_field_placeholder, 'Выберите ответ')

        buttons = [
            'Да',
            'Нет'
        ]

        actual_buttons = [button[0].text for button in keyboard.keyboard]

        self.assertListEqual(actual_buttons, buttons)