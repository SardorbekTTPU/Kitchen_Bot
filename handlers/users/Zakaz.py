from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from keyboards.default.admin_keyboards import taomlar
from keyboards.default.customer_keyboards import buyurtma
from keyboards.default.food import zakaz_menu
from keyboards.inline.taomlar import buyrtma_buttons
from loader import dp, Database as db
from states.user import Buyurtma


@dp.message_handler(state=Buyurtma.address)
async def food_buyurtma(message: Message):
    await message.answer("Qanday taom yo'ki ichimlik buyurtmoqchisiz?", reply_markup=taomlar)
    await Buyurtma.taom.set()


@dp.message_handler(text="Back", state=Buyurtma.taom)
async def orqa_menyu(message: Message):
    await message.answer("Iltimos manzilingizni jo'nating 📍 yo'ki manzilni tanlang", reply_markup=buyurtma())
    await Buyurtma.address.set()


@dp.message_handler(text="🍟 Fast Food", state=Buyurtma.taom)
async def fastfood(message: Message):
    await message.answer("<b> FAST FOODLAR OLAMI</b>", reply_markup=zakaz_menu)
    fastfood = await db.all_fast_food()
    for food in fastfood:
        name = food.get("name")
        price = food.get("price")
        pic = food.get("foto_id")
        await message.answer_photo(pic, caption=f"Nomi: {name}\n"
                                                f"Narxi: {price} so'm", reply_markup=buyrtma_buttons(name))
    await Buyurtma.fast_food.set()


@dp.message_handler(text="◀️Ortga", state=Buyurtma.fast_food)
async def orqaga_taomlar(message: Message):
    await food_buyurtma(message)
    await Buyurtma.taom.set()


@dp.message_handler(text="🍛 Milliy taomlar", state=Buyurtma.taom)
async def milliy_taomlar(message: Message):
    await message.answer("<b> MILLIY TAOMLAR OLAMI</b>", reply_markup=zakaz_menu)
    milliy = await db.milliy_taomlar()
    for ovqat in milliy:
        name = ovqat.get("name")
        price = ovqat.get("price")
        pic = ovqat.get("foto_id")
        await message.answer_photo(pic, caption=f"Nomi: {name}\n"
                                                f"Narxi: {price} so'm", reply_markup=buyrtma_buttons(name))
    await Buyurtma.milliy_taom.set()


@dp.message_handler(text="◀️Ortga", state=Buyurtma.milliy_taom)
async def orqaga_taomlar(message: Message):
    await food_buyurtma(message)
    await Buyurtma.taom.set()


@dp.message_handler(text="🍻 Ichimliklar", state=Buyurtma.taom)
async def ichmliklar(message: Message):
    await message.answer("<b> Ichmliklar OLAMI</b>", reply_markup=zakaz_menu)
    new_drinks = await db.all_drinks()
    for drink in new_drinks:
        name = drink.get("name")
        price = drink.get("price")
        pic = drink.get("foto_id")
        await message.answer_photo(pic, caption=f"Nomi: {name}\n"
                                                f"Narxi: {price} so'm", reply_markup=buyrtma_buttons(name))
    await Buyurtma.drinks.set()


@dp.message_handler(text="◀️Ortga", state=Buyurtma.drinks)
async def orqaga_taomlar(message: Message):
    await food_buyurtma(message)
    await Buyurtma.taom.set()
