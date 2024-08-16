import logging
import config
from aiogram.utils import executor
from handlers import commands, echo, game, FSM_reg, FSM_store, send_products
from db import db_main

admin = [1196009647]


async def on_startup(_):
    for i in admin:
        await config.bot.send_message(chat_id=i, text='Бот включен')
        await db_main.sql_create()


async def on_shutdown(_):
    for i in admin:
        await config.bot.send_message(chat_id=i, text='Бот выкдючен')


commands.register_commands(config.dp)
game.register_quiz(config.dp)
FSM_reg.register_fsm_store(config.dp)
FSM_store.store_fsm(config.dp)
send_products.register_send_products_handler(config.dp)
echo.register_echo(config.dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(config.dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
