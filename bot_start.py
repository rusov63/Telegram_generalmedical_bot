from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

user_router = Router()


@user_router.message(CommandStart())
async def command_start(message: types.Message):
    """
    Функция, которая обрабатывает команду /start, отправленную пользователем.

    :arg message (types.Message): Объект, содержащий информацию о сообщении пользователя.
    :return Ничего не возвращает, но отправляет приветственное сообщение пользователю и
    предлагает выбрать команду.
    """
    await message.reply(f'Добро пожаловать пользователь, {hbold(message.from_user.full_name)}!')

    await message.answer(f'Для начала выберите команду: ', reply_markup=inline_skf())


@user_router.callback_query(F.data == '/start')
async def command(callback: CallbackQuery):
    """
    Функция, которая обрабатывает нажатие на кнопку со ссылкой на команду /start.

    :arg callback (CallbackQuery): Объект, содержащий информацию о нажатии на кнопку.
    :return Ничего не возвращает, но отправляет сообщение с предложением выбрать команду и
    отвечает на callback.
    """
    await callback.message.answer(f'Для начала выберите команду: ', reply_markup=inline_skf())

    await callback.answer(f'Стартовая')



def inline_skf() -> InlineKeyboardMarkup:
    """
    Создает и возвращает клавиатуру с 5 кнопками:
    1. "Оценка опер. анестезиологического риска" - с callback_data '/anesthetic_risk'
    2. "Cкорость клубочковой фильтрации" - с callback_data '/skf'
    3. "Подбор донора крови" - с callback_data '/donor'
    4. "Шкала SOFA" - с callback_data '/sofa'
    5. "Обратная связь" - с callback_data 'Обратная связь'

    Эта клавиатура может быть использована для навигации пользователя в боте
    :return InlineKeyboardMarkup: Объект клавиатуры с 5 кнопками.
    """

    inline_main = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='💉 Оценка опер. анестезиологического риска', callback_data='/anesthetic_risk')],
        [InlineKeyboardButton(text='💦 Cкорость клубочковой фильтрации', callback_data='/skf')],
        [InlineKeyboardButton(text='🩸 Подбор донора крови', callback_data='/donor')],
        [InlineKeyboardButton(text='🧟 Шкала SOFA', callback_data='/sofa')],
        [InlineKeyboardButton(text='📌 Обратная связь', callback_data='Обратная связь')]
    ])

    return inline_main

