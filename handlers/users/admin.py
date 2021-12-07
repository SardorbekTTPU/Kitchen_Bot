from aiogram.types import Message, ReplyKeyboardRemove, ContentType, CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.default.admin_keyboards import profile, menu_keyboards, taomlar
from keyboards.inline.taomlar import delete
from states.admin import Admin, Profile, Food
from keyboards.default.food import food_keyboard, back_menu
from loader import dp, Database as db


@dp.message_handler(text="☎️ Aloqa tizimi", state=Admin.menu)
async def aloqa(message: Message):
    admin = await db.admin_data(message.from_user.id)
    name = admin.get("name") or "Kiritilmagan"
    admin_id = admin.get("admin_id") or "Kiritilmagan"
    phone = admin.get("phone") or "Kiritilmagan"
    await message.answer(f"<b> Aloqa tizimi  ID:{admin_id} </b>\n \n"
                         f"Name: {name}\n"
                         f"phone: {phone}", reply_markup=profile)
    await Admin.menu.set()


@dp.message_handler(text="Yangilash", state=Admin.menu)
async def yangilash(message: Message):
    await message.answer("<b>Iltimos ismingizni kiriting</b>", reply_markup=ReplyKeyboardRemove(True))
    await Profile.name.set()


@dp.message_handler(state=Profile.name)
async def ism(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer("<b>Iltimos telefon raqamingizni kiriting</b>")
    await Profile.phone.set()


@dp.message_handler(state=Profile.phone)
async def number(message: Message, state: FSMContext):
    phone = message.text
    await state.update_data(
        {"phone": phone}
    )
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    admin_id = message.from_user.id
    await db.update_profile(name, phone, admin_id)
    await message.answer(f"<b> Aloqa tizimi  ID:{admin_id} </b>\n \n"
                         f"Name: {name}\n"
                         f"phone: {phone}", reply_markup=profile)
    await Admin.menu.set()


@dp.message_handler(text="Back", state=Admin.menu)
async def back(message: Message):
    await message.answer("<b>Salom janob admin, xush kelibsiz!</b>", reply_markup=menu_keyboards)
    await Admin.menu.set()


# Taomlar ro'yxati
@dp.message_handler(text="🍴 Taomlar", state=Admin.menu)
async def taomlar_bolimi(message: Message):
    await message.answer("<b> Taomlar bilan ishlash bo'limi </b>", reply_markup=taomlar)
    await Admin.menu.set()


# ----------------------------------------------- FAST FOOD -------------------------------------------------------
@dp.message_handler(text="🍟 Fast Food", state=Admin.menu)
async def fast_food(message: Message):
    await message.answer("<b>FastFood bo'limi</b>", reply_markup=food_keyboard)
    await Food.fastfood.set()


@dp.message_handler(text="🥙 Mavjud", state=Food.fastfood)
async def mavjud_taomlar(message: Message):
    await message.answer("<b> Mavjud taomlar: </b>")
    foods = await db.all_fast_food()
    for food in foods:
        name = food.get("name")
        pic = food.get("foto_id")
        price = food.get("price")
        food_id = food.get("id")
        await message.answer_photo(pic, caption=f"Nomi: {name}\n"
                                                f"Narxi: {price} so'm", reply_markup=delete(food_id))
    await Food.fastfood.set()


@dp.callback_query_handler(text_contains="delete", state=Food.fastfood)
async def deleting(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    food_id = call.data.split('#')[1]
    await db.delete_food(food_id)
    await call.answer(text="Mahsulot o'chirib tashlandi", cache_time=60, show_alert=True)


@dp.message_handler(text="📝 Yangi", state=Food.fastfood)
async def yangi(message: Message):
    await message.answer("<b>Mahsulot nomini kiriting</b>\n\n"
                         "Masalan: Lavash ", reply_markup=back_menu)
    await Food.fastfood_nomi.set()


@dp.message_handler(state=Food.fastfood_nomi)
async def nomi(message: Message, state: FSMContext):
    name = message.text
    if name == "◀️Ortga":
        await message.answer("<b>FastFood bo'limi</b>", reply_markup=food_keyboard)
        await Food.fastfood.set()
    else:
        await state.update_data(
            {"name": name}
        )
        await message.answer("<b> Mahsulot narxini kiritng </b>\n"
                             "Valyuta: So'm\n"
                             "Masalan: 10000", reply_markup=ReplyKeyboardRemove(True))
        await Food.fastfood_price.set()


@dp.message_handler(state=Food.fastfood_price)
async def narx(message: Message, state: FSMContext):
    try:
        taom_narxi = int(message.text)
        await state.update_data(
                {"price": taom_narxi}
            )
        await message.answer("<b> Mahsulot rasmini kiritng </b>")
        await Food.fastfood_pic.set()
    except ValueError:
        await message.answer("Iltimos faqat rasm kiriting")


@dp.message_handler(state=Food.fastfood_pic, content_types=ContentType.PHOTO)
async def picture(message: Message, state: FSMContext):
    try:
        rasm = message.photo[-1].file_id
        await state.update_data(
                {"rasm": rasm}
            )
        data = await state.get_data()
        name = data.get("name")
        price = data.get("price")
        new_pic = data.get("rasm")
        await db.apply("insert into fastfood(name, foto_id, price) values(%s, %s, %s)", (name, new_pic, price))
        await message.answer("<b> Yangi mahsulot Fast-Food bo'limiga qo'shildi </b>", reply_markup=food_keyboard)
        await Food.fastfood.set()
    except TypeError:
            await message.answer("Iltimos faqat mahsulotni rasmni yuboring")


# ---------------------------------------------------------------------------------------------------------------

# -----------------------------------------------ICHMLIKLAR-------------------------------------------------------


@dp.message_handler(text="🍻 Ichimliklar", state=Admin.menu)
async def ichmlik(message: Message, state: FSMContext):
    await message.answer("<b> Ichmliklar bo'limi</b>", reply_markup=food_keyboard)
    await Food.ichmliklar.set()


@dp.message_handler(text="🥙 Mavjud", state=Food.ichmliklar)
async def mavjud_taomlar(message: Message):
    await message.answer("<b> Mavjud taomlar: </b>")
    drinks = await db.all_drinks()
    for drink in drinks:
        name = drink.get("name")
        pic = drink.get("foto_id")
        price = drink.get("price")
        drink_id = drink.get("id")
        await message.answer_photo(pic, caption=f"Nomi: {name}\n"
                                                f"Narxi: {price} so'm", reply_markup=delete(drink_id))
    await Food.ichmliklar.set()


@dp.callback_query_handler(text_contains="delete", state=Food.ichmliklar)
async def deleting(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    drink_id = call.data.split('#')[1]
    await db.delete_drink(drink_id)
    await call.answer(text="Mahsulot o'chirib tashlandi", cache_time=60, show_alert=True)


@dp.message_handler(text="📝 Yangi", state=Food.ichmliklar)
async def yangi(message: Message):
    await message.answer("<b>Mahsulot nomini kiriting</b>\n\n"
                         "Masalan: Cola ", reply_markup=back_menu)
    await Food.ichmliklar_nomi.set()


@dp.message_handler(state=Food.ichmliklar_nomi)
async def nomi(message: Message, state: FSMContext):
    name = message.text
    if name == "◀️Ortga":
        await message.answer("<b>Ichmliklar bo'limi</b>", reply_markup=food_keyboard)
        await Food.ichmliklar.set()
    else:
        await state.update_data(
            {"name": name}
        )
        await message.answer("<b> Ichmlik narxini kiritng </b>\n"
                             "Valyuta: so'm\n"
                             "Masalan: 10000",reply_markup=ReplyKeyboardRemove(True))
    await Food.ichmliklar_price.set()


@dp.message_handler(state=Food.ichmliklar_price)
async def narx(message: Message, state: FSMContext):
    try:
        ichmlik_narxi = int(message.text)
        await state.update_data(
                {"price": ichmlik_narxi}
            )
        await message.answer("<b> Mahsulot rasmini kiritng </b>")
        await Food.ichmliklar_pic.set()
    except ValueError:
        await message.answer("Iltimos faqat raqam kiriting")


@dp.message_handler(state=Food.ichmliklar_pic, content_types=ContentType.PHOTO)
async def picture(message: Message, state: FSMContext):
    try:
        rasm = message.photo[-1].file_id
        await state.update_data(
                {"rasm": rasm}
            )
        data = await state.get_data()
        name = data.get("name")
        price = data.get("price")
        new_pic = data.get("rasm")
        await db.apply("insert into drinks(name, foto_id, price) values(%s, %s, %s)", (name, new_pic, price))
        await message.answer("<b> Yangi mahsulot Ichmliklar bo'limiga qo'shildi </b>", reply_markup=food_keyboard)
        await Food.ichmliklar.set()
    except TypeError:
        await message.answer("Iltimos faqat rasm kiriting")

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------- MILLIY TAOMLAR -------------------------------------------------------

@dp.message_handler(text="🍛 Milliy taomlar", state=Admin.menu)
async def milliy_taomlar(message: Message):
    await message.answer("<b> Milliy-taomlar bo'limi</b>", reply_markup=food_keyboard)
    await Food.milliy_taom.set()


@dp.message_handler(text="🥙 Mavjud", state=Food.milliy_taom)
async def mavjud_taomlar(message: Message):
    await message.answer("<b> Mavjud taomlar: </b>")
    ovqatlar = await db.milliy_taomlar()
    for ovqat in ovqatlar:
        name = ovqat.get("name")
        pic = ovqat.get("foto_id")
        price = ovqat.get("price")
        taom_id = ovqat.get("id")
        await message.answer_photo(pic, caption=f"Nomi: {name}\n"
                                                f"Narxi: {price} so'm", reply_markup=delete(taom_id))
    await Food.milliy_taom.set()


@dp.callback_query_handler(text_contains="delete", state=Food.milliy_taom)
async def deleting(call: CallbackQuery):
    await call.message.delete()
    taom_id = call.data.split('#')[1]

    await db.delete_milliy(taom_id)
    await call.answer(text="Mahsulot o'chirib tashlandi", cache_time=60, show_alert=True)


@dp.message_handler(text="📝 Yangi", state=Food.milliy_taom)
async def yangi(message: Message):
    await message.answer("<b>Mahsulot nomini kiriting</b>\n\n", reply_markup=back_menu)
    await Food.milliy_taom_nomi.set()


@dp.message_handler(state=Food.milliy_taom_nomi)
async def nomi(message: Message, state: FSMContext):
    name = message.text
    if name == "◀️Ortga":
        await message.answer("<b>Milliy-taomlar bo'limi</b>", reply_markup=food_keyboard)
        await Food.milliy_taom.set()
    else:
        await state.update_data(
            {"name": name}
        )
        await message.answer("<b> Mahsulot narxini kiritng </b>\n"
                             "Valyuta: so'm\n"
                             "Masalan: 10000",reply_markup=ReplyKeyboardRemove(True))
        await Food.milliy_taom_price.set()


@dp.message_handler(state=Food.milliy_taom_price)
async def narx(message: Message, state: FSMContext):
    try:
        milliy_taom_narxi = int(message.text)
        await state.update_data(
                {"price": milliy_taom_narxi}
            )
        await message.answer("<b> Mahsulot rasmini kiritng </b>")
        await Food.milliy_taom_pic.set()
    except ValueError:
        await message.answer("Iltimos faqat raqam kiriting!")


@dp.message_handler(state=Food.milliy_taom_pic, content_types=ContentType.PHOTO)
async def picture(message: Message, state: FSMContext):
    try:
        rasm = message.photo[-1].file_id
        await state.update_data(
                {"rasm": rasm}
            )
        data = await state.get_data()
        name = data.get("name")
        price = data.get("price")
        new_pic = data.get("rasm")
        await db.apply("insert into milliy(name, foto_id, price) values(%s, %s, %s)", (name, new_pic, price))
        await message.answer("<b> Yangi mahsulot Milliy-taom bo'limiga qo'shildi </b>", reply_markup=food_keyboard)
        await Food.milliy_taom.set()
    except TypeError:
            await message.answer("Iltimos faqat mahsulotni rasmini yuboring")


# ----------------------------------------------------------------------------------------------------------------------
@dp.message_handler(text="🔙 Ortga", state="*")
async def back_main_menu(message: Message):
    await message.answer("<b> Taomlar bilan ishlash bo'limi </b>", reply_markup=taomlar)
    await Admin.menu.set()
