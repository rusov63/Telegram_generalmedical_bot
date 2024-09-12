import time
from functools import lru_cache


@lru_cache(maxsize=3)
def calc_skf(gender: str, age: str, creatinin: str) -> int:
    """
    Функция рассчитывающая "Скорость клубочковой фильтрации по формуле CKD-EPI".

    Данная функция принимает пол, возраст и уровень креатинина пользователя и
    вычисляет скорость клубочковой фильтрации (СКФ) по формуле CKD-EPI.
    Формула учитывает различия в расчетах для мужчин и женщин, а также
    диапазоны значений креатинина. Результат возвращается в виде округленного
    значения, выраженного в мл/мин/1.73м².

    Формула взята из источника: https://www.invitro.ru/analizes/for-doctors/2368/28340/
    Онлайн калькулятор для проверки результатов:
    https://boris.bikbov.ru/2013/07/21/kalkulyator-skf-rascheta-skorosti-klubochkovoy-filtratsii/
    https://www.kidney.org/professionals/kdoqi/gfr_calculator

    :param gender: Пол пользователя ('мужской' или 'женский').
    :param age: Возраст пользователя в годах.
    :param creatinin: Уровень креатинина в мкмоль/л.
    :return: Integer. Возвращает округленный результат по формуле.
    Кэширование:
    Функция использует декоратор '@lru_cache' для кэширования результатов.
    Это означает, что если функция вызывается с теми же аргументами,
    результат будет возвращен из кэша, что ускоряет выполнение и
    уменьшает количество вычислений. Максимальный размер кэша установлен
    на 3, что позволяет хранить результаты трех последних уникальных
    вызовов функции.
    """

    ML_MIN = 'мл/мин/1.73м²'

    if gender in ('женский', 'жен'):
        if int(creatinin) <= 62:
            result = round(144 * (0.993 ** int(age)) * ((int(creatinin) / 88.4) / 0.7) ** (-0.328))
            return f'Скорость клубочковой фильтрации: <b>{result} {ML_MIN}</b>'

        elif int(creatinin) > 62:
            result = round(144 * (0.993 ** int(age)) * ((int(creatinin) / 88.4) / 0.7) ** (-1.210))
            return f'Скорость клубочковой фильтрации: <b>{result} {ML_MIN}</b>'

    elif gender in ('мужской', 'муж'):
        if int(creatinin) <= 80:
            result = round(141 * (0.993 ** int(age)) * ((int(creatinin) / 88.4) / 0.9) ** (-0.412))
            return f'Скорость клубочковой фильтрации: <b>{result} {ML_MIN}</b>'

        elif int(creatinin) > 80:
            result = round(141 * (0.993 ** int(age)) * ((int(creatinin) / 88.4) / 0.9) ** (-1.210))
            return f'Скорость клубочковой фильтрации: <b>{result} {ML_MIN}</b>'

# gender = ('женский')
# age = int(78)
# creatinin = int(-1)
#
# start_time = time.perf_counter()
#print(calc_skf(gender, age, creatinin))
# end_time = time.perf_counter()
#
# print(f"Время выполнения: {end_time - start_time:.8f} seconds")
# print(calc_skf.cache_info())