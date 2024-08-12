import sqlite3
from db import queries

db = sqlite3.connect('db/db.sqlite3')
curses = db.cursor()


async def sql_create():
    if db:
        print('База данных SQLite3 подключена!')
    curses.execute(queries.CREATE_TABLE_REGISTRATION)
    db.commit()


async def sql_insert_registration(telegram_id, firstname):
    # Предполагаем, что INSERT_INTO_TABLE_REGISTRATION — это строка с запросом
    # Используем параметризованный запрос для предотвращения SQL-инъекций
    curses.execute(queries.INSERT_INTO_TABLE_REGISTRATION, (telegram_id, firstname))
    db.commit()
