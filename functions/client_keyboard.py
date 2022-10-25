from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton('/Кино')
button2 = KeyboardButton('/Расписание')
button3 = KeyboardButton('/Погода')
client_kb = ReplyKeyboardMarkup(resize_keyboard=True)
client_kb.row(button1, button2, button3)

button4 = KeyboardButton('/Назад')
back_kb = ReplyKeyboardMarkup(resize_keyboard=True)
back_kb.add(button4)
