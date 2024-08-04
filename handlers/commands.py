from aiogram import types, Dispatcher
from config import bot


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет!')
    await message.answer(text='Привет')


def register_commands(dp: Dispatcher):
    dp.register_message_heandler(start_handler, comands=['start'])
