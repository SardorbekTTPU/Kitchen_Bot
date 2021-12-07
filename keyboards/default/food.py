from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


food_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
food_keyboard.insert(KeyboardButton(text="🥙 Mavjud"))
food_keyboard.insert(KeyboardButton(text="📝 Yangi"))
food_keyboard.insert(KeyboardButton(text="🔙 Ortga"))


back_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
back_menu.insert(KeyboardButton(text="◀️Ortga"))


zakaz_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
zakaz_menu.insert(KeyboardButton(text="📥 Korzina"))
zakaz_menu.insert(KeyboardButton(text="◀️Ortga"))