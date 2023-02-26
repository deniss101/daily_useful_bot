from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from os import environ
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(environ.get('tele_useful_bot'))
disp = Dispatcher(bot, storage=storage)
