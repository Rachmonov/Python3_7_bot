from aiogram.dispatcher.filters.state import State,StatesGroup


class AdminState(StatesGroup):
    ism = State()
    manzil = State()
    yosh = State()
    tel = State()
    text = State()
    tasdiqlash = State()