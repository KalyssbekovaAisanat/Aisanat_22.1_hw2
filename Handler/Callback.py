
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


#@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "Какой национальный цветок Японии?"
    answers = [
        "фиалка",
        "роза",
        "сакура"
    ]
    await bot.send_poll(
       chat_id=call.from_user.id,
       question=question,
       options=answers,
       is_anonymous=False,
       type='quiz',
       correct_option_id=2,
       explanation="ИЗИ",
       open_period=10,
       reply_markup=markup
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, lambda call: call.data == "button_call_1")


