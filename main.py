
from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, dp
import logging
from Handler import client, Callback, exstra

client.register_handlers_client(dp)
Callback.register_handlers_callback(dp)
exstra.register_handlers_extra(dp)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)