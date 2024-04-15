from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import base

menular = base.select_all_turlar()


j = 0
index=0
keys = []

for menu in menular:
    if j %3==0 and j !=0:
        index+=1
    if j % 3 == 0:
        keys.append([KeyboardButton(text=f"{menu[1]}",)])
    else:
        keys[index].append(KeyboardButton(text=f"{menu[1]}",))
    j += 1

keys.append([KeyboardButton(text=f"Adminga murojat")])

menu_buttons = ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)

Мену_батл = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text="Автомобили"),
            KeyboardButton(text="Электромобили"),
        ],
        [

            KeyboardButton(text="Грузовики")
        ],
        [
            KeyboardButton(text="Свяжитесь с админом")
        ],
    ],
    resize_keyboard=True
)
tastiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ],
    ],
    resize_keyboard=True
)