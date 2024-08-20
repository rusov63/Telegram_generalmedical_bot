# Основная логика Расчета скорости клубочковой фильтрации (SKF)

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from app.skf.handlers.calc_GenAgeCreatinin import calc_skf
from app.skf.keyboard import kb_skf

skf_router = Router()


class Reg(StatesGroup):
    """
    Создаем состояние FSM context. Сбор информации от пользователя.
    """
    gender = State()  # пол.
    age = State()  # возраст.
    creatinin = State()  # креатинин.


@skf_router.message(Command('skf'))
async def cmd_skf(message: types.Message, state: FSMContext):
    """
    Команда /skf. Начало ввода запрашиваемой информации от пользователя.
    """
    await state.set_state(Reg.gender)

    await message.answer(f'Выбрали: скорость клубочковой фильтрации (CKD-EPI)')
    await message.answer(f'Выберите пол: ', reply_markup=kb_skf())


@skf_router.message(Reg.gender)
async def reg_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text.lower())
    await state.set_state(Reg.age)

    await message.answer(f'Введите возраст: ')


@skf_router.message(Reg.age)
async def reg_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Reg.creatinin)

    await message.answer(f'Введите креатинин (мкмоль/л): ')


@skf_router.message(Reg.creatinin)
async def reg_creatinin(message: types.Message, state: FSMContext):
    await state.update_data(creatinin=message.text)
    data = await state.get_data()

    # Получение данных от пользователя и возврат результата.
    total = calc_skf(data['gender'], data['age'], data['creatinin'])
    await message.answer(f'<b>{total}</b>')

    await message.answer(f'Для возврата запустите команду:  /skf \n'
                         f'или воспользуйтесь меню')

    await state.clear()