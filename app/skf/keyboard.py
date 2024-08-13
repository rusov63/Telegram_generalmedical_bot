from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def kb_skf() -> ReplyKeyboardMarkup:
    """
    Клавиатура привязанная к функции cmd_skf (команда /skf).
    :return: ReplyKeyboardMarkup
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Женский"), KeyboardButton(text="Мужской")]],

        input_field_placeholder='Пол: Женский - Мужской', resize_keyboard=True, one_time_keyboard=True)

    return keyboard
