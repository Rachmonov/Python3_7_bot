from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tillar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili", callback_data="til1"),
            InlineKeyboardButton(text="Rus tili", callback_data="til2"),
        ],
        [
            InlineKeyboardButton(text="English tili", callback_data="til3"),
        ]
    ]

)


async def sotib_olish_func(max_id):
    buy_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Sotib olish', callback_data=f'buy {max_id}')
            ]
        ]
    )
    return buy_button
