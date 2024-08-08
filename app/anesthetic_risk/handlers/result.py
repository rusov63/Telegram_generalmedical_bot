def print_result(operate_patient, operate_operation, operate_character) -> str:
    """
    Функция принимающая три аргумента (функции), складывает и возвращает итоговый результат.
    :return: None or integer. Выводит общую сумму баллов.
    """
    patient_score = operate_patient
    operation_score = operate_operation
    character_score = operate_character

    if patient_score == None or operation_score == None or character_score == None:
        return f'<b>Ошибка, повторите еще раз!</b>'

    total = int(patient_score + operation_score + character_score)

    if total <= 1.5:
        return f'<b>Степень риска: I (незначительная)</b>'
    elif 2 <= total <= 3:
        return f'<b>Степень риска: II (умеренная)</b>'
    elif 3.5 <= total <= 5:
        return f'<b>Степень риска: III (значительная)</b>'
    elif 5.5 <= total <= 8:
        return f'<b>Степень риска: IV (высокая)</b>'
    elif 8.5 <= total <= 12:
        return f'<b>Степень риска: V (крайне высокая)</b>'