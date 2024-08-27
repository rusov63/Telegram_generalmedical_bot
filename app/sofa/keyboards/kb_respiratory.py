from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ONE = ('Да')

TWO = ('Нет')



def kb_respiratory() -> ReplyKeyboardMarkup:
    """
    Функция kb_respiratory создает клавиатуру для бота.

    :return: Возвращает объект типа ReplyKeyboardMarkup.
    """
    key_typle = [[KeyboardButton(text=ONE)],
                 [KeyboardButton(text=TWO)]]

    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Выберите ответ',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
