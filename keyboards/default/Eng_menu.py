from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_home = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text="Cars"),
            KeyboardButton(text="Electric cars"),
        ],
        [

            KeyboardButton(text="Trucks")
        ],
    ],
    resize_keyboard=True
)