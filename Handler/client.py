
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


#@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Hello {message.from_user.first_name}!")


#@dp.message_handler(commands=['quiz'])
async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Что означает «www» в браузере веб-сайтов?"
    answers = [
        "Всемирная паутина",
        "Адрес сайтов",
        "База данные сети"
    ]
    await bot.send_poll(
       chat_id=message.from_user.id,
       question=question,
       options=answers,
       is_anonymous=False,
       type='quiz',
       correct_option_id=0,
       explanation="ИЗИ",
       open_period=10,
       reply_markup=markup
    )


#@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])


