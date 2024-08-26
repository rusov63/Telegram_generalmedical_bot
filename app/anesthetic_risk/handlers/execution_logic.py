# Классификация операционно-анестезиологического риска
# Таблица и общая информация взята:
# https://anest-rean.ru/international-scale/mnoar-classification/


def get_operate_patient(patient: str) -> int or float:
    """
    Функция принимает от пользователя ответ (data['patient']),
    сравнивает по условию и возвращает балл
    :param patient: string data['patient'] (def start_Read_user_dataPatient)
    :return: integer or float
    """
    if patient[:5] == 'удовл':
        return 0.5
    elif patient[:5] == 'средн':
        return 1
    elif patient[:5] == 'тяжел':
        return 2
    elif patient[:5] == 'крайн':
        return 4
    elif patient[:5] == 'терми':
        return 6


def get_operate_operation(operation: str) -> int or float:
    """
    Функция принимает от пользователя ответ (data['operation']),
    сравнивает по условию и возвращает балл
    :param operation: string data['operation'] (def read_user_dataOperation)
    :return: integer or float
    """
    if operation[:5] == 'малые':
        return 0.5
    elif operation[:5] == 'более':
        return 1
    elif operation[:5] == 'обшир':
        return 1.5
    elif operation[:5] == 'серде':
        return 2
    elif operation[:5] == 'опера':
        return 2.5


def get_operate_character(character: str) -> int or float:
    """
    Функция принимает от пользователя ответ (data['character']),
    сравнивает по условию и возвращает балл
    :param character: string data['character'] (def read_user_dataCharacter)
    :return: integer or float
    """
    if character[:5] == 'потен':
        return 0.5
    elif character[:5] == 'регио':
        return 1
    elif character[:5] == 'станд':
        return 1.5
    elif character[:5] == 'комби':
        return 2
    elif character[:5] == 'эндот':
        return 2.5

# def print_result(patient: int or float, operation: int or float, character: int or float):
#     """
#     Функция принимающая три параметра, складывает и возвращает итоговый результат
#     :param patient, operation, character:  None or integer or float
#     :return: None or integer. Выводит общую сумму баллов.
#     """
#     if patient == None or operation == None or character == None:
#         return f'<b>Ошибка, повторите!</b>'
#
#     total = int(patient + operation + character)
#
#     if total <= 1.5: return f'<b>Степень риска: I (незначительная)</b>'
#     elif 2 <= total <= 3: return f'<b>Степень риска: II (умеренная)</b>'
#     elif 3.5 <= total <= 5: return f'<b>Степень риска: III (значительная)</b>'
#     elif 5.5 <= total <= 8: return f'<b>Степень риска: IV (высокая)</b>'
#     elif 8.5 <= total <= 12: return f'<b>Степень риска: V (крайне высокая)</b>'

# patient = 'средней тяжести (больные с легкими/умеренными сист. расcтройствами, связанными/не связанными с хир. забол)'
# total_PatientOperationCharacter(get_patient(patient))