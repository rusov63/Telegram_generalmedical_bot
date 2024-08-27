from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# четыре строки, каждая из которых описывает уровень реакции
ONE = ('Открывает самопроизвольно, наблюдает')

TWO = ('Открывает, в ответ на голос')

THREE = ('Открывает, как реакция на болевое раздражение')

FOUR = ('Не открывает')



def kb_eye() -> ReplyKeyboardMarkup:
    """
    Функция предназначена для создания клавиатуры с кнопками,
    которые представляют различные варианты реакции глаз. Она используется в контексте бота.

    :return: Возвращает созданный объект клавиатуры, который может быть использован для отправки пользователю.
    """
    key_typle = [[KeyboardButton(text=ONE)],
                 [KeyboardButton(text=TWO)],
                 [KeyboardButton(text=THREE)],
                 [KeyboardButton(text=FOUR)]]

    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Выберите ответ',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
