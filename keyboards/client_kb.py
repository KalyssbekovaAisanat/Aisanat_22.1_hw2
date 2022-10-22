from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton


start_markap = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)


start_button = KeyboardButton("/start")
info_button = KeyboardButton("/info")

share_location = KeyboardButton("Share location", request_location=True)
share_info = KeyboardButton("Share info", request_contact=True)

start_markap.add(start_button, info_button).add(share_location, share_info)