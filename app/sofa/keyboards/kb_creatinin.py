from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Определение текстов для кнопок
ONE = ('< 110')

TWO = ('110 - 170')

THREE = ('171 - 299')

FOUR = ('300 - 440 или диурез <500 мл в сутки')

FIVE = ('> 440 или < 200 мл мочи/сутки')


def kb_creatinin() -> ReplyKeyboardMarkup:
    """
    Функция для создания клавиатуры "Креатинин" с кнопками для выбора диапазонов значений.

    Возвращает:
    ReplyKeyboardMarkup: Клавиатура с кнопками, представляющими различные диапазоны значений.

    Кнопки:
    - '< 110'
    - '110 - 170'
    - '171 - 299'
    - '300 - 440 или диурез <500 мл в сутки'
    - '> 440 или < 200 мл мочи/сутки'

    Клавиатура настроена с параметрами:
    - input_field_placeholder: 'Выберите ответ'
    - resize_keyboard: True (автоматическая подстройка размера клавиатуры)
    - one_time_keyboard: True (клавиатура скрывается после выбора)
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