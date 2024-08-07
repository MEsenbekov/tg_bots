from aiogram import types, Dispatcher
from config import bot
import os
from aiogram.types import InputFile
import random


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет!')
    await message.answer(text='Привет')


async def info_handler(message: types.Message):
    await message.answer("Бот для группы 44-2 Backend")


async def mem_handler(message: types.Message):
    path = 'media'
    files = []

    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            files.append(full_path)
    random_photo = random.choice(files)

    await message.answer_photo(photo=InputFile(random_photo))


async def send_file(message: types.Message):
    file_path = r"C:\Users\ACER\PycharmProjects\HomeTGBot\main.py"

    if os.path.isfile(file_path):
        file_to_send = InputFile(file_path)
        await bot.send_document(chat_id=message.chat.id, document=file_to_send)
    else:
        await message.answer("Файл не найден.")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_file, commands=['sendfile'])


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(mem_handler, commands=['mem', 'photo'])
    dp.register_message_handler(send_file, commands=['file'])
