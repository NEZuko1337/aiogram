from aiogram import Router, F
from aiogram.types import Message
from keyboards import reply, inline, fabrics,builders
from data.subloader import get_json

router = Router()

@router.message(F.text.lower() == 'ссылки')
async def links_keyboard(message: Message):
    await message.answer("Вот ссылки на мои соц. сети", reply_markup=inline.LinksKeyboard)


@router.message(F.text.lower() == 'спец. кнопки')
async def special_keyboard(message: Message):
    await message.answer("Специальные кнопки", reply_markup=reply.SpecialKeyboard)


@router.message(F.text.lower() == 'калькулятор')
async def special_keyboard(message: Message):
    await message.answer("Специальные кнопки", reply_markup=builders.calculate_keyboard())

@router.message(F.text.lower() == "смайлики")
async def smile_keyboard(message: Message):
    SMILES = await get_json("smiles.json")
    await message.answer(f"{SMILES[0][0]} <b>{SMILES[0][1]}</b>", reply_markup=fabrics.paginator())


@router.message()
async def echo(message: Message):
    await message.answer("Я не понимаю тебя, напиши /start, чтобы узнать подробности")
    await message.answer(f"Ты ввел: {message.text.lower()}")
