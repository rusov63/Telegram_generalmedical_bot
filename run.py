import asyncio
import logging

import bot_start
from app import echo
from app.anesthetic_risk.handlers import handler_anest
from app.blood_donor.handlers import handler_donor
from app.skf.handlers import handler_skf

from config import dp, bot

from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands():
    """Командное меню. Дефолтное значение"""

    commands = [BotCommand(command='/start', description='Старт'),
                BotCommand(command='/anesthetic_risk', description='Оценка операционно- анестезиологического риска'),
                BotCommand(command='/skf', description='Cкорость клубочковой фильтрации'),
                BotCommand(command='/donor', description='Подбор донора крови')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def main():
    # регистрация роутеров
    dp.include_routers(
        bot_start.user_router,  # команда /start

        handler_anest.anesthesia_router,  # команда /anesthetic risk

        handler_skf.skf_router,  # команда /skf

        handler_donor.donor_router,  # команда /donor

        echo.echo_router  # неизвестная команда
    )

    await dp.start_polling(bot)

    await set_commands()  # Командное меню.


if __name__ == '__main__':
    # в терминале выводит ход запросов/работы бота
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    if True:
        asyncio.run(main())
    elif False:
        print("exit")
