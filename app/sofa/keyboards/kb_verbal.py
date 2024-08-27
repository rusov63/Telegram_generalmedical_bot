from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ONE = ('Ориентирован и контактен (осмысленный ответ)')

TWO = ('Произносит фразы, но речь бессвязная')

THREE = ('Произносит отдельные слова')

FOUR = ('Издает звуки, но не слова')

FIVE = ('Отсутствие речи')



def kb_verbal() -> ReplyKeyboardMarkup:
    """
    Предназначена для создания клавиатуры с кнопками, которые представляют
    различные варианты вербальной реакции пользователя.
    :return: Функция возвращает созданную клавиатуру, которая может быть использована в сообщениях бота.
    """
    key_typle = [[KeyboardButton(text=ONE)],
                 [KeyboardButton(text=TWO)],
                 [KeyboardButton(text=THREE)],
                 [KeyboardButton(text=FOUR)],
                 [KeyboardButton(text=FIVE)]]

    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Выберите ответ',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
