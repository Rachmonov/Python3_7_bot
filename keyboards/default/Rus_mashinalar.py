from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


Автомобили_батл = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кобалт"),
            KeyboardButton(text="Джентра"),
            KeyboardButton(text="Нексия 3"),
        ],
        [
            KeyboardButton(text="Спарк"),
            KeyboardButton(text="Матиз"),
            KeyboardButton(text="Назад")
        ],
    ],
    resize_keyboard=True
)



from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Электромобили_батл = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тесла"),
            KeyboardButton(text="Хонги"),
        ],
        [
            KeyboardButton(text="Элантра"),
            KeyboardButton(text="Соната"),
            KeyboardButton(text="Кия К5"),
        ],
        [
            KeyboardButton(text="Назад")
        ],
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Грузовики_батл = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Камаз"),
            KeyboardButton(text="Фура"),
            KeyboardButton(text="Зил"),
        ],
        [
            KeyboardButton(text="Лабо"),
            KeyboardButton(text="Назад")
        ],
    ],
    resize_keyboard=True
)