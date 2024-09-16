# Классификации операционно-анастезиологического риска MHOAP-89
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery

from app.anesthetic_risk.handlers.execution_logic import (get_operate_patient, get_operate_operation,
                                                          get_operate_character)

from app.anesthetic_risk.handlers.check_correct_values import (check_correct_valuesOperation, check_correct_valuesPatient,
                                                               check_correct_valuesCharacter)

from app.anesthetic_risk.handlers.result import print_result
from app.anesthetic_risk.keyboards.inline_kb_anesthetic import inline_anest

from app.anesthetic_risk.keyboards.keyboard_operation import kb_operation
from app.anesthetic_risk.keyboards.keyboard_patient import kb_patient
from app.anesthetic_risk.keyboards.keyboards_character import kb_character

anesthesia_router = Router()


class Reg(StatesGroup):
    """
    Создаем состояние FSM context. Сбор информации от пользователя.
    """
    patient = State()  # Состояние больного.
    operation = State()  # хирургическая операция.
    character = State()  # характер анастезии.


@anesthesia_router.message(Command('anesthetic_risk'))
async def start_Read_user_dataPatient(message: types.Message, state: FSMContext):
    """
    Команда /anesthetic_risk. Начало ввода запрашиваемой информации от пользователя.

    Данная функция:
    - Очищает состояние FSM контекста.
    - Устанавливает состояние Reg.patient для сбора информации о состоянии пациента.
    - Отправляет сообщение пользователю с выбором состояния больного и соответствующей клавиатурой.
    """
    await state.clear()  # Очистка состояния!

    await state.set_state(Reg.patient)  # Установка состояния Reg.patient.

    await message.answer(f'Выбрали: Оценка операционно-анестезиологического риска (MHOAP-89)')
    await message.answer(f'Выберите состояние больного: ', reply_markup=kb_patient())


@anesthesia_router.callback_query(F.data == '/anesthetic_risk')
async def start_callbacks(callback: CallbackQuery, state: FSMContext):
    """
     Обработчик callback-запроса для команды /anesthetic_risk.

     Данная функция выполняется, когда пользователь нажимает на кнопку, связанную с командой /anesthetic_risk.
     Она очищает текущее состояние FSM контекста и устанавливает новое состояние Reg.patient.
     Затем отправляет сообщение пользователю с информацией о выбранной оценке операционно-анестезиологического риска (MHOAP-89)
     и предлагает выбрать состояние пациента из предопределенных вариантов, используя клавиатуру 'kb_patient()'.

     :arg:
         callback (CallbackQuery): Объект callback-запроса, содержащий информацию о нажатой кнопке.
         state (FSMContext): Контекст конечного автомата состояний (Finite State Machine),
         используемый для управления состоянием диалога.

     :return None
     """
    await state.clear()  # Очистка состояния!

    await state.set_state(Reg.patient)  # Установка состояния Reg.patient.

    await callback.message.answer(f'Выбрали: оценка операционно-анестезиологического риска (MHOAP-89)')
    await callback.answer(f'Оценка опер. анестезиологического риска')
    await callback.message.answer(f'Выберите состояние больного: ', reply_markup=kb_patient())


@anesthesia_router.message(F.text, Reg.patient)
async def read_user_dataOperation(message: types.Message, state: FSMContext):

    # проверяем на корректность введенных значений
    user = check_correct_valuesPatient(message.text)
    if user is None:
        await message.reply(f'<b>Выберите корректное значение из предложенного!</b>', reply_markup=kb_patient())
        return

    await state.update_data(patient=message.text.lower())  # сохраняем результат.
    await state.set_state(Reg.operation)  # Установка состояния Reg.operation.

    await message.answer(f'Выберите характер операции: ', reply_markup=kb_operation())


@anesthesia_router.message(F.text,Reg.operation)
async def read_user_dataCharacter(message: types.Message, state: FSMContext):

    # проверяем на корректность введенных значений
    user = check_correct_valuesOperation(message.text)
    if user is None:
        await message.reply(f'<b>Выберите корректное значение из предложенного!</b>', reply_markup=kb_operation())
        return

    await state.update_data(operation=message.text.lower())  # сохраняем результат.
    await state.set_state(Reg.character)

    await message.answer(f'Выберите характер анастезии: ', reply_markup=kb_character())


@anesthesia_router.message(Reg.character)
async def save_data_user(message: types.Message, state: FSMContext):

    # проверяем на корректность введенных значений
    user = check_correct_valuesCharacter(message.text)
    if user is None:
        await message.reply(f'<b>Выберите корректное значение из предложенного!</b>', reply_markup=kb_character())
        return

    await state.update_data(character=message.text.lower())
    data = await state.get_data()

    # Получение сохраненных данных (FSM) и возврат результата
    total_result = print_result(get_operate_patient(data['patient']),
                                get_operate_operation(data['operation']),
                                get_operate_character(data['character']))

    # вывод значения
    await message.answer(f'{total_result}')

    await state.clear()  # очистка состояния.

    # Меню: на стартовую страницу или вернуться назад
    await message.answer(f'Выберите действие: ', reply_markup=inline_anest())