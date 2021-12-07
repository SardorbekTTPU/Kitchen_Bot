from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📬 Buyurtmalar"),
            KeyboardButton(text="⏰ Jarayonda")
        ],
        [
            KeyboardButton(text="🍴 Taomlar"),
            KeyboardButton(text="☎️ Aloqa tizimi")
        ]
    ], resize_keyboard=True
)

profile = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yangilash")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ], resize_keyboard=True
)

orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Back")
        ]
    ],resize_keyboard=True
)

# Taomlar knopkalari
taomlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍟 Fast Food"),
            KeyboardButton(text="🍛 Milliy taomlar")
        ],
        [
            KeyboardButton(text="🍻 Ichimliklar")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ], resize_keyboard=True
)