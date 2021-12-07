from aiogram.dispatcher.filters.state import State, StatesGroup


class Public(StatesGroup):
    sozlamalar = State()
    qaror = State()
    profile = State()


class Profile(StatesGroup):
    ism = State()
    nomer = State()


class Buyurtma(StatesGroup):
    address = State()
    taom = State()
    fast_food = State()
    milliy_taom = State()
    drinks = State()