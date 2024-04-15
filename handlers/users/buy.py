import datetime

from aiogram import types

from loader import dp,base


# Echo bot
@dp.callback_query_handler(text_contains="buy")
async def bot_echo(message: types.CallbackQuery):
    data = message.data.split(" ")
    user_id = message.from_user.id
    date = datetime.datetime.now()
    trade = base.select_trade(tg_id=user_id,product_id=int(data[1]),status=False )
    if trade:
        print(trade,"jjjjjjjjjjjjjjjjj")
        new_number = trade[2]+1
        base.update_trade_number(number=new_number,tg_id=user_id,product_id=int(data[1]))
    else:
        base.buy_product(product_id=int(data[1]),tg_id=message.from_user.id,number=1,date=date)
    await message.answer(text=f'Maxsulot sotib olindi')