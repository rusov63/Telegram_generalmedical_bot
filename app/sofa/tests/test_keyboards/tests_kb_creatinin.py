import unittest
from aiogram.types import ReplyKeyboardMarkup

from app.sofa.keyboards.kb_creatinin import kb_creatinin


class TestKbCreatinin(unittest.TestCase):


    def test_kb_creatinin(self):
        """
        Создает клавиатуру для выбора диапазонов значений креатинина.

        Эта функция формирует клавиатуру с кнопками, представляющими различные диапазоны значений креатинина,
        которые могут быть использованы в Telegram-боте. Клавиатура включает следующие кнопки:
        - '< 110'
        - '110 - 170'
        - '171 - 299'
        - '300 - 440 или диурез <500 мл в сутки'
        - '> 440 или < 200 мл мочи/сутки'

        Возвращает:
            ReplyKeyboardMarkup: Клавиатура с кнопками, настроенная с параметрами:
            - input_field_placeholder: 'Выберите ответ'
            - resize_keyboard: True (автоматическая подстройка размера клавиатуры)
            - one_time_keyboard: True (клавиатура скрывается после выбора)
        """

        # Создаем клавиатуру
        keyboard = kb_creatinin()

        # Проверяем, что клавиатура имеет правильные настройки
        self.assertIsInstance(keyboard, ReplyKeyboardMarkup)
        self.assertTrue(keyboard.resize_keyboard)
        self.assertTrue(keyboard.one_time_keyboard)
        self.assertEqual(keyboard.input_field_placeholder, 'Выберите ответ')

        # Проверяем, что клавиатура содержит правильные кнопки
        expected_buttons = [
            '< 110',
            '110 - 170',
            '171 - 299',
            '300 - 440 или диурез <500 мл в сутки',
            '> 440 или < 200 мл мочи/сутки'
        ]

        # Извлекаем текст кнопок из клавиатуры
        actual_buttons = [button[0].text for button in keyboard.keyboard]

        # Проверяем, что все ожидаемые кнопки присутствуют
        self.assertListEqual(actual_buttons, expected_buttons)