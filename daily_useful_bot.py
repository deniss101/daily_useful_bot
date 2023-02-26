from aiogram.utils import executor
from creation import disp
from handlers import client, fsm
import sqlite_db
from functions import films_parse


async def on_startup(_):
    try:
        sqlite_db.sql_connect()
        films_parse.get_cinema_sessions()
    except:
        print('Base not connected')
    print('I`m ONLINE')


client.register_client_handlers(disp)
fsm.register_fsm_handlers(disp)

executor.start_polling(disp, skip_updates=True, on_startup=on_startup)
