# Классификации операционно-анастезиологического риска MHOAP-89
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from app.anesthetic_risk.handlers.execution_logic import (get_operate_patient, get_operate_operation,
                                                          get_operate_character)
from app.anesthetic_risk.handlers.result import print_result

from app.anesthetic_risk.keyboards.keyboard_oper import kb_operation
from app.anesthetic_risk.keyboards.keyboard_pat import kb_patient
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
    """
    await state.set_state(Reg.patient)  # Установка состояния Reg.patient.

    await message.answer(f'Выбрали: оценка операционно-анестезиологического риска (MHOAP-89)')
    await message.answer(f'Выберите состояние больного: ', reply_markup=kb_patient())


@anesthesia_router.message(Reg.patient)
async def read_user_dataOperation(message: types.Message, state: FSMContext):
    await state.update_data(patient=message.text.lower())  # сохраняем результат.

    await state.set_state(Reg.operation)  # Установка состояния Reg.operation.
    await message.answer(f'Выберите характер операции: ', reply_markup=kb_operation())


@anesthesia_router.message(Reg.operation)
async def read_user_dataCharacter(message: types.Message, state: FSMContext):
    await state.update_data(operation=message.text.lower())  # сохраняем результат.
    await state.set_state(Reg.character)

    await message.answer(f'Выберите характер анастезии: ', reply_markup=kb_character())


@anesthesia_router.message(Reg.character)
async def save_data_user(message: types.Message, state: FSMContext):
    await state.update_data(character=message.text.lower())
    data = await state.get_data()

    # Получение данных от пользователя и возврат результата
    total_result = print_result(get_operate_patient(data['patient']),
                                get_operate_operation(data['operation']),
                                get_operate_character(data['character']))

    await message.answer(f'{total_result}')

    await message.answer(f'Для возврата запустите команду:  /anesthetic_risk \n'
                         f'или воспользуйтесь меню')

    await state.clear()  # очистка состояния.
