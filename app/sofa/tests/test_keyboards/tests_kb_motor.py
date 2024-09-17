import unittest

from aiogram.types import ReplyKeyboardMarkup

from app.sofa.keyboards.kb_motor import kb_motor


class TestKb_motor(unittest.TestCase):

    def test_kb_motor(self):
        """
          Тестирование функции создания клавиатуры для оценки моторной активности.

          Этот тест проверяет, что функция `kb_motor()` возвращает объект типа
          `ReplyKeyboardMarkup` с правильными настройками и кнопками.

          Проверяемые параметры:
          - Тип клавиатуры должен быть `ReplyKeyboardMarkup`.
          - Клавиатура должна быть настроена на одноразовое использование (one_time_keyboard).
          - Клавиатура должна быть изменяемой по размеру (resize_keyboard).
          - Плейсхолдер для ввода должен быть 'Выберите ответ'.

          Ожидаемые кнопки:
          - 'Выполнение движений по голосовой команде'
          - 'Локализует боль, пытается её избежать'
          - 'Бессмысленные движения в ответ на боль'
          - 'Патологическое сгибание в ответ на боль (декортикационная ригидность)'
          - 'Патологическое разгибание в ответ на боль (децеребрационная ригидность)'
          - 'Не двигается'
          """
        keyboard = kb_motor()

        self.assertIsInstance(keyboard, ReplyKeyboardMarkup)
        self.assertTrue(keyboard.resize_keyboard)
        self.assertTrue(keyboard.one_time_keyboard)
        self.assertEqual(keyboard.input_field_placeholder,'Выберите ответ')

        buttons = [
            'Выполнение движений по голосовой команде',
            'Локализует боль, пытается её избежать',
            'Бессмысленные движения в ответ на боль',
            'Патологическое сгибание в ответ на боль (декортикационная ригидность)',
            'Патологическое разгибание в ответ на боль (децеребрационная ригидность)',
            'Не двигается'
        ]


        actual_buttons = [button[0].text for button in keyboard.keyboard]

        self.assertListEqual(actual_buttons, buttons)