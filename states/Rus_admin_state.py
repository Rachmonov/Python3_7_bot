from aiogram.dispatcher.filters.state import State,StatesGroup


class AdminState2(StatesGroup):
    imya = State()
    adres = State()
    let = State()
    tel = State()
    text = State()
    tasdiqlash = State()