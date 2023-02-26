from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from creation import disp
from functions import trains
import sqlite_db


class FSM_Admin(StatesGroup):
    station_from = State()
    station_to = State()


@disp.message_handler(commands='Расписание', state=None)
async def rasp_start(message: types.Message):
    await FSM_Admin.station_from.set()
    await message.answer('Станция отправления:')


@disp.message_handler(content_types=['text'], state=FSM_Admin.station_from)
async def station_from_data(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['from'] = message.text
    await FSM_Admin.next()
    await message.answer('Станция назначения:')


@disp.message_handler(state=FSM_Admin.station_to)
async def station_to_data(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['to'] = message.text
    await FSM_Admin.next()
    await message.answer('Принято:')
    await message.answer(str(data['from']) +'\n' + str(data['to']))
    station_from_code = sqlite_db.yandex_code_read(str(data['from']))
    station_to_code = sqlite_db.yandex_code_read(str(data['to']))
    train_times = trains.trains_request(station_from_code[0][0], station_to_code[0][0])
    await message.answer(train_times)

    await state.finish()

'''@disp.message_handler(state=FSM_Admin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSM_Admin.next()
    await message.reply('Укажи цену')


@disp.message_handler(state=FSM_Admin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    await sqlite_db.sql_add(state)

    await state.finish()'''


def register_fsm_handlers(disp: Dispatcher):
    disp.register_message_handler(rasp_start, Text(equals='Расписание'), state=None)
    disp.register_message_handler(station_from_data, state=FSM_Admin.station_from)
    disp.register_message_handler(station_to_data, state=FSM_Admin.station_to)
