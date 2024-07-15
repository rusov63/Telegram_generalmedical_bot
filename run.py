import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from config import TOKEN
#from app.handlers import start_bot, get_my_id, get_text, get_document, echo
from command_start import start_router



# является основной функцией запросф на сервер ТГ, и обновляет информацию если есть новые сообщения
async def main():
    bot = Bot(token=TOKEN)

    dp = Dispatcher()

    dp.include_routers(
        start_router,
    )

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout) # в терминале выводит ход работы/запросы ТГ бота
    if True:
        asyncio.run(main())
    elif False:
        print("exit")

