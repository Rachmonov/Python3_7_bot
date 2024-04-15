from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from keyboards.inline.tillar_uchun import tillar_buttons
from loader import dp


@dp.callback_query_handler(text='www')
async def bot_start(xabar: types.CallbackQuery):
    await xabar.message.answer(f"Assalomu alaykum botga hush kelibsiz",reply_markup=tillar_buttons)

