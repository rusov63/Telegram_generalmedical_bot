from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ONE = ('Нет гипотензии')

TWO = ('АДср < 70 мм.рт.ст.')

THREE = ('Допамин <= 5 или любая доза добутамина')

FOUR = ('Допамин > 5 или адреналин <= 0.1 или НА <= 0.1')

FIVE = ('Допамин > 15 или адреналин > 0.1 или НА > 0.1')


def kb_hypotension() -> ReplyKeyboardMarkup:
    key_typle = [[KeyboardButton(text=ONE)],
                 [KeyboardButton(text=TWO)],
                 [KeyboardButton(text=THREE)],
                 [KeyboardButton(text=FOUR)],
                 [KeyboardButton(text=FIVE)]]

    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Выберите ответ',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
