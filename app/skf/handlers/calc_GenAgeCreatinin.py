def calc_skf(gender: str, age: str, creatinin: str) -> int:
    """
    Функция рассчитывающая "Скорость клубочкой фильтрации по формуле CKD-EPI".
    Формула взята из источника: https://www.invitro.ru/analizes/for-doctors/2368/28340/
    Онлайн калькулятор для проверки результатов:
    https://boris.bikbov.ru/2013/07/21/kalkulyator-skf-rascheta-skorosti-klubochkovoy-filtratsii/
    https://www.kidney.org/professionals/kdoqi/gfr_calculator

    :return: Integer. Возвращает округленный результат по формуле.
    """
    ML_MIN = 'мл/мин/1.73м²'

    if gender not in ['женский', 'мужской']:
        return f'<b>Ошибка, повторите еще раз!</b>'

    elif age.isalpha() or int(age) >= 100 or int(age) <= 14:
        return f'<b>Ошибка, повторите еще раз!</b>'

    elif creatinin.isalpha():
        return f'<b>Ошибка, повторите еще раз!</b>'

    elif gender == 'женский':
        if int(creatinin) <= 62:
            result = round(144 * (0.993 ** int(age)) * ((int(creatinin) / 88.4) / 0.7) ** (-0.328))
            return f'Скорость клубочковой фильтрации: <b>{result} {ML_MIN}</b>'

        elif int(creatinin) > 62:
            result = round(144 * (0.993 ** int(age)) * ((int(creatinin) / 88.4) / 0.7) ** (-1.210))
            return f'Скорость клубочковой фильтрации: <b>{result} {ML_MIN}</b>'

    elif gender == 'мужской':
        if int(creatinin) <= 80:
            result = round(141 * (0.993 ** int(age)) * ((int(creatinin) / 88.4) / 0.9) ** (-0.412))
            return f'Скорость клубочковой фильтрации: <b>{result} {ML_MIN}</b>'

        elif int(creatinin) > 80:
            result = round(141 * (0.993 ** int(age)) * ((int(creatinin) / 88.4) / 0.9) ** (-1.210))
            return f'Скорость клубочковой фильтрации: <b>{result} {ML_MIN}</b>'

# gender = 'мужской'
# age = int(50)
# creatinin = int(102)

# print(calc_skf(gender, age, creatinin))
