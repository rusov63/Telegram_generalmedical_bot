import asyncio
from config import db_manager


async def get_table_donor(recipient: str, table_name='donor') -> None or str:
    """
    Функция, которая достает данные из таблицы.
    :param recipient: Поиск в столбце recipient из table donor.
    :param table_name: Таблица - donor из БД Medical.
    :return: Возвращает None если список пустой (введены не корректные данные), иначе
    возвращает ответ str.
    """
    RESIPIENT = ('CcDee', 'CCDee', 'CcDEe', 'ccddee', 'ccDEe', 'CwCDee', 'ccDEE', 'CwcDee', 'ccDee',
                 'Ccddee', 'CwcDEe', 'ccDweakee', 'CcddEe', 'CCDEe', 'ccddEe', 'CcDEE', 'Cwcddee',
                 'CCddee', 'CCDEE', 'CCddEe', 'CcddEE', 'ccddEE', 'CCDweakee', 'CcDweakee', 'ccDweakEe',
                 'ccDweakEE', 'CwcddEe', 'CwcDEE', 'kk', 'Kk', 'KK')

    if recipient not in RESIPIENT:
        return f'<b>Ошибка, такой фенотип не существует!</b>'

    else:
        async with db_manager:
            info = await db_manager.select_data(table_name=table_name,
                                                where_dict=[{'recipient': recipient}],
                                                columns=['compatible', 'indications'],
                                                one_dict=False)

        recipient_list = sum([list(d.values()) for d in info], [])  # из вложенного списка
        # превращаем в обычный список

        return (f'Cовместимый, фенотип: \n'
                f'<b>{recipient_list[0]}</b> \n'
                f'\n'
                f'При экстренных показаниях к трансфузии (переливанию) допустим, фенотип: \n'
                f'<b>{recipient_list[1]}</b>')

#recipient = 'CcDee'
#recipient = '1'
# asyncio.run(get_table_donor(recipient))

# [{'compatible': 'CcDee CCDee ccddee ccDee Ccddee    ', 'indications': 'отсутствуют              '}]
