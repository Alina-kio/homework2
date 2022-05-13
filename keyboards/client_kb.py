from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = KeyboardButton("/start")
mem_button = KeyboardButton("/mem")
quiz_button = KeyboardButton("/quiz")

start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_markup.row(start_button, mem_button, quiz_button)
