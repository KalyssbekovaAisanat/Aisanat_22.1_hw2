from aiogram import types, Dispatcher
from config import bot, dp
import random

#@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


    if message.text.startswith('.'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.from_user.id == 'ADMIN':
        games = ['🎰', '🎳','🎲','🏀']
        if message.text.startswith('game'):
            await bot.send_message(message.chat.id, random.choice(games))




def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)

