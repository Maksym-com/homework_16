import logging

from aiogram import types
from aiogram.utils.exceptions import CantParseEntities

from loader import dp, db_bot


@dp.message_handler(commands=['add_me'])
async def add_user(msg: types.Message):
    user_id = msg.from_user.id
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    user_name = msg.from_user.username

    if not db_bot.user_exists(user_id):
        db_bot.add_user_to_db(user_id, first_name, last_name, user_name)
        await msg.reply("Користувача було успішно додано")
    else:
        await msg.reply("Такий користувач вже існує")

@dp.message_handler(commands=['get_my_info'])
async def get_user_info(msg: types.Message):
    user_name = msg.from_user.username
    if user_name:
        user_info = db_bot.get_my_info(user_name)
        await msg.reply(user_info)
    else:
        await msg.reply("Ми не маємо ніякої інформації про вас. Введіть команду /add_me")

@dp.message_handler(commands=["show_all_users"])
async def show_users(msg: types.Message):
    user_id = msg.from_user.id
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    username = msg.from_user.username
    await msg.answer(db_bot.show_all_users(user_id, first_name, last_name, username))
    await msg.answer('Ось всі користувачі⬆️')



