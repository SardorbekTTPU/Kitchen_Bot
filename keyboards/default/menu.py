from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍽 Menyu")
        ],
        [
            KeyboardButton(text="📥 Korzina"),
            KeyboardButton(text="🛍 Mening buyurtmalarim"),
        ],
        [
            KeyboardButton(text="☎️ Bog'lanish"),
            KeyboardButton(text="⚙️ Sozlamalar"),
        ]
    ], resize_keyboard=True
)


sozlamalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💼 Profil"),
            KeyboardButton(text="🗑 Akkauntni o'chirish")
        ],
        [
            KeyboardButton(text="🔙 Back")
        ]
    ],resize_keyboard=True
)

profile = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yangilash"),
        ],
        [
            KeyboardButton(text="🔙 Back")
        ]
    ], resize_keyboard= True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 Back")
        ]
    ], resize_keyboard=True
)