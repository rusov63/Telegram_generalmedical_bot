import unittest

from aiogram.types import ReplyKeyboardMarkup

from app.sofa.keyboards.kb_eye import kb_eye


class TestKb_eye(unittest.TestCase):

    def test_kb_eye(self):
        """
         Создает клавиатуру для выбора реакций глаз.

         Эта функция формирует клавиатуру с кнопками, представляющими различные реакции глаз,
         которые могут быть использованы в Telegram-боте. Клавиатура включает следующие кнопки:
         - 'Открывает самопроизвольно, наблюдает'
         - 'Открывает, в ответ на голос'
         - 'Открывает, как реакция на болевое раздражение'
         - 'Не открывает'

         Возвращает:
             ReplyKeyboardMarkup: Клавиатура с кнопками, настроенная с параметрами:
             - input_field_placeholder: 'Выберите ответ'
             - resize_keyboard: True (автоматическая подстройка размера клавиатуры)
             - one_time_keyboard: True (клавиатура скрывается после выбора)
         """
        keyboard = kb_eye()

        self.assertIsInstance(keyboard, ReplyKeyboardMarkup)
        self.assertTrue(keyboard.one_time_keyboard)
        self.assertTrue(keyboard.resize_keyboard)
        self.assertEqual(keyboard.input_field_placeholder, 'Выберите ответ')

        expected_buttons = [
            'Открывает самопроизвольно, наблюдает',
            'Открывает, в ответ на голос',
            'Открывает, как реакция на болевое раздражение',
            'Не открывает'
        ]

        # Извлекаем текст кнопок из клавиатуры
        actual_buttons = [button[0].text for button in keyboard.keyboard]

        # Проверяем, что все ожидаемые кнопки присутствуют
        self.assertListEqual(actual_buttons, expected_buttons)
