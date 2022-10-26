import sqlite3
import random
from config import bot



def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('База данных подключена!')

    db.execute("CREATE TABLE IF NOT EXISTS mentor "
               "(id INTEGER PRIMARY KEY, username TEXT, "
               "name TEXT,  age INTEGER, direction TEXT,  "
               "ggroup TEXT)")
    db.commit()




async def sgl_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentor VALUES (?, ?, ?, ?, ?, ?,)", tuple(data.values()))
        db.commit()



async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentor").fetchall()
    random_user = random.choice(result)
    await message.answer(f"{random_user[2]}, {random_user[3]}, {random_user[4]}, {random_user[5]},/"
                         f" {random_user[1]}")





async def sql_command_all():
    return cursor.execute("SELECT * FROM mentor").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentor WHERE id = ?", (user_id,))
    db.commit()