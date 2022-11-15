import sqlite3

from aiogram import Bot
from os import environ
bot = Bot(environ.get('tele_useful_bot'))

con = sqlite3.connect('cinema_sessions.db', check_same_thread=False)
cur = con.cursor()


def sql_connect():
    if con:
        print('Base connected')
    cur.execute('CREATE TABLE IF NOT EXISTS sessions (id INTEGER PRIMARY KEY, title TEXT, cinema TEXT, address TEXT, subway TEXT, time TEXT, price TEXT)')
    con.commit()


async def sql_add(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO sessions VALUES (?, ?, ?, ?)', tuple(data.values()))
        con.commit()


async def sql_read(message):
    for line in cur.execute('SELECT * FROM sessions').fetchall():
        await bot.send_message(message.from_user.id, line[0], f'{line[1]}')


async def sql_read_title_id():
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    films = cur.execute("SELECT DISTINCT title FROM sessions ").fetchall()
    ids = cur.execute("SELECT DISTINCT id FROM sessions ").fetchall()
    cur.close()
    return films, ids


def sql_read_details(film_id):
    return cur.execute("SELECT cinema, address, subway, time, price FROM sessions WHERE id=?",(film_id,)).fetchall()


def sql_read_film_name(film_id):
    return cur.execute("SELECT DISTINCT title FROM sessions WHERE id=?",(film_id,)).fetchone()


def sql_read_cinema_name(film_id):
    return cur.execute("SELECT DISTINCT cinema, subway FROM sessions WHERE id=?",(film_id,)).fetchall()


def sql_read_time_price(id, cinema):
    return cur.execute("SELECT time, price FROM sessions WHERE id =? AND cinema=?",(id, cinema,)).fetchall()
