from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import Database as db


def decision():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.insert(InlineKeyboardButton(text="✅ Ha", callback_data="yes"))
    keyboard.insert(InlineKeyboardButton(text="❌ Yo'q", callback_data="no"))
    return keyboard


