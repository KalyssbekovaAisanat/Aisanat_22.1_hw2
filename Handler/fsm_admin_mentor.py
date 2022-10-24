from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.client_kb import  start_markap
from config import bot, ADMIN



class Fsmadmin(StatesGroup):
    id_mentor = State()
    name = State()
    age = State()
    direction = State()
    group = State()




async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMIN:
        await Fsmadmin.id_mentor.set()
        await message.answer(
            f"{message.from_user.id} ",
            reply_markup=start_markap
        )
    else:
        await message.answer('Пиши в личку!')




async def id_mentor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id_mentor'] = message.from_user.id
    await Fsmadmin.next()
    await message.answer('Укажите имя!')



async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Fsmadmin.next()
    await message.answer('Укажите ваш возраст')



async def  age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await Fsmadmin.next()
        await message.answer('Укажите ваше напраление.')
    except:
        await message.answer('Пиши числа!')




async def  direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await Fsmadmin.next()
    await message.answer('Укажите ваше группу.')




async def group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"{data['name']}, {data['age']}, {data['direction']}, {data['group']}")
        await Fsmadmin.next()
        await message.answer('Все верно???')




def register_handlers_fsm_admin(dp: Dispatcher):
    dp.register_message_handler( fsm_start, commands=['info'])
    dp.register_message_handler(id_mentor, state=Fsmadmin.id_mentor)
    dp.register_message_handler(name, state=Fsmadmin.name)
    dp.register_message_handler(age, state=Fsmadmin.age)
    dp.register_message_handler(direction, state=Fsmadmin.direction)
    dp.register_message_handler(group, state=Fsmadmin.group)