from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


cars_home = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cobalt"),
            KeyboardButton(text="Gentra"),
            KeyboardButton(text="Nexia 3"),
        ],
        [
            KeyboardButton(text="Spark"),
            KeyboardButton(text="Matiz"),
            KeyboardButton(text="Back")
        ],
    ],
    resize_keyboard=True
)



from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
electric_home = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tesla"),
            KeyboardButton(text="Hongi"),
        ],
        [
            KeyboardButton(text="Elantra"),
            KeyboardButton(text="Sonata"),
            KeyboardButton(text="Kia K5"),
        ],
        [
            KeyboardButton(text="Back")
        ],
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
trucks_home = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kamaz"),
            KeyboardButton(text="Fura"),
            KeyboardButton(text="Zil"),
        ],
        [
            KeyboardButton(text="Labo"),
            KeyboardButton(text="Back")
        ],
    ],
    resize_keyboard=True
)