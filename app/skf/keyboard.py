from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


ONE = ('Женский')

TWO = ('Мужской')

def kb_skf() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру для команды /skf.

    Эта функция возвращает объект ReplyKeyboardMarkup, который содержит
    кнопки для выбора пола: 'Женский' и 'Мужской'. Клавиатура
    настроена так, чтобы быть компактной и исчезать после выбора.

    :return: Объект ReplyKeyboardMarkup с кнопками выбора пола.
    """

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Женский"), KeyboardButton(text="Мужской")]],

        input_field_placeholder='Выберите ответ', resize_keyboard=True, one_time_keyboard=True)

    return keyboard
