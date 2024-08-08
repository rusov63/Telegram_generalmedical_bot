from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ONE = ('Малые полостные или небольшие (операции на поверхности тела)')

TWO = ('Более сложные и длительные (операции на поверх. тела, позвоночнике, ЦНС, и внут. органах)')

THREE = ('Обширные или продолжительные (операции в различных обл хирургии, нейро, урологии, травмат, '
         'онкологии)')

FOUR = ('Сердечно-сосудистые без ИК')

FIVE = ('Операции с ИК или пересадки внутр. орг')


def kb_operation() -> ReplyKeyboardMarkup:
    key_typle = [[KeyboardButton(text=ONE)],
                 [KeyboardButton(text=TWO)],
                 [KeyboardButton(text=THREE)],
                 [KeyboardButton(text=FOUR)],
                 [KeyboardButton(text=FIVE)]]

    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Оценка объёма и характер операции',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
