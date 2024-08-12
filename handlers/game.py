from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
import random

games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']


class GameState(StatesGroup):
    waiting_for_player_dice = State()


async def game(message: types.Message, state: FSMContext):
    random_game = random.choice(games)
    bot_dice = await bot.send_dice(chat_id=message.chat.id, emoji=random_game)
    bot_result = bot_dice.dice.value

    await message.answer("Теперь ваша очередь! Киньте дайс.")

    await state.update_data(bot_result=bot_result, random_game=random_game)
    await GameState.waiting_for_player_dice.set()


async def player_dice(message: types.Message, state: FSMContext):
    if not message.dice:
        await message.answer("Пожалуйста, киньте дайс!")
        return

    player_result = message.dice.value
    data = await state.get_data()
    bot_result = data['bot_result']
    random_game = data['random_game']

    if bot_result > player_result:
        await message.answer(f"Бот выиграл! {random_game}")
    elif bot_result < player_result:
        await message.answer(f"Вы выиграли! {random_game}")
    else:
        await message.answer(f"Ничья! {random_game}")

    await state.finish()


import logging


async def game(message: types.Message, state: FSMContext):
    random_game = random.choice(games)
    bot_dice = await bot.send_dice(chat_id=message.chat.id, emoji=random_game)
    bot_result = bot_dice.dice.value

    logging.info(f"Бот кинул {random_game}: {bot_result}")

    await message.answer("Теперь ваша очередь! Киньте дайс.")
    await state.update_data(bot_result=bot_result, random_game=random_game)
    await GameState.waiting_for_player_dice.set()


async def player_dice(message: types.Message, state: FSMContext):
    if not message.dice:
        await message.answer("Пожалуйста, киньте дайс!")
        return

    player_result = message.dice.value
    data = await state.get_data()
    bot_result = data['bot_result']
    random_game = data['random_game']

    logging.info(f"Игрок кинул {random_game}: {player_result}")
    logging.info(f"Бот кинул {random_game}: {bot_result}")

    if bot_result > player_result:
        await message.answer(f"Бот выиграл! {random_game}")
    elif bot_result < player_result:
        await message.answer(f"Вы выиграли! {random_game}")
    else:
        await message.answer(f"Ничья! {random_game}")

    await state.finish()


def register_game(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'], state='*')
    dp.register_message_handler(player_dice, content_types=types.ContentType.DICE,
                                state=GameState.waiting_for_player_dice)
