from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Определение текстов для кнопок
ONE = ('< 20')
TWO = ('20 - 32')
THREE = ('33 - 101')
FOUR = ('102 - 204')
FIVE = ('> 204')


def kb_liver() -> ReplyKeyboardMarkup:
    """
    Функция для создания клавиатуры с кнопками, представляющими диапазоны значений для анализа печени.

    Возвращает:
    ReplyKeyboardMarkup: Клавиатура с кнопками, описывающими различные диапазоны значений.

    Кнопки:
    - '< 20'
    - '20 - 32'
    - '33 - 101'
    - '102 - 204'
    - '> 204'

    Клавиатура настроена с параметрами:
    - input_field_placeholder: 'Выберите ответ'
    - resize_keyboard: True (автоматическая подстройка размера клавиатуры)
    - one_time_keyboard: True (клавиатура скрывается после выбора)
    """

    # Создание списка кнопок
    key_typle = [[KeyboardButton(text=ONE)],
                 [KeyboardButton(text=TWO)],
                 [KeyboardButton(text=THREE)],
                 [KeyboardButton(text=FOUR)],
                 [KeyboardButton(text=FIVE)]]

    # Создание клавиатуры с настройками
    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Выберите ответ',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
