from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from geopy.geocoders import Nominatim
from keyboards.default.customer_keyboards import buyurtma, manzilar
from keyboards.default.menu import back, main_menu
from states.registration import new_user
from states.user import Buyurtma
from loader import dp, Database as db


@dp.message_handler(text="☎️ Bog'lanish", state=new_user.bosh_menyu)
async def aloqa(message: Message):
    await message.answer("Mavjud oshpazlar ro'yxati", reply_markup=back)
    admins = await db.all_admins()
    for admin in admins:
        name = admin.get("name")
        admin_id = admin.get("admin_id")
        phone = admin.get("phone")
        username = admin.get("username")
        await message.answer(f"ID : {admin_id}\n"
                             f"name : {name}\n"
                             f"phone : {phone}\n"
                             f"username : @{username}")
    await new_user.bosh_menyu.set()


@dp.message_handler(text="🔙 Back", state=new_user.bosh_menyu)
async def orqaga(message: Message):
    await message.answer("Quyidagi buyruqlardan birini tanlang", reply_markup=main_menu)
    await new_user.bosh_menyu.set()


@dp.message_handler(text="🍽 Menyu", state=new_user.bosh_menyu)
async def menyu(message: Message):
    await message.answer("Iltimos manzilingizni jo'nating 📍 yo'ki manzilni tanlang", reply_markup=buyurtma())
    await Buyurtma.address.set()


@dp.message_handler(content_types='location', state=Buyurtma.address)
async def get_location(message: Message, state: FSMContext):
    with Nominatim(user_agent="mukhammadjonovkhamidullo@gmail.com") as geolocator:
        location = message.location
        latitude = location.latitude
        longitude = location.longitude
        final_location = f"{latitude},{longitude}"
        address = geolocator.geocode(final_location)
        await db.update_location(telegram_id=message.from_user.id, location=str(address))
    await Buyurtma.address.set()


@dp.message_handler(text="⬅️Orqaga", state=Buyurtma.address)
async def qaytish_bosh_menyu(message: Message):
    await orqaga(message)


@dp.message_handler(text="Mening manzilarim", state=Buyurtma.address)
async def manzillar(message: Message):
    await message.answer("Yetkazib berish manzilini tanlang", reply_markup=await manzilar(message.from_user.id))
    await Buyurtma.address.set()


@dp.message_handler(text="🔙 Orqaga", state=Buyurtma.address)
async def orqaga_qaytish(message: Message):
    await menyu(message)

