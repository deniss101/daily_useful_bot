from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions import films_parse


films, film_ids = films_parse.sql_read_title_id()


inline_kb = InlineKeyboardMarkup(row_width=1)
for i in range(len(films)):
    inline_kb.add(InlineKeyboardButton(text=films[i], callback_data=film_ids[i]))
