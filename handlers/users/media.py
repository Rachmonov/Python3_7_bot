from aiogram import types
from keyboards.inline.tillar_uchun import sotib_olish_func
from loader import dp,base,bot


maxsulotlar = base.select_all_maxsulotlar()

@dp.message_handler(text=[maxsulot[1] for maxsulot in maxsulotlar])
async def bot_start(message: types.Message):
    one_product = base.select_maxsulot(nomi=message.text)
    rasm_manzili = f'{one_product[3]}'
    sotib_olish_buttons = await sotib_olish_func(max_id=one_product[0])
    await bot.send_photo(chat_id=message.from_user.id,photo=rasm_manzili,caption=f'{one_product[2]}',reply_markup=sotib_olish_buttons)