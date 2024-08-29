from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ONE = ('Ориентирован и контактен (осмысленный ответ)')

TWO = ('Произносит фразы, но речь бессвязная')

THREE = ('Произносит отдельные слова')

FOUR = ('Издает звуки, но не слова')

FIVE = ('Отсутствие речи')



def kb_verbal() -> ReplyKeyboardMarkup:
    """
     Создает клавиатуру с кнопками для выбора уровня вербальной реакции.

     Клавиатура содержит следующие кнопки:
     - 'Ориентирован и контактен (осмысленный ответ)': для обозначения осмысленного ответа.
     - 'Произносит фразы, но речь бессвязная': для обозначения бессвязной речи.
     - 'Произносит отдельные слова': для обозначения произнесения отдельных слов.
     - 'Издает звуки, но не слова': для обозначения издания звуков без слов.
     - 'Отсутствие речи': для обозначения полного отсутствия речи.

     Возвращает объект ReplyKeyboardMarkup, который можно использовать в сообщениях бота.
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
