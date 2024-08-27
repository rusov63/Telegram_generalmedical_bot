from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ONE = ('Выполнение движений по голосовой команде')

TWO = ('Локализует боль, пытается её избежать')

THREE = ('Бессмысленные движения в ответ на боль')

FOUR = ('Патологическое сгибание в ответ на боль (декортикационная ригидность)')

FIVE = ('Патологическое разгибание в ответ на боль (децеребрационная ригидность)')

SIX = ('Не двигается')



def kb_motor() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для выбора ответа.

    Клавиатура будет иметь поле ввода с подсказкой 'Выберите ответ' и будет автоматически изменять
    размер в зависимости от количества кнопок.
    :return: ReplyKeyboardMarkup: Клавиатура с кнопками, представляющими различные реакции:
        - Выполнение движений по голосовой команде
        - Локализует боль, пытается её избежать
        - Бессмысленные движения в ответ на боль
        - Патологическое сгибание в ответ на боль (декортикационная ригидность)
        - Патологическое разгибание в ответ на боль (децеребрационная ригидность)
        - Не двигается
    """
    key_typle = [[KeyboardButton(text=ONE)],
                 [KeyboardButton(text=TWO)],
                 [KeyboardButton(text=THREE)],
                 [KeyboardButton(text=FOUR)],
                 [KeyboardButton(text=FIVE)],
                 [KeyboardButton(text=SIX)]]

    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Выберите ответ',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
