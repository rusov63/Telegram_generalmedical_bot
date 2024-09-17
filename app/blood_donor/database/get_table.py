import asyncio
from config import db_manager


async def get_table_donor(recipient: str, table_name='donor') -> str:
    """
    Получает информацию о доноре, совместимом с указанным реципиентом, из базы данных.

    :param:
    - recipient (str): Идентификатор реципиента, для которого необходимо найти
      совместимого донора.
    - table_name (str): Название таблицы в базе данных, из которой будет
      извлекаться информация. По умолчанию используется 'donor'.

    :return:
    - None: Если информация о доноре не найдена.
    - str: Форматированная строка с информацией о совместимом фенотипе и
      показаниях к трансфузии.

    Описание работы функции:
    1. Устанавливает асинхронное соединение с менеджером базы данных.
    2. Извлекает данные о совместимых донорах, соответствующих указанному
       реципиенту, включая совместимый фенотип и показания.
    3. Преобразует полученные данные в обычный список.
    4. Форматирует и возвращает строку с информацией о совместимом фенотипе и
       экстренных показаниях к трансфузии.

    Пример использования:
    recipient = 'CcDee'
    result = await get_table_donor(recipient)
    """
    async with db_manager:
        info = await db_manager.select_data(table_name=table_name,
                                            where_dict=[{'recipient': recipient}],
                                            columns=['compatible', 'indications'],
                                            one_dict=False)

    # if not info:
    #     return None  # Возвращаем None, если данных нет

    recipient_list = sum([list(d.values()) for d in info], [])

    return (f'Cовместимый фенотип: \n'
            f'<b>{recipient_list[0].strip()}</b> \n'
            f'\n'
            f'При экстренных показаниях к трансфузии (переливанию): \n'
            f'<b>{recipient_list[1].strip()}</b>')

# recipient = 'CcDee'
# #recipient = '1'
# asyncio.run(get_table_donor(recipient))

# [{'compatible': 'CcDee CCDee ccddee ccDee Ccddee    ', 'indications': 'отсутствуют              '}]
