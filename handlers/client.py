from aiogram import types, Dispatcher
from aiogram.dispatcher.webhook import SendMessage

from main import dp


async def command_start(message: types.Message):
    # Regular request
    # or reply INTO webhook
    return SendMessage(
        chat_id=message.chat.id,
        text="Пошел в пизду ))))",
    )


async def echo(message: types.Message):
    # Regular request
    # or reply INTO webhook
    print(dp.storage.__getattribute__("dic"))
    print(dp.__getattribute__("dic"))
    return SendMessage(message.chat.id, message.text)


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(
        callback=command_start,
        commands=["start"]
    )

    dispatcher.register_message_handler(
        callback=echo,
    )

