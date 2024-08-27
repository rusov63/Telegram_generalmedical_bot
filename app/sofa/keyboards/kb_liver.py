from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Определение текстов для кнопок
ONE = ('< 20')
TWO = ('20 - 32')
THREE = ('33 - 101')
FOUR = ('102 - 204')
FIVE = ('> 204')


def kb_liver() -> ReplyKeyboardMarkup:
    """
    Эта клавиатура содержит кнопки, которые позволяют пользователю
    выбирать различные диапазоны значений, связанных с печенью.
    :return: Функция возвращает созданную клавиатуру, которую можно использовать в сообщениях
    бота, выбирая один из предложенных диапазонов значений.
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
