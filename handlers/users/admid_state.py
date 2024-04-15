from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import  ReplyKeyboardRemove
from data.config import ADMINS
from keyboards.default.menu_uchun import tasdiqlash_buttons, menu_buttons
from states.adminga_murojat import AdminState
from loader import dp, bot


# Echo bot
@dp.message_handler(text="Adminga murojat")
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text="Ismni kiriting",reply_markup=ReplyKeyboardRemove())
    await AdminState.ism.set()

@dp.message_handler(state=AdminState.ism)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"name":matn})
    await message.answer(text="Manzilni kiriting")
    await AdminState.manzil.set()

@dp.message_handler(state=AdminState.manzil)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"Lokatsiya": matn})
    await message.answer(text="Yoshni kiriting")
    await AdminState.yosh.set()

@dp.message_handler(state=AdminState.yosh)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"age": matn})
    await message.answer(text="Telefon raqamni kiriting")
    await AdminState.tel.set()

@dp.message_handler(state=AdminState.tel)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"Phone": matn})
    await message.answer(text="Murojatingizni kiriting")
    await AdminState.text.set()

@dp.message_handler(state=AdminState.text)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"text": matn})

    malumot = await state.get_data()
    ismi = malumot.get("name")
    manzili = malumot.get("Lokatsiya")
    yoshi = malumot.get("age")
    tel = malumot.get("Phone")
    matn = malumot.get("text")

    user_matn = f"Ism : {ismi}\n" \
                f"Manzil : {manzili}\n" \
                f"Yosh : {yoshi}\n" \
                f"Tel : {tel}\n" \
                f"Murojat : {matn}\n"
    await bot.send_message(chat_id=message.from_user.id,text=user_matn,reply_markup=tasdiqlash_buttons)
    await AdminState.tasdiqlash.set()

@dp.message_handler(state=AdminState.tasdiqlash,text="Ha")
async def bot_echo(message: types.Message,state:FSMContext):
    malumot = await state.get_data()
    ismi = malumot.get("name")
    manzili = malumot.get("Lokatsiya")
    yoshi = malumot.get("age")
    tel = malumot.get("Phone")
    matn = malumot.get("text")

    user_matn = f"Ism : {ismi}\n" \
                f"Manzil : {manzili}\n" \
                f"Yosh : {yoshi}\n" \
                f"Tel : {tel}\n" \
                f"Murojat : {matn}\n"
    await bot.send_message(chat_id=ADMINS[0], text=user_matn, reply_markup=tasdiqlash_buttons)
    await bot.send_message(chat_id=message.from_user.id, text="Adminga yuborildi", reply_markup=menu_buttons)
    await state.finish()

@dp.message_handler(state=AdminState.tasdiqlash,text="Yo'q")
async def bot_echo(message: types.Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text="Bekor qilindi", reply_markup=menu_buttons)
    await state.finish()