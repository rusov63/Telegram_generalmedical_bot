import unittest

from aiogram.types import ReplyKeyboardMarkup

from app.sofa.keyboards.kb_liver import kb_liver


class TestKb_liver(unittest.TestCase):

    def test_kb_liver(self):
        """
        Тестовый класс для проверки функции создания клавиатуры 'kb_liver'.

        Этот класс наследует от unittest.TestCase и содержит тесты для проверки
        корректности работы функции kb_liver, которая создает клавиатуру с кнопками
        для выбора диапазонов значений.

        Тесты проверяют следующие аспекты:
        - Тип возвращаемого объекта: должен быть экземпляр ReplyKeyboardMarkup.
        - Настройки клавиатуры:
            - one_time_keyboard должно быть True (клавиатура скрывается после выбора).
            - resize_keyboard должно быть True (автоматическая подстройка размера клавиатуры).
            - input_field_placeholder должен быть равен 'Выберите ответ'.
        - Наличие правильных кнопок на клавиатуре: проверяется, что все ожидаемые кнопки
          присутствуют в созданной клавиатуре.
        """

        keyboard = kb_liver()

        self.assertIsInstance(keyboard, ReplyKeyboardMarkup)
        self.assertTrue(keyboard.resize_keyboard)
        self.assertTrue(keyboard.one_time_keyboard)
        self.assertEqual(keyboard.input_field_placeholder, 'Выберите ответ')

        buttons = [
            '< 20',
            '20 - 32',
            '33 - 101',
            '102 - 204',
            '> 204'
        ]

        # Извлекаем текст кнопок из клавиатуры
        actual_buttons = [button[0].text for button in keyboard.keyboard]

        # Проверяем, что все ожидаемые кнопки присутствуют
        self.assertListEqual(actual_buttons, buttons)