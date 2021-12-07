from aiogram.dispatcher.filters.state import State, StatesGroup


class new_user(StatesGroup):
    telephone = State()
    bosh_menyu = State()