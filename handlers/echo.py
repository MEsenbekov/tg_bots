from aiogram import types, Dispatcher

async def echo_handler(message: types.Message):
    text = message.text
    if text.isdigit():
        await message.answer(int(text)**2)
    else:
        await message.answer(message.text)



def register_echo(dp: Dispatcher) -> object:
    """

    :rtype: object
    """
    dp.register_message_handler(echo_handler)
