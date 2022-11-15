from aiogram.utils import executor
from creation import disp
from handlers import client
import sqlite_db


async def on_startup(_):
    try:
        sqlite_db.sql_connect()
    except:
        print('Base not connected')
    print('I`m ONLINE')


client.register_client_handlers(disp)

executor.start_polling(disp, skip_updates=True, on_startup=on_startup)
