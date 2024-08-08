from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# menu_keyboard = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="📖 Подбор донора крови"),
#     KeyboardButton(text="🏃‍♀️💨 Cкорость клубочковой фильтрации")],
#     [KeyboardButton(text="📝 Скорость инфузии")],
# ], input_field_placeholder='Выберите из пункта меню: ', resize_keyboard=True, one_time_keyboard=True)



# menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="📖 Подбор донора крови", callback_data='/donor')],
#     [InlineKeyboardButton(text="🏃‍♀️💨 Cкорость клубочковой фильтрации", callback_data='/skf')]
# ], input_field_placeholder = 'Выберите из пункта меню: ', resize_keyboard=True, one_time_keyboard=True)

# menu_keyboard = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="📖 О нас"), KeyboardButton(text="👤 Профиль")],
#     [KeyboardButton(text="📝 Заполнить анкету"), KeyboardButton(text="📚 Каталог")]
# ], resize_keyboard=True, one_time_keyboard=True)


# def create_spec_kb():
#     kb_list = [
#         [KeyboardButton(text="")]]
#     keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
#                                    resize_keyboard=True,
#                                    one_time_keyboard=True,
#                                    input_field_placeholder="Воспользуйтесь:")
#     return keyboard

