import asyncio

from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold, hitalic

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums import ChatAction

from app.blood_donor.database.get_table import get_table_donor

from aiogram.filters import Command

from app.blood_donor.handlers.check_correct import СheckСorrectPhenotype
from app.blood_donor.inline_kb_donor import inline_donor
from config import bot

donor_router = Router()


class Reg(StatesGroup):
    """
    Создаем состояние FSM context. Сбор информации от пользователя.
    """
    phenotype = State()  # фенотип


@donor_router.message(Command('donor'))
async def cmd_donor(message: types.Message, state: FSMContext):
    """
     Обрабатывает команду /donor.

     Эта функция устанавливает состояние FSMContext для сбора информации
     о фенотипе реципиента. При получении команды /donor, бот очищает
     текущее состояние и запрашивает у пользователя ввод фенотипа.

     :param:
     message (types.Message): Сообщение, содержащее команду /donor.
     state (FSMContext): Контекст состояния для управления состоянием
     пользователя в процессе взаимодействия с ботом.

     :return:
     None: Функция не возвращает значения, но отправляет сообщение
     пользователю с просьбой ввести фенотип.
     """
    await state.clear()  # автоматический сброс закрытие сценария заполнения.

    await state.set_state(Reg.phenotype)  # установлено состояние.

    await message.answer(f'{hbold("Введите фенотип реципиента: ")}\n'
                         f'{hitalic("Например: CcDee, CwCDee, ccddee")}')


@donor_router.callback_query(F.data == '/donor')
async def start_callback(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик колбэков для команды '/donor'.

    Эта функция вызывается, когда пользователь нажимает на кнопку, связанную с командой '/donor'.
    Она очищает текущее состояние FSMContext и устанавливает новое состояние для сбора информации о фенотипе реципиента.
    Затем отправляет пользователю сообщение с просьбой ввести фенотип, а также пример корректного ввода.

    :param:
    - callback: CallbackQuery - объект, содержащий информацию о колбэке.
    - state: FSMContext - контекст состояния для управления состоянием пользователя.
    """
    await state.clear()  # автоматический сброс закрытие сценария заполнения.

    await state.set_state(Reg.phenotype)  # установлено состояние.

    await callback.message.answer(f'{hbold("Введите фенотип реципиента: ")}\n'
                                  f'{hitalic("Например: CcDee, CwCDee, ccddee")}')
    await callback.answer(f'Подбор донора крови')


@donor_router.message(F.text, Reg.phenotype)
async def operate_with_data(message: types.Message, state: FSMContext):
    """
    Обрабатывает введенные пользователем данные о фенотипе реципиента.

    Эта функция выполняет следующие действия:
    1. Отображает действие "печатает" в чате, чтобы показать пользователю, что бот обрабатывает запрос.
    2. Проверяет корректность введенного фенотипа с помощью функции `СheckСorrectPhenotype`.
    3. Если фенотип некорректен, отправляет пользователю сообщение с просьбой ввести корректный фенотип.
    4. Если фенотип корректен, сохраняет его в состоянии и извлекает данные из базы данных о донорах.
    5. Отправляет пользователю информацию о подходящих донорах.
    6. Очищает состояние FSM, чтобы подготовить бота к следующему запросу.
    7. Предлагает пользователю выбрать следующее действие через меню.

    :param message: Объект сообщения, содержащий текст, введенный пользователем.
    :param state: Контекст состояния FSM, используемый для хранения данных между сообщениями.
    """
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)  # отображает то, что бот печатает.
    await asyncio.sleep()  # время отображения ответа бота.

    # проверяем корректность введенных значений от пользователя
    user = СheckСorrectPhenotype(message.text)
    if user is None:
        await message.reply(f'<b>Введите корректный фенотип!</b>')
        return

    await state.update_data(phenotype=message.text)  # сохраняет введенное пользователем значение phenotype

    data = await state.get_data()

    # получение значения phenotype из базы данных
    recipient = await get_table_donor(data['phenotype'])

    # Вывод результата пользователю
    await message.answer(f'{recipient}')

    await state.clear()  # автоматический сброс закрытие сценария заполнения.

    # Меню: на стартовую страницу или вернуться назад
    await message.answer(f'Выберите действие: ', reply_markup=inline_donor())