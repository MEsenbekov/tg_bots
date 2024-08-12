import logging
from config import dp, bot
from aiogram.utils import executor
from handlers import commands, echo, quiz, game
from db import db_main
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

dp.storage = storage

admin = [1196009647, ]


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='Бот включен!')
    await db_main.sql_create()


async def on_shutdown(_):
    for i in admin:
        try:
            await bot.send_message(chat_id=i, text='Бот выключен!')
        except Exception as e:
            logging.error(f"Ошибка при отправке сообщения об отключении: {e}")


commands.register_commands(dp)
quiz.register_quiz(dp)
game.register_game(dp)
echo.register_echo(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
