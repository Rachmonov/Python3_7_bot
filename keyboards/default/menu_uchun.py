from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import base
from loader import base

menular = base.select_all_turlar()


j = 0
index=0
keys = []

for menu in menular:
    if j %2==0 and j !=0:
        index+=1
    if j % 2 == 0:
        keys.append([KeyboardButton(text=f"{menu[1]}",)])
    else:
        keys[index].append(KeyboardButton(text=f"{menu[1]}",))
    j += 1

keys.append([KeyboardButton(text=f"Adminga murojat")])

menu_buttons = ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)



tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q")
        ],
    ],
    resize_keyboard=True
)

async def maxsulot_func(maxsulotlar):
    menular = base.select_all_turlar()

    j = 0
    index = 0
    keys = []

    for menu in maxsulotlar:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f"{menu[1]}", )])
        else:
            keys[index].append(KeyboardButton(text=f"{menu[1]}", ))
        j += 1

    keys.append([KeyboardButton(text=f"Ortga")])

    maxsulot_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return maxsulot_buttons