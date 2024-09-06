# Основная логика Расчета скорости клубочковой фильтрации (SKF)

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from app.skf.handlers.calc_GenAgeCreatinin import calc_skf
from app.skf.handlers.get_gender_user import get_gender
from app.skf.handlers.get_number_user import get_answer_age_creatinin
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
    Обрабатывает команду /skf и инициирует процесс ввода данных для
    расчета скорости клубочковой фильтрации (СКФ).

    Параметры:
    - message (types.Message): Сообщение, отправленное пользователем,
      содержащие команду /skf.
    - state (FSMContext): Контекст состояния, используемый для хранения
      и управления состоянием пользователя в процессе ввода данных.

    Описание:
    Функция отправляет пользователю сообщение о начале процесса
    расчета скорости клубочковой фильтрации для взрослых по формуле
    CKD-EPI. Затем запрашивает у пользователя выбор пола, предоставляя
    соответствующую клавиатуру для выбора. Устанавливает состояние
    Reg.gender для ожидания ввода данных о поле пользователя.
    """
    await message.answer(f'Выбрали: скорость клубочковой фильтрации для взрослых (CKD-EPI)')

    await state.set_state(Reg.gender)  # Установка состояния Reg.gender
    await message.answer(f'Выберите пол: ', reply_markup=kb_skf())


@skf_router.message(F.text, Reg.gender)
async def reg_gender(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод пола пользователя и сохраняет его в состоянии.

    Параметры:
    - message (types.Message): Сообщение, отправленное пользователем,
      содержащее текст с указанием пола.
    - state (FSMContext): Контекст состояния, используемый для хранения
      и управления состоянием пользователя в процессе ввода данных.

    Описание:
    Функция получает текст сообщения, преобразует его в нижний регистр
    и определяет пол пользователя с помощью функции get_gender. Если
    ввод пользователя некорректен (возвращается "Ошибка"), отправляется
    сообщение с просьбой повторить ввод. В противном случае введенное
    значение пола сохраняется в состоянии, и пользователю запрашивается
    ввод возраста. Устанавливается состояние Reg.age для ожидания
    следующего ввода.
    """
    user = get_gender(message.text.lower())

    if user == "Ошибка":
        await message.reply(f'<b>Введите корректный пол!</b>')
        return

    await state.update_data(gender=message.text.lower())  # Сохраняет введенное пользователем значение пол.

    await state.set_state(Reg.age)
    await message.answer(f'Введите возраст: ')


@skf_router.message(F.text, Reg.age)
async def reg_age(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод возраста пользователя и сохраняет его в состоянии.

    Параметры:
    - message (types.Message): Сообщение, отправленное пользователем,
      содержащее текст с указанием возраста.
    - state (FSMContext): Контекст состояния, используемый для хранения
      и управления состоянием пользователя в процессе ввода данных.

    Описание:
    Функция получает текст сообщения и проверяет его на корректность
    с помощью функции get_answer_age_creatinine. Если введенное значение
    некорректно (не является числом или не находится в диапазоне от 18 до 100),
    пользователю отправляется сообщение с просьбой ввести корректный возраст.
    В противном случае введенное значение возраста сохраняется в состоянии,
    и пользователю запрашивается ввод значения креатинина. Устанавливается
    состояние Reg.creatinin для ожидания следующего ввода.
    """

    # Создаем функцию и получаем число от пользователя.
    get_check = get_answer_age_creatinin(message.text)

    # Проверяем на корректность получаемых значений
    if not get_check or not (18 <= get_check <= 100):
        await message.reply(f'Пожалуйста, введите корректный возраст (от 18 до 100)!')
        return

    # Сохраняет введенное пользователем значение возраст.
    await state.update_data(age=message.text)

    await message.answer(f'Введите креатинин (мкмоль/л): ')
    await state.set_state(Reg.creatinin)


@skf_router.message(F.text, Reg.creatinin)
async def reg_creatinin(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод значения креатинина пользователя и сохраняет его в состоянии.

    Параметры:
    - message (types.Message): Сообщение, отправленное пользователем,
      содержащее текст с указанием значения креатинина.
    - state (FSMContext): Контекст состояния, используемый для хранения
      и управления состоянием пользователя в процессе ввода данных.

    Описание:
    Функция получает текст сообщения и проверяет его на корректность
    с помощью функции get_answer_age_creatinine. Если введенное значение
    некорректно (не является числом или не находится в диапазоне от 0 до 2000),
    пользователю отправляется сообщение с просьбой ввести корректное значение креатинина.
    В противном случае введенное значение креатинина сохраняется в состоянии,
    извлекаются данные о поле и возрасте пользователя, и выполняется расчет
    скорости клубочковой фильтрации с помощью функции calc_skf.
    Результат расчета отправляется пользователю, а затем состояние очищается
    для подготовки к следующему вводу.
    """

    # Создаем функцию и получаем число от пользователя.
    get_check = get_answer_age_creatinin(message.text)

    # Проверяем на корректность получаемых значений
    if not get_check or not (0 <= get_check <= 2000):
        await message.reply(f'Пожалуйста, введите корректный креатинин (от 0 до 2000)')
        return

    # Сохраняет введенное пользователем значение креатинин
    await state.update_data(creatinin=message.text)

    # извлекаем данные полученные от пользователя: пол, возраст, креатинин.
    data = await state.get_data()

    # Расчет результата.
    total = calc_skf(data['gender'], data['age'], data['creatinin'])

    # Распечатка полученного результата.
    await message.answer(f'{total}')

    await message.answer(f'Для возврата запустите команду:  /skf \n'
                         f'или воспользуйтесь меню')

    await state.clear()