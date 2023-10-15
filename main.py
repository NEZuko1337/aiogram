from tokens import bot_api
# from contextlib import suppress
from aiogram import Bot, Dispatcher, F
# from aiogram.filters import Command, CommandObject
# from aiogram.types import Message, CallbackQuery
# from aiogram.enums.dice_emoji import DiceEmoji
# from aiogram.exceptions import TelegramBadRequest
import asyncio
# from random import randint
from handlers import bot_messages, user_commands, questionarie
from callbacks import pagination
TOKEN = bot_api

async def main():
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers( 
        user_commands.router, 
        pagination.router,
        questionarie.router,
        bot_messages.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

