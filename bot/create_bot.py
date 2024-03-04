import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from loguru import logger

# TODO прописать рабочую откладку логов по всем исключениям

logger.add('testing_log.log', format='{time} {level} {message}',
           level='DEBUG')
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

storage = MemoryStorage()
# bot = Bot(token=TOKEN)
bot = Bot(token="6627326875:AAEZl0B84v1wQdu67G1ch8LbKGxPfc9xY9I")
dispatcher = Dispatcher(bot, storage=storage)
