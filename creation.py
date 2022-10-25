from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from os import environ

bot = Bot(environ.get('tele_useful_bot'))
disp = Dispatcher(bot)
