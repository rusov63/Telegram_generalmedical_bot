from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_sofa() -> InlineKeyboardMarkup:
    """
    Создает и возвращает клавиатуру с двумя кнопками:
    1. "На стартовую" - с callback_data '/start'
    2. "Вернуться назад" - с callback_data '/sofa'

    Эта клавиатура может быть использована для навигации пользователя
    в боте, позволяя ему вернуться на главную страницу или перейти
    обратно к предыдущему меню.

    :return: InlineKeyboardMarkup: Объект клавиатуры с двумя кнопками.
    """
    inline_main = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🚀 На стартовую', callback_data='/start')],
        [InlineKeyboardButton(text='🔙 Вернуться назад', callback_data='/sofa')]
    ])

    return inline_main