from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

SATISFACTORY = ('Удовлетворительное (соматически здоровые без системных заболеваний)')

AVERAGE = ('Средней тяжести (легкие/умеренные системные расcтройства)')

HEAVY = ('Тяжелое (выражен. сист. расстройства, которые обусловлены/не обусловлены хир. забол)')

EXTREMELY_SEVERE = ('Крайне тяжелое (системные расстройства, кот. предст.опасность для жизни без опер)')

TERMINAL = ('Терминальное (с выраженными явлениями декомпенсации при кот.ожидается смерть)')


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
