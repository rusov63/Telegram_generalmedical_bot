from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

SATISFACTORY = ('Удовлетворительное (соматически здоровые без системных заболеваний)')

AVERAGE = ('Средней тяжести (легкие/умеренные сист. расcтройства, связанными/не связанными с хир. забол)')

HEAVY = ('Тяжелое (выражен. сист. расстройства, которые обусловлены/не обусловлены хир. забол)')

EXTREMELY_SEVERE = ('Крайне тяжелое (системные расстройства, которые связаны/не связаны с хир. забол. '
                    'и предст.опасность для жизни б-го без опер)')

TERMINAL = ('Терминальное (с выраженными явлениями декомпенсации функ. жизненно важных органов при '
            'кот.ожидается смерть без/с опер.)')


def kb_patient() -> ReplyKeyboardMarkup:
    key_typle = [[KeyboardButton(text=SATISFACTORY)],
                 [KeyboardButton(text=AVERAGE)],
                 [KeyboardButton(text=HEAVY)],
                 [KeyboardButton(text=EXTREMELY_SEVERE)],
                 [KeyboardButton(text=TERMINAL)]]

    keyboard = ReplyKeyboardMarkup(keyboard=key_typle,
                                   input_field_placeholder='Оценка общего состояния больных',
                                   resize_keyboard=True, one_time_keyboard=True)

    return keyboard
