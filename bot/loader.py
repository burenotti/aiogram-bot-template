import aiogram
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.mongo import MongoStorage

from bot.settings import config


bot = aiogram.Bot(token=config.bot_token)
dispatcher = Dispatcher(bot)

fsm_storage = MongoStorage(
    host=config.mongo_host,
    port=config.mongo_port,
)