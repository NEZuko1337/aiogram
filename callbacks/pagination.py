from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery
from keyboards import fabrics
from contextlib import suppress
from data.subloader import get_json
router = Router()
@router.callback_query(fabrics.Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_handler(call:CallbackQuery, callback_data: fabrics.Pagination):
    SMILES = await get_json("smiles.json")
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == 'next':
        page = page_num + 1 if page_num < (len(SMILES) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f"{SMILES[page][0]} <b>{SMILES[page][1]}</b>",
            reply_markup=fabrics.paginator(page=page)
        )
    await call.asnwer()