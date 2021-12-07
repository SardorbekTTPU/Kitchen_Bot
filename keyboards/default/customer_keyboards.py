from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import Database as db


def buyurtma():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.insert(KeyboardButton(text="Lokatsiya 📍", request_location=True))
    keyboard.insert(KeyboardButton(text="Mening manzilarim"))
    keyboard.insert(KeyboardButton(text="⬅️Orqaga"))
    return keyboard


async def manzilar(user_id):
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    location = await db.user_data(user_id)
    if location:
        keyboard.insert(KeyboardButton(location.get("location")))
    else:
        pass
    keyboard.insert(KeyboardButton(text="🔙 Orqaga"))
    return keyboard