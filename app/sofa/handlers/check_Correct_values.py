from functools import lru_cache

@lru_cache(maxsize=4)
def check_correct_values_FioPao(data):
    """
    Проверяет корректность значения Pao/Fio или числового значения.

    Если строка является числом (и не равна 'o', 'O' или '0'),
    возвращает это значение. Если строка может быть преобразована в
    число с плавающей запятой, возвращает строку. В противном случае
    возвращает None.

    :param data: Строка, которую необходимо проверить.
    :return: Проверенное значение или None.
    """
    if data.isdigit():
        if data not in ['o', "O", '0']:
            return data
    else:
        try:
            float_value = float(data)  # Попытка преобразовать строку в float
            return data  # Возвращаем строку, если преобразование прошло успешно
        except ValueError:
            return None  # Возвращаем None, если произошла ошибка преобразования
    return None  # Возвращаем None, если ни одно из условий не выполнено


@lru_cache(maxsize=2)
def check_correct_kb_respiratory(data):
    """
    Проверяет корректность значения для респираторной функции.

    Если значение равно 'Да' или 'Нет', возвращает его. В противном случае
    возвращает None.

    :param data: Строка, которую необходимо проверить.
    :return: Проверенное значение или None.
    """
    ONE = ('Да')
    TWO = ('Нет')

    if data in (ONE, TWO):
        return data
    return None

@lru_cache(maxsize=2)
def check_correct_kb_platelet(data):
    """
    Проверяет корректность значения для тромбоцитов.

    Если значение соответствует одному из предопределенных диапазонов,
    возвращает его. В противном случае возвращает None.

    :param data: Строка, которую необходимо проверить.
    :return: Проверенное значение или None.
    """
    ONE = ('> 151')
    TWO = ('<= 150')
    THREE = ('<= 100')
    FOUR = ('<= 50')
    FIVE = ('<= 20')

    if data in (ONE, TWO, THREE, FOUR, FIVE):
        return data
    return None


def check_correct_kb_liver(data):
    """
    Проверяет корректность значения для функции печени.

    Если значение соответствует одному из предопределенных диапазонов,
    возвращает его. В противном случае возвращает None.

    :param data: Строка, которую необходимо проверить.
    :return: Проверенное значение или None.
    """
    ONE = ('< 20')
    TWO = ('20 - 32')
    THREE = ('33 - 101')
    FOUR = ('102 - 204')
    FIVE = ('> 204')

    if data in (ONE, TWO, THREE, FOUR, FIVE):
        return data
    return None


def check_correct_kb_creatinin(data):
    """
    Проверяет корректность значения для креатинина.

    Если значение соответствует одному из предопределенных диапазонов,
    возвращает его. В противном случае возвращает None.

    :param data: Строка, которую необходимо проверить.
    :return: Проверенное значение или None.
    """
    ONE = ('< 110')
    TWO = ('110 - 170')
    THREE = ('171 - 299')
    FOUR = ('300 - 440 или диурез <500 мл в сутки')
    FIVE = ('> 440 или < 200 мл мочи/сутки')

    if data in (ONE, TWO, THREE, FOUR, FIVE):
        return data
    return None


def check_correct_kb_hypotension(data):
    """
    Проверяет корректность значения для гипотензии.

    Если значение соответствует одному из предопределенных состояний,
    возвращает его. В противном случае возвращает None.

    :param data: Строка, которую необходимо проверить.
    :return: Проверенное значение или None.
    """
    ONE = ('Нет гипотензии')
    TWO = ('АДср < 70 мм.рт.ст.')
    THREE = ('Допамин <= 5 или любая доза добутамина')
    FOUR = ('Допамин > 5 или адреналин <= 0.1 или НА <= 0.1')
    FIVE = ('Допамин > 15 или адреналин > 0.1 или НА > 0.1')

    if data in (ONE, TWO, THREE, FOUR, FIVE):
        return data
    return None


def check_correct_kb_eye(data):
    """
    Проверяет корректность значения для реакции глаз.

    Если значение соответствует одному из предопределенных состояний,
    возвращает его. В противном случае возвращает None.

    :param data: Строка, которую необходимо проверить.
    :return: Проверенное значение или None.
    """
    ONE = ('Открывает самопроизвольно, наблюдает')
    TWO = ('Открывает, в ответ на голос')
    THREE = ('Открывает, как реакция на болевое раздражение')
    FOUR = ('Не открывает')

    if data in (ONE, TWO, THREE, FOUR):
        return data
    return None


def check_correct_kb_verbal(data):
    """
    Проверяет корректность значения для вербальной реакции.

    Если значение соответствует одному из предопределенных состояний,
    возвращает его. В противном случае возвращает None.

    :param data: Строка, которую необходимо проверить.
    :return: Проверенное значение или None.
    """
    ONE = ('Ориентирован и контактен (осмысленный ответ)')
    TWO = ('Произносит фразы, но речь бессвязная')
    THREE = ('Произносит отдельные слова')
    FOUR = ('Издает звуки, но не слова')
    FIVE = ('Отсутствие речи')

    if data in (ONE, TWO, THREE, FOUR, FIVE):
        return data
    return None


def check_correct_kb_motor(data):
    """
    Проверяет корректность значения для моторной реакции.

    Если значение соответствует одному из предопределенных состояний,
    возвращает его. В противном случае возвращает None.

    :param data: Строка, которую необходимо проверить.
    :return: Проверенное значение или None.
    """
    ONE = ('Выполнение движений по голосовой команде')
    TWO = ('Локализует боль, пытается её избежать')
    THREE = ('Бессмысленные движения в ответ на боль')
    FOUR = ('Патологическое сгибание в ответ на боль (декортикационная ригидность)')
    FIVE = ('Патологическое разгибание в ответ на боль (децеребрационная ригидность)')
    SIX = ('Не двигается')

    if data in (ONE, TWO, THREE, FOUR, FIVE, SIX):
        return data
    return None
