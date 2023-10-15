from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from random import randint
from aiogram.enums.dice_emoji import DiceEmoji
from keyboards import reply

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f"Привет {message.from_user.first_name}, в этом боте ты сможешь выбрать случайное число(в заданных тобой границах), увидеть как я угадываю числа с кубика до его выпадения и создать свою крутую анкету, прямо как в Дай Винчике(/rn, /game, /profile)",
        reply_markup=reply.MainKeyboard
    )

@router.message(Command(commands=["rn", "random-number"]))
async def random_number(message: Message, command: CommandObject):
    try:
        a, b = [int(n) for n in command.args.split("-")]
        rand_int = randint(a,b)
        await message.reply(f"Твое случайное число: {rand_int}")
    except ValueError:
        await message.answer(f"Введи запрос правильно, например /rn 1-25| /random-number 1-25 ")
    except AttributeError:
        await message.answer(f"Введи запрос правильно, например /rn 1-25| /random-number 1-25 ")


@router.message(Command("game"))
async def game(message: Message):
    x = await message.answer_dice(DiceEmoji.DICE)
    await message.answer(f"Давай я предугадаю твое число, им будет: {(x.dice.value)}")

