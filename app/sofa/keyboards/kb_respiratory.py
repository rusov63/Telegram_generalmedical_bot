from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ONE = ('Да')

TWO = ('Нет')



def kb_respiratory() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для выбора ответа на вопрос о респираторной функции.

    Клавиатура содержит две кнопки:
    - 'Да': для подтверждения положительного ответа.
    - 'Нет': для подтверждения отрицательного ответа.

    Возвращает объект ReplyKeyboardMarkup, который можно использовать в сообщениях бота.
    """
    key_typle = [[KeyboardButton(text=ONE)],
                 [KeyboardButton(text=TWO)]]

    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Выберите ответ',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
