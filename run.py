import asyncio
import logging

import bot_start
from app.other_files import echo, feedback_project
from app.anesthetic_risk.handlers import handler_main_anest
from app.blood_donor.handlers import handler_donor
from app.skf.handlers import handler_main_skf
from app.sofa.handlers import handler_main_sofa

from config import dp, bot, ADMIN_ID

from aiogram.types import BotCommand, BotCommandScopeDefault


async def on_startup():
    await bot.send_message(chat_id=ADMIN_ID, text=f'🤩 Бот запущен!')


async def on_shutdown():
    await bot.send_message(chat_id=ADMIN_ID, text=f'🤨 Внимание, бот остановлен!')
    # Закрываем сессию бота, освобождая ресурсы
    await bot.session.close()


async def set_commands():
    """Командное меню. Дефолтное значение"""

    commands = [
        BotCommand(command='/start', description='Старт'),
        BotCommand(command='/anesthetic_risk', description='Оценка опер. анестезиологического риска'),
        BotCommand(command='/skf', description='Cкорость клубочковой фильтрации'),
        BotCommand(command='/donor', description='Подбор донора крови'),
        BotCommand(command='/sofa', description='Шкала SOFA')
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def main():
    # регистрация роутеров

    dp.include_routers(

        bot_start.user_router,  # команда /start

        feedback_project.user_router,  # callback 'Обратная связь'

        handler_main_anest.anesthesia_router,  # команда /anesthetic risk

        handler_main_skf.skf_router,  # команда /skf

        handler_donor.donor_router,  # команда /donor

        handler_main_sofa.sofa_router,  # команда /sofa

        echo.echo_router  # неизвестная команда
    )

    # Регистрируем функцию, которая будет вызвана при старте бота
    dp.startup.register(on_startup)

    # Регистрируем функцию, которая будет вызвана при остановке бота
    dp.shutdown.register(on_shutdown) # Ctrl-C для остановки бота и вывода сообщения

    await set_commands()  # Командное меню.

    await dp.start_polling(bot)



if __name__ == '__main__':
    # в терминале выводит ход запросов/работы бота
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    if True:
        asyncio.run(main())
    elif False:
        print("exit")
