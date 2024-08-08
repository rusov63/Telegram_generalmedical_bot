from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ONE = ('Потенцированная местная')

TWO = ('Регионарная или общая с самостоятельным дыханием')

THREE = ('Стандартные варианты комб. эндотрахеального наркоза или ТВВА')

FOUR = ('Комбинированная эндотрахеальная + регионарная или + интенс.тер.')

FIVE = ('Эндотрахеальная комбинированная + спец. методы (ИК, ГБО)')


def kb_character() -> ReplyKeyboardMarkup:
    key_typle = [[KeyboardButton(text=ONE)],
                 [KeyboardButton(text=TWO)],
                 [KeyboardButton(text=THREE)],
                 [KeyboardButton(text=FOUR)],
                 [KeyboardButton(text=FIVE)]]

    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Оценка характера анестезии',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
