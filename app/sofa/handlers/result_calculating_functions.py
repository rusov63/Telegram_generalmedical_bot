from functools import lru_cache


@lru_cache(maxsize=5)
def total_result_functions(total_PaoFio, total_respiratory,
                           total_platelet, total_liver,
                           total_kidney, total_hypotension,
                           total_EyeVerbalMotor):
    """
    Вычисляет общий результат на основе значений различных функций организма.

    :param total_PaoFio: Значение функции PAO/FIO (float или int).
    :param total_respiratory: Значение респираторной функции (float или int).
    :param total_platelet: Значение функции тромбоцитов (float или int).
    :param total_liver: Значение функции печени (float или int).
    :param total_kidney: Значение функции почек (float или int).
    :param total_hypotension: Значение функции гипотензии (float или int).
    :param total_EyeVerbalMotor: Значение функции глазного, вербального и моторного ответа (float или int).

    :return: Строка с общим количеством баллов и соответствующей оценкой смертности.
       """
    # if total_PaoFio is None or not isinstance(total_PaoFio, (int, float)):
    #     return f'<b>Ошибка, повторите еще раз!</b>'

    total_functions = int(total_PaoFio + total_respiratory +
                          total_platelet + total_liver +
                          total_kidney + total_hypotension +
                          total_EyeVerbalMotor)



    if 0 <= total_functions <= 6:
        points = f'<b>Баллов: {total_functions} \nСмертность: &lt; 10%</b>'

    elif 7 <= total_functions <= 9:
        points = f'<b>Баллов: {total_functions} \nСмертность: 15-20%</b>'

    elif 10 <= total_functions <= 12:
        points = f'<b>Баллов: {total_functions} \nСмертность: 40-50%</b>'

    elif 13 <= total_functions <= 14:
        points = f'<b>Баллов: {total_functions} \nСмертность: 50-60%</b>'

    elif total_functions == 15:
        points = f'<b>Баллов: {total_functions} \nСмертность: &gt; 80%</b>'

    elif 16 <= total_functions <= 24:
        points = f'<b>Баллов: {total_functions} \nСмертность: &gt; 90%</b>'

    return f'{points}'

#  При сумме баллов не более 12 предполагаются множественные органные дисфункции,
#  13—17 баллов — предполагается переход дисфункции в недостаточность,
#  сумма баллов около 24 указывает на высокую вероятность летального исхода.
