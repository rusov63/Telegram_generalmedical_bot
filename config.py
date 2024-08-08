from dotenv import load_dotenv
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from asyncpg_lite import DatabaseManager

load_dotenv()

TOKEN = str(os.getenv('BOT_TOKEN'))


# Deletion_password - нужен для дополнительной защиты в критических операциях.
# Взамодействие с базой данных.
db_manager = DatabaseManager(db_url=os.getenv('PG_LINK'), deletion_password=os.getenv('ROOT_PASS'))

# инициируем объект бота, передавая ему parse_mode=ParseMode.HTML по умолчанию
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# инициируем объект бота
dp = Dispatcher()