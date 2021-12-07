from aiogram.dispatcher.filters.state import State, StatesGroup


class Admin(StatesGroup):
    menu = State()


class Profile(StatesGroup):
    name = State()
    phone = State()


class Food(StatesGroup):
    fastfood = State()
    fastfood_nomi = State()
    fastfood_price = State()
    fastfood_pic = State()
    milliy_taom = State()
    milliy_taom_nomi = State()
    milliy_taom_price = State()
    milliy_taom_pic = State()
    ichmliklar = State()
    ichmliklar_nomi = State()
    ichmliklar_price = State()
    ichmliklar_pic = State()