from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from functions import client_kb, back_kb

from functions import films_parse
from functions import openweathermap
from functions import trains
'''from datetime import date
import sqlite3

import films_parse
import openweathermap
import trains
import sql_usage

date_input = str(date.today())'''


#@disp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}', reply_markup=client_kb)
    await message.delete()


#@disp.message_handler(commands=['Идём в кино'])
async def cinema(message: types.Message):
    films, film_ids = films_parse.sql_read_title_id()
    await message.answer('\n'.join(films), reply_markup=back_kb)


#@disp.message_handler(commands=['Расписание'])
async def transport_shedule(message: types.Message):
    await message.answer(trains.trains_request(), reply_markup=back_kb)


#@disp.message_handler(commands=['Погода'])
async def weather(message: types.Message):
    await message.answer(openweathermap.weather_request(), reply_markup=back_kb)


async def back(message: types.Message):
    await message.answer('Назад', reply_markup=client_kb)
    await message.delete()


#@disp.message_handler()
async def command_else(message: types.Message):  # declare last. catches all mesages, what wasn`t processed by handlers above.
    await message.answer('Не понимаю команду')


def register_client_handlers(disp: Dispatcher):
    disp.register_message_handler(command_start, commands=['start', 'help'])
    disp.register_message_handler(cinema, commands=['Кино'])
    disp.register_message_handler(transport_shedule, commands=['Расписание'])
    disp.register_message_handler(weather, commands=['Погода'])
    disp.register_message_handler(back, commands=['Назад'])
    disp.register_message_handler(command_else)
