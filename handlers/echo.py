from aiogram import types
import logging
from config import dp, bot
from aiogram.utils import executor

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)






if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)