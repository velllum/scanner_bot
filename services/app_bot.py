import logging
import os
from sre_parse import State

from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from dotenv import load_dotenv

from handlers.client import register_handlers
from main import dp, bot

State()


load_dotenv()

logging.basicConfig(level=logging.INFO)


async def on_startup(dp: Dispatcher):
    logging.info('Программа запущенна ...')

    dp.storage.dic = {"pol": 37}
    dp.dic = {"pol": 37}

    await bot.set_webhook(os.getenv("WEBHOOK_URL"))
    # insert code here to run it after start


async def on_shutdown(dp: Dispatcher):
    logging.warning('Программа остановлена ...')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


async def main():
    ...


register_handlers(dp)


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=os.getenv("WEBHOOK_PATH"),
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=os.getenv("WEBAPP_HOST"),
        port=os.getenv("WEBAPP_PORT"),
    )

