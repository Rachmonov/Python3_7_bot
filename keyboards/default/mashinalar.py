from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import base

async def menu_uchun(tur_id):
    maxsulotlar = base.select_maxsulotlar(tur_id=tur_id)

    j = 0
    index = 0
    keys = []

    for menu in maxsulotlar:
        if j %3==0 and j !=0:
            index+=1
        if j % 3 == 0:
            keys.append([KeyboardButton(text=f"{menu[1]}",)])
        else:
            keys[index].append(KeyboardButton(text=f"{menu[1]}",))
        j += 1

    keys.append([KeyboardButton(text=f"Adminga murojat")])

    return   ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
mashinalar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Gentra"),

        ],
        [
            KeyboardButton(text="Kobalt"),
            KeyboardButton(text="Spark"),
            KeyboardButton(text="Matiz"),
        ],
        [
            KeyboardButton(text="Nexia 3"),
            KeyboardButton(text="Ortga")
        ],
    ],
    resize_keyboard=True
)



from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
elektromobillar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tesla"),

        ],
        [
            KeyboardButton(text="Elantra"),
            KeyboardButton(text="Sonata"),
            KeyboardButton(text="Kia K5"),
        ],
        [
            KeyboardButton(text="Ortga")
        ],
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
yuk_mashinalar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kamaz"),
            KeyboardButton(text="Fura"),
            KeyboardButton(text="Zil"),
        ],
        [
            KeyboardButton(text="Labo"),
            KeyboardButton(text="Ortga")
        ],
    ],
    resize_keyboard=True
)