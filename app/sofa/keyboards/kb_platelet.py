from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Определение текстов для кнопок
ONE = ('> 151')

TWO = ('<= 150')

THREE = ('<= 100')

FOUR = ('<= 50')

FIVE = ('<= 20')


def kb_platelet() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для выбора уровня тромбоцитов.

    Эта функция формирует клавиатуру с пятью кнопками, каждая из которых
    соответствует определенному диапазону значений тромбоцитов. Клавиатура
    предназначена для использования в чат-боте на платформе Telegram и
    позволяет пользователю выбрать один из предложенных вариантов.

    Возвращает:
        ReplyKeyboardMarkup: Клавиатура с кнопками для выбора уровня тромбоцитов.
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
