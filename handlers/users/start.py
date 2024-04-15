from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from data.config import ADMINS
from keyboards.default.menu_uchun import menu_buttons, maxsulot_func
from keyboards.default.mashinalar import mashinalar_buttons
from keyboards.default.mashinalar import elektromobillar_buttons
from keyboards.default.mashinalar import yuk_mashinalar_buttons
from keyboards.inline.tillar_uchun import tillar_buttons, sotib_olish_func
from loader import dp, base, bot




@dp.message_handler(commands='reklama',chat_id=ADMINS[0])
async def bot_start(message: types.Message):
    userlar = base.select_all_users()
    for user in userlar:
        await bot.send_message(chat_id=user[3],text="jfyffuyfhgf")



@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlovni kiriting",reply_markup=menu_buttons)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    ismi = message.from_user.first_name
    familiya = message.from_user.last_name
    user_id = message.from_user.id
    try:
        base.user_qoshish(ism=ismi,tg_id=user_id,fam=familiya)
    except Exception as x:
        pass
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu_buttons)

turlar = base.select_all_turlar()

@dp.message_handler(text=[tur[1] for tur in turlar])
async def bot_start(message: types.Message):
    text = message.text
    tur = base.select_tur(nomi=text)
    maxsulotlar = base.select_maxsulotlar(turi_id = tur[0][0])
    maxsulot_buttons = await maxsulot_func(maxsulotlar=maxsulotlar)
    await message.answer(text="Maxsulotlardan birini tanlang",reply_markup=maxsulot_buttons)



maxsulotlar = base.select_all_maxsulotlar()

@dp.message_handler(text=[maxsulot[1] for maxsulot in maxsulotlar])
async def bot_start(message: types.Message):
    one_product = base.select_maxsulot(nomi=message.text)
    rasm_manzili = f'{one_product[3]}'
    sotib_olish_buttons = await sotib_olish_func(max_id=one_product[0])
    await bot.send_photo(chat_id=message.from_user.id,photo=rasm_manzili,caption=f'{one_product[2]}',reply_markup=sotib_olish_buttons)


