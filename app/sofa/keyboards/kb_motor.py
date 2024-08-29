from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ONE = ('Выполнение движений по голосовой команде')

TWO = ('Локализует боль, пытается её избежать')

THREE = ('Бессмысленные движения в ответ на боль')

FOUR = ('Патологическое сгибание в ответ на боль (декортикационная ригидность)')

FIVE = ('Патологическое разгибание в ответ на боль (децеребрационная ригидность)')

SIX = ('Не двигается')



def kb_motor() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру с кнопками, представляющими различные уровни реакции на болевое раздражение.

    Уровни реакции:
    1. Выполнение движений по голосовой команде
    2. Локализует боль, пытается её избежать
    3. Бессмысленные движения в ответ на боль
    4. Патологическое сгибание в ответ на боль (декортикационная ригидность)
    5. Патологическое разгибание в ответ на боль (децеребрационная ригидность)
    6. Не двигается

    Возвращает:
        ReplyKeyboardMarkup: Клавиатура с кнопками для выбора уровня реакции.
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
