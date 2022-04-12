from aiogram.types import Message

from bot.loader import dispatcher


@dispatcher.message_handler(commands=['start'])
async def hello(message: Message):
    await message.answer('Hello, world!')
