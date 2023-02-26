from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions import films_parse


films, film_ids = films_parse.sql_read_title_id()


inline_kb = InlineKeyboardMarkup(row_width=1)
for i in range(len(films)):
    inline_kb.add(InlineKeyboardButton(text=films[i], callback_data=film_ids[i]))

inline_kb_city = InlineKeyboardMarkup(row_width=2)
inline_kb_city.row((InlineKeyboardButton(text='Москва', callback_data='city_msk')),
                    (InlineKeyboardButton(text='Санкт-Перербург', callback_data='city_spb')))

inline_kb_date = InlineKeyboardMarkup(row_width=2)
inline_kb_date.row((InlineKeyboardButton(text='Сегодня', callback_data='day1')),
                    (InlineKeyboardButton(text='Завтра', callback_data='day2')),
                    (InlineKeyboardButton(text='Послезавтра', callback_data='day3')))
