from aiogram.utils import executor
from creation import disp
from handlers import client, admin


async def on_startup(_):
    print('Работаю...')


client.register_client_handlers(disp)

executor.start_polling(disp, skip_updates=True, on_startup=on_startup)
