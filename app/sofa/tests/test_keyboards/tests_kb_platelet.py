import unittest

from aiogram.types import ReplyKeyboardMarkup

from app.sofa.keyboards.kb_platelet import kb_platelet


class TestKb_platelet(unittest.TestCase):

    def test_kb_platelet(self):
        """
        Тестирование функции клавиатуры для выбора значений тромбоцитов.

        Этот тест проверяет, что клавиатура, создаваемая функцией `kb_platelet`,
        имеет правильные настройки и содержит ожидаемые кнопки.

        Проверяемые параметры:
        - Тип клавиатуры должен быть `ReplyKeyboardMarkup`.
        - Поле ввода должно содержать текст 'Выберите ответ'.
        - Клавиатура должна быть настроена на изменение размера и одноразовое использование.

        Ожидаемые кнопки:
        - '> 151'
        - '<= 150'
        - '<= 100'
        - '<= 50'
        - '<= 20'
        """

        keyboard = kb_platelet()

        self.assertIsInstance(keyboard, ReplyKeyboardMarkup)
        self.assertEqual(keyboard.input_field_placeholder,'Выберите ответ')
        self.assertTrue(keyboard.resize_keyboard)
        self.assertTrue(keyboard.input_field_placeholder)

        buttons = [
            '> 151',
            '<= 150',
            '<= 100',
            '<= 50',
            '<= 20'
        ]

        actual_buttons = [button[0].text for button in keyboard.keyboard]

        self.assertListEqual(actual_buttons, buttons)
