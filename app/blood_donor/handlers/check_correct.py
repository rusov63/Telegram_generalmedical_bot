RESIPIENT = ('CcDee', 'CCDee', 'CcDEe', 'ccddee', 'ccDEe', 'CwCDee', 'ccDEE', 'CwcDee', 'ccDee',
             'Ccddee', 'CwcDEe', 'ccDweakee', 'CcddEe', 'CCDEe', 'ccddEe', 'CcDEE', 'Cwcddee',
             'CCddee', 'CCDEE', 'CCddEe', 'CcddEE', 'ccddEE', 'CCDweakee', 'CcDweakee', 'ccDweakEe',
             'ccDweakEE', 'CwcddEe', 'CwcDEE', 'kk', 'Kk', 'KK')

def СheckСorrectPhenotype(data):
    """
    Проверяет, является ли указанный фенотип корректным.

    Эта функция принимает строку 'data', представляющую фенотип, и проверяет,
    содержится ли она в предопределенном кортеже RESIPIENT. Если фенотип
    найден, функция возвращает его. В противном случае возвращает None.

    :param
    data (str): Фенотип, который необходимо проверить.

    :return
    str или None: Возвращает корректный фенотип, если он найден в 'RESIPIENT,
    иначе возвращает None.
    """
    if data in RESIPIENT:
        return data
    return None

