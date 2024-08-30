from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# четыре строки, каждая из которых описывает уровень реакции
ONE = ('Открывает самопроизвольно, наблюдает')

TWO = ('Открывает, в ответ на голос')

THREE = ('Открывает, как реакция на болевое раздражение')

FOUR = ('Не открывает')



def kb_eye() -> ReplyKeyboardMarkup:
    """
    Функция для создания клавиатуры с кнопками, представляющими уровни реакции глаз.

    Возвращает:
    ReplyKeyboardMarkup: Клавиатура с кнопками, описывающими различные уровни реакции глаз.

    Кнопки:
    - 'Открывает самопроизвольно, наблюдает'
    - 'Открывает, в ответ на голос'
    - 'Открывает, как реакция на болевое раздражение'
    - 'Не открывает'

    Клавиатура настроена с параметрами:
    - input_field_placeholder: 'Выберите ответ'
    - resize_keyboard: True (автоматическая подстройка размера клавиатуры)
    - one_time_keyboard: True (клавиатура скрывается после выбора)
    """
    key_typle = [[KeyboardButton(text=ONE)],
                 [KeyboardButton(text=TWO)],
                 [KeyboardButton(text=THREE)],
                 [KeyboardButton(text=FOUR)]]

    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Выберите ответ',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
