from functools import lru_cache


@lru_cache(maxsize=2)
def calculation_respiratory(respiratory):
    """
    Функция предназначена для вычисления количества очков на основе ответа
    пользователя.
    :param respiratory представляет собой ответ пользователя str
    :return: Если пользователь вводит 'Да', функция присваивает переменной points значение 1.
    Если пользователь вводит 'Нет', функция присваивает переменной points значение 0.
    В конце функция возвращает значение переменной points.
    """

    if respiratory == 'Да':
        points = 1
    elif respiratory == 'Нет':
        points = 0
    # else:
    #     raise ValueError("Некорректный ввод: введите 'Да' или 'Нет'")
    return points


# total = calculation_respiratory('Да')
# print(total)