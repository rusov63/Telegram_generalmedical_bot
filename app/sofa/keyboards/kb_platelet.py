from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Определение текстов для кнопок
ONE = ('> 151')

TWO = ('<= 150')

THREE = ('<= 100')

FOUR = ('<= 50')

FIVE = ('<= 20')


def kb_platelet() -> ReplyKeyboardMarkup:
    """
    Клавиатура содержит кнопки, которые позволяют пользователю выбирать различные диапазоны значений тромбоцитов.
    :return: Функция возвращает объект ReplyKeyboardMarkup, который можно использовать для отправки клавиатуры
    пользователю в Telegram.
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
