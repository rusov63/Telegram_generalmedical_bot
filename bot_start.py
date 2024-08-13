from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold

user_router = Router()

@user_router.message(CommandStart())
async def command_start(message: types.Message):
    """
    Стартовая страница, команда /Start.
    """
    await message.reply(f'Добро пожаловать пользователь, {hbold(message.from_user.full_name)}!')
    await message.answer(f'Для начала выберите команду: \n'
                         f'{hbold(' 🩺 Оценка операционно - анестезиологического риска: \n /anesthetic_risk')} \n'
                         f'\n'
                         f'{hbold(' 💦 Cкорость клубочковой фильтрации:  /skf')} \n'
                         f'\n'
                         f'{hbold(' 🩸 Подбор донора крови:  /donor')} \n'
                         f'\n'
                         f'{hbold(' 💉 Скорость инфузии: в разработке')} \n')