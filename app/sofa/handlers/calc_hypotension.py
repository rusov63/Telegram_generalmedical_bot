from functools import lru_cache
# ONE = ('Нет гипотензии')
# TWO = ('АДср < 70 мм.рт.ст.')
# THREE = ('Допамин <= 5 или любая доза добутамина')
# FOUR = ('Допамин > 5 или адреналин <= 0.1 или НА <= 0.1')
# FIVE = ('Допамин > 15 или адреналин > 0.1 или НА > 0.1')


@lru_cache(maxsize=2)
def calculate_hypotension(user):
    """
    Функция предназначена для вычисления количества очков на основе
    числовых значений, извлеченных из строки, переданной пользователем.
    :param user: Принимает один аргумент user, который представляет собой строку, содержащую текст.
    :return: С помощью генератора выражений функция извлекает все числовые символы из строки и объединяет их в
            одну строку, присваивая результат переменной total.
    """

    total = ''.join(i for i in user if i.isnumeric())

    if total == '':
        points = 0
    elif total == '70':
        points = 1
    elif total == '5':
        points = 2
    elif total == '50101':
        points = 3
    elif total == '150101':
        points = 4

    return points

# total = calculate_hypotension('Нет гипотензии')
# print(total)
