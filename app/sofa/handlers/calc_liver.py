# ONE = ('< 20')
# TWO = ('20 - 32')
# THREE = ('33 - 101')
# FOUR = ('102 - 204')
# FIVE = ('> 204')

def calculation_liver(user: str) -> int:
    """
    Функция сначала извлекает все числовые символы из строки user и объединяет их в одно целое число.
    Это достигается с помощью генератора списков и метода join. Например, если входная строка равна '> 204',
    то функция извлечет 204.
    :param user: принимает строку user в качестве аргумента и возвращает целое число
    :return: Функция возвращает рассчитанное количество баллов в зависимости от количества
    """
    total = int(''.join([i for i in user if i.isnumeric()]))

    if total == 20:
        points = 0
    elif total == 2032:
        points = 1
    elif total == 33101:
        points = 2
    elif total == 102204:
        points = 3
    elif total == 204:
        points = 4
    else:
        points = 0

    return points


# total = calculation_liver('> 204')
# print(total)