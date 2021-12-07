from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def phone():
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.insert(KeyboardButton(text="📞 Register", request_contact=True))
    return keyboard

