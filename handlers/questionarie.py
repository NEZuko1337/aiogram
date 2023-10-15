from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import Form
from keyboards import builders, reply

router = Router()

@router.message(Command("profile"))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Введи свое имя", reply_markup=builders.profile(message.from_user.first_name))


@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer("Отлично, введи свой возраст",reply_markup=reply.rmk)

@router.message(Form.age)
async def form_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(Form.sex)
        await message.answer("Теперь Выбери свой пол", reply_markup=builders.profile(["Парень", "Девушка"]))
    else:
        await message.answer("Введи свой возраст корректно")

@router.message(Form.sex, F.text.casefold().in_(["парень", "девушка"]))
async def form_sex(message:Message, state:FSMContext):
    await state.update_data(sex = message.text)
    await state.set_state(Form.about)
    await message.answer("Отлично! Теперь расскажи немного о себе", reply_markup=reply.rmk)


@router.message(Form.sex)
async def incorrect_sex_form(message:Message, state:FSMContext):
    await message.answer("Нажми на кнопку")

@router.message(Form.about)
async def form_about(message:Message, state:FSMContext):
    if len(message.text)<5:
        await message.answer("Введи что-нибудь поинтересней🤥")
    else:
        await state.update_data(about=message.text)
        await state.set_state(Form.photo)
        await message.answer("Классный текст, теперь отправь свою фотку")

@router.message(Form.photo, F.photo)
async def form_photo(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await state.clear()

    formatted_profile = []
    [
        formatted_profile.append(f'{key} : {value}')
        for key, value in data.items()
    ]
    await message.answer_photo(
        photo_file_id,
        "\n".join(formatted_profile)
    )


# ~ короче not только в aiogram
@router.message(Form.photo, ~F.photo)
async def incorrect_form_photo(message: Message):
    await message.answer("Ты отправил не фотку!")