from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from functions import client_kb, inline_kb, back_kb

from functions import films_parse
from functions import openweathermap
from functions import trains

from creation import disp

import sqlite_db
from datetime import date


date_input = str(date.today())


#@disp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}', reply_markup=client_kb)
    await message.delete()


#@disp.message_handler(commands=['Идём в кино'])
async def cinema(message: types.Message):
    #films, film_ids = films_parse.sql_read_title_id()
    await message.answer('Фильмы:', reply_markup=inline_kb)


#@disp.message_handler(commands=['Расписание'])
async def transport_shedule(message: types.Message):
    await message.answer(trains.trains_request(), reply_markup=client_kb)


#@disp.message_handler(commands=['Погода'])
async def weather(message: types.Message):
    await message.answer(openweathermap.weather_request(), reply_markup=client_kb)


async def back(message: types.Message):
    await message.answer('Назад', reply_markup=client_kb)
    await message.delete()


#@disp.message_handler()
async def command_else(message: types.Message):  # declared last. catches all mesages, what wasn`t processed by handlers above.
    await message.answer('Не понимаю команду')


@disp.callback_query_handler(Text(startswith='5'))
async def test_callback(callback: types.CallbackQuery):
    film_name = sqlite_db.sql_read_film_name(callback.data)
    await callback.message.answer(f'{film_name[0]}:')
    cinema_list = sqlite_db.sql_read_cinema_name(callback.data)
    for cinema_subway in cinema_list:
        answer_session = ''
        answer_cinema_name = '\n'.join(cinema_subway)
        times_prices = sqlite_db.sql_read_time_price(callback.data, cinema_subway[0])
        for time in times_prices:
            answer_session += ' '.join(time) + '\n'
        await callback.message.answer(f'{answer_cinema_name}\n{answer_session}')
    await callback.answer()


def register_client_handlers(disp: Dispatcher):
    disp.register_message_handler(command_start, commands=['start', 'help'])
    disp.register_message_handler(cinema, Text(equals='Идём в кино'))
    disp.register_message_handler(transport_shedule, Text(equals='Расписание'))
    disp.register_message_handler(weather, Text(equals='Погода'))
    disp.register_message_handler(back, Text(equals='Назад'))
    disp.register_message_handler(command_else)
