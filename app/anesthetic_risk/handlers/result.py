def print_result(operate_patient, operate_operation, operate_character) -> str:
    """
    Вычисляет степень риска на основе трех параметров:
    состояние пациента, операция и характер операции.

    :param
    operate_patient (float или int): Оценка состояния пациента.
    operate_operation (float или int): Оценка операции.
    operate_character (float или  int): Оценка характера операции.

    :return Строка с сообщением о степени риска.
    """

    total = int(operate_patient + operate_operation + operate_character)

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
