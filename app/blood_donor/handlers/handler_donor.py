import asyncio

from aiogram import Router, types
from aiogram.utils.markdown import hbold, hitalic

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums import ChatAction

from app.blood_donor.database.get_table import get_table_donor

from aiogram.filters import Command

from config import bot

donor_router = Router()


class Reg(StatesGroup):
    """
    Создаем состояние FSM context. Сбор информации от пользователя.
    """
    get_user = State()  # фенотип


@donor_router.message(Command('donor'))
async def cmd_donor(message: types.Message, state: FSMContext):
    """
    Команда /donor. Функция которая, устанавливает состояние FSMContext
    и задающая вопрос пользователю.
    """
    await state.set_state(Reg.get_user)  # установлено состояние.
    await bot.send_message(message.from_user.id, f'{hbold("Введите фенотип реципиента: ")}\n'
                                                 f'{hitalic("Например: CcDee, CwCDee, ccddee")}')


@donor_router.message(Reg.get_user)
async def operate_with_data(message: types.Message, state: FSMContext):
    """
    Функция, которая сохраняет ответ от пользователя - Reg.get_user,
    отправляет сохраненный ответ в функцию get_table_(БД),
    получает данные из БД и отправляет пользователю.
    """
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)  # отображает то, что бот печатает.
    await asyncio.sleep(0.3)  # время отображения ответа бота.

    await state.update_data(get_user=message.text)  # сохраняем информацию присланное пользователем.
    data = await state.get_data()  # сохраненная информация была выведена через ключ-индекс.
    recipient = await get_table_donor(data['get_user'])

    await state.clear()  # очистка состояния.

    await message.answer(f'{recipient}')

    await message.answer(f'Для возврата запустите команду:  /donor  \n'
                         f'или воспользуйтесь меню')