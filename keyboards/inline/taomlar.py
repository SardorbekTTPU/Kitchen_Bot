from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import Database as db


def delete(food_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.insert(InlineKeyboardButton(text="❌ O'chirish", callback_data=f"delete#{food_id}"))
    return keyboard


def buyrtma_buttons(name, increase=None):
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.insert(InlineKeyboardButton(text="➖", callback_data="delete"))
    keyboard.insert(InlineKeyboardButton(text=f"{1 if increase is None else increase}", callback_data=f"increment"))
    keyboard.insert(InlineKeyboardButton(text="➕", callback_data="add"))
    keyboard.row(InlineKeyboardButton(text="Korzinkaga qo'shish", callback_data=f"AddBasket#{name}"))
    return keyboard
